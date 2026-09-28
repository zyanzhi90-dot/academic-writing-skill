from __future__ import annotations

import json
import re
from pathlib import Path

import pymupdf

ROOT = Path(r"D:\桌面\正文writing skill")
SOURCE = ROOT / "文献资料"
OUT = ROOT / "analysis" / "extracted"
OUT.mkdir(parents=True, exist_ok=True)

inventory = []
for index, pdf in enumerate(sorted(SOURCE.glob("*.pdf")), start=1):
    doc = pymupdf.open(pdf)
    pages = [page.get_text("text", sort=True) for page in doc]
    normalized = [re.sub(r"\s+", " ", page).strip() for page in pages]
    body = "\n\n".join(f"=== PDF PAGE {i + 1} ===\n{page}" for i, page in enumerate(pages))
    (OUT / f"P{index:02d}.txt").write_text(body, encoding="utf-8")
    inventory.append({
        "id": f"P{index:02d}",
        "file": str(pdf),
        "pages": len(doc),
        "page_chars": [len(page.strip()) for page in pages],
        "text_chars": sum(len(page.strip()) for page in pages),
        "first_page": normalized[0][:2200] if normalized else "",
        "last_page": normalized[-1][:500] if normalized else "",
        "pdf_metadata": doc.metadata,
    })

(ROOT / "analysis" / "inventory.json").write_text(
    json.dumps(inventory, ensure_ascii=False, indent=2), encoding="utf-8"
)
for item in inventory:
    print(f"{item['id']} | {item['pages']}p | {item['text_chars']} chars | min={min(item['page_chars'])} | {Path(item['file']).name}")
