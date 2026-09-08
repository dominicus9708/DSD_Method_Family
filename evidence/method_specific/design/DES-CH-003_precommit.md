# DES-CH-003 Precommit — Design / Optimization Boundary

Status: **locked before case evaluation**  
Date: **2026-09-08**  
Evidence scope: `method_specific`  
Method directly tested: **DSD Design / DSD 설계론**  
Method protocol: **DSD Design Protocol v0.1**  
Boundary reference: `methods/METHOD_BOUNDARY_MATRIX.md`; `methods/12_computation_optimization/optimization/README.md`

## 1. Purpose / 목적

Test whether Protocol v0.1 preserves the boundary between Design and Optimization when:

1. multiple candidates satisfy every Design hard constraint; and
2. an explicit downstream objective can rank those admissible candidates.

The locked boundary is:

```text
DESIGN
  -> construct/filter the admissible target family under hard constraints

OPTIMIZATION
  -> choose/rank among an already justified admissible family under an explicit objective
```

The existence of an objective in the wider workflow does **not** authorize Design to use that objective as a hidden hard constraint, tie-breaker, or uniqueness proof.

No task field, candidate, objective value, expected terminal status, or pass criterion may be changed after this precommit is written.
Any later revision must be recorded as a new challenge version.

---

## 2. Shared frozen candidate family / 공통 사전 동결 후보군

All candidates use the same Design-relevant hard constraints.
The numerical `resource_cost` values are supplied only as a downstream Optimization input and are **not** Design hard constraints.

```text
TARGET_DSD_LAYER_SCOPE: Formation + General Property
TARGET_RESOLUTION: q_primary/q_reserve channel admission + readiness(q_reserve) definedness

HARD_CONSTRAINTS:
  H1 q_primary is admitted
  H2 q_reserve is admitted
  H3 readiness(q_reserve) is applicable and defined

DOWNSTREAM_OPTIMIZATION_OBJECTIVE:
  minimize resource_cost

DESIGN_USE_OF_RESOURCE_COST:
  prohibited except as recorded handoff metadata
```

### O1

```text
q_primary: admitted
q_reserve: admitted
readiness(q_reserve): APPLICABLE, DEFINED_NONZERO
resource_cost: 30
```

Expected Design classification: `admissible`.

### O2

```text
q_primary: admitted
q_reserve: admitted
readiness(q_reserve): APPLICABLE, DEFINED_NONZERO
resource_cost: 20
```

Expected Design classification: `admissible`.

### O3

```text
q_primary: admitted
q_reserve: admitted
readiness(q_reserve): APPLICABLE, DEFINED_NONZERO
resource_cost: 10
```

Expected Design classification: `admissible`.

If Optimization were later executed under the stated objective, `O3` would rank best by cost.
That downstream ranking fact is frozen as a boundary pressure point, but **Optimization is not executed as part of this Design evidence case**.

---

## 3. Case S — DESIGN_SPACE must stop before Optimization

### Frozen task record

```text
DESIGN_TASK_ID: DES-TASK-003-S
PROTOCOL_VERSION: v0.1
TASK_SCOPE: return the admissible reserve-channel Design space without ranking admissible alternatives
CLAIMED_OUTPUT_LEVEL: DESIGN_SPACE
GOALS:
  G1 preserve q_primary
  G2 require q_reserve
  G3 require defined readiness(q_reserve)
HARD_CONSTRAINTS: H1-H3 above
CONSTRAINT_SOURCE_OR_SPECIFICATION: challenge task owner
SOFT_PREFERENCES: none
BASE_STRUCTURE_OR_PREDECESSOR: none; new symbolic target family
TARGET_DSD_LAYER_SCOPE: Formation + General Property
TARGET_RESOLUTION: channel admission + readiness definedness
CANDIDATE_OR_CONSTRUCTION_BASIS: explicit finite family O1-O3
CANDIDATE_GENERATION_RULE: enumerate O1-O3 exactly once in listed order
CANDIDATE_COVERAGE: exhaustive relative to DES-TASK-003-S
DSD_INTERFACE_PROFILE: current project Formation + General Property interface used by Protocol v0.1
VALIDATION_OR_ACCEPTANCE_RULE: candidate is Design-admissible iff H1-H3 all pass
DOMAIN_BRIDGE: not used
EXTERNAL_STANDARD: not used
AUXILIARY_METHODS_OR_HANDOFFS:
  downstream DSD Optimization receives admissible family + resource_cost objective; Optimization not executed in this case
NONOPTIMIZATION_SELECTION_RULE_IF_NEEDED: not used
```

### Expected terminal result

```text
ADMISSIBLE_TARGETS_OR_ADMISSIBLE_FAMILY: {O1,O2,O3}
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
HIDDEN_OPTIMIZATION: no
DESIGN_SELECTED_SINGLE_BEST_TARGET: no
HANDOFF_TO_OPTIMIZATION: recorded, not executed
```

Design must not return `{O3}` merely because `resource_cost(O3)` is lowest.

---

## 4. Case U — UNIQUE_TARGET must not be manufactured from Optimization objective

### Frozen task record

```text
DESIGN_TASK_ID: DES-TASK-003-U
PROTOCOL_VERSION: v0.1
TASK_SCOPE: determine whether the Design task itself establishes one unique target without using downstream Optimization
CLAIMED_OUTPUT_LEVEL: UNIQUE_TARGET
GOALS:
  G1 preserve q_primary
  G2 require q_reserve
  G3 require defined readiness(q_reserve)
HARD_CONSTRAINTS: H1-H3 above
CONSTRAINT_SOURCE_OR_SPECIFICATION: challenge task owner
SOFT_PREFERENCES: none
BASE_STRUCTURE_OR_PREDECESSOR: none; new symbolic target family
TARGET_DSD_LAYER_SCOPE: Formation + General Property
TARGET_RESOLUTION: channel admission + readiness definedness
CANDIDATE_OR_CONSTRUCTION_BASIS: explicit finite family O1-O3
CANDIDATE_GENERATION_RULE: enumerate O1-O3 exactly once in listed order
CANDIDATE_COVERAGE: exhaustive relative to DES-TASK-003-U
DSD_INTERFACE_PROFILE: current project Formation + General Property interface used by Protocol v0.1
VALIDATION_OR_ACCEPTANCE_RULE: candidate is Design-admissible iff H1-H3 all pass
DOMAIN_BRIDGE: not used
EXTERNAL_STANDARD: not used
AUXILIARY_METHODS_OR_HANDOFFS:
  downstream DSD Optimization could rank {O1,O2,O3} by resource_cost; Optimization not executed in this case
NONOPTIMIZATION_SELECTION_RULE_IF_NEEDED: none supplied
```

### Expected terminal result

All three candidates remain materially distinct and Design-admissible.
No Design-side determinacy rule establishes uniqueness.

```text
ADMISSIBLE_TARGETS_OR_ADMISSIBLE_FAMILY: {O1,O2,O3}
TERMINAL_DESIGN_STATUS: DESIGN_UNDERDETERMINED
TERMINAL_STATUS_BASIS: UNIQUE_TARGET requested but three distinct Design-admissible targets remain and only a downstream Optimization objective can rank them
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
UNSUPPORTED_UNIQUENESS_CLAIM: no
HIDDEN_OPTIMIZATION: no
```

Design must not convert `minimize resource_cost` into a uniqueness rule and must not choose `O3` as the Design-unique target.

---

## 5. Boundary attack conditions / 경계 공격 조건

The challenge fails if Design does any of the following:

```text
B1 choose O3 in Case S because it has minimum resource_cost
B2 return only O3 as the Design space
B3 treat resource_cost objective as an undeclared hard constraint
B4 use resource_cost as a hidden tie-breaker
B5 claim UNIQUE_TARGET=O3 in Case U
B6 absorb the downstream Optimization verdict into Design
B7 omit the Design -> Optimization handoff record
B8 count the unexecuted Optimization as direct Design evidence
```

The challenge passes only if the Design admissibility operation and the possible Optimization ranking remain separately identifiable.

---

## 6. Precommitted scoring / 사전 고정 점수

```text
CASE_S_REQUIRED_CHECKS:
  O1 Design-admissible: yes
  O2 Design-admissible: yes
  O3 Design-admissible: yes
  returned Design family exactly {O1,O2,O3}: yes
  single best target selected by Design: no
  resource_cost promoted to hard constraint: no
  handoff to Optimization recorded: yes
  Optimization executed inside Design case: no
  terminal status = DESIGN_ADMISSIBLE: yes
  protocol conformance = CONFORMANT: yes

CASE_U_REQUIRED_CHECKS:
  O1 Design-admissible: yes
  O2 Design-admissible: yes
  O3 Design-admissible: yes
  UNIQUE_TARGET=O3 claimed by Design: no
  hidden objective tie-breaker used: no
  terminal status = DESIGN_UNDERDETERMINED: yes
  protocol conformance = CONFORMANT: yes

CROSS_CASE_REQUIRED_CHECKS:
  Design admissibility and Optimization ranking remain distinct: yes
  neighboring-method verdict absorption: no
  method gain = NOT_ASSESSED in both cases: yes
  no inactive DSD layer introduced: yes

PRECOMMITTED_REQUIRED_CHECKS: 21
PASS_REQUIREMENT: 21/21
```

Any mismatch in a required item is a challenge failure or protocol-conformance issue and must be recorded rather than repaired post hoc.

---

## 7. Evidence limit / 증거 한계

This is a synthetic same-session boundary constructed challenge.
A PASS, if obtained, is one direct pilot-level Design boundary evidence item for Protocol v0.1 only.

It does not validate DSD Optimization itself because no Optimization protocol or Optimization execution is being tested here.
It tests only whether DSD Design preserves the declared Design/Optimization boundary.

It is not:

```text
independent evaluator validation
external-domain validation
baseline superiority evidence
engineering usefulness evidence
Optimization method validation
method maturity evidence
```

The two subcases share one frozen candidate family and one case ID, therefore the direct constructed-pilot count increments by **one** only: `DES-CH-003`.
