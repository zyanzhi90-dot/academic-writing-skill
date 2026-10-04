"""Save exact abstract slices and check returned contents, not merely file paths."""
from pathlib import Path
import hashlib
import json
import re

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
frozen = json.loads((RECORD / "frozen-materials.json").read_text(encoding="utf-8"))
verification = json.loads((RECORD / "verification.json").read_text(encoding="utf-8"))
loaded = json.loads((RECORD / "drafting/loaded-files.json").read_text(encoding="utf-8"))
assert verification["first_output_matches_terminal_message_except_final_newline"]
assert verification["outside_materials_explicit_reads"] == []
assert verification["unresolved_read_commands"] == ["item_26"]
source = RECORD / "drafting/first-output.md"
raw = source.read_bytes()
assert hashlib.sha256(raw).hexdigest() == verification["first_output_sha256"]
english_start = raw.index(b"This paper proposes")
english_end = raw.index(b"\n\n", english_start)
zh_header = "**中文翻译**\n\n".encode("utf-8")
zh_start = raw.index(zh_header) + len(zh_header)
zh_end = raw.index(b"\n\n", zh_start)
english, chinese = raw[english_start:english_end], raw[zh_start:zh_end]
sentences = re.split(r"(?<=\.)\s+", english.decode("utf-8"))
events = [json.loads(line) for line in (RECORD / "drafting/events.jsonl").read_text(encoding="utf-8").splitlines()]
commands = {e["item"]["id"]: e["item"] for e in events
            if e.get("type") == "item.completed" and e.get("item", {}).get("type") == "command_execution"}
load_by_path = {entry["path"]: entry for entry in loaded["loaded_or_searched_files"]}
def returned_lines(name):
    entry = load_by_path[name]
    rows = {}
    for command_id in entry["command_ids"]:
        for line in commands[command_id].get("aggregated_output", "").splitlines():
            match = re.match(r"^(\d+): (.*)$", line)
            if match:
                rows[int(match.group(1))] = match.group(2)
    return rows
coverage = {}
for name in ["inputs/task.md", "inputs/scientific-facts.md", "inputs/personal-experience.txt",
             "inputs/core-requirements.txt", "skill-candidate/nature-writing/static/fragments/section/abstract.md",
             "skill-candidate/nature-writing/references/abstract.md"]:
    lines = (RECORD / "materials" / name).read_text(encoding="utf-8").splitlines()
    required = {i + 1: line for i, line in enumerate(lines) if line.strip()}
    rows = returned_lines(name)
    missing = [number for number, line in required.items() if rows.get(number) != line]
    coverage[name] = {"command_ids": load_by_path[name]["command_ids"],
                      "source_nonempty_lines": len(required), "mismatched_or_missing_line_numbers": missing,
                      "all_nonempty_lines_returned_verbatim": not missing}
    if name.endswith("core-requirements.txt"):
        coverage[name].update({"source_bytes": (RECORD / "materials" / name).stat().st_size,
                               "source_characters": len("\n".join(lines)),
                               "actual_returned_rows": rows,
                               "cause": "Single-line Get-Content returned a scalar string; indexing $t[0] returned its first character"})
    else:
        assert not missing, (name, missing)
examples = "skill-candidate/nature-shared/core/robotics-writing-examples.md"
text = (RECORD / "materials" / examples).read_text(encoding="utf-8")
rows = returned_lines(examples)
heading_search = commands["item_26"]
searched_headings = []
for line in heading_search["aggregated_output"].splitlines():
    match = re.match(r"^(\d+):(.*)$", line)
    assert match and text.splitlines()[int(match.group(1)) - 1] == match.group(2), line
    searched_headings.append(int(match.group(1)))
assert "robotics-writing-examples.md" in heading_search["command"] and heading_search["exit_code"] == 0
manual_resolution = {"command_id": "item_26", "source": examples,
                     "reason": "Collector path regex could not join shell-quoted path fragments; all returned heading rows match the unique frozen file",
                     "returned_heading_line_numbers": searched_headings,
                     "boundary_status": "Resolved as search of the permitted shared example file"}
cards = {}
for key in ("A05", "A06", "A07"):
    match = re.search(r"^### " + key + r".*?(?=^### |^## |\Z)", text, re.M | re.S)
    start_line = text[:match.start()].count("\n") + 1
    lines = match.group().splitlines()
    required = {start_line + i: line for i, line in enumerate(lines) if line.strip()}
    assert all(rows.get(number) == line for number, line in required.items()), key
    cards[key] = {"line_range": [start_line, start_line + len(lines) - 1],
                  "full_english_and_analysis_returned_verbatim": True}
sources = {"scientific-facts.md": ROOT / frozen["facts_source"],
           "personal-experience.txt": ROOT / frozen["experience_source"],
           "core-requirements.txt": ROOT / "核心要求.txt",
           "task.md": ROOT / "effect-test/E02-abstract-autonomous-regression-2026-10-04/materials/inputs/task.md"}
for name, original in sources.items():
    assert (RECORD / "materials/inputs" / name).read_bytes() == original.read_bytes(), name
allowed = set(frozen["original_candidate_files_sha256"]) | {item["path"] for item in frozen["corpus_sources"]} | {"inputs/" + name for name in sources}
assert set(frozen["materials_files_sha256"]) == allowed
report = {
    "run_kind": "known-E02-autonomous-regression", "model": "gpt-6.1-sol", "reasoning_effort": "high",
    "single_cli_invocation": True, "generation_feedback_reruns_selection_or_edits": False,
    "first_output_sha256": verification["first_output_sha256"],
    "english_slice_byte_offsets": [english_start, english_end], "chinese_slice_byte_offsets": [zh_start, zh_end],
    "derived_files_are_exact_byte_slices_without_added_newline": True,
    "english_sentences": sentences, "english_sentence_count": len(sentences),
    "english_word_count": len(english.decode("utf-8").split()),
    "returned_input_and_rule_content_coverage": coverage, "actual_example_loading": cards,
    "writer_input_files": len(allowed), "only_allowed_input_inventory": True,
    "facts_experience_core_and_standard_request_byte_identical": True,
    "full_required_input_actually_returned": all(item["all_nonempty_lines_returned_verbatim"] for item in coverage.values()),
    "outside_materials_explicit_reads": [],
    "collector_unresolved_commands_retained": verification["unresolved_read_commands"],
    "manual_command_resolution": manual_resolution, "remaining_unresolved_read_commands": [],
    "isolation_limit": "Fresh ephemeral context and material-only directory with audited reads; no OS-level read isolation claimed",
    "effect_verdict": "See evaluation.md; incomplete core-requirements read prevents a full-input autonomous pass claim",
}
for name, data in (("abstract.en.txt", english), ("abstract.zh.txt", chinese)):
    assert not (RECORD / name).exists(), "Do not overwrite a first-output derivative"
    (RECORD / name).write_bytes(data)
(RECORD / "first-output-audit.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
assert source.read_bytes() == raw
print(json.dumps({"verbatim_output": True, "word_count": report["english_word_count"],
                  "sentence_count": len(sentences), "full_input_actually_returned": report["full_required_input_actually_returned"]}))
