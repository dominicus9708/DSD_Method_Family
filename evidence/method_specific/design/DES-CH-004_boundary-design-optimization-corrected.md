# DES-CH-004 — Corrected Design / Optimization Boundary

Status: **PASS — successful boundary constructed Design pilot under Protocol v0.1**  
Date: **2026-09-08**  
Evidence scope: `method_specific`  
Method directly tested: **DSD Design / DSD 설계론**  
Method protocol: **DSD Design Protocol v0.1**  
Precommit: `DES-CH-004_precommit.md`, commit `47d73f6`

## 1. Evidence claim / 증거 주장

This case prospectively corrects the target-resolution defect exposed by `DES-CH-003`.

The corrected challenge freezes three candidates that are materially distinct inside the Design target resolution through the exact value of:

```text
reserve_mode(q_reserve)
```

The candidates are all Design-admissible, while a separate downstream objective:

```text
minimize resource_cost
```

would rank them if Optimization were later executed.

Optimization itself is not executed in this Design evidence case.

---

## 2. Frozen candidate evaluation / 동결 후보 평가

Shared hard constraints:

```text
H1 q_primary is admitted
H2 q_reserve is admitted
H3 readiness(q_reserve) is applicable and defined
H4 reserve_mode(q_reserve) is applicable and defined
H5 reserve_mode(q_reserve) is one of {MODE_A, MODE_B, MODE_C}
```

### C1

```text
q_primary: admitted
q_reserve: admitted
readiness(q_reserve): APPLICABLE, DEFINED_NONZERO
reserve_mode(q_reserve): APPLICABLE, DEFINED value MODE_A
resource_cost: 30
```

Result:

```text
H1: pass
H2: pass
H3: pass
H4: pass
H5: pass
ADMISSIBILITY_RESULT: admissible
```

### C2

```text
q_primary: admitted
q_reserve: admitted
readiness(q_reserve): APPLICABLE, DEFINED_NONZERO
reserve_mode(q_reserve): APPLICABLE, DEFINED value MODE_B
resource_cost: 20
```

Result:

```text
H1: pass
H2: pass
H3: pass
H4: pass
H5: pass
ADMISSIBILITY_RESULT: admissible
```

### C3

```text
q_primary: admitted
q_reserve: admitted
readiness(q_reserve): APPLICABLE, DEFINED_NONZERO
reserve_mode(q_reserve): APPLICABLE, DEFINED value MODE_C
resource_cost: 10
```

Result:

```text
H1: pass
H2: pass
H3: pass
H4: pass
H5: pass
ADMISSIBILITY_RESULT: admissible
```

Distinctness at the declared target resolution is preserved:

```text
C1 -> reserve_mode = MODE_A
C2 -> reserve_mode = MODE_B
C3 -> reserve_mode = MODE_C

C1 != C2 != C3 at TARGET_RESOLUTION
```

No candidate is rejected or preferred because of `resource_cost`.

---

## 3. Case S execution — DESIGN_SPACE

Frozen output claim:

```text
CLAIMED_OUTPUT_LEVEL: DESIGN_SPACE
```

All three materially distinct candidates satisfy every Design hard constraint.

Therefore:

```text
ADMISSIBLE_TARGETS_OR_ADMISSIBLE_FAMILY: {C1,C2,C3}
REJECTED_CANDIDATES: {}
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
HIDDEN_OPTIMIZATION: no
DESIGN_SELECTED_SINGLE_BEST_TARGET: no
RESOURCE_COST_PROMOTED_TO_HARD_CONSTRAINT: no
```

The downstream handoff is recorded as:

```text
Design admissible family {C1,C2,C3}
+ resource_cost objective
-> prospective DSD Optimization input
```

No Optimization verdict is imported into Design.

Case S: **PASS**.

---

## 4. Case U execution — UNIQUE_TARGET

Frozen output claim:

```text
CLAIMED_OUTPUT_LEVEL: UNIQUE_TARGET
```

The Design hard constraints permit all three reserve-mode values.
The exact reserve-mode value is part of the declared target resolution.
Therefore the three candidates remain materially distinct Design targets.

No Design-side determinacy rule chooses among them.
The only supplied ranking rule is the downstream Optimization objective `minimize resource_cost`.

Protocol v0.1 forbids using that objective as a hidden Design tie-breaker or uniqueness proof.

Result:

```text
ADMISSIBLE_TARGETS_OR_ADMISSIBLE_FAMILY: {C1,C2,C3}
UNRESOLVED_FIELDS:
  unique reserve_mode selection among MODE_A / MODE_B / MODE_C
TERMINAL_DESIGN_STATUS: DESIGN_UNDERDETERMINED
TERMINAL_STATUS_BASIS:
  UNIQUE_TARGET requested while three materially distinct Design-admissible targets remain;
  only a downstream Optimization objective ranks them
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
HIDDEN_OPTIMIZATION: no
UNSUPPORTED_UNIQUENESS_CLAIM: no
```

Design does not claim `C3` as unique merely because `resource_cost(C3)` is lowest.

Case U: **PASS**.

---

## 5. Boundary verdict / 경계 판정

The executable Design boundary is preserved:

```text
HARD CONSTRAINTS
-> {C1,C2,C3} Design-admissible family

OBJECTIVE: minimize resource_cost
-> prospective Optimization ranking
```

These operations remain separately identifiable.

The Design result does not absorb:

```text
objective ranking
best-candidate selection
Optimization evidence
Optimization validation standard
Optimization method status
```

The challenge therefore supports the current method-family boundary statement:

```text
Design forms an admissible target/design space from goals and constraints.
Optimization selects among an already justified admissible space under an objective and constraints.
```

---

## 6. Precommitted scoring result / 사전 고정 점수 결과

```text
CASE_S_REQUIRED_CHECKS:
  C1 Design-admissible: PASS
  C2 Design-admissible: PASS
  C3 Design-admissible: PASS
  C1/C2/C3 remain distinct at target resolution: PASS
  returned Design family exactly {C1,C2,C3}: PASS
  single best target selected by Design: PASS (no)
  resource_cost promoted to hard constraint: PASS (no)
  handoff to Optimization recorded: PASS
  Optimization executed inside Design case: PASS (no)
  terminal status = DESIGN_ADMISSIBLE: PASS
  protocol conformance = CONFORMANT: PASS

CASE_U_REQUIRED_CHECKS:
  C1 Design-admissible: PASS
  C2 Design-admissible: PASS
  C3 Design-admissible: PASS
  C1/C2/C3 remain distinct at target resolution: PASS
  UNIQUE_TARGET=C3 claimed by Design: PASS (no)
  resource_cost used as hidden tie-breaker: PASS (no)
  terminal status = DESIGN_UNDERDETERMINED: PASS
  unresolved uniqueness basis explicitly recorded: PASS
  protocol conformance = CONFORMANT: PASS

CROSS_CASE_REQUIRED_CHECKS:
  Design admissibility and Optimization ranking remain distinct: PASS
  neighboring-method verdict absorption: PASS (none)
  method gain = NOT_ASSESSED in both cases: PASS
  no inactive DSD layer introduced: PASS

PRECOMMITTED_REQUIRED_CHECKS: 23
PASSED: 23
FAILED: 0
CHALLENGE_VERDICT: PASS
```

---

## 7. Relation to DES-CH-003 / DES-CH-003과의 관계

`DES-CH-003` is not rewritten or discarded.
It remains a failed precommitted challenge whose candidate distinctions existed only in downstream objective metadata excluded from its own Design target resolution.

`DES-CH-004` corrects that defect prospectively by putting the distinguishing categorical property `reserve_mode` inside the frozen target resolution before evaluation.

This pair therefore demonstrates both:

```text
precommit failure preservation
and
prospective test correction without historical rewriting
```

---

## 8. Reproducibility / 재현성

```text
REPRODUCIBILITY_RECORD:
  protocol: methods/04_design/PROTOCOL_v0.1.md
  failed predecessor challenge: DES-CH-003
  precommit: evidence/method_specific/design/DES-CH-004_precommit.md
  precommit_commit: 47d73f6
  candidate_order: C1,C2,C3
  candidate_modes: MODE_A,MODE_B,MODE_C
  resource_costs: 30,20,10
  stochastic_generation: none
  task_revision_after_lock: none
  candidate_addition_after_lock: none
  target_resolution_change_after_lock: none
  objective_used_inside_Design: no
  Optimization_execution: none
```

The result is deterministically retraceable from the frozen record.

---

## 9. Evidence limit / 증거 한계

This case directly supports only the Design-side boundary under Protocol v0.1.
It does not validate DSD Optimization itself.

It does not establish:

```text
NO_GAIN or baseline superiority
external-domain applicability
independent evaluator agreement
engineering or practical usefulness
Optimization protocol validity
method maturity
```

---

## 10. Evidence verdict / 증거 판정

```text
CASE_ID: DES-CH-004
CASE_CLASS: boundary
CASE_ORIGIN: constructed_same_session
PROTOCOL: v0.1
CASE_S_STATUS: DESIGN_ADMISSIBLE
CASE_U_STATUS: DESIGN_UNDERDETERMINED
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT in both subcases
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
DIRECT_EVIDENCE_RESULT: PASS
DIRECT_CONSTRUCTED_PILOT_INCREMENT: +1
BOUNDARY_VALIDATION_PASS_INCREMENT: +1
```

This is the first successful executable-protocol Design boundary validation.
