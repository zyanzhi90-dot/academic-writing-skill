"""Reuse the E04 one-shot isolated mechanism; preserve author and scientific inputs."""
from pathlib import Path
import difflib
import hashlib
import json
import shutil
import subprocess

record = Path(__file__).resolve().parent
root = record.parents[1]
prior = root/'effect-test/E04-introduction-delivery-253dae3-2026-10-05'
commit = 'ee74b27dffa59ba79b5f14cf18687f60e0d866c5'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
git = lambda *a: subprocess.check_output(['git',*a],cwd=root)
assert git('rev-parse','HEAD').decode().strip()==commit
assert git('rev-parse','origin/main').decode().strip()==commit
for name in ('scientific-facts.md','background-facts.md','citation-facts.md','accepted-abstract.en.txt',
             'drafting-task.md','polishing-task.md','retain_sections.py','verify_stage.py','save_delivery.py'):
    assert not (record/name).exists()
    shutil.copyfile(prior/name,record/name)
update = record/'current-author-adjustment.txt'
assert not update.exists()
update.write_text(
    '本轮作者最新调整，优先于原样作者材料中的旧表述：\n'
    '本指令明确的范围和最新调整优先于历史任务与旧结论。ee74b27 删除的是新增实验排除规则，ESO 范例及其他引言要求保留；不得恢复该规则或新增替代规则。\n'
    'Introduction 内容由正向范例和正常科学论证决定，而不是额外增加禁止性默认规则。\n'
    '候选内正向学习资源用于模仿；audit 中出版原文、未采用表达和历史诊断用于审计，不进入写作会话作为模仿库。历史报告仅供协调端追溯，不作为写作材料。\n', encoding='utf-8')

identity = json.loads((prior/'coordinator/input-identity.json').read_text(encoding='utf-8'))
identity.update({'candidate_commit':commit,'coordinator_start_commit':commit,'origin_main_at_start':commit,
    'selection_basis':'Known E04 case; byte-identical 253dae3 scientific, background, citation and accepted Abstract inputs.',
    'source_identity_record':(prior/'coordinator/input-identity.json').relative_to(root).as_posix(),
    'source_identity_record_sha256':sha(prior/'coordinator/input-identity.json'),
    'candidate_git_bytes_sha256':{},
    'author_inputs':{n:sha(root/n) for n in ('核心要求.txt','我自己的经验和做法.txt','引言写作方法.txt')},
    'current_author_adjustment_sha256':sha(update),
    'author_input_conflict':'Original introduction-method.txt retains a withdrawn experiment-default sentence. The latest explicit author adjustment takes priority; original file bytes remain unchanged.',
    'task_sha256':{s:sha(record/(s+'-task.md')) for s in ('drafting','polishing')},
    'validation_scope':'Known-case E04 Introduction only; no migration, reliable omission detection or stability evidence'})
for name in filter(None,git('ls-tree','-r','--name-only','-z',commit,'skill-candidate').decode('utf-8').split('\0')):
    identity['candidate_git_bytes_sha256'][name]=hashlib.sha256(git('show',commit+':'+name)).hexdigest()
(record/'coordinator').mkdir()
(record/'coordinator/input-identity.json').write_text(json.dumps(identity,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(record/'coordinator/experiment-state.json').write_text(json.dumps({
    'local_head_and_origin_main_at_current_start':commit,'frozen_candidate':commit,
    'model':'gpt-6.1-sol','reasoning_effort':'high','stages':['drafting','polishing'],
    'one_invocation_per_stage':True,'first_outputs_only':True,
    'feedback_reruns_allowed':False,'coordinator_prose_edits_allowed':False,
    'Skill_changes_or_installation_allowed':False},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

original = (prior/'execute_once.py').read_text(encoding='utf-8')
code = original
changes = [
    ("effect-test/E04-introduction-delivery-1be5954-2026-10-05/drafting", "effect-test/E04-introduction-delivery-253dae3-2026-10-05/drafting"),
    ("'introduction-method.txt': ROOT / '引言写作方法.txt',", "'introduction-method.txt': ROOT / '引言写作方法.txt',\n        'current-author-adjustment.txt': RECORD / 'current-author-adjustment.txt',"),
    ("'introduction-method.txt', 'background-facts.md'", "'introduction-method.txt', 'current-author-adjustment.txt', 'background-facts.md'"),
    ('"Only the material directory is permitted input.',
     '"The current-author-adjustment.txt is the latest author requirement and takes priority over conflicting older author text. "\n        "Use the frozen candidate positive learning for imitation; publication sources are only optional source lookups. "\n        "Only the material directory is permitted input.'),
    ("    assert command[0] and Path(command[0]).suffix == '.exe'",
     "    historical_cli = command[0]\n    command[0] = 'C:/Users/user2/AppData/Roaming/npm/node_modules/@openai/codex-win32-x64/vendor/x86_64-pc-windows-msvc/bin/codex.exe'\n    assert Path(command[0]).is_file() and Path(command[0]).suffix == '.exe'"),
    ("'cli_version': subprocess.check_output([command[0], '--version']).decode().strip(),",
     "'cli_version': subprocess.check_output([command[0], '--version']).decode().strip(),\n        'historical_cli_path': historical_cli,\n        'cli_location_adjustment': 'Same installed Codex CLI, current npm vendor location; no install or executor logic change.',"),
]
for a,b in changes:
    assert code.count(a)==1,(a,code.count(a))
    code=code.replace(a,b)
(record/'execute_once.py').write_text(code,encoding='utf-8')
(record/'runner-adaptation.diff').write_text(''.join(difflib.unified_diff(
    original.splitlines(True),code.splitlines(True),fromfile='E04 253dae3 isolated runner',
    tofile='E04 ee74b27 isolated runner')),encoding='utf-8')
pre = (prior/'preflight.py').read_text(encoding='utf-8').replace('253dae364a603c477fd7d9d5c3cae89c98274927',commit)
pre = pre.replace("'introduction-method.txt':identity['author_inputs']['引言写作方法.txt'],",
                  "'introduction-method.txt':identity['author_inputs']['引言写作方法.txt'],\n    'current-author-adjustment.txt':identity['current_author_adjustment_sha256'],")
(record/'preflight.py').write_text(pre,encoding='utf-8')
(record/'runner-provenance.json').write_text(json.dumps({
    'candidate_commit':commit,'source_record':prior.relative_to(root).as_posix(),
    'runner_source_sha256':sha(prior/'execute_once.py'),'runner_sha256':sha(record/'execute_once.py'),
    'input_copies':{n:{'source_sha256':sha(prior/n),'copy_sha256':sha(record/n),
                      'byte_identical':(prior/n).read_bytes()==(record/n).read_bytes()}
                  for n in ('scientific-facts.md','background-facts.md','citation-facts.md','accepted-abstract.en.txt','drafting-task.md','polishing-task.md')},
    'changes':'Reuse 253dae3 materials; preserve three current raw author files and separately supply the explicit latest author override; locate existing CLI at current npm vendor path. Same isolation flags, stdin transport and single-invocation guards.',
    'mainline_order_or_repair_supplied':False,'evaluation_checklist_supplied':False,
    'model':'gpt-6.1-sol','reasoning_effort':'high','one_invocation_per_stage':True,
    'historical_records_changed':False,'scope':'Only this new effect-test record; no Skill change or installation'},
    ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Frozen candidate and unchanged E04 inputs prepared; no model invoked.')
