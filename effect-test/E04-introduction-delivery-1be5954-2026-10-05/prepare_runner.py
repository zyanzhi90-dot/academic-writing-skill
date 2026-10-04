"""Reuse the accepted one-shot mechanism for a new section without changing the candidate."""
from pathlib import Path
import hashlib
import json
import re
import shutil
from html.parser import HTMLParser

class Metadata(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.values = {}
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta' and attrs.get('name','').startswith('citation_'):
            self.values.setdefault(attrs['name'], []).append(attrs.get('content',''))

record = Path(__file__).resolve().parent
root = record.parents[1]
prior = root / 'effect-test/E04-independent-delivery-1be5954-2026-10-04'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

for name, source in {
    'scientific-facts.md': prior/'scientific-facts.md',
    'accepted-abstract.en.txt': prior/'delivery/abstract.en.txt',
}.items():
    assert not (record/name).exists()
    shutil.copyfile(source, record/name)

entries = []
venues = {
    'R1': 'CoRL 2021; PMLR 164:1678–1690，2022 年出版。',
    'R2': 'NeurIPS 2022；arXiv:2206.11251。',
    'R3': 'CoRL 2021; PMLR 164:158–168，2022 年出版。',
    'R4': 'NeurIPS 2020；arXiv:2006.11239。',
    'R5': 'NeurIPS 2019；arXiv:1907.05600。',
    'R6': 'ICML 2022; PMLR 162:9902–9915。',
    'R7': 'arXiv:2208.06193；2022 年首次公开，RSS 2023 之前版本为 v2（2022-10-03）。',
    'R8': 'RSS 2023；arXiv:2304.02532，首次公开于 2023-04-05。',
    'R9': 'ICLR 2023；arXiv:2301.10677，2023 年首次公开。',
}
claims = {
    'R1':'B01：离线人类示范、历史模型与机器人操作；循环高斯混合基线的本文比较另见 S02。',
    'R2':'B02：动作聚类、连续偏移、多模态及时间上下文。',
    'R3':'B03：能量策略、负例对比训练、视觉高维和精密实机能力；B05 的波动是 E04 观察。',
    'R4':'B06：去噪扩散生成基础。',
    'R5':'B06：多噪声尺度得分学习与采样基础。',
    'R6':'B07：状态—动作轨迹扩散规划。',
    'R7':'B08：离线强化学习的条件扩散动作策略。',
    'R8':'B09：目标条件扩散模仿学习、采样及仿真验证。',
    'R9':'B09：多模态人类行为扩散模仿与仿真／游戏验证。',
}
retrieval = json.loads((record/'coordinator/citation-retrieval.json').read_text(encoding='utf-8'))
ledger = '# 引用身份与支持事实\n\nR 编号只标识文献，不规定引言顺序或要求全部引用。英文仅为文献题名与作者身份，不是目标论文原文或表达范例。引用的科学事实见 background-facts.md；按正文实际采用的事实选择引用。\n'
for rid in venues:
    p = record/'coordinator/citation-sources'/f'{rid}.html'
    meta = Metadata(p.read_text(encoding='utf-8')).values
    title = meta['citation_title'][0]
    authors = meta['citation_author']
    source = next(x['url'] for x in retrieval if x['id']==rid and x['path'].endswith('.html'))
    entries.append({'id':rid,'title':title,'authors':authors,'venue':venues[rid], 'url':source,'supports':claims[rid]})
    ledger += '\n## '+rid+'\n\n题名：'+title+'\n\n作者：'+'; '.join(authors)+'\n\n出版身份：'+venues[rid]+'\n\n来源：'+source+'\n\n支持：'+claims[rid]+'\n'
(record/'citation-facts.md').write_text(ledger,encoding='utf-8')
(record/'coordinator/citation-identities.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
identity = json.loads((prior/'coordinator/input-identity.json').read_text(encoding='utf-8'))
identity.update({
    'section':'Introduction', 'accepted_abstract_sha256':sha(record/'accepted-abstract.en.txt'),
    'facts_sha256':sha(record/'scientific-facts.md'), 'background_sha256':sha(record/'background-facts.md'),
    'citations_sha256':sha(record/'citation-facts.md'),
    'source_identity_record':str((prior/'coordinator/input-identity.json').relative_to(root)).replace('\\','/'),
    'source_identity_record_sha256':sha(prior/'coordinator/input-identity.json'),
    'task_sha256':{'drafting':sha(record/'drafting-task.md'),'polishing':sha(record/'polishing-task.md')},
})
(record/'coordinator/input-identity.json').write_text(json.dumps(identity,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
code = (prior/'execute_once.py').read_text(encoding='utf-8')
code = code.replace("    if role == 'nature-writing':\n        packages.append('skill-candidate/nature-polishing')\n",'')
code = code.replace("ROOT / 'effect-test/E02-delivery-repair-2026-10-04/drafting-frozen'", "ROOT / 'effect-test/E04-independent-delivery-1be5954-2026-10-04/drafting'")
code = code.replace("'task.md': RECORD / 'drafting-task.md',", "'task.md': RECORD / ('drafting-task.md' if draft is None else 'polishing-task.md'),\n        'background-facts.md': RECORD / 'background-facts.md',\n        'citation-facts.md': RECORD / 'citation-facts.md',\n        'accepted-abstract.en.txt': RECORD / 'accepted-abstract.en.txt',")
code = code.replace("        'abstract-writing-method.txt': ROOT / '摘要写作方法.txt',\n",'')
start = code.index("        (materials / 'inputs/task.md').write_text(")
end = code.index("    assert (materials / 'inputs/scientific-facts.md')",start)
code = code[:start]+code[end:]
code = code.replace("'core-requirements.txt', 'abstract-writing-method.txt'", "'core-requirements.txt', 'background-facts.md', 'citation-facts.md', 'accepted-abstract.en.txt'")
code = code.replace('Abstract-only task','Introduction-only task').replace('target original paper/abstract','target original paper/introduction')
code = code.replace('complete English abstract, accurate Chinese translation', 'complete English Introduction, accurate paragraph-by-paragraph Chinese translation, used references')
code = code.replace('timeout=1200','timeout=1800')
code = code.replace("'case': 'E04', 'materials_sha256'", "'case': 'E04', 'section': 'Introduction', 'materials_sha256'")
(record/'execute_once.py').write_text(code,encoding='utf-8')
verify = (prior/'verify_stage.py').read_text(encoding='utf-8').replace('(A\\d+)', '(B\\d+)')
verify = verify.replace('section/abstract.md','section/intro.md').replace('core/abstract-delivery.md','core/robotics-main-text.md')
(record/'verify_stage.py').write_text(verify,encoding='utf-8')
print('Prepared scientific inputs, citation identities, and reused runner; no model invoked.')
