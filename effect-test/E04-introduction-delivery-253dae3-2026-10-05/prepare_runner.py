"""Freeze accepted candidate; reuse E04 inputs and established isolated runner."""
from pathlib import Path
import difflib
import hashlib
import json
import shutil
import subprocess

record = Path(__file__).resolve().parent
root = record.parents[1]
prior = root / 'effect-test/E04-introduction-delivery-1be5954-2026-10-05'
mechanism = root / 'effect-test/E04-introduction-delivery-3081815-2026-10-05'
commit = subprocess.check_output(['git', 'rev-parse', '253dae3'], cwd=root).decode().strip()
assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root).decode().strip() == commit
assert subprocess.check_output(['git', 'rev-parse', 'origin/main'], cwd=root).decode().strip() == commit
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

for name in ('scientific-facts.md', 'background-facts.md', 'citation-facts.md', 'accepted-abstract.en.txt'):
    assert not (record / name).exists()
    shutil.copyfile(prior / name, record / name)
for name in ('drafting-task.md', 'polishing-task.md', 'verify_stage.py', 'retain_sections.py',
             'save_delivery.py', 'summarize_loading.py', 'verify_records.py', 'preflight.py', 'verify_git_bytes.py'):
    assert not (record / name).exists()
    shutil.copyfile(mechanism / name, record / name)

task = record / 'drafting-task.md'
text = task.read_text(encoding='utf-8').replace(
    '并保持相邻段落之间的递进关系。',
    '每段结合适用范例的真实段落、连续句、句式和用词，使各段按科学关系递进，核心设计得到充分的采用理由。')
task.write_text(text, encoding='utf-8')
for name in ('drafting-task.md', 'polishing-task.md'):
    p = record / name
    p.write_text(p.read_text(encoding='utf-8').replace(
        '按《核心要求.txt》《我自己的经验和做法.txt》',
        '按《核心要求.txt》《我自己的经验和做法.txt》《引言写作方法.txt》'), encoding='utf-8')

identity = json.loads((prior / 'coordinator/input-identity.json').read_text(encoding='utf-8'))
identity.update({'candidate_commit': commit, 'coordinator_start_commit': commit,
                 'origin_main_at_start': commit,
                 'selection_basis': 'Known-case E04 comparison with byte-identical previously accepted inputs.',
                 'candidate_git_bytes_sha256': {},
                 'author_inputs': {name: sha(root / name) for name in
                                  ('核心要求.txt', '我自己的经验和做法.txt', '引言写作方法.txt')},
                 'task_sha256': {stage: sha(record / (stage + '-task.md')) for stage in ('drafting', 'polishing')},
                 'source_identity_record': (prior / 'coordinator/input-identity.json').relative_to(root).as_posix(),
                 'source_identity_record_sha256': sha(prior / 'coordinator/input-identity.json'),
                 'validation_scope': 'Known-case comparison; not migration, reliable omission detection or stability evidence'})
for name in filter(None, subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', '-z', commit,
                    'skill-candidate'], cwd=root).decode('utf-8').split('\0')):
    identity['candidate_git_bytes_sha256'][name] = hashlib.sha256(
        subprocess.check_output(['git', 'show', commit + ':' + name], cwd=root)).hexdigest()
(record / 'coordinator').mkdir()
(record / 'coordinator/input-identity.json').write_text(json.dumps(identity, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
(record / 'coordinator/experiment-state.json').write_text(json.dumps({
    'local_head_and_origin_main_at_current_start': commit, 'frozen_candidate': commit,
    'model': 'gpt-6.1-sol', 'reasoning_effort': 'high', 'stages': ['drafting', 'polishing'],
    'one_invocation_per_stage': True, 'first_outputs_only': True,
    'feedback_reruns_allowed': False, 'coordinator_prose_edits_allowed': False,
    'Skill_changes_or_installation_allowed': False}, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

original = (mechanism / 'execute_once.py').read_text(encoding='utf-8')
code = original.replace("'core-requirements.txt': ROOT / '核心要求.txt',",
                         "'core-requirements.txt': ROOT / '核心要求.txt',\n        'introduction-method.txt': ROOT / '引言写作方法.txt',")
code = code.replace("'core-requirements.txt', 'background-facts.md'",
                    "'core-requirements.txt', 'introduction-method.txt', 'background-facts.md'")
code = code.replace("    (dest / 'execution-prompt.txt').write_text(prompt, encoding='utf-8')",
                    "    assert len(subprocess.list2cmdline(command).encode('utf-16-le')) // 2 < 32767, 'Windows command line limit'\n    (dest / 'execution-prompt.txt').write_text(prompt, encoding='utf-8')")
(record / 'execute_once.py').write_text(code, encoding='utf-8')
(record / 'runner-adaptation.diff').write_text(''.join(difflib.unified_diff(
    original.splitlines(True), code.splitlines(True), fromfile='E04 established isolated runner',
    tofile='E04 frozen 253dae3 runner')), encoding='utf-8')
for name in ('preflight.py', 'verify_records.py', 'verify_git_bytes.py'):
    p = record / name
    code = p.read_text(encoding='utf-8').replace('3081815176c8e3fc130db8832b8a13677f591cdd', commit).replace('3081815', '253dae3')
    if name == 'preflight.py':
        code = code.replace("identity['candidate_commit']==frozen['candidate_commit']==",
                            "identity['candidate_commit']==subprocess.check_output(['git','rev-parse',frozen['candidate_commit']],cwd=root).decode().strip()==")
        code = code.replace("'personal-experience.txt':identity['author_inputs']['我自己的经验和做法.txt'],",
                            "'personal-experience.txt':identity['author_inputs']['我自己的经验和做法.txt'],\n    'introduction-method.txt':identity['author_inputs']['引言写作方法.txt'],")
    if name == 'verify_records.py':
        code = code.replace("assert frozen['candidate_commit']==identity['candidate_commit']",
                            "assert git('rev-parse',frozen['candidate_commit']).decode().strip()==identity['candidate_commit']")
    p.write_text(code, encoding='utf-8')
p = record / 'save_delivery.py'
p.write_text(p.read_text(encoding='utf-8').replace("'startup_process_creation_failures':1", "'startup_process_creation_failures':0"), encoding='utf-8')

provenance = {'candidate_commit': commit, 'source_record': prior.relative_to(root).as_posix(),
    'execution_mechanism_source': mechanism.relative_to(root).as_posix(),
    'input_copies': {name: {'source_sha256': sha(prior / name), 'copy_sha256': sha(record / name),
                         'byte_identical': (prior / name).read_bytes() == (record / name).read_bytes()}
                    for name in ('scientific-facts.md', 'background-facts.md', 'citation-facts.md', 'accepted-abstract.en.txt')},
    'runner_source_sha256': sha(mechanism / 'execute_once.py'), 'runner_sha256': sha(record / 'execute_once.py'),
    'changes': 'Add current author Introduction requirement input and pre-launch Windows length guard; retain stdin and isolation settings.',
    'mainline_or_repair_supplied': False, 'model': 'gpt-6.1-sol', 'reasoning_effort': 'high',
    'one_invocation_per_stage': True, 'historical_records_changed': False,
    'scope': 'Only new effect-test records; no Skill edits or installation'}
(record / 'runner-provenance.json').write_text(json.dumps(provenance, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print('Prepared accepted candidate and normal author inputs; no model invoked.')
