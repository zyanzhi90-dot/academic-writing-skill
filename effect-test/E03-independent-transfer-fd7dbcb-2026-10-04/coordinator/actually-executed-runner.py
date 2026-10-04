"""Freeze and run one independent E03 abstract transfer test; do not judge prose."""
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
COMMIT = json.loads((RECORD / "preflight.json").read_text(encoding="utf-8"))["frozen_candidate_commit"]
RUN_KIND = "E03-independent-transfer"
MODEL, EFFORT = "gpt-6.1-sol", "high"
FACTS = "effect-test/E02-abstract-materials-2026-10-03/科学事实包.md"
EXPERIENCE = "我自己的经验和做法.txt"
REQUIRED_INPUTS = ("inputs/task.md", "inputs/scientific-facts.md",
                   "inputs/personal-experience.txt", "inputs/core-requirements.txt")


def read_required_inputs(runtime, phase="preparation"):
    """Validate the actual PowerShell return, including a single-line input."""
    def literal(value):
        return "'" + str(value).replace("'", "''") + "'"
    script = "$OutputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)\n"
    script += "$records = @(\n"
    for name in REQUIRED_INPUTS:
        script += "$lines = @(Get-Content -LiteralPath " + literal(runtime / name) + " -Encoding UTF8)\n"
        script += "[pscustomobject]@{path=" + literal(name) + ";lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}\n"
    script += ")\nConvertTo-Json -InputObject @($records) -Depth 6\n"
    cmd = ["powershell", "-NoProfile", "-NonInteractive", "-Command", script]
    result = subprocess.run(cmd, capture_output=True, check=True)
    returned = json.loads(result.stdout.decode("utf-8-sig"))
    (RECORD / ("execution-read-" + phase + ".ps1")).write_text(script, encoding="utf-8-sig")
    (RECORD / ("execution-read-" + phase + ".stdout.json")).write_bytes(result.stdout)
    (RECORD / ("execution-read-" + phase + ".stderr.txt")).write_bytes(result.stderr)
    checks = []
    assert len(returned) == len(REQUIRED_INPUTS)
    for entry, name in zip(returned, REQUIRED_INPUTS):
        source = runtime / name
        expected = source.read_text(encoding="utf-8").splitlines()
        assert entry["path"] == name
        assert entry["lines"] == expected, (name, "Actual returned text is incomplete")
        assert entry["line_count"] == len(expected)
        checks.append({"path": name, "source_sha256": digest(source),
                       "line_count": len(expected), "actual_returned_lines": entry["lines"],
                       "all_lines_returned_verbatim": True})
    report = {"phase": phase, "array_wrapped_get_content": True,
              "actual_returned_content_checked": True, "inputs": checks}
    save("execution-read-" + phase + ".json", report)
    return report


def save(name, data):
    (RECORD / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def prepare():
    materials = RECORD / "materials"
    if (RECORD / "frozen-materials.json").exists():
        raise SystemExit("Refusing to replace frozen materials")
    materials.mkdir(exist_ok=True)
    original = {}
    paths = git("ls-tree", "-r", "--name-only", "-z", COMMIT,
                "skill-candidate/nature-writing", "skill-candidate/nature-shared").decode("utf-8").split("\0")
    for name in filter(None, paths):
        raw = git("show", COMMIT + ":" + name)
        original[name] = hashlib.sha256(raw).hexdigest()
        target = materials / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
    previous_record = ROOT / "effect-test/E02-abstract-autonomous-regression-2026-10-04"
    previous_frozen = json.loads((previous_record / "frozen-materials.json").read_text(encoding="utf-8"))
    prior_sources = {item["path"]: item for item in previous_frozen["corpus_sources"]}
    prior_extractions = {item["pdf"]: item for item in previous_frozen["corpus_extraction"]["papers"]}
    inputs = materials / "inputs"
    inputs.mkdir(exist_ok=True)
    (inputs / "scientific-facts.md").write_bytes((ROOT / FACTS).read_bytes())
    (inputs / "personal-experience.txt").write_bytes((ROOT / EXPERIENCE).read_bytes())
    (inputs / "core-requirements.txt").write_bytes((ROOT / "\u6838\u5fc3\u8981\u6c42.txt").read_bytes())
    (inputs / "task.md").write_text(
        "本轮仅调用提供的 nature-writing，根据 inputs/scientific-facts.md 中的中文科学事实包和 inputs/personal-experience.txt 中的原样作者经验，直接撰写完整英文摘要，并附准确中文翻译。\n"
        "由 Skill 自主确定中心贡献、内容取舍和论述组织，严格从认可参考的真实英文出发，借鉴段落推进、连续句关系、句型句式和具体用词，替换为本研究科学内容。表达准确、清晰、简洁、朴素、专业，结论限于事实包明确支持的范围。必要作者说明置于摘要之外。\n",
        encoding="utf-8")
    papers = sorted((ROOT / "文献资料").glob("*.pdf"))
    assert len(papers) == 21
    current_paper_count = len(papers)
    examples_name = "skill-candidate/nature-shared/core/robotics-writing-examples.md"
    links = dict(re.findall(r"^\[([^\]]+)\]: <\.\./\.\./\.\./(.*?)>$",
                            (materials / examples_name).read_text(encoding="utf-8"), re.M))
    archive_sources = []
    for label in ("P04", "P06", "P19"):
        relative = links[label]
        paper = ROOT / relative
        assert paper.is_file() and paper.suffix == ".pdf"
        historical_path = "文献资料/" + paper.name
        assert paper.read_bytes() == git("show", "20c7839:" + historical_path)
        archive_sources.append({"paper_id": label, "source_path": relative,
                                "sha256": digest(paper), "original_commit": "20c7839",
                                "original_path": historical_path,
                                "archive_byte_identical": True})
        papers.append(paper)
    assert len(papers) == 24
    previous_ids = {Path(paper["file"]).name: paper["id"] for paper in
                    json.loads((ROOT / "analysis/inventory.json").read_text(encoding="utf-8"))}
    corpus = []
    extractions = []
    extraction_tool = shutil.which("pdftotext")
    assert extraction_tool
    for paper in papers:
        assert paper.stem not in ("Impedance_Learning_for_Robots_Interacting_With_Unknown_Environments", "Residual_Reinforcement_Learning_for_Robot_Control")
        assert digest(paper) != digest(RECORD / "coordinator/source/target.pdf")
        relative = paper.relative_to(ROOT)
        target = materials / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(paper.read_bytes())
        paper_id = previous_ids.get(paper.name)
        corpus.append({"paper_id": paper_id, "path": relative.as_posix(), "sha256": digest(paper)})
        # Reuse the already verified PDF extraction, checking both its PDF and text hashes.
        previous = prior_extractions[relative.as_posix()]
        assert previous["pdf_sha256"] == digest(paper)
        text_relative = Path(previous["text"])
        previous_text = previous_record / "materials" / text_relative
        assert digest(previous_text) == previous["text_sha256"] == prior_sources[text_relative.as_posix()]["sha256"]
        text_target = materials / text_relative
        text_target.parent.mkdir(parents=True, exist_ok=True)
        text_target.write_bytes(previous_text.read_bytes())
        corpus.append({"paper_id": paper_id, "path": text_relative.as_posix(), "sha256": digest(text_target),
                       "generated_from_current_pdf": relative.as_posix(), "source_pdf_sha256": digest(paper)})
        extractions.append({"pdf": relative.as_posix(), "text": text_relative.as_posix(),
                            "pages": previous["pages"], "pdf_sha256": digest(paper),
                            "text_sha256": digest(text_target),
                            "stderr": previous["stderr"], "reused_verified_text": True})
    assert len(corpus) == 48
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
    runtime = Path(tempfile.mkdtemp(prefix="e03-independent-abstract-transfer-")) / "materials"
    shutil.copytree(materials, runtime)
    required_read = read_required_inputs(runtime)
    save("frozen-materials.json", {
        "required_input_return_validation": required_read,
        "candidate_commit": COMMIT, "run_kind": RUN_KIND, "new_paper_transfer_evidence": True, "preparation_commit": git("rev-parse", "HEAD").decode().strip(),
        "model": MODEL, "reasoning_effort": EFFORT,
        "original_candidate_files_sha256": original, "modified_copy_files": [],
        "facts_source": FACTS, "facts_source_sha256": digest(ROOT / FACTS),
        "facts_material_version": {
            "last_change_commit": git("log", "-1", "--format=%H", "--", FACTS).decode().strip(),
            "blob_id": None,
            "sha256": digest(ROOT / FACTS),
            "material_status": "Original E03 Chinese fact extraction frozen before the only writing invocation; source and provenance excluded",
            "status_record_not_provided_to_writer": True,
        },
        "experience_material_version": {
            "last_change_commit": git("log", "-1", "--format=%H", "--", EXPERIENCE).decode().strip(),
            "blob_id": git("rev-parse", "HEAD:" + EXPERIENCE).decode().strip(),
            "sha256": digest(ROOT / EXPERIENCE),
        },
        "experience_source": EXPERIENCE, "experience_source_sha256": digest(ROOT / EXPERIENCE),
        "corpus_sources": corpus, "materials_files_sha256": inventory(materials),
        "corpus_extraction": {"current_pdf_count": current_paper_count, "archived_pdf_count": len(archive_sources),
                              "total_pdf_count": len(papers), "reused_verified_text_count": len(extractions),
                              "method": "Reuse byte-verified prior pdftotext -raw -enc UTF-8 texts with page markers; no prose rewriting",
                              "reuse_source_record": previous_record.relative_to(ROOT).as_posix(),
                              "tool_path": extraction_tool, "tool_sha256": digest(Path(extraction_tool)),
                              "existing_ids_retained_only_for_matching_current_filenames": True,
                              "new_papers_named_by_pdf_stem": True, "papers": extractions},
        "archive_isolation": {"sources": archive_sources,
                              "method": "Copy only three exact archived PDFs into the declared relative locations inside the new isolated materials; no historical output, log, metadata or evaluation copied; frozen candidate bytes unchanged"},
        "runtime_directory": str(runtime), "protected_project_files_sha256": protected,
        "installed_skills": installed, "disabled_installed_skill_entrypoints": sorted(disabled),
        "example_loading": {"file": examples, "common_and_task_index_lines": [1, common_end],
                            "all_20_cards_available": True, "all_21_current_papers_available": True,
                            "all_3_declared_archive_papers_available": True},
        "excluded": ["target original paper and extraction texts", "source locators", "preparation records",
                     "evaluations", "old outputs and derived expressions", "source project and execution records"],
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
        f"Complete the Abstract-only Drafting task at {runtime / 'inputs/task.md'}. "
        f"Read the author facts at {runtime / 'inputs/scientific-facts.md'} and personal experience at "
        f"{runtime / 'inputs/personal-experience.txt'} and core requirements at "
        f"{runtime / 'inputs/core-requirements.txt'}. Invoke only the frozen local nature-writing at "
        f"{runtime / 'skill-candidate/nature-writing/SKILL.md'} and load its manifest, matching fragments "
        "and declared dependencies. Read all text explicitly as UTF-8: PowerShell Get-Content -Encoding UTF8 "
        "or Python read_text(encoding='utf-8'). When indexing PowerShell Get-Content results, always use "
        "$lines = @(Get-Content -LiteralPath $path -Encoding UTF8) so a one-line file returns its whole line. "
        "Check returned contents before drafting. For shared robotics examples, first read only common "
        f"instructions and task index (lines 1-{examples['common_and_task_index_lines'][1]}) in "
        f"{runtime / examples['file']}; then choose and read relevant card ranges, including their actual "
        "English, analysis and selection notes. Do not preload all cards or PDFs. Source-link definitions "
        "and all 21 current learning-paper PDFs, three separately copied archive-paper PDFs, and their corresponding verified extracted texts in this "
        "materials directory are available on demand. "
        "Reference science does not add author facts. "
        "Only files within the current materials directory are permitted inputs. Do not read outside it, "
        "installed skills, the source project, the target original paper or its extractions, source locators, "
        "preparation or evaluation materials, old outputs or their expression derivatives, or execution records. "
        "Do not browse the internet or change files. Use explicit absolute paths and bounded ranges for "
        "material reads so actual loading is auditable. Return the complete English abstract and accurate "
        "Chinese translation, with necessary notes outside the abstract."
    )
    # Execution-layer delivery of the four ORIGINAL permitted inputs only. No analysis or new writing instructions.
    required = read_required_inputs(runtime, phase="before-invocation")
    prompt += "\n\nThe execution layer has read and compared every returned line of the four required original inputs. " \
              "Their complete original text follows (the same files, not additional guidance):\n"
    for name in REQUIRED_INPUTS:
        original = (runtime / name).read_text(encoding="utf-8")
        prompt += "\n<original-input path=" + json.dumps(name) + ">\n" + original + "\n</original-input>\n"
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
        "candidate_commit": COMMIT, "run_kind": RUN_KIND, "new_paper_transfer_evidence": True, "model": MODEL, "reasoning_effort": EFFORT,
        "input_sha256": frozen["materials_files_sha256"],
        "required_inputs_delivered_verbatim_in_initial_prompt": list(REQUIRED_INPUTS),
        "execution_layer_actual_return_validation": required,
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
        "model": MODEL, "reasoning_effort": EFFORT, "candidate_commit": COMMIT, "run_kind": RUN_KIND, "new_paper_transfer_evidence": True, "attempt": 1,
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
