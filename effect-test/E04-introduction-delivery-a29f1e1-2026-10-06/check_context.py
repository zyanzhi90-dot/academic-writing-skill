"""Record actual context isolation, without assigning a prose quality verdict."""
from pathlib import Path
import hashlib
import json
import re

record=Path(__file__).resolve().parent
result={}
for stage in ('drafting','polishing'):
    dest=record/stage
    loading=json.loads((dest/'loading-and-retention.json').read_text(encoding='utf-8'))
    events=[json.loads(line) for line in (dest/'events.jsonl').read_text(encoding='utf-8').splitlines()]
    forbidden=('intro-general.md','references/introduction.md','references/examples/introduction',
               'nature-introduction.md','references/article-architecture.md',
               'references/published-article-patterns.md','references/section-moves.md')
    paths=loading['actual_numbered_returns']
    conflicts=[p for p in paths if any(f in p for f in forbidden)]
    # These are the actual conflicting directives, not declarations of another path's scope.
    signatures=('define a task abstractly, then show its applications',
                'lead with the unsolved difficulty',
                'Tell the user which variant you picked and why.',
                'The final paragraph states the contribution and approach, not the numbers.',
                'Do not summarize the Results section here.',
                'Explain concrete implementation steps',
                'Assume the target journal\'s readers understand the broad field\'s')
    hits=[]
    for event in events:
        item=event.get('item',{})
        if event.get('type')!='item.completed' or item.get('type')!='command_execution':continue
        output=item.get('aggregated_output','')
        for signature in signatures:
            if signature in output:hits.append({'command_id':item['id'],'directive':signature})
    intro='skill-candidate/'+('nature-writing' if stage=='drafting' else 'nature-polishing')+'/static/fragments/section/intro.md'
    result[stage]={
        'conflicting_generic_paths_actually_read':conflicts,
        'conflicting_generic_directives_actually_returned':hits,
        'domain_fragment_full_actual_return':paths.get(intro,{}).get('all_nonempty_lines_returned_exactly',False),
        'generic_isolated_from_actual_context':not conflicts and not hits,
        'retained_compatible_guidance':'Scientific capabilities, conditions, design transitions, paragraph-group relationships and evidence boundaries remain in the returned domain fragment.',
        'author_override':'Original introduction-method file and latest explicit adjustment supplied unchanged, with adjustment priority; no new experiment exclusion rule.',
        'limit':'Explicit paths and returned commands, not hidden reasoning. Context isolation is implementation evidence, not autonomous writing success.'}
out=record/'context-evidence.json'
assert not out.exists()
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({s:v['generic_isolated_from_actual_context'] for s,v in result.items()}))
