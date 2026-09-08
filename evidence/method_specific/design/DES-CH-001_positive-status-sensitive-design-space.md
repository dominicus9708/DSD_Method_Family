# DES-CH-001 — Positive Status-Sensitive Admissible Design Space

Status: **PASS — first direct constructed Design pilot under Protocol v0.1**  
Date: **2026-09-08**  
Evidence scope: `method_specific`  
Method directly tested: **DSD Design / DSD 설계론**  
Method protocol: **DSD Design Protocol v0.1**  
Precommit: `DES-CH-001_precommit.md`, commit `f82a333`

## 1. Evidence claim / 증거 주장

This challenge tests whether Protocol v0.1 can return an admissible design family from a pre-frozen exhaustive candidate set while preserving claim-relevant DSD status distinctions and avoiding hidden Optimization.

The frozen candidate family and pass criteria were committed before case evaluation.

## 2. Frozen task record / 동결 과업 레코드

```text
DESIGN_RESULT_ID: DES-CH-001-R1
DESIGN_TASK_ID: DES-TASK-001
PROTOCOL_VERSION: v0.1
TASK_SCOPE: construct the admissible two-channel readiness design space at the declared symbolic resolution
CLAIMED_OUTPUT_LEVEL: DESIGN_SPACE
GOALS:
  G1 preserve a primary operational channel q_primary
  G2 provide a reserve operational channel q_reserve
  G3 require an explicit defined readiness property for q_reserve
HARD_CONSTRAINTS:
  H1 q_primary is admitted
  H2 q_reserve is admitted
  H3 readiness(q_reserve) is applicable and defined
  H4 readiness(q_reserve) = 0 is allowed and must not be treated as undefined or absent
CONSTRAINT_SOURCE_OR_SPECIFICATION: challenge task owner; no upstream Specification run
SOFT_PREFERENCES: none
BASE_STRUCTURE_OR_PREDECESSOR: none; new symbolic target family
TARGET_DSD_LAYER_SCOPE: Formation + General Property
TARGET_RESOLUTION: admitted/absent channel status plus readiness property status; no geometry, magnitude semantics, aggregation, or dynamics
CANDIDATE_OR_CONSTRUCTION_BASIS: explicit finite candidate family T1-T4
CANDIDATE_GENERATION_RULE: enumerate T1-T4 exactly once in listed order
CANDIDATE_COVERAGE: exhaustive relative to this challenge task
DSD_INTERFACE_PROFILE: current project Formation + General Property interface used by Protocol v0.1
VALIDATION_OR_ACCEPTANCE_RULE: candidate is admissible iff H1-H4 are all satisfied at target resolution
DOMAIN_BRIDGE: not used
EXTERNAL_STANDARD: not used
AUXILIARY_METHODS_OR_HANDOFFS: none
NONOPTIMIZATION_SELECTION_RULE_IF_NEEDED: not used; return the complete covered admissible family
```

No task field was changed after precommit.

## 3. Protocol execution / 프로토콜 실행

### D1 — Lock task and claim

PASS.

The task, output level, goals, hard constraints, and target resolution were frozen before evaluation.

### D2 — Lock constraint sources

PASS.

All hard constraints are challenge-task constraints. No upstream Specification or external standard is claimed.

No soft preference exists, so no soft-to-hard promotion can occur.

### D3 — Lock candidate basis and coverage

PASS.

The candidate basis is the explicit finite family `{T1,T2,T3,T4}` and is exhaustive relative to the challenge task.

### D4 — Lock interfaces and bridges

PASS.

```text
FORMATION: active
GENERAL_PROPERTY: active
STATIC_AGGREGATION: inactive
DYNAMICS: inactive
OPTIONAL_SPECIALIZATION: inactive
DOMAIN_BRIDGE: not used
```

No inactive layer or bridge was introduced during scoring.

### D5 — Construct / enumerate candidates

PASS.

Candidates were evaluated exactly once in the frozen order `T1 -> T2 -> T3 -> T4`.

### D6 — Status-sensitive admissibility checks

Candidate results follow.

#### T1 — admitted reserve + defined zero

```text
q_primary: admitted
q_reserve: admitted
readiness(q_reserve): APPLICABLE, DEFINED_ZERO
```

Check:

```text
H1: pass
H2: pass
H3: pass
H4: pass
ADMISSIBILITY_RESULT: admissible
```

`DEFINED_ZERO` is a defined state and H4 explicitly permits zero.
It is not collapsed into `APPLICABLE_BUT_UNDEFINED` or `CHANNEL_ABSENCE`.

#### T2 — admitted reserve + defined nonzero

```text
q_primary: admitted
q_reserve: admitted
readiness(q_reserve): APPLICABLE, DEFINED_NONZERO
```

Check:

```text
H1: pass
H2: pass
H3: pass
H4: pass
ADMISSIBILITY_RESULT: admissible
```

H4 permits zero but does not require zero, so the defined nonzero state remains admissible.

#### T3 — admitted reserve + applicable but undefined

```text
q_primary: admitted
q_reserve: admitted
readiness(q_reserve): APPLICABLE_BUT_UNDEFINED
```

Check:

```text
H1: pass
H2: pass
H3: fail
H4: not needed to rescue H3
ADMISSIBILITY_RESULT: rejected
REJECTION_BASIS: H3 requires readiness(q_reserve) to be defined
```

The undefined property state was not zero-padded into `DEFINED_ZERO`.

#### T4 — reserve channel absent

```text
q_primary: admitted
q_reserve: CHANNEL_ABSENCE
readiness(q_reserve): not evaluated as a defined property on an admitted reserve channel
```

Check:

```text
H1: pass
H2: fail
H3: not established on an admitted reserve channel
H4: not applicable as a rescue rule
ADMISSIBILITY_RESULT: rejected
REJECTION_BASIS: H2 requires q_reserve to be admitted
```

Channel absence was not treated as an admitted channel with zero readiness.

### D7 — Domain / external / auxiliary checks

PASS as inactive.

No external standard, domain bridge, Synthesis, Transformation, Optimization, or other substantive neighboring-method verdict was required.

### D8 — Construct admissible family

```text
ADMISSIBLE_TARGETS_OR_ADMISSIBLE_FAMILY: {T1, T2}
REJECTED_CANDIDATES: {T3, T4}
```

PASS.

### D9 — Check claimed output level

The frozen output claim is `DESIGN_SPACE`.

The protocol therefore returns the complete admissible family within the declared exhaustive challenge space:

```text
{T1, T2}
```

No uniqueness or optimality claim is made.

PASS.

### D10 — Assign terminal Design status

```text
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
TERMINAL_STATUS_BASIS: at least one admissible target exists; exact returned family is {T1,T2}
```

PASS.

### D11 — Record protocol conformance

```text
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
```

No recorded nonconformance condition occurred:

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

PASS.

### D12 — Record method gain

```text
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
BASELINE_IF_GAIN_ASSESSED: not used
GAIN_CRITERION_IF_ASSESSED: not used
```

No baseline comparison was performed, so neither `GAIN_ESTABLISHED` nor `NO_GAIN` is asserted.

PASS.

### D13 — Limits and reproducibility

```text
REPRODUCIBILITY_RECORD:
  protocol: methods/04_design/PROTOCOL_v0.1.md
  precommit: evidence/method_specific/design/DES-CH-001_precommit.md
  precommit_commit: f82a333
  candidate_order: T1,T2,T3,T4
  stochastic_generation: none
  manual_candidate_addition_after_lock: none
  external_data: none
  external_standard: none
  inactive_layers_added_after_lock: none
```

The case is deterministically retraceable from the frozen record.

## 4. Precommitted scoring result / 사전 고정 점수 결과

```text
CANDIDATES_TOTAL: 4/4 evaluated
EXPECTED_ADMISSIBLE: 2/2 matched
EXPECTED_REJECTED: 2/2 matched

T1 classified admissible: PASS
T2 classified admissible: PASS
T3 rejected specifically on H3: PASS
T4 rejected specifically on H2: PASS
defined_zero not collapsed into undefined: PASS
channel absence not collapsed into defined_zero: PASS
returned design space exactly {T1,T2}: PASS
hidden Optimization used: PASS (none used)
terminal status = DESIGN_ADMISSIBLE: PASS
protocol conformance = CONFORMANT: PASS
method gain = NOT_ASSESSED: PASS

PRECOMMITTED_REQUIRED_CHECKS: 11
PASSED: 11
FAILED: 0
CHALLENGE_VERDICT: PASS
```

## 5. What this pilot directly supports / 직접 지지 범위

This case directly supports, at pilot level, that Protocol v0.1 can:

1. execute a pre-frozen `DESIGN_SPACE` task;
2. preserve `DEFINED_ZERO` versus `APPLICABLE_BUT_UNDEFINED` versus `CHANNEL_ABSENCE` when those distinctions control admissibility;
3. return more than one admissible target without converting the task into Optimization;
4. keep Design outcome, protocol conformance, and method gain in separate ledgers;
5. preserve rejected-candidate reasons and a deterministic retrace path.

## 6. What this pilot does not support / 비지지 범위

This case does not establish:

```text
negative/failure-case handling across all terminal statuses
infeasibility discipline under an exhaustive no-solution case
boundary robustness under the executable protocol
NO_GAIN or baseline superiority
external-domain applicability
independent evaluator agreement
engineering or practical usefulness
method maturity
```

## 7. Evidence verdict / 증거 판정

```text
CASE_ID: DES-CH-001
CASE_CLASS: positive
CASE_ORIGIN: constructed_same_session
PROTOCOL: v0.1
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
DIRECT_EVIDENCE_RESULT: PASS
DIRECT_CONSTRUCTED_PILOT_INCREMENT: +1
```

This is the first direct constructed Design pilot under Protocol v0.1.