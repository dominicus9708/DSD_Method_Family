# SC-08 — Baseline / Failure-NO_GAIN / Anti-Post-Hoc Discipline / 기준선·실패·무이득·사후변경 방지 규율 검증

Status: **promoted_with_conditions**  
Date: 2026-09-06  
Evidence scope: `shared_method_family`  
Case origin: `constructed_benchmark`

## 1. Result / 결과

`Baseline / Failure-NO_GAIN / Anti-Post-Hoc Discipline` is promoted as a **conditional shared-core evaluation rule**.

A representative method from each of the eight higher-level fields was tested against three evaluation-integrity perturbations:

- `SB`: strawman-baseline substitution — a known stronger task-matched baseline is omitted or replaced by a weaker comparator so that an apparent advantage is manufactured;
- `NR`: negative-result rescue/erasure — a locked `FAIL`, `PARTIAL`, `NO_GAIN`, `TIE`, `BASELINE_PREFERRED`, or `INDETERMINATE` outcome is deleted, relabeled, or excluded because it is unfavorable;
- `PH`: post-reveal criterion/exception editing — scoring rules, thresholds, weights, exclusions, or exceptions are changed after result reveal and then applied retroactively to the same run without versioning and re-test.

```text
STRAWMAN_BASELINE_SUBSTITUTION_CHECKS: 8/8 detected
NEGATIVE_RESULT_RESCUE_OR_ERASURE_CHECKS: 8/8 detected
POST_REVEAL_CRITERION_OR_EXCEPTION_EDIT_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
SHARED_CORE_PROMOTION_RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
```

Invariant meaning:

> When a DSD method makes a comparative, superiority, gain, performance, or locked success claim, evaluate it against the strongest reasonable task-matched baseline available under the declared comparison scope; preserve unfavorable, null, tied, and indeterminate outcomes as legitimate records; and do not retroactively alter locked criteria after reveal to rescue the same run. Revisions are allowed only as explicit new versions applied prospectively or to a separately recorded rerun.

SC-08 does **not** require a baseline for every descriptive task, and it does not prohibit exploratory criterion development. It restricts what may be claimed from a run after its evaluation conditions have been exposed to the result.

## 2. Source basis / 소스 근거

SC-08 is an operating/evidence discipline extracted primarily from existing DSD Analysis challenge records rather than from one foundational axiom clause.

### ANL-CH-003 — DSD Null / No-Gain

The challenge explicitly permits

```text
CORRESPONDENCE_RESULT: direct
BASELINE_SUFFICIENCY: sufficient
ANALYTICAL_GAIN: none
```

and treats the simpler external baseline as preferable when DSD adds no result, error detection, or structural distinction. The pass condition is correct recognition of `NO_GAIN`, not manufactured usefulness.

### ANL-CH-007 — Competing Explanation

The comparison is locked to the **strongest reasonable task-matched baseline**, not a weak scalar-only strawman. DSD is allowed to lose or tie. In both pilot cases, a stronger external baseline removed an apparent DSD advantage and the record preserved `baseline_preferred`.

### ANL-CH-008 — Unseen-Problem Transfer

Rules are locked before reveal. Post-reveal rule changes and added exceptions are explicit failure-sensitive fields. The challenge states that if a rule modification becomes necessary, the prior failure should be preserved and the revised rule versioned instead of rewriting history.

### ANL-CH-009 — Reverse Prediction

Directional predictions are committed before reveal. A mismatch must remain a `prediction_miss`; the original prediction is not rewritten. The completed record preserves the precommit commit and separately records that no post-reveal edit or exception was added.

Together these records support a domain-independent evaluation principle:

```text
strong baseline where a comparative claim is made
+ unfavorable/null outcome preservation
+ time-ordered rule/criterion lock
```

Existing Analysis evidence supports this shared rule but does not directly validate receiving methods.

## 3. Locked evaluation scaffold / 고정 평가 scaffold

For each representative method `M`, declare a task with three target obligations and two external baselines.

```text
TARGET_OBLIGATIONS: O1, O2, O3

B_weak:
  TARGET_FIT = 1/3

B_strong:
  TARGET_FIT = 3/3

M:
  TARGET_FIT = 3/3
  NOVEL_DISCRIMINATION_OVER_B_strong = none
```

For a superiority/gain claim, the locked interpretation is:

```text
WEAK_BASELINE_RESULT: M appears superior to B_weak
STRONG_BASELINE_RESULT: target-fit tie with B_strong
GAIN_OVER_STRONGEST_REASONABLE_BASELINE: none
CORRECT_EVALUATION: NO_GAIN or TIE
```

A separate failure-sensitive variant is also locked:

```text
PASS_THRESHOLD: 3/3 obligations
OBSERVED_M_FAIL_VARIANT: 2/3
CORRECT_RESULT: FAIL_or_PARTIAL_according_to_locked_vocabulary
```

The exact method-specific output differs by field, but the evaluation obligations remain the same.

## 4. Perturbations / 교란 연산

### SB — Strawman-baseline substitution

A known task-matched `B_strong` is available but is silently omitted, and only `B_weak` is used to support a superiority or gain claim.

Invalid transformation:

```text
M > B_weak
therefore M has positive gain
```

when the locked comparison set also contains

```text
M = B_strong
```

on the target obligations.

### NR — Negative-result rescue or erasure

Apply any of the following after scoring:

```text
NO_GAIN -> useful/pass
TIE -> DSD_preferred
BASELINE_PREFERRED -> omitted
FAIL -> partial_pass without locked rule
INDETERMINATE -> pass
failed case -> removed from denominator without predeclared exclusion rule
```

The original outcome must instead remain in the record.

### PH — Post-reveal criterion or exception editing

After observing `2/3` under a locked `PASS_THRESHOLD: 3/3`, change the threshold to `2/3`, alter weights, add a case-specific exception, or redefine the success vocabulary and then claim that the original run passed.

A legitimate revision requires a new version identifier and may be tested prospectively or through a separately recorded rerun. It cannot silently rewrite the already-revealed record.

## 5. Eight-field transfer test / 8개 상위 분야 교차 시험

| Field | Representative method | SB: weak-baseline substitution | NR: unfavorable result rescue | PH: post-reveal edit | Result |
|---|---|---|---|---|---|
| I. Structural Description & Understanding | Comparison | compare only against a lossy comparator while a structure-preserving comparator is available | tie/no-gain is rewritten as DSD-preferred | comparison criteria are changed after seeing which side wins | PASS: 3/3 detected |
| II. Criteria & Validation | Audit | audit is compared only against a minimal checklist while a competent fault-detection checklist is available | missed fault or `NO_GAIN` is removed from the audit verdict | pass criteria or exclusion rules are relaxed after fault reveal | PASS: 3/3 detected |
| III. Construction & Transformation | Design | DSD design is compared only with an intentionally under-constrained design rather than a competent constraint-matched design | equal target fit is reported as design gain or an infeasible design failure is omitted | design success constraints are relaxed after candidate evaluation | PASS: 3/3 detected |
| IV. Evidence & Lineage | Measurement | measurement procedure is compared only with an uncalibrated weak procedure while a calibrated reference is available | no improvement, failed calibration, or indeterminate reading is discarded | tolerance or acceptance interval is widened after observing the measurement | PASS: 3/3 detected |
| V. Reduction & Representation | Compression | compression is compared only with a poor baseline while a task-matched codec/representation is available | tie, worse distortion, or negative information-loss result is hidden | distortion/retention metric is changed after encoded outputs are inspected | PASS: 3/3 detected |
| VI. Inverse Inference & Reconstruction | Diagnosis | diagnosis is compared only with a weak rule while a competent task-matched diagnostic baseline is available | diagnostic miss/indeterminate/no-gain is relabeled as useful support | diagnostic threshold or exception is changed after true labels/outcomes are revealed | PASS: 3/3 detected |
| VII. Computation & Selection | Optimization | optimization is compared only with a naive candidate while a strong incumbent/search baseline is available | equal objective value or worse solution is omitted so positive gain appears | objective weights or stopping/success threshold are changed after results are known | PASS: 3/3 detected |
| VIII. Dynamics & Action | Prediction | prediction is compared only with a weak forecast while a competent reference forecast is available | prediction miss/tie/no-gain is removed or rescued | scoring window, tolerance, or exception is changed after outcomes are revealed | PASS: 3/3 detected |

This table tests transfer of the evaluation rule only. It is not direct validation of the eight representative methods as complete methodologies.

## 6. Negative controls / 음성 대조군

SC-08 is deliberately conditional.

1. **Purely descriptive/non-comparative task:** if no superiority, performance, novelty, or gain claim is made, a competitive baseline is not mandatory merely to perform the method.
2. **No competent baseline exists:** record `BASELINE_STATUS: unavailable_or_unknown` and narrow the claim. Do not invent a weak comparator merely to claim superiority.
3. **Exploratory criterion development:** criteria may change after inspecting data when the work is explicitly exploratory, but the same exposed run cannot then be represented as confirmatory validation under the revised criteria.
4. **Legitimate protocol correction:** if a factual bug or invalid input is discovered, preserve the original record, document the correction, issue a new protocol/version, and rerun or re-score transparently.
5. **Genuine win over a strong baseline:** `dsd_preferred` is allowed when the strongest reasonable baseline was fairly selected and the locked criteria support the result.
6. **Negative/null outcomes are not all identical:** `FAIL`, `PARTIAL`, `NO_GAIN`, `TIE`, `BASELINE_PREFERRED`, and `INDETERMINATE` remain separate when the task vocabulary distinguishes them.

Therefore SC-08 is not “always use a baseline” and not “never revise criteria.” It is:

> **Do not manufacture advantage by comparator choice, unfavorable-result deletion, or retroactive scoring changes.**

## 7. Standard evaluation-integrity record / 표준 평가 무결성 기록

```text
EVALUATION_RECORD_ID:
METHOD_UNDER_TEST:
TASK:
CLAIM_TYPE: descriptive / comparative / superiority / gain / performance / prediction

BASELINE_REQUIRED: yes / no
BASELINE_SET:
STRONGEST_REASONABLE_BASELINE:
BASELINE_SELECTION_RATIONALE:
BASELINE_SELECTION_LOCK:
STRAW_MAN_BASELINE_AVOIDED: yes / no / not_applicable

PRECOMMITTED_CRITERIA:
PASS_CRITERIA:
FAILURE_CRITERIA:
NO_GAIN_CRITERIA:
INDETERMINATE_CRITERIA:
PRECOMMIT_STATUS:
PRECOMMIT_ID_OR_COMMIT:

OBSERVED_RESULT:
COMPETITIVE_RESULT: dsd_preferred / baseline_preferred / tie / indeterminate / not_applicable
ANALYTICAL_OR_TASK_GAIN: positive / limited / none / negative / not_applicable
NEGATIVE_OR_NULL_OUTCOME_PRESERVED: yes / no / not_applicable
EXCLUDED_CASES_AND_PREDECLARED_RULE:

POST_REVEAL_RULE_CHANGE: none / declared_revision
POST_REVEAL_EXCEPTION_ADDED: none / declared_revision
REVISED_PROTOCOL_VERSION:
REVISION_APPLIES_TO: future_runs_only / separately_recorded_rerun / not_applicable
ORIGINAL_RECORD_PRESERVED: yes / no
```

## 8. Promotion test / 승격 시험

```text
SOURCE_SUPPORT: pass
SAME_SEMANTIC_MEANING_ACROSS_METHODS: pass_with_conditional_activation
STRAWMAN_BASELINE_SUBSTITUTION_COUNTEREXAMPLE: pass
NEGATIVE_RESULT_RESCUE_OR_ERASURE_COUNTEREXAMPLE: pass
POST_REVEAL_CRITERION_OR_EXCEPTION_EDIT_COUNTEREXAMPLE: pass
NON_TRANSFER_CASE_IDENTIFIED: pass
METHOD_TASK_REDEFINITION: none
DIRECT_VALIDATION_SEPARATION: pass
SHARED_CORE_PROMOTION_RESULT: promoted_with_conditions
```

## 9. Transfer conditions / 적용 조건

Apply the relevant SC-08 clauses when:

- a method makes a superiority, gain, novelty, performance, error-reduction, efficiency, or predictive-quality claim;
- a PASS/FAIL/NO_GAIN/TIE/INDETERMINATE-style evaluative verdict is recorded;
- scoring criteria, thresholds, exclusions, predictions, or rules can be fixed before reveal and the result is intended as confirmatory evidence;
- baseline choice could materially change the claimed advantage.

The baseline clause is inactive for a genuinely non-comparative descriptive task, while failure/no-gain preservation and anti-post-hoc clauses activate only when their corresponding evaluative structure exists.

## 10. Evidence limits / 한계

- This is a synthetic cross-field evaluation-integrity pilot.
- Its source support is mainly the existing Analysis challenges CH-003, CH-007, CH-008, and CH-009 plus the current DSD evidence architecture.
- One representative method per higher-level field was tested.
- The external baselines in this SC-08 scaffold are constructed controls, not independently selected domain standards.
- It does not validate the overall correctness, performance, or usefulness of all 22 methods.
- Independent real-domain benchmark selection, preregistration, and external holdout evaluation remain future evidence work.

## 11. Relation to SC-01–SC-07 / SC-01~07과의 관계

```text
SC-01 = preserve claim-relevant status/typed distinctions
SC-02 = lock source/interface/version semantics
SC-03 = make cross-structure bridges explicit
SC-04 = restrain dependencies to claim-relevant layers
SC-05 = respect information-loss/reconstruction limits
SC-06 = distinguish regular evolution, transition, and lineage
SC-07 = separate evidence applicability from case origin
SC-08 = preserve evaluation integrity across baseline choice, unfavorable outcomes, and reveal-time criterion changes
```

The eight rules are complementary but non-identical.

## 12. Remaining shared-core candidates / 남은 공통 구조 후보

SC-08 completes the previously grouped baseline/failure-no-gain/anti-post-hoc candidate, but it does **not** exhaust every candidate in the registry.

A remaining candidate is:

- **Evidence-status versus DSD-object-status separation** — whether `undefined`, `inapplicable`, `defined_zero`, etc. on the DSD object side remain distinct from `supported`, `insufficient_evidence`, `unverified`, `contradicted`, etc. on the evidence side.

This should be tested separately rather than silently absorbed into SC-08.
