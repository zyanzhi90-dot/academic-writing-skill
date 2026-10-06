"""Verify execution provenance separately from the manual effect assessment."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

record=Path(__file__).resolve().parent
root=record.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
git=lambda *a:subprocess.check_output(['git',*a],cwd=root)
identity=json.loads((record/'coordinator/input-identity.json').read_text(encoding='utf-8'))
base=identity['candidate_commit']
assert base=='a29f1e1045bc86093e2f74a4fe288ba1e5970d76'
assert not git('diff',base,'--','skill-candidate')
assert not git('diff','--name-only'), 'Only new record files may change'
assert not git('diff',base,'--','effect-test/E04-introduction-delivery-253dae3-2026-10-05')
checks={}
threads=[]
shared_inputs=('scientific-facts.md','background-facts.md','citation-facts.md','accepted-abstract.en.txt',
               'core-requirements.txt','personal-experience.txt','introduction-method.txt','current-author-adjustment.txt')
for stage in ('drafting','polishing'):
    dest=record/stage
    frozen=json.loads((dest/'frozen-run.json').read_text(encoding='utf-8'))
    audit=json.loads((dest/'audit.json').read_text(encoding='utf-8'))
    loading=json.loads((dest/'loading-and-retention.json').read_text(encoding='utf-8'))
    meta=json.loads((dest/'run-meta.json').read_text(encoding='utf-8'))
    pre=json.loads((dest/'pre-invocation-identity.json').read_text(encoding='utf-8'))
    assert frozen['candidate_commit']==base and frozen['case']=='E04' and frozen['section']=='Introduction'
    assert frozen['model']=='gpt-6.1-sol' and frozen['reasoning_effort']=='high' and frozen['attempt']==1
    assert meta['exit_code']==0 and meta['first_output_sha256']==sha(dest/'first-output.md')
    assert audit['first_output_matches_terminal_except_final_newline'] and not audit['outside_explicit_reads']
    assert audit['materials_unchanged'] and audit['runtime_unchanged']
    assert all(x['all_lines_returned_verbatim'] for x in frozen['required_input_actual_returns']['inputs'])
    for name,expected in pre['all_normal_input_hashes_verified'].items():
        assert sha(dest/'materials/inputs'/name)==expected
    for name,h in frozen['candidate_sha256'].items():
        assert h==identity['candidate_git_bytes_sha256'][name]==sha(dest/'materials'/name)
    assert not any('/coordinator/' in n or '/audit/' in n or 'first-output' in n for n in frozen['materials_sha256'])
    assert identity['target_pdf_sha256'] not in frozen['materials_sha256'].values()
    if stage=='polishing':
        assert (dest/'materials/inputs/current-draft.md').read_bytes()==(record/'drafting/raw-introduction-and-references.md').read_bytes()
        for name in shared_inputs:
            assert (dest/'materials/inputs'/name).read_bytes()==(record/'drafting/materials/inputs'/name).read_bytes()
        extras=set(p.name for p in (dest/'materials/inputs').iterdir())-set(p.name for p in (record/'drafting/materials/inputs').iterdir())
        assert extras=={'current-draft.md'}
    threads.append(loading['thread']['thread_id'])
    checks[stage]={'execution_completed':True,'first_output_matches_log':True,'complete_original_inputs':True,
        'candidate_and_materials_unchanged':True,'no_outside_explicit_reads':True,'one_session':True,
        'core_full_return_status':loading['core_full_return_status'],
        'first_output_sha256':sha(dest/'first-output.md')}
assert len(set(threads))==2
for src,dst in [('first-output.md','first-delivery.md'),('first-introduction.en.txt','introduction.en.txt'),
                ('first-introduction.zh.txt','introduction.zh.txt'),('first-references.md','references.md')]:
    assert (record/'polishing'/src).read_bytes()==(record/'delivery'/dst).read_bytes()
report=(record/'报告.md').read_text(encoding='utf-8')
for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',report):
    if target.startswith(('https://','http://')) or target=='verification.json':
        continue
    assert (record/target.split('#')[0]).is_file(),target
secrets=[]
for p in record.rglob('*'):
    if p.is_file() and p.suffix in ('.md','.txt','.json','.jsonl','.py','.ps1'):
        if re.search(r'\b(?:sk-[A-Za-z0-9_-]{32,}|ghp_[A-Za-z0-9]{30,}|Bearer [A-Za-z0-9_-]{40,})\b',p.read_text(encoding='utf-8-sig')):
            secrets.append(p.relative_to(record).as_posix())
assert not secrets
target=record/'verification.json'
assert not target.exists()
target.write_text(json.dumps({'frozen_candidate_commit':base,'stages':checks,'distinct_threads':threads,
    'same_author_and_science_inputs':True,'Polishing_only_extra_author_input':'Writing original English and bibliography',
    'withdrawn_rule_override':'Latest explicit author adjustment supplied identically; original files preserved.',
    'only_new_record_files_changed':True,'candidate_and_previous_E04_unchanged':True,
    'exact_first_polishing_delivery_preserved':True,'feedback_reruns':0,'manual_prose_edits':0,
    'scope':'Known-case E04 only; execution/read evidence does not imply effect, transfer, reliable omission detection or stability.',
    'report_links_resolve':True,'credential_pattern_scan_findings':secrets,
    'files_sha256':{p.relative_to(record).as_posix():sha(p) for p in sorted(record.rglob('*')) if p.is_file() and p.name not in ('verification.json','git-byte-verification.json')},
    'sync_status':'Pre-sync verification; verify branch clean and local/live remote equality after sync.ps1'},
    ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('First outputs, input identities, handoff, independent sessions and record scope verified; prose verdict remains separate.')
