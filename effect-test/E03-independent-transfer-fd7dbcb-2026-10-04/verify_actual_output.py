"""Preserve the actual first output and audit returned text; do not score it as E03."""
from pathlib import Path
import hashlib
import json
import re

RECORD = Path(__file__).resolve().parent
frozen = json.loads((RECORD / "frozen-materials.json").read_text(encoding="utf-8"))
verification = json.loads((RECORD / "verification.json").read_text(encoding="utf-8"))
loaded = json.loads((RECORD / "drafting/loaded-files.json").read_text(encoding="utf-8"))
assert verification["first_output_matches_terminal_message_except_final_newline"]
assert verification["outside_materials_explicit_reads"] == []
assert verification["unresolved_read_commands"] == []
runtime = Path(frozen["runtime_directory"])
events = [json.loads(line) for line in (RECORD / "drafting/events.jsonl").read_text(encoding="utf-8").splitlines()]
commands = {event["item"]["id"]: event["item"] for event in events
            if event.get("type") == "item.completed" and event.get("item", {}).get("type") == "command_execution"}
by_command = {}
for entry in loaded["loaded_or_searched_files"]:
    for command_id in entry["command_ids"]:
        by_command.setdefault(command_id, []).append(entry["path"])
rows = {}
for command_id, names in by_command.items():
    active = names[0] if len(names) == 1 else None
    headers = {str(runtime / name).replace("\\", "/"): name for name in names}
    for line in commands[command_id].get("aggregated_output", "").splitlines():
        header = line.replace("\\", "/")
        if header in headers:
            active = headers[header]
        match = re.match(r"^(\d+): (.*)$", line)
        if match and active:
            rows.setdefault(active, {})[int(match.group(1))] = match.group(2)
coverage = {}
for entry in loaded["loaded_or_searched_files"]:
    name = entry["path"]
    text = (RECORD / "materials" / name).read_text(encoding="utf-8")
    required = {i + 1: line for i, line in enumerate(text.splitlines()) if line.strip()}
    missing = [n for n, line in required.items() if rows.get(name, {}).get(n) != line]
    coverage[name] = {"command_ids": entry["command_ids"], "nonempty_source_lines": len(required),
                      "mismatched_or_missing_line_numbers": missing,
                      "whole_nonempty_contents_returned_verbatim": not missing}
for name in ["inputs/task.md", "inputs/scientific-facts.md", "inputs/personal-experience.txt",
             "inputs/core-requirements.txt", "skill-candidate/nature-writing/SKILL.md",
             "skill-candidate/nature-writing/manifest.yaml",
             "skill-candidate/nature-writing/static/fragments/section/abstract.md",
             "skill-candidate/nature-writing/references/abstract.md",
             "skill-candidate/nature-shared/core/scientific-expression.md"]:
    assert coverage[name]["whole_nonempty_contents_returned_verbatim"], name
examples = "skill-candidate/nature-shared/core/robotics-writing-examples.md"
text = (RECORD / "materials" / examples).read_text(encoding="utf-8")
cards = {}
for key in ("A04", "A05", "A06", "A07"):
    match = re.search(r"^### " + key + r".*?(?=^### |^## |\Z)", text, re.M | re.S)
    start = text[:match.start()].count("\n") + 1
    required = {start + i: line for i, line in enumerate(match.group().splitlines()) if line.strip()}
    assert all(rows[examples].get(n) == line for n, line in required.items()), key
    cards[key] = {"full_real_english_and_analysis_returned_verbatim": True,
                  "line_range": [start, start + len(match.group().splitlines()) - 1]}
raw = (RECORD / "drafting/first-output.md").read_bytes()
assert hashlib.sha256(raw).hexdigest() == verification["first_output_sha256"]
start = raw.index(b"This paper proposes")
end = raw.index(b"\n\n", start)
zh_header = "中文翻译：\n\n".encode("utf-8")
zh_start = raw.index(zh_header) + len(zh_header)
zh_end = raw.index(b"\n\n", zh_start)
for name, data in (("actual-invocation.en.txt", raw[start:end]), ("actual-invocation.zh.txt", raw[zh_start:zh_end])):
    assert not (RECORD / name).exists(), "Do not overwrite original slices"
    (RECORD / name).write_bytes(data)
run = json.loads((RECORD / "drafting/frozen-run.json").read_text(encoding="utf-8"))
assert hashlib.sha256((RECORD / "execute_once.py").read_bytes()).hexdigest() == run["runner_sha256"]
assert (RECORD / "coordinator/actually-executed-runner.py").read_bytes() == (RECORD / "execute_once.py").read_bytes()
audit = {"declared_run_kind": "E03-independent-transfer", "actual_writer_case": "E02",
         "eligible_as_E03_transfer": False, "single_cli_invocation": True,
         "no_feedback_rerun_selection_or_output_edit": True,
         "first_output_sha256": verification["first_output_sha256"],
         "english_byte_offsets": [start, end], "chinese_byte_offsets": [zh_start, zh_end],
         "derived_text_is_exact_byte_slice_without_added_newline": True,
         "english_word_count": len(raw[start:end].decode("utf-8").split()),
         "english_sentences": re.split(r"(?<=\.)\s+", raw[start:end].decode("utf-8")),
         "actual_returned_content_coverage": coverage, "actual_example_cards": cards,
         "core_requirements_whole_line_returned": True,
         "outside_materials_explicit_reads": [], "remaining_unresolved_commands": [],
         "effect_verdict": "Execution invalid for E03: wrong-case facts. No E03 prose judgment.",
         "input_identity_evidence": "input-identity-audit.json"}
(RECORD / "first-output-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"raw_output_preserved": True, "english_words": audit["english_word_count"],
                  "actual_input_contents_complete": True, "eligible_as_E03": False}))
