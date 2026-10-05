"""Record actual returned Introduction cards and execution messages, without quality inference."""
from pathlib import Path
import json
import re

record = Path(__file__).resolve().parent
summary = {}
for stage in ('drafting','polishing'):
    dest = record/stage
    loading = json.loads((dest/'loading-and-retention.json').read_text(encoding='utf-8'))
    exact = loading['actual_numbered_returns']
    cards = {}
    name = 'skill-candidate/nature-shared/core/robotics-introduction-examples.md'
    lines = (dest/'materials'/name).read_text(encoding='utf-8').splitlines()
    seen = set(exact.get(name,{}).get('matching_numbered_lines',[]))
    starts = [(i,s) for i,s in enumerate(lines,1) if re.fullmatch(r'## B\d+',s)]
    for k,(start,title) in enumerate(starts):
        end = starts[k+1][0]-1 if k+1<len(starts) else len(lines)
        returned = sorted(seen.intersection(range(start,end+1)))
        cards[title[3:]] = {'range':[start,end], 'returned_numbered_lines':returned,
            'any_returned':bool(returned),
            'all_nonempty_lines_returned_exactly':all(i in seen for i in range(start,end+1) if lines[i-1])}
    index = 'skill-candidate/nature-shared/core/robotics-writing-examples.md'
    common = (dest/'materials'/index).read_text(encoding='utf-8').splitlines()
    end = next(i-1 for i,s in enumerate(common,1) if s=='## 摘要')
    index_seen = set(exact.get(index,{}).get('matching_numbered_lines',[]))
    events = [json.loads(s) for s in (dest/'events.jsonl').read_text(encoding='utf-8').splitlines()]
    messages = [{'id':e['item'].get('id'),'text':e['item']['text']}
                for e in events if e.get('type')=='item.completed' and e.get('item',{}).get('type')=='agent_message']
    note = dest/'execution-agent-messages.json'
    assert not note.exists()
    note.write_text(json.dumps(messages,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    selection_end = starts[0][0]-1
    summary[stage] = {
        'core_full_actual_returns':loading['core_full_return_status'],
        'matching_fragments_actual_returns':{k:v['all_nonempty_lines_returned_exactly'] for k,v in exact.items() if '/static/fragments/' in k},
        'robotics_common_and_task_index':{'range':[1,end], 'all_nonempty_lines_returned_exactly':all(i in index_seen for i in range(1,end+1) if common[i-1])},
        'introduction_selection':{'range':[1,selection_end], 'all_nonempty_lines_returned_exactly':all(i in seen for i in range(1,selection_end+1) if lines[i-1])},
        'introduction_cards_actual_returns':cards,
        'other_robotics_cards':loading['selected_cards'],
        'additional_source_text_actual_returns':{k:v for k,v in exact.items() if not k.startswith(('inputs/','skill-candidate/'))},
        'execution_messages_file':note.relative_to(record).as_posix(),
        'limit':'Actual returns establish source access; they do not prove internal checks, attention or correct adaptation. Raw events preserve non-numbered and partial returns.'}
target = record/'loading-summary.json'
assert not target.exists()
target.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({s:{'Introduction_cards':{k:v['all_nonempty_lines_returned_exactly'] for k,v in d['introduction_cards_actual_returns'].items()}, 'other_cards':list(d['other_robotics_cards'])} for s,d in summary.items()},ensure_ascii=False))
