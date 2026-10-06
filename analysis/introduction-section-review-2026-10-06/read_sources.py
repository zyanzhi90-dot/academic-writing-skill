"""Read indexed publication PDFs afresh; retain page blocks and page renders."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess

import pymupdf

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
INDEX = ROOT / 'skill-candidate/nature-shared/core/robotics-writing-examples.md'
REFERENCE = ROOT / 'skill-candidate/nature-shared/core/robotics-introduction-examples.md'
assert '(robotics-introduction-examples.md#selection)' in INDEX.read_text(encoding='utf-8')
targets = dict(re.findall(r'^\[(P17|P05|Fuzzy2023|ESO2017)\]: <([^>]+)>$',
                          REFERENCE.read_text(encoding='utf-8'), re.M))
assert set(targets) == {'P17', 'P05', 'Fuzzy2023', 'ESO2017'}
poppler = shutil.which('pdftoppm')
assert poppler
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
provenance = {'scope': 'Fresh PDF Introduction reading for section-level analysis only',
              'base_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT).decode().strip(),
              'index_route': [INDEX.relative_to(ROOT).as_posix(), REFERENCE.relative_to(ROOT).as_posix()],
              'index_sha256': {p.relative_to(ROOT).as_posix(): sha(p) for p in (INDEX, REFERENCE)},
              'author_inputs_sha256': {name: sha(ROOT / name) for name in
                                       ('核心要求.txt', '我自己的经验和做法.txt', '引言写作方法.txt')},
              'author_change_present_at_start': ['核心要求.txt'],
              'render_engine': poppler, 'render_dpi': 140,
              'papers': {},
              'limit': 'Raw pages also contain non-Introduction matter; the separately identified paragraph units exclude it.'}
for paper, target in targets.items():
    pdf = (REFERENCE.parent / target).resolve()
    assert pdf.is_file() and pdf.is_relative_to(ROOT)
    doc = pymupdf.open(pdf)
    pages = 3 if paper == 'ESO2017' else 2
    blocks, plain = [], []
    for index in range(pages):
        page = doc[index]
        plain.append(f'=== PDF p.{index+1} ===\n' + page.get_text())
        for block in page.get_text('blocks'):
            if block[6] == 0:
                blocks.append({'id': f'p{index+1}-b{block[5]}', 'page': index+1,
                               'bbox': list(block[:4]), 'text': block[4]})
        image = OUT / f'{paper}-p{index+1}.png'
        assert not image.exists()
        subprocess.run([poppler, '-f', str(index+1), '-l', str(index+1), '-singlefile',
                        '-r', '140', '-png', str(pdf), str(image.with_suffix(''))],
                       check=True, capture_output=True)
    (OUT / f'{paper}-page-blocks.json').write_text(json.dumps(blocks, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    (OUT / f'{paper}-raw-pages.txt').write_text('\n'.join(plain), encoding='utf-8')
    (OUT / f'{paper}-block-reading.txt').write_text('\n\n'.join(
        f"[{b['id']}; bbox={','.join(str(round(v,1)) for v in b['bbox'])}]\n{b['text']}" for b in blocks), encoding='utf-8')
    provenance['papers'][paper] = {'pdf': pdf.relative_to(ROOT).as_posix(), 'pdf_sha256': sha(pdf),
                                 'document_pages': len(doc), 'read_pages': list(range(1, pages+1)),
                                 'metadata': doc.metadata, 'block_count': len(blocks),
                                 'renders': [f'{paper}-p{index+1}.png' for index in range(pages)]}
    doc.close()
(OUT / 'source-provenance.json').write_text(json.dumps(provenance, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({key: {'read_pages': value['read_pages'], 'block_count': value['block_count']}
                  for key, value in provenance['papers'].items()}, ensure_ascii=False))
