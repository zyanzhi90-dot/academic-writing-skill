"""Check final local edits, UTF-8, loaded dependencies and preserved history."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
frozen = json.loads((RECORD / "frozen-materials.json").read_text(encoding="utf-8"))
audit = json.loads((RECORD / "verification.json").read_text(encoding="utf-8"))
edits = json.loads((RECORD / "delivery-edits.json").read_text(encoding="utf-8"))


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


raw = (RECORD / "drafting/first-output.md").read_text(encoding="utf-8")
en = raw.split("**English abstract**\n\n", 1)[1].split("\n\n", 1)[0]
zh = raw.split("**中文翻译**\n\n", 1)[1].split("\n\n", 1)[0]
for edit in edits["delivery_check_local_edits"]:
    en = en.replace(edit["english_before"], edit["english_after"])
    zh = zh.replace(edit["chinese_before"], edit["chinese_after"])
assert en == (RECORD / "abstract.en.txt").read_text(encoding="utf-8")
assert zh == (RECORD / "abstract.zh.txt").read_text(encoding="utf-8")
delivery = (RECORD / "feedback-revision.md").read_text(encoding="utf-8")
assert en in delivery and zh in delivery
assert digest(RECORD / "drafting/first-output.md") == audit["output_sha256"] == edits["raw_model_revision_sha256"]
assert not edits["autonomous_pass"] and not edits["transfer_pass"]
required = [
    "skill-candidate/nature-writing/SKILL.md", "skill-candidate/nature-writing/manifest.yaml",
    *["skill-candidate/nature-shared/core/" + n + ".md" for n in
      ("reader-workflow", "paper-type-taxonomy", "ethics", "terminology-ledger", "scientific-expression")],
    *["skill-candidate/nature-writing/static/core/" + n + ".md" for n in ("stance", "workflow", "output-format")],
    *["skill-candidate/nature-writing/static/fragments/" + n + ".md" for n in
      ("task/manuscript", "paper_type/methods", "section/abstract", "language/zh-to-en", "language/en", "journal/generic")],
    "skill-candidate/nature-writing/references/abstract.md",
]
assert all(audit["actual_content_coverage"][name]["whole_nonblank_text_returned"] for name in required)
for name, sha in frozen["protected_project_files_sha256"].items():
    assert digest(ROOT / name) == sha, name
for name, sha in frozen["materials_files_sha256"].items():
    assert digest(RECORD / "materials" / name) == sha, name
utf8 = []
for path in RECORD.rglob("*"):
    if path.is_file() and path.suffix in (".md", ".txt", ".json", ".jsonl", ".py", ".yaml", ".ps1"):
        text = path.read_text(encoding="utf-8-sig")
        assert "\ufffd" not in text, path
        utf8.append(path.relative_to(RECORD).as_posix())
for path in (RECORD / "feedback-revision.md", RECORD / "revision-basis.md", RECORD / "README.md",
             ROOT / "effect-test/E03-independent-transfer-fd7dbcb-valid-2026-10-04/owner-acceptance-addendum-2026-10-04.md"):
    for linked in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
        assert (path.parent / linked).exists(), (path.name, linked)
assert not subprocess.check_output(["git", "diff", "--name-only", "--", "skill-candidate"], cwd=ROOT)
result = {"run_kind": "人工反馈修订", "autonomous_pass": False, "transfer_pass": False,
          "final_english_words": len(en.split()), "final_sentences": re.split(r"(?<=\.)\s+", en),
          "only_declared_two_delivery_edits": True, "raw_model_revision_unchanged": True,
          "original_first_draft_and_historical_evaluation_unchanged": True,
          "candidate_and_installed_skills_unchanged": True, "required_loaded_files_complete": required,
          "utf8_files_checked": len(utf8), "delivery_links_resolve": True,
          "effect_classification": "Human feedback revision pending owner acceptance, not autonomous evidence"}
target = RECORD / "delivery-check.json"
assert not target.exists()
target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"delivery_check": "passed", "english_words": len(en.split()), "utf8_files_checked": len(utf8), "skill_changed": False}))
