"""Run one isolated E01 feedback rewrite; not independent first-drafting evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
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
COMMIT = "11e900cc53ccee25f5f9d6b93971551b87f2e87a"
MODEL, EFFORT = "gpt-6.1-sol", "high"
FACTS = "effect-test/E01-abstract-materials-2026-10-02/科学事实包.md"
EXPERIENCE = "我自己的经验和做法.txt"
PREVIOUS = ROOT / "effect-test/E01-abstract-retest-2026-10-02"
DRAFT = "effect-test/E01-abstract-retest-2026-10-02/drafting/first-output.md"
RUN_KIND = "feedback-rewrite"


def save(name, data):
    (RECORD / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def prepare():
    materials = RECORD / "materials"
    if materials.exists():
        raise SystemExit("Refusing to replace frozen materials")
    previous = json.loads((PREVIOUS / "frozen-materials.json").read_text(encoding="utf-8"))
    assert previous["candidate_commit"] == COMMIT
    assert inventory(PREVIOUS / "materials") == previous["materials_files_sha256"]
    original = previous["original_candidate_files_sha256"]
    for name, expected in original.items():
        assert hashlib.sha256(git("show", COMMIT + ":" + name)).hexdigest() == expected
    assert digest(ROOT / FACTS) == previous["facts_source_sha256"]
    assert digest(ROOT / EXPERIENCE) == previous["experience_source_sha256"]
    corpus = previous["corpus_sources"]
    current_pdfs = {p.relative_to(ROOT).as_posix(): digest(p) for p in (ROOT / "文献资料").glob("*.pdf")}
    assert current_pdfs == {p["path"]: p["sha256"] for p in corpus if p["path"].endswith(".pdf")}
    assert len(current_pdfs) == 21
    shutil.copytree(PREVIOUS / "materials", materials)
    inputs = materials / "inputs"
    (inputs / "current-draft.md").write_bytes((ROOT / DRAFT).read_bytes())
    (inputs / "feedback.md").write_text(
        "当前稿已有进步，但开头仍以 Learning、Data fitting 展开，整体推进仍接近事实包顺序，主要参考的整段组织与具体英文没有充分落实。\n\n"
        "沿用已验收 E01 科学事实包、《我自己的经验和做法.txt》及当前冻结候选。先确定摘要真正需要表达的科学内容和重点，再以 A06 的实际英文为默认风格起点，按内容吸收其他已认可主要摘要的合适写法。从整段组织、句间逻辑到句型句式和用词重新适配，使本文方法及其优势得到准确、清晰、简洁、朴素、专业的表达。事实包排列不规定写作顺序；不沿用现稿句序机械压缩，也不只替换开头词语。每句话的对象、事实、条件和结论必须属于本研究。\n",
        encoding="utf-8")
    (inputs / "task.md").write_text(
        "本轮仅对 inputs/current-draft.md 中的摘要执行一次参考驱动的完整重写，不写其他部分。"
        "本任务是反馈重写，不是独立首次起草。\n\n"
        "科学内容以 inputs/scientific-facts.md 为依据，写作做法以 inputs/personal-experience.txt 为依据；"
        "当前稿仅供定位反馈，不能增补事实包未支持的科学内容。读取 inputs/feedback.md 并完整落实本次反馈。"
        "调用冻结 nature-writing：先确定摘要所需科学内容和重点，再以 A06 的实际英文为默认风格起点，"
        "按内容吸收其他已认可主要摘要的合适实现，从整段组织到具体英文重新选择、组合和适配。"
        "事实包顺序不规定摘要顺序，不沿用现稿句序机械压缩，不只替换开头词语。"
        "准确、清晰、简洁、朴素、专业地表达本文方法及其受支持优势；支持细节按摘要需要取舍。"
        "每句话的对象、事实、关系、条件和结论属于本研究，不补造缺少的材料、实验或保证。\n\n"
        "交付完整英文摘要及准确中文翻译。必要作者说明放在摘要正文之外。\n",
        encoding="utf-8")
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
    runtime = Path(tempfile.mkdtemp(prefix="e01-abstract-feedback-rewrite-")) / "materials"
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
        "corpus_sources": corpus, "materials_files_sha256": inventory(materials),
        "corpus_extraction": previous["corpus_extraction"],
        "runtime_directory": str(runtime), "protected_project_files_sha256": protected,
        "installed_skills": installed, "disabled_installed_skill_entrypoints": sorted(disabled),
        "example_loading": {"file": examples, "common_and_task_index_lines": [1, common_end],
                            "all_19_cards_available": True, "all_21_current_papers_available": True},
        "excluded": ["target original paper and extraction texts", "source locators", "preparation records",
                     "evaluations other than the supplied author feedback", "other outputs and derived expressions",
                     "source project and execution records"],
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
        f"Complete the Abstract-only feedback-rewrite task at {runtime / 'inputs/task.md'}. "
        f"Read the author facts at {runtime / 'inputs/scientific-facts.md'} and personal experience at "
        f"{runtime / 'inputs/personal-experience.txt'}, the supplied current draft at "
        f"{runtime / 'inputs/current-draft.md'}, and the author feedback at {runtime / 'inputs/feedback.md'}. "
        "This is a full reference-driven rewrite responding to feedback, not an independent first drafting. "
        f"Invoke only the frozen local nature-writing at "
        f"{runtime / 'skill-candidate/nature-writing/SKILL.md'} and load its manifest, matching fragments "
        "and declared dependencies. Read all text explicitly as UTF-8: PowerShell Get-Content -Encoding UTF8 "
        "or Python read_text(encoding='utf-8'). For shared robotics examples, first read only common "
        f"instructions and task index (lines 1-{examples['common_and_task_index_lines'][1]}) in "
        f"{runtime / examples['file']}; then choose and read relevant card ranges, including their actual "
        "English, analysis and selection notes. Do not preload all cards or PDFs. Source-link definitions "
        "and all 21 current learning-paper PDFs and their corresponding freshly extracted texts in this "
        "materials directory are available on demand. "
        "Reference science does not add author facts. This is a fresh isolated feedback-rewrite session. "
        "Only files within the current materials directory are permitted inputs. Do not read outside it, "
        "installed skills, the source project, the target original paper or its extractions, source locators, "
        "preparation or evaluation materials other than the supplied author feedback, other outputs or their "
        "expression derivatives, or execution records. "
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
    verification = json.loads((RECORD / "verification.json").read_text(encoding="utf-8"))
    verification.update({"run_kind": RUN_KIND, "independent_first_drafting_evidence": False})
    save("verification.json", verification)
    print("Runner and existing collector unchanged; output preserved without evaluation")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["prepare", "run", "collect"])
    {"prepare": prepare, "run": run, "collect": collect}[parser.parse_args().action]()
