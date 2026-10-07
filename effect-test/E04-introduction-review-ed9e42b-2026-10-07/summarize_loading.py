"""Available positive learning versus exact returned lines; no quality inference."""
from pathlib import Path
import hashlib
import json
import re

record = Path(__file__).resolve().parent
summary = {}
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
for stage in ('review',):
    dest = record/stage
    loading = json.loads((dest/'loading-and-retention.json').read_text(encoding='utf-8'))
    frozen = json.loads((dest/'frozen-run.json').read_text(encoding='utf-8'))
    exact = loading['actual_numbered_returns']
    resources = {}
    for filename in ('robotics-introduction-examples.md','robotics-introduction-section.md',
                     'robotics-introduction-paragraphs.md','robotics-introduction-expression.md'):
        name = 'skill-candidate/nature-shared/core/'+filename
        path = dest/'materials'/name
        lines = path.read_text(encoding='utf-8').splitlines()
        seen = set(exact.get(name,{}).get('matching_numbered_lines',[]))
        starts = [(n,re.fullmatch(r'<a id="([^"]+)"></a>',s)[1])
                  for n,s in enumerate(lines,1) if re.fullmatch(r'<a id="([^"]+)"></a>',s)]
        if not starts:
            starts = [(n,s[3:]) for n,s in enumerate(lines,1) if s.startswith('## ')]
        units = {}
        for k,(start,anchor) in enumerate(starts):
            end = starts[k+1][0]-1 if k+1<len(starts) else len(lines)
            heading = next((i for i in range(start,end+1) if lines[i-1].startswith(('## ','### '))),None)
            if heading is not None:
                level = len(re.match(r'#+',lines[heading-1])[0])
                next_group = next((i for i in range(heading+1,end+1)
                                   if re.match(r'^#{1,'+str(level)+r'} ',lines[i-1])),None)
                if next_group is not None:
                    end = next_group-1
            returned = sorted(seen.intersection(range(start,end+1)))
            english = [i for i in range(start,end+1) if lines[i-1].startswith('> ')]
            tables = [i for i in range(start,end+1) if lines[i-1].startswith('|')]
            title = next((s for s in lines[start-1:end] if s.startswith(('## ','### '))),anchor)
            units[anchor] = {'title':title,'range':[start,end],'available':True,
                'returned_numbered_lines':returned,
                'any_exact_numbered_return':bool(returned),
                'all_nonempty_lines_returned_exactly':all(i in seen for i in range(start,end+1) if lines[i-1]),
                'english_block_lines':english,'all_english_blocks_returned_exactly':bool(english) and all(i in seen for i in english),
                'analysis_table_lines':tables,'all_analysis_tables_returned_exactly':bool(tables) and all(i in seen for i in tables)}
        resources[filename] = {'available_sha256':sha(path),'frozen_git_sha256':frozen['candidate_sha256'][name],
            'file_line_count':len(lines),'file_all_nonempty_lines_returned_exactly':exact.get(name,{}).get('all_nonempty_lines_returned_exactly',False),
            'units':units}
    events = [json.loads(s) for s in (dest/'events.jsonl').read_text(encoding='utf-8').splitlines()]
    messages = [{'id':e['item'].get('id'),'text':e['item']['text']} for e in events
                if e.get('type')=='item.completed' and e.get('item',{}).get('type')=='agent_message']
    note = dest/'execution-agent-messages.json'
    content = json.dumps(messages,ensure_ascii=False,indent=2)+'\n'
    if note.exists():
        assert note.read_text(encoding='utf-8')==content
    else:
        note.write_text(content,encoding='utf-8')
    summary[stage] = {'core_full_actual_returns':loading['core_full_return_status'],
        'matching_fragments_actual_returns':{k:v['all_nonempty_lines_returned_exactly'] for k,v in exact.items() if '/static/fragments/' in k},
        'positive_Introduction_resources':resources,
        'other_robotics_cards':loading['selected_cards'],
        'additional_source_text_actual_returns':{k:v for k,v in exact.items() if not k.startswith(('inputs/','skill-candidate/'))},
        'execution_messages_file':note.relative_to(record).as_posix(),
        'limit':'Available, returned and adopted are distinct. Exact numbered matches prove returned lines only. Partial or non-numbered returns remain in raw events; manual prose evaluation is separate.'}
target = record/'loading-summary.json'
target.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({s:{n:sum(u['all_english_blocks_returned_exactly'] for u in r['units'].values())
                     for n,r in d['positive_Introduction_resources'].items()} for s,d in summary.items()},ensure_ascii=False))
