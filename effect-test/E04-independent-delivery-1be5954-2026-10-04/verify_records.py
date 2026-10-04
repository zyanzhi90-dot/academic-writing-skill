"""Final immutable-output, scope, handoff and artifact checks before sync."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

RECORD=Path(__file__).resolve().parent
ROOT=RECORD.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
git=lambda *a:subprocess.check_output(['git',*a],cwd=ROOT)
identity=json.loads((RECORD/'coordinator/input-identity.json').read_text(encoding='utf-8'))
assert sha(RECORD/'scientific-facts.md')==identity['facts_sha256']
assert not git('diff','1be5954','--','skill-candidate')
assert not git('diff','7f1ff90','--','effect-test/E02-delivery-repair-2026-10-04')
assert not git('diff','--name-only'), 'All project changes should be new E04 records'
threads=[]
checks={}
for stage in ('drafting','polishing'):
    p=RECORD/stage
    f=json.loads((p/'frozen-run.json').read_text(encoding='utf-8'))
    a=json.loads((p/'audit.json').read_text(encoding='utf-8'))
    l=json.loads((p/'loading-and-retention.json').read_text(encoding='utf-8'))
    m=json.loads((p/'run-meta.json').read_text(encoding='utf-8'))
    assert f['case']=='E04' and f['candidate_commit']==identity['candidate_commit']
    assert f['model']=='gpt-6.1-sol' and f['reasoning_effort']=='high' and f['attempt']==1
    assert m['exit_code']==0 and m['first_output_sha256']==sha(p/'first-output.md')
    assert a['first_output_matches_terminal_except_final_newline'] and not a['outside_explicit_reads']
    assert a['materials_unchanged'] and a['runtime_unchanged']
    assert all(l['core_full_return_status'].values())
    assert sha(p/'materials/inputs/scientific-facts.md')==identity['facts_sha256']
    assert all(x['all_lines_returned_verbatim'] for x in f['required_input_actual_returns']['inputs'])
    for role,path in [('core-requirements.txt','核心要求.txt'),('personal-experience.txt','我自己的经验和做法.txt'),('abstract-writing-method.txt','摘要写作方法.txt')]:
        assert sha(p/'materials/inputs'/role)==identity['author_inputs'][path]==sha(ROOT/path)
    for name,h in f['candidate_sha256'].items():
        assert identity['candidate_git_bytes_sha256'][name]==h==sha(p/'materials'/name)
    assert not any('/coordinator/' in name or '/source/' in name or 'first-output' in name for name in f['materials_sha256'])
    if stage=='polishing':
        assert (p/'materials/inputs/current-draft.md').read_bytes()==(RECORD/'drafting/first-abstract.en.txt').read_bytes()
    threads.append(l['thread']['thread_id'])
    checks[stage]={'first_output_matches_log':True,'all_original_inputs_complete':True,'facts_and_author_inputs_identical':True,
                   'candidate_and_declared_materials_unchanged':True,'no_outside_explicit_reads':True,
                   'core_full_returns':True,'one_session':True,'first_output_sha256':sha(p/'first-output.md')}
assert len(set(threads))==2
for src,dst in [('first-output.md','first-delivery.md'),('first-abstract.en.txt','abstract.en.txt'),('first-abstract.zh.txt','abstract.zh.txt')]:
    assert (RECORD/'polishing'/src).read_bytes()==(RECORD/'delivery'/dst).read_bytes()
report=(RECORD/'报告.md').read_text(encoding='utf-8')
for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',report):
    if target.startswith('https://') or target=='verification.json':
        continue
    assert (RECORD/target).is_file(),target
secrets=[]
for p in RECORD.rglob('*'):
    if p.is_file() and p.suffix in ('.md','.txt','.json','.jsonl','.py','.ps1'):
        text=p.read_text(encoding='utf-8-sig')
        if re.search(r'\b(?:sk-[A-Za-z0-9_-]{32,}|ghp_[A-Za-z0-9]{30,}|Bearer [A-Za-z0-9_-]{40,})\b',text):
            secrets.append(p.relative_to(RECORD).as_posix())
assert not secrets
out={'case':'E04','frozen_candidate_commit':identity['candidate_commit'],
     'preparation_origin_main':identity['origin_main_at_start'],'stages':checks,'distinct_threads':threads,
     'only_new_E04_records_changed':True,'candidate_and_E02_history_unchanged':True,
     'exact_first_polishing_delivery_preserved':True,'feedback_reruns':0,'manual_English_or_Chinese_edits':0,
     'mandatory_human_prose_adjustments_identified':0,'effect_scope':'This one E04 Abstract; no capability/stability generalization',
     'report_local_links_resolve':True,'credential_pattern_scan_findings':secrets,
     'synchronization_status':'Pre-sync verification; final local/origin equality must be checked after sync.ps1',
     'files_sha256':{p.relative_to(RECORD).as_posix():sha(p) for p in sorted(RECORD.rglob('*')) if p.is_file() and p.name!='verification.json'}}
dest=RECORD/'verification.json'
assert not dest.exists()
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Scope, immutable first outputs, original input identity, complete returns, loading, handoff, links and credential-pattern checks passed')
