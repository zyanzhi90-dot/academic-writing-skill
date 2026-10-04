"""Read-only check that every committed record blob preserves the actual file bytes."""
from pathlib import Path
import hashlib
import json
import subprocess

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
PREFIX = RECORD.relative_to(ROOT).as_posix() + "/"
entries = []
for item in subprocess.check_output(["git", "ls-tree", "-r", "-z", "HEAD", PREFIX], cwd=ROOT).split(b"\0"):
    if item:
        meta, name = item.split(b"\t", 1)
        entries.append((meta.split()[2], name.decode("utf-8")))
output = subprocess.check_output(["git", "cat-file", "--batch"], cwd=ROOT,
                                 input=b"\n".join(item[0] for item in entries) + b"\n")
offset = 0
for blob, name in entries:
    end = output.index(b"\n", offset)
    length = int(output[offset:end].split()[-1])
    offset = end + 1
    data = output[offset:offset + length]
    offset += length + 1
    assert data == (ROOT / name).read_bytes(), name
frozen = json.loads((RECORD / "frozen-materials.json").read_text(encoding="utf-8"))
for name, expected in frozen["materials_files_sha256"].items():
    assert hashlib.sha256((RECORD / "materials" / name).read_bytes()).hexdigest() == expected, name
verification = json.loads((RECORD / "verification.json").read_text(encoding="utf-8"))
assert hashlib.sha256((RECORD / "drafting/first-output.md").read_bytes()).hexdigest() == verification["first_output_sha256"]
print(json.dumps({"committed_record_files_byte_identical": len(entries),
                  "all_152_frozen_input_files_match_manifest": True,
                  "first_output_bytes_unchanged": True}))
