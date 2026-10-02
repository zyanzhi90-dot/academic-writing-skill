"""Prepare, execute once, and collect an isolated P17 abstract run; never assess prose."""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import time

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
COMMIT = "e126a659d77195f79416815db6ddb5827e60588e"
MODEL, EFFORT = "gpt-6-sol", "medium"
CLI = Path("C:/Users/user2/AppData/Roaming/npm/node_modules/@openai/codex/node_modules/@openai/codex-win32-x64/vendor/x86_64-pc-windows-msvc/bin/codex.exe")
FACTS = "effect-test/P17-abstract-materials-2026-10-02/\u79d1\u5b66\u4e8b\u5b9e\u5305.md"
EXPERIENCE = "\u6211\u81ea\u5df1\u7684\u7ecf\u9a8c\u548c\u505a\u6cd5.txt"
CORPUS = "\u6587\u732e\u8d44\u6599"


def git(*args):
    return subprocess.check_output(["git", "-c", "safe.directory=" + ROOT.as_posix(), *args], cwd=ROOT)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(directory):
    return {p.relative_to(directory).as_posix(): digest(p)
            for p in sorted(directory.rglob("*")) if p.is_file()}


def save(name, data):
    (RECORD / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def prepare():
    materials = RECORD / "materials"
    if materials.exists():
        raise SystemExit("Refusing to replace prepared materials")
    materials.mkdir()
    files = git("ls-tree", "-r", "--name-only", COMMIT, "skill-candidate/nature-writing", "skill-candidate/nature-shared").decode().splitlines()
    original = {}
    differences = []
    modified = []
    for name in files:
        raw = git("show", COMMIT + ":" + name)
        original[name] = hashlib.sha256(raw).hexdigest()
        target = materials / name
        target.parent.mkdir(parents=True, exist_ok=True)
        content = raw
        if name.endswith("core/robotics-writing-examples.md"):
            text = raw.decode("utf-8")
            text, count_a = re.subn(r"### A06\uff5c.*?(?=^## |^### |\Z)", "", text, flags=re.M | re.S)
            text, count_b = re.subn(r"### B01\uff5c.*?(?=^## |^### |\Z)", "", text, flags=re.M | re.S)
            assert count_a == count_b == 1
            text = text.replace("start with B01/B13", "start with B13")
            text = text.replace("B01\u3001B13", "B13").replace("\u53cc\u7ec4\u4ef6\u4e0e\u6784\u9020\u4f9d\u8d56", "\u6784\u9020\u4f9d\u8d56")
            text = text.replace("A01\u2013A06", "A01\u2013A05").replace("\u6bd4\u8f83\u6216\u7cfb\u7edf\u8d21\u732e", "\u6bd4\u8f83")
            text = text.replace("19 author-approved local papers", "18 author-approved local papers")
            text = text.replace("19 \u5361\u7247\u6db5\u76d6\u516d\u79cd", "17 \u5361\u7247\u6db5\u76d6\u4e94\u79cd").replace("19 \u7bc7\u5404\u7ed9", "18 \u7bc7\u5404\u7ed9")
            text = re.sub(r"^\[P17\]:.*\n?", "", text, flags=re.M)
            assert not re.search(r"P17|A06|B01|Robot_Learning_System", text)
            content = text.encode("utf-8")
        elif name.endswith("core/robotics-main-text.md"):
            text = raw.decode("utf-8")
            old = "P17 p.7 \u00a7V\n  explicitly separates tests of its controller and motion model; P06 p.12"
            assert old in text
            text = text.replace(old, "P06 p.12")
            text = re.sub(r"^\[P17\]\(.*\),\n", "", text, flags=re.M)
            assert "P17" not in text
            content = text.encode("utf-8")
        target.write_bytes(content)
        if content != raw:
            modified.append(name)
            differences.extend(difflib.unified_diff(raw.decode().splitlines(True), content.decode().splitlines(True), fromfile=COMMIT + "/" + name, tofile="isolated/" + name))
    assert len(modified) == 2
    (RECORD / "version-isolation.diff").write_text("".join(differences), encoding="utf-8")
    inputs = materials / "inputs"
    inputs.mkdir()
    (inputs / "scientific-facts.md").write_bytes((ROOT / FACTS).read_bytes())
    (inputs / "personal-experience.txt").write_bytes((ROOT / EXPERIENCE).read_bytes())
    task = (
        "\u672c\u8f6e\u4ec5\u8d77\u8349\u672c\u7814\u7a76\u7684 Abstract\uff0c\u4e0d\u5199\u5176\u4ed6\u90e8\u5206\u3002\n\n"
        "\u79d1\u5b66\u5185\u5bb9\u4ee5 inputs/scientific-facts.md \u4e3a\u4f9d\u636e\uff0c\u5199\u4f5c\u505a\u6cd5\u4ee5 inputs/personal-experience.txt \u4e3a\u4f9d\u636e\u3002"
        "\u4f7f\u7528\u6307\u5b9a\u7684 nature-writing\uff0c\u4ece\u53ef\u7528\u53c2\u8003\u4e2d\u9009\u62e9\u3001\u7ec4\u5408\u548c\u8c03\u6574\u5408\u9002\u7684\u7ec4\u7ec7\u4e0e\u5177\u4f53\u82f1\u6587\u5b9e\u73b0\uff0c"
        "\u5fe0\u5b9e\u3001\u51c6\u786e\u3001\u7b80\u6d01\u3001\u6e05\u6670\u3001\u6734\u7d20\u3001\u4e13\u4e1a\u5730\u8868\u8fbe\u4f5c\u8005\u81ea\u5df1\u7684\u79d1\u5b66\u5185\u5bb9\u3002"
        "\u4e8b\u5b9e\u5305\u4e2d\u7684\u652f\u6301\u7ec6\u8282\u6309\u6458\u8981\u9700\u8981\u53d6\u820d\uff0c\u4e0d\u8981\u6c42\u5168\u90e8\u5199\u5165\uff1b\u4e0d\u8865\u9020\u4e8b\u5b9e\u3001\u6761\u4ef6\u6216\u7ed3\u679c\u3002\n\n"
        "\u8f93\u51fa\u5b8c\u6574\u82f1\u6587\u6458\u8981\u53ca\u5176\u51c6\u786e\u4e2d\u6587\u7ffb\u8bd1\u3002\u5982\u6709\u5fc5\u8981\u7684\u4f5c\u8005\u8bf4\u660e\uff0c\u7f6e\u4e8e\u6458\u8981\u4e4b\u5916\u3002\n"
    )
    (inputs / "task.md").write_text(task, encoding="utf-8")
    papers = json.loads((ROOT / "analysis/inventory.json").read_text(encoding="utf-8"))
    corpus_sources = []
    for paper in papers:
        if paper["id"] == "P17":
            continue
        paths = [ROOT / CORPUS / Path(paper["file"]).name,
                 ROOT / "analysis/reading" / (paper["id"] + ".txt"),
                 ROOT / "analysis/extracted" / (paper["id"] + ".txt")]
        for source in paths:
            assert source.is_file()
            relative = source.relative_to(ROOT)
            dest = materials / relative
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(source.read_bytes())
            corpus_sources.append({"paper_id": paper["id"], "path": relative.as_posix(), "sha256": digest(source), "git_blob": git("hash-object", str(source)).decode().strip()})
    assert len(corpus_sources) == 54
    for path in materials.rglob("*"):
        assert "P17" not in path.name and "Robot_Learning_System" not in path.name
    protected = {name: digest(ROOT / name) for name in git("ls-files", "-z").decode().split("\0") if name and (ROOT / name).is_file()}
    installed = []
    for home in ("user", "user2"):
        for base in (".agents/skills", ".codex/skills"):
            for role in ("nature-writing", "nature-polishing", "nature-shared"):
                directory = Path("C:/Users") / home / base / role
                if directory.is_dir():
                    installed.append({"directory": str(directory), "files": inventory(directory)})
    runtime = Path(tempfile.mkdtemp(prefix="p17-abstract-independent-")) / "materials"
    shutil.copytree(materials, runtime)
    save("frozen-materials.json", {
        "candidate_commit": COMMIT, "preparation_commit": git("rev-parse", "HEAD").decode().strip(),
        "model": MODEL, "reasoning_effort": EFFORT,
        "original_candidate_files_sha256": original, "modified_copy_files": modified,
        "facts_source": FACTS, "facts_source_sha256": digest(ROOT / FACTS),
        "experience_source": EXPERIENCE, "experience_source_sha256": digest(ROOT / EXPERIENCE),
        "corpus_sources": corpus_sources, "materials_files_sha256": inventory(materials),
        "runtime_directory": str(runtime), "protected_project_files_sha256": protected,
        "installed_skills": installed,
        "excluded": ["P17 original PDF", "P17 extraction texts", "A06", "B01", "other P17-specific guidance and links", "source locators", "analyses", "old outputs", "evaluations", "isolation diff and run records"],
        "isolation": "Fresh ephemeral CLI context; separate material-only working directory outside project; allowed-file boundary in execution prompt, audited via command logs. No OS-level read isolation is claimed. No inherited writing conversation.",
    })
    print("Prepared", len(original), "candidate dependency files and", len(corpus_sources), "reference files")


def run():
    dest = RECORD / "drafting"
    if dest.exists():
        raise SystemExit("Refusing a second execution or overwriting first output")
    frozen = json.loads((RECORD / "frozen-materials.json").read_text(encoding="utf-8"))
    runtime = Path(frozen["runtime_directory"])
    assert inventory(runtime) == frozen["materials_files_sha256"]
    dest.mkdir()
    prompt = (
        f"Complete the Abstract-only task at {runtime / 'inputs/task.md'}. "
        f"Read its author scientific facts at {runtime / 'inputs/scientific-facts.md'} and "
        f"personal writing experience at {runtime / 'inputs/personal-experience.txt'}. "
        f"Invoke only the frozen local nature-writing at {runtime / 'skill-candidate/nature-writing/SKILL.md'} "
        "and read its manifest, matching fragments, and declared dependencies. "
        "Use the available example reference and other local papers on demand; their science does not add author facts. "
        "This is a new independent first-pass writing context. Only files inside the current materials directory "
        "are permitted inputs. Do not access any file outside it, installed skills, the source project, "
        "P17 original paper or extractions, P17 examples or analysis, A06, B01, source locators, prior outputs, "
        "evaluations, or execution records. Do not browse the internet. "
        "Use explicit absolute paths for individual material reads so the actual loading can be recorded; "
        "selected ranges are allowed. Do not change files. Return the complete English abstract and accurate "
        "Chinese translation, with any necessary author notes outside the abstract."
    )
    cmd = [str(CLI), "exec", "--json", "--ephemeral", "--ignore-user-config", "--skip-git-repo-check",
           "-s", "danger-full-access", "-m", MODEL, "-c", f'model_reasoning_effort="{EFFORT}"',
           "-c", "project_doc_max_bytes=0", "-c", 'web_search="disabled"',
           "-C", str(runtime), "-o", str(dest / "first-output.md"), prompt]
    (dest / "execution-prompt.txt").write_text(prompt, encoding="utf-8")
    (dest / "execution-command.json").write_text(json.dumps(cmd, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    save("drafting/frozen-run.json", {"candidate_commit": COMMIT, "model": MODEL, "reasoning_effort": EFFORT,
         "input_sha256": frozen["materials_files_sha256"], "prompt_sha256": digest(dest / "execution-prompt.txt"),
         "working_directory": str(runtime), "cli_sha256": digest(CLI),
         "cli_version": subprocess.check_output([str(CLI), "--version"]).decode().strip(),
         "attempt": 1})
    started = time.time()
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    with (dest / "events.jsonl").open("wb") as stdout, (dest / "stderr.txt").open("wb") as stderr:
        try:
            result = subprocess.run(cmd, stdout=stdout, stderr=stderr, env=env, timeout=900)
            code = result.returncode
        except subprocess.TimeoutExpired:
            code = 124
    save("drafting/run-meta.json", {"exit_code": code, "duration_seconds": round(time.time() - started, 2),
         "model": MODEL, "reasoning_effort": EFFORT, "candidate_commit": COMMIT,
         "first_output_exists": (dest / "first-output.md").is_file(), "attempt": 1,
         "evaluation": "Not performed; no prose editing"})
    print("exit", code, "output", (dest / "first-output.md").is_file())
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
    dest = RECORD / "drafting"
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
    save("drafting/loaded-files.json", {"loaded_or_searched_files": list(reads.values()), "commands": commands,
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["prepare", "run", "collect"])
    action = parser.parse_args().action
    {"prepare": prepare, "run": run, "collect": collect}[action]()
