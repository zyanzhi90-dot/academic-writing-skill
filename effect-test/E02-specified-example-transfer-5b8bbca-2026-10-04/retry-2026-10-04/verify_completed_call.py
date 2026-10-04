"""Check first-output retention and input isolation after the authorized call retry."""
from pathlib import Path
import hashlib
import json
import subprocess

DEST = Path(__file__).resolve().parent
RECORD = DEST.parent
ROOT = RECORD.parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(path):
    return {p.relative_to(path).as_posix(): digest(p)
            for p in sorted(path.rglob("*")) if p.is_file()}


assert not (DEST / "verification.json").exists()
frozen = json.loads((RECORD / "frozen-materials.json").read_text(encoding="utf-8"))
preflight = json.loads((DEST / "preflight.json").read_text(encoding="utf-8"))
meta = json.loads((DEST / "run-meta.json").read_text(encoding="utf-8"))
audit = json.loads((DEST / "loading-audit.json").read_text(encoding="utf-8"))
events = [json.loads(line) for line in (DEST / "events.jsonl").read_text(encoding="utf-8").splitlines()]
messages = [e["item"] for e in events if e.get("type") == "item.completed"
            and e.get("item", {}).get("type") == "agent_message"]
raw = (DEST / "first-output.md").read_bytes()
final = messages[-1]["text"].encode("utf-8")
old_record_changes = [name for name, expected in preflight["old_raw_record_sha256"].items()
                      if digest(RECORD / "drafting" / name) != expected]
protected_changes = [name for name, expected in frozen["protected_project_files_sha256"].items()
                     if not (ROOT / name).is_file() or digest(ROOT / name) != expected]
installed_changes = [item["directory"] for item in frozen["installed_skills"]
                     if inventory(Path(item["directory"])) != item["files"]]
example_coverage = []
for label in ("A06", "A07"):
    name = f"source-examples/{label}-full-text.txt"
    lines = (RECORD / "materials" / name).read_text(encoding="utf-8").split("\n")
    stop = next(i + 1 for i, line in enumerate(lines) if line == "REFERENCES") - 1
    seen = set()
    for entry in audit["commands"]:
        if name in entry["paths"] and entry["verified_lines_match_frozen_text"]:
            for start, end in entry["verified_source_line_ranges"]:
                seen.update(range(start, end + 1))
    missing = [i for i in range(1, stop + 1) if lines[i - 1].strip() and i not in seen]
    example_coverage.append({"id": label, "required_scientific_range": [1, stop],
                             "unreturned_nonblank_lines": missing})
old_cmd = json.loads((RECORD / "drafting/execution-command.json").read_text(encoding="utf-8"))
new_cmd = json.loads((DEST / "execution-command.json").read_text(encoding="utf-8"))
differences = [i for i, (a, b) in enumerate(zip(old_cmd, new_cmd)) if a != b]
result = {
    "record_kind": "指定范例迁移路线验证：失败模型调用的授权重试",
    "candidate_commit": frozen["candidate_commit"],
    "model_requested": frozen["model"], "reasoning_effort_requested": frozen["reasoning_effort"],
    "prior_failed_model_invocations": 1, "authorized_retry_model_invocations": 1,
    "retry_thread_ids": [e["thread_id"] for e in events if e.get("type") == "thread.started"],
    "retry_turn_started_count": sum(e.get("type") == "turn.started" for e in events),
    "retry_turn_completed_count": sum(e.get("type") == "turn.completed" for e in events),
    "retry_exit_code": meta["exit_code"],
    "first_output_matches_final_event": raw in (final, final + b"\n"),
    "first_output_retained_sha256": hashlib.sha256(raw).hexdigest(),
    "original_prompt_byte_identical": (DEST / "execution-prompt.txt").read_bytes() == (RECORD / "drafting/execution-prompt.txt").read_bytes(),
    "only_changed_command_position": differences,
    "only_output_path_changed": differences == [old_cmd.index("-o") + 1],
    "old_raw_record_changes": old_record_changes,
    "materials_unchanged": inventory(RECORD / "materials") == frozen["materials_files_sha256"],
    "runtime_unchanged": inventory(Path(frozen["runtime_directory"])) == frozen["materials_files_sha256"],
    "protected_project_changes": protected_changes, "installed_skill_changes": installed_changes,
    "loading_text_mismatches": audit["text_mismatches"],
    "unmapped_numbered_returns": audit["unmapped_numbered_returns"],
    "source_text_coverage": example_coverage,
    "complete_example_cards_returned": [x["id"] for x in audit["examples"]["cards"] if x["complete_nonblank_card_returned"]],
    "autonomous_pass": False, "transfer_pass": False,
    "feedback_to_writer": False, "alternate_output_selection": False,
    "retry_raw_record_sha256": {name: digest(DEST / name) for name in ("first-output.md", "events.jsonl", "stderr.txt", "execution-command.json", "execution-prompt.txt", "run-meta.json")},
    "evidence_limit": "Actual command returns and unchanged bytes; no OS-level isolation or independent backend model resolution claimed. Prose is evaluated separately.",
}
(DEST / "verification.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
assert meta["exit_code"] == 0 and result["retry_turn_completed_count"] == 1
assert result["first_output_matches_final_event"] and result["original_prompt_byte_identical"]
assert result["only_output_path_changed"] and result["materials_unchanged"] and result["runtime_unchanged"]
assert not old_record_changes and not protected_changes and not installed_changes
assert not audit["text_mismatches"] and not audit["unmapped_numbered_returns"]
assert all(not x["unreturned_nonblank_lines"] for x in example_coverage)
print(json.dumps({"exit_code": meta["exit_code"], "first_output_matches_final_event": result["first_output_matches_final_event"],
                  "old_record_changes": old_record_changes, "complete_source_texts": [x["id"] for x in example_coverage]}))
