"""Introduction-only evidence and static checks; never invokes a writing model."""
from pathlib import Path
import hashlib
import json
import re
import runpy
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]
DEST = Path(__file__).resolve().parent
BASE = "025528f5c5621e14631f9abd61fa9b5021624b72"
RECORD = ROOT / "effect-test/E04-introduction-delivery-22cc2ca-2026-10-07"
CHANGED = [
    "skill-candidate/nature-shared/core/robotics-introduction-examples.md",
    "skill-candidate/nature-polishing/static/fragments/section/intro.md",
]
AUTHORS = ["核心要求.txt", "我自己的经验和做法.txt", "引言写作方法.txt",
           "current-author-adjustment.txt"]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(name, value):
    (DEST / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def unit(text, anchor):
    start = text.index(f'<a id="{anchor}"></a>')
    end = text.find('<a id="', start + 1)
    return text[start:end if end >= 0 else len(text)]


def main():
    assert git("rev-parse", "HEAD").decode().strip() == BASE, "Run before synchronization"
    inputs = DEST / "inputs"
    inputs.mkdir(exist_ok=True)
    for name in AUTHORS:
        target = inputs / name
        if not target.exists():
            shutil.copyfile(ROOT / name, target)
        assert sha(target) == sha(ROOT / name), (name, "Current author input changed")
    override = DEST / "current-author-adjustment.txt"
    if not override.exists():
        shutil.copyfile(ROOT / "current-author-adjustment.txt", override)
    assert sha(override) == sha(inputs / override.name)
    tracked = git("ls-tree", "-r", "--name-only", "-z", BASE).decode("utf-8").split("\0")
    protected = {p: sha(ROOT / p) for p in tracked if p and p not in CHANGED}
    protected_snapshot = {"files": len(protected), "sha256": hashlib.sha256(
        json.dumps(protected, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest(),
        "scope": "All files tracked at base_commit except the two changed Introduction candidate files"}
    protected_path = DEST / "protected-snapshot.json"
    if not protected_path.exists():
        write(protected_path.name, protected_snapshot)
    assert protected_snapshot == json.loads(protected_path.read_text(encoding="utf-8"))
    actual_changed = git("diff", "--name-only", BASE).decode("utf-8").splitlines()
    assert sorted(actual_changed) == sorted(CHANGED), actual_changed
    evidence = {"base_commit": BASE, "current_root_author_sha256": {p: sha(ROOT / p) for p in AUTHORS},
                "author_override_copied_to_record_and_inputs": True, "historical_requirements": "audit only",
                "stages": {}}
    for stage in ("drafting", "polishing"):
        folder = RECORD / stage
        events = [json.loads(s) for s in (folder / "events.jsonl").read_text(encoding="utf-8").splitlines()]
        commands = [e["item"] for e in events if e.get("type") == "item.completed"
                    and e.get("item", {}).get("type") == "command_execution"]
        messages = [e["item"] for e in events if e.get("type") == "item.completed"
                    and e.get("item", {}).get("type") == "agent_message"]
        returns = {}
        files = ["core/scientific-expression.md", "core/robotics-introduction-examples.md",
                 "core/robotics-introduction-section.md", "core/robotics-introduction-paragraphs.md",
                 "core/robotics-introduction-expression.md"]
        for relative in files:
            path = folder / "materials/skill-candidate/nature-shared" / relative
            lines = path.read_text(encoding="utf-8").splitlines()
            seen = set()
            witnesses = []
            for command in commands:
                if path.name not in command.get("command", ""):
                    continue
                exact = []
                for line in command.get("aggregated_output", "").splitlines():
                    match = re.fullmatch(r"(\d+): (.*)", line)
                    if match:
                        n = int(match[1])
                        if 0 < n <= len(lines) and match[2] == lines[n-1]:
                            seen.add(n)
                            exact.append(n)
                witnesses.append({"event_id": command["id"], "exact_lines": exact})
            anchors = [(i, re.fullmatch(r'<a id="([^"]+)"></a>', line)[1])
                       for i, line in enumerate(lines, 1) if re.fullmatch(r'<a id="([^"]+)"></a>', line)]
            coverage = {}
            for i, (start, anchor) in enumerate(anchors):
                end = anchors[i+1][0]-1 if i+1 < len(anchors) else len(lines)
                english = [n for n in range(start, end+1) if lines[n-1].startswith("> ")]
                coverage[anchor] = {"english_lines": english, "all_english_returned": bool(english) and all(n in seen for n in english)}
            returns[relative] = {"sha256": sha(path), "command_witnesses": witnesses,
                                 "all_nonempty_lines_returned": all(i in seen for i, s in enumerate(lines, 1) if s),
                                 "unit_english_coverage": coverage}
        audit = json.loads((folder / "audit.json").read_text(encoding="utf-8"))
        identity = json.loads((folder / "pre-invocation-identity.json").read_text(encoding="utf-8"))
        prompt = (folder / "execution-prompt.txt").read_text(encoding="utf-8")
        b03 = next(s for s in (RECORD / "background-facts.md").read_text(encoding="utf-8").splitlines() if s.startswith("B03："))
        assert b03 in prompt, "Original scientific division missing from prompt"
        assert audit["attempts"] == 1 and audit["model"] == "gpt-6.1-sol" and audit["reasoning_effort"] == "high"
        assert sha(folder / "first-output.md") == audit["first_output_sha256"]
        evidence["stages"][stage] = {
            "attempts": audit["attempts"], "model": audit["model"], "effort": audit["reasoning_effort"],
            "events_sha256": sha(folder / "events.jsonl"), "prompt_sha256": sha(folder / "execution-prompt.txt"),
            "first_output_sha256": sha(folder / "first-output.md"),
            "english_sha256": sha(folder / "first-introduction.en.txt"),
            "identity_flags": {k: identity[k] for k in ("identity_verified", "candidate_git_bytes_verified", "actual_complete_returns_verified", "no_coordinator_evaluation_supplied")},
            "original_B03_present_in_initial_prompt": b03,
            "explicit_scientific_fact_reopen_event_ids": [c["id"] for c in commands if any(n in c.get("command", "") for n in ("background-facts.md", "scientific-facts.md", "citation-facts.md"))],
            "execution_messages_before_final": [{"id": m["id"], "text": m["text"]} for m in messages if len(m["text"]) < 4000],
            "actual_returns_recomputed_from_raw_events": returns,
            "limits": "Exact returns prove loading only; initial science was supplied in full. No inference about private reasoning or reliable adoption.",
        }
    provenance = json.loads((ROOT / "analysis/introduction-section-review-2026-10-06/source-provenance.json").read_text(encoding="utf-8"))
    source_units = {"P17": ["I04", "I05", "I06", "I07"], "P05": ["I02", "I07"],
                    "Fuzzy2023": ["I02", "I03"], "ESO2017": ["I07", "I08"]}
    sources = {}
    for label, headings in source_units.items():
        item = provenance["papers"][label]
        pdf = ROOT / item["pdf"]
        assert sha(pdf) == item["pdf_sha256"]
        original = ROOT / f"analysis/introduction-section-review-2026-10-06/{label}-introduction.md"
        text = original.read_text(encoding="utf-8")
        paragraphs = {}
        for heading in headings:
            match = re.search(r"^## " + heading + r"\n(.*?)(?=^## |\Z)", text, re.M | re.S)
            assert match, (label, heading)
            paragraphs[heading] = match[1].strip()
        sources[label] = {"pdf": item["pdf"], "current_pdf_sha256": sha(pdf),
                          "matches_prior_pdf_provenance": True, "original_reading": original.relative_to(ROOT).as_posix(),
                          "original_reading_sha256": sha(original), "complete_applicable_publication_paragraphs": paragraphs}
    evidence["sources"] = sources
    write("evidence.json", evidence)
    # Import definitions only; do not run old checkers or rewrite their records.
    helper = runpy.run_path(str(ROOT / "analysis/check_candidate_loading.py"))
    paths = helper["manifests_at"](ROOT / "skill-candidate")
    routes = []
    with tempfile.TemporaryDirectory(prefix="introduction-static-") as temp:
        detached = Path(temp) / "skills"
        shutil.copytree(ROOT / "skill-candidate", detached)
        helper["manifests_at"](detached)
        for base in (ROOT / "skill-candidate", detached):
            for name in ("nature-writing", "nature-polishing"):
                package = base / name
                manifest = paths[name][0]
                fragment = package / manifest["axes"]["section"]["values"]["intro"]
                index = (package / "../nature-shared/core/robotics-introduction-examples.md").resolve()
                read = [package / "SKILL.md", package / "manifest.yaml", fragment, index]
                axes = {"paper_type": "algorithmic", "language": "en", "journal": "generic"}
                if name == "nature-writing":
                    axes["task"] = "manuscript"
                read.extend(package / manifest["axes"][axis]["values"][value] for axis, value in axes.items())
                read.extend((package / p).resolve() for p in manifest["always_load"])
                for p in read:
                    assert p.is_file() and p.read_text(encoding="utf-8")
                assert "../nature-shared/core/robotics-introduction-examples.md" in fragment.read_text(encoding="utf-8")
                assert any(p["path"] == "../nature-shared/core/robotics-introduction-examples.md" for p in manifest["references"]["on_demand"])
                links = re.findall(r"\]\((robotics-introduction-[^)]+)\)", index.read_text(encoding="utf-8"))
                for link in links:
                    file, _, anchor = link.partition("#")
                    resource = index.parent / file
                    content = resource.read_text(encoding="utf-8")
                    assert f'<a id="{anchor}"></a>' in content, link
                selected = [("robotics-introduction-paragraphs.md", a) for a in ("p17-i04", "p17-i05", "fuzzy-i02", "fuzzy-i03")]
                selected += [("robotics-introduction-expression.md", a) for a in ("e19", "e22")]
                units = [{"file": f, "anchor": a, "sha256": hashlib.sha256(unit((index.parent / f).read_text(encoding="utf-8"), a).encode()).hexdigest()} for f, a in selected]
                routes.append({"location": "project" if base == ROOT / "skill-candidate" else "detached candidate only", "skill": name,
                               "read_files": [p.relative_to(base.resolve()).as_posix() for p in read], "index_link_count": len(links), "selected_units_read": units})
        assert not (detached.parent / "analysis").exists()
    validation = {}
    validator = Path("C:/Users/user/.codex/skills/.system/skill-creator/scripts/quick_validate.py")
    for name in ("nature-writing", "nature-polishing", "nature-shared"):
        result = subprocess.run(["python", "-X", "utf8", str(validator), str(ROOT / "skill-candidate" / name)], capture_output=True, text=True, encoding="utf-8")
        assert result.returncode == 0, result.stderr + result.stdout
        validation[name] = result.stdout.strip()
    result = {"base_commit": BASE, "candidate_files_changed": CHANGED,
              "candidate_sha256_after": {p: sha(ROOT / p) for p in CHANGED},
              "protected_existing_tracked_files": len(protected), "protected_hashes_unchanged": True,
              "current_author_inputs_match_fresh_copies": True,
              "routes": routes, "quick_validate": validation,
              "effect_test_run": False, "installation_run": False,
              "effect_verdict": "not assessed; static loading and implementation do not establish effect or stability"}
    write("static-check.json", result)
    print(json.dumps({"static_checks": "passed", "changed_candidate_files": len(CHANGED), "protected_files": len(protected), "effect_test": "not run"}))


if __name__ == "__main__":
    main()
