# Matched lesson directions for a proposed comparison

These are proposed instructor directions, not a tested protocol or evidence of learning. Pilot the directions for clarity and timing before a formal study. The comparison is an active lesson in alert interpretation, with the same security content as the proposed activity.

For exact file selection and release timing, follow [Preparing handouts for the lesson conditions](session_guide.md#preparing-handouts-for-the-lesson-conditions). The generated `instruction` directory must not be distributed unchanged: it contains D+ and activity-only prompts. Both lessons receive A-D initially and D+ only at minutes 35-50.

## Shared preparation and content

Use the same eight records, A-D and D+ project briefs, glossary, case order, 65-minute duration, and opportunities for pair discussion. Teach both conditions that a CVE does not establish project exposure, that identity and affected conditions require checking, and that sufficient verified exercise facts can resolve one concern without proving overall security. Give the same factual explanation of each case in both conditions. Do not give one group extra advisory facts, additional practice records, or more feedback time. Use the student-only packets and withhold instructor scoring examples until practice is complete.

## Lesson schedule

| Time | Shared cases and content | Proposed activity | Alert-summary comparison |
| --- | --- | --- | --- |
| 0-8 minutes | Vocabulary, adoption scenario, and an instructor model using D. | Model the four memo questions and connect the next action to the missing project facts. | Model a short narrative summary covering the report, its fields, what it does and does not establish about the project, and the appropriate follow-up. |
| 8-20 minutes | D, followed by A; discuss applicability and questionable package extraction. | Students draft memos using the four questions. | Students write short narrative alert summaries and discuss their interpretations in pairs. |
| 20-35 minutes | B/C; discuss conflicting names, grouping, and retaining distinct CVE references. | Partners challenge one claim using specific evidence; authors respond. | Partners discuss their summaries and questions. Do not require a formal challenge and response. |
| 35-50 minutes | Release D+ at the same time. Explain why the stipulated checks resolve the range-based concern. | Students revise a memo and explain why the recommendation changed or remained justified. | Students update a summary to include the follow-up facts and their implications. Discuss why the specific concern is resolved. Do not require a separate justification of revisions. |
| 50-65 minutes | T1/T2 independent practice, without case-specific hints or feedback between responses. | Recommend an action and justify it from the evidence, without the four prompts. | Use the identical independent instructions. |

## Instructor models

Use the following factual content in both models for D: the record identifies requests in PyPI and a range below 2.32.4. Its stored snippet describes possible netrc credential leakage through URL parsing. The project brief leaves the candidate version and credential configuration undecided. The record alone therefore does not establish project exposure. Check the candidate version and planned credential use against the advisory conditions before dependency acceptance. Continuing candidate evaluation can be justified while acceptance remains conditional on those checks.

For the proposed activity, organize that explanation under the four memo questions. For the comparison, present it as a connected narrative alert summary. Do not omit the applicability reasoning from the comparison model.

For D+, both instructors explain that verified exercise facts place the selected 2.32.4 version outside the confirmed <2.32.4 range. This resolves that specific concern and allows ordinary adoption review to continue; it does not establish overall security. The proposed activity explicitly asks students to compare this decision with D and justify their revision. The comparison incorporates the same facts and conclusion into its narrative summary.

## Student instructions

**Proposed activity:** Use the decision memo's four questions. Exchange your memo with a partner, challenge one interpretation using the supplied evidence, respond to the challenge, and explain any revision.

**Comparison:** Write a short narrative summary of each supplied alert and what it means for the proposed project. Discuss your summaries and questions with a partner. When follow-up facts are released, update the summary to include them and their implications. Do not provide the four-question worksheet, a required peer challenge, or a separate revision explanation.

The intended difference is how students organize and practice the reasoning. Both conditions teach the same security concepts, including sufficient evidence. The comparison evaluates the complete activity against this matched lesson; it does not isolate the effect of any one component. Record departures from the directions and pilot instructor delivery before claiming comparable enactment.

## Research assessments

T1/T2 are public practice candidates, not validated equivalent research forms. Formal pre/post and delayed assessments require additional unfamiliar records balanced across the proposed task types, including sufficient evidence. Administer the same unprompted action-and-justification instructions in both conditions. Research assessments take additional time beyond the 65-minute lesson. Withhold feedback between paired assessment responses and use the evaluation plan's independent scoring procedure.

The hypothesis concerns explicitly explaining and defending why the evidence warrants an action through the complete memo, critique, and revision sequence. Since both lessons include the same case contrasts, this design cannot attribute an advantage to contrasting cases alone. See the evaluation plan's assessment-task requirements and task-specific decision scoring guide; both conditions use those same neutral assessment instructions and scoring rules.
