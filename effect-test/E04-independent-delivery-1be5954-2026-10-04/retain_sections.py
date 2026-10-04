"""Extract exact first-output sections; do not rewrite or assess their text."""
from pathlib import Path
import argparse
import hashlib
import json
import re

RECORD = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

def retain(stage):
    dest = RECORD / stage
    p = dest / 'first-output.md'
    text = p.read_text(encoding='utf-8')
    headings = list(re.finditer(r'(?m)^(?:\*\*[^\n]+\*\*|#{1,4} [^\n]+)\s*$', text))
    result = {}
    for i, heading in enumerate(headings):
        label = heading.group().lower()
        name = 'first-abstract.en.txt' if 'english' in label or '英文摘要' in label else ('first-abstract.zh.txt' if '中文' in label else None)
        if name is None:
            continue
        start = heading.end()
        end = headings[i+1].start() if i+1 < len(headings) else len(text)
        body = text[start:end].strip('\r\n')
        assert body and name not in result
        target = dest / name
        assert not target.exists()
        target.write_text(body + '\n', encoding='utf-8')
        assert body in text
        result[name] = {'sha256': sha(target), 'exact_original_substring': True, 'heading': heading.group().strip(),
                        'operation': 'Separate the original section; only surrounding line breaks normalized'}
    assert {'first-abstract.en.txt','first-abstract.zh.txt'} <= result.keys()
    report = {'stage':stage, 'source':p.name, 'source_sha256':sha(p), 'sections':result,
              'English_wording_changed':False, 'assessment_or_author_notes_sent_to_polishing':False}
    target = dest / 'section-retention.json'
    assert not target.exists()
    target.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Exact English and Chinese first sections retained:',stage)

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('stage')
    retain(parser.parse_args().stage)
