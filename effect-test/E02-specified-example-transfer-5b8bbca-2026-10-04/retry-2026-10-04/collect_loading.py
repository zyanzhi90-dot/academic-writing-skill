"""Reuse the existing returned-text auditor with only the output directory changed."""
from pathlib import Path
import hashlib
import json

DEST = Path(__file__).resolve().parent
RECORD = DEST.parent
SOURCE = RECORD / "collect_loading.py"
source = SOURCE.read_text(encoding="utf-8")
before = 'dest = RECORD / "drafting"'
after = 'dest = RECORD / "retry-2026-10-04"'
assert source.count(before) == 1
assert not (DEST / "loading-audit.json").exists()
scope = {"__file__": str(SOURCE), "__name__": "__main__"}
exec(compile(source.replace(before, after), str(SOURCE), "exec"), scope)
(DEST / "collector-provenance.json").write_text(json.dumps({
    "original_collector": "../collect_loading.py",
    "original_collector_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    "only_in_memory_change": {"before": before, "after": after},
    "no_original_collector_or_old_audit_modified": True,
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
