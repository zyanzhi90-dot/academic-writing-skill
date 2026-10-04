"""Validate actual abstract-only changes and dependency relocation before freezing."""
from pathlib import Path
import hashlib
import json
import runpy
import shutil
import subprocess
import tempfile

RECORD = Path(__file__).resolve().parent
ROOT = RECORD.parents[1]
BASE = 'e24dc05'
CHANGED = [
    'skill-candidate/nature-writing/manifest.yaml',
    'skill-candidate/nature-polishing/manifest.yaml',
    'skill-candidate/nature-writing/static/fragments/section/abstract.md',
    'skill-candidate/nature-polishing/static/fragments/section/abstract.md',
    'skill-candidate/nature-shared/core/abstract-delivery.md',
]
checker = runpy.run_path(str(ROOT / 'analysis/check_candidate_loading.py'))
base = ROOT / 'skill-candidate'
manifests = checker['manifests_at'](base)
case = {'id': 'abstract-delivery', 'sections': ['abstract'], 'language': 'zh-to-en',
        'journal': 'generic', 'abstract_references': ['A06', 'A07', 'A08']}
reads = [checker['read_case'](base, role, case, manifests[role][0])
         for role in ('nature-writing', 'nature-polishing')]
with tempfile.TemporaryDirectory(prefix='abstract-delivery-loading-') as tmp:
    relocated = Path(tmp) / 'skill-candidate'
    shutil.copytree(base, relocated)
    moved = checker['manifests_at'](relocated)
    assert reads == [checker['read_case'](relocated, role, case, moved[role][0])
                     for role in ('nature-writing', 'nature-polishing')]
    for role in ('nature-writing', 'nature-polishing'):
        fragment = relocated / role / 'static/fragments/section/abstract.md'
        assert (fragment.parent / '../../../../nature-shared/core/abstract-delivery.md').resolve().is_file()
        assert '../../../../nature-shared/core/abstract-delivery.md' in fragment.read_text(encoding='utf-8')
checks = [checker['check_powershell_utf8'](ROOT / name) for name in CHANGED]
validation = []
for role in ('nature-writing', 'nature-polishing'):
    result = subprocess.run(['python', '-X', 'utf8', 'C:/Users/user/.codex/skills/.system/skill-creator/scripts/quick_validate.py', str(base / role)],
                            capture_output=True, check=True)
    validation.append({'role': role, 'exit_code': result.returncode, 'stdout': result.stdout.decode('utf-8')})
unchanged = []
for name in subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', BASE, 'skill-candidate'], cwd=ROOT).decode().splitlines():
    if name in CHANGED:
        continue
    old = subprocess.check_output(['git', 'show', BASE + ':' + name], cwd=ROOT)
    assert (ROOT / name).read_bytes().replace(b'\r\n', b'\n') == old.replace(b'\r\n', b'\n'), name
    unchanged.append(name)
subprocess.run(['git', 'diff', '--check'], cwd=ROOT, check=True)
report = {'base': BASE, 'changed_skill_files': CHANGED, 'all_other_candidate_files_unchanged': unchanged,
          'routers_workflows_examples_scientific_expression_and_guarantees_unchanged': True,
          'utf8_actual_powershell_returns': checks, 'quick_validate': validation,
          'two_routes': reads, 'relocated_routes_identical': True, 'relative_delivery_links_resolve': True,
          'changed_files_sha256': {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in CHANGED},
          'effect_verdict': 'No effect conclusion from implementation or loading'}
assert not (RECORD / 'preflight.json').exists()
(RECORD / 'preflight.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('Scope, UTF-8, manifests, relative links, relocation and validation passed')
