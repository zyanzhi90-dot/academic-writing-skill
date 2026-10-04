"""Frozen material-only, one invocation per stage; never overwrite a first result."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import runpy
import shutil
import subprocess
import tempfile
import time

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
PRIOR = ROOT / 'effect-test/E02-abstract-judgment-regression-2026-10-04'
MODEL, EFFORT = 'gpt-6.1-sol', 'high'


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def inventory(p):
    return {f.relative_to(p).as_posix(): digest(f) for f in sorted(p.rglob('*')) if f.is_file()}


def save(p, obj):
    assert not p.exists(), p
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def prepare(stage, commit, draft):
    dest = RECORD / stage
    assert not dest.exists(), 'Never replace a prepared or running stage'
    materials = dest / 'materials'
    materials.mkdir(parents=True)
    role = 'nature-writing' if draft is None else 'nature-polishing'
    candidate = {}
    packages = ['skill-candidate/' + role, 'skill-candidate/nature-shared']
    if role == 'nature-writing':
        packages.append('skill-candidate/nature-polishing')
    for name in filter(None, git('ls-tree', '-r', '--name-only', '-z', commit,
                                *packages).decode('utf-8').split('\0')):
        p = materials / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(git('show', commit + ':' + name))
        candidate[name] = digest(p)
    previous = json.loads((PRIOR / 'frozen-materials.json').read_text(encoding='utf-8'))
    reused = {}
    for name, expected in previous['materials_files_sha256'].items():
        if name.startswith('skill-candidate/'):
            continue
        source = PRIOR / 'materials' / name
        assert digest(source) == expected
        p = materials / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(source.read_bytes())
        reused[name] = {'source': source.relative_to(ROOT).as_posix(), 'sha256': expected}
    if draft is not None:
        source = draft.resolve()
        assert source.is_relative_to(ROOT) and source.is_file()
        (materials / 'inputs/current-draft.md').write_bytes(source.read_bytes())
        reused['inputs/current-draft.md'] = {'source': source.relative_to(ROOT).as_posix(), 'sha256': digest(source)}
        (materials / 'inputs/task.md').write_text(
            '本轮仅调用提供的 nature-polishing，润色 inputs/current-draft.md 的完整英文摘要，并附准确中文翻译。'
            '以 inputs/scientific-facts.md 的原样科学事实和作者要求为依据，由 Skill 自主完成贡献判断、内容取舍、论述组织和具体英文。'
            '直接参照认可范例的真实英文，把科学内容换成作者自己的；必要作者说明置于摘要之外。\n', encoding='utf-8')
    assert (materials / 'inputs/scientific-facts.md').read_bytes() == (ROOT / previous['facts_source']).read_bytes()
    examples = (materials / 'skill-candidate/nature-shared/core/robotics-writing-examples.md').read_text(encoding='utf-8')
    for name in re.findall(r'^\[[^\]]+\]: <\.\./\.\./\.\./(.*?)>$', examples, re.M):
        assert (materials / name).is_file(), name
    runtime = Path(tempfile.mkdtemp(prefix=stage + '-')) / 'materials'
    shutil.copytree(materials, runtime)
    required = tuple('inputs/' + name for name in ('task.md', 'scientific-facts.md', 'personal-experience.txt',
                                                  'core-requirements.txt', 'abstract-writing-method.txt'))
    if draft is not None:
        required += ('inputs/current-draft.md',)
    reader = runpy.run_path(str(ROOT / 'effect-test/E03-independent-transfer-fd7dbcb-valid-2026-10-04/execute_once.py'))
    reader['read_required_inputs'].__globals__.update({'RECORD': dest, 'REQUIRED_INPUTS': required,
                                                    'save': lambda name, obj: save(dest / name, obj)})
    returned = reader['read_required_inputs'](runtime, phase='before-invocation')
    prompt = (
        f"Complete the Abstract-only task at {runtime / 'inputs/task.md'} using only the frozen local "
        f"{role} at {runtime / ('skill-candidate/' + role + '/SKILL.md')} and its declared dependencies. "
        "Read its router, manifest, required core, matching fragments, robotics common instructions and task index, "
        "then only selected cards with their real English, analysis and selection notes. Declared reference PDFs and "
        "verified analysis/reading texts are available on demand. Reference science does not add author facts. "
        "Only the material directory is permitted input. Do not read installed skills, the source project, "
        "target original paper/abstract, source locators, historical revisions, feedback, diagnoses, evaluations or "
        "execution records. Do not browse or change files. This invocation performs only the " + role +
        " stage; the execution layer handles any subsequent delivery stage separately. Return complete English abstract, accurate Chinese translation "
        "and necessary author notes. Read UTF-8 using absolute paths and bounded numbered ranges, one file per command. "
        "Always wrap indexed Get-Content in @(...) and verify actual returned content. This is a fresh first-pass "
        "session; there is no feedback or selection. The following normal author inputs were compared line by line "
        "with actual PowerShell returns and are included in full:\n"
    )
    for name in required:
        prompt += '\n<original-input path=' + json.dumps(name) + '>\n' + (runtime / name).read_text(encoding='utf-8') + '\n</original-input>\n'
    command = json.loads((PRIOR / 'drafting/execution-command.json').read_text(encoding='utf-8'))
    command[0] = subprocess.check_output(['powershell', '-NoProfile', '-Command', '(Get-Command codex).Source']).decode('utf-8-sig').strip()
    assert command[0] and Path(command[0]).suffix == '.exe'
    command[command.index('-C') + 1] = str(runtime)
    command[command.index('-o') + 1] = str(dest / 'first-output.md')
    command[-1] = prompt
    # Retain all prior isolation settings, additionally disable currently discoverable skills.
    installed = []
    for base in (Path('C:/Users/user/.agents/skills'), Path('C:/Users/user/.codex/skills')):
        if base.exists():
            installed.extend(p.as_posix() for p in base.rglob('SKILL.md'))
    previous_disabled = next(x for x in command if x.startswith('skills.config='))
    command[command.index(previous_disabled)] = 'skills.config=[' + ','.join(
        '{path=' + json.dumps(p) + ',enabled=false}' for p in sorted(set(installed))) + ']'
    (dest / 'execution-prompt.txt').write_text(prompt, encoding='utf-8')
    (dest / 'runner-snapshot.py').write_bytes(Path(__file__).read_bytes())
    save(dest / 'execution-command.json', command)
    save(dest / 'frozen-run.json', {
        'candidate_commit': commit, 'stage': stage, 'role': role, 'model': MODEL, 'reasoning_effort': EFFORT,
        'attempt': 1, 'new_paper_transfer_evidence': False, 'materials_sha256': inventory(materials),
        'candidate_sha256': candidate, 'reused_sources': reused, 'required_input_actual_returns': returned,
        'runtime': str(runtime), 'prompt_sha256': digest(dest / 'execution-prompt.txt'),
        'runner_sha256': digest(Path(__file__)), 'cli_sha256': digest(Path(command[0])),
        'cli_version': subprocess.check_output([command[0], '--version']).decode().strip(),
        'isolation': 'Material-only external directory and disabled automatic context; explicit read audit, no OS read sandbox claimed.',
    })
    print('Prepared once:', stage, commit)


def run(stage):
    dest = RECORD / stage
    assert not (dest / 'events.jsonl').exists(), 'Never rerun a stage'
    frozen = json.loads((dest / 'frozen-run.json').read_text(encoding='utf-8'))
    runtime = Path(frozen['runtime'])
    assert inventory(runtime) == inventory(dest / 'materials') == frozen['materials_sha256']
    assert digest(Path(__file__)) == frozen['runner_sha256']
    cmd = json.loads((dest / 'execution-command.json').read_text(encoding='utf-8'))
    started = time.time()
    with (dest / 'events.jsonl').open('xb') as out, (dest / 'stderr.txt').open('xb') as err:
        try:
            code = subprocess.run(cmd, stdin=subprocess.DEVNULL, stdout=out, stderr=err, cwd=runtime,
                                  env={**os.environ, 'PYTHONUTF8': '1'}, timeout=1200).returncode
        except subprocess.TimeoutExpired:
            code = 124
    save(dest / 'run-meta.json', {'exit_code': code, 'duration_seconds': round(time.time()-started, 2),
        'attempt': 1, 'first_output_exists': (dest / 'first-output.md').is_file(),
        'first_output_sha256': digest(dest / 'first-output.md') if (dest / 'first-output.md').is_file() else None})
    print(stage, 'exit', code)
    if code:
        raise SystemExit(code)


def audit(stage):
    dest = RECORD / stage
    frozen = json.loads((dest / 'frozen-run.json').read_text(encoding='utf-8'))
    runtime = Path(frozen['runtime'])
    commands, outside, reads, terminal = [], [], {}, None
    for line in (dest / 'events.jsonl').read_text(encoding='utf-8').splitlines():
        event = json.loads(line)
        item = event.get('item', {})
        if event.get('type') != 'item.completed':
            continue
        if item.get('type') == 'agent_message':
            terminal = item['text']
        if item.get('type') != 'command_execution':
            continue
        cmd, output = item.get('command', ''), item.get('aggregated_output', '')
        commands.append({'id': item.get('id'), 'command': cmd, 'exit_code': item.get('exit_code'), 'output_characters': len(output)})
        if not re.search(r'Get-Content|\brg\b|read_text|read_bytes|fitz|pdftotext', cmd, re.I):
            continue
        for value in re.findall(r"[A-Za-z]:[\\/][^'\"\r\n]*?\.(?:md|yaml|txt|pdf|py|json)\b", cmd.replace('\\\\', '\\')):
            p = Path(value).resolve()
            if not p.is_relative_to(runtime):
                outside.append({'id': item.get('id'), 'path': str(p)})
            elif p.is_file():
                name = p.relative_to(runtime).as_posix()
                reads.setdefault(name, []).append(item.get('id'))
    output = (dest / 'first-output.md').read_text(encoding='utf-8')
    # Numbered line reads: verify content against actual returns, without assuming command paths imply full loading.
    coverage = {}
    for name in reads:
        if Path(name).suffix not in ('.md', '.yaml', '.txt'):
            continue
        lines = (runtime / name).read_text(encoding='utf-8').splitlines()
        seen = set()
        for raw in (dest / 'events.jsonl').read_text(encoding='utf-8').splitlines():
            item = json.loads(raw).get('item', {})
            if item.get('id') not in reads[name] or item.get('type') != 'command_execution':
                continue
            returned = item.get('aggregated_output', '')
            for i, content in enumerate(lines, 1):
                if f'{i}: {content}' in returned or (content and content in returned):
                    seen.add(i)
        coverage[name] = {'matching_returned_lines': sorted(seen), 'line_count': len(lines),
                          'limit': 'Nonempty exact content or numbered lines; raw events determine any ambiguous duplicate text.'}
    report = {'stage': stage, 'attempts': 1, 'model': MODEL, 'reasoning_effort': EFFORT,
              'first_output_sha256': digest(dest / 'first-output.md'),
              'first_output_matches_terminal_except_final_newline': terminal is not None and output.rstrip('\r\n') == terminal.rstrip('\r\n'),
              'materials_unchanged': inventory(dest / 'materials') == frozen['materials_sha256'],
              'runtime_unchanged': inventory(runtime) == frozen['materials_sha256'],
              'outside_explicit_reads': outside, 'read_commands': commands, 'loaded_paths': reads,
              'actual_return_coverage': coverage, 'effect_verdict': 'Not determined by execution or loading checks'}
    save(dest / 'audit.json', report)
    assert report['first_output_matches_terminal_except_final_newline'] and report['materials_unchanged'] and report['runtime_unchanged']
    print('Retained and audited', stage, 'outside explicit reads', len(outside))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['prepare', 'run', 'audit'])
    parser.add_argument('stage')
    parser.add_argument('--commit')
    parser.add_argument('--draft', type=Path)
    args = parser.parse_args()
    if args.action == 'prepare':
        assert args.commit
        prepare(args.stage, args.commit, args.draft)
    else:
        globals()[args.action](args.stage)
