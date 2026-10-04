"""Check saved-stage identity and committed bytes without rerunning a model."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
STAGES = ('polishing-baseline', 'polishing-source-check', 'drafting-frozen', 'polishing-combined')


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def verify_records():
    stages = {}
    for name in STAGES:
        dest = RECORD / name
        frozen = json.loads((dest / 'frozen-run.json').read_text(encoding='utf-8'))
        meta = json.loads((dest / 'run-meta.json').read_text(encoding='utf-8'))
        assert meta['exit_code'] == 0 and meta['attempt'] == 1
        assert sha(dest / 'first-output.md') == meta['first_output_sha256']
        assert sha(dest / 'runner-snapshot.py') == frozen['runner_sha256']
        assert sha(dest / 'execution-prompt.txt') == frozen['prompt_sha256']
        assert {p.relative_to(dest / 'materials').as_posix(): sha(p) for p in sorted((dest/'materials').rglob('*')) if p.is_file()} == frozen['materials_sha256']
        for input_name, source in (('scientific-facts.md','effect-test/E02-abstract-materials-2026-10-03/科学事实包.md'),
                                   ('personal-experience.txt','我自己的经验和做法.txt'),
                                   ('core-requirements.txt','核心要求.txt'),
                                   ('abstract-writing-method.txt','摘要写作方法.txt')):
            assert (dest / 'materials/inputs' / input_name).read_bytes() == (ROOT / source).read_bytes()
        for path, expected in frozen['candidate_sha256'].items():
            assert hashlib.sha256(subprocess.check_output(['git','show',frozen['candidate_commit']+':'+path],cwd=ROOT)).hexdigest() == expected
        stages[name] = {'candidate': frozen['candidate_commit'], 'attempts': 1, 'first_output_sha256': sha(dest/'first-output.md'),
                        'model': frozen['model'], 'effort': frozen['reasoning_effort'], 'duration_seconds': meta['duration_seconds']}
    original = ROOT / 'effect-test/E02-abstract-judgment-regression-2026-10-04/drafting/first-output.md'
    for stage in ('polishing-baseline','polishing-source-check'):
        assert (RECORD/stage/'materials/inputs/current-draft.md').read_bytes() == original.read_bytes()
    assert (RECORD/'polishing-combined/materials/inputs/current-draft.md').read_bytes() == (RECORD/'drafting-frozen/first-output.md').read_bytes()
    assert (RECORD/'drafting-frozen/materials/inputs/task.md').read_bytes() == (ROOT/'effect-test/E02-abstract-judgment-regression-2026-10-04/materials/inputs/task.md').read_bytes()
    report = {'stages': stages, 'all_original_author_inputs_byte_identical': True,
              'same_draft_polishing_control_byte_identical': True, 'combined_handoff_byte_identical': True,
              'standard_drafting_request_byte_identical': True, 'runner_snapshots_match_pre_run_hashes': True,
              'frozen_candidate_bytes_match_git': True, 'effect_status': 'Separate prose evaluations; no migration claim'}
    target=RECORD/'record-integrity.json'
    assert not target.exists()
    target.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Four first outputs, original inputs, controls, handoff, runner and candidate identity passed')


def verify_git():
    names = subprocess.check_output(['git','ls-files','-z','--',str(RECORD.relative_to(ROOT))],cwd=ROOT).decode('utf-8').split('\0')
    count = 0
    for name in filter(None,names):
        if (ROOT/name).read_bytes() != subprocess.check_output(['git','show','HEAD:'+name],cwd=ROOT):
            raise AssertionError('Committed bytes differ: '+name)
        count += 1
    assert count > 0
    subprocess.run(['git','merge-base','--is-ancestor','1be5954','HEAD'],cwd=ROOT,check=True)
    print('Committed project record bytes verified:',count,'; frozen candidate remains reachable')


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('action',choices=['records','git'])
    args=parser.parse_args()
    verify_records() if args.action=='records' else verify_git()
