"""Separate first-output prose and bibliography exactly; never revise their wording."""
from pathlib import Path
import hashlib
import json
import re
import sys

record = Path(__file__).resolve().parent
stage = sys.argv[1]
dest = record/stage
text = (dest/'first-output.md').read_text(encoding='utf-8')
sha = lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
headings = list(re.finditer(r'(?m)^(?:#{1,4} [^\n]+|\*\*[^\n]+\*\*)\s*$',text))
chosen = {}
for kind, pattern in [('en',r'English|英文|^(?:#{1,4}\s+|\*\*)(?:\d+[.)]?\s*)?Introduction\b'),
                      ('zh',r'中文|Chinese'),('references',r'References|参考文献')]:
    found = [h for h in headings if re.search(pattern,h.group(),re.I)]
    assert len(found)==1,(kind,[h.group() for h in found])
    h = found[0]
    level = len(re.match(r'#+',h.group()).group()) if h.group().startswith('#') else 1
    later = [x for x in headings if x.start()>h.start() and
             not re.search(r'第[0-9一二三四五六七八九十]+段|Paragraph\s+\d+',x.group(),re.I) and
             (not x.group().startswith('#') or len(re.match(r'#+',x.group()).group())<=level)]
    end = later[0].start() if later else len(text)
    body = text[h.end():end].strip('\r\n')
    assert body and body in text
    chosen[kind] = (body,h.group().strip())
files = {}
for kind,(body,heading) in chosen.items():
    name = 'first-introduction.'+kind+'.txt' if kind in ('en','zh') else 'first-references.md'
    p = dest/name
    assert not p.exists()
    p.write_text(body+'\n',encoding='utf-8')
    files[name] = {'sha256':sha(p),'exact_original_substring':True,'heading':heading}
raw = dest/'raw-introduction-and-references.md'
assert not raw.exists()
raw.write_text(chosen['en'][0]+'\n\n'+chosen['references'][1]+'\n\n'+chosen['references'][0]+'\n',encoding='utf-8')
(dest/'section-retention.json').write_text(json.dumps({'stage':stage,'source_sha256':sha(dest/'first-output.md'),
    'sections':files,'raw_handoff_sha256':sha(raw),'English_or_reference_wording_changed':False,
    'translation_assessment_or_author_notes_sent_to_polishing':False,
    'operation':'Separate exact original prose and bibliography, normalize only outer line breaks and retain bibliography heading'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(stage,'first full English, Chinese and references retained without prose changes')
