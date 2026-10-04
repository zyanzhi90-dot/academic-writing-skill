"""Reuse the established single-run collector; only adapt freeze, core input and corpus reuse."""
from pathlib import Path
import hashlib
import json

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
SOURCE = ROOT / "effect-test/E02-abstract-autonomous-regression-2026-10-04/execute_once.py"
text = SOURCE.read_text(encoding="utf-8")
changes = []


def replace(old, new):
    global text
    assert text.count(old) == 1, old
    text = text.replace(old, new)
    changes.append({"old": old, "new": new})


replace('COMMIT = "5b8bbca46a436f4a3b73cb2cf3bc73984e16471d"',
        'COMMIT = json.loads((RECORD / "preflight.json").read_text(encoding="utf-8"))["frozen_candidate_commit"]')
replace('    inputs = materials / "inputs"',
        '    previous_record = ROOT / "effect-test/E02-abstract-autonomous-regression-2026-10-04"\n'
        '    previous_frozen = json.loads((previous_record / "frozen-materials.json").read_text(encoding="utf-8"))\n'
        '    prior_sources = {item["path"]: item for item in previous_frozen["corpus_sources"]}\n'
        '    prior_extractions = {item["pdf"]: item for item in previous_frozen["corpus_extraction"]["papers"]}\n'
        '    inputs = materials / "inputs"')
replace('    (inputs / "personal-experience.txt").write_bytes((ROOT / EXPERIENCE).read_bytes())',
        '    (inputs / "personal-experience.txt").write_bytes((ROOT / EXPERIENCE).read_bytes())\n'
        '    (inputs / "core-requirements.txt").write_bytes((ROOT / "\\u6838\\u5fc3\\u8981\\u6c42.txt").read_bytes())')
start = text.index('        # Extract only current PDFs;')
end = text.index('        corpus.append({"paper_id": paper_id, "path": text_relative.as_posix()', start)
replace(text[start:end],
        '        # Reuse the already verified PDF extraction, checking both its PDF and text hashes.\n'
        '        previous = prior_extractions[relative.as_posix()]\n'
        '        assert previous["pdf_sha256"] == digest(paper)\n'
        '        text_relative = Path(previous["text"])\n'
        '        previous_text = previous_record / "materials" / text_relative\n'
        '        assert digest(previous_text) == previous["text_sha256"] == prior_sources[text_relative.as_posix()]["sha256"]\n'
        '        text_target = materials / text_relative\n'
        '        text_target.parent.mkdir(parents=True, exist_ok=True)\n'
        '        text_target.write_bytes(previous_text.read_bytes())\n')
replace('"pages": len(pages), "pdf_sha256": digest(paper),',
        '"pages": previous["pages"], "pdf_sha256": digest(paper),')
replace('"stderr": result.stderr.decode("utf-8", errors="replace")})',
        '"stderr": previous["stderr"], "reused_verified_text": True})')
replace('"total_pdf_count": len(papers), "fresh_text_count": len(extractions),',
        '"total_pdf_count": len(papers), "reused_verified_text_count": len(extractions),')
replace('"method": "pdftotext -raw -enc UTF-8; page markers; no prose rewriting",',
        '"method": "Reuse byte-verified prior pdftotext -raw -enc UTF-8 texts with page markers; no prose rewriting",\n'
        '                              "reuse_source_record": previous_record.relative_to(ROOT).as_posix(),')
replace('        f"{runtime / \'inputs/personal-experience.txt\'}. Invoke only the frozen local nature-writing at "',
        '        f"{runtime / \'inputs/personal-experience.txt\'} and core requirements at "\n'
        '        f"{runtime / \'inputs/core-requirements.txt\'}. Invoke only the frozen local nature-writing at "')
replace('and their corresponding freshly extracted texts in this ', 'and their corresponding verified extracted texts in this ')
replace('Reference science does not add author facts. This is one autonomous first-pass regression on the known E02 materials in a fresh context, not a new-paper transfer test. ',
        'Reference science does not add author facts. ')
target = RECORD / "execute_once.py"
assert not target.exists(), "Do not replace a prepared runner"
target.write_text(text, encoding="utf-8")
(RECORD / "runner-adaptation.json").write_text(json.dumps({
    "source": SOURCE.relative_to(ROOT).as_posix(),
    "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    "changes": changes,
    "single_invocation_and_collection_implementation_retained": True,
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("Created auditable single-run adapter; no model invoked")
