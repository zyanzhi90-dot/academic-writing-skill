"""Assemble complete Introductions from freshly read, visually checked PDF blocks.

This is source bookkeeping, not a writing executor or a Skill test.
"""
from pathlib import Path
import json
import re
import unicodedata

OUT = Path(__file__).resolve().parent
# Entries follow the printed paragraph indents, not extraction block boundaries.
# Contribution items are separately locatable units subordinate to their lead-in.
MAP = {
    'P17': [('I01', ['p1-b8', 'p1-b16']), ('I02', ['p1-b17']),
            ('I03', ['p1-b18']), ('I04', ['p1-b19', 'p2-b2']),
            ('I05', ['p2-b3']), ('I06', ['p2-b4', 'p2-b5']),
            ('I07', ['p2-b6']), ('I08', ['p2-b7']), ('I09', ['p2-b8'])],
    'P05': [('I01', ['p1-b8', 'p1-b15']), ('I02', ['p1-b16']),
            ('I03', ['p1-b17']), ('I04', ['p1-b18', 'p2-b1']),
            ('I05', ['p2-b2']), ('I06', ['p2-b3']),
            ('I07', ['p2-b4', 'p2-b6']), ('I08', ['p2-b7']),
            ('C1', ['p2-b8']), ('C2', ['p2-b8']), ('C3', ['p2-b8']),
            ('I09', ['p2-b8'])],
    'Fuzzy2023': [('I01', ['p1-b7', 'p1-b13']), ('I02', ['p1-b14']),
                  ('I03', ['p1-b15', 'p2-b1']), ('I04', ['p2-b2']),
                  ('C1', ['p2-b3']), ('C2', ['p2-b3']), ('C3', ['p2-b3'])],
    'ESO2017': [('I01', ['p1-b10', 'p1-b17']), ('I02', ['p1-b18']),
                ('I03', ['p1-b19']), ('I04', ['p2-b1']),
                ('I05', ['p2-b2']), ('I06', ['p2-b3']),
                ('I07', ['p2-b4']), ('I08', ['p2-b5']),
                ('C1', ['p2-b6']), ('C2', ['p3-b2']), ('C3', ['p3-b2']),
                ('I09', ['p3-b2'])],
}
DROP = {'P17': 'R', 'P05': 'R', 'Fuzzy2023': 'F', 'ESO2017': 'U'}
PRINT_START = {'P17': 777, 'P05': 1010, 'Fuzzy2023': 1041, 'ESO2017': 6785}
# Preserve semantic hyphens that happen to coincide with a printed line break.
COMPOUNDS = {
    'dual-arm', 'single-arm', 'semi-Nussbaum', 'fixed-time', 'finite-time',
    'prescribed-time', 'event-triggered', 'event-based', 'NN-based',
    'ESO-based', 'MIMO-ESO-based', 'neural-network-based', 'two-degree-of-freedom',
    'sliding-mode', 'sliding-mode-based', 'high-gain', 'high-order', 'dc-link',
    'output-feedback', 'output-feedback-based', 'output-feedback-tracking',
    'output-feedback-control', 'robot-environment', 'brain-actuated',
    'linear-in-parameter', 'model-based', 'nonstrict-feedback', 'strict-feedback',
    'leader-following', 'full-state', 'low-speed', 'NN-learning', 'nonmodel-based',
    'electro-hydraulic', 'DMP-based', 'style-adaptive', 'spring-damper',
    'above-mentioned', 'backpropagation', 'neural-learning', 'On-board',
    'sliding-mode-controller', 'integral-sliding-mode', 'state-observer',
    'error-integral', 'time-delay', 'multiple-output',
}
JOIN_LOG = {}


def normalize(paper, text):
    text = unicodedata.normalize('NFKC', text)
    def join(match):
        left, right = match.groups()
        compound = left + '-' + right
        merged = compound if compound in COMPOUNDS else left + right
        JOIN_LOG.setdefault(paper, {})[compound] = merged
        return merged
    text = re.sub(r'([A-Za-z]+)-\n([A-Za-z]+)', join, text)
    return re.sub(r'\s+', ' ', text).strip()


def split_selected(paper, unit, text):
    if paper == 'P05' and unit in ('C1', 'C2', 'C3', 'I09'):
        chunks = re.split(r'(?=\b[123]\) |In the following sections,)', text)
        return next(c.strip() for c in chunks if c.startswith(
            'In the following sections,' if unit == 'I09' else unit[-1] + ') '))
    if paper == 'Fuzzy2023' and unit.startswith('C'):
        return next(c.strip() for c in re.split(r'(?=\b[123]\) )', text)
                    if c.startswith(unit[-1] + ') '))
    if paper == 'ESO2017' and unit in ('C2', 'C3', 'I09'):
        chunks = re.split(r'(?=\b[23]\) |The remainder of this paper)', text)
        return next(c.strip() for c in chunks if c.startswith(
            'The remainder of this paper' if unit == 'I09' else unit[-1] + ') '))
    return text


assembled = {}
provenance = json.loads((OUT / 'source-provenance.json').read_text(encoding='utf-8'))
for paper, mapping in MAP.items():
    blocks = {b['id']: b for b in json.loads((OUT / f'{paper}-page-blocks.json').read_text(encoding='utf-8'))}
    units = []
    lines = [f'# {paper} — 完整 Introduction 原文定位', '',
             f"出版 PDF：`{provenance['papers'][paper]['pdf']}`。", '',
             '正文段落以 I 编号，贡献条目以 C 编号；C 是其引导段下的列表条目，不另造正文段落。', '',
             '仅恢复版面阅读顺序、跨栏/跨页续段、首字母、合字与行末断词；不润色出版原文。原始文本块和页面图像另行保留。', '']
    for unit, ids in mapping:
        raw = '\n'.join(blocks[i]['text'].strip() for i in ids)
        text = split_selected(paper, unit, normalize(paper, raw))
        if unit == 'I01':
            text = DROP[paper] + text
        spans = [{'block': i, 'pdf_page': blocks[i]['page'],
                  'printed_page': PRINT_START[paper] + blocks[i]['page'] - 1,
                  'column': '左' if blocks[i]['bbox'][0] < 300 else '右',
                  'bbox': blocks[i]['bbox']} for i in ids]
        # ESO p1 right column x=300.9 (the other papers have x>=305).
        if paper == 'ESO2017':
            for span in spans:
                if span['bbox'][0] > 300:
                    span['column'] = '右'
        units.append({'id': unit, 'source_spans': spans, 'text': text})
        location = ' → '.join(f"PDF p.{s['pdf_page']} / 刊页 {s['printed_page']} {s['column']}栏 ({s['block']})" for s in spans)
        lines += [f'## {unit}', '', location, '', text, '']
    assembled[paper] = units
    (OUT / f'{paper}-introduction.md').write_text('\n'.join(lines), encoding='utf-8')
(OUT / 'curated-introductions.json').write_text(json.dumps(assembled, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
(OUT / 'layout-normalization.json').write_text(json.dumps(JOIN_LOG, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'units': {p: len(u) for p, u in assembled.items()}, 'line_end_hyphen_decisions': JOIN_LOG}, ensure_ascii=False, indent=2))
