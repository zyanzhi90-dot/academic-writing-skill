"""Implementation/source/read-path checks only; no model or effect-test runner.

Reuse the established manifest checker as functions, never its main entrypoint
or historical output path. Cases resolve scope explicitly; file reads cannot
prove natural-language routing, example adoption, prose quality or stability.
"""
from pathlib import Path
import hashlib
import json
import re
import runpy
import shutil
import subprocess
import sys
import tempfile

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[1]
CANDIDATE=ROOT/'skill-candidate'
BASE='54f9e39773e92c8ced719d4bcd4d01db6195980b'
INDEX='nature-shared/core/robotics-writing-examples.md'
NEW='nature-shared/core/robotics-introduction-examples.md'
EXPECTED={NEW,INDEX,'nature-shared/SKILL.md','nature-shared/manifest.yaml',
          'nature-writing/references/introduction.md'}
CHECKER=runpy.run_path(str(ROOT/'analysis/check_candidate_loading.py'))
manifest_check=CHECKER['manifests_at']
old_cards=CHECKER['cards']

def sha(value):
    return hashlib.sha256(value).hexdigest()

def frozen(path):
    return subprocess.check_output(['git','show',BASE+':'+path],cwd=ROOT)

def card_units(text):
    return {m[1]:m[0] for m in re.finditer(r'^## (B\d{2})\n.*?(?=^## |\Z)',text,re.M|re.S)}

new_text=(CANDIDATE/NEW).read_text(encoding='utf-8')
units=card_units(new_text)
assert set(units)=={'B15','B16','B17','B18'}
assert '{{' not in new_text
prior_index=frozen('skill-candidate/'+INDEX).decode('utf-8')
current_index=(CANDIDATE/INDEX).read_text(encoding='utf-8')
previous,current=old_cards(prior_index),old_cards(current_index)
assert len(previous)==22 and previous==current
assert '(robotics-introduction-examples.md#selection)' in current_index
assert '## Selection' in new_text
source_records=json.loads((OUT/'quote-provenance.json').read_text(encoding='utf-8'))
source=json.loads(frozen(source_records['source_path']))
quotes=re.findall(r'^> (.+)$',new_text,re.M)
assert quotes==[q['text'] for q in source_records['quotes']]
for record in source_records['quotes']:
    original=next(u['text'] for u in source[record['paper']] if u['id']==record['unit'])
    assert record['text'] in original
    assert sha(record['text'].encode('utf-8'))==record['sha256']
provenance=json.loads(frozen('analysis/introduction-learning-2026-10-05/source-provenance.json'))
pdfs={key:{'path':provenance[key]['pdf'],'sha256':sha((ROOT/provenance[key]['pdf']).read_bytes())}
      for key in source}
for key,value in pdfs.items():
    assert value['sha256']==provenance[key]['pdf_sha256']
links=dict(re.findall(r'^\[([^\]]+)\]: <(.*?)>$',new_text,re.M))
assert set(links)==set(source)
for target in links.values():
    assert ((CANDIDATE/NEW).parent/target).resolve().is_file()

CASES=[
    {'id':'robotics-intro-default','section':'intro','language':'en','robotics':True,'cards':['B15']},
    {'id':'robotics-intro-task-learning-zh','section':'intro','language':'zh-to-en','robotics':True,'cards':['B15','B16']},
    {'id':'robotics-intro-joint-performance','section':'intro','language':'en','robotics':True,'cards':['B15','B17']},
    {'id':'robotics-intro-sensor-compensation','section':'intro','language':'en','robotics':True,'cards':['B15','B18']},
    {'id':'robotics-abstract-exclusion','section':'abstract','language':'en','robotics':True,'cards':['A06']},
    {'id':'nonrobotics-intro-exclusion','section':'intro','language':'en','robotics':False,'cards':[]},
]

def read_route(base,name,case,manifest,environment):
    package=base/name
    relative=['SKILL.md','manifest.yaml',*manifest['always_load']]
    axes={'paper_type':'research','section':case['section'],'language':case['language'],'journal':'generic'}
    if name=='nature-writing':
        axes['task']='manuscript'
    for axis,value in axes.items():
        relative.append(manifest['axes'][axis]['values'][value])
    if case['language']=='zh-to-en':
        relative.append('static/fragments/language/en.md')
    refs={entry['path'] for entry in manifest['references']['on_demand']}
    if name=='nature-writing' and case['section']=='intro':
        assert 'references/introduction.md' in refs
        relative.append('references/introduction.md')
    if case['robotics']:
        index='../'+INDEX
        assert index in refs and index in (package/'SKILL.md').read_text(encoding='utf-8')
        relative.append(index)
        if case['section']=='intro':
            body='../nature-shared/core/robotics-main-text.md'
            assert body in refs
            relative.extend([body,'../'+NEW])
    assert '../nature-shared/core/scientific-expression.md' in relative
    reads=[]
    for path in dict.fromkeys(relative):
        actual=(package/path).resolve()
        assert actual.is_relative_to(base.resolve())
        data=actual.read_bytes()
        content=data.decode('utf-8').replace('\r\n','\n')
        record={'path':actual.relative_to(base.resolve()).as_posix(),'sha256':sha(data)}
        if path=='../'+INDEX:
            common=content[:content.index('## 摘要\n')]
            record['selected_text']={'common_and_task_index':{'characters':len(common),'sha256':sha(common.encode('utf-8'))}}
            if case['section']=='abstract':
                text=old_cards(content)['A06']
                record['selected_text']['A06']={'characters':len(text),'sha256':sha(text.encode('utf-8'))}
            else:
                assert '(robotics-introduction-examples.md#selection)' in common
                record['follows_index_link']='robotics-introduction-examples.md#selection'
        elif path=='../'+NEW:
            extracted=card_units(content)
            assert extracted==units
            selection=content[:content.index('## B15\n')]
            chosen={key:extracted[key] for key in case['cards']}
            record['selected_text']={'selection_and_source_notes':{'characters':len(selection),'sha256':sha(selection.encode('utf-8'))},
                                     **{key:{'characters':len(text),'sha256':sha(text.encode('utf-8'))} for key,text in chosen.items()}}
            record['unselected_cards_not_in_selected_text']=sorted(set(extracted)-set(chosen))
            assert all(re.findall(r'^> (.+)$',text,re.M) for text in chosen.values())
        reads.append(record)
    has_new=any(record['path']==NEW for record in reads)
    assert has_new==(case['robotics'] and case['section']=='intro')
    return {'environment':environment,'skill':name,'case':case,'resolved_axes':axes,
            'mode':'explicitly resolved file-read audit, no model invocation',
            'files_read':reads}

results=[]
powershell_reads=[CHECKER['check_powershell_utf8'](CANDIDATE/NEW),
                  CHECKER['check_powershell_utf8'](CANDIDATE/INDEX)]
with tempfile.TemporaryDirectory(prefix='intro-candidate-read-') as temporary:
    moved=Path(temporary)/'candidate-only'
    shutil.copytree(CANDIDATE,moved)
    for base,environment in [(CANDIDATE,'project'),(moved,'relocated-candidate-only')]:
        manifests=manifest_check(base)
        for name in ('nature-writing','nature-polishing'):
            for case in CASES:
                results.append(read_route(base,name,case,manifests[name][0],environment))
        for name in ('nature-writing','nature-polishing','nature-shared'):
            for path in (base/name).rglob('*'):
                if path.is_file():
                    path.read_bytes().decode('utf-8')
    assert not (moved/'analysis').exists() and not (moved/'文献资料').exists()
    relocated_source_links=[{'paper':key,'exists_in_relocated_candidate':((moved/NEW).parent/target).resolve().exists(),
                             'role':'optional lookup, excluded from execution dependencies'} for key,target in links.items()]
    assert all(not item['exists_in_relocated_candidate'] for item in relocated_source_links)
    validation=[]
    validator=Path('C:/Users/user/.codex/skills/.system/skill-creator/scripts/quick_validate.py')
    for name in ('nature-writing','nature-polishing','nature-shared'):
        process=subprocess.run([sys.executable,'-X','utf8',str(validator),str(moved/name)],capture_output=True,text=True,encoding='utf-8')
        assert process.returncode==0,(name,process.stdout,process.stderr)
        validation.append({'package':name,'tool':'skill-creator/scripts/quick_validate.py',
                           'arguments':['-X','utf8','<relocated-candidate-only>/'+name],
                           'exit_code':process.returncode,'stdout':process.stdout,'stderr':process.stderr,
                           'scope':'frontmatter and naming only, no writing-effect claim'})

# Preserve pre-existing candidate files except the justified set.
tree=subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'skill-candidate'],cwd=ROOT).decode('utf-8').splitlines()
modified=[]
preserved=0
for path in tree:
    old=frozen(path).decode('utf-8').splitlines()
    actual=(ROOT/path).read_text(encoding='utf-8').splitlines()
    if actual!=old:
        relative=path.removeprefix('skill-candidate/')
        assert relative in EXPECTED,relative
        modified.append(relative)
    else:
        preserved+=1
all_current={p.relative_to(CANDIDATE).as_posix() for p in CANDIDATE.rglob('*') if p.is_file()}
all_previous={p.removeprefix('skill-candidate/') for p in tree}
assert all_previous<=all_current
assert all_current-all_previous=={NEW}
assert set(modified)|{NEW}==EXPECTED
state=[{'path':path,'sha256':sha((CANDIDATE/path).read_bytes()),
        'text_LF_sha256':sha((CANDIDATE/path).read_text(encoding='utf-8').encode('utf-8'))} for path in sorted(all_current)]
inputs=[{'path':name,'working_sha256':sha((ROOT/name).read_bytes()),
         'equals_54f9e39_after_EOL_normalization':(ROOT/name).read_text(encoding='utf-8').splitlines()==frozen(name).decode('utf-8').splitlines()}
        for name in ['核心要求.txt','我自己的经验和做法.txt','analysis/introduction-learning-2026-10-05/report.md']]
assert all(item['equals_54f9e39_after_EOL_normalization'] for item in inputs)
assert not subprocess.check_output(['git','diff',BASE,'--','effect-test','skill-baseline','analysis/introduction-learning-2026-10-05'],cwd=ROOT)
payload={'base_commit':BASE,'scope':'source, package integrity and real file-read paths only',
         'new_card_ids':list(units),'quotes_verified':len(quotes),'pdf_sources':pdfs,
         'existing_22_cards_preserved_verbatim':True,'unchanged_existing_candidate_files':preserved,
         'candidate_changes':sorted(EXPECTED),'author_and_analysis_inputs':inputs,
         'manifest_declared_paths':{name:len(item[1]) for name,item in manifest_check(CANDIDATE).items()},
         'package_validator':validation,'route_file_reads':results,
         'actual_powershell_utf8_reads':powershell_reads,
         'relocated_optional_pdf_links':relocated_source_links,
         'limitation':'Axes and cards resolved explicitly. Actual file reads do not establish autonomous router/example use or writing quality.',
         'historical_outputs_and_baseline_unchanged':True,
         'effect_evaluation':{'Drafting':'not run / not evaluated','Polishing':'not run / not evaluated',
                              'combined':'not run / not evaluated','transfer':'not run / not evaluated','stability':'not evaluated'},
         'installation_performed':False}
(OUT/'implementation-check.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(OUT/'candidate-files.json').write_text(json.dumps({'scope':'frozen implementation content hashes; no effect acceptance',
                                                 'files':state},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'new_cards':list(units),'source_identical_quotes':len(quotes),'read_paths':len(results),
                  'declared_paths':payload['manifest_declared_paths'],'existing_cards_preserved':22,
                  'modified_candidate_files':len(EXPECTED),'effect_evaluation':'not run'},ensure_ascii=False))
