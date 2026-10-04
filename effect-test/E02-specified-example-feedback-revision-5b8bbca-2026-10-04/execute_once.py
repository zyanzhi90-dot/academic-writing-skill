"""Reuse verified scientific/example materials for one feedback-revision invocation."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import time

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
PRIOR = ROOT / "effect-test/E02-specified-example-transfer-5b8bbca-2026-10-04"
COMMIT = "5b8bbca46a436f4a3b73cb2cf3bc73984e16471d"
MODEL, EFFORT = "gpt-6.1-sol", "high"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(path):
    return {p.relative_to(path).as_posix(): digest(p)
            for p in sorted(path.rglob("*")) if p.is_file()}


def save(name, value):
    path = RECORD / name
    if path.exists():
        raise SystemExit(f"Refusing to overwrite {name}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


assert not (RECORD / "materials").exists() and not (RECORD / "drafting").exists()
old = json.loads((PRIOR / "frozen-materials.json").read_text(encoding="utf-8"))
assert old["candidate_commit"] == COMMIT
assert inventory(PRIOR / "materials") == old["materials_files_sha256"]
candidate = old["original_candidate_files_sha256"]
sources = {}
for name, expected in candidate.items():
    raw = subprocess.check_output(["git", "show", COMMIT + ":" + name], cwd=ROOT)
    assert hashlib.sha256(raw).hexdigest() == expected
    sources[name] = PRIOR / "materials" / name
for item in old["corpus_sources"]:
    assert digest(PRIOR / "materials" / item["path"]) == item["sha256"]
    sources[item["path"]] = PRIOR / "materials" / item["path"]
for name in ("scientific-facts.md", "personal-experience.txt", "core-requirements.txt"):
    sources["inputs/" + name] = PRIOR / "materials/inputs" / name
sources["example-analysis.md"] = PRIOR / "materials/example-analysis.md"
draft_source = PRIOR / "retry-2026-10-04/first-output.md"
draft_verification = json.loads((PRIOR / "retry-2026-10-04/verification.json").read_text(encoding="utf-8"))
assert digest(draft_source) == draft_verification["first_output_retained_sha256"]
sources["inputs/current-draft.md"] = draft_source
sources["inputs/author-feedback.txt"] = RECORD / "author-feedback.txt"
sources["inputs/task.md"] = RECORD / "task-input.txt"
materials = RECORD / "materials"
for name, source in sources.items():
    target = materials / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(source.read_bytes())
runtime = Path(tempfile.mkdtemp(prefix="e02-example-feedback-writing-")) / "materials"
shutil.copytree(materials, runtime)
tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode("utf-8").split("\0")
protected = {name: digest(ROOT / name) for name in tracked if name and (ROOT / name).is_file()}
installed = [{"directory": item["directory"], "files": inventory(Path(item["directory"]))}
             for item in old["installed_skills"]]
save("frozen-materials.json", {
    "candidate_commit": COMMIT, "preparation_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT).decode().strip(),
    "model": MODEL, "reasoning_effort": EFFORT, "run_kind": "人工反馈修订",
    "autonomous_pass": False, "transfer_pass": False,
    "original_candidate_files_sha256": candidate,
    "materials_files_sha256": inventory(materials), "runtime_directory": str(runtime),
    "reused_sources": {name: {"path": source.relative_to(ROOT).as_posix(), "sha256": digest(source)} for name, source in sources.items()},
    "source_examples": old["source_examples"], "example_loading": old["example_loading"],
    "protected_project_files_sha256": protected, "installed_skills": installed,
    "draft_source": draft_source.relative_to(ROOT).as_posix(), "draft_source_sha256": digest(draft_source),
    "excluded": ["E02 target original abstract/full paper", "prior coordinator evaluations", "unrelated old drafts", "execution records", "installed skills"],
    "isolation": "New ephemeral context in external material-only directory. Automatic project docs, installed skills, plugins, memories, network and multi-agent disabled; command returns audited. No OS-level read isolation claimed.",
})
prompt = (
    f"Complete the human-feedback revision task at {runtime / 'inputs/task.md'}. "
    f"Read the complete current author feedback at {runtime / 'inputs/author-feedback.txt'}, "
    f"the unchanged current draft at {runtime / 'inputs/current-draft.md'}, sole scientific facts at "
    f"{runtime / 'inputs/scientific-facts.md'}, personal experience at {runtime / 'inputs/personal-experience.txt'}, "
    f"and core requirements at {runtime / 'inputs/core-requirements.txt'}. Invoke only the frozen Writing "
    f"candidate at {runtime / 'skill-candidate/nature-writing/SKILL.md'}, loading its manifest, required core, "
    "matching fragments and declared dependencies. This is feedback revision with Writing, not an installed Polishing skill. "
    f"Reuse the example-only analysis at {runtime / 'example-analysis.md'} and check the actual complete abstracts, "
    f"contribution passages and relevant methods in {runtime / 'source-examples/A06-full-text.txt'} and "
    f"{runtime / 'source-examples/A07-full-text.txt'} through the scientific body and conclusions. "
    f"For {runtime / old['example_loading']['file']}, read the common instructions and task index first "
    "(lines 1-144), then A06/A07 only. Preserve the established contribution organization and accurate mature expressions. "
    "Make only scientifically or rhetorically justified sentence-group and word-level changes; do not require each sentence "
    "to change. Use source consecutive-sentence relationships and actual English during generation and the final internal "
    "sentence/phrase/paragraph check. Current feedback governs this revision, including no exhaustive high/low-weight curve "
    "description. Return one complete English abstract, accurate Chinese translation and concise actual-change rationale. "
    "Label the result as human-feedback revision, not autonomous writing pass evidence. "
    "Only this materials directory is permitted input. Do not read external files, installed skills, target original paper "
    "or abstract, unrelated drafts, coordinator evaluations or execution records. Do not browse, modify files, request "
    "further feedback, generate alternatives, rerun or proceed to E03. Read UTF-8 with explicit absolute paths and bounded "
    "numbered ranges, one file per command: PowerShell $n=0; Get-Content -LiteralPath <path> -Encoding UTF8 | "
    'ForEach-Object { $n++; "${n}: $_" } | Select-Object -Skip <start> -First <count>.'
)
old_cmd = json.loads((PRIOR / "retry-2026-10-04/execution-command.json").read_text(encoding="utf-8"))
cmd = old_cmd.copy()
cmd[cmd.index("-C") + 1] = str(runtime)
dest = RECORD / "drafting"
dest.mkdir()
cmd[cmd.index("-o") + 1] = str(dest / "first-output.md")
cmd[-1] = prompt
assert cmd[cmd.index("-m") + 1] == MODEL
save("drafting/execution-command.json", cmd)
(dest / "execution-prompt.txt").write_text(prompt, encoding="utf-8")
save("preflight.json", {
    "observed_at_utc": datetime.now(timezone.utc).isoformat(),
    "run_kind": "人工反馈修订", "candidate_commit": COMMIT, "model_requested": MODEL, "reasoning_effort_requested": EFFORT,
    "single_revision_invocation": True, "candidate_byte_identical_to_git": True,
    "draft_and_scientific_inputs_byte_preserved": True, "material_file_count": len(sources),
    "runner_sha256": digest(Path(__file__)), "cli_sha256": digest(Path(cmd[0])),
    "cli_version": subprocess.check_output([cmd[0], "--version"]).decode().strip(),
    "prompt_sha256": digest(dest / "execution-prompt.txt"),
    "autonomous_pass": False, "transfer_pass": False,
})
started = time.time()
env = os.environ.copy()
env["PYTHONUTF8"] = "1"
with (dest / "events.jsonl").open("xb") as stdout, (dest / "stderr.txt").open("xb") as stderr:
    try:
        result = subprocess.run(cmd, stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr,
                                cwd=runtime, env=env, timeout=1200)
        code = result.returncode
    except subprocess.TimeoutExpired:
        code = 124
save("drafting/run-meta.json", {
    "exit_code": code, "duration_seconds": round(time.time() - started, 2),
    "model_requested": MODEL, "reasoning_effort_requested": EFFORT, "candidate_commit": COMMIT,
    "run_kind": "人工反馈修订", "revision_invocation": 1,
    "first_output_exists": (dest / "first-output.md").exists(), "no_output_editing_or_selection": True,
    "autonomous_pass": False, "transfer_pass": False,
})
print(json.dumps({"exit_code": code, "first_output_exists": (dest / "first-output.md").exists()}))
if code:
    raise SystemExit(code)
