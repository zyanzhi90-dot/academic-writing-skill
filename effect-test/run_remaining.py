"""Run remaining independent first-pass CLI sessions at bounded concurrency."""

from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
PAIRS = [(task, version) for task in ("F1", "D1", "D1v2", "D2", "P1", "P2", "P3") for version in ("baseline", "candidate")]


def run(pair: tuple[str, str]) -> tuple[str, str, int, str]:
    task, version = pair
    if (ROOT / "runs" / task / version).exists():
        return task, version, 0, "already recorded"
    result = subprocess.run(
        [sys.executable, str(ROOT / "run_once.py"), task, version],
        text=True, capture_output=True, cwd=ROOT.parent,
    )
    return task, version, result.returncode, (result.stdout + result.stderr).strip()


with ThreadPoolExecutor(max_workers=2) as pool:
    for future in as_completed([pool.submit(run, pair) for pair in PAIRS]):
        task, version, code, message = future.result()
        print(f"{task}/{version}: {message}", flush=True)
        if code:
            print(f"RUN FAILED: {task}/{version} exit={code}", flush=True)
