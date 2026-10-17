# Constructed scoring examples

These are invented responses, not learner observations. Scores are claim scope, evidence trace, uncertainty, next action (0-2 each).

**Overconfidence on D (0,1,0,0; 1/8).** "The CVE proves requests will make our service vulnerable. Reject it." The identifier is relevant, but applicability and rejection are unsupported.

**Blanket dismissal on D (0,0,0,0; 0/8).** "The dataset is incomplete, so ignore this alert." The response does not use available evidence or explain the relevance of missing information.

**Generic caution on D (2,1,1,1; 5/8).** "The record reports a concern about requests, but does not prove our service is affected. It includes a CVE and version range. We need more information before deciding." The bounded claim receives full credit; fields are merely listed, uncertainty is generic, and the request has only an implicit, general reason: applicability remains unresolved. That reason earns one action point, but the response does not say which check would resolve it. Ask what candidate-version and credential-use facts would change the decision.

**Deferral on D (2,2,2,2; 8/8).** "The OSV record names requests in PyPI, a range below 2.32.4, and CVE-2024-47081. Our team has not selected a version or credential configuration. Defer adoption until we select a candidate version and check the advisory's affected range and netrc conditions against the planned use. Resolving this report would not establish the absence of other risks."

**Conditional proceeding on D (2,2,2,2; 8/8).** "Continue evaluating requests as a candidate, but make acceptance contingent on checking the selected version against the reported range and the planned credential use against advisory conditions. The PyPI package and CVE identify a specific concern; they do not establish exposure in our unconfigured service. Stop acceptance if those checks leave this concern unresolved." This continues candidate evaluation, not unverified deployment.

**Resolving a specific concern on D+ (2,2,2,2; 8/8).** "The brief stipulates verified package identity and range information. The selected 2.32.4 version is outside the reported <2.32.4 range, so this range-based concern does not block the candidate. Continue ordinary adoption review; this conclusion does not establish overall security." Evidence sufficiency for this claim earns uncertainty credit without inventing another information request.

Instructors should calibrate borderline responses before scoring, score justifications rather than preferred actions, and report agreement before adjudication in formal research.

## Calibration boundaries

Score each dimension on a distinct feature: conclusion scope; field-to-claim support; decision consequence of uncertainty/sufficiency; and action rationale. The same error can affect multiple dimensions only when it separately fails each criterion. Do not deduct repeatedly merely because the recommendation differs from an exemplar. Misreading a version expression is not a defensible alternative interpretation.

For partial credit, generic caution bounds its claim (2), lists fields without interpreting them (1), leaves uncertainty generic (1), and offers a plausible pause with an implicit general reason (1). Full uncertainty credit on D+ explains why stipulated verification supports the particular closure; a request to repeat that verification without identifying a new decision-relevant concern does not show stronger reasoning.

Separate recommendations about candidate evaluation, dependency acceptance, and deployment. Conditional proceeding on D authorizes evaluation of the candidate, not acceptance before the checks. Deferral pauses adoption; both can be justified under the open brief. A concise response can earn full credit when it supplies all four features. Assessors should record the criterion and reasoning behind disagreements, then adjudicate; these proposed anchors still require reliability/validity testing.

## Case C: grouping and evidence preservation

**Full credit (2,2,2,2; 8/8).** "C1/C2 share an exact ecosystem-package-version triple; C3 has trailing whitespace. These are two exact groups, one after trimming, and three distinct CVEs before grouping. A surviving row cannot establish one vulnerability or complete coverage. Retain all three CVE references and check their affected conditions against the proposed version and use before closing the assessment."

Claim scope bounds the count and avoids asserting project applicability. Evidence trace links the triple, whitespace, and different CVEs to grouping. Uncertainty identifies unestablished applicability/coverage. The action retains the distinct evidence and specifies how it would inform the dependency decision.

**Normalization error (0,1,0,0; 1/8).** "Trim the version; the one remaining row means only one vulnerability needs review." It recognizes a grouping change but treats a group count as vulnerability coverage. Feedback: what happened to the other CVE references, and what claims can the surviving row support?

**Correct counts, incomplete decision (2,2,1,1; 6/8).** "The records yield two exact groups, one trimmed group, and three different CVEs. That is not proof of three vulnerabilities in our project. We need more information before choosing the dependency." The claim and field interpretation are strong, but the missing information and next action are generic. Full credit requires an explanation of which version/use or report facts matter and why retaining the references changes review.

These constructed examples illustrate proposed rubric use across a different reasoning demand; they do not validate scoring reliability or learning outcomes.

## Next-action boundary: 0, 1, or 2 points

An implicit reason can earn partial credit only when it is present in the student's own response. Do not supply facts or reasoning the student never expressed.

- **0:** "We need more information." This gives neither a reason nor a useful check. Do not infer a reason from the task brief alone.
- **1:** "The report does not establish whether our service is affected. We need more information before deciding." Unresolved applicability provides a general reason to pause. The response does not identify what information to check or how it would change the decision.
- **2:** "Our candidate version is unknown. Check it against the reported <2.32.4 range before accepting the dependency, because that comparison determines whether this version falls within the reported range." The response identifies a particular check and its consequence. Full credit for the whole memo still requires the other rubric dimensions and any other relevant advisory conditions.

These anchors clarify the next-action dimension only. They do not change the existing four-dimension example totals or establish scoring reliability.
