# GovernIQ Expert Review Questionnaire

Two-round modified Delphi instrument, with qualitative feedback for thematic analysis and improvement triage.
Prepared 8 October 2026. Platform-ready wording for two separate Google Forms; no online form has been created.

## Researcher setup — not participant questions

Interpretation of triage: prioritising identified problems and proposed improvements by consequence and urgency.
This is separate from thematic analysis and Delphi agreement. If the supervisor intended triangulation, that is a
different methodological step and should be specified separately.

Before distribution, attach the university-approved participant information/consent material, with researcher
contact details, data access/retention arrangements and withdrawal conditions. This questionnaire does not invent
those commitments or claim ethics approval. Pilot wording and completion time with a suitable reviewer first.

Use stable participant codes across rounds. Keep any contact list separate from responses and avoid unnecessary
employer/project identifiers. Participants' responses should not be attributable to them in panel feedback; codes
allow the researcher to link rounds, so do not promise fully anonymous collection. Decide email/sign-in settings
accordingly. Round 2 invitations should go to the same panel.

Give all experts the same prototype version, brief, tasks and explanations. Record the version and whether they
used the system directly or watched a demonstration. Review mode affects usability conclusions. Do not present
positive results alone: include a false alarm and a missed delay. Do not ask experts to certify model accuracy.

The following order and item IDs should be retained. Closed questions may be required if “Unable to assess” or
“Prefer not to say” is available. Open feedback is optional unless the approved protocol specifies otherwise.
Estimated completion: 20–25 minutes after the demonstration; confirm through piloting.

---

# FORM 1 — GovernIQ Expert Evaluation: Delphi Round 1

## Introduction — form description

GovernIQ is a research prototype exploring how Knowledge Graphs, predictive models and explanations can support
programme/project governance. This evaluation concerns the prototype's observed clarity, usefulness, limitations
and improvement priorities. There are no preferred answers; critical feedback is valuable.

The prototype uses real portfolio records for graph analysis and a separate synthetic dataset for machine-learning
evaluation. These datasets are not joined project by project. Model scores are not calibrated real-world risk
probabilities. Automated tests do not establish enterprise readiness or independent correctness of source assumptions.

You will be invited to a second round containing a de-identified summary of the panel's feedback and a clear record
of any changes made. You may retain or revise your judgement. Agreement is not compulsory.

Please review the accompanying participant information before deciding whether to participate. Do not include
confidential organisational information or identify colleagues in your answers.

## A. Participation and background

**A1. Having read the accompanying participant information, do you voluntarily agree to participate in this expert evaluation?**
Type: Multiple choice, required. Options: Yes / No. Route No to end of form.

**A2. What is your assigned participant code?**
Type: Short answer, required. Use the same code in Round 2.

**A3. Which areas best describe your relevant professional experience?**
Type: Checkboxes. Options: Programme management / Project management / PMO or governance / Risk management /
Scheduling or project controls / Data science or AI / Enterprise or solution architecture / Research or academia /
Other (please specify) / Prefer not to say.

**A4. How many years of experience do you have in these areas?**
Type: Multiple choice. Options: Less than 3 / 3–5 / 6–10 / More than 10 / Prefer not to say.

**A5. How familiar are you with the following?**
Type: Multiple-choice grid. Columns: Not familiar / Basic awareness / Some practical experience / Extensive practical experience / Unable to assess.
Rows: Project dependency analysis / AI-based prediction / Explainable AI, including SHAP / Knowledge Graphs.

**A6. How did you review GovernIQ?**
Type: Multiple choice. Options: Used the prototype directly / Watched a live guided demonstration /
Watched a recorded demonstration / Combination of direct use and demonstration.

## B. Guided review tasks

Task 1: Inspect one real project's dependency path and its source evidence. Notice the direction of the links and any inferred relationships.

Task 2: Inspect a prediction and its feature explanation. Identify what increased and decreased the model's score.

Task 3: Inspect a false alarm and a missed delay. Review the confusion matrix and the limitations attached to the model scores.

Task 4: Identify the boundary between the real-project graph example and the separate synthetic prediction example.

**B1. Which tasks were you able to review?**
Type: Multiple-choice grid. Columns: Reviewed sufficiently / Reviewed partly / Not reviewed.
Rows: Task 1 — dependency path and provenance / Task 2 — prediction explanation /
Task 3 — false alarm, missed delay and performance / Task 4 — dataset separation.

**B2. What information or assistance, if any, was missing during these tasks?**
Type: Paragraph. Optional. Please identify the task and explain what was missing.

## C. Core Delphi statements — repeat unchanged in Round 2

For each statement, rate what the demonstrated prototype currently supports. Do not rate anticipated future features.

Response scale for C1–C15:
1 — Strongly disagree; 2 — Disagree; 3 — Neither agree nor disagree; 4 — Agree; 5 — Strongly agree;
Unable to assess — not demonstrated, not enough information, or outside my expertise.

Google Forms: three short multiple-choice grids, each with five rows and the six columns above.

### Graph representation and evidence

**C1. I can identify the prerequisite and dependent records in the displayed dependency paths.**

**C2. The graph view helps me identify records that may be affected by a change to another record.**

**C3. I can trace a displayed dependency to the source evidence used to construct it.**

**C4. The presentation makes inferred relationships distinguishable from relationships supported by reciprocal source declarations.**

**C5. I can recognise when a displayed record represents a summary section rather than an individual activity.**

### Prediction and explanation

**C6. I can identify which features increase or decrease the model's score for the displayed example.**

**C7. The feature explanation helps me understand why the model produced its displayed prediction.**

**C8. The presentation makes clear that feature contributions explain model behaviour rather than establish causes of project delay.**

**C9. The false-alarm and missed-delay examples help me understand the model's limitations.**

**C10. I can distinguish the real-portfolio graph findings from the synthetic-data model findings.**

### Presentation and decision support

**C11. The displayed information is organised so that I can follow a review scenario.**

**C12. The terminology used in the presentation is understandable to me.**

**C13. The outputs would help me formulate questions for a governance review meeting.**

**C14. The presentation provides enough evidence to question or challenge its outputs.**

**C15. The limits on applying the prototype to real organisational decisions are sufficiently clear.**

## D. Open feedback for thematic analysis

Type for D1–D6: Paragraph. Encourage concrete examples and reasoning. Do not require agreement with the ratings.

**D1. Which aspect of GovernIQ, if any, would be useful in your work, and in what situation? Please explain why.**

**D2. Which output or interaction was difficult to understand, unconvincing or potentially misleading? Describe a specific example and its possible consequence.**

**D3. How did the dependency-path and feature explanations affect your judgement of the outputs, if at all? Explain where they helped and where they did not.**

**D4. What additional evidence would you need before using this type of system in a real governance decision?**

**D5. Compared with your current approach to reviewing project information, what does this prototype add, omit or make more difficult?**

**D6. What important concern or perspective has this questionnaire not captured?**

## E. Improvement triage

**E1. Which areas should receive the highest improvement priority? Select up to three.**
Type: Checkboxes with maximum-three validation.
Options: Source-data interpretation and review / Graph readability and navigation / Summary-record versus activity distinction /
Relationship evidence and traceability / Prediction and error handling / Feature-explanation clarity /
Communication of uncertainty and limitations / Workflow and usability / Other (please specify) /
No priority improvement identified / Unable to assess.
Instruction: Select either of the last two options on its own.

**E2. Describe your single highest-priority issue and the change you recommend. If possible, say what a satisfactory improvement would look like.**
Type: Paragraph. If no issue was identified, leave blank. Route No priority improvement identified or Unable to assess past E2–E4 where practical.

**E3. How consequential is that issue if it remains unresolved?**
Type: Multiple choice.
Options: Critical — could materially mislead a governance decision / Major — substantially limits interpretation or use /
Moderate — creates difficulty but a reasonable workaround exists / Minor — mainly presentation or convenience /
Unable to assess / Not applicable.

**E4. When should that issue be addressed?**
Type: Multiple choice.
Options: Before another expert demonstration / Before a supervised real-world pilot /
Before broader organisational use / Suitable for future research or development / Unable to assess / Not applicable.

**E5. Which next step is most appropriate for the prototype in its current state?**
Type: Multiple choice.
Options: Further development before another demonstration / Suitable for further research evaluation only /
Consider a supervised pilot after specified conditions are met / Unable to assess.

**E6. Please explain your answer to E5 and state any conditions that should be met.**
Type: Paragraph.

---

# FORM 2 — GovernIQ Expert Evaluation: Delphi Round 2

## Introduction and controlled feedback

Thank you for participating in Round 1. Please review the de-identified panel summary and the change log before
responding. The summary includes agreement, disagreement and minority concerns, not only favourable feedback.
Your judgement remains your own; there is no obligation to agree with the group.

Researcher supplies, for every C item: exact wording, valid response count, median, interquartile range,
percentage agreeing, full response distribution and Unable to assess count. Where practical, provide each
participant their own previous ratings privately. Do not expose another person's individual response.

Supply concise qualitative findings and an issue/change log: issue ID, description, triage decision,
action taken or reason deferred, evidence of change, and prototype version. Proposed changes must not be
presented as implemented. If an item or feature changed, identify that explicitly.

**R2-A1. Do you agree to participate in this second round under the accompanying participant information?**
Type: Multiple choice. Yes / No. Route No to end.

**R2-A2. What is your assigned participant code?**
Type: Short answer.

**R2-A3. Which materials did you review before answering?**
Type: Checkboxes. Panel rating summary / Qualitative feedback summary / Change log / Updated demonstration /
None of these. Instruction: Select None on its own.

**R2-A4. How did you review the prototype in this round?**
Type: Multiple choice. Used it directly / Live demonstration / Recorded demonstration /
Combination / Reviewed the feedback materials only.

## Repeat C1–C15 verbatim

Use the exact Round 1 statements and response scale. Do not replace “current prototype” judgements with a
leading question such as “Has the improved system become better?”. If no prototype changes were made,
participants can still reassess after controlled feedback. Report that no refinement occurred.

## Round 2 reflection and priority

**R2-D1. Which ratings, if any, did you change, and what evidence or reasoning led you to change them?**
Type: Paragraph.

**R2-D2. Where do you disagree with the panel summary or the researcher's interpretation of the feedback? Please explain your reasoning.**
Type: Paragraph.

**R2-D3. Which changes, if any, addressed your concerns, and which concerns remain unresolved? Refer to issue IDs where possible.**
Type: Paragraph.

**R2-D4. Has reviewing the updated material revealed any new concern or unintended consequence? Please describe it.**
Type: Paragraph.

**R2-E1. Select up to three unresolved issues that should receive the highest priority next.**
Type: Checkboxes populated with the stable issue IDs/descriptions from Round 1; add New issue (describe below),
No unresolved priority issue identified and Unable to assess. Use maximum-three validation; the last two options stand alone.

**R2-E2. For your highest-priority remaining issue, state its ID or describe it, explain its consequence, and recommend the next action.**
Type: Paragraph.

**R2-E3. How consequential is that issue if it remains unresolved?**
Type: Multiple choice. Repeat E3 severity options verbatim.

**R2-E4. When should that issue be addressed?**
Type: Multiple choice. Repeat E4 timing options verbatim.

**R2-E5. Which next step is most appropriate for the prototype in its current state?**
Type: Multiple choice. Repeat E5 options verbatim.

**R2-E6. What evidence or conditions support your recommendation?**
Type: Paragraph.

---

# Researcher analysis plan — not part of the participant form

## 1. Modified Delphi

Agree and record the panel criteria, target size and decision rules with the supervisor before collecting data.
Use two planned rounds with controlled de-identified feedback. Do not call a single questionnaire a completed Delphi.
Predefined statements make this a modified rather than open first-round Delphi approach.

Suggested study-specific rule, not a universal Delphi standard:

- Agreement: at least 80% of valid numeric ratings are 4 or 5.
- Disagreement: at least 80% of valid numeric ratings are 1 or 2.
- Otherwise: no consensus. A concentration at 3 is not agreement.
- Classify consensus only when at least 70% of that round's responding panel supplies a numeric rating for the item;
  otherwise mark insufficient assessable responses. Exclude Unable to assess from the numeric denominator and report it.
- Report actual counts as well as percentages, especially with a small panel. Fix any minimum panel-size requirement
  with the supervisor before collection; a high percentage from very few responses is weak evidence.

For each item report median, IQR, response counts/distribution and consensus status in each round. Show linked
participant changes separately from whole-panel summaries and report attrition. Do not pool rounds as independent
observations, average all constructs into an unvalidated single effectiveness score, or infer statistical significance
from small descriptive changes. Do not claim psychometric validation merely because these questions were used.

Stop after the planned two rounds and report unresolved disagreement; do not keep adding rounds just to force
consensus. If the protocol permits a further round, define its trigger in advance. A change in ratings may reflect
feedback, prototype changes, panel attrition or several factors; do not attribute it solely to system improvement.

## 2. Thematic analysis

Use paragraph responses from both rounds, retaining participant code, question ID and round. A defensible choice is
Braun and Clarke's reflexive thematic analysis: familiarisation, coding, initial theme development, theme review,
definition/naming and analytic writing. The process is iterative rather than a rigid checklist.

Code the actual responses rather than treating the questionnaire headings as predetermined findings. Develop
patterns of meaning across responses, preserve contradictory/minority perspectives, and support claims with
de-identified excerpts. Keep reflexive notes about the researcher's role as prototype developer and expectations.
Round 2 responses can refine or challenge the interpretation; they do not automatically validate every theme.

Short survey comments may provide limited depth. Do not claim thematic saturation solely because the questionnaire
has been completed. If depth is insufficient, discuss that limitation or arrange approved follow-up questions.
If claiming reflexive TA, do not simultaneously claim that coder agreement or inter-rater reliability proves the
themes are correct; a different TA approach would require its own coherent justification.

## 3. Improvement triage and audit trail

Create one record for each distinct actionable issue. Triage decisions are researcher judgements informed by expert
feedback, not automatically Delphi consensus or thematic findings. Merge duplicates carefully while preserving origins.

Recommended columns:
Issue ID | Participant codes/question IDs | Verbatim evidence | Related theme(s) | Affected component |
Reported severity | Requested timing | Researcher verification | Priority | Proposed action | Feasibility/dependency |
Decision (implement/defer/investigate/not adopt) | Rationale | Change reference | Validation evidence | Round 2 feedback.

Suggested priority rules:
- P1: credible risk of materially misleading interpretation or incorrect evidence; investigate before the next demonstration.
- P2: substantial clarity/workflow limitation; address before a supervised pilot where feasible.
- P3: minor presentation issue or justified future enhancement; schedule or defer with reasons.

Do not equate frequency with severity. A single credible serious concern may outrank many cosmetic requests.
Check evidence and feasibility rather than accepting every requested feature. Do not silently change the established
ML evaluation protocol or retune against the already inspected holdout in response to expert preference.
In Round 2, report completed changes, tested effects and unresolved issues honestly. Expert preference is not proof
of predictive accuracy, causal validity or enterprise readiness.

## Methodological references

- Example of a two-round modified Delphi using rating/ranking, briefing material and piloted questions:
  https://bmjopen.bmj.com/content/9/3/e023890
- Controlled feedback and explicit consensus decisions in a modified Delphi protocol:
  https://doi.org/10.1136/bmjopen-2018-026701
- Braun and Clarke's guidance on the reflexive thematic-analysis process:
  https://www.thematicanalysis.net/doing-reflexive-ta/
- Their guidance on methodological coherence when reporting reflexive thematic analysis:
  https://www.thematicanalysis.net/editor-checklist/

The questionnaire wording and proposed consensus/triage rules above are tailored to GovernIQ; they are not a
validated published measurement scale. Finalise the protocol with the supervisor before recruiting participants.
