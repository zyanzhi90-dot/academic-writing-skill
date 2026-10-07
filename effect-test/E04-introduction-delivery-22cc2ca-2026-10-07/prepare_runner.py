"""Freeze current author inputs; bind the unchanged executor to one E04 run."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess

record = Path(__file__).resolve().parent
root = record.parents[1]
prior = root / 'effect-test/E04-introduction-delivery-447c0c4-2026-10-07'
commit = '22cc2ca4a7329e2a905a71e151ce589b114416e5'
old = '447c0c4165afb7fdc08a0458d534042a8704dc94'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
git = lambda *a: subprocess.check_output(['git', *a], cwd=root)

assert git('rev-parse', 'HEAD').decode().strip() == commit
assert git('rev-parse', 'origin/main').decode().strip() == commit
live = git('-c', 'http.proxy=', '-c', 'https.proxy=', 'ls-remote', 'origin', 'refs/heads/main').decode().split()[0]
assert live == commit
assert not git('diff', '--name-only') and not git('diff', '--cached', '--name-only')
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
    if name == 'verify_records.py':
        text = text.replace("'withdrawn_rule_override':'Latest explicit author adjustment supplied identically; original files preserved.'",
                            "'current_author_inputs':'Fresh root author files and root current-author-adjustment supplied identically; no historical override.'")
    assert not (record / name).exists()
    (record / name).write_text(text, encoding='utf-8')

author_names = ('核心要求.txt', '我自己的经验和做法.txt', '引言写作方法.txt', 'current-author-adjustment.txt')
author_inputs = {}
author_sources = {}
for name in author_names:
    source = root / name
    assert not (record / name).exists()
    shutil.copyfile(source, record / name)
    author_inputs[name] = sha(source)
    assert sha(record / name) == author_inputs[name]
    author_sources[name] = {
        'source': name, 'sha256': author_inputs[name], 'frozen_record_copy': name,
        'git_blob_at_frozen_commit': git('rev-parse', commit + ':' + name).decode().strip(),
        'last_change_commit': git('log', '-1', '--format=%H', commit, '--', name).decode().strip(),
        'git_bytes_match_root': hashlib.sha256(git('show', commit + ':' + name)).hexdigest() == author_inputs[name],
    }

previous = json.loads((prior / 'coordinator/input-identity.json').read_text(encoding='utf-8'))
# Reuse scientific provenance only; no previous author requirement or override is inherited.
science_keys = ('case', 'paper', 'version', 'primary_url', 'additional_project_pdf_url',
                'target_pdf_sha256', 'target_pages', 'pages', 'current_library_pdf_names',
                'source_material_excluded_from_writers', 'facts_categories_only',
                'no_target_english_mainline_order_or_expression_guidance_in_facts', 'section')
identity = {key: previous[key] for key in science_keys}
science_fields = {'facts_sha256': 'scientific-facts.md', 'background_sha256': 'background-facts.md',
                  'citations_sha256': 'citation-facts.md', 'accepted_abstract_sha256': 'accepted-abstract.en.txt'}
for key, name in science_fields.items():
    identity[key] = sha(record / name)
    assert identity[key] == previous[key]
identity.update({
    'candidate_commit': commit, 'coordinator_start_commit': commit, 'origin_main_at_start': live,
    'author_inputs': author_inputs, 'author_input_sources': author_sources,
    'current_author_adjustment_sha256': author_inputs['current-author-adjustment.txt'],
    'task_sha256': {s: sha(record / (s + '-task.md')) for s in ('drafting', 'polishing')},
    'candidate_git_bytes_sha256': {},
    'scientific_provenance_record': (prior / 'coordinator/input-identity.json').relative_to(root).as_posix(),
    'scientific_provenance_record_sha256': sha(prior / 'coordinator/input-identity.json'),
    'selection_basis': 'Confirmed E04 science, background, citations and accepted abstract reused byte-exact; current root author inputs freshly frozen.',
    'validation_scope': 'One known-case E04 Introduction run; no transfer or stability claim.',
    'author_input_conflict': 'Current root current-author-adjustment takes priority if any normal author text conflicts; no historical override inherited.',
})
for name in filter(None, git('ls-tree', '-r', '--name-only', '-z', commit, 'skill-candidate').decode().split('\0')):
    identity['candidate_git_bytes_sha256'][name] = hashlib.sha256(git('show', commit + ':' + name)).hexdigest()
(record / 'coordinator').mkdir()
def save(name, value):
    path = record / name
    assert not path.exists()
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
save('coordinator/input-identity.json', identity)
save('coordinator/experiment-state.json', {
    'local_head_and_live_origin_main_at_start': live, 'frozen_candidate': commit,
    'model': 'gpt-6.1-sol', 'reasoning_effort': 'high', 'stages': ['drafting', 'polishing'],
    'one_invocation_per_stage': True, 'first_outputs_only': True,
    'feedback_reruns_allowed': False, 'coordinator_prose_edits_allowed': False,
    'Skill_changes_or_installation_allowed': False, 'historical_author_override_supplied': False,
})
save('runner-provenance.json', {
    'candidate_commit': commit, 'source_record': prior.relative_to(root).as_posix(),
    'byte_identical_copies': {n: {'source_sha256': sha(prior / n), 'copy_sha256': sha(record / n)} for n in copies},
    'executor_byte_identical': sha(prior / 'execute_once.py') == sha(record / 'execute_once.py'),
    'adaptations': 'Preparation and audit commit bindings only; fresh current root author identity. Execution, transport, task requests and isolation unchanged.',
    'author_inputs': author_sources, 'historical_author_override_inherited': False,
    'model': 'gpt-6.1-sol', 'reasoning_effort': 'high', 'one_invocation_per_stage': True,
    'diagnosis_or_preset_argument_supplied': False, 'prior_outputs_supplied': False,
    'remote_check': {'live_main': live, 'transport': 'Per-command empty Git proxy; default local proxy unavailable'},
})
print('Current root author inputs freshly frozen; existing executor unchanged; no model invoked.')
