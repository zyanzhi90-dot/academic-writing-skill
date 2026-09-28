from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

paper, query = sys.argv[1], sys.argv[2]
path = Path(r"D:\桌面\正文writing skill\analysis\reading") / f"{paper}.txt"
raw = path.read_text(encoding="utf-8")
for chunk in re.split(r"(?==== PDF PAGE \d+ ===)", raw):
    match = re.search(r"=== PDF PAGE (\d+) ===", chunk)
    if not match:
        continue
    clean = re.sub(r"-\s+([a-z])", r"\1", chunk)
    clean = re.sub(r"\s+", " ", clean)
    pos = clean.casefold().find(query.casefold())
    if pos >= 0:
        print(f"{paper} PDF p.{match.group(1)} | {query}")
        print(clean[max(0, pos - 230) : pos + len(query) + 850])
