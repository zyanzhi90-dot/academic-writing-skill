"""Candidate integrity and explicitly selected file reads; no model execution.

Reuse established manifest/UTF-8/read-route audit functions without executing
their historical entrypoints or overwriting their historical records.
"""
import ast
import hashlib
import json
from pathlib import Path
import re
import runpy
import shutil
import subprocess
import sys
import tempfile

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
CANDIDATE = ROOT / 'skill-candidate'
BASE = '033fb2f77ba3df5a0da916963c600e80bd018f19'
REVIEW = ROOT / 'analysis/introduction-three-level-review-2026-10-05'
INDEX = 'nature-shared/core/robotics-writing-examples.md'
NEW = 'nature-shared/core/robotics-introduction-examples.md'
EXPECTED_REVIEW = {'P05-analysis.md', 'ESO2017-analysis.md', 'analysis-notes.json',
                   'build_analysis.py', 'report.md'}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def frozen(path):
    return subprocess.check_output(['git', 'show', BASE + ':' + path], cwd=ROOT)


CHECKER = runpy.run_path(str(ROOT / 'analysis/check_candidate_loading.py'))
old_cards = CHECKER['cards']
manifest_check = CHECKER['manifests_at']
# Only compile these reusable definitions; the old audit's module body is not run.
prior_audit = ROOT / 'analysis/introduction-candidate-update-2026-10-05/check_update.py'
tree = ast.parse(prior_audit.read_text(encoding='utf-8'))
definitions = [node for node in tree.body
               if isinstance(node, ast.FunctionDef) and node.name in {'card_units', 'read_route'}
               or isinstance(node, ast.Assign)
               and any(isinstance(t, ast.Name) and t.id == 'CASES' for t in node.targets)]
exec(compile(ast.Module(body=definitions, type_ignores=[]), str(prior_audit), 'exec'))

new_text = (CANDIDATE / NEW).read_text(encoding='utf-8')
units = card_units(new_text)
assert set(units) == {'B15', 'B16', 'B17', 'B18'}
assert new_text.count('**科学链。**') == 4
index_text = (CANDIDATE / INDEX).read_text(encoding='utf-8')
assert old_cards(index_text) == old_cards(frozen('skill-candidate/' + INDEX).decode('utf-8'))
assert len(old_cards(index_text)) == 22
assert '(robotics-introduction-examples.md#selection)' in index_text
assert '默认表达锚点' in new_text and 'B15／P17／A06' in new_text
assert '按当前段落任务选读完整英文及其逐句表' in new_text
assert '整节主线与段落任务由作者研究自主确定' in new_text
assert not re.search(r'\]\([^)]*analysis/', new_text)

source = json.loads((REVIEW / 'curated-introductions.json').read_text(encoding='utf-8'))
sentences = json.loads((REVIEW / 'source-sentences.json').read_text(encoding='utf-8'))
notes = json.loads((REVIEW / 'analysis-notes.json').read_text(encoding='utf-8'))
provenance = json.loads((REVIEW / 'source-provenance.json').read_text(encoding='utf-8'))
paper_for = {'B15': 'P17', 'B16': 'P05', 'B17': 'Fuzzy2023', 'B18': 'ESO2017'}
quote_records = []
for card, text in units.items():
    paper = paper_for[card]
    for quote in re.findall(r'^> (.+)$', text, re.M):
        matches = []
        for paragraph in source[paper]:
            ss = sentences[paper][paragraph['id']]
            for start in range(len(ss)):
                for end in range(start + 1, len(ss) + 1):
                    if quote == ' '.join(ss[start:end]):
                        matches.append((paragraph, start + 1, end))
        assert len(matches) == 1, (card, quote)
        paragraph, start, end = matches[0]
        quote_records.append({'card': card, 'paper': paper, 'unit': paragraph['id'],
                              'sentences': [start, end], 'blocks': paragraph['blocks'],
                              'complete_paragraph': quote == paragraph['text'],
                              'verbatim_contiguous_sentences': True,
                              'text': quote, 'sha256': sha(quote.encode('utf-8'))})

old_quotes = re.findall(r'^> (.+)$', frozen('skill-candidate/' + NEW).decode('utf-8'), re.M)
current_quotes = [q['text'] for q in quote_records]
assert all(q in current_quotes or any(q in current for current in current_quotes) for q in old_quotes)
sentence_tables = []
subselection = []
for card, text in units.items():
    paper = paper_for[card]
    default_unit = None
    for line in text.splitlines():
        header = re.match(r'^\| (I\d{2}) (?:句|原句范围) \|', line)
        if header:
            default_unit = header[1]
        row = re.match(r'^\| (?:(I\d{2}) )?S(\d{2}) \| (.+) \|$', line)
        if row:
            unit = row[1] or default_unit
            number = int(row[2])
            assert unit and 1 <= number <= len(sentences[paper][unit]), (card, line)
            assert any(q['paper'] == paper and q['unit'] == unit
                       and q['sentences'][0] <= number <= q['sentences'][1] for q in quote_records)
            sentence_tables.append({'card': card, 'unit': unit, 'sentence': number,
                                    'analysis': row[3]})
    # Demonstrate selecting a paragraph group with its English and analysis.
    # This records a file-slice audit, not a model's autonomous reading decision.
    target = {'B15': 'I05', 'B16': 'I02–I03', 'B17': 'I02–I03', 'B18': 'I06'}[card]
    headings = list(re.finditer(r'^\*\*[^\n]+\*\*$', text, re.M))
    selected = next(i for i, m in enumerate(headings) if target in m[0])
    start = headings[selected].start()
    end = headings[selected+1].start() if selected+1 < len(headings) else len(text)
    section = text[start:end]
    assert '> ' in section and '| S' in section or '> ' in section and '| I' in section
    subselection.append({'card': card, 'target': target, 'heading': headings[selected][0],
                         'characters': len(section), 'sha256': sha(section.encode('utf-8')),
                         'complete_English_context_and_sentence_analysis_read': True})
source_checks = {}
for paper, paragraphs in source.items():
    assert source[paper] == json.loads(frozen(str(REVIEW.relative_to(ROOT) / 'curated-introductions.json').replace('\\', '/')))[paper]
    assert sha((ROOT / provenance[paper]['pdf']).read_bytes()) == provenance[paper]['pdf_sha256']
    analysis = (REVIEW / f'{paper}-analysis.md').read_text(encoding='utf-8')
    for p in paragraphs:
        assert ' '.join(sentences[paper][p['id']]) == p['text']
        assert '> ' + p['text'] in analysis
        assert len(notes[paper][p['id']]['sentences']) == len(sentences[paper][p['id']])
    source_checks[paper] = {'pdf': provenance[paper]['pdf'],
                           'pdf_sha256': provenance[paper]['pdf_sha256'],
                           'original_units_preserved': len(paragraphs)}

report = (REVIEW / 'report.md').read_text(encoding='utf-8')
report_quotes = []
for match in re.finditer(r'<!-- source (\w+) (\w+) (\d+) (\d+) -->\s*\n> ([^\n]+)', report):
    paper, unit, start, end, quote = match.groups()
    assert quote == ' '.join(sentences[paper][unit][int(start)-1:int(end)])
    report_quotes.append({'paper': paper, 'unit': unit, 'sentences': [int(start), int(end)]})
assert len(report_quotes) == report.count('<!-- source ')
assert '优势带来运动控制复杂性' not in (REVIEW / 'P05-analysis.md').read_text(encoding='utf-8')
assert '为 I07 当前传感条件下的状态估计铺垫' not in notes['ESO2017']['I06']['paragraph_handoff']
assert '当前速度不可直接测量' in notes['ESO2017']['I06']['paragraph_handoff']
assert 'The designed observer estimates not only the model uncertainties but also the unmeasured states.' in units['B18']

links = dict(re.findall(r'^\[([^\]]+)\]: <(.*?)>$', new_text, re.M))
assert set(links) == set(source)
assert all(((CANDIDATE / NEW).parent / target).resolve().is_file() for target in links.values())
routes = []
powershell_reads = [CHECKER['check_powershell_utf8'](CANDIDATE / NEW),
                    CHECKER['check_powershell_utf8'](CANDIDATE / INDEX)]
validation = []
with tempfile.TemporaryDirectory(prefix='intro-three-level-read-') as temporary:
    moved = Path(temporary) / 'candidate-only'
    shutil.copytree(CANDIDATE, moved)
    for base, environment in ((CANDIDATE, 'project'), (moved, 'relocated-candidate-only')):
        manifests = manifest_check(base)
        declared = manifests['nature-shared'][0]['core']['on_demand']
        assert any(entry['path'] == 'core/robotics-introduction-examples.md' for entry in declared)
        for name in ('nature-writing', 'nature-polishing'):
            for case in CASES:
                routes.append(read_route(base, name, case, manifests[name][0], environment))
        for name in ('nature-writing', 'nature-polishing', 'nature-shared'):
            for path in (base / name).rglob('*'):
                if path.is_file():
                    path.read_bytes().decode('utf-8')
    assert not (moved / 'analysis').exists() and not (moved / '文献资料').exists()
    assert all(not ((moved / NEW).parent / target).resolve().exists() for target in links.values())
    validator = Path('C:/Users/user2/.codex/skills/.system/skill-creator/scripts/quick_validate.py')
    for name in ('nature-writing', 'nature-polishing', 'nature-shared'):
        process = subprocess.run([sys.executable, '-X', 'utf8', str(validator), str(moved / name)],
                                 capture_output=True, text=True, encoding='utf-8')
        assert process.returncode == 0, (name, process.stdout, process.stderr)
        validation.append({'package': name, 'exit_code': process.returncode,
                           'stdout': process.stdout, 'stderr': process.stderr,
                           'scope': 'frontmatter/naming, not behavioral or effect validation'})

candidate_changes = []
all_paths = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', BASE, 'skill-candidate'], cwd=ROOT).decode('utf-8').splitlines()
for path in all_paths:
    if frozen(path).decode('utf-8').splitlines() != (ROOT / path).read_text(encoding='utf-8').splitlines():
        candidate_changes.append(path)
assert candidate_changes == ['skill-candidate/' + NEW]
assert set(p.relative_to(ROOT).as_posix() for p in CANDIDATE.rglob('*') if p.is_file()) == set(all_paths)
for path in REVIEW.iterdir():
    if path.is_file() and path.name not in EXPECTED_REVIEW:
        assert path.read_bytes() == frozen(path.relative_to(ROOT).as_posix()), path.name
changes = subprocess.check_output(['git', 'diff', BASE, '--name-only', '-z'], cwd=ROOT).decode('utf-8').split('\0')
allowed = {'skill-candidate/' + NEW, *[REVIEW.relative_to(ROOT).as_posix() + '/' + name for name in EXPECTED_REVIEW]}
assert all(path in allowed or path.startswith(OUT.relative_to(ROOT).as_posix() + '/') for path in changes if path)
assert not subprocess.check_output(['git', 'diff', BASE, '--', 'effect-test',
    'analysis/introduction-learning-2026-10-05', 'analysis/introduction-candidate-update-2026-10-05'], cwd=ROOT)
author_hashes = {}
for name in ('核心要求.txt', '我自己的经验和做法.txt', '引言写作方法.txt'):
    assert (ROOT / name).read_text(encoding='utf-8').splitlines() == frozen(name).decode('utf-8').splitlines()
    author_hashes[name] = sha((ROOT / name).read_bytes())

result = {'base_commit': BASE, 'scope': 'candidate integrity and explicit file-read audit only',
          'candidate_changed_files': candidate_changes,
          'candidate_files_preserved': len(all_paths)-1,
          'source_checks': source_checks, 'quotes': quote_records,
          'sentence_tables': sentence_tables, 'on_demand_subsection_read_evidence': subselection,
          'report_contiguous_quotes': report_quotes,
          'author_input_hashes': author_hashes, 'read_routes': routes,
          'powershell_UTF8_reads': powershell_reads, 'package_validation': validation,
          'required_analysis_or_PDF_dependencies': False,
          'historical_evidence_records_preserved': True,
          'installation_or_model_or_effect_test_run': False,
          'limit': 'Explicit file reads do not prove autonomous routing, example use, writing quality, transfer, omission detection or stability.',
          'current_files_sha256': {p.relative_to(ROOT).as_posix(): sha(p.read_bytes()) for p in
                                  [CANDIDATE / NEW, *[REVIEW / name for name in sorted(EXPECTED_REVIEW)], OUT / 'check_update.py']}}
(OUT / 'implementation-check.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'verbatim_quote_units': len(quote_records), 'read_routes': len(routes),
                  'candidate_changed_files': candidate_changes, 'packages_valid': len(validation),
                  'effect_tests_run': False}, ensure_ascii=False))
