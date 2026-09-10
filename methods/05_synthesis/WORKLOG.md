# DSD Synthesis Worklog / DSD 합성론 작업 기록

## 2026-09-10 — Planning preparation and Step 1

Status: **planning started / Step 1 complete**

Locked project paths:

```text
methods/05_synthesis/
evidence/method_specific/synthesis/
```

Defined DSD Synthesis as:

```text
supplied parts + supplied composition rule
-> admissible whole/composition space
```

Created `TASK_INTERFACE_v0.1-draft.md` with component identity/status, composition-rule provenance, candidate basis/coverage, interface/prerequisites, property-lift discipline, retention/loss, formation effect, output levels, ledgers, handoffs, and reproducibility fields.

---

## 2026-09-10 — Step 2: pre-protocol boundary counterexamples

```text
BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md   d089b04
TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md d1f51b2
```

```text
BOUNDARY_ATTACKS_RUN: 16
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
```

Required non-breaking refinements:

```text
R1 COMPOSITION_LAW_PROFILE + GROUPING_OR_PARENTHESIZATION_POLICY
R2 COMPOSITION_EQUIVALENCE_OR_CANONICALIZATION_RULE
R3 RESIDUAL_OPEN_INTERFACES_OR_OBLIGATIONS
R4 ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE
```

The Step-1 draft remained historical and was not rewritten.

---

## 2026-09-10 — Step 4: Protocol v0.1 establishment

Created `methods/05_synthesis/PROTOCOL_v0.1.md` at commit `8787b24`. Executable sequence: `S1-S17`. Protocol creation itself added no direct pilot.

---

## 2026-09-10 — Step 5: SYN-CH-001 positive direct challenge

```text
PRECOMMIT: 4eeba2a
RESULT: 71e5d5c
ADMISSIBLE_FAMILY: {K1,K2}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
SCORE: 28/28 PASS
```

Evidence effect: direct pilot 1, successful positive 1.

---

## 2026-09-10 — Step 6: SYN-CH-002 negative/failure challenge

```text
PRECOMMIT: 09fc616
RESULT: 7dac87c
I -> SYNTHESIS_INFEASIBLE
U -> SYNTHESIS_UNDERDETERMINED
B -> SYNTHESIS_BLOCKED
SCORE: 36/36 PASS
PROTOCOL_REVISION_REQUIRED: no
```

Evidence effect: direct pilot 2, successful negative/failure 1.

---

## 2026-09-10 — Step 7: SYN-CH-003 direct method-boundary challenge

```text
PRECOMMIT: 2eea8ae
RESULT: cb55dba
BASE FAMILY: {S0,S1}
D -> DESIGN_REQUIRED
T -> TRANSFORMATION_REQUIRED
A -> AGGREGATION_REQUIRED
O -> OPTIMIZATION_REQUIRED
SCORE: 46/46 PASS
PROTOCOL_REVISION_REQUIRED: no
```

Evidence effect: direct pilot 3, successful executable boundary 1.

---

## 2026-09-10 — Step 8A: SYN-CH-004 first NO_GAIN baseline attempt

```text
PRECOMMIT: 1c77a0e
FIRST RESULT: 29730a5
POSTEXECUTION AUDIT: fe55899
STRICT SCORE: 33/35 FAIL
FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
PROTOCOL_FAILURE_INFERRED: no
```

The frozen H4 required `readiness(Y)` but malformed candidate Q5 placed `SRC` in the middle position without a frozen readiness record. The first execution's uncommitted exception was rejected. The failed challenge remains preserved and fills no successful NO_GAIN category.

---

## 2026-09-10 — Step 8B: SYN-CH-005 prospective corrected NO_GAIN challenge

```text
PRECOMMIT: 3c6f323
RESULT: f062d3f
DSD FAMILY: {R1,R2}
B0 FAMILY: {R1,R2}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NO_GAIN
SCORE: 37/37 PASS
```

The correction was prospective: `SRC` and `SNK` received explicit readiness records before execution. `B0_TYPED_CHAIN_CHECKER` preserved the same five comparison dimensions. Evidence state became direct attempts 5, successful NO_GAIN 1, successful baseline comparison 1.

---

## 2026-09-10 — Step 9: SYN-CH-006 broader strongest-reasonable-baseline comparison

Status: **52/52 PASS / NO_GAIN / strongest-reasonable-baseline category established at constructed level**

Precommit:

```text
evidence/method_specific/synthesis/SYN-CH-006_precommit.md
commit: 4a6c1fe7c702a0fd04bb01a029a9672bc5c7b6d1
blob: 5f210fe84ea8ade1bf34449f1a09236bff03c45e
```

Result:

```text
evidence/method_specific/synthesis/SYN-CH-006_strongest-reasonable-baseline-comparison.md
commit: 8ad51b5ffff826547d0f69890f979df8b7d556f8
```

The richer fixture froze eight candidates and simultaneously activated:

```text
supplied associativity and left/right grouping
material-target canonicalization
L_READY whole-Property lift
DEFINED_ZERO / DEFINED_NONZERO / APPLICABLE_BUT_UNDEFINED
structural-prerequisite staging with NOT_REACHED downstream checks
adjacency-relation retention
same_background vs new_formation_required
raw candidate family vs canonical class family
```

Execution:

```text
A1 -> admissible / C0
A2 -> admissible / C0
A3 -> admissible / C1
A4 -> admissible / C1
A5 -> rejected {H3}
A6 -> rejected {H2}; H3-H5 NOT_REACHED
A7 -> rejected {H4}
A8 -> rejected {H5}

RAW DSD FAMILY: {A1,A2,A3,A4}
RAW B1 FAMILY: {A1,A2,A3,A4}
CANONICAL DSD FAMILY: {C0,C1}
CANONICAL B1 FAMILY: {C0,C1}
```

`B1_TYPED_COMPOSITION_GRAPH_CHECKER` received all the same claim-relevant records and was competent to preserve every scored distinction. Gain evaluation:

```text
G1 STATUS_AND_PROPERTY_LIFT_GAIN: NOT_ESTABLISHED
G2 FAILURE_TRACEABILITY_GAIN: NOT_ESTABLISHED
G3 GROUPING_EQUIVALENCE_GAIN: NOT_ESTABLISHED
G4 RELATION_RETENTION_GAIN: NOT_ESTABLISHED
G5 FORMATION_EFFECT_GAIN: NOT_ESTABLISHED
G6 COMPOSITION_CLOSURE_GAIN: NOT_ESTABLISHED
G7 RETRACEABILITY_GAIN: NOT_ESTABLISHED
SYNTHESIS_METHOD_GAIN_STATUS: NO_GAIN
```

Scoring and protocol pressure:

```text
PRECOMMITTED_REQUIRED_CHECKS: 52
PASSED: 52
FAILED: 0
CHALLENGE_VERDICT: PASS
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

Evidence state after Step 9:

```text
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 6
SUCCESSFUL_POSITIVE_SYNTHESIS_CASES: 1
SUCCESSFUL_NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
SUCCESSFUL_BOUNDARY_SYNTHESIS_CASES: 1
PRESERVED_FAILED_BASELINE_CHALLENGE_DESIGNS: 1
SUCCESSFUL_NO_GAIN_SYNTHESIS_CASES: 2
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
REPRODUCIBILITY_CASES: 0
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
```

Interpretation: DSD Synthesis handled a richer typed composition task correctly, but a strong non-DSD baseline supplied with the same semantics matched every measured dimension. This is intentionally retained as `NO_GAIN`; it establishes no superiority.

### Next technical step

Create a separately precommitted `SYN-APP-001` from a stable external public source whose own rules supply component/interface compatibility or composition/assembly legitimacy. Avoid validating a domain grammar invented by this project. Method gain may remain `NOT_ASSESSED` unless a fair external baseline is independently justified.
