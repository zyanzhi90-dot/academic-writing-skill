"""Record direct PDF reads and exact continuous evidence for expression study."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

import pymupdf

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
PRIOR = ROOT / 'analysis/introduction-section-review-2026-10-06'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
provenance = json.loads((PRIOR / 'source-provenance.json').read_text(encoding='utf-8'))
curated = json.loads((PRIOR / 'curated-introductions.json').read_text(encoding='utf-8'))
specs = {
    'E01': [('P17', 'I01', 1, 3)],
    'E02': [('P05', 'I01', 1, 2)],
    'E03': [('ESO2017', 'I01', 1, 2)],
    'E04': [('P17', 'I02', 1, 3)],
    'E05': [('P17', 'I03', 1, 6)],
    'E06': [('P17', 'I04', 1, 5)],
    'E07': [('P17', 'I04', 6, 8)],
    'E08': [('P05', 'I02', 1, 3)],
    'E09': [('Fuzzy2023', 'I02', 2, 6)],
    'E10': [('ESO2017', 'I03', 6, 7)],
    'E11': [('ESO2017', 'I06', 3, 4)],
    'E12': [('ESO2017', 'I06', 6, 7)],
    'E13': [('P05', 'I07', 1, 4)],
    'E14': [('P17', 'I02', 4, 8)],
    'E15': [('P05', 'I02', 4, 5), ('P05', 'I03', 1, 2)],
    'E16': [('Fuzzy2023', 'I03', 3, 8)],
    'E17': [('P17', 'I06', 1, 6)],
    'E18': [('P17', 'I06', 7, 10)],
    'E19': [('P17', 'I05', 1, 2)],
    'E20': [('P17', 'I05', 3, 5)],
    'E21': [('P05', 'I07', 6, 7)],
    'E22': [('ESO2017', 'I08', 1, 3)],
    'E23': [('P17', 'I07', 1, 5)],
    'E24': [('P17', 'I08', 1, 5)],
    'E25': [('P05', 'I08', 1, 2), ('P05', 'C1', 1, 1),
            ('P05', 'C2', 1, 1), ('P05', 'C3', 1, 1)],
    'E26': [('Fuzzy2023', 'C1', 1, 1), ('Fuzzy2023', 'C2', 1, 2),
            ('Fuzzy2023', 'C3', 1, 1)],
}
record = {
    'base_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT).decode().strip(),
    'scope': 'Introduction expression study; direct complete PDF Introduction reads',
    'text_engine': 'PyMuPDF ' + pymupdf.VersionBind,
    'author_inputs_sha256': {n: sha(ROOT/n) for n in provenance['author_inputs_sha256']},
    'accepted_learning_inputs_sha256': {
        n: sha(ROOT/n) for n in [
            'analysis/introduction-section-learning-draft-2026-10-06/learning-draft.md',
            'analysis/introduction-paragraph-learning-2026-10-06/learning-draft.md']},
    'source_locator': (PRIOR/'curated-introductions.json').relative_to(ROOT).as_posix(),
    'source_locator_sha256': sha(PRIOR/'curated-introductions.json'),
    'papers': {},
}
for paper, p in provenance['papers'].items():
    pdf = ROOT/p['pdf']
    assert sha(pdf) == p['pdf_sha256']
    old = {b['id']: b for b in json.loads((PRIOR/f'{paper}-page-blocks.json').read_text(encoding='utf-8'))}
    with pymupdf.open(pdf) as doc:
        actual = {}
        for page_number in p['read_pages']:
            for b in doc[page_number-1].get_text('blocks'):
                if b[6] == 0:
                    actual[f'p{page_number}-b{b[5]}'] = {
                        'page': page_number, 'bbox': list(b[:4]), 'text': b[4]}
        ids = list(dict.fromkeys(s['block'] for u in curated[paper] for s in u['source_spans']))
        for bid in ids:
            assert actual[bid]['text'] == old[bid]['text'], (paper, bid)
        record['papers'][paper] = {
            'pdf': p['pdf'], 'pdf_sha256': sha(pdf), 'reopened_pages': p['read_pages'],
            'raw_intro_blocks': {bid: actual[bid] for bid in ids},
            'complete_verified_introduction': curated[paper],
            'all_intro_blocks_match_verified_source': True,
            'visually_reviewed_existing_page_renders': {n: sha(PRIOR/n) for n in p['renders']},
        }
evidence = []
for eid, spans in specs.items():
    selections = []
    for paper, uid, start, end in spans:
        u = next(u for u in curated[paper] if u['id'] == uid)
        sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', u['text'])
        assert ' '.join(sentences) == u['text']
        assert 1 <= start <= end <= len(sentences)
        chosen = sentences[start-1:end]
        text = ' '.join(chosen)
        assert text in u['text']
        selections.append({
            'paper': paper, 'unit': uid, 'sentence_range': [start, end],
            'source_spans': u['source_spans'], 'complete_source_unit': u['text'],
            'context_before': ' '.join(sentences[:start-1]),
            'context_after': ' '.join(sentences[end:]),
            'selected_text': text, 'selected_sentences': chosen,
            'selected_text_sha256': hashlib.sha256(text.encode('utf-8')).hexdigest(),
        })
    evidence.append({'id': eid, 'selections': selections})
(OUT/'pdf-reread.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
(OUT/'selected-expressions.json').write_text(json.dumps(evidence, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'pdfs': list(record['papers']), 'groups': len(evidence),
                  'sentences': sum(len(s['selected_sentences']) for e in evidence for s in e['selections'])}, ensure_ascii=False))
