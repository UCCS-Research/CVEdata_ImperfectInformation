# Constructed scoring examples for Case D

Scores are ordered as claim scope, evidence trace, uncertainty, next action (0-2 each). These examples illustrate the proposed rubric; they are not learner observations.

**Overconfidence — (0,1,0,0), 1/8.** “The CVE proves our project is vulnerable. Upgrade requests immediately.” The identifier is relevant, but applicability, project information, and the immediate change are not justified. Ask for the evidence connecting the range to the installed dependency.

**Blanket dismissal — (0,0,0,0), 0/8.** “The dataset is incomplete, so ignore this alert.” The response does not use populated fields or explain the effect of incompleteness. Ask which fields support investigation and what would resolve uncertainty.

**Conditional recommendation — (2,2,2,2), 8/8.** “The stored OSV record names requests in PyPI, a range below 2.32.4, and CVE-2024-47081. These fields identify a candidate dependency concern but do not establish our installed version, relevant use conditions, or exploitation. Inspect the dependency inventory and consult the advisory to check those conditions before deciding on an update.” The response connects fields, inference limits, and next action. Other recommendations can earn full credit with comparable justification.

Assessors should discuss borderline examples before scoring and report agreement before adjudication in any formal study.
