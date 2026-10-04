"""Audit actual input returns and preserve the single autonomous output, without editing it."""
from pathlib import Path
import hashlib
import json
import re

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
frozen = json.loads((RECORD / "frozen-materials.json").read_text(encoding="utf-8"))
runtime = Path(frozen["runtime_directory"])
material, dest = RECORD / "materials", RECORD / "drafting"


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def inventory(p):
    return {q.relative_to(p).as_posix(): digest(q) for q in sorted(p.rglob("*")) if q.is_file()}


def physical_lines(text):
    return text.split("\n")[:-1] if text.endswith("\n") else text.split("\n")


events = [json.loads(line) for line in (dest / "events.jsonl").read_text(encoding="utf-8").splitlines()]
rows, commands, mismatches, unresolved, outside = {}, [], [], [], []
for event in events:
    item = event.get("item", {})
    if event.get("type") != "item.completed" or item.get("type") != "command_execution":
        continue
    command, output = item["command"].replace("\\\\", "\\"), item.get("aggregated_output", "")
    paths = []
    for value in re.findall(r"[A-Za-z]:[\\/][^'\"\r\n]*?\.(?:md|yaml|txt|pdf|py|json)\b", command):
        p = Path(value).resolve()
        if p.is_file():
            if p.is_relative_to(runtime):
                name = p.relative_to(runtime).as_posix()
                if name not in paths:
                    paths.append(name)
            else:
                outside.append({"id": item["id"], "path": str(p)})
    numbered = [(int(n), line.rstrip("\r")) for n, line in re.findall(r"^\s*(\d+): ?([^\n]*)", output, re.M)]
    matched = 0
    if numbered:
        if len(paths) != 1:
            unresolved.append({"id": item["id"], "paths": paths, "reason": "Cannot uniquely associate numbered return"})
        else:
            name = paths[0]
            source = physical_lines((material / name).read_text(encoding="utf-8"))
            for n, line in numbered:
                if n > len(source) or line != source[n - 1]:
                    mismatches.append({"id": item["id"], "path": name, "line": n})
                else:
                    rows.setdefault(name, {})[n] = line
                    matched += 1
    elif re.search(r"Get-Content|read_text", command, re.I):
        unresolved.append({"id": item["id"], "paths": paths, "reason": "Content read without mapped numbered return"})
    commands.append({"id": item["id"], "command": item["command"], "exit_code": item.get("exit_code"),
                     "paths": paths, "numbered_lines": len(numbered), "verified_lines": matched,
                     "utf8_explicit": bool(re.search(r"-Encoding\s+UTF8|encoding=['\"]utf-8", command, re.I))})
coverage = {}
for name, returned in rows.items():
    source = physical_lines((material / name).read_text(encoding="utf-8"))
    required = {n: line for n, line in enumerate(source, 1) if line.strip()}
    missing = [n for n, line in required.items() if returned.get(n) != line]
    coverage[name] = {"missing_nonblank_lines": missing, "whole_nonblank_text_returned": not missing}
examples = frozen["example_loading"]["file"]
lines = physical_lines((material / examples).read_text(encoding="utf-8"))
cards = {}
for start, line in enumerate(lines, 1):
    match = re.match(r"### (A\d+)\b", line)
    if not match:
        continue
    end = next((i for i in range(start + 1, len(lines) + 1) if lines[i - 1].startswith(("### ", "## "))), len(lines) + 1) - 1
    required = {i: lines[i - 1] for i in range(start, end + 1) if lines[i - 1].strip()}
    if not any(i != start and rows.get(examples, {}).get(i) == t for i, t in required.items()):
        continue
    missing = [i for i, t in required.items() if rows.get(examples, {}).get(i) != t]
    cards[match[1]] = {"source_range": [start, end], "missing_nonblank_lines": missing,
                       "full_real_english_and_analysis_returned": not missing}
common_end = frozen["example_loading"]["common_and_task_index_lines"][1]
common_missing = [i for i in range(1, common_end + 1) if lines[i - 1].strip()
                  and rows.get(examples, {}).get(i) != lines[i - 1]]
required_files = ["skill-candidate/nature-writing/" + name for name in (
    "SKILL.md", "manifest.yaml", "static/core/stance.md", "static/core/workflow.md", "static/core/output-format.md",
    "static/fragments/task/manuscript.md", "static/fragments/section/abstract.md",
    "static/fragments/language/zh-to-en.md", "static/fragments/language/en.md", "static/fragments/journal/generic.md",
    "references/abstract.md")]
required_files.extend("skill-candidate/nature-shared/core/" + name + ".md" for name in
                      ("reader-workflow", "paper-type-taxonomy", "ethics", "terminology-ledger", "scientific-expression"))
required_missing = [name for name in required_files if not coverage.get(name, {}).get("whole_nonblank_text_returned")]
prompt = (dest / "execution-prompt.txt").read_text(encoding="utf-8")
inputs = {}
for name in ("task.md", "scientific-facts.md", "personal-experience.txt", "core-requirements.txt", "abstract-writing-method.txt"):
    path = "inputs/" + name
    assert (material / path).read_text(encoding="utf-8") in prompt
    inputs[path] = {"sha256": digest(material / path), "whole_original_text_in_initial_prompt": True,
                    "model_read_coverage": coverage.get(path)}
meta = json.loads((dest / "run-meta.json").read_text(encoding="utf-8"))
run = json.loads((dest / "frozen-run.json").read_text(encoding="utf-8"))
raw = (dest / "first-output.md").read_bytes()
assert digest(dest / "first-output.md") == meta["first_output_sha256"]
final_message = [e["item"]["text"] for e in events if e.get("type") == "item.completed"
                 and e.get("item", {}).get("type") == "agent_message"][-1]
assert raw.decode("utf-8").rstrip("\r\n") == final_message.rstrip("\r\n")
assert digest(RECORD / "execute_once.py") == run["runner_sha256"]
assert inventory(material) == inventory(runtime) == frozen["materials_files_sha256"]
changed = [name for name, sha in frozen["protected_project_files_sha256"].items() if digest(ROOT / name) != sha]
installed_changed = [x["directory"] for x in frozen["installed_skills"] if inventory(Path(x["directory"])) != x["files"]]
assert not changed and not installed_changed and not mismatches and not unresolved and not outside
assert not required_missing and not common_missing and cards.get("A06", {}).get("full_real_english_and_analysis_returned")
assert all(card["full_real_english_and_analysis_returned"] for card in cards.values())
report = {"run_kind": frozen["run_kind"], "candidate_commit": frozen["candidate_commit"],
          "model_requested": frozen["model"], "reasoning_effort_requested": frozen["reasoning_effort"],
          "single_invocation": True, "new_paper_transfer_evidence": False,
          "first_output_sha256": digest(dest / "first-output.md"), "raw_output_matches_final_logged_message": True,
          "raw_output_unedited": True, "inputs": inputs, "commands": commands, "actual_content_coverage": coverage,
          "actual_example_cards": cards, "common_missing_nonblank_lines": common_missing,
          "required_missing_files": required_missing, "source_return_mismatches": mismatches,
          "unresolved_content_reads": unresolved, "outside_materials_explicit_reads": outside,
          "changed_protected_files": changed, "changed_installed_skills": installed_changed,
          "raw_record_sha256": {name: digest(dest / name) for name in ("events.jsonl", "stderr.txt", "execution-command.json", "execution-prompt.txt")},
          "limit": "Actual returned contents and explicit paths audited; not an effect verdict or OS-level isolation claim."}
target = RECORD / "verification.json"
assert not target.exists()
target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"first_output_preserved": True, "complete_cards": list(cards),
                  "verified_lines": sum(c["verified_lines"] for c in commands), "protected_files_unchanged": True}))
