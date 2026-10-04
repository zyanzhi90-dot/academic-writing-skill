"""Audit loading and first-result retention independently of prose quality."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import yaml

RECORD = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

def verify(stage):
    dest = RECORD / stage
    frozen = json.loads((dest / 'frozen-run.json').read_text(encoding='utf-8'))
    audit = json.loads((dest / 'audit.json').read_text(encoding='utf-8'))
    events = [json.loads(s) for s in (dest / 'events.jsonl').read_text(encoding='utf-8').splitlines()]
    commands = {e['item']['id']: e['item'] for e in events if e.get('type') == 'item.completed' and e.get('item', {}).get('type') == 'command_execution'}
    exact = {}
    for name, ids in audit['loaded_paths'].items():
        p = dest / 'materials' / name
        if p.suffix not in ('.md', '.txt', '.yaml'):
            continue
        lines = p.read_text(encoding='utf-8').splitlines()
        matches, conflicts = {}, []
        for cid in ids:
            for raw in commands[cid].get('aggregated_output', '').splitlines():
                m = re.fullmatch(r'\s*(\d+): (.*)', raw)
                if not m:
                    continue
                n, text = int(m[1]), m[2]
                if 1 <= n <= len(lines) and lines[n-1] == text:
                    matches.setdefault(n, []).append(cid)
                else:
                    conflicts.append({'command': cid, 'number': n, 'returned': text})
        exact[name] = {'sha256': sha(p), 'matching_numbered_lines': sorted(matches),
                       'all_nonempty_lines_returned_exactly': all(i in matches for i,s in enumerate(lines,1) if s),
                       'ambiguous_or_mismatched_numbered_lines': conflicts}
    example = 'skill-candidate/nature-shared/core/robotics-writing-examples.md'
    lines = (dest / 'materials' / example).read_text(encoding='utf-8').splitlines()
    seen = set(exact.get(example, {}).get('matching_numbered_lines', []))
    cards = {}
    for i, line in enumerate(lines, 1):
        m = re.match(r'### (A\d+)\b', line)
        if not m:
            continue
        end = next((j-1 for j in range(i+1,len(lines)+1) if lines[j-1].startswith(('### ', '## '))),len(lines))
        if any(j in seen for j in range(i,end+1)):
            cards[m[1]] = {'range': [i,end], 'all_nonempty_lines_returned_exactly': all(j in seen for j in range(i,end+1) if lines[j-1])}
    role = frozen['role']
    manifest = dest / ('materials/skill-candidate/' + role + '/manifest.yaml')
    config = yaml.safe_load(manifest.read_text(encoding='utf-8'))
    core = [str((manifest.parent / s).resolve().relative_to((dest/'materials').resolve())).replace('\\','/') for s in config['always_load']]
    core += ['skill-candidate/' + role + '/SKILL.md', 'skill-candidate/' + role + '/manifest.yaml',
             'skill-candidate/' + role + '/static/fragments/section/abstract.md',
             'skill-candidate/nature-shared/core/abstract-delivery.md']
    core_status = {name: exact.get(name,{}).get('all_nonempty_lines_returned_exactly',False) for name in core}
    threads = [e for e in events if e.get('type') == 'thread.started']
    assert len(threads) == 1
    assert audit['first_output_matches_terminal_except_final_newline']
    assert audit['materials_unchanged'] and audit['runtime_unchanged'] and not audit['outside_explicit_reads']
    assert (dest/'materials/inputs/scientific-facts.md').read_bytes() == (RECORD/'scientific-facts.md').read_bytes()
    assert frozen['model'] == 'gpt-6.1-sol' and frozen['reasoning_effort'] == 'high'
    report = {'stage': stage, 'thread': threads[0], 'one_effective_model_session': True,
              'case': 'E04', 'original_facts_unchanged': True, 'first_output_sha256': sha(dest/'first-output.md'),
              'no_outside_explicit_reads': True, 'actual_numbered_returns': exact,
              'core_full_return_status': core_status, 'selected_cards': cards,
              'facts_reopened_commands': audit['loaded_paths'].get('inputs/scientific-facts.md',[]),
              'complete_original_inputs_delivered_in_initial_prompt': frozen['required_input_actual_returns']['actual_returned_content_checked'],
              'limit': 'Material-only path constraints and explicit command audit; no OS read isolation claim. Returned sources do not prove a hidden check was carried out correctly.',
              'effect_verdict': 'Prose evaluation separate, after final output has been saved'}
    target = dest/'loading-and-retention.json'
    assert not target.exists()
    target.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'stage':stage, 'core':core_status, 'cards':cards}, ensure_ascii=False))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('stage')
    verify(parser.parse_args().stage)
