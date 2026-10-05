"""Keep the first independent Polishing delivery byte-exact, then freeze stage provenance."""
from pathlib import Path
import difflib
import hashlib
import json
import shutil

record=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
dest=record/'delivery'
assert not (dest/'provenance.json').exists()
dest.mkdir(exist_ok=True)
for source,name in [('first-output.md','first-delivery.md'),('first-introduction.en.txt','introduction.en.txt'),
                    ('first-introduction.zh.txt','introduction.zh.txt'),('first-references.md','references.md')]:
    if not (dest/name).exists():
        shutil.copyfile(record/'polishing'/source,dest/name)
    assert (record/'polishing'/source).read_bytes()==(dest/name).read_bytes()
stages={}
for stage in ('drafting','polishing'):
    p=record/stage
    f=json.loads((p/'frozen-run.json').read_text(encoding='utf-8'))
    l=json.loads((p/'loading-and-retention.json').read_text(encoding='utf-8'))
    events=[json.loads(s) for s in (p/'events.jsonl').read_text(encoding='utf-8').splitlines()]
    en=(p/'first-introduction.en.txt').read_text(encoding='utf-8').strip()
    stages[stage]={'thread_id':l['thread']['thread_id'],'candidate_commit':f['candidate_commit'],
        'model':f['model'],'reasoning_effort':f['reasoning_effort'],'first_output_sha256':sha(p/'first-output.md'),
        'English_sha256':sha(p/'first-introduction.en.txt'),'Chinese_sha256':sha(p/'first-introduction.zh.txt'),
        'word_count':len(en.split()),'paragraph_count':len(en.split('\n\n')),
        'run_meta':json.loads((p/'run-meta.json').read_text(encoding='utf-8')),
        'usage':[e.get('usage') for e in events if e.get('type')=='turn.completed'],
        'core_return_checks':l['core_full_return_status']}
assert stages['drafting']['thread_id']!=stages['polishing']['thread_id']
a=(record/'drafting/first-introduction.en.txt').read_text(encoding='utf-8')
b=(record/'polishing/first-introduction.en.txt').read_text(encoding='utf-8')
(dest/'English-stage-diff.patch').write_text(''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),
    fromfile='Drafting first Introduction',tofile='Polishing first Introduction')),encoding='utf-8')
out={'case':'E04','section':'Introduction','stages':stages,'combined_delivery_source':'polishing/first-output.md',
     'delivery_file_hashes':{p.name:sha(p) for p in dest.iterdir() if p.is_file()},'writer_invocations':2,
     'startup_process_creation_failures':1,'startup_model_sessions':0,
     'feedback_reruns':0,'English_manual_edits':0,'Chinese_manual_edits':0,'manual_content_or_order_feedback':0,
     'coordinator_operation':'Exact section separation and copy; no prose revision',
     'separate_statuses_required':True,'stability_pass_not_inferred':True,
     'evaluation_timing':'Both complete first outputs saved before coordinator prose evaluation',
     'validation_scope':'Known-case comparison; no migration, reliable omission detection or stability pass'}
(dest/'provenance.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({s:{k:v[k] for k in ['thread_id','word_count','paragraph_count']} for s,v in stages.items()},ensure_ascii=False,indent=2))
