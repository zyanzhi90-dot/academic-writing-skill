from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(r"D:\桌面\正文writing skill")
OUT = ROOT / "analysis" / "reading"
OUT.mkdir(parents=True, exist_ok=True)
inventory = json.loads((ROOT / "analysis" / "inventory.json").read_text(encoding="utf-8"))

for item in inventory:
    result = subprocess.run(
        ["pdftotext", "-raw", "-enc", "UTF-8", item["file"], "-"],
        capture_output=True,
        check=True,
    )
    pages = result.stdout.decode("utf-8", errors="replace").replace("\r\n", "\n").split("\f")
    if not pages[-1].strip():
        pages.pop()
    lines = []
    for page_num, page in enumerate(pages, 1):
        lines.extend([f"=== PDF PAGE {page_num} ===", page.strip(), ""])
    (OUT / f"{item['id']}.txt").write_text("\n".join(lines), encoding="utf-8")
    item["raw_page_chars"] = [len(page.strip()) for page in pages]
    item["raw_pages"] = len(pages)
    item["raw_first_page"] = pages[0][:2400] if pages else ""
    item["raw_last_page"] = pages[-1][-1000:] if pages else ""
    print(item["id"], "pages", len(pages), "chars", sum(item["raw_page_chars"]))

(ROOT / "analysis" / "inventory.json").write_text(
    json.dumps(inventory, ensure_ascii=False, indent=2), encoding="utf-8"
)
