"""Check the two-card edit and freeze a Git snapshot without moving any branch."""
from pathlib import Path
import hashlib
import json
import os
import re
import runpy
import subprocess
import tempfile

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
BASE = "e18c5165c4f57e670da8e66452c8dd1eebdeaf05"
ORIGINAL_CANDIDATE = "5b8bbca46a436f4a3b73cb2cf3bc73984e16471d"
EXAMPLES = "skill-candidate/nature-shared/core/robotics-writing-examples.md"
CHECKER = runpy.run_path(str(ROOT / "analysis/check_candidate_loading.py"))


def git(*args, **kwargs):
    return subprocess.check_output(["git", *args], cwd=ROOT, **kwargs)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    assert not (RECORD / "preflight.json").exists(), "Do not replace a previous freeze"
    assert git("rev-parse", "HEAD").decode().strip() == BASE
    assert git("rev-parse", "origin/main").decode().strip() == BASE
    changed = git("diff", "--name-only").decode("utf-8").splitlines()
    assert changed == [EXAMPLES], changed
    assert not git("diff", "--cached", "--name-only").strip()
    before = git("show", BASE + ":" + EXAMPLES).decode("utf-8")
    raw = (ROOT / EXAMPLES).read_bytes()
    after = raw.decode("utf-8")
    assert not raw.startswith(b"\xef\xbb\xbf") and "\ufffd" not in after
    old_cards, new_cards = CHECKER["cards"](before), CHECKER["cards"](after)
    assert len(old_cards) == len(new_cards) == 20
    for key in old_cards:
        if key not in ("A06", "A07"):
            assert old_cards[key] == new_cards[key], key
    def outside_two_cards(text):
        for key in ("A06", "A07"):
            text = text.replace(CHECKER["cards"](text)[key], f"<unchanged-position-{key}>\n")
        return text
    assert outside_two_cards(before) == outside_two_cards(after)
    quotes = {}
    for key in ("A06", "A07"):
        old, new = old_cards[key], new_cards[key]
        assert old.split("**组织与句法。**")[0] == new.split("**贡献与内容选择。**")[0]
        assert old[old.index("**可迁移实现。**"):] == new[new.index("**可迁移实现。**"):]
        old_quote = next(line for line in old.splitlines() if line.startswith("> "))
        new_quote = next(line for line in new.splitlines() if line.startswith("> "))
        assert old_quote == new_quote
        quotes[key] = {"full_english_quote_unchanged": True, "sha256": sha(new_quote.encode("utf-8"))}
    assert before[:before.index("## 摘要")] == after[:after.index("## 摘要")]
    git("diff", "--check")
    manifests = CHECKER["manifests_at"](ROOT / "skill-candidate")
    case = {"id": "robotics-abstract-A06-A07", "sections": ["abstract"], "language": "zh-to-en",
            "journal": "generic", "abstract_references": ["A07"]}
    reads = [CHECKER["read_case"](ROOT / "skill-candidate", name, case, manifests[name][0])
             for name in ("nature-writing", "nature-polishing")]
    utf8 = CHECKER["check_powershell_utf8"](ROOT / EXAMPLES)
    with tempfile.TemporaryDirectory(prefix="two-card-loading-check-") as directory:
        relocated = Path(directory) / "skill-candidate"
        import shutil
        shutil.copytree(ROOT / "skill-candidate", relocated)
        moved = CHECKER["manifests_at"](relocated)
        relocated_reads = [CHECKER["read_case"](relocated, name, case, moved[name][0])
                           for name in ("nature-writing", "nature-polishing")]
        assert reads == relocated_reads
    # A private temporary Git index captures the exact edit; the main index and branch stay untouched.
    blob = git("hash-object", "-w", "--stdin", input=raw).decode().strip()
    with tempfile.TemporaryDirectory(prefix="candidate-freeze-index-") as directory:
        env = os.environ.copy()
        env["GIT_INDEX_FILE"] = str(Path(directory) / "index")
        git("read-tree", BASE, env=env)
        git("update-index", "--add", "--cacheinfo", "100644", blob, EXAMPLES, env=env)
        tree = git("write-tree", env=env).decode().strip()
        snapshot = git("commit-tree", tree, "-p", BASE,
                       "-m", "Freeze A06 A07 analysis candidate for one E02 autonomous regression", env=env).decode().strip()
    assert git("show", snapshot + ":" + EXAMPLES) == raw
    all_files = git("ls-tree", "-r", "--name-only", BASE, "skill-candidate").decode().splitlines()
    for name in all_files:
        if name != EXAMPLES:
            current = (ROOT / name).read_bytes().replace(b"\r\n", b"\n")
            assert current == git("show", BASE + ":" + name).replace(b"\r\n", b"\n"), name
    report = {
        "accepted_base_commit": BASE, "original_candidate_commit": ORIGINAL_CANDIDATE,
        "frozen_candidate_commit": snapshot, "frozen_git_tree": tree,
        "freeze_method": "Unreferenced commit object from a private index; HEAD, main index and installed skills unchanged",
        "modified_candidate_files": [EXAMPLES], "modified_cards": ["A06", "A07"],
        "scope": "Only the two cards' analysis; source quote, metadata, transfer notes and selection variants unchanged",
        "examples_sha256": sha(raw), "examples_git_blob": blob,
        "full_quotes": quotes, "other_18_cards_unchanged": True,
        "common_language_core_and_reference_division_unchanged": True,
        "all_other_candidate_files_unchanged": True,
        "git_diff_check_passed": True, "utf8": utf8,
        "manifest_paths_resolve": True, "loading_cases": reads,
        "relocated_loading_identical": True,
        "effect_verdict": "Not evaluated by implementation checks",
    }
    (RECORD / "preflight.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (RECORD / "candidate-change.patch").write_bytes(git("diff", BASE, "--", EXAMPLES))
    print(json.dumps({"scope_check": "passed", "utf8_and_loading": "passed", "frozen_candidate_commit": snapshot}))


if __name__ == "__main__":
    main()
