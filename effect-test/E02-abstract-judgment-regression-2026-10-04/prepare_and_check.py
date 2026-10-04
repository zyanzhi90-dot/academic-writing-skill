"""Validate a three-file Abstract edit and freeze its Git snapshot, preserving main."""
from pathlib import Path
import hashlib
import json
import os
import runpy
import shutil
import subprocess
import tempfile

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
BASE = "6ddace481104d6a3de33ddd3fb2e1b890b3cfa33"
ALLOWED = ["skill-candidate/nature-polishing/static/fragments/section/abstract.md",
           "skill-candidate/nature-writing/references/abstract.md",
           "skill-candidate/nature-writing/static/fragments/section/abstract.md"]
CHECKER_PATH = ROOT / "analysis/check_candidate_loading.py"
CHECKER = runpy.run_path(str(CHECKER_PATH))


def git(*args, **kwargs):
    return subprocess.check_output(["git", *args], cwd=ROOT, **kwargs)


assert not (RECORD / "preflight.json").exists()
assert git("rev-parse", "HEAD").decode().strip() == BASE
assert git("rev-parse", "origin/main").decode().strip() == BASE
assert git("diff", "--name-only").decode().splitlines() == ALLOWED
assert not git("diff", "--cached", "--name-only").strip()
git("diff", "--check")
counts = {}
for name in git("ls-tree", "-r", "--name-only", BASE, "skill-candidate").decode().splitlines():
    old = git("show", BASE + ":" + name)
    new = (ROOT / name).read_bytes()
    if name not in ALLOWED:
        assert new.replace(b"\r\n", b"\n") == old.replace(b"\r\n", b"\n"), name
    else:
        text = new.decode("utf-8")
        assert "\ufffd" not in text and not new.startswith(b"\xef\xbb\xbf")
        counts[name] = {"before_words": len(old.decode("utf-8").split()), "after_words": len(text.split())}
manifests = CHECKER["manifests_at"](ROOT / "skill-candidate")
case = {"id": "robotics-abstract-judgment", "sections": ["abstract"], "language": "zh-to-en",
        "journal": "generic", "abstract_references": ["A07", "A08"]}
reads = [CHECKER["read_case"](ROOT / "skill-candidate", name, case, manifests[name][0])
         for name in ("nature-writing", "nature-polishing")]
utf8 = [CHECKER["check_powershell_utf8"](ROOT / name) for name in ALLOWED]
with tempfile.TemporaryDirectory(prefix="abstract-judgment-loading-") as directory:
    relocated = Path(directory) / "skill-candidate"
    shutil.copytree(ROOT / "skill-candidate", relocated)
    moved = CHECKER["manifests_at"](relocated)
    moved_reads = [CHECKER["read_case"](relocated, name, case, moved[name][0])
                   for name in ("nature-writing", "nature-polishing")]
    assert reads == moved_reads
validator = Path("C:/Users/user2/.codex/skills/.system/skill-creator/scripts/quick_validate.py")
validation = []
for name in ("nature-writing", "nature-polishing"):
    result = subprocess.run(["python", "-X", "utf8", str(validator), str(ROOT / "skill-candidate" / name)],
                            capture_output=True, check=True)
    validation.append({"skill": name, "exit_code": result.returncode,
                       "stdout": result.stdout.decode("utf-8"), "stderr": result.stderr.decode("utf-8")})
with tempfile.TemporaryDirectory(prefix="abstract-judgment-freeze-index-") as directory:
    env = os.environ.copy()
    env["GIT_INDEX_FILE"] = str(Path(directory) / "index")
    git("read-tree", BASE, env=env)
    blobs = {}
    for name in ALLOWED:
        blob = git("hash-object", "-w", "--stdin", input=(ROOT / name).read_bytes()).decode().strip()
        blobs[name] = blob
        git("update-index", "--add", "--cacheinfo", "100644", blob, name, env=env)
    tree = git("write-tree", env=env).decode().strip()
    snapshot = git("commit-tree", tree, "-p", BASE, "-m",
                   "Freeze Abstract design rationale and evidence selection for E02 regression", env=env).decode().strip()
for name in ALLOWED:
    assert git("show", snapshot + ":" + name) == (ROOT / name).read_bytes()
report = {"accepted_base_commit": BASE, "frozen_candidate_commit": snapshot, "frozen_git_tree": tree,
          "freeze_method": "Existing temporary-index Git snapshot method; main/index unchanged before final synchronization",
          "modified_candidate_files": ALLOWED, "modified_blobs": blobs, "word_counts": counts,
          "all_other_candidate_files_unchanged": True,
          "examples_expression_core_routers_workflows_and_guarantees_preserved": True,
          "git_diff_check_passed": True, "utf8": utf8, "quick_validate": validation,
          "loading_cases": reads, "relocated_loading_identical": True,
          "checker_source": CHECKER_PATH.relative_to(ROOT).as_posix(),
          "checker_source_sha256": hashlib.sha256(CHECKER_PATH.read_bytes()).hexdigest(),
          "effect_verdict": "Not evaluated by scope, format or static loading"}
(RECORD / "preflight.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(RECORD / "candidate-change.patch").write_bytes(git("diff", BASE, "--", *ALLOWED))
print(json.dumps({"scope_format_utf8_static_loading": "passed", "frozen_candidate_commit": snapshot}))
