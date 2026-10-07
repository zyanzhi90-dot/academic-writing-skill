"""Audit freshly frozen root author inputs and their exact delivery to both stages."""
from pathlib import Path
import hashlib
import json
import subprocess

record = Path(__file__).resolve().parent
root = record.parents[1]
identity = json.loads((record / 'coordinator/input-identity.json').read_text(encoding='utf-8'))
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
mapping = {'核心要求.txt': 'core-requirements.txt', '我自己的经验和做法.txt': 'personal-experience.txt',
           '引言写作方法.txt': 'introduction-method.txt', 'current-author-adjustment.txt': 'current-author-adjustment.txt'}
assert set(identity['author_inputs']) == set(mapping)
checks = {}
for source, delivered in mapping.items():
    current = (root / source).read_bytes()
    frozen = (record / source).read_bytes()
    assert current == frozen
    expected = identity['author_inputs'][source]
    assert sha(root / source) == sha(record / source) == expected
    stages = {}
    for stage in ('drafting', 'polishing'):
        actual = record / stage / 'materials/inputs' / delivered
        assert actual.read_bytes() == current
        stages[stage] = sha(actual)
    blob = subprocess.check_output(['git', 'show', identity['candidate_commit'] + ':' + source], cwd=root)
    normalized_equal = current.replace(b'\r\n', b'\n') == blob.replace(b'\r\n', b'\n')
    assert normalized_equal
    checks[source] = {'root_sha256': expected, 'record_sha256': sha(record / source),
                      'stage_sha256': stages, 'root_git_bytes_equal': current == blob,
                      'root_git_content_equal_after_newline_normalization': normalized_equal}
assert identity['current_author_adjustment_sha256'] == identity['author_inputs']['current-author-adjustment.txt']
assert 'latest_author_clarification' not in identity and 'source_identity_record' not in identity
out = record / 'coordinator/current-author-input-verification.json'
assert not out.exists()
out.write_text(json.dumps({'author_inputs': checks, 'root_current_override_copied_byte_exact': True,
                          'historical_author_identity_or_override_inherited': False,
                          'executor_changed': False, 'coordinator_prose_edited': False,
                          'scope': 'Input provenance only; no effect verdict'}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('All four current root author inputs match record and both actual stage packets byte-exact.')
