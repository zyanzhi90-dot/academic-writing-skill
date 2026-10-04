"""Check the Abstract-only edit and freeze a Git snapshot without moving main."""
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
BASE = "420b71181a0822a84d3966fe0a4cd2da618bc4ab"
PREVIOUS_CANDIDATE = "7f7631279920a08ef93108c8a23512ccacaff479"
ALLOWED = ["skill-candidate/nature-polishing/static/fragments/section/abstract.md",
           "skill-candidate/nature-writing/references/abstract.md",
           "skill-candidate/nature-writing/static/fragments/section/abstract.md"]
CHECKER = runpy.run_path(str(ROOT / "analysis/check_candidate_loading.py"))


def git(*args, **kwargs):
    return subprocess.check_output(["git", *args], cwd=ROOT, **kwargs)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    assert not (RECORD / "preflight.json").exists(), "Do not overwrite a freeze"
    assert git("rev-parse", "HEAD").decode().strip() == BASE
    assert git("rev-parse", "origin/main").decode().strip() == BASE
    assert git("diff", "--name-only").decode().splitlines() == ALLOWED
    assert not git("diff", "--cached", "--name-only").strip()
    git("diff", "--check")
    word_counts = {}
    for name, marker in ((ALLOWED[0], "## Polishing priorities"),
                         (ALLOWED[2], "## Diagnostics before submitting the draft")):
        old = git("show", BASE + ":" + name).decode("utf-8")
        new_raw = (ROOT / name).read_bytes()
        new = new_raw.decode("utf-8")
        assert not new_raw.startswith(b"\xef\xbb\xbf") and "\ufffd" not in new
        assert new.startswith(old[:old.index(marker)])
        word_counts[name] = {"before": len(old.split()), "after": len(new.split())}
    all_files = git("ls-tree", "-r", "--name-only", BASE, "skill-candidate").decode().splitlines()
    for name in all_files:
        if name not in ALLOWED:
            assert (ROOT / name).read_bytes().replace(b"\r\n", b"\n") == git("show", BASE + ":" + name).replace(b"\r\n", b"\n"), name
    manifests = CHECKER["manifests_at"](ROOT / "skill-candidate")
    case = {"id": "robotics-abstract", "sections": ["abstract"], "language": "zh-to-en",
            "journal": "generic", "abstract_references": ["A07"]}
    reads = [CHECKER["read_case"](ROOT / "skill-candidate", name, case, manifests[name][0])
             for name in ("nature-writing", "nature-polishing")]
    utf8 = [CHECKER["check_powershell_utf8"](ROOT / name) for name in ALLOWED]
    with tempfile.TemporaryDirectory(prefix="abstract-rule-loading-check-") as directory:
        relocated = Path(directory) / "skill-candidate"
        shutil.copytree(ROOT / "skill-candidate", relocated)
        moved = CHECKER["manifests_at"](relocated)
        moved_reads = [CHECKER["read_case"](relocated, name, case, moved[name][0])
                       for name in ("nature-writing", "nature-polishing")]
        assert reads == moved_reads
    with tempfile.TemporaryDirectory(prefix="abstract-candidate-index-") as directory:
        env = os.environ.copy()
        env["GIT_INDEX_FILE"] = str(Path(directory) / "index")
        git("read-tree", BASE, env=env)
        blobs = {}
        for name in ALLOWED:
            blob = git("hash-object", "-w", "--stdin", input=(ROOT / name).read_bytes()).decode().strip()
            blobs[name] = blob
            git("update-index", "--add", "--cacheinfo", "100644", blob, name, env=env)
        tree = git("write-tree", env=env).decode().strip()
        snapshot = git("commit-tree", tree, "-p", BASE,
                       "-m", "Freeze Abstract decision-rule refinement for E02 autonomous regression", env=env).decode().strip()
    for name in ALLOWED:
        assert git("show", snapshot + ":" + name) == (ROOT / name).read_bytes()
    report = {"accepted_base_commit": BASE, "previous_test_candidate_commit": PREVIOUS_CANDIDATE,
              "frozen_candidate_commit": snapshot, "frozen_git_tree": tree,
              "freeze_method": "Private temporary Git index; main and its index unchanged until delivery",
              "modified_candidate_files": ALLOWED, "modified_blobs": blobs,
              "all_other_candidate_files_unchanged": True,
              "examples_shared_expression_routers_and_workflows_unchanged": True,
              "method_opening_and_discussion_authorization_unchanged": True,
              "word_counts": word_counts, "utf8": utf8,
              "git_diff_check_passed": True, "manifest_paths_resolve": True,
              "loading_cases": reads, "relocated_loading_identical": True,
              "effect_verdict": "Not evaluated by loading or format checks"}
    (RECORD / "preflight.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    (RECORD / "candidate-change.patch").write_bytes(git("diff", BASE, "--", *ALLOWED))
    previous = ROOT / "effect-test/E02-autonomous-regression-A06-A07-2026-10-04"
    for name in ("execute_once.py", "verify_git_bytes.py"):
        assert not (RECORD / name).exists()
        (RECORD / name).write_bytes((previous / name).read_bytes())
    (RECORD / "runner-provenance.json").write_text(json.dumps({
        "source_record": previous.relative_to(ROOT).as_posix(),
        "copied_scripts_sha256": {name: sha((RECORD / name).read_bytes()) for name in ("execute_once.py", "verify_git_bytes.py")},
        "source_scripts_reused_byte_identically": True,
        "standard_request_inputs_and_run_parameters_unchanged": True,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"scope_format_utf8_and_loading": "passed", "frozen_candidate_commit": snapshot}))


if __name__ == "__main__":
    main()
