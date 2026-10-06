"""Check the narrow implementation scope; this is not an effect test."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import yaml

ROOT = Path(__file__).resolve().parents[2]
DEST = Path(__file__).resolve().parent
BASE = '50d77287873375de04c851a6840f3fb06588ef84'
git = lambda *a: subprocess.check_output(['git', *a], cwd=ROOT)
sha = lambda b: hashlib.sha256(b).hexdigest()
allowed = {
    'skill-candidate/nature-shared/core/robotics-introduction-examples.md',
    *('skill-candidate/'+r+'/'+p for r in ('nature-writing','nature-polishing')
      for p in ('SKILL.md','manifest.yaml','static/fragments/section/intro.md')),
}
unchanged = []
for name in filter(None, git('ls-tree','-r','--name-only','-z',BASE,'skill-candidate').decode().split('\0')):
    prior = git('show', BASE+':'+name).decode('utf-8').replace('\r\n','\n')
    current = (ROOT/name).read_text(encoding='utf-8')
    if prior != current:
        assert name in allowed, name
    else:
        unchanged.append(name)
for role, start in [('nature-writing','## Default funnel'),('nature-polishing','The Introduction should:')]:
    directory=ROOT/'skill-candidate'/role
    old=git('show',BASE+':skill-candidate/'+role+'/static/fragments/section/intro.md').decode()
    general=(directory/'static/fragments/section/intro-general.md').read_text(encoding='utf-8')
    assert general.split('\n\n',1)[1]==old[old.index(start):]
    default=(directory/'static/fragments/section/intro.md').read_text(encoding='utf-8')
    for conflict in ('task-then-application','here we show','Draft backward','question or hypothesis','Do not summarize','not the numbers'):
        assert conflict not in default
    cfg=yaml.safe_load((directory/'manifest.yaml').read_text(encoding='utf-8'))
    for p in cfg['always_load']:
        assert (directory/p).is_file()
    for axis in cfg['axes'].values():
        for p in axis['values'].values():
            assert (directory/p).is_file()
    for entry in cfg['references']['on_demand']:
        assert (directory/entry['path']).is_file(),entry['path']
    for entry in cfg['references']['on_demand']:
        if entry['path'].endswith('nature-introduction.md'):
            assert 'outside the robotics-centred Introduction scope' in entry['condition']
prior=ROOT/'effect-test/E04-introduction-delivery-ee74b27-2026-10-06'
evidence={'baseline':BASE,'actual_events':{},'source_documents':{}}
for stage in ('drafting','polishing'):
    path=prior/stage/'events.jsonl'
    events=[json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()]
    selected=[]
    for event in events:
        item=event.get('item',{})
        if event.get('type')=='item.completed' and (item.get('type')=='agent_message' or
           any(term in item.get('command','').replace('\\','/') for term in
               ('intro.md','scientific-expression.md','robotics-introduction'))):
            selected.append(event)
    evidence['actual_events'][stage]={'source':path.relative_to(ROOT).as_posix(),
                                    'sha256':sha(path.read_bytes()),'events':selected}
for pattern in ('analysis/introduction-section-review-2026-10-06/*introduction.md',
                'analysis/introduction-*-learning*/learning-draft.md'):
    for path in ROOT.glob(pattern):
        evidence['source_documents'][path.relative_to(ROOT).as_posix()]=sha(path.read_bytes())
for path in ROOT.glob('*.txt'):
    evidence['source_documents'][path.name]=sha(path.read_bytes())
(DEST/'evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(DEST/'implementation-check.json').write_text(json.dumps({
    'baseline':BASE,'allowed_existing_candidate_files':sorted(allowed),
    'unchanged_candidate_files':unchanged,'generic_content_preserved_in_separate_files':True,
    'accepted_three_learning_resources_unchanged':True,'manifest_targets_exist':True,
    'executor_and_historical_outputs_unchanged':not git('diff',BASE,'--','effect-test'),
    'effect_verdict':'Not established by static checks'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Narrow candidate scope, unchanged accepted resources, generic preservation and both entry paths verified.')
