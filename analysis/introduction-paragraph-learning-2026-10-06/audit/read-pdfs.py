"""Reopen the publication PDFs and retain source evidence for paragraph study."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

import pymupdf

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
PRIOR = ROOT / 'analysis/introduction-section-review-2026-10-06'
provenance = json.loads((PRIOR / 'source-provenance.json').read_text(encoding='utf-8'))
curated = json.loads((PRIOR / 'curated-introductions.json').read_text(encoding='utf-8'))
selected = [('P17', 'I01'), ('ESO2017', 'I01'), ('P05', 'I02'),
            ('P17', 'I04'), ('Fuzzy2023', 'I02'), ('Fuzzy2023', 'I03'),
            ('P17', 'I05'), ('P17', 'I07'), ('P17', 'I08')]
sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
record = {'base_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT).decode().strip(),
          'scope': 'Fresh read of complete publication Introductions; paragraph and continuous-sentence study',
          'text_engine': 'PyMuPDF ' + pymupdf.VersionBind,
          'author_inputs_sha256': {name: sha(ROOT / name) for name in provenance['author_inputs_sha256']},
          'source_locator': (PRIOR / 'curated-introductions.json').relative_to(ROOT).as_posix(),
          'source_locator_sha256': sha(PRIOR / 'curated-introductions.json'),
          'papers': {}}
for paper, p in provenance['papers'].items():
    pdf = ROOT / p['pdf']
    assert sha(pdf) == p['pdf_sha256']
    original = {b['id']: b for b in json.loads((PRIOR / f'{paper}-page-blocks.json').read_text(encoding='utf-8'))}
    with pymupdf.open(pdf) as doc:
        actual = {}
        for page_number in p['read_pages']:
            for block in doc[page_number - 1].get_text('blocks'):
                if block[6] == 0:
                    actual[f'p{page_number}-b{block[5]}'] = {'page': page_number, 'bbox': list(block[:4]), 'text': block[4]}
        ids = list(dict.fromkeys(s['block'] for unit in curated[paper] for s in unit['source_spans']))
        for block_id in ids:
            assert actual[block_id]['text'] == original[block_id]['text'], (paper, block_id)
        record['papers'][paper] = {'pdf': p['pdf'], 'pdf_sha256': sha(pdf),
                                   'reopened_pages': p['read_pages'],
                                   'introduction_units': len(curated[paper]),
                                   'raw_intro_blocks': {block_id: actual[block_id] for block_id in ids},
                                   'all_intro_blocks_match_verified_source': True,
                                   'reused_page_renders': {name: sha(PRIOR / name) for name in p['renders']}}
units = []
for paper, unit_id in selected:
    unit = next(u for u in curated[paper] if u['id'] == unit_id)
    # These selected paragraphs contain no sentence-internal abbreviations with periods.
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', unit['text'])
    assert ' '.join(sentences) == unit['text']
    units.append({'paper': paper, 'unit': unit_id, 'source_spans': unit['source_spans'],
                  'text': unit['text'], 'sentences': sentences,
                  'text_sha256': hashlib.sha256(unit['text'].encode('utf-8')).hexdigest()})
(OUT / 'pdf-reread.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
(OUT / 'selected-sentences.json').write_text(json.dumps(units, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'pdfs_reopened': list(record['papers']), 'selected_paragraphs': len(units),
                  'sentence_counts': {u['paper'] + '-' + u['unit']: len(u['sentences']) for u in units}}, ensure_ascii=False))
