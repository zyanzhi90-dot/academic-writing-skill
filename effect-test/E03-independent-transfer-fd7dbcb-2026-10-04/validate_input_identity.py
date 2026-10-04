"""Check case identity and actual returned contents; never invoke a writing model."""
from pathlib import Path
import hashlib
import json
import runpy
import shutil

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
expected = json.loads((RECORD / "coordinator/intended-input-identity.json").read_text(encoding="utf-8"))
frozen = json.loads((RECORD / "frozen-materials.json").read_text(encoding="utf-8"))
digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
source = ROOT / expected["facts_source"]
assert digest(source) == expected["facts_source_sha256"]
actual = RECORD / "materials/inputs/scientific-facts.md"
identity = {
    "intended_case": expected["case"],
    "expected_facts_source": expected["facts_source"],
    "expected_sha256": expected["facts_source_sha256"],
    "actual_frozen_facts_source": frozen["facts_source"],
    "actual_sha256": digest(actual),
    "actual_first_line": actual.read_text(encoding="utf-8").splitlines()[0],
    "expected_first_line": source.read_text(encoding="utf-8").splitlines()[0],
    "source_identity_matches": frozen["facts_source"].replace("\\", "/") == expected["facts_source"].replace("\\", "/"),
    "facts_bytes_match_selected_source": actual.read_bytes() == source.read_bytes(),
}
identity["eligible_as_E03_run"] = identity["source_identity_matches"] and identity["facts_bytes_match_selected_source"]
assert not identity["eligible_as_E03_run"], "This record is the preserved wrong-input invocation"

# Verify the intended four original inputs with the same corrected PowerShell reader.
# These are preparation evidence only, never added to the already running session.
intended = RECORD / "coordinator/intended-inputs"
assert not intended.exists(), "Do not overwrite preparation evidence"
(intended / "inputs").mkdir(parents=True)
for name in ("task.md", "personal-experience.txt", "core-requirements.txt"):
    shutil.copyfile(RECORD / "materials/inputs" / name, intended / "inputs" / name)
shutil.copyfile(source, intended / "inputs/scientific-facts.md")
helper = runpy.run_path(str(RECORD / "execute_once.py"))
returned = helper["read_required_inputs"](intended.resolve(), phase="intended-E03")
assert (intended / "inputs/scientific-facts.md").read_bytes() == source.read_bytes()
identity["intended_input_return_validation"] = returned
identity["intended_inputs_delivered_to_writer"] = False
identity["additional_model_invocations"] = 0
(RECORD / "input-identity-audit.json").write_text(json.dumps(identity, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"actual_run_eligible_as_E03": False, "intended_E03_full_return_verified": True,
                  "additional_model_invocations": 0}))
