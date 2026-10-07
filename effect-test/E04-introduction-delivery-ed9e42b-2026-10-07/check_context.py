"""Audit actual task boundaries, including A cards missed by the earlier B-only audit."""
from pathlib import Path
import json
import re

record=Path(__file__).resolve().parent
result={}
for stage in ('drafting','polishing'):
 dest=record/stage
 loading=json.loads((dest/'loading-and-retention.json').read_text(encoding='utf-8'))
 paths=loading['actual_numbered_returns']
 events=[json.loads(s) for s in (dest/'events.jsonl').read_text(encoding='utf-8').splitlines()]
 forbidden=('intro-general.md','references/introduction.md','references/examples/introduction',
            'nature-introduction.md','references/article-architecture.md',
            'references/published-article-patterns.md','references/section-moves.md')
 generic_paths=[p for p in paths if any(f in p for f in forbidden)]
 signatures=('define a task abstractly, then show its applications',
             'lead with the unsolved difficulty',
             'Tell the user which variant you picked and why.',
             'The final paragraph states the contribution and approach, not the numbers.',
             'Do not summarize the Results section here.',
             'Explain concrete implementation steps',
             "Assume the target journal's readers understand the broad field's")
 hits=[]
 for event in events:
  item=event.get('item',{})
  if event.get('type')!='item.completed' or item.get('type')!='command_execution':continue
  for signature in signatures:
   if signature in item.get('aggregated_output',''):hits.append({'command_id':item['id'],'directive':signature})
 name='skill-candidate/nature-shared/core/robotics-writing-examples.md'
 lines=(dest/'materials'/name).read_text(encoding='utf-8').splitlines()
 seen=set(paths.get(name,{}).get('matching_numbered_lines',[]))
 cards=[]
 content_returns=[]
 for event in events:
  item=event.get('item',{})
  if event.get('type')!='item.completed' or item.get('type')!='command_execution':continue
  output=item.get('aggregated_output','')
  for n,line in enumerate(lines,1):
   if line.startswith('> ') and len(line)>80 and line[2:] in output:
    content_returns.append({'command_id':item['id'],'source_line':n})
 for n,line in enumerate(lines,1):
  match=re.match(r'^### ([AB]\d+)\b',line)
  if not match:continue
  end=next((i-1 for i in range(n+1,len(lines)+1) if lines[i-1].startswith(('### ','## '))),len(lines))
  english=[i for i in range(n,end+1) if lines[i-1].startswith('> ')]
  actual=sorted(seen.intersection(english))
  if actual:cards.append({'card':match[1],'range':[n,end],'raw_English_lines_returned':actual})
 role='nature-writing' if stage=='drafting' else 'nature-polishing'
 intro='skill-candidate/'+role+'/static/fragments/section/intro.md'
 hub='skill-candidate/nature-shared/core/robotics-introduction-examples.md'
 result[stage]={
  'generic_conflicting_paths_actually_read':generic_paths,'generic_conflicting_directives_returned':hits,
  'generic_isolation_preserved':not generic_paths and not hits,
  'monolithic_other_section_index_actually_read':name in paths,
  'other_section_raw_English_cards_returned':cards,
  'other_section_raw_English_detected_in_command_content':content_returns,
  'Introduction_only_reading_boundary_respected':name not in paths and not cards and not content_returns,
  'domain_fragment_full_actual_return':paths.get(intro,{}).get('all_nonempty_lines_returned_exactly',False),
  'dedicated_index_full_actual_return':paths.get(hub,{}).get('all_nonempty_lines_returned_exactly',False),
  'limit':'Actual numbered returns and explicit read paths; no inference about hidden checks or a causal link between old card co-loading and expression failures.'}
out=record/'context-evidence.json'
assert not out.exists()
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({s:{k:v[k] for k in ('generic_isolation_preserved','Introduction_only_reading_boundary_respected')} for s,v in result.items()}))
