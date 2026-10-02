"""Freeze the requested tasks and provenance; no writing model or evaluation."""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
RECORD = Path(__file__).resolve().parent
COMMIT = "e126a659d77195f79416815db6ddb5827e60588e"
GIT = ["git", "-c", f"safe.directory={ROOT.as_posix()}"]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def file_map(directory):
    return {p.relative_to(ROOT).as_posix(): digest(p.read_bytes())
            for p in sorted(directory.rglob("*")) if p.is_file()}


def main():
    for name in ("provenance.json", "inputs"):
        if (RECORD / name).exists():
            raise SystemExit(f"Refusing to replace frozen material: {name}")
    assert subprocess.check_output(GIT + ["rev-parse", "HEAD"], cwd=ROOT).decode().strip() == COMMIT
    changed = subprocess.check_output(GIT + ["diff", COMMIT, "--", "skill-candidate"], cwd=ROOT)
    assert not changed, "Candidate differs from accepted commit"
    source_input = ROOT / "effect-test/inputs/F1.md"
    old_output = ROOT / "effect-test/runs/F1/candidate-repair-2/first-output.md"
    preference = ROOT / "\u6211\u81ea\u5df1\u7684\u7ecf\u9a8c\u548c\u505a\u6cd5.txt"
    original_input = source_input.read_bytes()
    original_output = old_output.read_bytes()
    facts_start = original_input.index(b"Research facts (P17, provided as author notes):")
    facts = original_input[facts_start:]
    body_start = original_output.index(b"### Introduction")
    body_end = original_output.index(b"## Notes", body_start)
    body = original_output[body_start:body_end]
    style = preference.read_bytes()
    drafting_task = b"""# Drafting | overall argument, abstract, and connected manuscript body

Target: a generic robotics research journal. Using the author facts below,
provide the overall argument and evidence organization for human discussion,
an English abstract, and a connected English manuscript body covering
Introduction, technical method, analysis, experiments, Discussion, and
Conclusion. Use informative section/subsection headings and substantive prose.
Proceed with the requested complete deliverable rather than waiting for outline
approval. Keep any necessary author notes outside the manuscript.

Express the author's own scientific content accurately, concisely, clearly,
plainly, and professionally. Preserve scientific facts and necessary boundaries.
You may state equations supplied here, but do not invent equations, statistics,
citations, or unreported tests. Use the specified Skill and its declared
references, including on-demand examples and original papers, to select and
adapt suitable organization and concrete English realizations.

## Author's writing preferences (provided verbatim)

"""
    polishing_task = b"""# Polishing | complete manuscript body

Target: a generic robotics research journal. Polish the complete supplied
English manuscript body using the same author facts below. Return the complete
polished body, covering Introduction, technical method, analysis, experiments,
Discussion, and Conclusion, with any necessary author/revision notes outside
the manuscript. No new abstract is requested for this task.

Treat the author facts as the scientific authority. Preserve the author's
supported scientific meanings and necessary boundaries. Improve organization
and English within this full-body task, retaining accurate natural expressions
and reasonable alternatives. Do not add equations, statistics, citations,
unreported tests, or scientific claims absent from author material. Use the
specified Skill and its declared references, including on-demand examples and
original papers, to select and adapt suitable organization and concrete English
realizations. Express the work accurately, concisely, clearly, plainly, and
professionally.

## Author's writing preferences (provided verbatim)

"""
    inputs = RECORD / "inputs"
    inputs.mkdir()
    drafting = drafting_task + style + b"\n\n## Author scientific material\n\n" + facts
    polishing = polishing_task + style + b"\n\n## Author scientific material\n\n" + facts + b"\n\n## Supplied manuscript body (verbatim)\n\n" + body
    (inputs / "drafting.md").write_bytes(drafting)
    (inputs / "polishing.md").write_bytes(polishing)
    assert facts in drafting and facts in polishing
    assert polishing.endswith(body)
    candidate = file_map(ROOT / "skill-candidate")
    tracked = subprocess.check_output(GIT + ["ls-files", "-z"], cwd=ROOT).decode("utf-8").split("\0")
    protected_project = {name: digest((ROOT / name).read_bytes()) for name in tracked
                         if name and name != "effect-test/run_once.py"}
    installed = []
    for user in ("user", "user2"):
        for package in ("nature-writing", "nature-polishing", "nature-shared"):
            directory = Path(f"C:/Users/{user}/.agents/skills/{package}")
            files = {p.relative_to(directory).as_posix(): digest(p.read_bytes())
                     for p in sorted(directory.rglob("*")) if p.is_file()}
            installed.append({"directory": str(directory), "files": files})
    provenance = {
        "candidate_commit": COMMIT,
        "candidate_files_sha256": candidate,
        "model": "gpt-6-sol", "reasoning_effort": "medium",
        "settings_source": "effect-test/runs/F1/candidate-repair-2/run-meta.json",
        "source_input": source_input.relative_to(ROOT).as_posix(),
        "source_input_sha256": digest(original_input),
        "author_facts_byte_range": [facts_start, len(original_input)],
        "author_facts_sha256": digest(facts),
        "polishing_source": old_output.relative_to(ROOT).as_posix(),
        "polishing_source_sha256": digest(original_output),
        "polishing_body_byte_range": [body_start, body_end],
        "polishing_body_sha256": digest(body),
        "body_extraction": "Exact bytes from ### Introduction to before ## Notes; no text edits; routing/central-argument/notes excluded",
        "author_preferences_sha256": digest(style),
        "frozen_inputs_sha256": file_map(inputs),
        "runner_sha256": digest((ROOT / "effect-test/run_once.py").read_bytes()),
        "protected_project_files_sha256": protected_project,
        "installed_skills": installed,
        "policy": "One execution per task; preserve first full output; no selection, evaluation, or revision in this round",
    }
    (RECORD / "provenance.json").write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"frozen_candidate": COMMIT, "candidate_files": len(candidate),
                      "inputs": list(provenance["frozen_inputs_sha256"]),
                      "facts_verbatim_in_both": True, "polishing_body_verbatim": True}))


if __name__ == "__main__":
    main()
