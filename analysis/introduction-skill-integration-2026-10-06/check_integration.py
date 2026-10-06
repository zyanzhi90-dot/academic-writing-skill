"""Static candidate/read-path verification only; no Skill/model execution or installation."""
from pathlib import Path
import hashlib
import json
import re
import runpy
import shutil
import subprocess
import tempfile
from urllib.parse import unquote

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
CANDIDATE = ROOT / 'skill-candidate'
BASE = '177d720dcae4131f653c9dee3194e781f824946c'
helpers = runpy.run_path(str(ROOT/'analysis/check_candidate_loading.py'))
sha = lambda b: hashlib.sha256(b).hexdigest()
lf = lambda b: b.replace(b'\r\n', b'\n')
git = lambda *args: subprocess.check_output(['git', '-c', 'core.quotepath=false', *args], cwd=ROOT)
old = lambda p: git('show', BASE+':'+p)
provenance = json.loads((OUT/'audit/learning-resource-provenance.json').read_text(encoding='utf-8'))
manifests = helpers['manifests_at'](CANDIDATE)

accepted = []
for item in provenance['resources']:
    src, dest = ROOT/item['accepted_source'], ROOT/item['runtime_path']
    source, runtime = src.read_text(encoding='utf-8'), dest.read_text(encoding='utf-8')
    assert sha(src.read_bytes()) == item['accepted_source_sha256']
    assert sha(dest.read_bytes()) == item['runtime_sha256']
    assert lf(src.read_bytes()) == lf(old(item['accepted_source']))
    assert re.findall(r'^> (.*)$', source, re.M) == re.findall(r'^> (.*)$', runtime, re.M)
    assert re.findall(r'^\|.*$', source, re.M) == re.findall(r'^\|.*$', runtime, re.M)
    source_labels = re.sub(r'(?:; |；)\[来源审计定位\]\([^)]+\)', '', source)
    source_labels = re.sub(r'\[([^\]]+)\]\(\.\./introduction-section-review-2026-10-06/[^)]+\)', r'\1', source_labels)
    assert re.findall(r'^\*\*.*$', source_labels, re.M) == re.findall(r'^\*\*.*$', runtime, re.M)
    assert 'analysis/' not in runtime and '../introduction-' not in runtime
    for block in re.findall(r'^> (.*)$', runtime, re.M):
        assert ';' not in block and not re.search(r'(^|\. )Here\b', block)
    accepted.append({'level':item['level'], 'english_blocks':item['english_blocks'],
                     'english_analysis_and_source_labels_unchanged':True})
assert sum(x['english_blocks'] for x in accepted) == 65

# Every new runtime link is package-local and its explicit retrieval anchor exists.
links = []
for path in [CANDIDATE/'nature-shared/core/robotics-introduction-examples.md',
             *(ROOT/i['runtime_path'] for i in provenance['resources'])]:
    for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
        assert not target.startswith(('http:', 'https:', '../'))
        relative, _, anchor = target.partition('#')
        dest = (path.parent/unquote(relative)).resolve()
        assert dest.is_relative_to(CANDIDATE.resolve()) and dest.is_file(), target
        if anchor:
            assert f'<a id="{anchor}"></a>' in dest.read_text(encoding='utf-8'), target
        links.append({'from':path.relative_to(CANDIDATE).as_posix(), 'to':target})

index_path = 'skill-candidate/nature-shared/core/robotics-writing-examples.md'
before, after = old(index_path).decode('utf-8'), (ROOT/index_path).read_text(encoding='utf-8')
before_cards, after_cards = helpers['cards'](before), helpers['cards'](after)
assert before_cards.keys() == after_cards.keys()
assert len(after_cards) == 22
assert all(lf(a.encode()) == lf(after_cards[k].encode()) for k,a in before_cards.items())
def between(text, start, end):
    return text[text.index(start):text.index(end,text.index(start))]
assert between(before,'## Abstract reference selection','## Introduction reference selection') == between(after,'## Abstract reference selection','## Introduction reference selection')
assert re.search(r'^\| 摘要 .*$', before, re.M)[0] == re.search(r'^\| 摘要 .*$', after, re.M)[0]

modified = set(git('diff','--name-only',BASE).decode('utf-8').splitlines())
allowed = {
    'skill-candidate/nature-writing/manifest.yaml',
    'skill-candidate/nature-shared/manifest.yaml',
    'skill-candidate/nature-writing/references/introduction.md',
    'skill-candidate/nature-writing/static/fragments/section/intro.md',
    'skill-candidate/nature-polishing/static/fragments/section/intro.md',
    'skill-candidate/nature-shared/core/robotics-writing-examples.md',
    'skill-candidate/nature-shared/core/robotics-main-text.md',
    'skill-candidate/nature-shared/core/robotics-introduction-examples.md',
    *(i['runtime_path'] for i in provenance['resources']),
}
assert all(p in allowed or p.startswith('analysis/introduction-skill-integration-2026-10-06/') for p in modified), modified-allowed
preserved = []
for name in git('ls-tree','-r','--name-only',BASE,'skill-candidate').decode('utf-8').splitlines():
    if name not in allowed:
        assert lf((ROOT/name).read_bytes()) == lf(old(name)), name
        preserved.append(name)
for name in ('nature-writing','nature-polishing'):
    previous = helpers['yaml'].safe_load(old('skill-candidate/'+name+'/manifest.yaml').decode('utf-8'))
    current = manifests[name][0]
    assert current['always_load'] == previous['always_load'] and current['axes'] == previous['axes']
    section = CANDIDATE/name/current['axes']['section']['values']['intro']
    current_text = section.read_text(encoding='utf-8')
    previous_text = old(section.relative_to(ROOT).as_posix()).decode('utf-8')
    assert lf(current_text[current_text.index('## Default funnel') if name=='nature-writing' else current_text.index('The Introduction should:'):].encode()) == lf(previous_text[previous_text.index('## Default funnel') if name=='nature-writing' else previous_text.index('The Introduction should:'):].encode())

# Check source integrity without rewriting or rerunning the historical test.
inputs = {}
source_provenance = json.loads((ROOT/'analysis/introduction-section-review-2026-10-06/source-provenance.json').read_text(encoding='utf-8'))
for name in source_provenance['author_inputs_sha256']:
    path = ROOT/name
    assert lf(path.read_bytes()) == lf(old(name))
    inputs[name] = sha(path.read_bytes())
for paper, details in source_provenance['papers'].items():
    assert sha((ROOT/details['pdf']).read_bytes()) == details['pdf_sha256']
    inputs[details['pdf']] = details['pdf_sha256']
for name in git('ls-tree','-r','--name-only',BASE,'effect-test/E04-introduction-delivery-253dae3-2026-10-05').decode('utf-8').splitlines():
    data = (ROOT/name).read_bytes()
    assert lf(data) == lf(old(name)), name
    inputs[name] = sha(data)
assert (OUT/'audit/previous-robotics-introduction-examples.md').read_bytes() == old('skill-candidate/nature-shared/core/robotics-introduction-examples.md')

def selected_unit(path, anchor):
    text = path.read_text(encoding='utf-8')
    start = text.index(f'<a id="{anchor}"></a>')
    following = text.find('<a id="',start+len('<a id="'))
    unit = text[start:following if following>=0 else len(text)]
    assert '> ' in unit and ('|' in unit or path.name.endswith('section.md'))
    return {'anchor':anchor, 'sha256':sha(unit.encode()),'lines':len(unit.splitlines()),
            'complete_english_blocks':len(re.findall(r'^> ',unit,re.M))}

def read_cases(base):
    loaded = helpers['manifests_at'](base)
    records = []
    selection = {'section':['field-value','prior-capability','design-role','design-connection','contributions'],
                 'paragraphs':['p17-i01','p17-i04','p17-i05','p17-i07','p17-i08','p05-i02','fuzzy-i02','fuzzy-i03','eso-i01'],
                 'expression':['e01','e02','e03','e05','e06','e09','e13','e14','e17','e18','e19','e21','e22','e23','e24','e25','e26']}
    for name in ('nature-writing','nature-polishing'):
        manifest = loaded[name][0]
        for language in ('en','zh-to-en'):
            package = base/name
            paths = ['SKILL.md','manifest.yaml',*manifest['always_load']]
            axes = {'paper_type':'algorithmic','section':'intro','language':language,'journal':'generic'}
            if name=='nature-writing': axes['task']='manuscript'
            paths.extend(manifest['axes'][axis]['values'][value] for axis,value in axes.items())
            if language=='zh-to-en': paths.append('static/fragments/language/en.md')
            refs = {x['path'] for x in manifest['references']['on_demand']}
            for relative in ('../nature-shared/core/robotics-writing-examples.md','../nature-shared/core/robotics-main-text.md'):
                assert relative in refs
                paths.append(relative)
            fragment = package/manifest['axes']['section']['values']['intro']
            hub_relative = '../nature-shared/core/robotics-introduction-examples.md'
            assert hub_relative in fragment.read_text(encoding='utf-8')
            paths.append(hub_relative)
            reads = []
            for relative in dict.fromkeys(paths):
                path = (package/relative).resolve()
                data = path.read_bytes()
                data.decode('utf-8')
                reads.append({'path':path.relative_to(base.resolve()).as_posix(),'sha256':sha(data)})
            for level, anchors in selection.items():
                path = base/'nature-shared/core'/f'robotics-introduction-{level}.md'
                assert 'core/'+path.name in loaded['nature-shared'][1]
                reads.append({'path':path.relative_to(base.resolve()).as_posix(), 'sha256':sha(path.read_bytes()),
                              'selected_complete_units':[selected_unit(path,a) for a in anchors]})
            records.append({'skill':name,'language':language,'axes':axes,'files_actually_read':reads})
    return records

local_reads = read_cases(CANDIDATE)
with tempfile.TemporaryDirectory(prefix='intro-candidate-read-') as tmp:
    relocated = Path(tmp)/'candidate'
    shutil.copytree(CANDIDATE,relocated)
    relocated_reads = read_cases(relocated)
assert local_reads == relocated_reads
result = {'baseline':BASE,'verification_kind':'Static manifest, package integrity and actual file/complete-unit reads; no model or effect test.',
          'accepted_learning':accepted, 'resolved_runtime_links':links,
          'manifest_declared_paths_resolved':{n:len(v[1]) for n,v in manifests.items()},
          'unchanged_example_cards':len(after_cards), 'unchanged_other_candidate_files':len(preserved),
          'unchanged_files':preserved, 'author_pdf_and_E04_sha256':inputs,
          'local_and_relocated_reads_identical':True,'read_cases':local_reads,
          'scope':'Manually resolved robotics Intro axes; non-Intro fragments, routing axes, core workflows, scripts and Abstract material remain unchanged. This does not establish autonomous routing, model attention or writing effect.'}
(OUT/'audit/verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'cards_unchanged':len(after_cards),'english_blocks':65,'read_cases':len(local_reads),'relocation_identical':True}))
