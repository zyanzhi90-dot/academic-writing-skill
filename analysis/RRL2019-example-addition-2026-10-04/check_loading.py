"""Read the added example through existing routes without overwriting historical checks."""
from pathlib import Path
import hashlib
import json
import re
import runpy
import shutil
import subprocess
import tempfile
import unicodedata

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
CANDIDATE = ROOT / "skill-candidate"
CHECKER = runpy.run_path(str(ROOT / "analysis/check_candidate_loading.py"))
manifests_at, read_case = CHECKER["manifests_at"], CHECKER["read_case"]
digest = lambda data: hashlib.sha256(data).hexdigest()
example = "nature-shared/core/robotics-writing-examples.md"
text = (CANDIDATE / example).read_text(encoding="utf-8")
old = subprocess.check_output(["git", "show", "15efa72:skill-candidate/" + example], cwd=ROOT).decode("utf-8")
def units(value):
    return {m[1]: m[0] for m in re.finditer(r"^### ([AB]\d{2}).*?(?=^### |^## |\Z)", value, re.M | re.S)}
previous, current = units(old), units(text)
assert len(previous) == 20 and len(current) == 22
assert all(current[key] == value for key, value in previous.items())
source = (RECORD / "local-full-text.txt").read_text(encoding="utf-8")
def normalize(value):
    return " ".join(re.sub(r"-\s*\n\s*", "", unicodedata.normalize("NFKC", value)).split())
quotes = []
for key in ("A08", "B14"):
    for quote in re.findall(r"^> (.*)$", current[key], re.M):
        assert normalize(quote) in normalize(source), key
        quotes.append({"card": key, "sha256": digest(quote.encode("utf-8")), "publisher_text_match": True})
links = dict(re.findall(r"^\[([^\]]+)\]: <\.\./\.\./\.\./(.*?)>$", text, re.M))
assert len(links) == 15
for target in links.values():
    assert (ROOT / target).is_file(), target
assert digest((ROOT / links["RRL2019"]).read_bytes()) == "885f62e07ee4bd37fb0e08bdaa6068fd5e4e473d11e0be239ba8bdd2d8c393db"
changes = subprocess.check_output(["git", "diff", "--name-only", "15efa72", "--", "skill-candidate/"], cwd=ROOT).decode().splitlines()
assert changes == ["skill-candidate/" + example], changes

cases = [
    {"id": "abstract-added-supplement", "sections": ["abstract"], "abstract_references": ["A08"], "paper_type": "algorithmic"},
    {"id": "abstract-zh-to-en", "sections": ["abstract"], "abstract_references": ["A08"], "language": "zh-to-en"},
    {"id": "mixed-abstract-body", "sections": ["abstract", "method"], "abstract_references": ["A08"]},
    {"id": "body-coupled-control", "sections": ["method"]},
    {"id": "nonrobotics-abstract", "sections": ["abstract"], "robotics": False},
]
results = []
with tempfile.TemporaryDirectory(prefix="rrl-example-loading-") as temporary:
    moved = Path(temporary) / "skill-candidate"
    shutil.copytree(CANDIDATE, moved)
    for base in (CANDIDATE, moved):
        manifests = manifests_at(base)
        for skill in ("nature-writing", "nature-polishing"):
            for case in cases:
                request = dict(case)
                if skill == "nature-polishing":
                    request["sections"] = ["methods" if section == "method" else section for section in case["sections"]]
                result = read_case(base, skill, request, manifests[skill][0])
                if result["body_module"]:
                    # The existing checker selects B04 for generic method tasks.
                    # Read B14 as the indexed supplementary passage, without changing routing.
                    actual = units((base / example).read_text(encoding="utf-8"))["B14"]
                    assert actual == current["B14"]
                    result["supplementary_body_card"] = {"card": "B14", "sha256": digest(actual.encode("utf-8"))}
                result["environment"] = "project" if base == CANDIDATE else "moved-candidate-only"
                results.append(result)
        for path in base.rglob("*"):
            if path.is_file():
                path.read_bytes().decode("utf-8")
    literal = str(CANDIDATE / example).replace("'", "''")
    command = "[Console]::OutputEncoding=[System.Text.UTF8Encoding]::new($false); [Console]::Write((Get-Content -LiteralPath '" + literal + "' -Raw -Encoding UTF8))"
    returned = subprocess.check_output(["powershell", "-NoProfile", "-Command", command]).decode("utf-8")
    assert returned.splitlines() == text.splitlines()
    declared = {name: len(item[1]) for name, item in manifests_at(CANDIDATE).items()}
report = {
    "scope": "Example addition after the frozen fd7dbcb first output; no writing generation",
    "current_cards": 22, "all_20_existing_cards_preserved": True,
    "A06_anchor_and_main_reference_roles_preserved": True,
    "modified_candidate_files": changes, "new_quotes": quotes,
    "source_links_resolved": len(links), "declared_paths": declared,
    "strict_utf8_and_actual_powershell_contents_match": True,
    "candidate_only_relocation_reads": True, "cases": results,
    "new_example_effect_pass_claimed": False,
    "candidate_example_sha256": digest((CANDIDATE / example).read_bytes()),
}
(RECORD / "loading-check.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"route_reads": len(results), "declared_paths": declared, "existing_cards_preserved": 20,
                  "new_quotes_verified": len(quotes), "source_links": len(links), "new_effect_claim": False}))
