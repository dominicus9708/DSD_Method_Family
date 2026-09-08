# DES-CH-001 Precommit — Status-Sensitive Admissible Design Space

Status: **locked before case evaluation**  
Date: **2026-09-08**  
Evidence scope: `method_specific`  
Method directly tested: **DSD Design / DSD 설계론**  
Method protocol: **DSD Design Protocol v0.1**

## 1. Purpose / 목적

Test whether Protocol v0.1 can construct an admissible Design space from a finite exhaustive candidate family while preserving the difference between:

```text
DEFINED_ZERO
APPLICABLE_BUT_UNDEFINED
CHANNEL_ABSENCE
```

The challenge is intentionally positive: at least one candidate must be admissible if the protocol is applied correctly.

The case also tests that Design returns the admissible family without introducing a hidden Optimization step.

No task field, candidate, hard constraint, expected candidate classification, or pass criterion may be changed after this precommit is written. Any later change must be recorded as a new challenge version.

## 2. Frozen task record / 사전 동결 과업 레코드

```text
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
CANDIDATE_OR_CONSTRUCTION_BASIS: explicit finite candidate family T1-T4 below
CANDIDATE_GENERATION_RULE: enumerate T1-T4 exactly once in listed order
CANDIDATE_COVERAGE: exhaustive relative to this challenge task
DSD_INTERFACE_PROFILE: current project Formation + General Property interface used by Protocol v0.1
VALIDATION_OR_ACCEPTANCE_RULE: candidate is admissible iff H1-H4 are all satisfied at target resolution
DOMAIN_BRIDGE: not used
EXTERNAL_STANDARD: not used
AUXILIARY_METHODS_OR_HANDOFFS: none
NONOPTIMIZATION_SELECTION_RULE_IF_NEEDED: not used; return the complete covered admissible family
```

## 3. Frozen candidate family / 사전 동결 후보군

All candidates share:

```text
q_primary: admitted
```

The challenge-relevant difference is the reserve channel and its readiness property.

### T1 — admitted reserve + defined zero

```text
q_reserve: admitted
readiness(q_reserve): APPLICABLE, DEFINED_ZERO
```

Expected classification: `admissible`.

Reason: H1-H3 are satisfied and H4 explicitly allows defined zero.

### T2 — admitted reserve + defined nonzero

```text
q_reserve: admitted
readiness(q_reserve): APPLICABLE, DEFINED_NONZERO
```

Expected classification: `admissible`.

Reason: H1-H3 are satisfied; H4 does not prohibit nonzero values.

### T3 — admitted reserve + applicable but undefined

```text
q_reserve: admitted
readiness(q_reserve): APPLICABLE_BUT_UNDEFINED
```

Expected classification: `rejected`.

Expected rejection basis: H3 requires the readiness property to be defined.

### T4 — reserve channel absent

```text
q_reserve: CHANNEL_ABSENCE
readiness(q_reserve): not evaluated as a defined property on an admitted reserve channel
```

Expected classification: `rejected`.

Expected rejection basis: H2 requires q_reserve to be admitted.

## 4. Expected Design result / 예상 설계 결과

```text
ADMISSIBLE_TARGETS_OR_ADMISSIBLE_FAMILY: {T1, T2}
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

`T1` and `T2` are intentionally both admissible.
The protocol must not choose between them by preferring zero, nonzero, fewer states, or any other unstated objective.

## 5. Precommitted scoring / 사전 고정 점수

```text
CANDIDATES_TOTAL: 4
EXPECTED_ADMISSIBLE: 2
EXPECTED_REJECTED: 2

PASS_REQUIREMENT:
  T1 classified admissible: yes
  T2 classified admissible: yes
  T3 rejected specifically because applicable-but-undefined does not satisfy H3: yes
  T4 rejected specifically because channel absence does not satisfy H2: yes
  defined_zero is not collapsed into undefined: yes
  channel absence is not collapsed into defined_zero: yes
  returned design space is exactly {T1, T2}: yes
  hidden Optimization used: no
  terminal status = DESIGN_ADMISSIBLE: yes
  protocol conformance = CONFORMANT: yes
  method gain = NOT_ASSESSED: yes
```

Any mismatch in a required item is a challenge failure or protocol-conformance issue and must be recorded rather than repaired post hoc.

## 6. Activated and inactive DSD layers / 활성·비활성 층위

```text
FORMATION: active
GENERAL_PROPERTY: active
STATIC_AGGREGATION: inactive
DYNAMICS: inactive
OPTIONAL_SPECIALIZATION: inactive
```

No inactive layer may be introduced to rescue or strengthen the result.

## 7. Evidence limit / 증거 한계

This is a synthetic same-session positive constructed challenge.
A PASS, if obtained, is one direct pilot-level evidence item for DSD Design Protocol v0.1 only.

It is not:

```text
independent evaluator validation
external-domain validation
baseline superiority evidence
engineering usefulness evidence
method maturity evidence
```

Method gain must remain `NOT_ASSESSED` because this challenge contains no baseline comparison.