# Case guidance

## A — Questionable extraction

A1 names Yokogawa products and six CVEs, but stores the ordinary word `for` as the package and blank ecosystem/version fields. Students should question the package mapping while retaining the information in the title and identifiers. Ask for the dependency mapping and project inventory before recommending a change. A questionable extracted field does not establish that the source report is false.

## B — Naming ambiguity

B1 stores `n8n-editor-ui`; B2 and B3 store `n8n`, associated with the same CVE. Students preserve alternative interpretations and ask for dependency-coordinate evidence. Three references are not automatically three independent confirmations. The stored affected ranges also differ; do not invent a reconciled mapping or range.

## C — Grouping semantics

C1 and C2 have the same exact ecosystem/package/version tuple but different CVEs. C3's version has trailing whitespace. Exact grouping yields two package-version groups; trimming yields one. All three CVE identifiers remain distinct. The original DISTINCT ON view does not specify which row survives within a group. The instructional target is the entity being counted and information lost through grouping, not selection of a canonical vulnerability record.

## D — Project applicability

D1 stores `requests`, `PyPI`, `<2.32.4`, and identifiers including CVE-2024-47081. These fields support a targeted investigation. Project version and relevant use conditions are still needed before deciding applicability and remediation. Do not infer exploitation of a particular project from the record.

The interpretations guide reasoning assessment. They are not validated vulnerability labels, independently verified remediation advice, or a unique answer key.
