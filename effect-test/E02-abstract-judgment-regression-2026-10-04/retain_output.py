"""Save exact byte slices of the single first English abstract and Chinese translation."""
from pathlib import Path
import hashlib
import json
import re

RECORD = Path(__file__).resolve().parent
raw = (RECORD / "drafting/first-output.md").read_bytes()
verification = json.loads((RECORD / "verification.json").read_text(encoding="utf-8"))
assert hashlib.sha256(raw).hexdigest() == verification["first_output_sha256"]
en_header = b"**English abstract**\n\n"
zh_header = "**中文翻译**\n\n".encode("utf-8")
en_start = raw.index(en_header) + len(en_header)
en_end = raw.index(b"\n\n", en_start)
zh_start = raw.index(zh_header) + len(zh_header)
zh_end = raw.index(b"\n\n", zh_start)
for name, data in (("abstract.en.txt", raw[en_start:en_end]), ("abstract.zh.txt", raw[zh_start:zh_end])):
    target = RECORD / name
    assert not target.exists()
    target.write_bytes(data)
result = {"run_kind": "known-E02-autonomous-regression", "new_paper_transfer_evidence": False,
          "first_output_sha256": hashlib.sha256(raw).hexdigest(),
          "english_byte_offsets": [en_start, en_end], "chinese_byte_offsets": [zh_start, zh_end],
          "exact_byte_slices_without_added_newlines": True,
          "english_words": len(raw[en_start:en_end].decode("utf-8").split()),
          "english_sentences": re.split(r"(?<=\.)\s+", raw[en_start:en_end].decode("utf-8")),
          "output_unchanged_before_evaluation": True,
          "classification": "Known-case autonomous first output; effect evaluated separately, no revision made"}
target = RECORD / "first-output-retention.json"
assert not target.exists()
target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"exact_english_and_chinese_slices_saved": True, "words": result["english_words"]}))
