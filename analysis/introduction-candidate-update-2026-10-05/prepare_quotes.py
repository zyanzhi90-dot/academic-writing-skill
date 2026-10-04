"""Populate only the new candidate reference from frozen, inspected source units.

No model calls or historical-file edits. This is an implementation helper,
not a candidate workflow or a writing-effect test.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[1]
SOURCE_PATH='analysis/introduction-learning-2026-10-05/curated-introductions.json'
data=subprocess.check_output(['git','show',f'54f9e39:{SOURCE_PATH}'],cwd=ROOT)
assert (ROOT/SOURCE_PATH).read_text(encoding='utf-8').splitlines()==data.decode('utf-8').splitlines()
source=json.loads(data.decode('utf-8'))
units={f'{key}:{unit["id"]}':unit['text'] for key,items in source.items() for unit in items}
reference=ROOT/'skill-candidate/nature-shared/core/robotics-introduction-examples.md'
records=[]

def insert(match):
    kind,key,unit,extra=match.groups()
    text=units[f'{key}:{unit}']
    if kind=='excerpt':
        text=text[text.index(extra):]
    elif kind=='first':
        text=' '.join(re.split(r'(?<=[.!?])\s+',text)[:int(extra)])
    elif kind=='sentence':
        start=text.index(extra)
        text=re.split(r'(?<=[.!?])\s+',text[start:])[0]
    assert text in units[f'{key}:{unit}']
    records.append({'paper':key,'unit':unit,'selection':kind,
                    'selection_argument':extra,'source_block':next(u['blocks'] for u in source[key] if u['id']==unit),
                    'sha256':hashlib.sha256(text.encode('utf-8')).hexdigest(),
                    'text':text})
    return '> '+text

text=reference.read_text(encoding='utf-8')
text=re.sub(r'\{\{(quote|excerpt|first|sentence):([^:}]+):([^:}]+)(?::([^}]+))?\}\}',insert,text)
assert '{{' not in text
assert len(records)==25, len(records)
reference.write_text(text,encoding='utf-8')
payload={'source_commit':'54f9e39773e92c8ced719d4bcd4d01db6195980b',
         'source_path':SOURCE_PATH,'git_source_sha256':hashlib.sha256(data).hexdigest(),
         'working_source_sha256':hashlib.sha256((ROOT/SOURCE_PATH).read_bytes()).hexdigest(),
         'working_source_matches_frozen_after_EOL_normalization':True,
         'candidate_reference':reference.relative_to(ROOT).as_posix(),
         'scope':'Source-identical Introduction quotes. No writing/test generation.',
         'quotes':records}
(OUT/'quote-provenance.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'{len(records)} source-identical quotations inserted into new candidate reference.')
