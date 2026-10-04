"""One known-E02 autonomous regression with repaired reads and original inputs."""
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
E02_PRIOR = ROOT / "effect-test/E02-abstract-rule-refinement-2026-10-04"
MODEL, EFFORT = "gpt-6.1-sol", "high"
RUN_KIND = "known-E02-autonomous-regression"
FACTS = "effect-test/E02-abstract-materials-2026-10-03/科学事实包.md"
REQUIRED = ("inputs/task.md", "inputs/scientific-facts.md", "inputs/personal-experience.txt",
            "inputs/core-requirements.txt", "inputs/abstract-writing-method.txt")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(path):
    return {p.relative_to(path).as_posix(): digest(p) for p in sorted(path.rglob("*")) if p.is_file()}


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def save(name, value):
    p = RECORD / name
    assert not p.exists(), name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


assert not (RECORD / "materials").exists() and not (RECORD / "drafting").exists()
preflight = json.loads((RECORD / "preflight.json").read_text(encoding="utf-8"))
COMMIT = preflight["frozen_candidate_commit"]
canonical = json.loads((E02_PRIOR / "frozen-materials.json").read_text(encoding="utf-8"))
assert canonical["facts_source"] == FACTS
assert digest(ROOT / FACTS) == canonical["facts_source_sha256"]
previous = json.loads((PRIOR / "frozen-materials.json").read_text(encoding="utf-8"))
materials = RECORD / "materials"
materials.mkdir()
candidate = {}
for name in filter(None, git("ls-tree", "-r", "--name-only", "-z", COMMIT,
                             "skill-candidate/nature-writing", "skill-candidate/nature-shared").decode("utf-8").split("\0")):
    raw = git("show", COMMIT + ":" + name)
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
    "文献资料/Residual_Reinforcement_Learning_for_Robot_Control.pdf": ROOT / "文献资料/Residual_Reinforcement_Learning_for_Robot_Control.pdf",
    "analysis/reading/RRL2019.txt": ROOT / "analysis/reading/RRL2019.txt",
    "inputs/scientific-facts.md": ROOT / FACTS,
    "inputs/personal-experience.txt": ROOT / "我自己的经验和做法.txt",
    "inputs/core-requirements.txt": ROOT / "核心要求.txt",
    "inputs/abstract-writing-method.txt": ROOT / "摘要写作方法.txt",
    "inputs/task.md": PRIOR / "materials/inputs/task.md",
})
reused = {}
for name, source in sources.items():
    p = materials / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(source.read_bytes())
    reused[name] = {"source": source.relative_to(ROOT).as_posix(), "sha256": digest(source)}
assert len(candidate) == 100 and len(sources) == 55
assert (materials / "inputs/scientific-facts.md").read_bytes() == (ROOT / FACTS).read_bytes()
assert (materials / "inputs/task.md").read_bytes() == (E02_PRIOR / "materials/inputs/task.md").read_bytes()
target_sha = digest(ROOT / "effect-test/E02-abstract-materials-2026-10-03/source/Impedance_Learning_for_Robots_Interacting_With_Unknown_Environments.pdf")
assert not any(digest(p) == target_sha for p in materials.rglob("*.pdf"))
examples = "skill-candidate/nature-shared/core/robotics-writing-examples.md"
for name in re.findall(r"^\[[^\]]+\]: <\.\./\.\./\.\./(.*?)>$", (materials / examples).read_text(encoding="utf-8"), re.M):
    assert (materials / name).is_file(), name
assert {p.suffix for p in (materials / "effect-test").rglob("*") if p.is_file()} == {".pdf"}
runtime = Path(tempfile.mkdtemp(prefix="e02-abstract-judgment-regression-")) / "materials"
shutil.copytree(materials, runtime)
assert inventory(runtime) == inventory(materials)
protected = {name: digest(ROOT / name) for name in git("ls-files", "-z").decode("utf-8").split("\0")
             if name and (ROOT / name).is_file()}
installed = [{"directory": item["directory"], "files": inventory(Path(item["directory"]))}
             for item in previous["installed_skills"]]
common_end = (materials / examples).read_text(encoding="utf-8").splitlines().index("## 摘要")
save("frozen-materials.json", {
    "candidate_commit": COMMIT, "preparation_commit": git("rev-parse", "HEAD").decode().strip(),
    "run_kind": RUN_KIND, "new_paper_transfer_evidence": False, "model": MODEL, "reasoning_effort": EFFORT,
    "original_candidate_files_sha256": candidate, "materials_files_sha256": inventory(materials),
    "runtime_directory": str(runtime), "reused_sources": reused,
    "facts_source": FACTS, "facts_source_sha256": digest(ROOT / FACTS),
    "correct_original_E02_fact_pack_verified": True, "standard_request_byte_unchanged": True,
    "example_loading": {"file": examples, "common_and_task_index_lines": [1, common_end],
                        "available_reference_pdfs": 25, "reused_verified_reference_texts": 25},
    "protected_project_files_sha256": protected, "installed_skills": installed,
    "excluded": ["E02 original paper/abstract and source locators", "old drafts and human revisions",
                 "feedback", "human main line", "coordinator analyses/evaluations and execution records"],
    "isolation": "Fresh ephemeral CLI in external material-only directory; automatic project docs, installed skills, plugins, memories, network search and multi-agent disabled. Explicit command audit; no OS-level isolation claimed.",
})
reader = runpy.run_path(str(PRIOR / "execute_once.py"))
reader["read_required_inputs"].__globals__.update({"RECORD": RECORD, "REQUIRED_INPUTS": REQUIRED, "save": save})
returned = reader["read_required_inputs"](runtime, phase="before-invocation")
assert digest(runtime / "inputs/scientific-facts.md") == canonical["facts_source_sha256"]
prompt = (
    f"Complete the Abstract-only Drafting task at {runtime / 'inputs/task.md'}. "
    f"Read original author facts at {runtime / 'inputs/scientific-facts.md'}, personal experience at "
    f"{runtime / 'inputs/personal-experience.txt'}, complete core requirements at "
    f"{runtime / 'inputs/core-requirements.txt'} and the author's abstract-writing method at "
    f"{runtime / 'inputs/abstract-writing-method.txt'}. Invoke only the frozen local nature-writing at "
    f"{runtime / 'skill-candidate/nature-writing/SKILL.md'}, loading its manifest, required core, matching "
    "fragments and declared dependencies. For shared robotics examples, read common instructions and task "
    f"index first (lines 1-{common_end} of {runtime / examples}), then choose relevant cards and read their "
    "actual English, analysis and selection notes. Do not preload all cards or PDFs. The 25 declared reference "
    "PDFs and their verified extracted texts in analysis/reading are available on demand. Reference science "
    "does not add author facts. This is one autonomous first-pass regression on known E02 materials, "
    "not a new-paper transfer test. Only the materials directory is permitted input. Do not read outside it, "
    "installed skills, the source project, target original paper/abstract, source locators, old outputs, "
    "feedback, human main lines, coordinator analyses/evaluations or execution records. Do not browse or "
    "change files. Return one complete English abstract and accurate Chinese translation with necessary "
    "notes outside the abstract. Read UTF-8 using absolute paths and bounded numbered ranges, one file per "
    "command. Always wrap indexed Get-Content in @(...) and check actual returned contents. Numbered reads: "
    "$lines = @(Get-Content -LiteralPath <path> -Encoding UTF8); $start = <first>; $end = <last>; "
    "for ($i=$start; $i -le $end; $i++) { if ($i -le $lines.Count) { '{0}: {1}' -f $i,$lines[$i-1] } }. "
    "The execution layer has compared all returned lines of the following permitted original inputs; "
    "their complete texts follow, without additional writing guidance:\n"
)
for name in REQUIRED:
    prompt += "\n<original-input path=" + json.dumps(name) + ">\n" + (runtime / name).read_text(encoding="utf-8") + "\n</original-input>\n"
cmd = json.loads((PRIOR / "drafting/execution-command.json").read_text(encoding="utf-8"))
cmd[cmd.index("-C") + 1] = str(runtime)
dest = RECORD / "drafting"
dest.mkdir()
cmd[cmd.index("-o") + 1] = str(dest / "first-output.md")
cmd[-1] = prompt
assert cmd[cmd.index("-m") + 1] == MODEL and 'model_reasoning_effort="high"' in cmd
(dest / "execution-prompt.txt").write_text(prompt, encoding="utf-8")
save("drafting/execution-command.json", cmd)
save("drafting/frozen-run.json", {
    "observed_at_utc": datetime.now(timezone.utc).isoformat(), "candidate_commit": COMMIT,
    "run_kind": RUN_KIND, "new_paper_transfer_evidence": False, "model": MODEL, "reasoning_effort": EFFORT,
    "attempt": 1, "input_sha256": inventory(materials), "execution_layer_actual_return_validation": returned,
    "prompt_sha256": digest(dest / "execution-prompt.txt"), "working_directory": str(runtime),
    "runner_sha256": digest(Path(__file__)), "reader_source_sha256": digest(PRIOR / "execute_once.py"),
    "cli_sha256": digest(Path(cmd[0])), "cli_version": subprocess.check_output([cmd[0], "--version"]).decode().strip(),
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
    "exit_code": code, "duration_seconds": round(time.time() - started, 2), "candidate_commit": COMMIT,
    "model": MODEL, "reasoning_effort": EFFORT, "run_kind": RUN_KIND, "new_paper_transfer_evidence": False,
    "attempt": 1, "first_output_exists": (dest / "first-output.md").is_file(),
    "first_output_sha256": digest(dest / "first-output.md") if (dest / "first-output.md").is_file() else None,
    "no_feedback_rerun_selection_or_prose_edit": True,
})
print(json.dumps({"only_invocation_exit_code": code, "first_output_exists": (dest / "first-output.md").is_file()}))
if code:
    raise SystemExit(code)
