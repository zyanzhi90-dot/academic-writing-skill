"""Run one local, independent first-pass task against a frozen skill path."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
TEST = ROOT / "effect-test"
MODEL = "gpt-6-sol"
EFFORT = "medium"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("task", choices=["F1", "F1-polishing", "D1", "D1v2", "D2", "P1", "P2", "P3"])
    parser.add_argument("version", choices=["baseline", "candidate"])
    parser.add_argument("--run-label", default=None, help="Separate record directory for a retest; never replaces an existing run")
    parser.add_argument("--input-file", type=Path, help="Frozen task input inside this project")
    parser.add_argument("--record-dir", type=Path, help="New record directory under effect-test; never replaces an existing directory")
    parser.add_argument("--allow-source-papers", action="store_true", help="Allow declared, on-demand local corpus lookups")
    parser.add_argument("--cli", default="codex", help="Installed CLI executable, including its native Windows entry point")
    args = parser.parse_args()

    role = "nature-writing" if args.task in {"F1", "D1", "D1v2", "D2"} else "nature-polishing"
    source = ROOT / f"skill-{args.version}"
    task_path = (args.input_file or TEST / "inputs" / f"{args.task}.md").resolve()
    if not task_path.is_relative_to(ROOT) or not task_path.is_file():
        parser.error("task input must be an existing file inside the project")
    run_label = args.run_label or args.version
    if Path(run_label).name != run_label or run_label in {".", ".."}:
        parser.error("run label must be a single directory name")
    dest = (args.record_dir or TEST / "runs" / args.task / run_label).resolve()
    if not dest.is_relative_to(TEST) or dest == TEST:
        parser.error("record directory must be below effect-test")
    if dest.exists():
        raise SystemExit(f"Refusing to replace first-pass output: {dest}")
    dest.mkdir(parents=True)

    resource_rules = (
        "You may consult the local source papers and extraction texts under "
        f"{ROOT / '文献资料'}, {ROOT / 'analysis' / 'reading'}, and "
        f"{ROOT / 'analysis' / 'extracted'} on demand as directed by the skill's "
        "declared references. Source scientific content does not add author facts. "
        "Do not read installed skills, other writing instructions, evaluator notes, "
        "diagnostics, or previous task outputs outside the supplied frozen input. "
        if args.allow_source_papers else
        "Do not use any installed skill, other writing instructions, source papers, "
        "evaluator notes, or previous task outputs. "
    )
    prompt = (
        f"Carry out the manuscript task in {task_path} using only the "
        f"specified local skill at {source / role / 'SKILL.md'} and its declared "
        "local dependencies. Read the skill router, manifest, and files it directs "
        "you to load for this task. " + resource_rules +
        "This is an independent first-pass writing run. Do not change files. "
        "Return the requested prose and any notes required by the task."
    )
    cmd = [
        args.cli, "exec", "--json", "--ephemeral", "--ignore-user-config",
        "-s", "danger-full-access", "-m", MODEL,
        "-c", f'model_reasoning_effort="{EFFORT}"',
        "-C", str(ROOT), "-o", str(dest / "first-output.md"), prompt,
    ]
    (dest / "execution-prompt.txt").write_text(prompt, encoding="utf-8")
    (dest / "execution-command.json").write_text(json.dumps(cmd, ensure_ascii=False, indent=2), encoding="utf-8")
    task_digest = sha256(task_path)
    (dest / "frozen-run.json").write_text(json.dumps({
        "task": args.task, "role": role, "model": MODEL, "reasoning_effort": EFFORT,
        "input": str(task_path), "input_sha256": task_digest,
        "prompt_sha256": sha256(dest / "execution-prompt.txt"),
        "allow_source_papers": args.allow_source_papers,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    started = time.time()
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    with (dest / "events.jsonl").open("wb") as stdout, (dest / "stderr.txt").open("wb") as stderr:
        try:
            result = subprocess.run(cmd, stdout=stdout, stderr=stderr, env=env, timeout=900)
            exit_code = result.returncode
        except subprocess.TimeoutExpired:
            exit_code = 124
    meta = {
        "task": args.task,
        "version": args.version,
        "run_label": run_label,
        "role": role,
        "skill_manifest": (source / role / "manifest.yaml").read_text(encoding="utf-8").split("\n", 5)[:5],
        "skill_sha256": sha256(source / role / "SKILL.md"),
        "shared_sha256": sha256(source / "nature-shared" / "SKILL.md"),
        "task_sha256": task_digest,
        "task_unchanged": sha256(task_path) == task_digest,
        "allow_source_papers": args.allow_source_papers,
        "cli_executable": args.cli,
        "model": MODEL,
        "reasoning_effort": EFFORT,
        "cli_arguments": cmd[1:9] + ["-c", f'model_reasoning_effort="{EFFORT}"', "-C", "<project-root>", "-o", "<first-output.md>", "<prompt>"],
        "working_directory": str(ROOT),
        "prompt": prompt,
        "exit_code": exit_code,
        "duration_seconds": round(time.time() - started, 2),
        "first_output_exists": (dest / "first-output.md").exists(),
    }
    (dest / "run-meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{args.task}/{args.version}: exit={exit_code}, seconds={meta['duration_seconds']}, output={meta['first_output_exists']}")
    if exit_code:
        raise SystemExit(exit_code)
    if not meta["task_unchanged"]:
        raise SystemExit("Frozen task input changed during execution")


if __name__ == "__main__":
    main()
