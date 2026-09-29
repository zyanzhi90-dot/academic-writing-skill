"""Produce anonymous A/B copies after all first-pass outputs are frozen."""

from __future__ import annotations

import json
from pathlib import Path
import random
import shutil

TEST = Path(__file__).resolve().parent
TASKS = ("F1", "D1", "D2", "P1", "P2", "P3")
OUT = TEST / "blind"
if OUT.exists():
    raise SystemExit("Blind copies already exist; refusing to overwrite them")

for task in TASKS:
    for version in ("baseline", "candidate"):
        output = TEST / "runs" / task / version / "first-output.md"
        if not output.is_file() or not output.read_text(encoding="utf-8").strip():
            raise SystemExit(f"Missing output: {output}")

OUT.mkdir()
randomizer = random.SystemRandom()
mapping: dict[str, dict[str, str]] = {}
for task in TASKS:
    versions = ["baseline", "candidate"]
    randomizer.shuffle(versions)
    mapping[task] = dict(zip(("A", "B"), versions))
    for label, version in mapping[task].items():
        shutil.copy2(TEST / "runs" / task / version / "first-output.md", OUT / f"{task}-{label}.md")

(OUT / "mapping.json").write_text(json.dumps(mapping, ensure_ascii=False, indent=2), encoding="utf-8")
print("Created anonymous A/B outputs for all six tasks. Open mapping.json only after writing the anonymous evaluations.")
