"""Prepare student-only files and a separate independent-practice packet."""
from pathlib import Path
import argparse,shutil

parser=argparse.ArgumentParser()
parser.add_argument('destination',type=Path)
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
dest=args.destination.resolve()
dest.mkdir(parents=True,exist_ok=True)
groups={
    'instruction':['data/cases.json','data/cases.csv','student/activity.md','student/decision_memo.md','student/decision_briefs.md','student/glossary.md','analysis/original_unique_view.sql'],
    'independent':['data/independent_records.json','data/independent_records.csv','student/independent_tasks.md'],
}
for group,files in groups.items():
    for name in files:
        target=dest/group/name
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(root/name,target)
print('Prepared instruction and independent packets; no instructor files copied.')
