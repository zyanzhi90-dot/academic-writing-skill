"""Audit first-result retention and actual numbered source returns, not prose quality."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def verify(stage):
    dest = RECORD / stage
    frozen = json.loads((dest / 'frozen-run.json').read_text(encoding='utf-8'))
    audit = json.loads((dest / 'audit.json').read_text(encoding='utf-8'))
    events = [json.loads(line) for line in (dest / 'events.jsonl').read_text(encoding='utf-8').splitlines()]
    commands = {e['item']['id']: e['item'] for e in events if e.get('type') == 'item.completed'
                and e.get('item', {}).get('type') == 'command_execution'}
    exact = {}
    for name, ids in audit['loaded_paths'].items():
        p = dest / 'materials' / name
        if p.suffix not in ('.txt', '.md', '.yaml'):
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
                       'numbered_return_commands': sorted(set(c for cs in matches.values() for c in cs)),
                       'all_nonempty_lines_returned_exactly': all(i in matches for i,s in enumerate(lines,1) if s),
                       'ambiguous_or_mismatched_numbered_lines': conflicts,
                       'limit': 'Plain or search returns are retained in raw logs; this does not infer complete loading from path access.'}
    module = 'skill-candidate/nature-shared/core/abstract-delivery.md'
    example = 'skill-candidate/nature-shared/core/robotics-writing-examples.md'
    source_text = (dest / 'materials' / example).read_text(encoding='utf-8').splitlines()
    cards = {}
    for card in ('A06', 'A07', 'A08'):
        start = next(i for i,s in enumerate(source_text,1) if s.startswith('### ' + card))
        end = next((i-1 for i,s in enumerate(source_text,1) if i>start and (s.startswith('### ') or s.startswith('## '))),len(source_text))
        returned = set(exact.get(example,{}).get('matching_numbered_lines',[]))
        cards[card] = {'range': [start,end], 'all_nonempty_lines_returned_exactly': all(i in returned for i in range(start,end+1) if source_text[i-1])}
    threads = [e for e in events if e.get('type') == 'thread.started']
    assert len(threads) == 1
    assert audit['first_output_matches_terminal_except_final_newline']
    assert audit['materials_unchanged'] and audit['runtime_unchanged'] and not audit['outside_explicit_reads']
    assert frozen['model'] == 'gpt-6.1-sol' and frozen['reasoning_effort'] == 'high'
    facts = dest / 'materials/inputs/scientific-facts.md'
    assert facts.read_bytes() == (ROOT / 'effect-test/E02-abstract-materials-2026-10-03/科学事实包.md').read_bytes()
    report = {'stage': stage, 'thread': threads[0], 'one_effective_model_session': True,
              'original_E02_facts_unchanged': True, 'first_output_sha256': sha(dest / 'first-output.md'),
              'no_outside_explicit_reads': True, 'actual_numbered_returns': exact, 'selected_cards': cards,
              'delivery_module_loaded_exactly': exact.get(module,{}).get('all_nonempty_lines_returned_exactly',False),
              'original_facts_reopened_command_ids': audit['loaded_paths'].get('inputs/scientific-facts.md',[]),
              'initial_inputs_in_full_prompt_verified_by_execution_layer': frozen['required_input_actual_returns']['actual_returned_content_checked'],
              'effect_verdict': 'Evaluate actual prose separately; map execution beyond observable read/outputs is not proven'}
    target = dest / 'loading-and-retention.json'
    if target.exists():
        target = dest / 'loading-and-retention-padded-number-audit.json'
    assert not target.exists()
    target.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k: report[k] for k in ['stage','one_effective_model_session','delivery_module_loaded_exactly','original_facts_reopened_command_ids']},ensure_ascii=False))


def snapshot_baseline():
    source = (RECORD / 'execute_once.py').read_text(encoding='utf-8')
    start = source.index('    packages = ')
    end = source.index('        p = materials / name', start)
    source = source[:start] + """    for name in filter(None, git('ls-tree', '-r', '--name-only', '-z', commit,
                                'skill-candidate/' + role, 'skill-candidate/nature-shared').decode('utf-8').split('\\0')):
""" + source[end:]
    source = source.replace('        "execution records. Do not browse or change files. This invocation performs only the " + role +\n'
                            '        " stage; the execution layer handles any subsequent delivery stage separately. Return complete English abstract, accurate Chinese translation "\n',
                            '        "execution records. Do not browse or change files. Return complete English abstract, accurate Chinese translation "\n')
    source = source.replace("    (dest / 'runner-snapshot.py').write_bytes(Path(__file__).read_bytes())\n", '')
    frozen = json.loads((RECORD / 'polishing-baseline/frozen-run.json').read_text(encoding='utf-8'))
    assert hashlib.sha256(source.encode()).hexdigest() == frozen['runner_sha256']
    target = RECORD / 'polishing-baseline/runner-snapshot.py'
    assert not target.exists()
    target.write_bytes(source.encode())
    print('Reconstructed baseline runner matches pre-run frozen SHA-256 exactly')


def compact_failures():
    active = RECORD / 'polishing-baseline/materials'
    for name in ('preparation-cli-resolution-no-invocation', 'startup-config-error-no-model-session'):
        dest = RECORD / name
        sources = dest / 'materials'
        files = {p.relative_to(sources).as_posix(): sha(p) for p in sorted(sources.rglob('*')) if p.is_file()}
        assert all((active / n).is_file() and sha(active / n) == h for n,h in files.items())
        report = {'effective_model_sessions': 0, 'first_abstract_outputs': 0, 'duplicate_materials_reused_at': '../polishing-baseline/materials',
                  'files_sha256': files, 'all_bytes_identical_to_retained_materials': True,
                  'reason': 'CLI resolution/preparation or TOML parsing failed before thread.started; no model generation to rerun.'}
        (dest / 'duplicate-material-retention.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Duplicate inputs verified byte-identical; failure logs and input-return records remain')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['verify','snapshot-baseline','compact-failures'])
    parser.add_argument('stage', nargs='?')
    args = parser.parse_args()
    if args.action == 'verify':
        verify(args.stage)
    elif args.action == 'snapshot-baseline':
        snapshot_baseline()
    else:
        compact_failures()
