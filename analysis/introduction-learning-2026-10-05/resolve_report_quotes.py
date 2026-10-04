"""Insert source-identical quotations into the evidence analysis, without models."""
from pathlib import Path
import json
import re

OUT = Path(__file__).resolve().parent
DATA=json.loads((OUT/'curated-introductions.json').read_text(encoding='utf-8'))
REPORT=OUT/'report.md'
SOURCE={f'{k}:{u["id"]}':u['text'] for k,units in DATA.items() for u in units}

def resolve(match):
    kind,key,unit,extra=match.groups()
    text=SOURCE[f'{key}:{unit}']
    if kind=='excerpt':
        text=text[text.index(extra):]
    elif kind=='first':
        # Selected source sentences contain no internal decimal/abbreviation period.
        sentences=re.split(r'(?<=[.!?])\s+',text)
        text=' '.join(sentences[:int(extra)])
    return '> '+text

report=REPORT.read_text(encoding='utf-8')
report=re.sub(r'\{\{(quote|excerpt|first):([^:}]+):([^:}]+)(?::([^}]+))?\}\}',resolve,report)
assert '{{' not in report
REPORT.write_text(report,encoding='utf-8')
print('Inserted complete paragraphs and contiguous sentence excerpts from curated sources.')
