"""Read-only implementation checks; no model invocation or writing-effect test.

Axes and domain/task boundaries in the cases are manually resolved from the
routers. This script checks manifest lookup, real file reads, selective card
extraction, and relocation, not a natural-language routing interpreter.
Run from any directory: python -X utf8 analysis/check_candidate_loading.py
"""
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

import yaml

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "skill-candidate"
BASE_COMMIT = "105a6ea"
EXAMPLES = "../nature-shared/core/robotics-writing-examples.md"
BODY = "../nature-shared/core/robotics-main-text.md"
SAFE_GIT = ["git", "-c", f"safe.directory={ROOT.as_posix()}"]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def declared_paths(value):
    paths = []
    if isinstance(value, dict):
        for key, item in value.items():
            if key == "always_load":
                paths.extend(item)
            elif key == "values":
                paths.extend(item.values())
            elif key in ("path", "consistency_script"):
                paths.append(item)
            else:
                paths.extend(declared_paths(item))
    elif isinstance(value, list):
        for item in value:
            paths.extend(declared_paths(item))
    return paths


def manifests_at(base):
    result = {}
    for name in ("nature-writing", "nature-polishing", "nature-shared"):
        package = base / name
        manifest = yaml.safe_load((package / "manifest.yaml").read_text(encoding="utf-8"))
        paths = declared_paths(manifest)
        for relative in paths:
            path = (package / relative).resolve()
            assert path.is_relative_to(base.resolve()), (name, relative)
            assert path.is_file() and path.read_bytes(), (name, relative)
        result[name] = (manifest, paths)
    return result


def cards(text):
    matches = list(re.finditer(r"^### ([AB]\d{2})[^\n]*", text, re.M))
    result = {}
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else text.index("## \u9009\u62e9\u8303\u4f8b\u65f6\u7684\u8fb9\u754c", match.end())
        result[match.group(1)] = text[match.start():end]
    return result


def read_case(base, name, case, manifest):
    package = base / name
    paths = ["SKILL.md", "manifest.yaml", *manifest["always_load"]]
    refs = {entry["path"] for entry in manifest["references"]["on_demand"]}
    sections = case.get("sections", [])
    admin = case.get("admin", False)
    layout = case.get("layout", False)
    paper_type = None if layout else case.get("paper_type", manifest["axes"]["paper_type"]["default"])
    if layout:
        paths.append("references/latex-layout.md")
    else:
        axes = {"paper_type": paper_type, "language": case.get("language", "en"),
                "journal": case.get("journal", "generic")}
        if name == "nature-writing":
            axes["task"] = "submission-package" if admin else "manuscript"
        for axis, value in axes.items():
            paths.append(manifest["axes"][axis]["values"][value])
        if not admin:
            paths.extend(manifest["axes"]["section"]["values"][section] for section in sections)
        if axes["language"] == "zh-to-en" and not admin:
            paths.append("static/fragments/language/en.md")
    eligible = (case.get("robotics", True) and not case.get("incidental", False)
                and not admin and not layout and sections != ["title"])
    has_body = eligible and (not sections or any(s not in ("title", "abstract") for s in sections))
    selected = []
    if eligible:
        assert EXAMPLES in refs
        paths.append(EXAMPLES)
        if "abstract" in sections:
            selected.append("A02")
        if has_body:
            assert BODY in refs
            paths.append(BODY)
            if case.get("whole"):
                selected.extend(["B01", "B13"])
            elif any(s in ("intro", "related-work") for s in sections):
                selected.append("B02")
            elif "discussion" in sections:
                selected.append("B11")
            else:
                selected.append("B04")
    if not admin and not layout:
        if case.get("journal") == "nature":
            for section, ref in (("abstract", "nature-abstract"), ("intro", "nature-introduction"),
                                 ("discussion", "nature-results-discussion")):
                if section in sections or (section == "intro" and case.get("whole")):
                    path = f"../nature-shared/core/{ref}.md"
                    assert path in refs
                    paths.append(path)
        if "discussion" in sections:
            paths.append("../nature-shared/core/discussion-argument-language.md")
        if case.get("whole") or any(s in ("results", "experiments") for s in sections):
            paths.append("../nature-shared/core/main-text-discipline.md")
        if name == "nature-polishing" and case.get("whole"):
            paths.append("../nature-shared/core/consistency-sweep.md")
    paths = list(dict.fromkeys(paths))
    reads = []
    for relative in paths:
        path = (package / relative).resolve()
        data = path.read_bytes()
        text = data.decode("utf-8")
        record = {"path": path.relative_to(base.resolve()).as_posix(), "sha256": sha(data)}
        if relative == EXAMPLES:
            units = cards(text)
            common_and_index = text[:text.index("## \u6458\u8981")]
            fragments = {"common_and_task_index": sha(common_and_index.encode("utf-8"))}
            fragments.update({card: sha(units[card].encode("utf-8")) for card in selected})
            assert "## Internal expression and context check before delivery" in common_and_index
            record["selected_fragment_sha256"] = fragments
        reads.append(record)
    assert (EXAMPLES in paths) == eligible
    assert (BODY in paths) == has_body
    if sections == ["abstract"] and case.get("journal", "generic") == "generic":
        assert "../nature-shared/core/nature-abstract.md" not in paths
    if case.get("language") == "zh-to-en" and not admin and not layout:
        assert "static/fragments/language/zh-to-en.md" in paths
        assert "static/fragments/language/en.md" in paths
    return {"skill": name, "case": case["id"], "resolved_request": case,
            "resolved_paper_type": paper_type,
            "examples": eligible, "body_module": has_body, "selected_cards": selected,
            "files_read": reads}


def check():
    manifests = manifests_at(CANDIDATE)
    for name in ("nature-writing", "nature-polishing"):
        assert manifests[name][0]["axes"]["paper_type"]["default"] == "research"
    source = subprocess.check_output(SAFE_GIT + ["show", BASE_COMMIT + ":analysis/robotics-writing-examples.md"], cwd=ROOT).decode("utf-8")
    destination = (CANDIDATE / "nature-shared/core/robotics-writing-examples.md").read_text(encoding="utf-8")
    old_cards, new_cards = cards(source), cards(destination)
    assert len(old_cards) == len(new_cards) == 19
    assert old_cards == new_cards, "Accepted card text changed"
    old_quotes = [s for s in source.splitlines() if s.startswith("> ")]
    new_quotes = [s for s in destination.splitlines() if s.startswith("> ")]
    assert old_quotes == new_quotes and len(old_quotes) == 26
    old_links = re.findall(r"^\[P\d+\]: <\.\./(.*?)>$", source, re.M)
    new_links = re.findall(r"^\[P\d+\]: <\.\./\.\./\.\./(.*?)>$", destination, re.M)
    assert old_links == new_links
    for link in new_links:
        assert (ROOT / link).is_file()
    scenarios = [
        {"id": "generic-abstract", "sections": ["abstract"]},
        {"id": "abstract-zh-to-en", "sections": ["abstract"], "language": "zh-to-en"},
        {"id": "nature-abstract", "sections": ["abstract"], "journal": "nature"},
        {"id": "specified-intro", "sections": ["intro"]},
        {"id": "method", "sections": ["method"]},
        {"id": "explicit-algorithmic-method", "sections": ["method"], "paper_type": "algorithmic"},
        {"id": "related-work-zh-to-en", "sections": ["related-work"], "language": "zh-to-en"},
        {"id": "free-paragraph", "sections": []},
        {"id": "overall-reasoning", "sections": [], "whole": True},
        {"id": "full-body", "sections": ["intro", "related-work", "method", "experiments", "discussion", "conclusion"], "whole": True},
        {"id": "body-feedback", "sections": ["method"], "feedback": True},
        {"id": "abstract-feedback", "sections": ["abstract"], "feedback": True},
        {"id": "abstract-and-body", "sections": ["abstract", "method"]},
        {"id": "nature-discussion", "sections": ["discussion"], "journal": "nature"},
        {"id": "nonrobotics-body", "sections": ["intro"], "robotics": False},
        {"id": "incidental-robotics", "sections": ["method"], "incidental": True},
        {"id": "title-only", "sections": ["title"]},
        {"id": "administration", "sections": [], "admin": True},
        {"id": "layout", "sections": [], "layout": True},
        {"id": "nonrobotics-abstract", "sections": ["abstract"], "robotics": False},
    ]
    records = []
    for name in ("nature-writing", "nature-polishing"):
        for original in scenarios:
            case = dict(original)
            if name == "nature-polishing":
                case["sections"] = [{"method": "methods", "experiments": "results"}.get(s, s) for s in case["sections"]]
            if name == "nature-writing" and case.get("layout"):
                # Writing has no layout workflow; explicit exclusion is router-reviewed.
                continue
            records.append(read_case(CANDIDATE, name, case, manifests[name][0]))
    with tempfile.TemporaryDirectory(prefix="robotics-candidate-loading-") as directory:
        detached = Path(directory) / "skills"
        shutil.copytree(CANDIDATE, detached)
        detached_manifests = manifests_at(detached)
        for record in records:
            read_case(detached, record["skill"], record["resolved_request"], detached_manifests[record["skill"]][0])
        assert not (detached.parent / "analysis").exists()
        assert not (detached.parent / "\u6587\u732e\u8d44\u6599").exists()
    return {"basis_commit": BASE_COMMIT,
            "method": "Manually resolved routing cases; manifest lookup and real file/selected-fragment reads. Not model invocation, automatic semantic routing, or writing-effect evidence.",
            "versions_and_declared_paths": {name: {"version": value[0]["version"], "path_entries": len(value[1])} for name, value in manifests.items()},
            "source_preservation": {"cards_unchanged": 19, "quote_blocks_unchanged": 26, "source_links_resolved": len(new_links)},
            "detached_candidate_only_reads": "passed; no plan, evidence report, extraction text, or PDF present",
            "scenarios": records}


if __name__ == "__main__":
    result = check()
    output = ROOT / "analysis/candidate-loading-check.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"result": "passed", "scenarios": len(result["scenarios"]),
                      "versions_and_declared_paths": result["versions_and_declared_paths"],
                      "source_preservation": result["source_preservation"]}, ensure_ascii=True))
