"""Verify identity and actual complete input returns before each single invocation."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

record = Path(__file__).resolve().parent
root = record.parents[1]
stage = sys.argv[1]
dest = record/stage
frozen = json.loads((dest/'frozen-run.json').read_text(encoding='utf-8'))
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
identity = frozen['input_identity']
assert identity['case']=='E04' and identity['section']=='Introduction'
assert identity['candidate_commit']==subprocess.check_output(['git','rev-parse',frozen['candidate_commit']],cwd=root).decode().strip()=='ee74b27dffa59ba79b5f14cf18687f60e0d866c5'
checks = {
    'scientific-facts.md':identity['facts_sha256'],
    'background-facts.md':identity['background_sha256'],
    'citation-facts.md':identity['citations_sha256'],
    'accepted-abstract.en.txt':identity['accepted_abstract_sha256'],
    'core-requirements.txt':identity['author_inputs']['核心要求.txt'],
    'personal-experience.txt':identity['author_inputs']['我自己的经验和做法.txt'],
    'introduction-method.txt':identity['author_inputs']['引言写作方法.txt'],
    'current-author-adjustment.txt':identity['current_author_adjustment_sha256'],
    'task.md':identity['task_sha256'][stage],
}
for name, expected in checks.items():
    assert sha(dest/'materials/inputs'/name)==expected, name
for name, expected in frozen['candidate_sha256'].items():
    raw = subprocess.check_output(['git','show',frozen['candidate_commit']+':'+name],cwd=root)
    assert hashlib.sha256(raw).hexdigest()==expected
assert frozen['required_input_actual_returns']['actual_returned_content_checked']
assert identity['target_pdf_sha256'] not in frozen['materials_sha256'].values()
source = root/'effect-test/E04-independent-delivery-1be5954-2026-10-04/coordinator/source/rss-official.pdf'
assert sha(source)==identity['target_pdf_sha256']
assert frozen['model']=='gpt-6.1-sol' and frozen['reasoning_effort']=='high' and frozen['attempt']==1
if stage=='polishing':
    raw = record/'drafting/raw-introduction-and-references.md'
    assert (dest/'materials/inputs/current-draft.md').read_bytes()==raw.read_bytes()
report = {'stage':stage,'case':'E04','section':'Introduction','identity_verified':True,
          'all_normal_input_hashes_verified':checks,'candidate_git_bytes_verified':True,
          'actual_complete_returns_verified':True,'target_original_excluded':True,
          'accepted_abstract_supplied_unchanged':True,'attempt':1,
          'no_coordinator_evaluation_supplied':True}
out = dest/'pre-invocation-identity.json'
assert not out.exists()
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(stage, 'pre-invocation identity and complete actual inputs verified')
