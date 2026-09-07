# SPEC-CH-007 — Source-Intentional Openness / Accidental Underspecification Boundary Challenge — Precommit

Date: 2026-09-07
Evidence scope: `method_specific`
Method directly tested: **DSD Specification / DSD 명세론**
Protocol basis: **Specification Protocol v0.2 + prospective openness/determinacy axis candidate**

## 1. Challenge question

Can DSD Specification distinguish:

```text
source-intentional openness
!= accidental missing specification
!= uncertainty about whether the openness was intentional
```

without weakening `SPEC_UNDERSPECIFIED`, and without inventing a deterministic answer where the source intentionally preserves judgment?

The challenge also tests a stronger separation:

```text
SOURCE_OPENNESS_STATUS
!= DOWNSTREAM_DETERMINACY_STATUS
```

A source may intentionally leave a judgment open and still be insufficient for a downstream task that demands a fully automated deterministic answer. Those are different propositions and may coexist.

## 2. Candidate axes locked before reveal

### Axis O — Source openness status

```text
O1 SOURCE_DETERMINATE
  the source supplies a determinate value/rule/set at the resolution relevant to the task

O2 SOURCE_INTENTIONAL_OPENNESS
  the source itself supports that bounded discretion, professional judgment,
  contextual balancing, or an open choice is intentionally preserved

O3 OPENNESS_INTENT_UNDETERMINED
  the source leaves a point unresolved but does not support a stronger claim
  that the openness was intentional or accidental

O4 NOT_APPLICABLE
```

### Axis D — Downstream determinacy status

```text
D1 SUFFICIENT_AT_DECLARED_RESOLUTION
  the source supplies enough structure for the declared downstream task

D2 UNDERDETERMINED_FOR_DECLARED_TASK
  the declared downstream task requires a value/selector/actor/bridge/criterion
  not determined at the locked source resolution

D3 NOT_APPLICABLE
```

The axes are independent. In particular:

```text
SOURCE_INTENTIONAL_OPENNESS
+ UNDERDETERMINED_FOR_DECLARED_TASK
```

is an allowed joint state when, for example, a source intentionally delegates bounded professional judgment but the downstream task demands an automatic binary decision without that human judgment step.

## 3. Relation to existing Specification outcomes

`SPEC_UNDERSPECIFIED` remains active when the **declared downstream task** needs a missing distinction/selector/threshold/actor/bridge/criterion.

The candidate source-openness axis does not excuse accidental missing data and does not automatically suppress `SPEC_UNDERSPECIFIED`.

Conversely, a source-supported intentional judgment boundary is not itself called an accidental source defect merely because no single deterministic answer exists.

## 4. Locked cases

### C1 — Explicit bounded professional judgment, human review task

Source:
```text
A qualified reviewer shall choose among A/B/C using criteria K1-K3
and document the reasons for the choice.
```
Downstream task: check whether a qualified reviewer applied K1-K3 and documented the choice.

Expected:
```text
SOURCE_OPENNESS_STATUS: SOURCE_INTENTIONAL_OPENNESS
DOWNSTREAM_DETERMINACY_STATUS: SUFFICIENT_AT_DECLARED_RESOLUTION
SPEC_UNDERSPECIFIED: no
HARD_FAILURE: no
```

### C2 — Same intentional judgment, but fully automated binary task

Same source as C1.
Downstream task: produce an automatic A-or-not-A answer without reviewer judgment.

Expected:
```text
SOURCE_OPENNESS_STATUS: SOURCE_INTENTIONAL_OPENNESS
DOWNSTREAM_DETERMINACY_STATUS: UNDERDETERMINED_FOR_DECLARED_TASK
SPEC_UNDERSPECIFIED: yes_relative_to_automation_task
HARD_FAILURE: no
```

This case is essential: intentional openness and task-relative underspecification can coexist.

### C3 — Explicit admissible interval, membership-check task

Source:
```text
Any value x in [5,10] is acceptable.
```
Downstream task: check whether supplied x is admissible.

Expected:
```text
SOURCE_OPENNESS_STATUS: SOURCE_DETERMINATE
DOWNSTREAM_DETERMINACY_STATUS: SUFFICIENT_AT_DECLARED_RESOLUTION
SPEC_UNDERSPECIFIED: no
HARD_FAILURE: no
```

An admissible set is not called vague merely because it contains multiple values.

### C4 — Missing threshold required by automated checker

Source:
```text
Reject values that are too high.
```
No threshold, external criterion, or competent judgment actor is supplied.
Downstream task: automatic numeric pass/fail.

Expected:
```text
SOURCE_OPENNESS_STATUS: OPENNESS_INTENT_UNDETERMINED
DOWNSTREAM_DETERMINACY_STATUS: UNDERDETERMINED_FOR_DECLARED_TASK
SPEC_UNDERSPECIFIED: yes
HARD_FAILURE: no
```

### C5 — Missing bridge selector disguised as discretion

Source requires transfer from carrier A to carrier B but supplies neither bridge selector nor a source-supported judgment mechanism among B1/B2.
A derivative draft labels this “reviewer discretion” without source support.

Expected:
```text
SOURCE_OPENNESS_STATUS: OPENNESS_INTENT_UNDETERMINED
DOWNSTREAM_DETERMINACY_STATUS: UNDERDETERMINED_FOR_DECLARED_TASK
SPEC_UNDERSPECIFIED: yes
HARD_FAILURE: no_if_the_draft_does_not_claim_source_support
GUARDRAIL_PRESSURE_OR_DISTORTION: distortion_if_discretion_is_attributed_to_source
```

### C6 — Missing authority/actor

Source:
```text
Approval is required before release.
```
No actor or authority is identified and no external standard fills the role.
Downstream task: determine who may validly approve.

Expected:
```text
SOURCE_OPENNESS_STATUS: OPENNESS_INTENT_UNDETERMINED
DOWNSTREAM_DETERMINACY_STATUS: UNDERDETERMINED_FOR_DECLARED_TASK
SPEC_UNDERSPECIFIED: yes
HARD_FAILURE: no
```

### C7 — Explicit contextual judgment with competent external standard

Source:
```text
Use professional judgment appropriate to the case.
```
The source explicitly incorporates external Standard S, which defines qualified actor, minimum considerations, and documentation obligations but intentionally does not force one result.
Downstream task: check competent process and documented judgment, not force a unique substantive outcome.

Expected:
```text
SOURCE_OPENNESS_STATUS: SOURCE_INTENTIONAL_OPENNESS
DOWNSTREAM_DETERMINACY_STATUS: SUFFICIENT_AT_DECLARED_RESOLUTION
SPEC_UNDERSPECIFIED: no
HARD_FAILURE: no
```

### C8 — Invented closure of an open or unresolved source

Source leaves a threshold unresolved or intentionally contextual.
DSD derivative inserts threshold `7` without source or external-standard support and presents it as source-grounded.

Expected:
```text
SOURCE_OPENNESS_STATUS: not_needed_for_hard_failure_decision
DOWNSTREAM_DETERMINACY_STATUS: fabricated_not_counted_as_sufficient
SPEC_UNDERSPECIFIED_SOURCE_GAP_IF_ACCIDENTAL: preserve_if_applicable
HARD_FAILURE: yes
HARD_FAILURE_CLASS: SOURCE_FACT_INVENTION
GUARDRAIL_VERDICT: PURPOSE_OR_VIEWPOINT_DISTORTED
```

## 5. Precommitted scoring

```text
EXACT_SOURCE_OPENNESS_AXIS_MATCHES: 8/8
EXACT_DOWNSTREAM_DETERMINACY_AXIS_MATCHES: 8/8
EXACT_JOINT_AXIS_MATCHES: 8/8

TASK_SUFFICIENT_INTENTIONAL_OPENNESS_ACCEPTED: 2/2   # C1, C7
INTENTIONAL_OPENNESS_WITH_AUTOMATION_GAP_PRESERVED: 1/1  # C2
DETERMINATE_ADMISSIBLE_SET_NOT_MISLABELED_OPEN: 1/1      # C3
ACCIDENTAL_OR_UNRESOLVED_MISSING_DATA_DETECTED: 3/3      # C4-C6
UNSUPPORTED_INTENT_NOT_INVENTED: 3/3                     # C4-C6
INVENTED_RESOLUTION_ESCALATED_TO_HARD_FAILURE: 1/1       # C8

FALSE_UNDERSPECIFICATION_ON_TASK_SUFFICIENT_INTENTIONAL_OPENNESS: 0
FALSE_OPENNESS_EXCUSE_FOR_MISSING_REQUIRED_DATA: 0
FALSE_DETERMINACY_FROM_INVENTED_VALUE: 0
```

For C8, axis scoring accepts the locked sentinel values:

```text
SOURCE_OPENNESS_AXIS_EXPECTED: NOT_SCORED_DUE_TO_HARD_FAILURE
DOWNSTREAM_DETERMINACY_AXIS_EXPECTED: NOT_SCORED_DUE_TO_FABRICATION
```

so “8/8” means exact match to the locked case-specific expected state, including the hard-failure sentinel.

## 6. Anti-post-hoc rule

After this precommit is committed:
- no case may be removed because it complicates the distinction;
- `SPEC_UNDERSPECIFIED` may not be weakened merely to protect intentional openness;
- intentional openness may not be converted into a unique value for scoring convenience;
- `OPENNESS_INTENT_UNDETERMINED` may not be upgraded to intentional without source evidence;
- no protocol field may be added and retrospectively credited to this challenge;
- failure, mixed, or no-gain outcomes must be preserved.

## 7. Promotion restraint

Passing this constructed challenge would support a **prospective method-specific protocol refinement only**.

It would not establish:
- independent evaluator validation;
- broad external utility;
- improved ethical/legal/professional judgment;
- a new shared-core rule;
- automatic `established` method status.
