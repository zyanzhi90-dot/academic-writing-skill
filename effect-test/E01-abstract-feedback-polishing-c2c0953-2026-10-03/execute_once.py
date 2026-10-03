"""Freeze and run one targeted E01 feedback polish; not independent drafting evidence."""
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
COMMIT = "c2c09537e4f1f944eb8a8aa82cbc7ecf5203b6a7"
MODEL, EFFORT = "gpt-6.1-sol", "high"
FACTS = "effect-test/E01-abstract-materials-2026-10-02/科学事实包.md"
EXPERIENCE = "我自己的经验和做法.txt"
PREVIOUS = ROOT / "effect-test/E01-abstract-retest-c2c0953-2026-10-03"
DRAFT = "effect-test/E01-abstract-retest-c2c0953-2026-10-03/drafting/first-output.md"
RUN_KIND = "targeted-feedback-polishing"


def save(name, data):
    (RECORD / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def prepare():
    materials = RECORD / "materials"
    if materials.exists():
        raise SystemExit("Refusing to replace frozen materials")
    previous = json.loads((PREVIOUS / "frozen-materials.json").read_text(encoding="utf-8"))
    assert previous["candidate_commit"] == COMMIT
    assert inventory(PREVIOUS / "materials") == previous["materials_files_sha256"]
    assert digest(ROOT / FACTS) == previous["facts_source_sha256"]
    assert digest(ROOT / EXPERIENCE) == previous["experience_source_sha256"]
    materials.mkdir()
    original = {}
    paths = git("ls-tree", "-r", "--name-only", "-z", COMMIT,
                "skill-candidate/nature-polishing", "skill-candidate/nature-shared").decode("utf-8").split("\0")
    for name in filter(None, paths):
        raw = git("show", COMMIT + ":" + name)
        original[name] = hashlib.sha256(raw).hexdigest()
        target = materials / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
    corpus = previous["corpus_sources"]
    for item in corpus:
        name = item["path"]
        source = PREVIOUS / "materials" / name
        assert digest(source) == item["sha256"], name
        target = materials / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source.read_bytes())
    assert len(corpus) == 48
    inputs = materials / "inputs"
    inputs.mkdir()
    (inputs / "scientific-facts.md").write_bytes((ROOT / FACTS).read_bytes())
    (inputs / "personal-experience.txt").write_bytes((ROOT / EXPERIENCE).read_bytes())
    (inputs / "current-draft.md").write_bytes((ROOT / DRAFT).read_bytes())
    (inputs / "feedback.md").write_text(
        "作者此前明确指出 Simulations of …、Experiments with … 的表达不符合要求，并认可 Experimental studies are also carried out to …、Numerical simulation results demonstrate … 等成熟写法。本稿验证句仍保留上述问题。请读取匹配的认可范例实际英文，分别适配模拟研究目的、实机结果和移动目标观察，落实作者要求的朴素句法、明确对象及句间推进。保持研究目的、实际发现和模型能力的区别，不补造模拟结论或增强证据。\n\n"
        "修改限于验证部分及必要上下文，保留其余合格内容，准确同步中文翻译。\n",
        encoding="utf-8")
    (inputs / "task.md").write_text(
        "本轮仅对 inputs/current-draft.md 的摘要执行一次定点反馈修订，不起草新稿或推进其他部分。本任务为反馈 Polishing，不是独立首次 Drafting。\n\n"
        "调用冻结的 nature-polishing，以 inputs/scientific-facts.md 为唯一作者科学依据，并依据原样 inputs/personal-experience.txt 及 inputs/feedback.md。读取匹配认可范例的实际英文，再适配为作者自己的科学内容。修改限于验证部分及必要上下文，保留其余合格内容；稿件不能作为增补事实的依据。\n\n"
        "返回完整英文摘要及准确同步的中文翻译。必要说明置于摘要正文外，简要指出本次修改位置、实际参考和修改依据；不把本次反馈修订当作独立首次起草通过证据。\n",
        encoding="utf-8")
    examples = "skill-candidate/nature-shared/core/robotics-writing-examples.md"
    lines = (materials / examples).read_text(encoding="utf-8").splitlines()
    common_end = lines.index("## 摘要")
    archive_files = [p for p in (materials / "effect-test").rglob("*") if p.is_file()]
    assert len(archive_files) == 3 and all(p.suffix == ".pdf" for p in archive_files)
    links = dict(re.findall(r"^\[([^\]]+)\]: <\.\./\.\./\.\./(.*?)>$", (materials / examples).read_text(encoding="utf-8"), re.M))
    assert all((materials / name).is_file() for name in links.values())
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
    runtime = Path(tempfile.mkdtemp(prefix="e01-abstract-feedback-polishing-c2c0953-")) / "materials"
    shutil.copytree(materials, runtime)
    save("frozen-materials.json", {
        "candidate_commit": COMMIT, "preparation_commit": git("rev-parse", "HEAD").decode().strip(),
        "run_kind": RUN_KIND, "independent_first_drafting_evidence": False,
        "model": MODEL, "reasoning_effort": EFFORT,
        "original_candidate_files_sha256": original, "modified_copy_files": [],
        "facts_source": FACTS, "facts_source_sha256": digest(ROOT / FACTS),
        "experience_source": EXPERIENCE, "experience_source_sha256": digest(ROOT / EXPERIENCE),
        "draft_source": DRAFT, "draft_source_sha256": digest(ROOT / DRAFT),
        "feedback_file": "inputs/feedback.md", "feedback_sha256": digest(inputs / "feedback.md"),
        "reuse_materials_source": PREVIOUS.relative_to(ROOT).as_posix() + "/materials",
        "reuse_freeze_record_sha256": digest(PREVIOUS / "frozen-materials.json"),
        "corpus_sources": corpus, "corpus_extraction": previous["corpus_extraction"],
        "corpus_transfer": "Copy only verified permitted PDFs and corresponding texts; no previous runtime inputs, logs, reports or output except the explicitly authorized current draft",
        "archive_isolation": previous["archive_isolation"],
        "materials_files_sha256": inventory(materials), "runtime_directory": str(runtime),
        "protected_project_files_sha256": protected,
        "installed_skills": installed, "disabled_installed_skill_entrypoints": sorted(disabled),
        "example_loading": {"file": examples, "common_and_task_index_lines": [1, common_end],
                            "all_20_cards_available": True, "all_21_current_papers_available": True,
                            "all_3_declared_archive_papers_available": True},
        "excluded": ["target original paper and extraction texts", "source locators", "preparation records",
                     "evaluations other than supplied author feedback", "other outputs and derived expressions",
                     "source project and execution records"],
        "isolation": "Fresh ephemeral CLI in a project-external material-only directory; automatic project docs, installed skills, plugins and network search disabled for this invocation. Allowed-input prompt and actual command audit; no OS-level read isolation claimed.",
    })
    print("Frozen", len(original), "polishing/shared candidate files and", len(corpus), "reference files; no candidate changes")

def run():
    dest = RECORD / "polishing"
    if dest.exists():
        raise SystemExit("Refusing a second invocation or overwriting first output")
    frozen = json.loads((RECORD / "frozen-materials.json").read_text(encoding="utf-8"))
    runtime = Path(frozen["runtime_directory"])
    assert inventory(runtime) == frozen["materials_files_sha256"]
    dest.mkdir()
    examples = frozen["example_loading"]
    prompt = (
        f"Complete the Abstract-only targeted-feedback Polishing task at {runtime / 'inputs/task.md'}. "
        f"Read the author facts at {runtime / 'inputs/scientific-facts.md'} and personal experience at "
        f"{runtime / 'inputs/personal-experience.txt'}, the authorized current draft at "
        f"{runtime / 'inputs/current-draft.md'}, and feedback at {runtime / 'inputs/feedback.md'}. "
        "This is one targeted feedback revision, not independent first drafting. "
        "Invoke only the frozen local nature-polishing at "
        f"{runtime / 'skill-candidate/nature-polishing/SKILL.md'} and load its manifest, matching fragments "
        "and declared dependencies. Read all text explicitly as UTF-8: PowerShell Get-Content -Encoding UTF8 "
        "or Python read_text(encoding='utf-8'). For shared robotics examples, first read only common "
        f"instructions and task index (lines 1-{examples['common_and_task_index_lines'][1]}) in "
        f"{runtime / examples['file']}; then choose and read relevant card ranges, including their actual "
        "English, analysis and selection notes. Do not preload all cards or PDFs. Source-link definitions "
        "and all 21 current learning-paper PDFs, three separately copied archive-paper PDFs, and their corresponding freshly extracted texts in this "
        "materials directory are available on demand. "
        "Reference science does not add author facts. This is a fresh isolated feedback-polishing context. "
        "Only files within the current materials directory are permitted inputs. Do not read outside it, "
        "installed skills, the source project, the target original paper or its extractions, source locators, "
        "preparation or evaluation materials other than the supplied feedback, other outputs or their expression derivatives, or execution records. "
        "Do not browse the internet or change files. Use explicit absolute paths and bounded ranges for "
        "material reads so actual loading is auditable. Return the complete English abstract and accurate "
        "Chinese translation, with necessary notes outside the abstract."
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
    save("polishing/execution-command.json", cmd)
    save("polishing/frozen-run.json", {
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
    save("polishing/run-meta.json", {
        "exit_code": code, "duration_seconds": round(time.time() - started, 2),
        "model": MODEL, "reasoning_effort": EFFORT, "candidate_commit": COMMIT, "attempt": 1,
        "run_kind": RUN_KIND, "independent_first_drafting_evidence": False,
        "first_output_exists": (dest / "first-output.md").is_file(), "evaluation": "Not independent first-drafting evidence; no post-run manual prose editing",
    })
    print("Only invocation: exit", code, "output", (dest / "first-output.md").is_file())
    if code:
        raise SystemExit(code)


def collect():
    frozen = json.loads((RECORD / "frozen-materials.json").read_text(encoding="utf-8"))
    runtime = Path(frozen["runtime_directory"])
    assert inventory(RECORD / "materials") == frozen["materials_files_sha256"]
    assert inventory(runtime) == frozen["materials_files_sha256"]
    for name, expected in frozen["protected_project_files_sha256"].items():
        assert digest(ROOT / name) == expected, name
    for item in frozen["installed_skills"]:
        assert inventory(Path(item["directory"])) == item["files"], item["directory"]
    dest = RECORD / "polishing"
    commands, reads, unresolved, outside = [], {}, [], []
    terminal = None
    for line in (dest / "events.jsonl").read_text(encoding="utf-8").splitlines():
        event = json.loads(line)
        item = event.get("item", {})
        if event.get("type") == "item.completed" and item.get("type") == "agent_message":
            terminal = item["text"]
        if event.get("type") != "item.completed" or item.get("type") != "command_execution":
            continue
        command = item.get("command", "")
        commands.append({"id": item.get("id"), "command": command, "exit_code": item.get("exit_code"),
                         "output_characters": len(item.get("aggregated_output", ""))})
        normalized = command.replace("\\\\", "\\")
        paths = re.findall(r"[A-Za-z]:[\\/][^'\"\r\n]*?\.(?:md|yaml|txt|pdf|py|json)\b", normalized)
        if re.search(r"Get-Content|\brg\b|read_text|read_bytes|pymupdf|pdfplumber|fitz|pdftotext", command, re.I):
            found = False
            for value in paths:
                path = Path(value).resolve()
                if path.is_relative_to(runtime) and path.is_file():
                    found = True
                    name = path.relative_to(runtime).as_posix()
                    entry = reads.setdefault(name, {"path": name, "sha256": digest(path), "command_ids": []})
                    entry["command_ids"].append(item.get("id"))
                elif not path.is_relative_to(runtime):
                    outside.append({"command_id": item.get("id"), "path": str(path)})
            if not found:
                unresolved.append(item.get("id"))
    output = dest / "first-output.md"
    matches = output.is_file() and terminal is not None and output.read_text(encoding="utf-8").rstrip("\r\n") == terminal.rstrip("\r\n")
    save("polishing/loaded-files.json", {"loaded_or_searched_files": list(reads.values()), "commands": commands,
         "unresolved_read_commands": unresolved, "outside_materials_explicit_reads": outside,
         "evidence_limit": "Explicit file paths in completed commands; raw events preserve outputs and selected ranges. A search or range read is not asserted to be a complete-file read.",
         "evaluation": "Not performed"})
    run_frozen = json.loads((dest / "frozen-run.json").read_text(encoding="utf-8"))
    assert digest(dest / "execution-prompt.txt") == run_frozen["prompt_sha256"]
    save("verification.json", {"materials_unchanged": True, "runtime_unchanged": True,
         "protected_project_files_unchanged": True, "installed_skills_unchanged": True,
         "first_output_sha256": digest(output) if output.is_file() else None,
         "first_output_bytes": output.stat().st_size if output.is_file() else 0,
         "first_output_matches_terminal_message_except_final_newline": matches,
         "outside_materials_explicit_reads": outside, "unresolved_read_commands": unresolved,
         "attempts": 1, "evaluation": "Not performed; no quality verdict"})
    print("Collected loading and byte-preservation evidence; no prose evaluation")

    run_frozen = json.loads((RECORD / "polishing/frozen-run.json").read_text(encoding="utf-8"))
    assert digest(Path(__file__)) == run_frozen["runner_sha256"]
    assert digest(HELPER_PATH) == run_frozen["collector_helper_sha256"]
    verification = json.loads((RECORD / "verification.json").read_text(encoding="utf-8"))
    verification.update({"run_kind": RUN_KIND, "independent_first_drafting_evidence": False})
    save("verification.json", verification)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["prepare", "run", "collect"])
    {"prepare": prepare, "run": run, "collect": collect}[parser.parse_args().action]()
