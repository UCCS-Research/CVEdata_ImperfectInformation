# Case data

`cases.json` preserves types and whitespace; `cases.csv` is a convenient tabular copy. Eight records form Cases A (one), B (three), C (three), and D (one). These are selected teaching examples, not a representative sample of the collection.

`case_id` and `record_id` are teaching locators. `threat_id` is the stored row key; `source_site`, `title`, `url`, `date_scraped`, `compromised_package`, `ecosystem`, `compromised_version`, `identifiers`, and `description_snippet` are original fields. The prefix `compromised_` is the original schema's name: it does not certify compromise. A blank is a stored blank, not a conclusion that no package/version exists. Timestamp timezone is not specified in the original values.

Keep `PyPi` as stored in Case C and the trailing space in C3's `1.4.2 `. Case D's exact range is `<2.32.4`. Do not trim, normalize, or merge records silently. Social-post content, workflow labels, and the full database are excluded; stored snippets are included. Source locators remain attached to each record.

Description snippets are exported unchanged from the snapshot and may be truncated or contain HTML/Markdown. They are stored text, not executable content or independently corroborating evidence. JSON preserves nulls; CSV represents nulls as blank cells.

`independent_records.json`/`.csv` contain T1/T2, two additional records reserved from modeled instruction. Instructor data notes should not be distributed as an answer key before assessment.
