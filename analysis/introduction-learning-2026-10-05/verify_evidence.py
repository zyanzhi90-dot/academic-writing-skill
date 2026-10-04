"""Read-only integrity checks for analysis artifacts; not a writing-effect test."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
sources=json.loads((OUT/'source-provenance.json').read_text(encoding='utf-8'))
curated=json.loads((OUT/'curated-introductions.json').read_text(encoding='utf-8'))
records=[]

def check(name, condition, detail):
    if not condition:
        raise AssertionError(f'{name}: {detail}')
    records.append({'check':name,'result':'verified','detail':detail})

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

for key,units in curated.items():
    src=sources[key]
    check(f'{key} PDF unchanged',sha(ROOT/src['pdf'])==src['pdf_sha256'],src['pdf'])
    if 'reused_extraction' in src:
        check(f'{key} old extraction unchanged',sha(ROOT/src['reused_extraction'])==src['reused_sha256'],src['reused_extraction'])
    else:
        check(f'{key} extraction identity',sha(ROOT/src['new_raw_extraction'])==src['raw_sha256'],src['new_raw_extraction'])
    quotes=re.findall(r'^> (.+)$',(OUT/f'{key}-introduction.md').read_text(encoding='utf-8'),re.M)
    check(f'{key} full-source quotation identity',quotes==[u['text'] for u in units],f'{len(units)} units, all paragraphs/contribution items')

report=(OUT/'report.md').read_text(encoding='utf-8')
quotes=re.findall(r'^> (.+)$',report,re.M)
for i,quote in enumerate(quotes,1):
    matches=[f'{k}:{u["id"]}' for k,units in curated.items() for u in units if quote in u['text']]
    check(f'report quotation {i}',len(matches)==1,matches)
check('report English excerpts',len(quotes)==14,f'{len(quotes)} source-identical full paragraphs or contiguous sentence excerpts')
links=re.findall(r'\]\(<?([^)>]+)>?\)',report)
for target in links:
    check('report relative link exists',(OUT/target).resolve().is_file(),target)
check('author core requirements unchanged this turn',sha(ROOT/'核心要求.txt')==sources['session']['core_requirements_sha256'],'Author working-tree edit preserved verbatim; not introduced by this analysis')
check('author experience unchanged',sha(ROOT/'我自己的经验和做法.txt')==sources['session']['author_experience_sha256'],'Author scientific meaning and expression preferences')
skill_diff=subprocess.check_output(['git','diff',sources['session']['base_commit'],'--','skill-candidate'],cwd=ROOT)
check('candidate Skills unchanged',not skill_diff,'Compared with evidence-reading base commit; no Skill edit')
pngs=list((OUT/'page-previews').glob('*.png'))
check('Introduction visual evidence complete',len(pngs)==9,'Four first/second-page pairs plus ESO third-page continuation, all inspected')
payload={'scope':'Analysis source, quotation, link, input and diff integrity only; no model/test execution or effect acceptance',
         'writing_tests':{'Drafting':'not run / not evaluated','Polishing':'not run / not evaluated',
                          'combined':'not run / not evaluated','transfer':'not run / not evaluated'},
         'root1_pdf':'Not found in repository, D:/桌面, user Downloads, Desktop or Documents; final rg search included hidden files and case-insensitive filename glob; no substitute used',
         'records':records}
(OUT/'evidence-checks.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'{len(records)} evidence-integrity checks verified; no writing tests or Skill changes.')
