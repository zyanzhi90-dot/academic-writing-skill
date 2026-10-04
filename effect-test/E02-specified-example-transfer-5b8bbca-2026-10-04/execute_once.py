"""Freeze and run one specified-example E02 route validation; do not judge prose."""
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
COMMIT = "5b8bbca46a436f4a3b73cb2cf3bc73984e16471d"
RUN_KIND = "specified-example-transfer-route-validation"
MODEL, EFFORT = "gpt-6.1-sol", "high"
FACTS = "effect-test/E02-abstract-materials-2026-10-03/科学事实包.md"
EXPERIENCE = "我自己的经验和做法.txt"


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
    sources = {"scientific-facts.md": ROOT / FACTS,
               "personal-experience.txt": ROOT / EXPERIENCE,
               "core-requirements.txt": ROOT / "\u6838\u5fc3\u8981\u6c42.txt",
               "author-request.txt": RECORD / "author-request.txt",
               "task.md": RECORD / "task-input.txt"}
    for name, source in sources.items():
        (inputs / name).write_bytes(source.read_bytes())
    (materials / "example-analysis.md").write_bytes((RECORD / "example-analysis.md").read_bytes())
    corpus = []
    source_info = json.loads((RECORD / "source-examples/inventory.json").read_text(encoding="utf-8"))
    for label in ("A06", "A07"):
        item = next(item for item in source_info if item["id"] == label)
        assert digest(ROOT / item["source"]) == item["pdf_sha256"]
        for suffix, key in ((".pdf", "pdf_sha256"), ("-full-text.txt", "full_text_sha256")):
            relative = "source-examples/" + label + suffix
            source = RECORD / relative
            assert digest(source) == item[key]
            target = materials / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())
            corpus.append({"example_id": label, "path": relative, "sha256": digest(source)})
    assert len(corpus) == 4
    examples = "skill-candidate/nature-shared/core/robotics-writing-examples.md"
    lines = (materials / examples).read_text(encoding="utf-8").splitlines()
    common_end = lines.index("## \u6458\u8981")
    protected = {name: digest(ROOT / name) for name in git("ls-files", "-z").decode("utf-8").split("\0")
                 if name and (ROOT / name).is_file()}
    installed, disabled = [], set()
    for home in ("user", "user2"):
        for base in (".agents/skills", ".codex/skills"):
            directory = Path("C:/Users") / home / base
            disabled.update(p.resolve().as_posix() for p in directory.rglob("SKILL.md"))
            for role in ("nature-writing", "nature-polishing", "nature-shared"):
                package = directory / role
                if package.is_dir():
                    installed.append({"directory": str(package), "files": inventory(package)})
    runtime = Path(tempfile.mkdtemp(prefix="e02-specified-example-route-")) / "materials"
    shutil.copytree(materials, runtime)
    save("frozen-materials.json", {
        "candidate_commit": COMMIT, "preparation_commit": git("rev-parse", "HEAD").decode().strip(),
        "run_kind": RUN_KIND, "autonomous_pass": False, "transfer_pass": False,
        "independent_skill_effect_evidence": False, "model": MODEL, "reasoning_effort": EFFORT,
        "original_candidate_files_sha256": original, "modified_copy_files": [],
        "facts_source": FACTS, "facts_source_sha256": digest(ROOT / FACTS),
        "experience_source": EXPERIENCE, "experience_source_sha256": digest(ROOT / EXPERIENCE),
        "inputs_sources": {name: {"source": source.relative_to(ROOT).as_posix(), "sha256": digest(source)}
                           for name, source in sources.items()},
        "example_analysis_sha256": digest(RECORD / "example-analysis.md"),
        "source_examples": source_info, "corpus_sources": corpus,
        "materials_files_sha256": inventory(materials), "runtime_directory": str(runtime),
        "protected_project_files_sha256": protected, "installed_skills": installed,
        "disabled_installed_skill_entrypoints": sorted(disabled),
        "example_loading": {"file": examples, "common_and_task_index_lines": [1, common_end],
                            "selected_full_papers": ["A06", "A07"], "other_papers_not_supplied": True},
        "excluded": ["E02 old outputs", "prewritten E02 mainline", "E02 target original abstract and full paper",
                     "E02 source locators", "prior evaluations and execution records", "source project",
                     "other reference PDFs and extraction texts"],
        "isolation": "Fresh ephemeral CLI in a project-external allowed-material-only directory. Automatic project docs, installed skills, plugins, memories, network and multi-agent disabled. Explicit-path command audit; no OS-level read isolation claimed.",
    })
    print("Frozen", len(original), "writing/shared files and two complete references; no old draft or E02 mainline supplied")


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
        f"Complete the specified-example Abstract route-validation task at {runtime / 'inputs/task.md'}. "
        f"Read the exact author request at {runtime / 'inputs/author-request.txt'}, core requirements at "
        f"{runtime / 'inputs/core-requirements.txt'}, personal experience at {runtime / 'inputs/personal-experience.txt'}, "
        f"and sole E02 scientific facts at {runtime / 'inputs/scientific-facts.md'}. "
        f"Invoke the frozen nature-writing at {runtime / 'skill-candidate/nature-writing/SKILL.md'} "
        "and load its manifest, required core, matching fragments and declared dependencies. "
        f"Read the example-only analysis at {runtime / 'example-analysis.md'}. "
        f"Both complete example PDFs and fresh full-text extractions are at {runtime / 'source-examples'}. "
        "Read A06-full-text.txt and A07-full-text.txt through their scientific body and Conclusion in bounded numbered chunks, "
        "including complete abstracts, actual contribution passages, relevant methods, conditions and evidence. "
        "For the shared example file, first read common instructions and task index "
        f"(lines 1-{examples['common_and_task_index_lines'][1]}) in {runtime / examples['file']}; "
        "then read A06 and A07 only for this explicitly selected reference route. Do not load other cards or reference sources. "
        "Determine E02 contributions and necessary content yourself from the author facts; select a main example and appropriate "
        "local support from the other. Adapt whole-paragraph organization, consecutive-sentence relations and mature exact English, "
        "not isolated labels or a post-draft synonym pass. Check every sentence and meaningful phrase against the source English "
        "and the E02 science, and check the paragraph as a whole before delivering the first answer. "
        "No E02 old draft, prewritten mainline, original abstract or full paper has been supplied. "
        "Only files within this materials directory are permitted inputs. Do not read outside it, installed skills, "
        "the source project, target E02 original or extractions, old outputs, mainline, source locators, "
        "preparation/evaluation/execution records. Do not browse the internet, change files, request feedback, generate alternative "
        "abstracts, rerun or proceed to E03. Return the complete English abstract, accurate Chinese translation and concise "
        "post-drafting transfer rationale, with all notes outside the abstract. This is a specified-example route validation, "
        "not autonomous or transfer pass evidence for the current Skill. "
        "Read text explicitly as UTF-8, with absolute file paths and source line numbers; one file per command and bounded chunks "
        "so actual returned text can be verified. For PowerShell use $n=0; Get-Content -LiteralPath <absolute-path> -Encoding UTF8 "
        "| ForEach-Object { $n++; \"${n}: $_\" } | Select-Object -Skip <start> -First <count>."
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
        "candidate_commit": COMMIT, "run_kind": RUN_KIND, "independent_skill_effect_evidence": False, "autonomous_pass": False, "transfer_pass": False, "model": MODEL, "reasoning_effort": EFFORT,
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
        "model": MODEL, "reasoning_effort": EFFORT, "candidate_commit": COMMIT, "run_kind": RUN_KIND, "independent_skill_effect_evidence": False, "autonomous_pass": False, "transfer_pass": False, "attempt": 1,
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
