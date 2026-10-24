# Case guidance

## A — Questionable extraction

A1 names Yokogawa products and six CVEs, but stores the ordinary word `for` as the package and blank ecosystem/version fields. Students should question the package mapping while retaining the information in the title and identifiers. Ask for the dependency mapping and project inventory before recommending a change. A questionable extracted field does not establish that the source report is false.

## B — Naming ambiguity

B1 stores `n8n-editor-ui`; B2 and B3 store `n8n`, associated with the same CVE. Students preserve alternative interpretations and ask for dependency-coordinate evidence. If students consult credible live sources that identify the affected package, accept that supported resolution; do not require them to retain uncertainty after the relevant evidence is available. They must still establish whether the report applies to the proposed deployment. Three references are not automatically three independent confirmations. The stored affected ranges also differ; do not invent a reconciled mapping or range.

## C — Grouping semantics

C1 and C2 have the same exact ecosystem/package/version tuple but different CVEs. C3's version has trailing whitespace. Exact grouping yields two package-version groups; trimming yields one. All three CVE identifiers remain distinct. The original DISTINCT ON view does not specify which row survives within a group. The instructional target is the entity being counted and information lost through grouping, not selection of a canonical vulnerability record.

## D — Project applicability

D1 stores `requests`, `PyPI`, `<2.32.4`, and identifiers including CVE-2024-47081. These fields support a targeted investigation. Project version and relevant use conditions are still needed before deciding applicability and remediation. Do not infer exploitation of a particular project from the record.

The interpretations guide reasoning assessment. They are not validated vulnerability labels, independently verified remediation advice, or a unique answer key.

## Decision contexts and D+
See `student/decision_briefs.md`. For C, retain distinct CVE references for applicability review rather than treating one grouped row as one vulnerability or a complete assessment. For D+, accept resolution of a specific concern of the stipulated range-based concern; do not require another identity/version inquiry to earn full credit. These exercise assumptions do not alter the snapshot.

## Reserved independent tasks
T1: the title and CVE identify a report about Apple macOS ImageIO, but `is` is questionable extracted package metadata. Request source-to-component mapping and project inventory before a dependency change; do not discard the source report. T2: the stored record names `langgraph`, `PyPi`, and `<4.0.0`, but those extracted fields need checking. The current advisory for CVE-2026-27794 identifies `langgraph-checkpoint` as the distribution affected below 4.0.0. Confirm the report-to-dependency mapping and that dependency's version before applying the range; do not transfer the boundary to the version of `langgraph`. Relevant conditions include enabled caching, a node caching policy, and attacker write access to the cache backend. Do not assume exploitation or certify versions outside that range. The maintainer advisory is https://github.com/langchain-ai/langgraph/security/advisories/GHSA-mhr3-j7m5-c7c9 (checked 23 October 2026). This guidance supplements the exercise; preserve the original snapshot fields. These guidance points are reasoning targets, not independently validated vulnerability findings.


## Stored records and live evidence

Use the fixed snapshot for the core exercise. If live sources are consulted, record the source and retrieval date, accept supported resolutions, and distinguish disagreement with an extracted field from demonstrated changes in the upstream report. Historical API payloads are not archived here, so a current disagreement alone does not establish when or why it arose.
