# DES-CH-002 Precommit — Negative Terminal-Status Separation

Status: **locked before case evaluation**  
Date: **2026-09-08**  
Evidence scope: `method_specific`  
Method directly tested: **DSD Design / DSD 설계론**  
Method protocol: **DSD Design Protocol v0.1**

## 1. Purpose / 목적

Test whether Protocol v0.1 distinguishes three non-success terminal states rather than collapsing them into one generic failure:

```text
DESIGN_INFEASIBLE
DESIGN_UNDERDETERMINED
DESIGN_BLOCKED
```

The locked distinctions are:

```text
DESIGN_INFEASIBLE
  = no admissible target exists in the declared design universe,
    supported by exhaustive candidate coverage or an explicit impossibility argument.

DESIGN_UNDERDETERMINED
  = the requested stronger result cannot be established from the declared information/coverage,
    while the protocol lacks a justified global no-target conclusion.

DESIGN_BLOCKED
  = a claim-required prerequisite is unavailable, so a required construction or validation check
    cannot be executed without fabrication.
```

No task field, candidate, candidate-coverage label, expected terminal status, or pass criterion may be changed after this precommit is written. Any later change must be recorded as a new challenge version.

## 2. Shared controls / 공통 통제

All three subcases use Protocol v0.1 and keep method gain unassessed.

```text
PROTOCOL_VERSION: v0.1
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
SOFT_PREFERENCES: none
STATIC_AGGREGATION: inactive
DYNAMICS: inactive
OPTIONAL_SPECIALIZATION: inactive
HIDDEN_OPTIMIZATION: prohibited
```

No inactive DSD layer or neighboring method may be introduced after lock to rescue a case.

---

## 3. Case I — Exhaustive no-solution / `DESIGN_INFEASIBLE`

### Frozen task record

```text
DESIGN_TASK_ID: DES-TASK-002-I
TASK_SCOPE: determine whether an admissible reserve-channel target exists in the complete toy candidate universe
CLAIMED_OUTPUT_LEVEL: ADMISSIBLE_TARGET
GOALS:
  G1 preserve q_primary
  G2 require q_reserve
  G3 require readiness(q_reserve) to be defined
HARD_CONSTRAINTS:
  H1 q_primary is admitted
  H2 q_reserve is admitted
  H3 readiness(q_reserve) is applicable and defined
CONSTRAINT_SOURCE_OR_SPECIFICATION: challenge task owner
BASE_STRUCTURE_OR_PREDECESSOR: none; new symbolic target family
TARGET_DSD_LAYER_SCOPE: Formation + General Property
TARGET_RESOLUTION: channel admission/absence plus readiness property defined/undefined status
CANDIDATE_OR_CONSTRUCTION_BASIS: explicit finite family I1-I2
CANDIDATE_GENERATION_RULE: enumerate I1-I2 exactly once in listed order
CANDIDATE_COVERAGE: exhaustive relative to DES-TASK-002-I
DSD_INTERFACE_PROFILE: current project Formation + General Property interface used by Protocol v0.1
VALIDATION_OR_ACCEPTANCE_RULE: admissible iff H1-H3 all pass
DOMAIN_BRIDGE: not used
EXTERNAL_STANDARD: not used
AUXILIARY_METHODS_OR_HANDOFFS: none
```

### Frozen candidates

#### I1

```text
q_primary: admitted
q_reserve: CHANNEL_ABSENCE
readiness(q_reserve): not established on an admitted reserve channel
```

Expected: `rejected` on H2.

#### I2

```text
q_primary: admitted
q_reserve: admitted
readiness(q_reserve): APPLICABLE_BUT_UNDEFINED
```

Expected: `rejected` on H3.

### Expected terminal result

```text
ADMISSIBLE_TARGETS: {}
TERMINAL_DESIGN_STATUS: DESIGN_INFEASIBLE
TERMINAL_STATUS_BASIS: exhaustive candidate universe I1-I2 evaluated; all candidates rejected on explicit hard constraints
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

No impossibility theorem is required because coverage is explicitly exhaustive relative to this challenge universe.

---

## 4. Case U — Non-exhaustive failure-to-find / `DESIGN_UNDERDETERMINED`

### Frozen task record

```text
DESIGN_TASK_ID: DES-TASK-002-U
TASK_SCOPE: return an admissible target if the declared search can justify one; do not claim global no-solution from partial coverage
CLAIMED_OUTPUT_LEVEL: ADMISSIBLE_TARGET
GOALS:
  G1 preserve q_primary
  G2 require q_reserve
  G3 require readiness(q_reserve) to be defined
HARD_CONSTRAINTS:
  H1 q_primary is admitted
  H2 q_reserve is admitted
  H3 readiness(q_reserve) is applicable and defined
CONSTRAINT_SOURCE_OR_SPECIFICATION: challenge task owner
BASE_STRUCTURE_OR_PREDECESSOR: none; larger symbolic target universe exists beyond evaluated sample
TARGET_DSD_LAYER_SCOPE: Formation + General Property
TARGET_RESOLUTION: channel admission/absence plus readiness property defined/undefined status
CANDIDATE_OR_CONSTRUCTION_BASIS: declared generator G_U over a larger symbolic family; this run evaluates only U1-U2
CANDIDATE_GENERATION_RULE: evaluate the first two frozen outputs U1-U2, then stop; no claim that these exhaust G_U
CANDIDATE_COVERAGE: non_exhaustive
DSD_INTERFACE_PROFILE: current project Formation + General Property interface used by Protocol v0.1
VALIDATION_OR_ACCEPTANCE_RULE: evaluated candidate admissible iff H1-H3 all pass
DOMAIN_BRIDGE: not used
EXTERNAL_STANDARD: not used
AUXILIARY_METHODS_OR_HANDOFFS: none
```

### Frozen evaluated candidates

#### U1

```text
q_primary: admitted
q_reserve: CHANNEL_ABSENCE
```

Expected: `rejected` on H2.

#### U2

```text
q_primary: admitted
q_reserve: admitted
readiness(q_reserve): APPLICABLE_BUT_UNDEFINED
```

Expected: `rejected` on H3.

### Expected terminal result

```text
ADMISSIBLE_TARGETS_IN_EVALUATED_SAMPLE: {}
TERMINAL_DESIGN_STATUS: DESIGN_UNDERDETERMINED
TERMINAL_STATUS_BASIS: no admissible target found in non-exhaustive evaluated sample; global infeasibility is unsupported
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The protocol must **not** assign `DESIGN_INFEASIBLE` merely because U1-U2 both fail.

---

## 5. Case B — Missing required predecessor / `DESIGN_BLOCKED`

### Frozen task record

```text
DESIGN_TASK_ID: DES-TASK-002-B
TASK_SCOPE: construct a target that preserves a required predecessor channel identity while adding a reserve channel
CLAIMED_OUTPUT_LEVEL: ADMISSIBLE_TARGET
GOALS:
  G1 preserve inherited q_legacy from predecessor P_B
  G2 add admitted q_reserve
HARD_CONSTRAINTS:
  H1 q_legacy in the candidate must match the locked predecessor identity in P_B
  H2 q_reserve is admitted
CONSTRAINT_SOURCE_OR_SPECIFICATION: challenge task owner
BASE_STRUCTURE_OR_PREDECESSOR: predecessor P_B is required by H1 but its identity record is unavailable at run time
TARGET_DSD_LAYER_SCOPE: Formation only
TARGET_RESOLUTION: channel identity/admission status
CANDIDATE_OR_CONSTRUCTION_BASIS: explicit target schema B1 containing a placeholder inherited q_legacy plus admitted q_reserve
CANDIDATE_GENERATION_RULE: evaluate B1 only; do not invent predecessor identity data
CANDIDATE_COVERAGE: exhaustive relative to the supplied schema family {B1}, but H1 cannot be validated without P_B
DSD_INTERFACE_PROFILE: current project Formation interface used by Protocol v0.1
VALIDATION_OR_ACCEPTANCE_RULE: candidate admissible iff H1-H2 are established
DOMAIN_BRIDGE: not used
EXTERNAL_STANDARD: not used
AUXILIARY_METHODS_OR_HANDOFFS: none
```

### Frozen candidate

#### B1

```text
q_legacy: placeholder reference to predecessor P_B identity
q_reserve: admitted
```

Expected:

```text
H1: blocked — predecessor identity record unavailable
H2: pass
ADMISSIBILITY_RESULT: blocked
```

### Expected terminal result

```text
TERMINAL_DESIGN_STATUS: DESIGN_BLOCKED
TERMINAL_STATUS_BASIS: claim-required predecessor identity is unavailable; H1 cannot be evaluated without fabrication
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The protocol must not fabricate P_B, reject B1 as if H1 were known false, or call the case infeasible.

---

## 6. Precommitted scoring / 사전 고정 점수

```text
CASE_I_REQUIRED_CHECKS:
  I1 rejected specifically on H2: yes
  I2 rejected specifically on H3: yes
  exhaustive coverage preserved: yes
  terminal status = DESIGN_INFEASIBLE: yes
  protocol conformance = CONFORMANT: yes

CASE_U_REQUIRED_CHECKS:
  U1 rejected specifically on H2: yes
  U2 rejected specifically on H3: yes
  non_exhaustive coverage preserved: yes
  terminal status = DESIGN_UNDERDETERMINED: yes
  unsupported DESIGN_INFEASIBLE claim made: no
  protocol conformance = CONFORMANT: yes

CASE_B_REQUIRED_CHECKS:
  missing predecessor explicitly identified: yes
  predecessor identity fabricated: no
  B1 candidate status = blocked rather than rejected: yes
  terminal status = DESIGN_BLOCKED: yes
  protocol conformance = CONFORMANT: yes

CROSS_CASE_REQUIRED_CHECKS:
  three terminal statuses remain distinct: yes
  no hidden Optimization: yes
  no inactive layer introduced: yes
  method gain = NOT_ASSESSED in all three cases: yes

PRECOMMITTED_REQUIRED_CHECKS: 20
PASS_REQUIREMENT: 20/20
```

Any mismatch in a required item is a challenge failure or protocol-conformance issue and must be recorded rather than repaired post hoc.

## 7. Evidence limit / 증거 한계

This is a synthetic same-session negative/failure constructed challenge.
A PASS, if obtained, is one direct pilot-level evidence item for DSD Design Protocol v0.1 only.

It is not:

```text
independent evaluator validation
external-domain validation
baseline superiority evidence
engineering usefulness evidence
method maturity evidence
```

This single challenge contains three locked subcases but increments the direct constructed-pilot count by **one** case ID only: `DES-CH-002`.
