# CVE Data and Imperfect Information

A teaching package for examining imperfect security records and justifying dependency decisions. Students connect a claim to evidence, explain relevant uncertainty, and recommend a next action. The package uses eight selected records from a fixed collection of 977 threat records collected from 12 March to 1 April 2026.

## Start here

- Students: [case data](data/README.md), [activity](student/activity.md), and [decision memo](student/decision_memo.md).
- Instructors: [session guide](instructor/session_guide.md), [case guidance](instructor/case_guidance.md), [rubric](instructor/rubric.csv), and [scoring examples](instructor/scoring_examples.md).
- Researchers: [snapshot provenance](provenance/snapshot.json), [analysis instructions](analysis/README.md), and [data dictionary](data/README.md).

## Verify the package

Run `python3 scripts/verify_artifact.py` from the repository root. It uses the standard library and checks the released records and the exact-versus-trimmed grouping example. No network, API key, scanner, or live advisory lookup is needed.

## Scope

The data are a teaching subset, not a vulnerability feed or a verified package-risk ranking. The original database is not distributed here. Aggregate counts describe that original snapshot; the eight-row subset cannot reproduce whole-database statistics. A read-only reproduction script is provided for users who already hold the original database. Instructor scoring examples are constructed examples, not student results.

Cases A-D cover questionable extraction, conflicting package references, grouping choices, and project applicability. The activity is designed for 50-75 minutes in an upper-level software engineering course. The instructor folder contains guidance students should consult only after completing their initial memos.

See [reuse and attribution](REUSE.md).
