# DES-CH-004 Precommit — Corrected Design / Optimization Boundary

Status: **locked before case evaluation**  
Date: **2026-09-08**  
Evidence scope: `method_specific`  
Method directly tested: **DSD Design / DSD 설계론**  
Method protocol: **DSD Design Protocol v0.1**  
Prospective successor to: `DES-CH-003` challenge-design defect

## 1. Purpose / 목적

Test the Design/Optimization boundary with candidates that are materially distinct **inside the declared Design target resolution**.

This prospectively corrects the test-design defect exposed by `DES-CH-003` without modifying that historical case.

Locked boundary:

```text
DESIGN
  -> determine the admissible target/design family under hard constraints

OPTIMIZATION
  -> rank or choose among already admissible alternatives under an explicit objective
```

A downstream objective may be recorded as a handoff, but Design must not convert it into:

```text
an undeclared hard constraint
a hidden tie-breaker
a uniqueness proof
a Design verdict imported from Optimization
```

No task field, candidate, target-resolution field, objective value, expected status, or pass criterion may be changed after this precommit.

---

## 2. Shared frozen Design structure / 공통 동결 설계 구조

```text
TARGET_DSD_LAYER_SCOPE: Formation + General Property
TARGET_RESOLUTION:
  q_primary admission
  q_reserve admission
  readiness(q_reserve) definedness
  exact categorical value of reserve_mode(q_reserve)
```

Hard constraints:

```text
H1 q_primary is admitted
H2 q_reserve is admitted
H3 readiness(q_reserve) is applicable and defined
H4 reserve_mode(q_reserve) is applicable and defined
H5 reserve_mode(q_reserve) is one of {MODE_A, MODE_B, MODE_C}
```

All three reserve-mode values are equally allowed by Design hard constraints.
The mode value is part of the declared Design target resolution, so candidates with different mode values are materially distinct Design targets.

Downstream-only objective:

```text
OPTIMIZATION_OBJECTIVE: minimize resource_cost
```

`resource_cost` is supplied only for the prospective downstream Optimization handoff and is not a Design hard constraint.

---

## 3. Frozen candidate family / 사전 동결 후보군

### C1

```text
q_primary: admitted
q_reserve: admitted
readiness(q_reserve): APPLICABLE, DEFINED_NONZERO
reserve_mode(q_reserve): APPLICABLE, DEFINED value MODE_A
resource_cost: 30
```

Expected Design classification: `admissible`.

### C2

```text
q_primary: admitted
q_reserve: admitted
readiness(q_reserve): APPLICABLE, DEFINED_NONZERO
reserve_mode(q_reserve): APPLICABLE, DEFINED value MODE_B
resource_cost: 20
```

Expected Design classification: `admissible`.

### C3

```text
q_primary: admitted
q_reserve: admitted
readiness(q_reserve): APPLICABLE, DEFINED_NONZERO
reserve_mode(q_reserve): APPLICABLE, DEFINED value MODE_C
resource_cost: 10
```

Expected Design classification: `admissible`.

Frozen distinction statement:

```text
C1 != C2 != C3 at TARGET_RESOLUTION
because reserve_mode values MODE_A, MODE_B, MODE_C are explicitly represented.
```

If a downstream Optimization run were later executed under the frozen objective, `C3` would rank best by `resource_cost`.
That fact is a boundary pressure point only; Optimization is not executed inside this Design evidence case.

---

## 4. Case S — DESIGN_SPACE boundary

```text
DESIGN_TASK_ID: DES-TASK-004-S
PROTOCOL_VERSION: v0.1
TASK_SCOPE: return the full admissible Design family at the declared target resolution without objective-based ranking
CLAIMED_OUTPUT_LEVEL: DESIGN_SPACE
GOALS:
  G1 preserve q_primary
  G2 require q_reserve
  G3 require defined readiness
  G4 require one explicitly defined reserve_mode
HARD_CONSTRAINTS: H1-H5 above
CONSTRAINT_SOURCE_OR_SPECIFICATION: challenge task owner
SOFT_PREFERENCES: none
BASE_STRUCTURE_OR_PREDECESSOR: none; new symbolic target family
TARGET_DSD_LAYER_SCOPE: Formation + General Property
TARGET_RESOLUTION: as frozen in Section 2
CANDIDATE_OR_CONSTRUCTION_BASIS: explicit finite family C1-C3
CANDIDATE_GENERATION_RULE: enumerate C1-C3 exactly once in listed order
CANDIDATE_COVERAGE: exhaustive relative to DES-TASK-004-S
DSD_INTERFACE_PROFILE: current project Formation + General Property interface used by Protocol v0.1
VALIDATION_OR_ACCEPTANCE_RULE: candidate is Design-admissible iff H1-H5 all pass
DOMAIN_BRIDGE: not used
EXTERNAL_STANDARD: not used
AUXILIARY_METHODS_OR_HANDOFFS:
  downstream DSD Optimization may consume {C1,C2,C3} plus resource_cost objective; Optimization not executed here
NONOPTIMIZATION_SELECTION_RULE_IF_NEEDED: not used
```

Expected:

```text
ADMISSIBLE_TARGETS_OR_ADMISSIBLE_FAMILY: {C1,C2,C3}
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
HIDDEN_OPTIMIZATION: no
DESIGN_SELECTED_SINGLE_BEST_TARGET: no
```

---

## 5. Case U — UNIQUE_TARGET boundary

```text
DESIGN_TASK_ID: DES-TASK-004-U
PROTOCOL_VERSION: v0.1
TASK_SCOPE: determine whether the Design task itself establishes one unique target at the declared resolution
CLAIMED_OUTPUT_LEVEL: UNIQUE_TARGET
GOALS: G1-G4 above
HARD_CONSTRAINTS: H1-H5 above
CONSTRAINT_SOURCE_OR_SPECIFICATION: challenge task owner
SOFT_PREFERENCES: none
BASE_STRUCTURE_OR_PREDECESSOR: none; new symbolic target family
TARGET_DSD_LAYER_SCOPE: Formation + General Property
TARGET_RESOLUTION: as frozen in Section 2
CANDIDATE_OR_CONSTRUCTION_BASIS: explicit finite family C1-C3
CANDIDATE_GENERATION_RULE: enumerate C1-C3 exactly once in listed order
CANDIDATE_COVERAGE: exhaustive relative to DES-TASK-004-U
DSD_INTERFACE_PROFILE: current project Formation + General Property interface used by Protocol v0.1
VALIDATION_OR_ACCEPTANCE_RULE: candidate is Design-admissible iff H1-H5 all pass
DOMAIN_BRIDGE: not used
EXTERNAL_STANDARD: not used
AUXILIARY_METHODS_OR_HANDOFFS:
  downstream DSD Optimization may rank {C1,C2,C3} by resource_cost; Optimization not executed here
NONOPTIMIZATION_SELECTION_RULE_IF_NEEDED: none supplied
```

Expected:

```text
ADMISSIBLE_TARGETS_OR_ADMISSIBLE_FAMILY: {C1,C2,C3}
UNRESOLVED_FIELDS:
  unique selection among MODE_A / MODE_B / MODE_C is not determined by Design hard constraints
TERMINAL_DESIGN_STATUS: DESIGN_UNDERDETERMINED
TERMINAL_STATUS_BASIS: UNIQUE_TARGET requested while three materially distinct Design-admissible targets remain; only downstream objective ranks them
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
HIDDEN_OPTIMIZATION: no
UNSUPPORTED_UNIQUENESS_CLAIM: no
```

Design must not claim `C3` as the unique Design target merely because its downstream `resource_cost` is smallest.

---

## 6. Precommitted scoring / 사전 고정 점수

```text
CASE_S_REQUIRED_CHECKS:
  C1 Design-admissible: yes
  C2 Design-admissible: yes
  C3 Design-admissible: yes
  C1/C2/C3 remain distinct at target resolution: yes
  returned Design family exactly {C1,C2,C3}: yes
  single best target selected by Design: no
  resource_cost promoted to hard constraint: no
  handoff to Optimization recorded: yes
  Optimization executed inside Design case: no
  terminal status = DESIGN_ADMISSIBLE: yes
  protocol conformance = CONFORMANT: yes

CASE_U_REQUIRED_CHECKS:
  C1 Design-admissible: yes
  C2 Design-admissible: yes
  C3 Design-admissible: yes
  C1/C2/C3 remain distinct at target resolution: yes
  UNIQUE_TARGET=C3 claimed by Design: no
  resource_cost used as hidden tie-breaker: no
  terminal status = DESIGN_UNDERDETERMINED: yes
  unresolved uniqueness basis explicitly recorded: yes
  protocol conformance = CONFORMANT: yes

CROSS_CASE_REQUIRED_CHECKS:
  Design admissibility and Optimization ranking remain distinct: yes
  neighboring-method verdict absorption: no
  method gain = NOT_ASSESSED in both cases: yes
  no inactive DSD layer introduced: yes

PRECOMMITTED_REQUIRED_CHECKS: 23
PASS_REQUIREMENT: 23/23
```

Any mismatch must be recorded rather than repaired post hoc.

---

## 7. Evidence limit / 증거 한계

This is a synthetic same-session boundary constructed challenge.
A PASS, if obtained, is one successful direct boundary evidence item for DSD Design Protocol v0.1 only.

It does not validate DSD Optimization itself because Optimization is not executed here.
It tests whether Design preserves the boundary stated by the current method-family architecture.

It is not:

```text
independent evaluator validation
external-domain validation
baseline superiority evidence
engineering usefulness evidence
Optimization method validation
method maturity evidence
```
