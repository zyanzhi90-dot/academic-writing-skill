"""Read-only PDF source inspection; create analysis evidence, never change Skills."""
from pathlib import Path
import hashlib
import json
import subprocess
import pymupdf

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
PAPERS = {
    'P17': 'Robot_Learning_System_Based_on_Adaptive_Neural_Control_and_Dynamic_Movement_Primitives.pdf',
    'P05': 'Composite-Learning-Based_Adaptive_Neural_Control_for_Dual-Arm_Robots_With_Relative_Motion.pdf',
    'Fuzzy2023': 'Fixed-Time_Fuzzy_Control_of_Uncertain_Robots_With_Guaranteed_Transient_Performance.pdf',
    'ESO2017': 'Extended_State_Observer-Based_Integral_Sliding_Mode_Control_for_an_Underwater_Robot_With_Unknown_Disturbances_and_Uncertain_Nonlinearities.pdf',
}
records = {}
for key,name in PAPERS.items():
    pdf = ROOT / '文献资料' / name
    doc = pymupdf.open(pdf)
    first = []
    display = []
    for i in range(min(3,len(doc))):
        page=doc[i]
        blocks=[]
        for bid,b in enumerate(page.get_text('blocks')):
            if b[6] == 0:
                blocks.append({'id':bid, 'bbox':list(b[:4]), 'text':b[4]})
        first.append({'pdf_page':i+1, 'width':page.rect.width, 'height':page.rect.height, 'blocks':blocks})
        display.append(f'=== PDF p.{i+1} / blocks in column reading order ===')
        for b in sorted(blocks,key=lambda b:(0 if b['bbox'][0]<page.rect.width/2 else 1,b['bbox'][1],b['bbox'][0])):
            display.append(f"[p{i+1}-b{b['id']} bbox={','.join(f'{v:.1f}' for v in b['bbox'])}]\n{b['text']}")
        # ESO's Introduction also continues onto page 3; inspect its final list and roadmap.
        if i<2 or key=='ESO2017':
            (OUT/'page-previews').mkdir(exist_ok=True)
            page.get_pixmap(matrix=pymupdf.Matrix(1.35,1.35),alpha=False).save(str(OUT/'page-previews'/f'{key}-p{i+1}.png'))
    (OUT/f'{key}-page-blocks.txt').write_text('\n'.join(display),encoding='utf-8')
    (OUT/f'{key}-page-blocks.json').write_text(json.dumps(first,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    reused=ROOT/'analysis/reading'/f'{key}.txt'
    raw=subprocess.check_output(['pdftotext','-raw','-enc','UTF-8',str(pdf),'-']).decode('utf-8').replace('\r\n','\n')
    if key in ('P17','P05'):
        assert reused.is_file()
        # Reuse existing extraction verbatim; fresh raw text is only a source-identity comparison.
        archive=reused.read_bytes()
        pages=raw.split('\f')
        if not pages[-1].strip(): pages.pop()
        reconstructed='\n'.join(part for n,p in enumerate(pages,1) for part in (f'=== PDF PAGE {n} ===',p.strip(),''))
        assert reused.read_text(encoding='utf-8').replace('\r\n','\n') == reconstructed
        records[key]={'reused_extraction':reused.relative_to(ROOT).as_posix(),'reused_sha256':hashlib.sha256(archive).hexdigest(),
                      'fresh_raw_extraction_identical_after_EOL_normalization':True}
    else:
        p=OUT/f'{key}-full-raw.txt'
        p.write_text(raw,encoding='utf-8')
        records[key]={'new_raw_extraction':p.relative_to(ROOT).as_posix(),'raw_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
    records[key].update({'pdf':pdf.relative_to(ROOT).as_posix(), 'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
                         'pages':len(doc),'metadata':doc.metadata,
                         'evidence_limit':'Page blocks are evidence for paragraph and column verification; footnotes and captions are excluded only in the separately curated Introduction.'})
records['session']={'base_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT).decode().strip(),
                    'status_at_evidence_capture':subprocess.check_output(['git','status','--short'],cwd=ROOT).decode('utf-8'),
                    'core_requirements_sha256':hashlib.sha256((ROOT/'核心要求.txt').read_bytes()).hexdigest(),
                    'author_experience_sha256':hashlib.sha256((ROOT/'我自己的经验和做法.txt').read_bytes()).hexdigest(),
                    'task':'Introduction evidence analysis only; no Skill edit or model test'}
(OUT/'source-provenance.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('\n'.join(f"{k}: {v['pages']} PDF pages, source {v['pdf']}" for k,v in records.items() if k!='session'))
