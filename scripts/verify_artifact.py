"""Verify the released teaching artifact without external dependencies."""
import csv,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
rows=json.loads((root/'data/cases.json').read_text())
assert [r['record_id'] for r in rows]==['A1','B1','B2','B3','C1','C2','C3','D1']
assert len({r['threat_id'] for r in rows})==8
assert rows[0]['compromised_package']=='for'
assert rows[0]['ecosystem']==rows[0]['compromised_version']==''
assert {r['compromised_package'] for r in rows if r['case_id']=='B'}=={'n8n','n8n-editor-ui'}
c=[r for r in rows if r['case_id']=='C']
exact={(r['ecosystem'],r['compromised_package'],r['compromised_version']) for r in c}
trimmed={(r['ecosystem'].strip(),r['compromised_package'].strip(),r['compromised_version'].strip()) for r in c}
assert len(exact)==2 and len(trimmed)==1
assert len({r['identifiers'] for r in c})==3
assert c[2]['compromised_version']=='1.4.2 '
assert rows[-1]['compromised_version']=='<2.32.4'
assert all(r.get('description_snippet') for r in rows)
d_snippet=rows[-1]['description_snippet'].lower()
assert 'netrc' in d_snippet and 'url' in d_snippet and 'credential' in d_snippet
with (root/'data/cases.csv').open(newline='') as f: assert list(csv.DictReader(f))==rows
m=json.loads((root/'provenance/snapshot.json').read_text())
assert m['source_record_count']==977 and m['missing_package_count']==778 and m['missing_ecosystem_count']==836
print('Verified 8 teaching records; Case C: 2 exact groups, 1 trimmed group, 3 distinct CVEs.')

reserved=json.loads((root/'data/independent_records.json').read_text())
assert [r['record_id'] for r in reserved]==['T1','T2']
assert not {r['threat_id'] for r in rows} & {r['threat_id'] for r in reserved}
assert reserved[0]['compromised_package']=='is'
assert reserved[1]['compromised_package']=='langgraph' and reserved[1]['compromised_version']=='<4.0.0'
with (root/'data/independent_records.csv').open(newline='') as f:
    table=list(csv.DictReader(f))
assert table==[{k:'' if v is None else str(v) for k,v in r.items()} for r in reserved]
assert m['independent_record_count']==2
print('Verified two separate independent-practice records; nulls retained in JSON and blank in CSV.')
