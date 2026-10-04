"""Curate complete local Introductions after visual paragraph/column verification.

No model calls. Preserve lexical and grammatical source errors. Record each
normalization and each source block; never use page-block order as reading order.
"""
from pathlib import Path
import json
import re
import unicodedata

OUT = Path(__file__).resolve().parent
PROVENANCE = json.loads((OUT/'source-provenance.json').read_text(encoding='utf-8'))
BLOCKS = {k: json.loads((OUT/f'{k}-page-blocks.json').read_text(encoding='utf-8'))
          for k in ('P17','P05','Fuzzy2023','ESO2017')}
CHANGES = []
# Physical line-end breaks in these exact Introduction blocks, inspected in PDF.
# A source compound keeps its hyphen; a word broken by layout loses the hyphen.
KEEP_HYPHEN = {'spring-damper','brain-actuated','prescribed-time','fixed-time',
               'ESO-based','MIMO-ESO','error-integral','multiple-output','time-delay'}

def block(key, page, bid):
    return next(b['text'] for b in BLOCKS[key][page-1]['blocks'] if b['id']==bid)

def normalize(key, unit, raw):
    text = unicodedata.normalize('NFKC', raw)
    def join(m):
        a, b = m.group(1),m.group(2)
        kept = f'{a}-{b}' in KEEP_HYPHEN
        result = f'{a}-{b}' if kept else a+b
        CHANGES.append({'paper':key,'unit':unit,'source':m.group(0),'normalized':result,
                        'operation':'retain compound hyphen' if kept else 'remove layout word break'})
        return result
    text = re.sub(r'([A-Za-z]+)-\n([A-Za-z]+)',join,text)
    return re.sub(r'\s+',' ',text).strip()

UNITS = {
 'P17': [
    ('I01',[(1,8),(1,16)],'Recently', 'R'),
    ('I02',[(1,17)],'The dynamic', ''),
    ('I03',[(1,18)],'DMPs', ''),
    ('I04',[(1,19),(2,2)],'Probabilistic', ''),
    ('I05',[(2,3)],'To take', ''),
    ('I06',[(2,4),(2,5)],'The imitation', ''),
    ('I07',[(2,6)],'In this paper', ''),
    ('I08',[(2,7)],'Here', ''),
    ('I09',[(2,8)],'The remainder', ''),
 ],
 'P05': [
    ('I01',[(1,8),(1,15)],'Recently', 'R'),
    ('I02',[(1,16)],'An adaptive', ''),
    ('I03',[(1,17)],'In this respect', ''),
    ('I04',[(1,18),(2,1)],'The dynamic', ''),
    ('I05',[(2,2)],'A fuzzy', ''),
    ('I06',[(2,3)],'In our recent', ''),
    ('I07',[(2,4),(2,6)],'The work', ''),
    ('I08',[(2,7)],'The objective', ''),
 ],
 'Fuzzy2023': [
    ('I01',[(1,7),(1,13)],'For', 'F'),
    ('I02',[(1,14)],'In practice', ''),
    ('I03',[(1,15),(2,1)],'In many', ''),
    ('I04',[(2,2)],'Motivated', ''),
 ],
 'ESO2017': [
    ('I01',[(1,10),(1,17)],'Underwater', 'U'),
    ('I02',[(1,18)],'In practice', ''),
    ('I03',[(1,19)],'Several', ''),
    ('I04',[(2,1)],'Although', ''),
    ('I05',[(2,2)],'As an', ''),
    ('I06',[(2,3)],'Another', ''),
    ('I07',[(2,4)],'In this', ''),
    ('I08',[(2,5)],'In this', ''),
 ],
}

def make_unit(key, name, refs, prefix='', raw_override=None):
    raw = raw_override if raw_override is not None else '\n'.join(block(key,p,b) for p,b in refs)
    text = normalize(key,name,prefix+raw)
    return {'id':name,'blocks':[f'p{p}-b{b}' for p,b in refs], 'text':text}

curated = {}
for key, spec in UNITS.items():
    units=[]
    for name, refs, expected, prefix in spec:
        item=make_unit(key,name,refs,prefix)
        assert item['text'].lower().startswith(expected.lower()), (key,name,item['text'][:100])
        units.append(item)
    if key=='P05':
        text=block(key,2,8)
        contributions,roadmap=text.split('In the following sections,',1)
        for n in range(1,4):
            part=re.split(r'(?=\d\))',contributions)[n]
            units.append(make_unit(key,f'C{n:02d}',[(2,8)],raw_override=part))
        units.append(make_unit(key,'I09',[(2,8)],raw_override='In the following sections,'+roadmap))
    elif key=='Fuzzy2023':
        contributions=block(key,2,3)
        for n in range(1,4):
            part=re.split(r'(?=\d\))',contributions)[n]
            units.append(make_unit(key,f'C{n:02d}',[(2,3)],raw_override=part))
    elif key=='ESO2017':
        units.append(make_unit(key,'C01',[(2,6)]))
        text=block(key,3,2)
        contributions,roadmap=text.split('The remainder of this paper',1)
        for n, part in enumerate(re.split(r'(?=\d\))',contributions)[1:],2):
            units.append(make_unit(key,f'C{n:02d}',[(3,2)],raw_override=part))
        units.append(make_unit(key,'I09',[(3,2)],raw_override='The remainder of this paper'+roadmap))
    curated[key]=units
    src=PROVENANCE[key]
    pdf='../../'+src['pdf']
    printed={'P17':'777–778','P05':'1010–1011','Fuzzy2023':'1041–1042','ESO2017':'6785–6787'}[key]
    lines=[f'# {key} — Introduction 原文核验副本','',
           f"来源：[{Path(src['pdf']).name}](<{pdf}>)；§I，PDF p.1–{3 if key=='ESO2017' else 2}，印刷页 {printed}。",'',
           f"PDF SHA-256：`{src['pdf_sha256']}`。",'',
           '本文件完整保留 Introduction，止于 §II 标题之前；摘要、作者脚注、图注和下一节不计入引言。I 为实际 prose 段落，C 为贡献条目；同一段跨栏／跨页时合并。编号是本轮定位号，不是论文原有编号。', '',
           '仅规范排版：NFKC 连字、行末断词、空白及首字下沉重接；原有词汇、语法、引用编号和句末标点不改。具体断词见 normalization-log.json。页面块与渲染图用于复核段落边界。', '',
           '这些英文是所提供本地论文的原文证据，不是作者新稿，也不是建议逐字继承的科学断言。', '']
    for item in units:
        lines += [f"## {item['id']} — {', '.join(item['blocks'])}", '', '> '+item['text'], '']
    (OUT/f'{key}-introduction.md').write_text('\n'.join(lines),encoding='utf-8')
(OUT/'curated-introductions.json').write_text(json.dumps(curated,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(OUT/'normalization-log.json').write_text(json.dumps(CHANGES,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Curated units:', ', '.join(f'{k}={len(v)}' for k,v in curated.items()))
