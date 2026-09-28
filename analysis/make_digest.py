from __future__ import annotations

import re
from pathlib import Path

READING = Path(r"D:\桌面\正文writing skill\analysis\reading")
OUT = Path(r"D:\桌面\正文writing skill\analysis\digests")
OUT.mkdir(exist_ok=True)
main_re = re.compile(r"^(?:[IVX]+\.\s+[A-Z][A-Z /–—-]{3,}|\d+\.\s+[A-Z][A-Za-z /–—-]{3,}|REFERENCES|References)$")
sub_re = re.compile(r"^(?:[A-Z]\.\s+[A-Z][A-Za-z /–—-]{3,}|\d+\.\d+(?:\.\d+)?\.\s+[A-Z][A-Za-z /–—-]{3,})$")
for path in sorted(READING.glob("P*.txt")):
    lines = path.read_text(encoding="utf-8").splitlines()
    heads = []
    page = 0
    for index, line in enumerate(lines):
        l = line.strip()
        if l.startswith("=== PDF PAGE "):
            page = int(re.search(r"\d+", l).group())
        elif main_re.fullmatch(l) and len(l) < 86:
            heads.append((index, page, l))
    out = [f"# {path.stem}"]
    for head_i, (start, page, title) in enumerate(heads):
        if "REFERENCES" in title.upper():
            break
        end = heads[head_i + 1][0] if head_i + 1 < len(heads) else len(lines)
        segment = lines[start + 1 : end]
        subs = [line.strip() for line in segment if sub_re.fullmatch(line.strip()) and len(line.strip()) < 85]
        joined = " ".join(segment)
        joined = re.sub(r"-\s+([a-z])", r"\1", joined)
        joined = re.sub(r"\s+", " ", joined)
        out.extend([f"\n## {title} [PDF p.{page}]", "Subsections: " + "; ".join(subs[:18]), "OPEN: " + joined[:340], "CLOSE: " + joined[-180:]])
    (OUT / f"{path.stem}.md").write_text("\n".join(out), encoding="utf-8")
