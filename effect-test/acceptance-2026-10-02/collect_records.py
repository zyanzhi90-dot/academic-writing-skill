"""Collect execution/read evidence and preservation checks, without evaluating prose."""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
RECORD = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    provenance = json.loads((RECORD / "provenance.json").read_text(encoding="utf-8"))
    for field in ("candidate_files_sha256", "protected_project_files_sha256", "frozen_inputs_sha256"):
        for name, expected in provenance[field].items():
            assert digest(ROOT / name) == expected, f"Frozen file changed: {name}"
    assert digest(ROOT / "effect-test/run_once.py") == provenance["runner_sha256"]
    for package in provenance["installed_skills"]:
        directory = Path(package["directory"])
        actual = {p.relative_to(directory).as_posix(): digest(p)
                  for p in directory.rglob("*") if p.is_file()}
        assert actual == package["files"], f"Installed skill changed: {directory}"
    source = (ROOT / provenance["polishing_source"]).read_bytes()
    start, end = provenance["polishing_body_byte_range"]
    body = source[start:end]
    assert hashlib.sha256(body).hexdigest() == provenance["polishing_body_sha256"]
    assert (RECORD / "inputs/polishing.md").read_bytes().endswith(body)
    summaries = []
    for task in ("drafting", "polishing"):
        run = RECORD / task
        meta = json.loads((run / "run-meta.json").read_text(encoding="utf-8"))
        frozen = json.loads((run / "frozen-run.json").read_text(encoding="utf-8"))
        assert digest(run / "execution-prompt.txt") == frozen["prompt_sha256"]
        assert digest(Path(frozen["input"])) == frozen["input_sha256"]
        commands = []
        reads = {}
        unresolved = []
        directory_listings = []
        terminal_message = None
        for line in (run / "events.jsonl").read_text(encoding="utf-8").splitlines():
            event = json.loads(line)
            item = event.get("item") or {}
            if event.get("type") == "item.completed" and item.get("type") == "agent_message":
                terminal_message = item.get("text")
            if event.get("type") != "item.completed" or item.get("type") != "command_execution":
                continue
            command = item.get("command", "")
            normalized = command.replace("\\\\", "\\")
            entry = {"id": item.get("id"), "command": command,
                     "exit_code": item.get("exit_code"),
                     "output_characters": len(item.get("aggregated_output", ""))}
            commands.append(entry)
            if item.get("exit_code") != 0 or not item.get("aggregated_output"):
                continue
            if not re.search(r"Get-Content|\brg\b|read_text|read_bytes|pdfplumber|fitz|pdftotext", command, re.I):
                continue
            if "rg --files" in normalized:
                directory_listings.append(item.get("id"))
                continue
            paths = re.findall(r"[A-Za-z]:[\\/][^'\"\r\n]*?\.(?:md|yaml|txt|pdf|py|json)\b", normalized)
            resolved_paths = [Path(value).resolve() for value in paths]
            if "Join-Path $root $f" in normalized:
                role_root = ROOT / "skill-candidate" / meta["role"]
                assert str(role_root) in normalized
                relative_files = re.findall(r"(?:\.\.[\\/]|static[\\/])[^'\"\r\n]*?\.md\b", normalized)
                assert relative_files
                for value in relative_files:
                    assert f"### {value}" in item["aggregated_output"], (task, item.get("id"), value)
                    resolved_paths.append((role_root / value).resolve())
            found = False
            for path in resolved_paths:
                if not path.is_file():
                    continue
                try:
                    name = path.relative_to(ROOT).as_posix()
                except ValueError:
                    name = str(path)
                found = True
                read = reads.setdefault(name, {"path": name, "sha256": digest(path), "command_ids": []})
                read["command_ids"].append(item.get("id"))
            if not found:
                unresolved.append(item.get("id"))
        candidates = sorted(name for name in reads if name.startswith("skill-candidate/"))
        sources = sorted(name for name in reads if name.startswith(("\u6587\u732e\u8d44\u6599/", "analysis/reading/", "analysis/extracted/")))
        others = sorted(set(reads) - set(candidates) - set(sources))
        output = run / "first-output.md"
        matches_terminal_event = (output.is_file() and terminal_message is not None
                                  and output.read_text(encoding="utf-8").rstrip("\r\n")
                                  == terminal_message.rstrip("\r\n"))
        result = {
            "task": task, "candidate_commit": provenance["candidate_commit"],
            "model": meta["model"], "reasoning_effort": meta["reasoning_effort"],
            "input_sha256": frozen["input_sha256"],
            "loaded_files": candidates, "source_lookups": sources,
            "other_explicit_reads": others, "explicit_read_evidence": list(reads.values()),
            "completed_commands": commands,
            "unresolved_read_command_ids": unresolved,
            "directory_listing_command_ids": directory_listings,
            "extraction_limit": "Explicit absolute paths plus observed Join-Path $root $f loops resolved against the declared role root and corroborated by per-file output markers. Directory listings are separate. Commands/raw events retain ranges and search patterns; a search is not asserted to be a full-file read.",
            "exit_code": meta["exit_code"],
            "first_output_exists": output.is_file(),
            "first_output_bytes": output.stat().st_size if output.is_file() else 0,
            "first_output_sha256": digest(output) if output.is_file() else None,
            "first_output_matches_terminal_agent_message_except_final_newline": matches_terminal_event,
            "evaluation": "Not performed; output preserved without edits",
        }
        (run / "loaded-files.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        summaries.append({"task": task, "exit_code": meta["exit_code"],
                          "candidate_files_read_or_searched": len(candidates),
                          "source_lookup_files": len(sources),
                          "unresolved_read_commands": len(unresolved),
                          "first_output_bytes": result["first_output_bytes"],
                          "matches_terminal_event_except_final_newline": matches_terminal_event,
                          "first_output_sha256": result["first_output_sha256"]})
    verification = {
        "candidate_commit": provenance["candidate_commit"],
        "candidate_unchanged": True, "protected_project_files_unchanged": True,
        "installed_skills_unchanged": True, "inputs_and_prompts_unchanged": True,
        "polishing_body_verbatim": True, "tasks": summaries,
        "evaluation": "Not performed; no pass/fail quality verdict",
    }
    (RECORD / "verification.json").write_text(json.dumps(verification, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(verification, ensure_ascii=True))


if __name__ == "__main__":
    main()
