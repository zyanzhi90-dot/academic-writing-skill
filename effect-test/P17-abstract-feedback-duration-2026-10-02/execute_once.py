"""One isolated feedback revision; reuse the accepted runner's record collector."""
from __future__ import annotations

import argparse
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
FIRST = ROOT / "effect-test/P17-abstract-first-drafting-2026-10-02"
HELPER_PATH = FIRST / "execute_once.py"
HELPER = runpy.run_path(str(HELPER_PATH))
git, digest, inventory = (HELPER[name] for name in ("git", "digest", "inventory"))
COMMIT, MODEL, EFFORT, CLI = (HELPER[name] for name in ("COMMIT", "MODEL", "EFFORT", "CLI"))


def save(name, data):
    (RECORD / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def prepare():
    target = RECORD / "materials"
    if target.exists():
        raise SystemExit("Refusing to replace frozen feedback materials")
    accepted = json.loads((FIRST / "frozen-materials.json").read_text(encoding="utf-8"))
    assert accepted["candidate_commit"] == COMMIT
    assert inventory(FIRST / "materials") == accepted["materials_files_sha256"]
    shutil.copytree(FIRST / "materials", target)
    inputs = target / "inputs"
    for name in ("task.md", "feedback.txt"):
        (inputs / name).write_bytes((RECORD / name).read_bytes())
    source_output = FIRST / "drafting/first-output.md"
    (inputs / "previous-first-output.md").write_bytes(source_output.read_bytes())
    assert digest(inputs / "scientific-facts.md") == digest(ROOT / accepted["facts_source"])
    assert digest(inputs / "personal-experience.txt") == digest(ROOT / accepted["experience_source"])
    example_path = "skill-candidate/nature-shared/core/robotics-writing-examples.md"
    lines = (target / example_path).read_text(encoding="utf-8").splitlines()
    starts = [(i + 1, line) for i, line in enumerate(lines) if re.match(r"^### [AB]\d+\uff5c", line)]
    abstract_heading = next(i + 1 for i, line in enumerate(lines) if line == "## \u6458\u8981")
    cards = []
    for start, heading in starts:
        end = next((i + 1 for i in range(start, len(lines)) if re.match(r"^## |^### ", lines[i])), len(lines) + 1) - 1
        cards.append({"id": re.match(r"^### ([AB]\d+)", heading)[1], "heading": heading,
                      "start_line": start, "end_line": end})
    assert len(cards) == 17 and not {"A06", "B01"} & {card["id"] for card in cards}
    links_start = next(i + 1 for i, line in enumerate(lines) if line.startswith("[P01]:"))
    ranges = {"file": example_path, "line_numbers": "1-based inclusive",
              "common_instructions_and_task_index": {"start_line": 1, "end_line": abstract_heading - 1},
              "cards": cards, "source_link_definitions": {"start_line": links_start, "end_line": len(lines)}}
    (target / "example-read-ranges.json").write_text(json.dumps(ranges, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for path, expected in accepted["materials_files_sha256"].items():
        if not path.startswith("inputs/"):
            assert digest(target / path) == expected, path
    (RECORD / "version-isolation.diff").write_bytes((FIRST / "version-isolation.diff").read_bytes())
    for item in accepted["installed_skills"]:
        assert inventory(Path(item["directory"])) == item["files"]
    protected = {name: digest(ROOT / name) for name in git("ls-files", "-z").decode().split("\0")
                 if name and (ROOT / name).is_file()}
    runtime = Path(tempfile.mkdtemp(prefix="p17-abstract-feedback-")) / "materials"
    shutil.copytree(target, runtime)
    save("frozen-materials.json", {
        "candidate_commit": COMMIT, "preparation_commit": git("rev-parse", "HEAD").decode().strip(),
        "model": MODEL, "reasoning_effort": EFFORT, "task": "P17 Abstract targeted feedback revision",
        "accepted_materials_record": FIRST.relative_to(ROOT).as_posix(),
        "original_candidate_files_sha256": accepted["original_candidate_files_sha256"],
        "modified_copy_files": accepted["modified_copy_files"],
        "additional_candidate_changes": [], "corpus_sources": accepted["corpus_sources"],
        "previous_output_source": source_output.relative_to(ROOT).as_posix(),
        "previous_output_sha256": digest(source_output), "facts_source": accepted["facts_source"],
        "facts_source_sha256": digest(inputs / "scientific-facts.md"),
        "experience_source": accepted["experience_source"],
        "experience_source_sha256": digest(inputs / "personal-experience.txt"),
        "feedback_sha256": digest(inputs / "feedback.txt"),
        "materials_files_sha256": inventory(target), "runtime_directory": str(runtime),
        "protected_project_files_sha256": protected, "installed_skills": accepted["installed_skills"],
        "example_loading": ranges, "helper_sha256": digest(HELPER_PATH),
        "excluded": ["P17 original PDF and extractions", "P17 examples and analyses", "A06", "B01",
                     "source locators", "evaluations", "all outputs except the supplied previous-first-output.md",
                     "project plans and execution records"],
        "isolation": "Fresh ephemeral context in a project-external material-only directory; allowed-file prompt boundary and actual command audit. No OS-level read isolation claimed.",
    })
    print("Frozen feedback materials; common/index lines 1-", abstract_heading - 1, "; cards:", len(cards))


def run():
    dest = RECORD / "drafting"
    if dest.exists():
        raise SystemExit("Refusing a second feedback execution or overwriting output")
    frozen = json.loads((RECORD / "frozen-materials.json").read_text(encoding="utf-8"))
    runtime = Path(frozen["runtime_directory"])
    assert inventory(runtime) == frozen["materials_files_sha256"]
    dest.mkdir()
    common = frozen["example_loading"]["common_instructions_and_task_index"]
    prompt = (
        f"Perform the targeted Abstract-only feedback task at {runtime / 'inputs/task.md'}. "
        f"Read the author facts at {runtime / 'inputs/scientific-facts.md'}, personal experience at "
        f"{runtime / 'inputs/personal-experience.txt'}, the supplied first complete output at "
        f"{runtime / 'inputs/previous-first-output.md'}, and feedback at {runtime / 'inputs/feedback.txt'}. "
        f"Invoke the frozen nature-writing at {runtime / 'skill-candidate/nature-writing/SKILL.md'} "
        "and load its manifest, matching fragments, and necessary declared dependencies. "
        f"For the shared robotics examples, first read ONLY lines {common['start_line']}-{common['end_line']} "
        f"of {runtime / frozen['example_loading']['file']} (common instructions and task index). "
        f"Then use the heading/line-number map at {runtime / 'example-read-ranges.json'} to select relevant "
        "cards yourself; read only selected card ranges including their English, analysis, and selection notes. "
        "Do not preload the entire example file or all cards. Source-link definitions may be read separately "
        "on demand. Available other-paper PDFs/extractions may be consulted on demand; their facts do not "
        "add author facts. Follow the Skill's targeted-feedback and internal expression-check requirements. "
        "This is one new independent writing context. Only files inside the current materials directory are "
        "permitted inputs. Do not read outside it, installed skills, the source project, P17 original paper "
        "or extractions, P17 examples or analysis, A06, B01, source locators, evaluations, execution records, "
        "or other outputs. The supplied previous-first-output.md is the only permitted prior output. "
        "Do not browse the internet. Use explicit absolute paths and bounded ranges for material reads so "
        "the actual loading is auditable. Do not change files. Return the complete revised English abstract "
        "and accurate Chinese translation, with necessary author notes outside the abstract."
    )
    cmd = [str(CLI), "exec", "--json", "--ephemeral", "--ignore-user-config", "--skip-git-repo-check",
           "-s", "danger-full-access", "-m", MODEL, "-c", f'model_reasoning_effort="{EFFORT}"',
           "-c", "project_doc_max_bytes=0", "-c", 'web_search="disabled"',
           "-C", str(runtime), "-o", str(dest / "first-output.md"), prompt]
    (dest / "execution-prompt.txt").write_text(prompt, encoding="utf-8")
    save("drafting/execution-command.json", cmd)
    save("drafting/frozen-run.json", {"candidate_commit": COMMIT, "model": MODEL, "reasoning_effort": EFFORT,
         "input_sha256": frozen["materials_files_sha256"], "prompt_sha256": digest(dest / "execution-prompt.txt"),
         "working_directory": str(runtime), "cli_sha256": digest(CLI),
         "cli_version": subprocess.check_output([str(CLI), "--version"]).decode().strip(),
         "runner_sha256": digest(Path(__file__)), "collector_helper_sha256": digest(HELPER_PATH), "attempt": 1})
    started = time.time()
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    with (dest / "events.jsonl").open("wb") as stdout, (dest / "stderr.txt").open("wb") as stderr:
        try:
            result = subprocess.run(cmd, stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr, env=env, timeout=900)
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
    globals_for_helper = HELPER["collect"].__globals__
    globals_for_helper["RECORD"] = RECORD
    HELPER["collect"]()
    frozen_run = json.loads((RECORD / "drafting/frozen-run.json").read_text(encoding="utf-8"))
    assert digest(Path(__file__)) == frozen_run["runner_sha256"]
    assert digest(HELPER_PATH) == frozen_run["collector_helper_sha256"]
    print("Runner and reused collector unchanged; raw events retain selected example ranges")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["prepare", "run", "collect"])
    {"prepare": prepare, "run": run, "collect": collect}[parser.parse_args().action]()
