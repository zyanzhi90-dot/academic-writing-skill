"""Coordinator-only primary sources; no source prose is sent to writers."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import requests
import pymupdf

RECORD=Path(__file__).resolve().parents[1]
OUT=RECORD/'coordinator/citation-sources'
OUT.mkdir(parents=True,exist_ok=True)
sources={
 'R1':('https://proceedings.mlr.press/v164/mandlekar22a.html','https://proceedings.mlr.press/v164/mandlekar22a/mandlekar22a.pdf'),
 'R2':('https://arxiv.org/abs/2206.11251','https://arxiv.org/pdf/2206.11251v1'),
 'R3':('https://proceedings.mlr.press/v164/florence22a.html','https://proceedings.mlr.press/v164/florence22a/florence22a.pdf'),
 'R4':('https://arxiv.org/abs/2006.11239',None),
 'R5':('https://arxiv.org/abs/1907.05600',None),
 'R6':('https://proceedings.mlr.press/v162/janner22a.html','https://proceedings.mlr.press/v162/janner22a/janner22a.pdf'),
 'R7':('https://arxiv.org/abs/2208.06193',None),
 'R8':('https://arxiv.org/abs/2304.02532',None),
 'R9':('https://arxiv.org/abs/2301.10677',None),
}
def retrieve(entry):
    key,urls=entry
    records=[]
    for ext,url in zip(('html','pdf'),urls):
        if url is None: continue
        target=OUT/(key+'.'+ext)
        assert not target.exists()
        try:
            result=requests.get(url,timeout=45)
            result.raise_for_status()
            target.write_bytes(result.content)
            item={'id':key,'url':url,'final_url':result.url,'status':result.status_code,'path':target.relative_to(RECORD).as_posix(),
                  'sha256':hashlib.sha256(result.content).hexdigest()}
            if ext=='pdf':
                document=pymupdf.open(target)
                text='\n'.join(f'=== PDF PAGE {i+1} ===\n'+p.get_text() for i,p in enumerate(document))
                extracted=OUT/(key+'.txt')
                extracted.write_text(text,encoding='utf-8')
                item.update({'pages':len(document),'extracted_path':extracted.relative_to(RECORD).as_posix(),
                             'text_sha256':hashlib.sha256(extracted.read_bytes()).hexdigest()})
            records.append(item)
        except Exception as error:
            records.append({'id':key,'url':url,'error':str(error)})
    return records
with ThreadPoolExecutor(max_workers=4) as pool:
    records=[item for group in pool.map(retrieve,sources.items()) for item in group]
target=RECORD/'coordinator/citation-retrieval.json'
assert not target.exists()
target.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{k:v for k,v in r.items() if k in ('id','status','pages','error')} for r in records],ensure_ascii=False))
