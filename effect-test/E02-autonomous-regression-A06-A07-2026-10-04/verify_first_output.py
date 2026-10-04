"""Retain verbatim abstract slices and audit actual card/input loading; never edit prose."""
from pathlib import Path
import hashlib
import json
import re
import runpy

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
frozen = json.loads((RECORD / "frozen-materials.json").read_text(encoding="utf-8"))
verification = json.loads((RECORD / "verification.json").read_text(encoding="utf-8"))
assert verification["first_output_matches_terminal_message_except_final_newline"]
assert verification["outside_materials_explicit_reads"] == verification["unresolved_read_commands"] == []
source = RECORD / "drafting/first-output.md"
raw = source.read_bytes()
assert hashlib.sha256(raw).hexdigest() == verification["first_output_sha256"]
english_start = raw.index(b"This paper proposes")
english_end = raw.index(b"\n\n", english_start)
zh_header = "**中文翻译**\n\n".encode("utf-8")
zh_start = raw.index(zh_header) + len(zh_header)
zh_end = raw.index(b"\n\n", zh_start)
english, chinese = raw[english_start:english_end], raw[zh_start:zh_end]
for name, data in (("abstract.en.txt", english), ("abstract.zh.txt", chinese)):
    assert not (RECORD / name).exists(), "Do not overwrite a first-output derivative"
    (RECORD / name).write_bytes(data)
sentences = re.split(r"(?<=\.)\s+", english.decode("utf-8"))
assert len(sentences) == 8 and all(sentence.endswith(".") for sentence in sentences)
events = [json.loads(line) for line in (RECORD / "drafting/events.jsonl").read_text(encoding="utf-8").splitlines()]
rows, quote_outputs, transport_events = {}, [], []
for event in events:
    item = event.get("item", {})
    if event.get("type") == "error" or item.get("type") == "error":
        transport_events.append(event)
    if event.get("type") == "item.completed" and item.get("type") == "command_execution":
        if "robotics-writing-examples.md" in item.get("command", ""):
            output = item.get("aggregated_output", "")
            quote_outputs.append(output)
            for line in output.splitlines():
                match = re.match(r"^(\d+): (.*)$", line)
                if match:
                    rows[int(match.group(1))] = match.group(2)
checker = runpy.run_path(str(ROOT / "analysis/check_candidate_loading.py"))
text = (RECORD / "materials/skill-candidate/nature-shared/core/robotics-writing-examples.md").read_text(encoding="utf-8")
card_evidence = {}
for key in ("A04", "A05", "A06", "A07"):
    match = re.search(r"^### " + key + r".*?(?=^### |^## |\Z)", text, re.M | re.S)
    start_line = text[:match.start()].count("\n") + 1
    lines = match.group().splitlines()
    required = {start_line + i: line for i, line in enumerate(lines) if line.strip()}
    assert all(rows.get(number) == line for number, line in required.items()), key
    quote = next(line for line in lines if line.startswith("> "))
    assert any(quote in output for output in quote_outputs)
    card_evidence[key] = {"line_range": [start_line, start_line + len(lines) - 1],
                          "all_nonempty_card_lines_returned_verbatim": True,
                          "full_english_quote_returned": True,
                          "card_sha256": hashlib.sha256(match.group().encode("utf-8")).hexdigest()}
inputs = RECORD / "materials/inputs"
sources = {"scientific-facts.md": ROOT / frozen["facts_source"],
           "personal-experience.txt": ROOT / frozen["experience_source"],
           "core-requirements.txt": ROOT / "核心要求.txt",
           "task.md": ROOT / "effect-test/E02-abstract-autonomous-regression-2026-10-04/materials/inputs/task.md"}
for name, original in sources.items():
    assert (inputs / name).read_bytes() == original.read_bytes(), name
allowed = set(frozen["original_candidate_files_sha256"]) | {item["path"] for item in frozen["corpus_sources"]} | {"inputs/" + name for name in sources}
assert set(frozen["materials_files_sha256"]) == allowed
report = {
    "run_kind": "known-E02-autonomous-regression", "model": "gpt-6.1-sol", "reasoning_effort": "high",
    "single_cli_invocation": True, "generation_feedback_reruns_selection_or_edits": False,
    "first_output_sha256": verification["first_output_sha256"],
    "english_slice_byte_offsets": [english_start, english_end],
    "chinese_slice_byte_offsets": [zh_start, zh_end],
    "derived_files_are_exact_byte_slices_without_added_newline": True,
    "english_sentences": sentences, "english_word_count": len(english.decode("utf-8").split()),
    "actual_example_card_loading": card_evidence,
    "updated_A06_A07_analysis_loaded_verbatim": True,
    "writer_input_files": len(allowed), "only_allowed_input_inventory": True,
    "author_facts_experience_core_and_standard_request_byte_identical": True,
    "outside_materials_explicit_reads": [],
    "transport_events_within_the_single_invocation": transport_events,
    "isolation_limit": "New ephemeral context and material-only directory with audited reads; no OS-level read isolation claimed",
    "scientific_or_writing_effect_verdict": "See coordinator evaluation.md; loading does not establish writing quality",
}
(RECORD / "first-output-audit.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
assert source.read_bytes() == raw
print(json.dumps({"verbatim_output": True, "word_count": report["english_word_count"], "full_cards_loaded": list(card_evidence), "input_files": len(allowed)}))
