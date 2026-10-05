"""Describe returned example sections, including incidental abstract cards."""
from pathlib import Path
import hashlib
import json
import re

record = Path(__file__).resolve().parent
result = {}
for stage in ('drafting', 'polishing'):
    dest = record / stage
    audit = json.loads((dest / 'loading-and-retention.json').read_text(encoding='utf-8'))
    exact = audit['actual_numbered_returns']
    files = {}
    for name in ('skill-candidate/nature-shared/core/robotics-introduction-examples.md',
                 'skill-candidate/nature-shared/core/robotics-writing-examples.md'):
        path = dest / 'materials' / name
        lines = path.read_text(encoding='utf-8').splitlines()
        seen = set(exact.get(name, {}).get('matching_numbered_lines', []))
        intro = name.endswith('robotics-introduction-examples.md')
        pattern = r'## B\d+' if intro else r'### [AB]\d+.*'
        cards = {}
        for start, title in enumerate(lines, 1):
            if not re.fullmatch(pattern, title):
                continue
            end = next((i-1 for i in range(start+1, len(lines)+1)
                        if lines[i-1].startswith(('## ',) if intro else ('### ', '## '))), len(lines))
            expected = {i for i in range(start, end+1) if lines[i-1]}
            returned = sorted(expected & seen)
            quotes = [i for i in range(start, end+1) if lines[i-1].startswith('> ')]
            card = re.search(r'\b[AB]\d+\b', title)[0]
            sections = []
            if intro:
                headings = [i for i in range(start, end+1) if re.fullmatch(r'\*\*[^*].*\*\*', lines[i-1])]
                for k, i in enumerate(headings):
                    if not re.search(r'I\d+|C\d+', lines[i-1]):
                        continue
                    last = headings[k+1]-1 if k+1 < len(headings) else end
                    nonempty = {j for j in range(i, last+1) if lines[j-1]}
                    sections.append({'heading': lines[i-1], 'range': [i, last],
                                     'all_nonempty_lines_returned_exactly': nonempty <= seen,
                                     'English_quote_lines_returned': [j for j in quotes if i <= j <= last and j in seen]})
            cards[card] = {'range': [start, end], 'returned_nonempty_lines': returned,
                           'any_nonempty_returned': bool(returned),
                           'all_nonempty_lines_returned_exactly': expected <= seen,
                           'source_quote_lines_returned': [i for i in quotes if i in seen],
                           'paragraph_sections': sections}
        files[name] = {'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'cards': cards}
    result[stage] = files
target = record / 'coordinator/reading-detail.json'
assert not target.exists()
target.write_text(json.dumps({'stages': result,
    'limit': 'Exact returned lines establish access only; snippets and headings are not full-card reading or proof of correct use.'},
    ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({s:{name:{key:{k:v[k] for k in ('any_nonempty_returned', 'all_nonempty_lines_returned_exactly')}
    for key,v in data['cards'].items() if v['any_nonempty_returned']} for name,data in files.items()}
    for s,files in result.items()}, ensure_ascii=False))
