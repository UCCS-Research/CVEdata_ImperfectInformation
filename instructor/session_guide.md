# Session guide


Prerequisites: package ecosystems, dependency versions, vulnerability identifiers. Introduce project applicability and the distinction between source reports and extracted metadata. Use separate decision briefs for A-D; the components are not assumed to belong to one project.


| Minutes | Task |
|---|---|
| 0-8 | Vocabulary, memo prompts, short instructor model |
| 8-20 | D adoption memo and A comparison |
| 20-35 | B/C pair analysis, challenge and response |
| 35-50 | Compare D+ and scoring examples; justified revision |
| 50-65 | Distribute T1/T2 records and briefs; independent responses |


A 50-minute version shortens pair work and debrief; 75 minutes permits deeper record/query inspection. The timing is proposed, not classroom-tested. Pilot whether two brief independent responses fit the final block.


Keep T1/T2 and their guidance unseen during modeled practice. They are available in this archive; no additional database is needed. Independent performance supports formative assessment. The tasks are not validated research instruments or equivalent forms.


Ask what uncertainty matters, what finding changes the decision, and when the evidence supports closing a particular concern. Distinguish urgency from confidence and candidate evaluation from acceptance/deployment. Do not reward generic caution, verbosity, or requests to repeat facts stipulated in D+.


Proportionality asks whether an action addresses the relevant limitation and whether the result could change the recommendation. A concise explanation of why a concern is resolved can earn full credit. Preserve initial and revised memos separately from independent responses.


Before class, run `python3 scripts/prepare_handouts.py handouts`. Treat `instruction` as a staging collection and make the selections below before distribution. Keep the data notes, instructor folder, and source-check notes as instructor resources. Release D+ only during minutes 35-50 and the independent packet only during minutes 50-65. Use the glossary if students need support.


## Why this sequence
Use D to establish a concrete adoption decision, then contrast A's identity problem with D's unresolved applicability. B/C pair work adds disagreement across reports and the consequences of grouping. Return to D+ to ask whether verified exercise facts warrant changing the action or closing the particular concern. Finish with independent tasks without peer assistance. This is a proposed learning progression, not an evaluated sequencing effect.


## Preparing handouts for the lesson conditions

The generated `instruction` directory is a staging collection, not a packet to distribute unchanged. It contains D+ and activity-specific prompts. Before students receive any files, prepare these selections:

1. **Shared initial handouts (both lessons):** `instruction/data/cases.json` and/or `cases.csv`, `instruction/student/glossary.md`, and `instruction/analysis/original_unique_view.sql`. Make an initial copy of `instruction/student/decision_briefs.md` containing its opening note and A-D sections only. Remove the entire section beginning `## D+: Follow-up with stipulated verification` from that initial copy.
2. **Withheld follow-up (both lessons):** save the D+ heading and its complete section as a separate handout. Release it only during minutes 35-50, at the same point in both lessons. Keep the exercise's hypothetical-facts qualification with it.
3. **Activity lesson only:** add `instruction/student/activity.md` and `instruction/student/decision_memo.md`. Do not give these files to comparison students; they contain the four questions, peer challenge, and revision instructions.
4. **Comparison lesson only:** provide this instruction instead: "Write a short narrative summary of each supplied alert and what it means for the proposed project. Discuss your summaries and questions with a partner. When follow-up facts are released, update the summary to include them and their implications." Do not provide the four-question worksheet or require a formal peer challenge and separate revision explanation.
5. **Final independent block (both lessons):** withhold all files in `independent` until minutes 50-65. Do not distribute instructor guidance or scoring examples with any student handout.

Check the assembled initial handouts before class: no D+ section in either lesson, and no activity worksheet or challenge/revision directions in the comparison selection. The builder separates practice from independent records; this manual selection provides the timing and condition separation.
