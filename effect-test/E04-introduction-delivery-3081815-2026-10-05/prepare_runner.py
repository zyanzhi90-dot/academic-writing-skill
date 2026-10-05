"""Reuse E04 Introduction inputs and the one-shot isolated runner unchanged in substance."""
from pathlib import Path
import difflib
import hashlib
import json
import shutil
import subprocess

record = Path(__file__).resolve().parent
root = record.parents[1]
prior = root / 'effect-test/E04-introduction-delivery-1be5954-2026-10-05'
commit = subprocess.check_output(['git', 'rev-parse', '3081815'], cwd=root).decode().strip()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

for name in ('scientific-facts.md', 'background-facts.md', 'citation-facts.md',
             'accepted-abstract.en.txt', 'drafting-task.md', 'polishing-task.md',
             'verify_stage.py', 'retain_sections.py', 'save_delivery.py'):
    assert not (record/name).exists()
    shutil.copyfile(prior/name, record/name)

# The request specifies a full-section scientific line followed by paragraph drafting.
# This is a normal author request, with no supplied line, paragraph map or remedy.
p = record/'drafting-task.md'
p.write_text(p.read_text(encoding='utf-8').replace(
    '先确定科学内容与整节思路，再逐段起草。',
    '先自主确定整节的科学主线与各段任务，再沿该主线逐段起草，并保持相邻段落之间的递进关系。一次交付完整 Introduction。'
), encoding='utf-8')

identity = json.loads((prior/'coordinator/input-identity.json').read_text(encoding='utf-8'))
identity['candidate_commit'] = commit
identity['candidate_git_bytes_sha256'] = {}
for name in filter(None, subprocess.check_output(
        ['git', 'ls-tree', '-r', '--name-only', '-z', commit,
         'skill-candidate/nature-writing', 'skill-candidate/nature-polishing',
         'skill-candidate/nature-shared'], cwd=root).decode().split('\0')):
    identity['candidate_git_bytes_sha256'][name] = hashlib.sha256(
        subprocess.check_output(['git', 'show', commit+':'+name], cwd=root)).hexdigest()
identity['author_inputs'] = {name: sha(root/name) for name in ('核心要求.txt', '我自己的经验和做法.txt')}
identity['task_sha256'] = {stage:sha(record/(stage+'-task.md')) for stage in ('drafting','polishing')}
identity['source_identity_record'] = (prior/'coordinator/input-identity.json').relative_to(root).as_posix()
identity['source_identity_record_sha256'] = sha(prior/'coordinator/input-identity.json')
identity['validation_scope'] = 'Known-case comparison; not migration, reliable omission detection or stability evidence'
(record/'coordinator').mkdir()
(record/'coordinator/input-identity.json').write_text(json.dumps(identity,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

original = (prior/'execute_once.py').read_text(encoding='utf-8')
code = original.replace(
    "ROOT / 'effect-test/E04-independent-delivery-1be5954-2026-10-04/drafting'",
    "ROOT / 'effect-test/E04-introduction-delivery-1be5954-2026-10-05/drafting'")
code = code.replace("'new_paper_transfer_evidence': True", "'new_paper_transfer_evidence': False, 'known_case_comparison': True")
(record/'execute_once.py').write_text(code,encoding='utf-8')
(record/'runner-adaptation.diff').write_text(''.join(difflib.unified_diff(
    original.splitlines(True),code.splitlines(True),fromfile='E04 prior runner',tofile='E04 frozen 3081815 runner')),encoding='utf-8')
preflight = (prior/'preflight.py').read_text(encoding='utf-8').replace(
    '1be5954bdcbd24c9d7bbc390441cb34bd9dc4f72', commit)
(record/'preflight.py').write_text(preflight,encoding='utf-8')
provenance = {'candidate_commit':commit, 'source_record':prior.relative_to(root).as_posix(),
    'input_copies':{name:{'source_sha256':sha(prior/name),'copy_sha256':sha(record/name),
                        'byte_identical':(prior/name).read_bytes()==(record/name).read_bytes()}
                   for name in ('scientific-facts.md','background-facts.md','citation-facts.md','accepted-abstract.en.txt')},
    'runner_source_sha256':sha(prior/'execute_once.py'), 'runner_sha256':sha(record/'execute_once.py'),
    'scope':'Only this new effect-test record; no Skill edits or installation',
    'mainline_or_repair_supplied':False, 'model':'gpt-6.1-sol', 'reasoning_effort':'high',
    'one_invocation_per_stage':True, 'historical_records_changed':False}
(record/'runner-provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Prepared normal inputs and adapted prior isolated one-shot runner; no model invoked.')
