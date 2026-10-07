"""Narrow scope and raw source evidence; no writing-effect verdict."""
from pathlib import Path
import hashlib
import json
import subprocess
import yaml

ROOT=Path(__file__).resolve().parents[2]
DEST=Path(__file__).resolve().parent
BASE='836b01aa7c45b14133452ebdf21cf3660b20a741'
git=lambda *a:subprocess.check_output(['git',*a],cwd=ROOT)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
allowed={
 'skill-candidate/nature-shared/core/robotics-introduction-examples.md',
 'skill-candidate/nature-shared/core/robotics-main-text.md',
 'skill-candidate/nature-shared/manifest.yaml',
 *('skill-candidate/'+r+'/'+p for r in ('nature-writing','nature-polishing')
   for p in ('SKILL.md','manifest.yaml','static/fragments/section/intro.md','static/fragments/language/en.md')),
 'skill-candidate/nature-writing/static/core/workflow.md',
 'skill-candidate/nature-polishing/static/core/failure-modes.md',
}
changed=[]
unchanged=[]
for name in filter(None,git('ls-tree','-r','--name-only','-z',BASE,'skill-candidate').decode().split('\0')):
 old=git('show',BASE+':'+name).decode('utf-8').replace('\r\n','\n')
 new=(ROOT/name).read_text(encoding='utf-8')
 if old!=new:
  assert name in allowed,name
  changed.append(name)
 else:unchanged.append(name)
assert set(changed)==allowed
assert not git('diff',BASE,'--','effect-test')
for role in ('nature-writing','nature-polishing','nature-shared'):
 directory=ROOT/'skill-candidate'/role
 cfg=yaml.safe_load((directory/'manifest.yaml').read_text(encoding='utf-8'))
 for p in cfg['always_load']:assert (directory/p).is_file()
 for axis in cfg.get('axes',{}).values():
  for p in axis['values'].values():assert (directory/p).is_file()
 entries=cfg.get('references',cfg.get('core',{})).get('on_demand',[])
 for entry in entries:
  assert (directory/entry['path']).is_file(),entry['path']
  if entry['path'].endswith('robotics-writing-examples.md'):
   assert 'Introduction-only' in entry['condition']
  if role!='nature-shared' and entry['path'].endswith('nature-introduction.md'):
   assert 'outside the robotics-centred Introduction scope' in entry['condition']
prior=ROOT/'effect-test/E04-introduction-delivery-a29f1e1-2026-10-06'
evidence={'baseline':BASE,'actual_events':{},'source_hashes':{}}
for stage in ('drafting','polishing'):
 path=prior/stage/'events.jsonl'
 events=[json.loads(s) for s in path.read_text(encoding='utf-8').splitlines()]
 selected=[]
 for event in events:
  item=event.get('item',{})
  if event.get('type')=='item.completed' and (item.get('type')=='agent_message' or
    any(t in item.get('command','') for t in ('robotics-writing-examples.md','scientific-expression.md','robotics-introduction-expression.md'))):
   selected.append(event)
 evidence['actual_events'][stage]={'source':path.relative_to(ROOT).as_posix(),'sha256':sha(path),'events':selected}
for pattern in ('analysis/introduction-section-review-2026-10-06/*introduction.md',
                'skill-candidate/nature-shared/core/robotics-introduction-*.md'):
 for path in ROOT.glob(pattern):evidence['source_hashes'][path.relative_to(ROOT).as_posix()]=sha(path)
for path in ROOT.glob('*.txt'):evidence['source_hashes'][path.name]=sha(path)
(DEST/'evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(DEST/'implementation-check.json').write_text(json.dumps({
 'baseline':BASE,'changed_files':changed,'unchanged_candidate_files':unchanged,
 'accepted_three_learning_resources_unchanged':True,'scientific_expression_core_unchanged':True,
 'other_section_cards_and_generic_isolation_unchanged':True,
 'declared_paths_exist':True,'historical_records_and_executor_unchanged':True,
 'static_validation_only':True,'effect_verdict':'Not inferred'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Checked',len(changed),'necessary Introduction routing/adaptation contacts;',len(unchanged),'candidate files unchanged.')
