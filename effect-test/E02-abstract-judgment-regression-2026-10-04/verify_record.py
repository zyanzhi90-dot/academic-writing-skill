"""Check frozen input identity, history preservation, UTF-8 and record links."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
frozen = json.loads((RECORD / "frozen-materials.json").read_text(encoding="utf-8"))
audit = json.loads((RECORD / "verification.json").read_text(encoding="utf-8"))
retention = json.loads((RECORD / "first-output-retention.json").read_text(encoding="utf-8"))
preflight = json.loads((RECORD / "preflight.json").read_text(encoding="utf-8"))


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


for name, sha in frozen["protected_project_files_sha256"].items():
    assert digest(ROOT / name) == sha, name
for name, sha in frozen["materials_files_sha256"].items():
    assert digest(RECORD / "materials" / name) == sha, name
assert digest(RECORD / "drafting/first-output.md") == audit["first_output_sha256"] == retention["first_output_sha256"]
assert frozen["facts_source"] == "effect-test/E02-abstract-materials-2026-10-03/科学事实包.md"
assert (RECORD / "materials/inputs/scientific-facts.md").read_bytes() == (ROOT / frozen["facts_source"]).read_bytes()
assert all(x["model_read_coverage"]["whole_nonblank_text_returned"] for x in audit["inputs"].values())
allowed = set(preflight["modified_candidate_files"])
for name, sha in frozen["original_candidate_files_sha256"].items():
    raw = subprocess.check_output(["git", "show", frozen["candidate_commit"] + ":" + name], cwd=ROOT)
    assert hashlib.sha256(raw).hexdigest() == sha
    assert (ROOT / name).read_bytes().replace(b"\r\n", b"\n") == raw.replace(b"\r\n", b"\n")
assert set(subprocess.check_output(["git", "diff", preflight["accepted_base_commit"], frozen["candidate_commit"],
                                  "--name-only"], cwd=ROOT).decode().splitlines()) == allowed
utf8 = []
for path in RECORD.rglob("*"):
    if path.is_file() and path.suffix in (".md", ".txt", ".json", ".jsonl", ".py", ".yaml", ".ps1", ".patch"):
        text = path.read_text(encoding="utf-8-sig")
        assert "\ufffd" not in text, path
        utf8.append(path.relative_to(RECORD).as_posix())
for path in (RECORD / "README.md", RECORD / "evaluation.md", RECORD / "change-rationale.md"):
    for linked in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
        assert (path.parent / linked).exists(), (path.name, linked)
for name in ("execute_once.py", "prepare_and_check.py", "audit_first_output.py", "retain_output.py", "verify_record.py", "verify_git_bytes.py"):
    path = RECORD / name
    compile(path.read_text(encoding="utf-8"), str(path), "exec")
report = {"run_kind": "known-E02-autonomous-regression", "new_paper_transfer_evidence": False,
          "first_output_unedited": True, "correct_E02_facts_and_five_inputs_complete": True,
          "declared_three_file_candidate_scope_verified": True,
          "all_protected_project_files_unchanged_since_invocation": len(frozen["protected_project_files_sha256"]),
          "all_frozen_inputs_unchanged": len(frozen["materials_files_sha256"]), "utf8_files_checked": len(utf8),
          "record_links_resolve": True, "scripts_compile": True,
          "effect_verdict": "Partial target behavior; necessary local human corrections remain. See evaluation.md."}
target = RECORD / "record-check.json"
assert not target.exists()
target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"record_check": "passed", "first_output_unedited": True, "utf8_files_checked": len(utf8)}))
