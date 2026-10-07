"""Read-only sentence locators and surface observations; not an effect test."""
from pathlib import Path
import hashlib
import json
import re

record=Path(__file__).resolve().parent
out={}
for stage in ('drafting','polishing'):
    p=record/stage/'first-introduction.en.txt'
    text=p.read_text(encoding='utf-8')
    paragraphs=[s.strip() for s in text.strip().split('\n\n') if s.strip()]
    out[stage]={'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
        'paragraphs':[{'id':f'P{i:02d}','text':paragraph,
                       'sentences':[{'id':f'P{i:02d}-S{j:02d}','text':sentence}
                                    for j,sentence in enumerate(re.split(r'(?<=[.!?])\s+(?=[A-Z])',paragraph),1)]}
                      for i,paragraph in enumerate(paragraphs,1)],
        'surface_observations':{'In_numbered_reference_count':len(re.findall(r'\bIn \[\d+\]',text)),
                                'prose_semicolons':text.count(';'),'prose_colons':text.count(':'),
                                'Here_openings':len(re.findall(r'(?:^|[.!?]\s+)Here\b',text)),
                                'Learning_openings':re.findall(r'(?:^|[.!?]\s+)(Learning [^.]+\.)',text)},
        'limit':'Locators preserve original sentence text. Surface counts are observations, not prose-quality or effect verdicts.'}
dest=record/'coordinator/output-index.json'
assert not dest.exists()
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for stage,data in out.items():
    print(stage,data['surface_observations'])
    for paragraph in data['paragraphs']:
        print(paragraph['id'],len(paragraph['sentences']),paragraph['sentences'][0]['text'])
