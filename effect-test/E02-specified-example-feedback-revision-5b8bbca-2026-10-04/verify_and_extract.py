"""Verify the one feedback output and preserve exact English/Chinese/rationale sections."""
from pathlib import Path
import hashlib
import json
import re

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
DEST = RECORD / "drafting"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(path):
    return {p.relative_to(path).as_posix(): digest(p)
            for p in sorted(path.rglob("*")) if p.is_file()}


assert not (RECORD / "verification.json").exists()
frozen = json.loads((RECORD / "frozen-materials.json").read_text(encoding="utf-8"))
preflight = json.loads((RECORD / "preflight.json").read_text(encoding="utf-8"))
meta = json.loads((DEST / "run-meta.json").read_text(encoding="utf-8"))
audit = json.loads((DEST / "loading-audit.json").read_text(encoding="utf-8"))
events = [json.loads(line) for line in (DEST / "events.jsonl").read_text(encoding="utf-8").splitlines()]
messages = [e["item"]["text"] for e in events if e.get("type") == "item.completed"
            and e.get("item", {}).get("type") == "agent_message"]
raw = (DEST / "first-output.md").read_bytes()
final = messages[-1].encode("utf-8")
changes = [name for name, expected in frozen["protected_project_files_sha256"].items()
           if not (ROOT / name).is_file() or digest(ROOT / name) != expected]
installed_changes = [item["directory"] for item in frozen["installed_skills"]
                     if inventory(Path(item["directory"])) != item["files"]]
input_changes = [name for name, item in frozen["reused_sources"].items()
                 if digest(ROOT / item["path"]) != item["sha256"]
                 or digest(RECORD / "materials" / name) != item["sha256"]]
coverage = []
for label in ("A06", "A07"):
    name = f"source-examples/{label}-full-text.txt"
    lines = (RECORD / "materials" / name).read_text(encoding="utf-8").split("\n")
    stop = next(i + 1 for i, line in enumerate(lines) if line == "REFERENCES") - 1
    seen = set()
    for entry in audit["commands"]:
        if name in entry["paths"] and entry["verified_lines_match_frozen_text"]:
            for start, end in entry["verified_source_line_ranges"]:
                seen.update(range(start, end + 1))
    coverage.append({"id": label, "scientific_text_range": [1, stop],
                     "unreturned_nonblank_lines": [i for i in range(1, stop + 1) if lines[i - 1].strip() and i not in seen]})
result = {
    "run_kind": "人工反馈修订", "candidate_commit": frozen["candidate_commit"],
    "model_requested": frozen["model"], "reasoning_effort_requested": frozen["reasoning_effort"],
    "thread_ids": [e["thread_id"] for e in events if e.get("type") == "thread.started"],
    "turn_started_count": sum(e.get("type") == "turn.started" for e in events),
    "turn_completed_count": sum(e.get("type") == "turn.completed" for e in events),
    "exit_code": meta["exit_code"], "first_output_matches_final_event": raw in (final, final + b"\n"),
    "input_changes": input_changes, "protected_project_changes": changes,
    "installed_skill_changes": installed_changes,
    "runtime_unchanged": inventory(Path(frozen["runtime_directory"])) == frozen["materials_files_sha256"],
    "scientific_source_coverage": coverage,
    "text_mismatches": audit["text_mismatches"], "unmapped_numbered_returns": audit["unmapped_numbered_returns"],
    "actual_complete_example_cards": [x["id"] for x in audit["examples"]["cards"] if x["complete_nonblank_card_returned"]],
    "raw_records_sha256": {name: digest(DEST / name) for name in ("first-output.md", "events.jsonl", "stderr.txt", "execution-command.json", "execution-prompt.txt", "run-meta.json")},
    "runner_hash_matches_preflight": digest(RECORD / "execute_once.py") == preflight["runner_sha256"],
    "autonomous_pass": False, "transfer_pass": False,
    "evidence_limit": "Unchanged inputs and source text returns can be verified; no OS-level isolation, independent backend resolution or autonomous-pass inference claimed.",
}
assert meta["exit_code"] == 0 and result["turn_started_count"] == 1 and result["turn_completed_count"] == 1
assert result["first_output_matches_final_event"] and result["runtime_unchanged"] and result["runner_hash_matches_preflight"]
assert not changes and not installed_changes and not input_changes
assert not result["text_mismatches"] and not result["unmapped_numbered_returns"]
assert all(not x["unreturned_nonblank_lines"] for x in coverage)
text = raw.decode("utf-8")
sections = []
for title, name in (("English abstract", "abstract.en.txt"), ("中文译文", "abstract.zh.txt"), ("修改依据", "change-rationale.txt")):
    value = text.split("**" + title + "**\n\n", 1)[1]
    if title != "修改依据":
        value = value.split("\n\n**", 1)[0]
    value = value.rstrip("\n") + "\n"
    section = value.encode("utf-8")
    assert section.rstrip(b"\n") in raw
    target = RECORD / name
    assert not target.exists()
    target.write_bytes(section)
    sections.append({"file": name, "sha256": digest(target), "exact_output_substring_except_terminal_newline": True})
result["sections"] = sections
(RECORD / "verification.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"exit_code": meta["exit_code"], "complete_source_texts": [x["id"] for x in coverage],
                  "original_files_changed": changes, "sections_retained": [x["file"] for x in sections]}))
