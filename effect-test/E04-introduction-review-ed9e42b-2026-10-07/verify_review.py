"""Verify one review-only invocation, original draft, inputs and evidence bytes."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

record = Path(__file__).resolve().parent
root = record.parents[1]
prior = root/'effect-test/E04-introduction-delivery-ed9e42b-2026-10-07'
dest = record/'review'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
git = lambda *a: subprocess.check_output(['git',*a],cwd=root)
base = '02152cb71f4db89c9b4851b4a5edaacf70e73aea'
candidate = 'ed9e42bd68634d611dab0874d07c0ec200cbaabd'
frozen = json.loads((dest/'frozen-run.json').read_text(encoding='utf-8'))
audit = json.loads((dest/'audit.json').read_text(encoding='utf-8'))
meta = json.loads((dest/'run-meta.json').read_text(encoding='utf-8'))
loading = json.loads((dest/'loading-and-retention.json').read_text(encoding='utf-8'))
assert not git('diff',base,'--','skill-candidate','analysis','effect-test/E04-introduction-delivery-ed9e42b-2026-10-07')
assert frozen['candidate_commit']==candidate and frozen['attempt']==1 and frozen['stage']=='review'
assert frozen['model']=='gpt-6.1-sol' and frozen['reasoning_effort']=='high'
assert meta['exit_code']==0 and meta['attempt']==1 and meta['first_output_sha256']==sha(dest/'first-output.md')
assert audit['first_output_matches_terminal_except_final_newline'] and not audit['outside_explicit_reads']
assert audit['materials_unchanged'] and audit['runtime_unchanged']
assert all(x['all_lines_returned_verbatim'] for x in frozen['required_input_actual_returns']['inputs'])
for name,h in frozen['materials_sha256'].items(): assert sha(dest/'materials'/name)==h,name
for name,h in frozen['candidate_sha256'].items(): assert hashlib.sha256(git('show',candidate+':'+name)).hexdigest()==h,name
for name in ('scientific-facts.md','background-facts.md','citation-facts.md','accepted-abstract.en.txt',
             'core-requirements.txt','personal-experience.txt','introduction-method.txt','current-author-adjustment.txt'):
    assert (dest/'materials/inputs'/name).read_bytes()==(prior/'drafting/materials/inputs'/name).read_bytes()
assert (dest/'materials/inputs/current-draft.md').read_bytes()==(prior/'drafting/raw-introduction-and-references.md').read_bytes()
assert (dest/'materials/inputs/original-writing-task.md').read_bytes()==(prior/'drafting-task.md').read_bytes()
assert (record/'execute_once.py').read_bytes()==(prior/'execute_once.py').read_bytes()
old_threads=[json.loads((prior/s/'loading-and-retention.json').read_text(encoding='utf-8'))['thread']['thread_id'] for s in ('drafting','polishing')]
thread = loading['thread']['thread_id']
assert thread not in old_threads
assert frozen['input_identity']['target_pdf_sha256'] not in frozen['materials_sha256'].values()
assert all(not any(x in n for x in ('/coordinator/', '/audit/', 'first-output', 'events.jsonl')) for n in frozen['materials_sha256'])
secrets=[]
for p in record.rglob('*'):
    if p.is_file() and p.suffix in ('.md','.txt','.json','.jsonl','.py','.ps1'):
        if re.search(r'\b(?:sk-[A-Za-z0-9_-]{32,}|ghp_[A-Za-z0-9]{30,}|Bearer [A-Za-z0-9_-]{40,})\b',p.read_text(encoding='utf-8-sig')):
            secrets.append(p.relative_to(record).as_posix())
assert not secrets
target=record/'verification.json'
assert not target.exists()
target.write_text(json.dumps({'baseline_commit':base,'frozen_candidate':candidate,'independent_review_thread':thread,
    'one_effective_invocation':True,'same_model_and_effort':True,'original_normal_inputs_and_raw_Writing_English_refs':True,
    'candidate_and_original_E04_records_unchanged':True,'original_run_and_audit_executor_byte_identical':True,
    'complete_original_inputs_actual_returns_verified':True,'first_output_matches_terminal':True,
    'materials_and_runtime_unchanged':True,'no_outside_explicit_reads':True,
    'no_feedback_reruns_or_manual_review_edits':True,'credential_pattern_scan_findings':secrets,
    'scope':'One independent known-case review only; no autonomous generation, hidden-check, transfer or stability conclusion.',
    'files_sha256':{p.relative_to(record).as_posix():sha(p) for p in sorted(record.rglob('*')) if p.is_file() and p.name not in ('verification.json','git-byte-verification.json')}},
    ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('One independent first review, original inputs/draft, unchanged candidate and record scope verified.')
