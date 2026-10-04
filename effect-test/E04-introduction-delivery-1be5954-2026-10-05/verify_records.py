"""Verify retained first outputs and test scope; prose verdict belongs in the report."""
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
start=json.loads((record/'coordinator/experiment-state.json').read_text(encoding='utf-8'))
assert not git('diff','1be5954','--','skill-candidate')
assert not git('diff',start['local_head_and_origin_main_at_current_start'],'--','effect-test/E02-delivery-repair-2026-10-04','effect-test/E04-independent-delivery-1be5954-2026-10-04')
assert not git('diff','--name-only'), 'Only new records may change'
checks={}
threads=[]
for stage in ('drafting','polishing'):
    dest=record/stage
    frozen=json.loads((dest/'frozen-run.json').read_text(encoding='utf-8'))
    audit=json.loads((dest/'audit.json').read_text(encoding='utf-8'))
    loading=json.loads((dest/'loading-and-retention.json').read_text(encoding='utf-8'))
    meta=json.loads((dest/'run-meta.json').read_text(encoding='utf-8'))
    pre=json.loads((dest/'pre-invocation-identity.json').read_text(encoding='utf-8'))
    assert frozen['case']=='E04' and frozen['section']=='Introduction'
    assert frozen['candidate_commit']==identity['candidate_commit']
    assert frozen['model']=='gpt-6.1-sol' and frozen['reasoning_effort']=='high' and frozen['attempt']==1
    assert meta['exit_code']==0 and meta['first_output_sha256']==sha(dest/'first-output.md')
    assert audit['first_output_matches_terminal_except_final_newline'] and not audit['outside_explicit_reads']
    assert audit['materials_unchanged'] and audit['runtime_unchanged']
    assert all(loading['core_full_return_status'].values())
    assert all(x['all_lines_returned_verbatim'] for x in frozen['required_input_actual_returns']['inputs'])
    for name,expected in pre['all_normal_input_hashes_verified'].items():
        assert sha(dest/'materials/inputs'/name)==expected
    for name,h in frozen['candidate_sha256'].items():
        assert h==identity['candidate_git_bytes_sha256'][name]==sha(dest/'materials'/name)
    assert not any('/coordinator/' in name or '/source/' in name or 'first-output' in name for name in frozen['materials_sha256'])
    if stage=='polishing':
        assert (dest/'materials/inputs/current-draft.md').read_bytes()==(record/'drafting/raw-introduction-and-references.md').read_bytes()
    threads.append(loading['thread']['thread_id'])
    checks[stage]={'first_output_matches_log':True,'complete_original_inputs':True,'same_scientific_and_author_inputs':True,
                   'candidate_and_materials_unchanged':True,'no_outside_explicit_reads':True,
                   'mandatory_core_full_returns':True,'one_session':True,'first_output_sha256':sha(dest/'first-output.md')}
assert len(set(threads))==2
for src,dst in [('first-output.md','first-delivery.md'),('first-introduction.en.txt','introduction.en.txt'),
                ('first-introduction.zh.txt','introduction.zh.txt'),('first-references.md','references.md')]:
    assert (record/'polishing'/src).read_bytes()==(record/'delivery'/dst).read_bytes()
report=(record/'报告.md').read_text(encoding='utf-8')
for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',report):
    if target.startswith('https://') or target=='verification.json':
        continue
    assert (record/target).is_file(),target
secrets=[]
for p in record.rglob('*'):
    if p.is_file() and p.suffix in ('.md','.txt','.json','.jsonl','.py','.ps1'):
        if re.search(r'\b(?:sk-[A-Za-z0-9_-]{32,}|ghp_[A-Za-z0-9]{30,}|Bearer [A-Za-z0-9_-]{40,})\b',p.read_text(encoding='utf-8-sig')):
            secrets.append(p.relative_to(record).as_posix())
assert not secrets
out={'case':'E04','section':'Introduction','frozen_candidate_commit':identity['candidate_commit'],
     'current_origin_main_at_start':start['local_head_and_origin_main_at_current_start'],
     'stages':checks,'distinct_threads':threads,'only_new_record_files_changed':True,
     'candidate_E02_and_accepted_E04_abstract_unchanged':True,'exact_first_polishing_delivery_preserved':True,
     'feedback_reruns':0,'manual_English_or_Chinese_edits':0,
     'effect_scope':'Only this E04 Introduction first delivery; no other section or stability pass',
     'report_local_links_resolve':True,'credential_pattern_scan_findings':secrets,
     'synchronization_status':'Pre-sync checks; verify final local/origin equality after sync.ps1',
     'files_sha256':{p.relative_to(record).as_posix():sha(p) for p in sorted(record.rglob('*')) if p.is_file() and p.name!='verification.json'}}
target=record/'verification.json'
assert not target.exists()
target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Scope, identity, inputs, loading, immutable first outputs, handoff, links and credential-pattern checks passed')
