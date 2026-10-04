"""Verify existing single-invocation records without invoking or editing the writer."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import subprocess

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(path):
    return {p.relative_to(path).as_posix(): digest(p)
            for p in sorted(path.rglob("*")) if p.is_file()}


def save(name, data):
    target = RECORD / name
    if target.exists():
        raise SystemExit(f"Refusing to overwrite {name}")
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


frozen = json.loads((RECORD / "frozen-materials.json").read_text(encoding="utf-8"))
run = json.loads((RECORD / "drafting/frozen-run.json").read_text(encoding="utf-8"))
audit = json.loads((RECORD / "drafting/loading-audit.json").read_text(encoding="utf-8"))
runtime = Path(frozen["runtime_directory"])
materials = RECORD / "materials"
events = [json.loads(line) for line in (RECORD / "drafting/events.jsonl").read_text(encoding="utf-8").splitlines()]

candidate_mismatches = []
for name, expected in frozen["original_candidate_files_sha256"].items():
    raw = subprocess.check_output(["git", "show", frozen["candidate_commit"] + ":" + name], cwd=ROOT)
    if hashlib.sha256(raw).hexdigest() != expected or digest(materials / name) != expected:
        candidate_mismatches.append(name)
protected_changes = [name for name, expected in frozen["protected_project_files_sha256"].items()
                     if not (ROOT / name).is_file() or digest(ROOT / name) != expected]
installed_changes = [item["directory"] for item in frozen["installed_skills"]
                     if inventory(Path(item["directory"])) != item["files"]]
input_mismatches = [name for name, item in frozen["inputs_sources"].items()
                    if digest(ROOT / item["source"]) != item["sha256"]
                    or digest(materials / "inputs" / name) != item["sha256"]]
example_checks = []
for item in frozen["source_examples"]:
    label = item["id"]
    example_checks.append({"id": label,
                           "original_pdf_matches": digest(ROOT / item["source"]) == item["pdf_sha256"],
                           "record_pdf_matches": digest(RECORD / "source-examples" / (label + ".pdf")) == item["pdf_sha256"],
                           "record_text_matches": digest(RECORD / "source-examples" / (label + "-full-text.txt")) == item["full_text_sha256"]})

coverage = []
for label in ("A06", "A07"):
    name = f"source-examples/{label}-full-text.txt"
    lines = (materials / name).read_text(encoding="utf-8").split("\n")
    stop = next(i + 1 for i, line in enumerate(lines) if line == "REFERENCES") - 1
    seen = set()
    ids = []
    for command in audit["commands"]:
        if name in command["paths"] and command["verified_lines_match_frozen_text"]:
            ids.append(command["command_id"])
            for start, end in command["verified_source_line_ranges"]:
                seen.update(range(start, end + 1))
    missing = [i for i in range(1, stop + 1) if lines[i - 1].strip() and i not in seen]
    coverage.append({"id": label, "scientific_text_through_conclusion": [1, stop],
                     "command_ids": ids, "unreturned_nonblank_lines": missing,
                     "complete_scientific_text_returned": not missing})

messages = [event for event in events if event.get("type") == "item.completed"
            and event.get("item", {}).get("type") == "agent_message"]
save("drafting/partial-agent-messages.json", {"status": "Progress messages only; no complete abstract, translation or final rationale",
                                             "events": messages})
errors = [event for event in events if event.get("type") == "error"
          or event.get("item", {}).get("type") == "error"]
raw_hashes = {name: digest(RECORD / "drafting" / name)
              for name in ("events.jsonl", "stderr.txt", "execution-command.json", "execution-prompt.txt", "frozen-run.json")}
result = {
    "observed_at_utc": datetime.now(timezone.utc).isoformat(),
    "record_kind": "指定范例迁移路线验证",
    "candidate_commit": frozen["candidate_commit"],
    "preparation_commit": frozen["preparation_commit"],
    "model_requested": run["model"], "reasoning_effort_requested": run["reasoning_effort"],
    "resolved_backend_model_not_independently_reported": True,
    "thread_started_count": sum(e.get("type") == "thread.started" for e in events),
    "turn_started_count": sum(e.get("type") == "turn.started" for e in events),
    "turn_completed_count": sum(e.get("type") == "turn.completed" for e in events),
    "turn_failed_count": sum(e.get("type") == "turn.failed" for e in events),
    "original_process_exit_code": None,
    "original_exit_code_reason": "No run-meta.json or terminal turn event retained; exit code cannot be reconstructed",
    "complete_first_output_exists": (RECORD / "drafting/first-output.md").exists(),
    "original_run_meta_exists": (RECORD / "drafting/run-meta.json").exists(),
    "status": "Incomplete single invocation; transport errors precede missing final output",
    "error_events": errors,
    "candidate_files_checked": len(frozen["original_candidate_files_sha256"]),
    "candidate_mismatches": candidate_mismatches,
    "materials_inventory_matches": inventory(materials) == frozen["materials_files_sha256"],
    "runtime_inventory_matches": runtime.is_dir() and inventory(runtime) == frozen["materials_files_sha256"],
    "input_mismatches": input_mismatches,
    "example_analysis_matches": digest(RECORD / "example-analysis.md") == frozen["example_analysis_sha256"],
    "examples": example_checks, "actual_read_coverage": coverage,
    "runner_matches_frozen_hash": digest(RECORD / "execute_once.py") == run["runner_sha256"],
    "helper_matches_frozen_hash": digest(ROOT / "effect-test/P17-abstract-first-drafting-2026-10-02/execute_once.py") == run["collector_helper_sha256"],
    "protected_project_files_checked": len(frozen["protected_project_files_sha256"]),
    "protected_project_changes": protected_changes, "installed_skill_changes": installed_changes,
    "raw_record_sha256": raw_hashes,
    "new_writer_invocations_during_record_recovery": 0,
    "feedback_added_to_writer": False, "old_draft_used": False,
    "autonomous_pass": False, "transfer_pass": False,
    "prose_quality_verdict": "Not assessable: no complete first English abstract or translation",
    "evidence_limit": "Material return and unchanged bytes can be checked. Progress self-reports do not establish final prose, phrase-level adaptation, comprehension, backend resolution or OS-level isolation."
}
save("verification.json", result)
assert not candidate_mismatches and not protected_changes and not installed_changes and not input_mismatches
assert result["materials_inventory_matches"] and result["runtime_inventory_matches"]
assert all(x["complete_scientific_text_returned"] for x in coverage)
assert result["thread_started_count"] == 1 and result["turn_started_count"] == 1
assert not result["complete_first_output_exists"] and result["turn_completed_count"] == 0
assert not audit["text_mismatches"] and not audit["unmapped_numbered_returns"]
print(json.dumps({"status": result["status"], "candidate_files": result["candidate_files_checked"],
                  "protected_project_files": result["protected_project_files_checked"],
                  "source_texts_read_through_conclusion": [x["id"] for x in coverage],
                  "new_invocations": 0}, ensure_ascii=True))
