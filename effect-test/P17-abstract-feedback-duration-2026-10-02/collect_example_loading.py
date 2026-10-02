"""Record example ranges actually returned to the context; do not assess prose."""
import json
from pathlib import Path
import re

RECORD = Path(__file__).resolve().parent
frozen = json.loads((RECORD / "frozen-materials.json").read_text(encoding="utf-8"))
mapping = frozen["example_loading"]
source_lines = (RECORD / "materials" / mapping["file"]).read_text(encoding="utf-8").splitlines()
reads = []
for line in (RECORD / "drafting/events.jsonl").read_text(encoding="utf-8").splitlines():
    event = json.loads(line)
    item = event.get("item", {})
    if event.get("type") != "item.completed" or item.get("type") != "command_execution":
        continue
    command = item.get("command", "")
    if "robotics-writing-examples.md" not in command:
        continue
    output = item.get("aggregated_output", "")
    returned = [int(value) for value in re.findall(r"^\s*(\d+):", output, re.M)]
    numbered_text = re.findall(r"^\s*(\d+): (.*)$", output, re.M)
    differing_lines = [int(number) for number, text in numbered_text
                       if text.rstrip("\r") != source_lines[int(number) - 1]]
    lower, upper = re.search(r"-ge\s+(\d+)", command), re.search(r"-le\s+(\d+)", command)
    requested = [int(lower[1]), int(upper[1])] if lower and upper else None
    cards = [card["id"] for card in mapping["cards"]
             if card["start_line"] in returned]
    reads.append({"command_id": item.get("id"), "command": command, "exit_code": item.get("exit_code"),
                  "requested_inclusive_range": requested,
                  "returned_inclusive_range": [min(returned), max(returned)] if returned else None,
                  "returned_numbered_lines": len(returned), "card_headings_returned": cards,
                  "encoding_utf8_explicit": bool(re.search(r"-Encoding\s+UTF8", command, re.I)),
                  "returned_lines_differing_from_utf8_source": differing_lines,
                  "raw_output_characters": len(output)})
common = mapping["common_instructions_and_task_index"]
common_range = [common["start_line"], common["end_line"]]
first_common_only = bool(reads and reads[0]["returned_inclusive_range"] == common_range
                         and not reads[0]["card_headings_returned"])
selected = [card for item in reads for card in item["card_headings_returned"]]
all_cards_returned = set(selected) == {card["id"] for card in mapping["cards"]}
record = {"common_instructions_and_index_returned_before_selected_cards": first_common_only,
          "selected_card_ids_in_loading_order": selected, "all_cards_preloaded": all_cards_returned,
          "range_reads": reads,
          "returned_text_encoding_difference_seen": any(item["returned_lines_differing_from_utf8_source"] for item in reads),
          "evidence_limit": "Returned line numbers and commands, not a claim about physical disk reads or complete comprehension. Raw events retain actual text and encoding evidence.",
          "evaluation": "No manuscript quality assessment"}
(RECORD / "drafting/example-loading.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({key: record[key] for key in (
    "common_instructions_and_index_returned_before_selected_cards", "selected_card_ids_in_loading_order", "all_cards_preloaded", "returned_text_encoding_difference_seen")}, ensure_ascii=True))
