"""Retry only the failed model call with unchanged validated inputs; keep prior records."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import time
from datetime import datetime, timezone

DEST = Path(__file__).resolve().parent
RECORD = DEST.parent
ROOT = RECORD.parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(path):
    return {p.relative_to(path).as_posix(): digest(p)
            for p in sorted(path.rglob("*")) if p.is_file()}


def save(name, value):
    path = DEST / name
    if path.exists():
        raise SystemExit(f"Refusing to overwrite {name}")
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if (DEST / "preflight.json").exists():
    raise SystemExit("Refusing an additional retry invocation")
frozen = json.loads((RECORD / "frozen-materials.json").read_text(encoding="utf-8"))
previous = json.loads((RECORD / "verification.json").read_text(encoding="utf-8"))
old_cmd = json.loads((RECORD / "drafting/execution-command.json").read_text(encoding="utf-8"))
runtime = Path(frozen["runtime_directory"])
assert inventory(runtime) == frozen["materials_files_sha256"]
assert inventory(RECORD / "materials") == frozen["materials_files_sha256"]
assert not (RECORD / "drafting/first-output.md").exists()
for name, expected in previous["raw_record_sha256"].items():
    assert digest(RECORD / "drafting" / name) == expected
prompt = (RECORD / "drafting/execution-prompt.txt").read_text(encoding="utf-8")
assert old_cmd[-1] == prompt
cmd = old_cmd.copy()
output_index = cmd.index("-o") + 1
cmd[output_index] = str(DEST / "first-output.md")
assert all(a == b for i, (a, b) in enumerate(zip(old_cmd, cmd)) if i != output_index)
assert digest(Path(cmd[0])) == json.loads((RECORD / "drafting/frozen-run.json").read_text(encoding="utf-8"))["cli_sha256"]
save("preflight.json", {
    "authorized_by": "user-continuation-request.txt",
    "observed_at_utc": datetime.now(timezone.utc).isoformat(),
    "project_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT).decode().strip(),
    "candidate_commit": frozen["candidate_commit"],
    "model_requested": frozen["model"], "reasoning_effort_requested": frozen["reasoning_effort"],
    "run_kind": "指定范例迁移路线验证：失败模型调用的授权重试",
    "prior_model_invocations": 1, "authorized_retry_invocations": 1,
    "session_continuity": "Original CLI was ephemeral; no saved rollout found for original thread. Retry starts a fresh context with the identical prompt and inputs.",
    "frozen_materials_reused_unchanged": True, "runtime_reused_unchanged": True,
    "new_example_analysis_or_scientific_facts": False, "feedback_to_writer": False,
    "only_command_argument_changed": "-o output path",
    "old_raw_record_sha256": previous["raw_record_sha256"],
    "inputs_sha256": frozen["materials_files_sha256"],
    "runner_sha256": digest(Path(__file__)),
    "prompt_sha256": digest(RECORD / "drafting/execution-prompt.txt"),
    "user_continuation_request_sha256": digest(DEST / "user-continuation-request.txt"),
    "autonomous_pass": False, "transfer_pass": False,
})
save("execution-command.json", cmd)
(DEST / "execution-prompt.txt").write_bytes((RECORD / "drafting/execution-prompt.txt").read_bytes())
start = time.time()
env = os.environ.copy()
env["PYTHONUTF8"] = "1"
timed_out = False
with (DEST / "events.jsonl").open("xb") as stdout, (DEST / "stderr.txt").open("xb") as stderr:
    try:
        result = subprocess.run(cmd, stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr,
                                env=env, cwd=runtime, timeout=1200)
        code = result.returncode
    except subprocess.TimeoutExpired:
        code = 124
        timed_out = True
save("run-meta.json", {
    "exit_code": code, "timed_out": timed_out, "duration_seconds": round(time.time() - start, 2),
    "model_requested": frozen["model"], "reasoning_effort_requested": frozen["reasoning_effort"],
    "retry_invocation": 1, "total_model_invocations_in_record": 2,
    "first_output_exists": (DEST / "first-output.md").is_file(),
    "evaluation": "Not performed by runner; first complete output retained without editing",
})
print(json.dumps({"exit_code": code, "duration_seconds": round(time.time() - start, 2),
                  "first_output_exists": (DEST / "first-output.md").is_file()}))
if code:
    raise SystemExit(code)
