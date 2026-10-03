"""Run one E02 Abstract content-organization feedback revision; not independent drafting evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from pathlib import Path
import runpy
import shutil
import subprocess
import tempfile
import time

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
HELPER_PATH = ROOT / "effect-test/P17-abstract-first-drafting-2026-10-02/execute_once.py"
HELPER = runpy.run_path(str(HELPER_PATH))
git, digest, inventory, CLI = (HELPER[name] for name in ("git", "digest", "inventory", "CLI"))
COMMIT = "f1d19cef06b3e4775213cd046e9555c2eaa0a53b"
MODEL, EFFORT = "gpt-6.1-sol", "high"
PREVIOUS = ROOT / "effect-test/E02-abstract-retest-f1d19ce-2026-10-03"
FACTS = "effect-test/E02-abstract-retest-f1d19ce-2026-10-03/materials/inputs/scientific-facts.md"
EXPERIENCE = "effect-test/E02-abstract-retest-f1d19ce-2026-10-03/materials/inputs/personal-experience.txt"
DRAFT = "effect-test/E02-abstract-retest-f1d19ce-2026-10-03/drafting/first-output.md"
DRAFT_COMMIT = "88c109681b9025ae93d6e779b4fb11693ecd946b"
RUN_KIND = "content-organization-feedback-revision"


def save(name, data):
    (RECORD / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def prepare():
    materials = RECORD / "materials"
    if materials.exists():
        raise SystemExit("Refusing to replace frozen materials")
    materials.mkdir()
    original = {}
    paths = git("ls-tree", "-r", "--name-only", "-z", COMMIT,
                "skill-candidate/nature-writing", "skill-candidate/nature-shared").decode("utf-8").split("\0")
    for name in filter(None, paths):
        raw = git("show", COMMIT + ":" + name)
        original[name] = hashlib.sha256(raw).hexdigest()
        target = materials / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
    inputs = materials / "inputs"
    inputs.mkdir()
    (inputs / "scientific-facts.md").write_bytes((ROOT / FACTS).read_bytes())
    (inputs / "personal-experience.txt").write_bytes((ROOT / EXPERIENCE).read_bytes())
    draft = git("show", DRAFT_COMMIT + ":" + DRAFT)
    assert draft == (ROOT / DRAFT).read_bytes()
    (inputs / "current-draft.md").write_bytes(draft)
    feedback = (RECORD / "author-feedback.md").read_bytes()
    (inputs / "feedback.md").write_bytes(feedback)
    (inputs / "task.md").write_text(
        "本轮仅对 inputs/current-draft.md 中的最新 E02 摘要作一次内容组织反馈修订，不推进其他部分。本任务是反馈修订，不是新的独立起草测试。\n"
        "读取 inputs/scientific-facts.md、inputs/personal-experience.txt、inputs/current-draft.md 和原样 inputs/feedback.md，调用提供的冻结 nature-writing 按作者反馈执行。科学内容以原样事实包为准，对照 A06／A07 完整摘要，按反馈允许的范围调整必要句子。\n"
        "交付完整英文摘要、准确中文翻译及简短修改依据，必要作者说明置于摘要正文之外。\n",
        encoding="utf-8")
    previous = json.loads((PREVIOUS / "frozen-materials.json").read_text(encoding="utf-8"))
    assert previous["candidate_commit"] == COMMIT
    assert inventory(PREVIOUS / "materials") == previous["materials_files_sha256"]
    assert digest(ROOT / FACTS) == previous["facts_source_sha256"]
    assert digest(ROOT / EXPERIENCE) == previous["experience_source_sha256"]
    corpus = previous["corpus_sources"]
    for item in corpus:
        name = item["path"]
        source = PREVIOUS / "materials" / name
        assert digest(source) == item["sha256"], name
        assert "Impedance_Learning_for_Robots_Interacting_With_Unknown_Environments" not in name
        target = materials / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source.read_bytes())
    assert len(corpus) == 48
    examples_name = "skill-candidate/nature-shared/core/robotics-writing-examples.md"
    links = dict(re.findall(r"^\[([^\]]+)\]: <\.\./\.\./\.\./(.*?)>$",
                            (materials / examples_name).read_text(encoding="utf-8"), re.M))
    archive_sources = previous["archive_isolation"]["sources"]
    # Preserve frozen candidate links without copying historical records.
    archived_materials = [p for p in (materials / "effect-test").rglob("*") if p.is_file()]
    assert {p.relative_to(materials).as_posix() for p in archived_materials} == {
        item["source_path"] for item in archive_sources}
    assert all(p.suffix == ".pdf" for p in archived_materials)
    for name, expected in original.items():
        assert digest(materials / name) == expected, name
    for relative in links.values():
        assert (materials / relative).is_file(), relative
    body_file = materials / "skill-candidate/nature-shared/core/robotics-main-text.md"
    for bracketed, plain in re.findall(r"\[[^\]]+\]\((?:<([^>]+)>|([^)]*))\)", body_file.read_text(encoding="utf-8")):
        relative = bracketed or plain
        if relative.endswith(".pdf"):
            assert (body_file.parent / relative).resolve().is_file(), relative
    examples = "skill-candidate/nature-shared/core/robotics-writing-examples.md"
    lines = (materials / examples).read_text(encoding="utf-8").splitlines()
    common_end = lines.index("## 摘要")
    protected = {name: digest(ROOT / name) for name in git("ls-files", "-z").decode("utf-8").split("\0")
                 if name and (ROOT / name).is_file()}
    installed = []
    disabled = set()
    for home in ("user", "user2"):
        for base in (".agents/skills", ".codex/skills"):
            directory = Path("C:/Users") / home / base
            disabled.update(p.resolve().as_posix() for p in directory.rglob("SKILL.md"))
            for role in ("nature-writing", "nature-polishing", "nature-shared"):
                package = directory / role
                if package.is_dir():
                    installed.append({"directory": str(package), "files": inventory(package)})
    runtime = Path(tempfile.mkdtemp(prefix="e02-abstract-f1d19ce-feedback-")) / "materials"
    shutil.copytree(materials, runtime)
    save("frozen-materials.json", {
        "candidate_commit": COMMIT, "preparation_commit": git("rev-parse", "HEAD").decode().strip(),
        "model": MODEL, "reasoning_effort": EFFORT,
        "run_kind": RUN_KIND, "independent_first_drafting_evidence": False,
        "draft_source": DRAFT, "draft_source_commit": DRAFT_COMMIT,
        "draft_source_sha256": digest(ROOT / DRAFT),
        "feedback_file": "inputs/feedback.md", "feedback_sha256": digest(inputs / "feedback.md"),
        "reuse_freeze_record_sha256": digest(PREVIOUS / "frozen-materials.json"),
        "corpus_transfer": "Only hash-verified permitted PDFs and corresponding texts copied; no prior execution records, other drafts, diagnoses or evaluations passed to writer",
        "original_candidate_files_sha256": original, "modified_copy_files": [],
        "facts_source": FACTS, "facts_source_sha256": digest(ROOT / FACTS),
        "facts_material_version": {
            "last_change_commit": git("log", "-1", "--format=%H", "--", FACTS).decode().strip(),
            "blob_id": git("rev-parse", "HEAD:" + FACTS).decode().strip(),
            "sha256": digest(ROOT / FACTS),
            "correction_owner_acceptance_status": "Pending owner acceptance; this run explicitly authorized using the current corrected materials",
            "status_record_not_provided_to_writer": True,
        },
        "experience_material_version": {
            "last_change_commit": git("log", "-1", "--format=%H", "--", EXPERIENCE).decode().strip(),
            "blob_id": git("rev-parse", "HEAD:" + EXPERIENCE).decode().strip(),
            "sha256": digest(ROOT / EXPERIENCE),
        },
        "experience_source": EXPERIENCE, "experience_source_sha256": digest(ROOT / EXPERIENCE),
        "corpus_sources": corpus, "materials_files_sha256": inventory(materials),
        "corpus_extraction": previous["corpus_extraction"],
        "archive_isolation": {"sources": archive_sources,
                              "method": "Copy only three exact archived PDFs into the declared relative locations inside the new isolated materials; no historical output, log, metadata or evaluation copied; frozen candidate bytes unchanged"},
        "runtime_directory": str(runtime), "protected_project_files_sha256": protected,
        "installed_skills": installed, "disabled_installed_skill_entrypoints": sorted(disabled),
        "example_loading": {"file": examples, "common_and_task_index_lines": [1, common_end],
                            "all_20_cards_available": True, "all_21_current_papers_available": True,
                            "all_3_declared_archive_papers_available": True},
        "excluded": ["target original paper and extraction texts", "source locators", "preparation records",
                     "evaluations other than supplied author feedback", "outputs and expression derivatives other than the authorized current draft", "source project and execution records"],
        "isolation": "Fresh ephemeral CLI in a project-external material-only directory; automatic project docs, installed skills, plugins and network search disabled for this invocation. Allowed-input prompt and actual command audit; no OS-level read isolation claimed.",
    })
    print("Frozen", len(original), "candidate files and", len(corpus), "reference files; no candidate changes")


def run():
    dest = RECORD / "drafting"
    if dest.exists():
        raise SystemExit("Refusing a second invocation or overwriting first output")
    frozen = json.loads((RECORD / "frozen-materials.json").read_text(encoding="utf-8"))
    runtime = Path(frozen["runtime_directory"])
    assert inventory(runtime) == frozen["materials_files_sha256"]
    dest.mkdir()
    examples = frozen["example_loading"]
    prompt = (
        f"Complete the Abstract-only content-organization feedback-revision task at {runtime / 'inputs/task.md'}. "
        f"Read the author facts at {runtime / 'inputs/scientific-facts.md'} and personal experience at "
        f"{runtime / 'inputs/personal-experience.txt'}, the current draft at "
        f"{runtime / 'inputs/current-draft.md'}, and author feedback at "
        f"{runtime / 'inputs/feedback.md'}. Invoke only the frozen local nature-writing at "
        f"{runtime / 'skill-candidate/nature-writing/SKILL.md'} and load its manifest, matching fragments "
        "and declared dependencies. Read all text explicitly as UTF-8: PowerShell Get-Content -Encoding UTF8 "
        "or Python read_text(encoding='utf-8'). For shared robotics examples, first read only common "
        f"instructions and task index (lines 1-{examples['common_and_task_index_lines'][1]}) in "
        f"{runtime / examples['file']}; then choose and read relevant card ranges, including their actual "
        "English, analysis and selection notes. Do not preload all cards or PDFs. Source-link definitions "
        "and all 21 current learning-paper PDFs, three separately copied archive-paper PDFs, and their corresponding freshly extracted texts in this "
        "materials directory are available on demand. "
        "Reference science does not add author facts. This is one feedback revision in a fresh context, not independent first drafting. "
        "Only files within the current materials directory are permitted inputs. Do not read outside it, "
        "installed skills, the source project, the target original paper or its extractions, source locators, "
        "preparation or evaluation materials other than the supplied author feedback, other outputs or their expression derivatives, or execution records. "
        "Do not browse the internet or change files. Use explicit absolute paths and bounded ranges for "
        "material reads so actual loading is auditable. Return the complete English abstract and accurate "
        "Chinese translation and brief revision rationale, with necessary notes outside the abstract."
    )
    disabled_skills = "skills.config=[" + ",".join(
        "{path=" + json.dumps(path) + ",enabled=false}"
        for path in frozen["disabled_installed_skill_entrypoints"]) + "]"
    cmd = [str(CLI), "exec", "--json", "--ephemeral", "--ignore-user-config", "--ignore-rules",
           "--skip-git-repo-check", "-s", "danger-full-access", "-m", MODEL,
           "-c", f'model_reasoning_effort="{EFFORT}"', "-c", "project_doc_max_bytes=0",
           "-c", 'web_search="disabled"', "-c", disabled_skills]
    for feature in ("plugins", "remote_plugin", "apps", "hooks", "memories", "multi_agent"):
        cmd.extend(["--disable", feature])
    cmd.extend(["-C", str(runtime), "-o", str(dest / "first-output.md"), prompt])
    (dest / "execution-prompt.txt").write_text(prompt, encoding="utf-8")
    save("drafting/execution-command.json", cmd)
    save("drafting/frozen-run.json", {
        "candidate_commit": COMMIT, "model": MODEL, "reasoning_effort": EFFORT,
        "run_kind": RUN_KIND, "independent_first_drafting_evidence": False,
        "input_sha256": frozen["materials_files_sha256"],
        "prompt_sha256": digest(dest / "execution-prompt.txt"), "working_directory": str(runtime),
        "cli_sha256": digest(CLI), "cli_version": subprocess.check_output([str(CLI), "--version"]).decode().strip(),
        "runner_sha256": digest(Path(__file__)), "collector_helper_sha256": digest(HELPER_PATH), "attempt": 1,
    })
    started = time.time()
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    with (dest / "events.jsonl").open("wb") as stdout, (dest / "stderr.txt").open("wb") as stderr:
        try:
            result = subprocess.run(cmd, stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr,
                                    env=env, cwd=runtime, timeout=900)
            code = result.returncode
        except subprocess.TimeoutExpired:
            code = 124
    save("drafting/run-meta.json", {
        "exit_code": code, "duration_seconds": round(time.time() - started, 2),
        "model": MODEL, "reasoning_effort": EFFORT, "candidate_commit": COMMIT, "attempt": 1,
        "run_kind": RUN_KIND, "independent_first_drafting_evidence": False,
        "first_output_exists": (dest / "first-output.md").is_file(), "evaluation": "Not performed; no prose editing",
    })
    print("Only invocation: exit", code, "output", (dest / "first-output.md").is_file())
    if code:
        raise SystemExit(code)


def collect():
    HELPER["collect"].__globals__["RECORD"] = RECORD
    HELPER["collect"]()
    frozen = json.loads((RECORD / "drafting/frozen-run.json").read_text(encoding="utf-8"))
    assert digest(Path(__file__)) == frozen["runner_sha256"]
    assert digest(HELPER_PATH) == frozen["collector_helper_sha256"]
    print("Runner and existing collector unchanged; output preserved without evaluation")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["prepare", "run", "collect"])
    {"prepare": prepare, "run": run, "collect": collect}[parser.parse_args().action]()
