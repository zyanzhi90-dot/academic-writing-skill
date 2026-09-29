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
    parser.add_argument("task", choices=["F1", "D1", "D1v2", "D2", "P1", "P2", "P3"])
    parser.add_argument("version", choices=["baseline", "candidate"])
    args = parser.parse_args()

    role = "nature-writing" if args.task in {"F1", "D1", "D1v2", "D2"} else "nature-polishing"
    source = ROOT / f"skill-{args.version}"
    task_path = TEST / "inputs" / f"{args.task}.md"
    dest = TEST / "runs" / args.task / args.version
    if dest.exists():
        raise SystemExit(f"Refusing to replace first-pass output: {dest}")
    dest.mkdir(parents=True)

    prompt = (
        f"Carry out the manuscript task in {task_path} using only the "
        f"specified local skill at {source / role / 'SKILL.md'} and its declared "
        "local dependencies. Read the skill router, manifest, and files it directs "
        "you to load for this task. Do not use any installed skill, other writing "
        "instructions, source papers, evaluator notes, or previous task outputs. "
        "This is an independent first-pass writing run. Do not change files. "
        "Return the requested prose and any notes required by the task."
    )
    cmd = [
        "codex", "exec", "--json", "--ephemeral", "--ignore-user-config",
        "-s", "danger-full-access", "-m", MODEL,
        "-c", f'model_reasoning_effort="{EFFORT}"',
        "-C", str(ROOT), "-o", str(dest / "first-output.md"), prompt,
    ]
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
        "role": role,
        "skill_manifest": (source / role / "manifest.yaml").read_text(encoding="utf-8").split("\n", 5)[:5],
        "skill_sha256": sha256(source / role / "SKILL.md"),
        "shared_sha256": sha256(source / "nature-shared" / "SKILL.md"),
        "task_sha256": sha256(task_path),
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


if __name__ == "__main__":
    main()
