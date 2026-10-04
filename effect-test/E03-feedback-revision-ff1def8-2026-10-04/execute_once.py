"""One human-feedback revision, with current frozen Writing and reused sources."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import runpy
import shutil
import subprocess
import tempfile
import time

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
PRIOR = ROOT / "effect-test/E03-independent-transfer-fd7dbcb-valid-2026-10-04"
SOURCE = ROOT / "effect-test/E03-independent-transfer-fd7dbcb-2026-10-04"
COMMIT = "ff1def8eb045c2e2e977a17034ea2ad6f6c97c2b"
MODEL, EFFORT = "gpt-6.1-sol", "high"
FACTS = SOURCE / "科学事实包.md"
FACTS_SHA = "247c1bcb6ec104de9cf0907ecbad2d38db50c6a1b29a0b49255c7d62710d8d5c"
DRAFT = PRIOR / "drafting/first-output.md"
DRAFT_SHA = "923b4a5b5a6dc9a4b9397ef0e1ca417888af15a65843178c1c9ff1ca0ea60e7b"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(path):
    return {p.relative_to(path).as_posix(): digest(p)
            for p in sorted(path.rglob("*")) if p.is_file()}


def save(name, value):
    p = RECORD / name
    assert not p.exists(), name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


assert not (RECORD / "materials").exists() and not (RECORD / "drafting").exists()
assert digest(FACTS) == FACTS_SHA and digest(DRAFT) == DRAFT_SHA
assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT).decode().strip() == COMMIT
previous = json.loads((PRIOR / "frozen-materials.json").read_text(encoding="utf-8"))
materials = RECORD / "materials"
materials.mkdir()
candidate, reused = {}, {}
paths = subprocess.check_output([
    "git", "ls-tree", "-r", "--name-only", "-z", COMMIT,
    "skill-candidate/nature-writing", "skill-candidate/nature-shared"], cwd=ROOT).decode("utf-8").split("\0")
for name in filter(None, paths):
    raw = subprocess.check_output(["git", "show", COMMIT + ":" + name], cwd=ROOT)
    candidate[name] = hashlib.sha256(raw).hexdigest()
    p = materials / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(raw)
sources = {}
for item in previous["corpus_sources"]:
    p = PRIOR / "materials" / item["path"]
    assert digest(p) == item["sha256"]
    sources[item["path"]] = p
sources.update({
    "inputs/scientific-facts.md": FACTS,
    "inputs/current-draft.md": DRAFT,
    "inputs/personal-experience.txt": ROOT / "我自己的经验和做法.txt",
    "inputs/core-requirements.txt": ROOT / "核心要求.txt",
    "inputs/task.md": RECORD / "task-input.txt",
    "文献资料/Residual_Reinforcement_Learning_for_Robot_Control.pdf": ROOT / "文献资料/Residual_Reinforcement_Learning_for_Robot_Control.pdf",
    "analysis/reading/RRL2019.txt": ROOT / "analysis/reading/RRL2019.txt",
    "analysis/RRL2019-example-addition-2026-10-04/source-basis.md": ROOT / "analysis/RRL2019-example-addition-2026-10-04/source-basis.md",
    "source-e03/author-v2.pdf": SOURCE / "coordinator/source/target.pdf",
    "source-e03/author-v2-full-text.txt": SOURCE / "coordinator/source/target-full-text.txt",
    "source-e03/source-check.md": SOURCE / "coordinator/source-check.md",
})
for name, source in sources.items():
    p = materials / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(source.read_bytes())
    reused[name] = {"source": source.relative_to(ROOT).as_posix(), "sha256": digest(source)}
examples = materials / "skill-candidate/nature-shared/core/robotics-writing-examples.md"
for name in re.findall(r"^\[[^\]]+\]: <\.\./\.\./\.\./(.*?)>$", examples.read_text(encoding="utf-8"), re.M):
    assert (materials / name).is_file(), name
runtime = Path(tempfile.mkdtemp(prefix="e03-human-feedback-")) / "materials"
shutil.copytree(materials, runtime)
assert inventory(runtime) == inventory(materials)
protected = {name: digest(ROOT / name) for name in subprocess.check_output(
    ["git", "ls-files", "-z"], cwd=ROOT).decode("utf-8").split("\0")
    if name and (ROOT / name).is_file()}
author_note = ROOT / "摘要写作方法.txt"
protected[author_note.name] = digest(author_note)
installed = [{"directory": item["directory"], "files": inventory(Path(item["directory"]))}
             for item in previous["installed_skills"]]
save("frozen-materials.json", {
    "candidate_commit": COMMIT, "run_kind": "人工反馈修订", "model": MODEL,
    "reasoning_effort": EFFORT, "autonomous_pass": False, "transfer_pass": False,
    "original_candidate_files_sha256": candidate, "materials_files_sha256": inventory(materials),
    "runtime_directory": str(runtime), "reused_sources": reused,
    "protected_project_files_sha256": protected, "installed_skills": installed,
    "draft_source": DRAFT.relative_to(ROOT).as_posix(), "draft_source_sha256": DRAFT_SHA,
    "facts_source": FACTS.relative_to(ROOT).as_posix(), "facts_source_sha256": FACTS_SHA,
    "source_scope": "Human feedback revision: original draft, current author feedback, original facts, A06/A07/A08 cards, verified source texts and source check permitted. Historical evaluations excluded.",
    "isolation": "Fresh ephemeral CLI and external material-only directory; automatic project docs, installed skills, plugins, network search and multi-agent disabled. Audited commands, not OS-level isolation.",
})
# Reuse the already repaired execution-layer reader, checking returned TEXT.
reader = runpy.run_path(str(PRIOR / "execute_once.py"))
reader["read_required_inputs"].__globals__.update({
    "RECORD": RECORD,
    "REQUIRED_INPUTS": ("inputs/task.md", "inputs/scientific-facts.md", "inputs/personal-experience.txt",
                        "inputs/core-requirements.txt", "inputs/current-draft.md"),
    "save": save,
})
returned = reader["read_required_inputs"](runtime, phase="before-invocation")
assert digest(runtime / "inputs/scientific-facts.md") == FACTS_SHA
assert digest(runtime / "inputs/current-draft.md") == DRAFT_SHA
prompt = (
    f"Complete the human-feedback abstract revision in {runtime / 'inputs/task.md'}. "
    f"Use the unchanged draft at {runtime / 'inputs/current-draft.md'} and original scientific facts at "
    f"{runtime / 'inputs/scientific-facts.md'}. Read the complete original personal experience and core requirements "
    f"in {runtime / 'inputs'}. Invoke only the current frozen Writing candidate at "
    f"{runtime / 'skill-candidate/nature-writing/SKILL.md'}, its manifest, required core, matching abstract "
    "fragments and declared dependencies. Read common instructions and task index of the shared robotics "
    "example library, then the complete A06/A07/A08 English and analysis. Compare actual consecutive sentences "
    "and wording during generation and final phrase/sentence/paragraph checks. Verified A06/A07 full texts "
    "are analysis/reading/P17.txt and P05.txt; A08 is analysis/reading/RRL2019.txt. Original E03 author-v2 "
    "text and source check are in source-e03, available to resolve scientific meaning. "
    "Retain accurate established organization and mature expressions; change only what current feedback "
    "scientifically or rhetorically requires. Do not presume each sentence needs editing. Return one complete "
    "English abstract, accurate Chinese translation and concise actual-change rationale. Label human-feedback "
    "revision, never autonomous or transfer pass. Do not generate alternatives, run tests, request more feedback "
    "or edit files. Only this materials directory is permitted input; do not browse or read historical "
    "evaluations, external files or installed skills. Read UTF-8 using explicit absolute paths and bounded "
    "numbered ranges, one file per command. Always wrap indexed PowerShell Get-Content in @(...) and verify "
    "actual returned contents. Numbered reads: $lines = @(Get-Content -LiteralPath <path> -Encoding UTF8); "
    "$start = <first-line>; $end = <last-line>; for ($i=$start; $i -le $end; $i++) { "
    "if ($i -le $lines.Count) { '{0}: {1}' -f $i,$lines[$i-1] } }. "
    "The execution layer has compared every returned line of the following original permitted inputs; "
    "the complete texts follow, without an added outline or prewritten target:\n"
)
for entry in returned["inputs"]:
    name = entry["path"]
    prompt += "\n<original-input path=" + json.dumps(name) + ">\n" + (runtime / name).read_text(encoding="utf-8") + "\n</original-input>\n"
old_cmd = json.loads((PRIOR / "drafting/execution-command.json").read_text(encoding="utf-8"))
cmd = old_cmd.copy()
cmd[cmd.index("-C") + 1] = str(runtime)
dest = RECORD / "drafting"
dest.mkdir()
cmd[cmd.index("-o") + 1] = str(dest / "first-output.md")
cmd[-1] = prompt
assert cmd[cmd.index("-m") + 1] == MODEL
(dest / "execution-prompt.txt").write_text(prompt, encoding="utf-8")
save("drafting/execution-command.json", cmd)
save("preflight.json", {
    "observed_at_utc": datetime.now(timezone.utc).isoformat(), "candidate_commit": COMMIT,
    "model": MODEL, "reasoning_effort": EFFORT, "run_kind": "人工反馈修订",
    "single_revision_invocation": True, "not_autonomous_retest": True,
    "original_draft_and_facts_byte_preserved": True, "candidate_git_bytes_preserved": True,
    "required_input_return_validation": returned, "runner_sha256": digest(Path(__file__)),
    "reader_source_sha256": digest(PRIOR / "execute_once.py"), "cli_sha256": digest(Path(cmd[0])),
    "cli_version": subprocess.check_output([cmd[0], "--version"]).decode().strip(),
    "prompt_sha256": digest(dest / "execution-prompt.txt"),
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
    "candidate_commit": COMMIT, "model": MODEL, "reasoning_effort": EFFORT,
    "run_kind": "人工反馈修订", "revision_invocation": 1,
    "first_output_exists": (dest / "first-output.md").exists(),
    "first_output_sha256": digest(dest / "first-output.md") if (dest / "first-output.md").exists() else None,
    "autonomous_pass": False, "transfer_pass": False,
})
print(json.dumps({"exit_code": code, "first_output_exists": (dest / "first-output.md").exists()}))
if code:
    raise SystemExit(code)
