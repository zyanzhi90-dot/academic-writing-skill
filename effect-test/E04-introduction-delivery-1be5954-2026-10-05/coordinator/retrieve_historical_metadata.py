"""Archive pre-RSS primary citation versions for source review only."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import requests

record=Path(__file__).resolve().parents[1]
def fetch(entry):
    rid, version=entry
    url='https://arxiv.org/abs/'+version
    p=record/'coordinator/citation-sources'/(rid+'-historical.html')
    assert not p.exists()
    try:
        response=requests.get(url,timeout=40)
        response.raise_for_status()
        p.write_bytes(response.content)
        return {'id':rid,'version':version,'url':url,'status':response.status_code,
                'path':p.relative_to(record).as_posix(),'sha256':hashlib.sha256(response.content).hexdigest()}
    except requests.RequestException as error:
        return {'id':rid,'version':version,'url':url,'error':str(error)}
with ThreadPoolExecutor(max_workers=4) as pool:
    result=list(pool.map(fetch,[('R2','2206.11251v1'),('R7','2208.06193v2'),('R8','2304.02532v1'),('R9','2301.10677v2')]))
target=record/'coordinator/historical-citation-retrieval.json'
assert not target.exists()
target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
