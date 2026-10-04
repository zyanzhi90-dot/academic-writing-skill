"""Audit the single revision's actual returns and preservation, without prose edits."""
from pathlib import Path
import hashlib
import json
import re

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
frozen = json.loads((RECORD / "frozen-materials.json").read_text(encoding="utf-8"))
runtime = Path(frozen["runtime_directory"])
material = RECORD / "materials"
dest = RECORD / "drafting"


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def inventory(p):
    return {q.relative_to(p).as_posix(): digest(q) for q in sorted(p.rglob("*")) if q.is_file()}


def physical_lines(value):
    return value.split("\n")[:-1] if value.endswith("\n") else value.split("\n")


events = [json.loads(line) for line in (dest / "events.jsonl").read_text(encoding="utf-8").splitlines()]
rows, commands, mismatches, unresolved, outside = {}, [], [], [], []
for event in events:
    item = event.get("item", {})
    if event.get("type") != "item.completed" or item.get("type") != "command_execution":
        continue
    command = item["command"].replace("\\\\", "\\")
    output = item.get("aggregated_output", "")
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
            unresolved.append({"id": item["id"], "paths": paths, "reason": "Numbered return is not associated with exactly one explicit input file"})
        else:
            name = paths[0]
            expected = physical_lines((material / name).read_text(encoding="utf-8"))
            for number, line in numbered:
                if number > len(expected) or line != expected[number - 1]:
                    mismatches.append({"id": item["id"], "path": name, "line": number})
                else:
                    rows.setdefault(name, {})[number] = line
                    matched += 1
    elif re.search(r"Get-Content|read_text", command, re.I):
        unresolved.append({"id": item["id"], "paths": paths, "reason": "Content read without auditable numbered return"})
    commands.append({"id": item["id"], "command": item["command"], "exit_code": item.get("exit_code"),
                     "paths": paths, "returned_numbered_lines": len(numbered), "verified_lines": matched,
                     "utf8_explicit": bool(re.search(r"-Encoding\s+UTF8|encoding=['\"]utf-8", command, re.I))})

coverage = {}
for name, returned in rows.items():
    expected = physical_lines((material / name).read_text(encoding="utf-8"))
    required = {n: line for n, line in enumerate(expected, 1) if line.strip()}
    missing = [n for n, line in required.items() if returned.get(n) != line]
    coverage[name] = {"nonblank_lines": len(required), "missing_nonblank_lines": missing,
                      "whole_nonblank_text_returned": not missing}
examples = "skill-candidate/nature-shared/core/robotics-writing-examples.md"
example_lines = physical_lines((material / examples).read_text(encoding="utf-8"))
cards = {}
for card in ("A06", "A07", "A08"):
    start = next(i for i, line in enumerate(example_lines, 1) if line.startswith("### " + card))
    end = next((i for i in range(start + 1, len(example_lines) + 1)
                if example_lines[i - 1].startswith(("### ", "## "))), len(example_lines) + 1) - 1
    needed = {i: example_lines[i - 1] for i in range(start, end + 1) if example_lines[i - 1].strip()}
    missing = [i for i, line in needed.items() if rows.get(examples, {}).get(i) != line]
    cards[card] = {"source_range": [start, end], "missing_nonblank_lines": missing,
                   "full_real_english_and_analysis_returned": not missing}
common_end = next(i for i, line in enumerate(example_lines, 1) if line == "## 摘要") - 1
common_missing = [i for i in range(1, common_end + 1) if example_lines[i - 1].strip()
                  and rows.get(examples, {}).get(i) != example_lines[i - 1]]
prompt = (dest / "execution-prompt.txt").read_text(encoding="utf-8")
inputs = {}
for name in ("task.md", "scientific-facts.md", "current-draft.md", "personal-experience.txt", "core-requirements.txt"):
    path = "inputs/" + name
    raw = (material / path).read_text(encoding="utf-8")
    assert raw in prompt, path
    inputs[path] = {"sha256": digest(material / path), "original_text_verbatim_in_initial_prompt": True,
                    "returned_read": coverage.get(path)}
meta = json.loads((dest / "run-meta.json").read_text(encoding="utf-8"))
preflight = json.loads((RECORD / "preflight.json").read_text(encoding="utf-8"))
raw = (dest / "first-output.md").read_bytes()
assert digest(dest / "first-output.md") == meta["first_output_sha256"]
final_message = [e["item"]["text"] for e in events if e.get("type") == "item.completed"
                 and e.get("item", {}).get("type") == "agent_message"][-1]
assert raw.decode("utf-8").rstrip("\r\n") == final_message.rstrip("\r\n")
assert digest(RECORD / "execute_once.py") == preflight["runner_sha256"]
assert inventory(material) == inventory(runtime) == frozen["materials_files_sha256"]
changed = [name for name, sha in frozen["protected_project_files_sha256"].items() if digest(ROOT / name) != sha]
installed_changed = [x["directory"] for x in frozen["installed_skills"] if inventory(Path(x["directory"])) != x["files"]]
assert not changed and not installed_changed and not mismatches and not unresolved and not outside
assert all(card["full_real_english_and_analysis_returned"] for card in cards.values())
assert not common_missing
result = {"run_kind": "人工反馈修订", "candidate_commit": frozen["candidate_commit"],
          "model_requested": frozen["model"], "reasoning_effort_requested": frozen["reasoning_effort"],
          "single_revision_invocation": True, "not_autonomous_retest": True,
          "autonomous_pass": False, "transfer_pass": False, "output_sha256": digest(dest / "first-output.md"),
          "output_matches_final_logged_message": True, "raw_output_unedited": True,
          "inputs": inputs, "commands": commands, "actual_content_coverage": coverage,
          "example_cards": cards, "common_missing_nonblank_lines": common_missing,
          "source_return_mismatches": mismatches, "unresolved_content_reads": unresolved,
          "outside_materials_explicit_reads": outside, "changed_protected_files": changed,
          "changed_installed_skills": installed_changed,
          "raw_record_sha256": {name: digest(dest / name) for name in ("events.jsonl", "stderr.txt", "execution-command.json", "execution-prompt.txt")},
          "limit": "Actual returned text and explicit file reads audited; not a quality verdict or OS-level isolation claim."}
target = RECORD / "verification.json"
assert not target.exists()
target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"single_human_revision": True, "actual_cards_complete": list(cards),
                  "protected_files_unchanged": True, "verified_lines": sum(c["verified_lines"] for c in commands)}))
