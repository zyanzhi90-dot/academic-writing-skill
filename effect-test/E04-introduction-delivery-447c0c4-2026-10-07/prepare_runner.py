"""Bind the existing one-shot executor to a new frozen record; no model call."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess

record = Path(__file__).resolve().parent
root = record.parents[1]
prior = root / 'effect-test/E04-introduction-delivery-ed9e42b-2026-10-07'
commit = '447c0c4165afb7fdc08a0458d534042a8704dc94'
old = 'ed9e42bd68634d611dab0874d07c0ec200cbaabd'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
git = lambda *a: subprocess.check_output(['git', *a], cwd=root)
assert git('rev-parse', 'HEAD').decode().strip() == commit
assert git('rev-parse', 'origin/main').decode().strip() == commit
copies = (
    'scientific-facts.md', 'background-facts.md', 'citation-facts.md', 'accepted-abstract.en.txt',
    'drafting-task.md', 'polishing-task.md', 'execute_once.py', 'retain_sections.py',
    'verify_stage.py', 'save_delivery.py', 'summarize_loading.py', 'index_outputs.py',
    'verify_git_bytes.py', 'check_context.py',
)
for name in copies:
    assert not (record / name).exists()
    shutil.copyfile(prior / name, record / name)
for name in ('preflight.py', 'verify_records.py'):
    text = (prior / name).read_text(encoding='utf-8').replace(old, commit)
    assert not (record / name).exists()
    (record / name).write_text(text, encoding='utf-8')

# Latest explicit author clarification is a normal requirement, not a diagnosis.
adjustment = (prior / 'current-author-adjustment.txt').read_text(encoding='utf-8')
clarification = (
    '当前有效作者澄清：目标是根据作者科学内容，模仿适用范例的逻辑组织、段落推进、连续句、句式和用词。'
    '表达应结合范例语境、科学关系及实际清晰度判断，不能仅凭动名词开句、代词或概括指代判错；'
    '也不能因语法成立就认定已对齐范例。\n'
)
assert not (record / 'current-author-adjustment.txt').exists()
(record / 'current-author-adjustment.txt').write_text(adjustment + '\n' + clarification, encoding='utf-8')

identity = json.loads((prior / 'coordinator/input-identity.json').read_text(encoding='utf-8'))
for name, expected in identity['author_inputs'].items():
    assert sha(root / name) == expected, name
identity.pop('diagnosis_start_commit', None)
identity.update({
    'candidate_commit': commit, 'coordinator_start_commit': commit, 'origin_main_at_start': commit,
    'candidate_git_bytes_sha256': {},
    'source_identity_record': (prior / 'coordinator/input-identity.json').relative_to(root).as_posix(),
    'source_identity_record_sha256': sha(prior / 'coordinator/input-identity.json'),
    'current_author_adjustment_sha256': sha(record / 'current-author-adjustment.txt'),
    'latest_author_clarification': clarification.strip(),
})
for name in filter(None, git('ls-tree', '-r', '--name-only', '-z', commit, 'skill-candidate').decode().split('\0')):
    identity['candidate_git_bytes_sha256'][name] = hashlib.sha256(git('show', commit + ':' + name)).hexdigest()
(record / 'coordinator').mkdir()
(record / 'coordinator/input-identity.json').write_text(json.dumps(identity, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
(record / 'coordinator/experiment-state.json').write_text(json.dumps({
    'local_head_and_origin_main_at_start': commit, 'frozen_candidate': commit,
    'model': 'gpt-6.1-sol', 'reasoning_effort': 'high', 'stages': ['drafting', 'polishing'],
    'one_invocation_per_stage': True, 'first_outputs_only': True,
    'feedback_reruns_allowed': False, 'coordinator_prose_edits_allowed': False,
    'Skill_changes_or_installation_allowed': False,
}, indent=2) + '\n', encoding='utf-8')
(record / 'runner-provenance.json').write_text(json.dumps({
    'candidate_commit': commit, 'source_record': prior.relative_to(root).as_posix(),
    'byte_identical_copies': {n: {'source_sha256': sha(prior / n), 'copy_sha256': sha(record / n)} for n in copies},
    'executor_byte_identical': sha(prior / 'execute_once.py') == sha(record / 'execute_once.py'),
    'adaptations': 'New record and candidate metadata bindings; latest explicit contextual author clarification appended to the normal author override. Execution, transport, task requests and isolation unchanged.',
    'author_adjustment': {'source_sha256': sha(prior / 'current-author-adjustment.txt'), 'current_sha256': sha(record / 'current-author-adjustment.txt'), 'appended_author_text': clarification.strip()},
    'model': 'gpt-6.1-sol', 'reasoning_effort': 'high', 'one_invocation_per_stage': True,
    'diagnosis_or_preset_argument_supplied': False, 'prior_outputs_supplied': False,
    'scope': 'Known-case E04; unchanged science and root author inputs; current explicit author requirements.',
}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('Existing executor and unchanged scientific inputs prepared; no model invoked.')
