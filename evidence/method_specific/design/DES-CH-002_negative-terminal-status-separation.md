# DES-CH-002 — Negative Terminal-Status Separation

Status: **PASS — negative/failure constructed Design pilot under Protocol v0.1**  
Date: **2026-09-08**  
Evidence scope: `method_specific`  
Method directly tested: **DSD Design / DSD 설계론**  
Method protocol: **DSD Design Protocol v0.1**  
Precommit: `DES-CH-002_precommit.md`, commit `1c40630`

## 1. Evidence claim / 증거 주장

This challenge tests whether Protocol v0.1 preserves the distinction among three non-success terminal states:

```text
DESIGN_INFEASIBLE
DESIGN_UNDERDETERMINED
DESIGN_BLOCKED
```

The three task records, candidate-coverage labels, expected terminal statuses, and scoring criteria were frozen before evaluation.

No field was changed after precommit.

---

## 2. Case I execution — exhaustive no-solution

### Frozen state

```text
DESIGN_TASK_ID: DES-TASK-002-I
CLAIMED_OUTPUT_LEVEL: ADMISSIBLE_TARGET
CANDIDATE_COVERAGE: exhaustive relative to DES-TASK-002-I
CANDIDATES: I1,I2
```

Required constraints:

```text
H1 q_primary admitted
H2 q_reserve admitted
H3 readiness(q_reserve) applicable and defined
```

### Candidate I1

```text
q_primary: admitted
q_reserve: CHANNEL_ABSENCE
```

Evaluation:

```text
H1: pass
H2: fail
H3: not established on an admitted reserve channel
ADMISSIBILITY_RESULT: rejected
REJECTION_BASIS: H2
```

The channel absence is a direct hard-constraint violation, not a missing-search-space problem.

### Candidate I2

```text
q_primary: admitted
q_reserve: admitted
readiness(q_reserve): APPLICABLE_BUT_UNDEFINED
```

Evaluation:

```text
H1: pass
H2: pass
H3: fail
ADMISSIBILITY_RESULT: rejected
REJECTION_BASIS: H3
```

Applicable-but-undefined does not satisfy the requirement that readiness be defined.

### Case I terminal result

The frozen candidate universe is exhaustive and every candidate is rejected on an explicit hard constraint.

```text
ADMISSIBLE_TARGETS: {}
TERMINAL_DESIGN_STATUS: DESIGN_INFEASIBLE
TERMINAL_STATUS_BASIS: exhaustive I1-I2 universe evaluated; no candidate satisfies H1-H3
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

No impossibility theorem was needed because the declared challenge universe itself was exhaustively evaluated.

Case I: **PASS**.

---

## 3. Case U execution — non-exhaustive failure-to-find

### Frozen state

```text
DESIGN_TASK_ID: DES-TASK-002-U
CLAIMED_OUTPUT_LEVEL: ADMISSIBLE_TARGET
CANDIDATE_COVERAGE: non_exhaustive
EVALUATED_CANDIDATES: U1,U2
```

The declared generator `G_U` covers a larger symbolic family than the evaluated sample.
The stopping rule was frozen at the first two outputs.

### Candidate U1

```text
q_primary: admitted
q_reserve: CHANNEL_ABSENCE
```

Evaluation:

```text
H1: pass
H2: fail
H3: not established on an admitted reserve channel
ADMISSIBILITY_RESULT: rejected
REJECTION_BASIS: H2
```

### Candidate U2

```text
q_primary: admitted
q_reserve: admitted
readiness(q_reserve): APPLICABLE_BUT_UNDEFINED
```

Evaluation:

```text
H1: pass
H2: pass
H3: fail
ADMISSIBILITY_RESULT: rejected
REJECTION_BASIS: H3
```

### Case U terminal result

No admissible candidate was found in the evaluated sample, but the search was explicitly non-exhaustive.
Therefore the run has no justified global no-target conclusion.

```text
ADMISSIBLE_TARGETS_IN_EVALUATED_SAMPLE: {}
TERMINAL_DESIGN_STATUS: DESIGN_UNDERDETERMINED
TERMINAL_STATUS_BASIS: no admissible target found in non-exhaustive sample; global infeasibility unsupported
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The protocol did **not** assign `DESIGN_INFEASIBLE`.
This directly exercises the candidate-coverage guard.

Case U: **PASS**.

---

## 4. Case B execution — missing required predecessor

### Frozen state

```text
DESIGN_TASK_ID: DES-TASK-002-B
CLAIMED_OUTPUT_LEVEL: ADMISSIBLE_TARGET
TARGET_DSD_LAYER_SCOPE: Formation only
CANDIDATE: B1
REQUIRED_PREDECESSOR: P_B identity record
PREDECESSOR_STATUS: unavailable at run time
```

Hard constraints:

```text
H1 candidate q_legacy must match predecessor P_B identity
H2 q_reserve admitted
```

### Candidate B1

```text
q_legacy: placeholder reference to predecessor P_B identity
q_reserve: admitted
```

Evaluation:

```text
H1: blocked
  reason: P_B identity record is unavailable
H2: pass
ADMISSIBILITY_RESULT: blocked
```

No predecessor identity was invented.
The candidate was not rejected as though H1 were known false.
The missing dependency was recorded explicitly.

### Case B terminal result

```text
TERMINAL_DESIGN_STATUS: DESIGN_BLOCKED
TERMINAL_STATUS_BASIS: required predecessor identity is unavailable, so H1 cannot be validated without fabrication
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The case is not `DESIGN_INFEASIBLE`: no exhaustive rejection proof exists because the required validation input is missing.
It is not merely `DESIGN_UNDERDETERMINED`: the run is stopped by a specifically identified claim-required prerequisite.

Case B: **PASS**.

---

## 5. Cross-case separation / 교차 사례 구분

The same protocol therefore produces three different non-success outcomes from three different evidence states:

```text
EXHAUSTIVE + ALL CANDIDATES REJECTED
-> DESIGN_INFEASIBLE

NON_EXHAUSTIVE + NO ADMISSIBLE CANDIDATE FOUND
-> DESIGN_UNDERDETERMINED

CLAIM-REQUIRED PREDECESSOR UNAVAILABLE
-> DESIGN_BLOCKED
```

No Optimization was used.
No inactive DSD layer was introduced.
No neighboring-method verdict was added after lock.
Method gain remains `NOT_ASSESSED` in all three subcases because no baseline comparison was performed.

---

## 6. Protocol-conformance check / 프로토콜 준수 검사

Across all three subcases:

```text
POST_HOC_SOFT_TO_HARD_PROMOTION: no
UNDECLARED_CANDIDATE_BASIS_CHANGE: no
UNSUPPORTED_EXHAUSTIVENESS_CLAIM: no
INFEASIBLE_FROM_NONEXHAUSTIVE_FAILURE_TO_FIND: no
CLAIM_RELEVANT_STATUS_COLLAPSE: no
REQUIRED_BRIDGE_OMISSION: no
EXTERNAL_STANDARD_SUBSTITUTION: no
HIDDEN_OPTIMIZATION: no
NEIGHBORING_METHOD_VERDICT_ABSORPTION: no
UNRECORDED_TASK_REVISION: no
UNSUPPORTED_UNIQUENESS_CLAIM: no
```

`DESIGN_BLOCKED + CONFORMANT` is observed in Case B exactly as Protocol v0.1 permits: the run correctly exposes a missing dependency instead of fabricating it.

---

## 7. Precommitted scoring result / 사전 고정 점수 결과

```text
CASE_I_REQUIRED_CHECKS:
  I1 rejected specifically on H2: PASS
  I2 rejected specifically on H3: PASS
  exhaustive coverage preserved: PASS
  terminal status = DESIGN_INFEASIBLE: PASS
  protocol conformance = CONFORMANT: PASS

CASE_U_REQUIRED_CHECKS:
  U1 rejected specifically on H2: PASS
  U2 rejected specifically on H3: PASS
  non_exhaustive coverage preserved: PASS
  terminal status = DESIGN_UNDERDETERMINED: PASS
  unsupported DESIGN_INFEASIBLE claim made: PASS (none made)
  protocol conformance = CONFORMANT: PASS

CASE_B_REQUIRED_CHECKS:
  missing predecessor explicitly identified: PASS
  predecessor identity fabricated: PASS (none fabricated)
  B1 candidate status = blocked rather than rejected: PASS
  terminal status = DESIGN_BLOCKED: PASS
  protocol conformance = CONFORMANT: PASS

CROSS_CASE_REQUIRED_CHECKS:
  three terminal statuses remain distinct: PASS
  no hidden Optimization: PASS
  no inactive layer introduced: PASS
  method gain = NOT_ASSESSED in all three cases: PASS

PRECOMMITTED_REQUIRED_CHECKS: 20
PASSED: 20
FAILED: 0
CHALLENGE_VERDICT: PASS
```

---

## 8. Reproducibility / 재현성

```text
REPRODUCIBILITY_RECORD:
  protocol: methods/04_design/PROTOCOL_v0.1.md
  precommit: evidence/method_specific/design/DES-CH-002_precommit.md
  precommit_commit: 1c40630
  case_I_order: I1,I2
  case_U_order: U1,U2
  case_U_stopping_rule: first two frozen outputs only
  case_B_candidate: B1
  stochastic_generation: none
  task_revision_after_lock: none
  manual_candidate_addition_after_lock: none
  inactive_layer_activation_after_lock: none
  baseline_comparison: none
```

The case is deterministically retraceable from the frozen record at the declared symbolic resolution.

---

## 9. What this pilot directly supports / 직접 지지 범위

At pilot level, this case directly supports that Protocol v0.1 can:

1. issue `DESIGN_INFEASIBLE` only when the challenge's no-target claim has exhaustive support;
2. refuse to convert non-exhaustive failure-to-find into infeasibility;
3. classify a missing claim-required predecessor as `DESIGN_BLOCKED` without fabrication;
4. keep candidate rejection, search underdetermination, and missing-prerequisite blocking separate;
5. keep Design outcome, protocol conformance, and method gain in separate ledgers.

## 10. What this pilot does not support / 비지지 범위

This case does not establish:

```text
boundary robustness against neighboring methods under Protocol v0.1
NO_GAIN or baseline superiority
external-domain applicability
independent evaluator agreement
engineering or practical usefulness
method maturity
```

---

## 11. Evidence verdict / 증거 판정

```text
CASE_ID: DES-CH-002
CASE_CLASS: negative_or_failure
CASE_ORIGIN: constructed_same_session
PROTOCOL: v0.1
SUBCASE_I_STATUS: DESIGN_INFEASIBLE
SUBCASE_U_STATUS: DESIGN_UNDERDETERMINED
SUBCASE_B_STATUS: DESIGN_BLOCKED
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT for all three subcases
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
DIRECT_EVIDENCE_RESULT: PASS
DIRECT_CONSTRUCTED_PILOT_INCREMENT: +1
```

This is the second direct constructed Design pilot under Protocol v0.1 and the first negative/failure pilot.
