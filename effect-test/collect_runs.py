"""Extract the files actually read in each independent writing session."""

from __future__ import annotations

import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "effect-test" / "runs"
LITERAL_RE = re.compile(r"Get-Content\s+(?:-LiteralPath|-Path)\s+'([^']+)'", re.I)


for meta_path in sorted(RUNS.glob("*/*/run-meta.json")):
    run_dir = meta_path.parent
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    reads: list[str] = []
    for line in (run_dir / "events.jsonl").read_text(encoding="utf-8").splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        item = event.get("item") or {}
        if event.get("type") != "item.completed" or item.get("type") != "command_execution":
            continue
        if item.get("exit_code") != 0 or not item.get("aggregated_output"):
            continue
        command = item.get("command", "")
        if "Get-Content" not in command and "type " not in command:
            continue
        for value in LITERAL_RE.findall(command):
            path = Path(value)
            if not path.is_absolute():
                if value.startswith("skill-") or value.startswith("effect-test/"):
                    path = ROOT / path
                else:
                    path = ROOT / f"skill-{meta['version']}" / meta["role"] / path
            try:
                relative = path.resolve().relative_to(ROOT)
            except ValueError:
                continue
            name = relative.as_posix()
            if name.startswith(f"skill-{meta['version']}/") and path.is_file() and name not in reads:
                reads.append(name)
    result = {
        "task": meta["task"],
        "version": meta["version"],
        "model": meta["model"],
        "reasoning_effort": meta["reasoning_effort"],
        "task_sha256": meta["task_sha256"],
        "loaded_files": reads,
        "loaded_robotics_module": any(p.endswith("core/robotics-main-text.md") for p in reads),
        "nonempty_first_output": (run_dir / "first-output.md").exists() and bool((run_dir / "first-output.md").read_text(encoding="utf-8").strip()),
    }
    (run_dir / "loaded-files.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{meta['task']}/{meta['version']}: {len(reads)} files, robotics={result['loaded_robotics_module']}, output={result['nonempty_first_output']}")
