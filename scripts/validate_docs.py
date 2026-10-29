"""Validate local references and example requests; no network requests."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1]
errors=[]
tools={t['name']:t for t in json.loads((R/'reference/tools-2026-10-30.json').read_text(encoding='utf-8-sig'))['tools']}
for path in R.rglob('*.md'):
    text=path.read_text(encoding='utf-8-sig')
    if not text.startswith('# '):errors.append(f'{path.relative_to(R)}: missing title')
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text):
        if not target.startswith(('https://','http://','#','mailto:')):
            local=target.split('#',1)[0]
            if local and not (path.parent/local).exists(): errors.append(f'{path.relative_to(R)}: missing {local}')
    if re.search(r'(REPLACE_WITH|YOUR_API_KEY|TODO:)',text):errors.append(f'{path.relative_to(R)}: unfinished placeholder')
mapping={'search-london':'search_cities','methods':'list_calculation_methods','prayer-london':'get_prayer_times','compare-london':'compare_prayer_methods','timezone-new-york':'convert_timezone','timetable-london':'generate_timetable'}
for label,name in mapping.items():
    p=R/'examples'/f'{label}.json'
    if not p.exists():errors.append(f'missing example {label}');continue
    args=json.loads(p.read_text(encoding='utf-8-sig'));schema=tools[name]['inputSchema'];props=schema.get('properties',{})
    for k in schema.get('required',[]):
        if k not in args:errors.append(f'{label}: missing {k}')
    for k,v in args.items():
        if k not in props:errors.append(f'{label}: unknown field {k}');continue
        spec=props[k]
        if 'enum'in spec and v not in spec['enum']:errors.append(f'{label}: invalid {k}')
        if isinstance(v,int) and not isinstance(v,bool):
            if v<spec.get('minimum',v)or v>spec.get('maximum',v):errors.append(f'{label}: out of bounds {k}')
print(json.dumps({'local_check_only':True,'markdown_files':len(list(R.rglob('*.md'))),'examples':len(mapping),'errors':errors},ensure_ascii=True))
raise SystemExit(bool(errors))
