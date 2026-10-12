# Constructed scoring examples for Case D

Scores are ordered as claim scope, evidence trace, uncertainty, next action (0-2 each). These examples illustrate the proposed rubric; they are not learner observations.

**Overconfidence — (0,1,0,0), 1/8.** “The CVE proves requests will make our service vulnerable. Reject it.” The identifier is relevant, but the response assumes applicability and does not justify rejection. Ask which proposed version and use conditions connect the report to the service.

**Blanket dismissal — (0,0,0,0), 0/8.** “The dataset is incomplete, so ignore this alert.” The response does not use populated fields or explain the effect of incompleteness. Ask which fields support investigation and what would resolve uncertainty.

**Conditional recommendation — (2,2,2,2), 8/8.** “The OSV record names requests in PyPI, a range below 2.32.4, and CVE-2024-47081. Our team has not selected a version or credential configuration. Defer adoption until we select a candidate version and check the advisory's affected range and netrc conditions against the planned use. Resolving this report would not establish the absence of other risks.” The response connects fields to a specific verification step and bounds its conclusion. Other recommendations can earn full credit with comparable reasoning.

Assessors should discuss borderline examples before scoring and report agreement before adjudication in any formal study.
