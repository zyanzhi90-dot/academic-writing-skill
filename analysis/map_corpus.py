from __future__ import annotations

import re
from pathlib import Path

READING = Path(r"D:\桌面\正文writing skill\analysis\reading")
heading_re = re.compile(
    r"^(?:[IVX]+\.|[A-Z]\.|\d+(?:\.\d+)*\.?)[ \t]+[A-Z][A-Za-z0-9,;:() /–—-]{3,}$"
)
for path in sorted(READING.glob("P*.txt")):
    print(f"\n### {path.stem}")
    page = 0
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("=== PDF PAGE "):
            page = int(re.search(r"\d+", line).group())
        elif (heading_re.match(line) or line.upper() in {"REFERENCES", "CONCLUSION", "CONCLUSIONS", "APPENDIX"}) and len(line) < 95:
            print(f"{page:>2}: {line}")
