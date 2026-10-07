"""Confirm raw evidence bytes in the staged Git blobs, without rewriting evidence."""
from pathlib import Path
import hashlib
import json
import subprocess

RECORD=Path(__file__).resolve().parent
ROOT=RECORD.parents[1]
prefix=RECORD.relative_to(ROOT).as_posix()+'/'
raw=subprocess.check_output(['git','ls-files','-s','-z','--',prefix],cwd=ROOT)
entries=[]
for entry in filter(None,raw.split(b'\0')):
    metadata,name=entry.split(b'\t',1)
    mode,oid,stage=metadata.decode().split()
    assert stage=='0'
    entries.append((name.decode('utf-8'),oid))
assert entries
process=subprocess.Popen(['git','cat-file','--batch'],cwd=ROOT,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
checks={}
for name,oid in entries:
    if name==prefix+'git-byte-verification.json':
        continue
    process.stdin.write((oid+'\n').encode())
    process.stdin.flush()
    header=process.stdout.readline().decode().split()
    assert header[1]=='blob'
    size=int(header[2])
    data=process.stdout.read(size)
    assert process.stdout.read(1)==b'\n'
    actual=hashlib.sha256(data).hexdigest()
    expected=hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
    assert actual==expected,(name,'Git changed raw evidence bytes')
    checks[name[len(prefix):]]={'git_blob':oid,'sha256':actual,'byte_exact':True}
process.stdin.close()
assert process.wait()==0
target=RECORD/'git-byte-verification.json'
target.write_text(json.dumps({'all_staged_record_blobs_byte_exact':True,'checked_files':checks,
    'scope':'E04 records only; record-level -text prevents inherited line-ending conversions; PDFs are binary',
    'exclusions':'This derived audit file is updated after the inspected staging snapshot; final post-commit byte comparison covers all files'},
    ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('All',len(checks),'staged record blobs match original file bytes exactly')
