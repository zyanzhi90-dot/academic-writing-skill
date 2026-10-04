"""Coordinator-only source and input checks, before either model invocation."""
from pathlib import Path
import hashlib
import json
import subprocess
import fitz

RECORD = Path(__file__).resolve().parents[1]
ROOT = RECORD.parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
git = lambda *a: subprocess.check_output(['git', *a], cwd=ROOT)
commit = '1be5954bdcbd24c9d7bbc390441cb34bd9dc4f72'
target = RECORD / 'coordinator/source/rss-official.pdf'
doc = fitz.open(target)
pages = []
for i, page in enumerate(doc, 1):
    text = page.get_text(sort=False)
    dest = RECORD / f'coordinator/source/page-{i:02}.txt'
    assert not dest.exists()
    dest.write_text(text, encoding='utf-8')
    pages.append({'page': i, 'path': dest.relative_to(ROOT).as_posix(), 'sha256': sha(dest)})
candidate = {}
for name in filter(None, git('ls-tree', '-r', '--name-only', '-z', commit, 'skill-candidate').decode('utf-8').split('\0')):
    raw = git('show', commit + ':' + name)
    assert (ROOT / name).read_bytes().replace(b'\r\n', b'\n') == raw.replace(b'\r\n', b'\n'), name
    candidate[name] = hashlib.sha256(raw).hexdigest()
target_names = [p.name for p in (ROOT / '文献资料').glob('*.pdf')]
assert not any('diffusion_policy' in name.lower() for name in target_names)
prior_targets = []
for p in (ROOT / 'effect-test').rglob('scientific-facts.md'):
    if RECORD in p.parents or 'materials' in p.parts:
        continue
    prior_targets.append(p.relative_to(ROOT).as_posix())
report = {
    'case': 'E04', 'paper': 'Diffusion Policy: Visuomotor Policy Learning via Action Diffusion',
    'version': 'RSS 2023 proceedings; not the IJRR extension',
    'primary_url': 'https://roboticsproceedings.org/rss19/p026.pdf',
    'additional_project_pdf_url': 'https://diffusion-policy.cs.columbia.edu/diffusion_policy_2023.pdf',
    'target_pdf_sha256': sha(target), 'target_pages': len(doc), 'pages': pages,
    'facts_sha256': sha(RECORD / 'scientific-facts.md'),
    'task_sha256': sha(RECORD / 'drafting-task.md'),
    'author_inputs': {name: sha(ROOT / name) for name in ['核心要求.txt', '我自己的经验和做法.txt', '摘要写作方法.txt']},
    'candidate_commit': commit, 'candidate_git_bytes_sha256': candidate,
    'coordinator_start_commit': git('rev-parse', 'HEAD').decode().strip(),
    'origin_main_at_start': git('rev-parse', 'origin/main').decode().strip(),
    'current_library_pdf_names': target_names,
    'selection_basis': 'Section 5.2: robot method paper absent as a library paper and absent as a prior test target; selected as E04 in this round. Citation mentions inside other papers do not imply a learned card or a target test. This is input isolation, not a claim of model-pretraining novelty.',
    'source_material_excluded_from_writers': True,
    'facts_categories_only': True, 'no_target_english_mainline_order_or_expression_guidance_in_facts': True,
}
dest = RECORD / 'coordinator/input-identity.json'
assert not dest.exists()
dest.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('E04 identity, source version, candidate unchanged and author inputs frozen')
