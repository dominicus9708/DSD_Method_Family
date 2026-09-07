# SPEC-MEAS-005 — Human Maintenance Triage Benchmark Precommit

Date: 2026-09-08
Status: PRECOMMITTED / NOT YET RUN
Method under test: DSD Specification v1.0
Benchmark rule: `PRACTICAL_BENCHMARK_RULE_v0.1.md`
Evidence class if completed: human practical comparative benchmark

## 1. Purpose

Measure a quantity not measured by `SPEC-MEAS-001` through `SPEC-MEAS-004`: actual human maintenance-triage time and human impact-selection error under a locked requirement-change task.

This benchmark does not assume DSD advantage.

The strong conventional route is deliberately given stable IDs, activation conditions, explicit dependency links, and external-standard metadata. DSD must not gain merely because the baseline is impoverished.

## 2. Primary question

For matched requirement corpora and matched change notices, does a human evaluator using a DSD Specification carrier differ from a human evaluator using a strong conventional traceability carrier in:

```text
ELAPSED_TASK_TIME_SECONDS
MISSED_IMPACT_IDS
FALSE_IMPACT_IDS
EXTERNAL_STANDARD_REVIEW_ERRORS
```

No cognitive-load, productivity, or organizational-cost claim may be inferred from these quantities alone.

## 3. Human-evaluator boundary

Primary evidence requires a human evaluator who is not the project author and who does not know the hidden gold answers before freezing their result.

```text
PROJECT_AUTHOR_SELF_RUN_AS_PRIMARY_EVIDENCE: prohibited
SAME_MODEL_OR_ASSISTANT_SELF_RUN_AS_HUMAN_EVIDENCE: prohibited
ANSWER_KEY_ACCESS_BEFORE_FREEZE: prohibited
EXTERNAL_BROWSING_DURING_TASK: prohibited
```

A project-author or same-session rehearsal may be recorded only as an unscored usability rehearsal and may not enter the primary measurement.

## 4. Study forms

Two matched, isomorphic corpora are used:

```text
CORPUS_O: ORBIT
CORPUS_H: HARBOR
REQUIREMENTS_PER_CORPUS: 14
CHANGE_NOTICES_PER_CORPUS: 4
EXPECTED_IMPACT_INSTANCE_COUNT_PER_CORPUS: 11
```

Two counterbalanced reviewer packet sets are prepared:

```text
SET_A:
  FORM_1 = conventional carrier on ORBIT
  FORM_2 = DSD carrier on HARBOR

SET_B:
  FORM_1 = DSD carrier on ORBIT
  FORM_2 = conventional carrier on HARBOR
```

Route names are not printed to the reviewer; forms are identified only as `FORM_1` and `FORM_2`.

## 5. Preferred design and fallback design

Preferred primary design:

```text
BETWEEN_EVALUATOR_COUNTERBALANCED
MINIMUM_TOTAL_EVALUATORS_FOR_DESCRIPTIVE_PRIMARY_RUN: 4
MINIMUM_PER_PACKET_SET: 2
EACH_EVALUATOR_COMPLETES: one form only
```

This avoids same-person learning transfer.

If only one or two humans are available, a crossover run may be executed with matched corpora and reversed order, but it must be labeled:

```text
EXPLORATORY_CROSSOVER
NOT_DECISIVE_FOR_METHOD_MATURITY
```

No p-value or population-level superiority claim is precommitted. Raw and descriptive results remain primary.

## 6. Timer rule

For each form:

1. The evaluator starts a stopwatch immediately before opening the carrier-and-task section.
2. The evaluator reads the carrier and four change notices.
3. The evaluator records impacted IDs and the external-standard-review yes/no field for each change.
4. The evaluator stops the stopwatch immediately after the final answer is frozen.
5. The evaluator records whole seconds.

```text
PAUSES_ALLOWED: no, except emergency interruption
INTERRUPTED_RUN: exclude_from_primary_time_and_preserve_as_interrupted
POST_FREEZE_CORRECTION: prohibited for primary score
```

The legend and all representation overhead are read inside the timer. This intentionally measures practical task exposure, not pure lookup speed after training.

## 7. Locked reviewer output

For each change notice:

```text
EVALUATOR_ID:
PACKET_SET:
FORM_ID:
CORPUS_ID:
CHANGE_ID:
IMPACT_IDS: comma-separated sorted IDs
EXTERNAL_STANDARD_REVIEW: yes | no
```

At form end:

```text
ELAPSED_TASK_TIME_SECONDS:
INTERRUPTED: yes | no
RESULT_FROZEN: yes
```

No rationale is required for scoring.

## 8. Locked scoring

After the evaluator result is frozen and the gold commitment is verified:

```text
CORRECT_IMPACT_ID = predicted ID is in locked gold closure
MISSED_IMPACT_ID = gold ID absent from prediction
FALSE_IMPACT_ID = predicted ID absent from gold closure
EXTERNAL_STANDARD_REVIEW_ERROR = yes/no differs from gold
```

Per form report:

```text
GOLD_IMPACT_INSTANCES:
CORRECT_IMPACT_INSTANCES:
MISSED_IMPACT_IDS:
FALSE_IMPACT_IDS:
EXTERNAL_STANDARD_REVIEW_ERRORS:
ELAPSED_TASK_TIME_SECONDS:
```

Aggregate route report:

```text
EVALUATOR_COUNT:
TOTAL_GOLD_IMPACT_INSTANCES:
TOTAL_MISSED_IMPACT_IDS:
TOTAL_FALSE_IMPACT_IDS:
TOTAL_EXTERNAL_STANDARD_REVIEW_ERRORS:
MEDIAN_ELAPSED_TASK_TIME_SECONDS:
MIN_ELAPSED_TASK_TIME_SECONDS:
MAX_ELAPSED_TASK_TIME_SECONDS:
```

If evaluator count is fewer than four, aggregate results remain exploratory.

## 9. Required result vector

The final benchmark must report:

```text
OUTCOME_ACCURACY_AXIS:
ERROR_OR_FALSE_POSITIVE_AXIS:
SOURCE_FIDELITY_AXIS:
EXTERNAL_STANDARD_BOUNDARY_AXIS:
STRUCTURAL_HANDOFF_AXIS:
REPRESENTATION_BURDEN_AXIS:
MEASURED_WORKLOAD_OR_TIME_AXIS:
REUSE_AXIS:
INDEPENDENCE_AXIS:
```

Inactive axes must be marked `not_measured` or `not_applicable`.

## 10. No scalar winner by default

```text
SCALAR_WINNER_REQUIRED: no
```

The benchmark may conclude `DSD_ADVANTAGE_ON_TIME_AXIS`, `BASELINE_ADVANTAGE_ON_TIME_AXIS`, `TIE_OR_OVERLAP`, `MIXED_RESULT`, or `INDETERMINATE`, but must not turn one axis into general practical superiority.

A time-axis descriptive direction may be stated only from actual human seconds. Error-axis direction may be stated only from actual frozen human outputs.

## 11. Gold-answer anti-leak discipline

The exact gold closures are not printed in reviewer packets.

Before any human run, a canonical answer sequence is committed by SHA-256 in a separate answer-commitment file.

```text
CANONICALIZATION:
  one line per change
  CASE_ID|sorted comma-separated impact IDs|EXTERNAL_STANDARD_REVIEW=yes/no
  ORBIT O-CH1..O-CH4 first
  HARBOR H-CH1..H-CH4 second
  LF separators
  no trailing newline
```

The hash must verify before the gold plaintext is used to score a frozen reviewer submission.

## 12. Stop condition

This turn prepares the benchmark but does not fabricate a human measurement.

```text
CURRENT_STAGE_COMPLETION:
  precommit
  reviewer packets
  answer hash commitment

HUMAN_RESULT:
  absent until a genuine human submission is frozen
```

## 13. Maturity effect before run

Preparation alone does not resolve the practical-benefit blocker.

```text
PRACTICAL_COMPARATIVE_BENCHMARKS_COMPLETED: remains 4
HUMAN_MEASUREMENT_BENCHMARKS_PREPARED: +1
MEASURED_HUMAN_TIME: not_established
POSITIVE_MEASURED_PRACTICAL_BENEFIT: not demonstrated
METHOD_EVIDENCE_STATUS: developing
PROTOCOL_V1_0_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```
