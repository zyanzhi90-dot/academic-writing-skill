"""Summarize exact returned ranges, keeping source access separate from quality claims."""
from pathlib import Path
import json

record=Path(__file__).resolve().parent
out={}
for stage in ('drafting','polishing'):
    dest=record/stage
    loading=json.loads((dest/'loading-and-retention.json').read_text(encoding='utf-8'))
    exact=loading['actual_numbered_returns']
    fragments={k:v['all_nonempty_lines_returned_exactly'] for k,v in exact.items() if '/static/fragments/' in k}
    name='skill-candidate/nature-shared/core/robotics-writing-examples.md'
    lines=(dest/'materials'/name).read_text(encoding='utf-8').splitlines()
    common_end=next(i-1 for i,s in enumerate(lines,1) if s=='## 摘要')
    seen=set(exact[name]['matching_numbered_lines'])
    common=all(i in seen for i in range(1,common_end+1) if lines[i-1])
    assert common and all(fragments.values())
    source_reads={k:v for k,v in exact.items() if not k.startswith(('inputs/','skill-candidate/'))}
    out[stage]={'matching_fragments_full_actual_returns':fragments,
                'robotics_common_and_task_index':{'range':[1,common_end],'all_nonempty_lines_returned_exactly':common},
                'selected_cards':loading['selected_cards'],'additional_source_text_actual_returns':source_reads,
                'additional_original_source_text_reads_observed':bool(source_reads),
                'limit':'Complete declared corpus availability is not proof of reading every PDF or of following every instruction. Cards carry original English excerpts, analysis and conditions; partial source returns remain partial.'}
target=record/'loading-summary.json'
assert not target.exists()
target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({s:{'common_full':v['robotics_common_and_task_index']['all_nonempty_lines_returned_exactly'],
    'cards':list(v['selected_cards']),'additional_sources':list(v['additional_source_text_actual_returns'])} for s,v in out.items()},ensure_ascii=False))
