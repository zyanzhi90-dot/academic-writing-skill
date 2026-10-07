"""Freeze one review-only task; reuse original run/audit executor unchanged."""
from pathlib import Path
import hashlib
import json
import re
import runpy
import shutil
import subprocess
import tempfile

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
PRIOR = ROOT / 'effect-test/E04-introduction-delivery-ed9e42b-2026-10-07'
COMMIT = 'ed9e42bd68634d611dab0874d07c0ec200cbaabd'
BASE = '02152cb71f4db89c9b4851b4a5edaacf70e73aea'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
git = lambda *args: subprocess.check_output(['git', *args], cwd=ROOT)
inventory = lambda p: {f.relative_to(p).as_posix(): sha(f) for f in sorted(p.rglob('*')) if f.is_file()}

def save(p, obj):
    assert not p.exists(), p
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

assert git('rev-parse', 'HEAD').decode().strip() == BASE
assert not git('diff', COMMIT, '--', 'skill-candidate')
assert not (RECORD/'review').exists(), 'Never replace a prepared session'
for name in ('execute_once.py', 'verify_stage.py', 'verify_git_bytes.py'):
    shutil.copyfile(PRIOR/name, RECORD/name)
for name in ('summarize_loading.py', 'check_context.py'):
    text = (PRIOR/name).read_text(encoding='utf-8').replace("('drafting','polishing')", "('review',)")
    (RECORD/name).write_text(text, encoding='utf-8')
dest = RECORD/'review'
materials = dest/'materials'
shutil.copytree(PRIOR/'polishing/materials', materials)
previous = json.loads((PRIOR/'polishing/frozen-run.json').read_text(encoding='utf-8'))
assert inventory(materials) == previous['materials_sha256']
candidate = previous['candidate_sha256']
for name, expected in candidate.items():
    assert hashlib.sha256(git('show', COMMIT+':'+name)).hexdigest() == expected == sha(materials/name)
original_identity = json.loads((PRIOR/'coordinator/input-identity.json').read_text(encoding='utf-8'))
inputs = materials/'inputs'
normal = ('scientific-facts.md', 'background-facts.md', 'citation-facts.md', 'accepted-abstract.en.txt',
          'core-requirements.txt', 'personal-experience.txt', 'introduction-method.txt', 'current-author-adjustment.txt')
for name in normal:
    assert (inputs/name).read_bytes() == (PRIOR/'drafting/materials/inputs'/name).read_bytes()
for label, name in (("核心要求.txt", 'core-requirements.txt'),
                    ("我自己的经验和做法.txt", 'personal-experience.txt'),
                    ("引言写作方法.txt", 'introduction-method.txt')):
    assert (ROOT/label).read_bytes() == (inputs/name).read_bytes()
assert (inputs/'current-draft.md').read_bytes() == (PRIOR/'drafting/raw-introduction-and-references.md').read_bytes()
(inputs/'task.md').write_bytes((RECORD/'review-task.md').read_bytes())
(inputs/'original-writing-task.md').write_bytes((PRIOR/'drafting-task.md').read_bytes())
assert original_identity['target_pdf_sha256'] not in inventory(materials).values()
assert all(not any(x in n for x in ('/coordinator/', '/audit/', 'first-output', 'events.jsonl'))
           for n in inventory(materials))
runtime = Path(tempfile.mkdtemp(prefix='review-'))/'materials'
shutil.copytree(materials, runtime)
required = tuple('inputs/'+name for name in ('task.md', 'original-writing-task.md', *normal, 'current-draft.md'))
reader = runpy.run_path(str(ROOT/'effect-test/E03-independent-transfer-fd7dbcb-valid-2026-10-04/execute_once.py'))
reader['read_required_inputs'].__globals__.update({'RECORD': dest, 'REQUIRED_INPUTS': required,
                                                'save': lambda name,obj: save(dest/name,obj)})
returned = reader['read_required_inputs'](runtime, phase='before-invocation')
prompt = (
    f"Perform only the review task at {runtime/'inputs/task.md'} using the frozen local nature-polishing "
    f"candidate at {runtime/'skill-candidate/nature-polishing/SKILL.md'} and its declared dependencies. "
    "Read its router, manifest, required core, matching fragments, robotics common instructions and task-selected "
    "Introduction positive learning with complete selected English, context and analysis. Apply the candidate's "
    "review capabilities to the supplied draft, subject to the review-only author task. "
    "The original-writing-task.md records the author assignment that produced this draft, not an instruction "
    "to write another draft. The current-author-adjustment.txt takes priority over conflicting older text. "
    "Reference science does not add author facts. Only the material directory is permitted input. "
    "Do not read installed skills, the source project, target original paper/introduction, historical outputs, "
    "feedback, diagnoses, evaluations or execution records. Do not browse or change files. "
    "Return only a review report grounded in actual draft passages and applicable author/source evidence, "
    "distinguishing issues from reasonable variants. Do not produce revised prose or replacement sentences. "
    "Read UTF-8 using absolute paths and bounded numbered ranges, one file per command. "
    "Always wrap indexed Get-Content in @(...) and verify actual returned content. "
    "This is a fresh first-pass session with no feedback or selection. The following normal author inputs "
    "were compared line by line with actual PowerShell returns and are included in full:\n"
)
for name in required:
    prompt += '\n<original-input path='+json.dumps(name)+'>\n'+(runtime/name).read_text(encoding='utf-8')+'\n</original-input>\n'
command = json.loads((PRIOR/'polishing/execution-command.json').read_text(encoding='utf-8'))
command[command.index('-C')+1] = str(runtime)
command[command.index('-o')+1] = str(dest/'first-output.md')
assert command[-1] == '-'
assert 'gpt-6.1-sol' in command and any('high' in x for x in command)
assert Path(command[0]).is_file()
(dest/'execution-prompt.txt').write_text(prompt, encoding='utf-8')
(dest/'runner-snapshot.py').write_bytes((RECORD/'execute_once.py').read_bytes())
save(dest/'execution-command.json', command)
identity = dict(original_identity)
identity.update({'baseline_commit':BASE, 'task_sha256':{'review':sha(inputs/'task.md')},
                 'original_writing_task_sha256':sha(inputs/'original-writing-task.md'),
                 'draft_sha256':sha(inputs/'current-draft.md'), 'review_only':True})
save(dest/'frozen-run.json', {
    'candidate_commit':COMMIT, 'stage':'review', 'role':'nature-polishing', 'model':'gpt-6.1-sol',
    'reasoning_effort':'high', 'attempt':1, 'case':'E04', 'section':'Introduction',
    'known_case_comparison':True, 'new_paper_transfer_evidence':False,
    'materials_sha256':inventory(materials), 'candidate_sha256':candidate,
    'input_identity':identity, 'required_input_actual_returns':returned, 'runtime':str(runtime),
    'prompt_sha256':sha(dest/'execution-prompt.txt'), 'runner_sha256':sha(RECORD/'execute_once.py'),
    'cli_sha256':sha(Path(command[0])), 'cli_version':subprocess.check_output([command[0],'--version']).decode().strip(),
    'isolation':'Same material-only external directory and disabled automatic context; explicit read audit, no OS sandbox claim.',
    'task_change':'One neutral review-only author request replaces generation request; original Writing assignment retained as provenance.'
})
save(RECORD/'input-provenance.json', {
    'baseline_commit':BASE, 'frozen_candidate':COMMIT, 'prior_record':PRIOR.relative_to(ROOT).as_posix(),
    'normal_input_sha256':{n:sha(inputs/n) for n in normal}, 'original_writing_task_sha256':sha(inputs/'original-writing-task.md'),
    'raw_writing_English_and_references_sha256':sha(inputs/'current-draft.md'),
    'same_candidate_and_normal_inputs':True, 'executor_byte_identical_to_prior':sha(RECORD/'execute_once.py')==sha(PRIOR/'execute_once.py'),
    'same_CLI_settings_except_runtime_and_output_path':all(a==b for i,(a,b) in enumerate(zip(command,json.loads((PRIOR/'polishing/execution-command.json').read_text(encoding='utf-8')))) if i not in (command.index('-C')+1,command.index('-o')+1)),
    'Polishing_output_evaluation_diagnosis_or_known_failure_supplied':False,
    'materials_inventory':inventory(materials), 'pre_invocation_actual_returns_verified':returned['actual_returned_content_checked']
})
print('Prepared one neutral review-only session; candidate, original author inputs and raw draft verified.')
