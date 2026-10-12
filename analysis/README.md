# Reproduction

`original_unique_view.sql` is the original stored view definition. `python3 scripts/verify_artifact.py` demonstrates exact versus whitespace-trimmed grouping of the three Case C records and verifies the released cases.

To reproduce the aggregate snapshot counts, install the dependency in `requirements.txt` and run `python3 scripts/reproduce_snapshot.py /path/to/threat_intel_phd.duckdb`. This opens the original database read-only and reports the file hash, record count, missingness, and date range. The original database is not included. `provenance/snapshot.json` records the source hash and aggregate counts used in the paper. Do not apply these counts to the teaching subset or interpret them as source-service defect rates.
