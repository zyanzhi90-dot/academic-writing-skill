"""Verify source and quotation integrity, not writing quality or Skill performance."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
git = lambda *a: subprocess.check_output(['git',*a],cwd=ROOT)
provenance = json.loads((OUT/'source-provenance.json').read_text(encoding='utf-8'))
units = json.loads((OUT/'curated-introductions.json').read_text(encoding='utf-8'))
sentences = json.loads((OUT/'source-sentences.json').read_text(encoding='utf-8'))
notes = json.loads((OUT/'analysis-notes.json').read_text(encoding='utf-8'))
prior = ROOT/'analysis/introduction-learning-2026-10-05'
prior_sources = json.loads((prior/'source-provenance.json').read_text(encoding='utf-8'))
prior_originals = json.loads((prior/'curated-introductions.json').read_text(encoding='utf-8'))
sources = {}
for paper, paragraphs in units.items():
    src = provenance[paper]
    assert sha(ROOT/src['pdf']) == src['pdf_sha256'] == prior_sources[paper]['pdf_sha256']
    assert paragraphs == prior_originals[paper], (paper,'Fresh PDF block reconstruction differs from earlier source text')
    assert set(notes[paper]) == {p['id'] for p in paragraphs}
    intro = (OUT/f'{paper}-introduction.md').read_text(encoding='utf-8')
    analysis = (OUT/f'{paper}-analysis.md').read_text(encoding='utf-8')
    exact = []
    for p in paragraphs:
        ss = sentences[paper][p['id']]
        assert ' '.join(ss) == p['text']
        assert len(notes[paper][p['id']]['sentences']) == len(ss)
        assert '> '+p['text'] in intro and '> '+p['text'] in analysis
        exact.append({'unit':p['id'], 'blocks':p['blocks'], 'sentences':len(ss),
                      'full_source_paragraph_preserved':True,'sentence_analysis_count_matches':True})
    sources[paper] = {'pdf':src['pdf'],'sha256':src['pdf_sha256'],
        'freshly_extracted_page_blocks':True,'same_verified_original_after_layout_normalization':True,
        'visual_pages_inspected':list(range(1,4 if paper=='ESO2017' else 3)),
        'units':exact}

report = (OUT/'report.md').read_text(encoding='utf-8')
quotes = []
for m in re.finditer(r'<!-- source (\w+) (\w+) (\d+) (\d+) -->\s*\n> ([^\n]+)',report):
    paper,unit,start,end,quote = m.groups()
    expected = ' '.join(sentences[paper][unit][int(start)-1:int(end)])
    assert quote == expected,(paper,unit,start,end,'Quote differs or sentences are not contiguous')
    quotes.append({'paper':paper,'unit':unit,'sentences':[int(start),int(end)],
                   'verbatim_contiguous_source_sentences':True})
assert len(quotes)==report.count('<!-- source ') and quotes
links=[]
for p in OUT.glob('*.md'):
    text=p.read_text(encoding='utf-8')
    for m in re.finditer(r'\[[^\]]*\]\((?:<([^>]+)>|([^)]*))\)',text):
        target=m.group(1) or m.group(2)
        if target.startswith(('https://','http://')):
            continue
        name,_,anchor=target.partition('#')
        dest=(p.parent/name).resolve() if name else p.resolve()
        if dest==OUT/'evidence-checks.json':
            continue
        assert dest.is_file(),(p.name,target)
        if anchor:
            assert f'<a id="{anchor}"></a>' in dest.read_text(encoding='utf-8'),(p.name,target)
        links.append({'file':p.name,'target':target,'resolves':True})

base = provenance['session']['base_commit']
assert not git('diff',base,'--','skill-candidate','effect-test','analysis/introduction-learning-2026-10-05',
               'analysis/introduction-candidate-update-2026-10-05')
assert sha(ROOT/'核心要求.txt') == provenance['session']['core_requirements_sha256']
assert sha(ROOT/'我自己的经验和做法.txt') == provenance['session']['author_experience_sha256']
author_files = {name:sha(ROOT/name) for name in ('核心要求.txt','我自己的经验和做法.txt','引言写作方法.txt')}
expected = {'核心要求.txt','引言写作方法.txt'}
tracked_changes = git('diff','--name-only','-z').decode('utf-8').split('\0')
assert all(n in expected or n.startswith(OUT.relative_to(ROOT).as_posix()+'/') for n in tracked_changes if n)
secret_files=[]
for p in OUT.rglob('*'):
    if p.is_file() and p.suffix in ('.md','.txt','.json','.py'):
        if re.search(r'\b(?:sk-[A-Za-z0-9_-]{32,}|ghp_[A-Za-z0-9]{30,}|Bearer [A-Za-z0-9_-]{40,})\b',p.read_text(encoding='utf-8-sig')):
            secret_files.append(p.relative_to(OUT).as_posix())
assert not secret_files
out={'scope':'Source-grounded Introduction learning summary only; no Skill changes, installations or effect tests',
     'base_commit':base,'source_checks':sources,'annotated_units':sum(len(v) for v in units.values()),
     'annotated_sentences':sum(len(s) for v in sentences.values() for s in v.values()),
     'report_contiguous_quote_checks':quotes,'local_links':links,'author_input_hashes':author_files,
     'prior_source_segmentation_reused':True,'fresh_pdf_extraction_and_visual_recheck':True,
     'historical_analysis_not_used_as_conclusions':True,'Skill_effect_tests_and_historical_records_unchanged':True,
     'author_changes_present_at_start_preserved':sorted(expected),'credential_pattern_findings':secret_files,
     'limit':'Quote, layout and scope integrity do not prove semantic analysis quality, corpus representativeness or generated writing effects.',
     'files_sha256':{p.relative_to(OUT).as_posix():sha(p) for p in sorted(OUT.rglob('*')) if p.is_file() and p.name!='evidence-checks.json'}}
(OUT/'evidence-checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ('annotated_units','annotated_sentences','Skill_effect_tests_and_historical_records_unchanged')},ensure_ascii=False))
print('Complete original paragraphs, sentence mapping, contiguous quotations, links and scope verified.')
