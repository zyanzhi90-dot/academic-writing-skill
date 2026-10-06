"""Reuse the last one-shot isolation unchanged; bind only this record and candidate."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess

record=Path(__file__).resolve().parent
root=record.parents[1]
prior=root/'effect-test/E04-introduction-delivery-ee74b27-2026-10-06'
commit='a29f1e1045bc86093e2f74a4fe288ba1e5970d76'
old='ee74b27dffa59ba79b5f14cf18687f60e0d866c5'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
git=lambda *a:subprocess.check_output(['git',*a],cwd=root)
assert git('rev-parse','HEAD').decode().strip()==commit
assert git('rev-parse','origin/main').decode().strip()==commit
copies=('scientific-facts.md','background-facts.md','citation-facts.md','accepted-abstract.en.txt',
        'drafting-task.md','polishing-task.md','current-author-adjustment.txt',
        'execute_once.py','retain_sections.py','verify_stage.py','save_delivery.py',
        'summarize_loading.py','index_outputs.py','verify_git_bytes.py')
for name in copies:
    assert not (record/name).exists()
    shutil.copyfile(prior/name,record/name)
for name in ('preflight.py','verify_records.py'):
    text=(prior/name).read_text(encoding='utf-8').replace(old,commit)
    if name=='verify_records.py':
        text=text.replace("p.name!='verification.json'", "p.name not in ('verification.json','git-byte-verification.json')")
    (record/name).write_text(text,encoding='utf-8')
identity=json.loads((prior/'coordinator/input-identity.json').read_text(encoding='utf-8'))
for name,expected in identity['author_inputs'].items():
    assert sha(root/name)==expected
identity.update({'candidate_commit':commit,'coordinator_start_commit':commit,'origin_main_at_start':commit,
                 'diagnosis_start_commit':'50d77287873375de04c851a6840f3fb06588ef84',
                 'candidate_git_bytes_sha256':{},
                 'source_identity_record':(prior/'coordinator/input-identity.json').relative_to(root).as_posix(),
                 'source_identity_record_sha256':sha(prior/'coordinator/input-identity.json')})
for name in filter(None,git('ls-tree','-r','--name-only','-z',commit,'skill-candidate').decode().split('\0')):
    identity['candidate_git_bytes_sha256'][name]=hashlib.sha256(git('show',commit+':'+name)).hexdigest()
(record/'coordinator').mkdir()
(record/'coordinator/input-identity.json').write_text(json.dumps(identity,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(record/'coordinator/experiment-state.json').write_text(json.dumps({
    'local_head_and_origin_main_at_current_start':commit,'frozen_candidate':commit,
    'model':'gpt-6.1-sol','reasoning_effort':'high','stages':['drafting','polishing'],
    'one_invocation_per_stage':True,'first_outputs_only':True,
    'feedback_reruns_allowed':False,'coordinator_prose_edits_allowed':False,
    'Skill_changes_after_freeze_or_installation_allowed':False},indent=2)+'\n',encoding='utf-8')
(record/'runner-provenance.json').write_text(json.dumps({
    'candidate_commit':commit,'source_record':prior.relative_to(root).as_posix(),
    'byte_identical_copies':{n:{'source_sha256':sha(prior/n),'copy_sha256':sha(record/n)} for n in copies},
    'executor_byte_identical':sha(prior/'execute_once.py')==sha(record/'execute_once.py'),
    'adaptations':'New record bindings, candidate identity in provenance checks, and exclusion of self-referential verification metadata from hash manifest. Execution, prompt construction, transport and isolation unchanged.',
    'model':'gpt-6.1-sol','reasoning_effort':'high','one_invocation_per_stage':True,
    'diagnosis_or_preset_argument_supplied':False,'prior_outputs_supplied':False,
    'scope':'Known-case E04; unchanged author/science inputs and author override'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Unchanged executor and inputs prepared for frozen candidate; no model invoked.')
