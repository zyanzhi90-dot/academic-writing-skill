"""Reuse the verified source-return auditor for this new feedback record."""
from pathlib import Path
import hashlib
import json

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
SOURCE = ROOT / "effect-test/E02-specified-example-transfer-5b8bbca-2026-10-04/collect_loading.py"
assert not (RECORD / "drafting/loading-audit.json").exists()
scope = {"__file__": str(Path(__file__)), "__name__": "__main__"}
exec(compile(SOURCE.read_text(encoding="utf-8"), str(SOURCE), "exec"), scope)
(RECORD / "collector-provenance.json").write_text(json.dumps({
    "source": SOURCE.relative_to(ROOT).as_posix(),
    "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    "only_context_change": "__file__ resolves RECORD to new feedback record; auditor source unchanged",
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
