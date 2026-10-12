"""Reproduce source statistics; never modifies the database."""
import hashlib,json,sys
from pathlib import Path
import duckdb
p=Path(sys.argv[1]);c=duckdb.connect(str(p),read_only=True)
r=c.execute("SELECT count(*),sum(CASE WHEN compromised_package IS NULL OR trim(compromised_package)='' THEN 1 ELSE 0 END),sum(CASE WHEN ecosystem IS NULL OR trim(ecosystem)='' THEN 1 ELSE 0 END),min(date_scraped),max(date_scraped) FROM oss_threats").fetchone()
with p.open('rb') as f: digest=hashlib.file_digest(f,'sha256').hexdigest()
print(json.dumps(dict(zip(['source_record_count','missing_package_count','missing_ecosystem_count','scrape_timestamp_min','scrape_timestamp_max'],r))|{'source_sha256':digest},default=str,indent=2))
