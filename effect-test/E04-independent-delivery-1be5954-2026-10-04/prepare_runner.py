"""Adapt the accepted material-only runner; preserve both first invocations."""
from pathlib import Path
import hashlib
import json

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
source = ROOT / 'effect-test/E02-delivery-repair-2026-10-04/execute_once.py'
text = source.read_text(encoding='utf-8')
start = text.index('    previous = json.loads(')
end = text.index('    if draft is not None:', start)
text = text[:start] + '''    previous_stage = ROOT / 'effect-test/E02-delivery-repair-2026-10-04/drafting-frozen'
    previous = json.loads((previous_stage / 'frozen-run.json').read_text(encoding='utf-8'))
    reused = {}
    for name, expected in previous['materials_sha256'].items():
        if name.startswith(('skill-candidate/', 'inputs/')):
            continue
        source = previous_stage / 'materials' / name
        assert digest(source) == expected
        p = materials / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(source.read_bytes())
        reused[name] = {'source': source.relative_to(ROOT).as_posix(), 'sha256': expected}
    inputs = materials / 'inputs'
    inputs.mkdir()
    input_sources = {
        'scientific-facts.md': RECORD / 'scientific-facts.md',
        'task.md': RECORD / 'drafting-task.md',
        'personal-experience.txt': ROOT / '我自己的经验和做法.txt',
        'core-requirements.txt': ROOT / '核心要求.txt',
        'abstract-writing-method.txt': ROOT / '摘要写作方法.txt',
    }
    for name, source in input_sources.items():
        (inputs / name).write_bytes(source.read_bytes())
        reused['inputs/' + name] = {'source': source.relative_to(ROOT).as_posix(), 'sha256': digest(source)}
    identity = json.loads((RECORD / 'coordinator/input-identity.json').read_text(encoding='utf-8'))
    assert identity['case'] == 'E04' and digest(inputs / 'scientific-facts.md') == identity['facts_sha256']
    target_hash = identity['target_pdf_sha256']
    assert target_hash not in inventory(materials).values()
''' + text[end:]
text = text.replace("assert (materials / 'inputs/scientific-facts.md').read_bytes() == (ROOT / previous['facts_source']).read_bytes()", "assert (materials / 'inputs/scientific-facts.md').read_bytes() == (RECORD / 'scientific-facts.md').read_bytes()")
start = text.index("    command[0] = subprocess.check_output(")
end = text.index("    assert command[0]", start)
text = text[:start] + text[end:]
start = text.index('    installed = []')
end = text.index('    previous_disabled =', start)
text = text[:start] + '''    installed = []
    for user in ('user', 'user2'):
        for folder in ('.agents/skills', '.codex/skills', '.codex/plugins/cache'):
            base = Path('C:/Users') / user / folder
            if base.exists():
                installed.extend(p.as_posix() for p in base.rglob('SKILL.md'))
''' + text[end:]
text = text.replace("'new_paper_transfer_evidence': False", "'new_paper_transfer_evidence': True, 'case': 'E04'")
text = text.replace("'required_input_actual_returns': returned,", "'required_input_actual_returns': returned, 'input_identity': identity,")
dest = RECORD / 'execute_once.py'
assert not dest.exists()
dest.write_text(text, encoding='utf-8')
(RECORD / 'runner-provenance.json').write_text(json.dumps({
    'source': source.relative_to(ROOT).as_posix(),
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'adaptations': ['E04 facts and identity', 'original current author inputs', 'reference files only from frozen prior materials', 'retain working native CLI path', 'disable installed and plugin skills for both user homes', 'independent transfer flag'],
    'unchanged': ['one invocation per stage', 'full actual input return check', 'ephemeral material-only session', 'model and effort', 'first output retention and read audit'],
}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
