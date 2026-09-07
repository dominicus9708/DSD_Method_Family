# SPEC-CH-007 — Source-Intentional Openness / Accidental Underspecification Boundary Challenge

Date: 2026-09-07
Evidence scope: `method_specific`
Method directly tested: **DSD Specification / DSD 명세론**
Protocol basis: **Specification Protocol v0.2 + precommitted openness/determinacy axis candidate**
Precommit: [`SPEC-CH-007_open-texture-underspecification_precommit.md`](SPEC-CH-007_open-texture-underspecification_precommit.md)
Precommit commit: `1b3665696007b29535b3f46815cad39f4f02c03f`

## 1. Result in one line

The challenge supports separating **what the source intentionally leaves open** from **whether the declared downstream task is sufficiently determined**. These are not opposite labels; they are independent axes.

```text
SOURCE_OPENNESS_STATUS
!= DOWNSTREAM_DETERMINACY_STATUS
```

Most importantly:

```text
SOURCE_INTENTIONAL_OPENNESS
+ UNDERDETERMINED_FOR_DECLARED_TASK
```

is a coherent joint state and was required by Case C2.

## 2. Locked candidate axes

### Axis O — Source openness status

```text
SOURCE_DETERMINATE
SOURCE_INTENTIONAL_OPENNESS
OPENNESS_INTENT_UNDETERMINED
NOT_APPLICABLE
NOT_SCORED_DUE_TO_HARD_FAILURE
```

### Axis D — Downstream determinacy status

```text
SUFFICIENT_AT_DECLARED_RESOLUTION
UNDERDETERMINED_FOR_DECLARED_TASK
NOT_APPLICABLE
NOT_SCORED_DUE_TO_FABRICATION
```

`SPEC_UNDERSPECIFIED` remains a task-relative method outcome. The source-openness axis does not replace it.

## 3. Case results

| Case | Source openness observed | Downstream determinacy observed | `SPEC_UNDERSPECIFIED` | Hard failure | Match |
|---|---|---|---|---|---|
| C1 bounded professional judgment, human review | `SOURCE_INTENTIONAL_OPENNESS` | `SUFFICIENT_AT_DECLARED_RESOLUTION` | no | no | yes |
| C2 same source, forced automation | `SOURCE_INTENTIONAL_OPENNESS` | `UNDERDETERMINED_FOR_DECLARED_TASK` | yes, relative to automation | no | yes |
| C3 explicit admissible interval | `SOURCE_DETERMINATE` | `SUFFICIENT_AT_DECLARED_RESOLUTION` | no | no | yes |
| C4 missing threshold | `OPENNESS_INTENT_UNDETERMINED` | `UNDERDETERMINED_FOR_DECLARED_TASK` | yes | no | yes |
| C5 missing bridge selector disguised as discretion | `OPENNESS_INTENT_UNDETERMINED` | `UNDERDETERMINED_FOR_DECLARED_TASK` | yes | no at structural-gap level | yes |
| C6 missing approval authority | `OPENNESS_INTENT_UNDETERMINED` | `UNDERDETERMINED_FOR_DECLARED_TASK` | yes | no | yes |
| C7 explicit contextual judgment + competent external standard | `SOURCE_INTENTIONAL_OPENNESS` | `SUFFICIENT_AT_DECLARED_RESOLUTION` | no | no | yes |
| C8 invented closure | `NOT_SCORED_DUE_TO_HARD_FAILURE` | `NOT_SCORED_DUE_TO_FABRICATION` | source gap preserved if applicable | `SOURCE_FACT_INVENTION` | yes |

## 4. Why the distinctions survive

### C1 — Intentional openness can be fully sufficient

The source does not pick A, B, or C in advance, but it supplies:

```text
qualified actor
admissible alternatives
criteria K1-K3
reason-recording obligation
```

The declared downstream task only asks whether that process occurred. Therefore the source is intentionally open at the substantive-choice level while still sufficient for the declared review task.

```text
SOURCE_OPENNESS_STATUS: SOURCE_INTENTIONAL_OPENNESS
DOWNSTREAM_DETERMINACY_STATUS: SUFFICIENT_AT_DECLARED_RESOLUTION
```

Calling this `SPEC_UNDERSPECIFIED` would wrongly demand more determinacy than the task requires.

### C2 — Intentional openness does not guarantee every downstream task

The source is identical to C1, but the downstream task demands a fully automatic A-or-not-A output with no reviewer judgment step.

The source's openness remains intentional; however, that same source is underdetermined relative to the stronger automation task.

```text
SOURCE_OPENNESS_STATUS: SOURCE_INTENTIONAL_OPENNESS
DOWNSTREAM_DETERMINACY_STATUS: UNDERDETERMINED_FOR_DECLARED_TASK
SPEC_UNDERSPECIFIED: yes_relative_to_automation_task
```

This case prevents the new openness concept from becoming an excuse that suppresses genuine downstream underspecification.

### C3 — Multiple allowed values are not automatically open texture

The interval `[5,10]` is a determinate admissible set. The source need not choose one unique value because the task asks only membership.

```text
SOURCE_OPENNESS_STATUS: SOURCE_DETERMINATE
DOWNSTREAM_DETERMINACY_STATUS: SUFFICIENT_AT_DECLARED_RESOLUTION
```

This prevents “more than one allowed outcome” from being mislabeled as ambiguity or discretion.

### C4 — Missing threshold remains underspecification

“Too high” supplies neither a threshold nor a competent source-supported judgment mechanism. No evidence establishes that the omission is a deliberate normative choice.

```text
SOURCE_OPENNESS_STATUS: OPENNESS_INTENT_UNDETERMINED
DOWNSTREAM_DETERMINACY_STATUS: UNDERDETERMINED_FOR_DECLARED_TASK
SPEC_UNDERSPECIFIED: yes
```

The protocol does not infer intentional openness simply because information is missing.

### C5 — Calling a missing bridge “discretion” does not repair it

The transfer needs a selector between B1 and B2. The source does not provide one and does not delegate that selection to a competent actor.

```text
SOURCE_OPENNESS_STATUS: OPENNESS_INTENT_UNDETERMINED
DOWNSTREAM_DETERMINACY_STATUS: UNDERDETERMINED_FOR_DECLARED_TASK
SPEC_UNDERSPECIFIED: yes
```

If a derivative merely records “reviewer discretion” as its own unresolved proposal, the structural gap remains but there is no additional source-fact hard failure. If it falsely attributes that discretion to the source, G1/G4 guardrails are crossed and source-invention rules may separately activate.

### C6 — Missing authority is not freedom of choice

An approval requirement with no actor or authority source cannot be converted into “any qualified person may approve.”

```text
OPENNESS_INTENT_UNDETERMINED
+ UNDERDETERMINED_FOR_DECLARED_TASK
```

The missing authority remains `SPEC_UNDERSPECIFIED` for the declared task.

### C7 — External competent judgment can make bounded openness sufficient

The source explicitly incorporates Standard S, which identifies the competent actor, minimum considerations, and documentation requirements while intentionally preserving contextual judgment.

This is not a wrong-standard substitution because the incorporation is source-supported.

```text
SOURCE_OPENNESS_STATUS: SOURCE_INTENTIONAL_OPENNESS
DOWNSTREAM_DETERMINACY_STATUS: SUFFICIENT_AT_DECLARED_RESOLUTION
SPEC_UNDERSPECIFIED: no
```

### C8 — Invented closure is not determinacy

Inserting threshold `7` without source or external-standard support does not transform an unresolved source into a well-specified one.

```text
HARD_FAILURE: SOURCE_FACT_INVENTION
DOWNSTREAM_DETERMINACY_STATUS: NOT_SCORED_DUE_TO_FABRICATION
GUARDRAIL_VERDICT: PURPOSE_OR_VIEWPOINT_DISTORTED
```

The fabricated answer is excluded from any apparent determinacy gain.

## 5. Scoring

```text
EXACT_SOURCE_OPENNESS_AXIS_MATCHES: 8/8
EXACT_DOWNSTREAM_DETERMINACY_AXIS_MATCHES: 8/8
EXACT_JOINT_AXIS_MATCHES: 8/8

TASK_SUFFICIENT_INTENTIONAL_OPENNESS_ACCEPTED: 2/2
INTENTIONAL_OPENNESS_WITH_AUTOMATION_GAP_PRESERVED: 1/1
DETERMINATE_ADMISSIBLE_SET_NOT_MISLABELED_OPEN: 1/1
ACCIDENTAL_OR_UNRESOLVED_MISSING_DATA_DETECTED: 3/3
UNSUPPORTED_INTENT_NOT_INVENTED: 3/3
INVENTED_RESOLUTION_ESCALATED_TO_HARD_FAILURE: 1/1

FALSE_UNDERSPECIFICATION_ON_TASK_SUFFICIENT_INTENTIONAL_OPENNESS: 0
FALSE_OPENNESS_EXCUSE_FOR_MISSING_REQUIRED_DATA: 0
FALSE_DETERMINACY_FROM_INVENTED_VALUE: 0

POST_REVEAL_CRITERION_CHANGE: no
POST_REVEAL_EXCEPTION_ADDED: no
```

## 6. Core methodological result

The challenge rejects a single-axis treatment such as:

```text
intentional_openness OR underspecified
```

because C2 proves the two statements answer different questions.

The better representation is:

```text
SOURCE_OPENNESS_STATUS:
  what does the source itself support about closure/discretion?

DOWNSTREAM_DETERMINACY_STATUS:
  is that source resolution sufficient for the declared downstream task?
```

Therefore:

```text
SOURCE_INTENTIONAL_OPENNESS
!= specification completeness for every downstream task

SPEC_UNDERSPECIFIED
!= proof that the source accidentally failed to specify something
```

`SPEC_UNDERSPECIFIED` remains explicitly task-relative.

## 7. Result

```text
RESULT:
SPECIFICATION_OPENNESS_DETERMINACY_AXIS_SEPARATION_PILOT_PASS_WITH_LIMITATIONS

SOURCE_OPENNESS_AND_DOWNSTREAM_DETERMINACY_SEPARATION:
pass_on_locked_constructed_cases

SPEC_UNDERSPECIFIED_DETECTOR_WEAKENED:
no

NEW_SHARED_CORE_RULE:
no
```

## 8. Protocol consequence

The result supports a **prospective minor protocol revision** rather than a replacement of v0.2 history.

Recommended fields for the next protocol version:

```text
SOURCE_OPENNESS_STATUS:
  SOURCE_DETERMINATE
  SOURCE_INTENTIONAL_OPENNESS
  OPENNESS_INTENT_UNDETERMINED
  NOT_APPLICABLE

DOWNSTREAM_DETERMINACY_STATUS:
  SUFFICIENT_AT_DECLARED_RESOLUTION
  UNDERDETERMINED_FOR_DECLARED_TASK
  NOT_APPLICABLE
```

These fields should remain separate from `FINAL_SPEC_STATUS` and the G1-G4 guardrail ledger.

## 9. Limits

- finite constructed challenge;
- same project/session/model family;
- no independent evaluator;
- intentionality is accepted only where source evidence supports it;
- no claim that DSD can infer an author's unexpressed intentions;
- no external v0.2.1 application yet;
- no measured practical-performance improvement.

## 10. Next step

Create prospective **Specification Protocol v0.2.1** with the two independent axes, preserving v0.2 and `SPEC-APP-002` unchanged. Then prioritize independent retrace or a new external application before another maturity-status decision.
