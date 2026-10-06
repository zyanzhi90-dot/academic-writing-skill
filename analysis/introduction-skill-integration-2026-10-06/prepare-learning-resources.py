"""Package accepted positive Introduction learning without audit dependencies."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
CORE = ROOT / 'skill-candidate/nature-shared/core'
AUDIT = OUT / 'audit'
AUDIT.mkdir(exist_ok=True)
BASE = '177d720dcae4131f653c9dee3194e781f824946c'
sha = lambda b: hashlib.sha256(b).hexdigest()
old = subprocess.check_output(['git', 'show', BASE+':skill-candidate/nature-shared/core/robotics-introduction-examples.md'], cwd=ROOT)
(AUDIT/'previous-robotics-introduction-examples.md').write_bytes(old)
specs = {
    'section': ('analysis/introduction-section-learning-draft-2026-10-06/learning-draft.md',
                'robotics-introduction-section.md',
                ['field-value','paragraph-tasks','prior-capability','design-role','design-connection','contributions']),
    'paragraph': ('analysis/introduction-paragraph-learning-2026-10-06/learning-draft.md',
                  'robotics-introduction-paragraphs.md',
                  ['p17-i01','eso-i01','p05-i02','p17-i04','fuzzy-i02','fuzzy-i03','p17-i05','p17-i07','p17-i08']),
    'expression': ('analysis/introduction-expression-learning-2026-10-06/learning-draft.md',
                   'robotics-introduction-expression.md', None),
}
records = []
for level, (src, dest, anchors) in specs.items():
    p = ROOT/src
    raw = p.read_text(encoding='utf-8')
    text = raw
    if level == 'section':
        text = text.replace('出版原文与逐句适配对应保留在[来源审计](../introduction-default-learning-cleanup-2026-10-06/audit/adaptation-map.json)中。',
                            '页码、I／C 编号和示例标记共同说明英文的来源与适配身份。')
    elif level == 'paragraph':
        text = text.replace('完整出版原文与逐句对应保留在[来源审计](../introduction-default-learning-cleanup-2026-10-06/audit/adaptation-map.json)中。',
                            '页码与 I／C 编号定位来源，A 编号定位当前示例句。')
    else:
        text = text.replace('../introduction-section-learning-draft-2026-10-06/learning-draft.md','robotics-introduction-section.md')
        text = text.replace('../introduction-paragraph-learning-2026-10-06/learning-draft.md','robotics-introduction-paragraphs.md')
        text = text.replace('逐句对应及完整出版原文保留在[来源审计](../introduction-default-learning-cleanup-2026-10-06/audit/adaptation-map.json)中。',
                            '页码与 I／C 编号定位来源。')
        text = text.replace('来源差异及选取审计另存于 [audit/](audit/preference-repair-record.md)。','')
    # Bibliographic locators remain; publication/audit lookup is outside runtime.
    text = re.sub(r'; \[来源审计定位\]\([^)]+\)', '', text)
    text = re.sub(r'；\[来源审计定位\]\([^)]+\)', '', text)
    text = re.sub(r'\[([^\]]+)\]\(\.\./introduction-section-review-2026-10-06/[^)]+\)', r'\1', text)
    if level == 'expression':
        text = re.sub(r'(?=^### (E\d+)｜)', lambda m: '<a id="'+m[1].lower()+'"></a>\n\n', text, flags=re.M)
    else:
        it = iter(anchors)
        pattern = r'(?=^## \d+\.)' if level == 'section' else r'(?=^### \d+\.\d+ )'
        text = re.sub(pattern, lambda m: '<a id="'+next(it)+'"></a>\n\n', text, flags=re.M)
        assert next(it, None) is None
    assert re.findall(r'^> (.*)$',raw,re.M) == re.findall(r'^> (.*)$',text,re.M)
    assert 'analysis/' not in text and '../introduction-' not in text
    target = CORE/dest
    target.write_text(text,encoding='utf-8')
    records.append({'level':level,'accepted_source':src,'accepted_source_sha256':sha(p.read_bytes()),
                    'runtime_path':target.relative_to(ROOT).as_posix(),'runtime_sha256':sha(target.read_bytes()),
                    'english_blocks':len(re.findall(r'^> ',text,re.M)),
                    'all_english_blocks_preserved_exactly':True,
                    'changes':'Local learning links, stable retrieval anchors, audit lookup separation only.'})
(AUDIT/'learning-resource-provenance.json').write_text(json.dumps({
    'baseline':BASE,'previous_runtime_reference_sha256':sha(old),'resources':records,
    'publication_and_adaptation_audit':'analysis/introduction-default-learning-cleanup-2026-10-06/audit/adaptation-map.json',
    'publication_audit_is_not_a_runtime_dependency':True,
},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'resources':len(records),'english_blocks':sum(r['english_blocks'] for r in records)}))
