"""Audit returned material ranges and preservation; never assess the abstract."""
from pathlib import Path
import hashlib
import json
import re

RECORD = Path(__file__).resolve().parent
frozen = json.loads((RECORD / "frozen-materials.json").read_text(encoding="utf-8"))
runtime = Path(frozen["runtime_directory"])
material = RECORD / "materials"
dest = RECORD / "drafting"
events = [json.loads(line) for line in (dest / "events.jsonl").read_text(encoding="utf-8").splitlines()]
commands, mismatches, unmatched_numbered, types = [], [], [], {}
example_reads = []
for event in events:
    if event.get("type") != "item.completed":
        continue
    item = event.get("item", {})
    kind = item.get("type", "unknown")
    types[kind] = types.get(kind, 0) + 1
    if kind != "command_execution":
        continue
    command = item.get("command", "")
    output = item.get("aggregated_output", "")
    normalized = command.replace("\\\\", "\\")
    paths = []
    for value in re.findall(r"[A-Za-z]:[\\/][^'\"\r\n]*?\.(?:md|yaml|txt|pdf|py|json)\b", normalized):
        path = Path(value).resolve()
        if path.is_relative_to(runtime) and path.is_file():
            name = path.relative_to(runtime).as_posix()
            if name not in paths:
                paths.append(name)
    numbered = [(int(number), text.rstrip("\r")) for number, text in
                re.findall(r"^\s*(\d+): ?(.*)$", output, re.M)]
    unnumbered_match = False
    reconstructed_by_file = {}
    # Verify actual unnumbered output against each explicit Get-Content path.
    # A single path may use TotalCount followed by Skip/First; a batched
    # whole-file command returns its explicit paths in command order.
    if not numbered and paths and re.search(r"Get-Content", command, re.I):
        expected, returned_positions = [], []
        for name in paths:
            if name.endswith(".pdf"):
                continue
            source_lines = (material / name).read_text(encoding="utf-8").splitlines()
            skip = re.search(r"-Skip\s+(\d+)", command, re.I) if len(paths) == 1 else None
            first = re.search(r"-First\s+(\d+)", command, re.I) if len(paths) == 1 else None
            total = re.search(r"-TotalCount\s+(\d+)", command, re.I) if len(paths) == 1 else None
            start = int(skip[1]) if skip else 0
            stop = min(len(source_lines), int(total[1])) if total else len(source_lines)
            if first:
                stop = min(stop, start + int(first[1]))
            selected = source_lines[start:stop]
            expected.extend(selected)
            returned_positions.extend(enumerate(selected, start + 1))
            if selected:
                reconstructed_by_file[name] = [[start + 1, start + len(selected)]]
        unnumbered_match = output.splitlines() == expected
        if unnumbered_match:
            numbered = returned_positions
        else:
            reconstructed_by_file = {}
            mismatches.append({"command_id": item.get("id"),
                               "reason": "Unnumbered return differs from explicit frozen source range",
                               "candidate_sources": paths})
    numbers = [number for number, _ in numbered]
    ranges = []
    for number in sorted(set(numbers)):
        if ranges and number == ranges[-1][1] + 1:
            ranges[-1][1] = number
        else:
            ranges.append([number, number])
    sources = {name: (material / name).read_text(encoding="utf-8").splitlines()
               for name in paths if not name.endswith(".pdf")}
    if numbered and not sources:
        unmatched_numbered.append(item.get("id"))
    for number, text in numbered:
        if sources and not any(number <= len(lines) and text == lines[number - 1]
                               for lines in sources.values()):
            mismatches.append({"command_id": item.get("id"), "line": number,
                               "candidate_sources": list(sources)})
    entry = {"command_id": item.get("id"), "exit_code": item.get("exit_code"), "paths": paths,
             "explicit_utf8_read": bool(re.search(r"-Encoding\s+UTF8|--encoding\s+utf-8|encoding\s*=\s*['\"]utf-8", command, re.I)),
             "verified_source_line_ranges": ranges, "verified_source_lines": len(numbered),
             "source_lines_reconstructed_from_unnumbered_return": unnumbered_match,
             "verified_source_ranges_by_file": reconstructed_by_file,
             "verified_lines_match_frozen_text": bool(sources and numbered) and
                 not any(x["command_id"] == item.get("id") for x in mismatches),
             "command": command}
    commands.append(entry)
    if frozen["example_loading"]["file"] in paths:
        example_reads.append((entry, set(numbers)))

example_path = frozen["example_loading"]["file"]
lines = (material / example_path).read_text(encoding="utf-8").splitlines()
headings = [(i + 1, re.match(r"### ([AB]\d+)\uff5c", line)[1])
            for i, line in enumerate(lines) if re.match(r"### ([AB]\d+)\uff5c", line)]
cards = []
returned_all = set().union(*(numbers for _, numbers in example_reads))
for start, name in headings:
    end = next((i for i in range(start + 1, len(lines) + 1)
                if lines[i - 1].startswith(("### ", "## "))), len(lines) + 1) - 1
    required = {i for i in range(start, end + 1) if lines[i - 1].strip()}
    cards.append({"id": name, "source_range": [start, end], "heading_returned": start in returned_all,
                  "complete_nonblank_card_returned": required.issubset(returned_all),
                  "command_ids": [entry["command_id"] for entry, numbers in example_reads if required & numbers]})
common_start, common_end = frozen["example_loading"]["common_and_task_index_lines"]
common_required = {i for i in range(common_start, common_end + 1) if lines[i - 1].strip()}
seen, first_common, first_card = set(), None, None
card_required = set().union(*({i for i in range(card["source_range"][0], card["source_range"][1] + 1)
                            if lines[i - 1].strip()} for card in cards))
for entry, numbers in example_reads:
    seen.update(numbers)
    if first_common is None and common_required.issubset(seen):
        first_common = entry["command_id"]
    if first_card is None and numbers & card_required:
        first_card = entry["command_id"]
order = {entry["command_id"]: i for i, entry in enumerate(commands)}
result = {"scope": "Actual loading and byte-preservation evidence; no prose quality verdict",
          "candidate_commit": frozen["candidate_commit"], "model_requested": frozen["model"],
          "reasoning_effort_requested": frozen["reasoning_effort"], "attempts": 1,
          "completed_item_types": types, "verified_source_lines_checked":
              sum(entry["verified_source_lines"] for entry in commands if entry["paths"]),
          "text_mismatches": mismatches, "unmapped_numbered_returns": unmatched_numbered,
          "commands": commands,
          "examples": {"common_range": [common_start, common_end],
                       "common_returned_command": first_common, "first_card_text_command": first_card,
                       "common_returned_before_card_text": bool(first_common is not None and first_card is not None
                                                               and order[first_common] < order[first_card]),
                       "cards": cards,
                       "all_cards_completely_returned": all(x["complete_nonblank_card_returned"] for x in cards)},
          "raw_record_sha256": {name: hashlib.sha256((dest / name).read_bytes()).hexdigest()
                                for name in ("events.jsonl", "stderr.txt", "execution-command.json", "execution-prompt.txt")},
          "evidence_limit": "Explicit command paths and source lines: returned numbers where present, or an explicit Get-Content/Select-Object range verified line for line against frozen UTF-8 text. Searches and headings are not complete card reads; no OS-level read isolation or comprehension claim."}
(dest / "loading-audit.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"completed_commands": len(commands), "verified_source_lines_checked":
                  result["verified_source_lines_checked"], "text_mismatches": len(mismatches),
                  "unmapped_numbered_returns": unmatched_numbered,
                  "complete_cards_returned": [x["id"] for x in cards if x["complete_nonblank_card_returned"]]},
                 ensure_ascii=True))
