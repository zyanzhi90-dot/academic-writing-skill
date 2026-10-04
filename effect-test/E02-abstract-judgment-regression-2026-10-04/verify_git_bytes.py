"""Verify published record blobs preserve runtime bytes; leave the worktree unchanged."""
from pathlib import Path
import hashlib
import json
import subprocess

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
prefix = RECORD.relative_to(ROOT).as_posix() + "/"
entries = []
for item in subprocess.check_output(["git", "ls-tree", "-r", "-z", "HEAD", prefix], cwd=ROOT).split(b"\0"):
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
    assert output[offset:offset + length] == (ROOT / name).read_bytes(), name
    offset += length + 1
frozen = json.loads((RECORD / "frozen-materials.json").read_text(encoding="utf-8"))
for name, sha in frozen["materials_files_sha256"].items():
    assert hashlib.sha256((RECORD / "materials" / name).read_bytes()).hexdigest() == sha, name
audit = json.loads((RECORD / "verification.json").read_text(encoding="utf-8"))
assert hashlib.sha256((RECORD / "drafting/first-output.md").read_bytes()).hexdigest() == audit["first_output_sha256"]
print(json.dumps({"committed_record_files_byte_identical": len(entries),
                  "frozen_inputs_preserved": len(frozen["materials_files_sha256"]), "first_output_unedited": True}))
