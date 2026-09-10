# DSD Synthesis Planning / DSD 합성론 기획

Status: **Protocol v0.1 established / Step 9 strongest-reasonable-baseline comparison complete / validation in progress**  
Date opened: **2026-09-10**

## Purpose / 목적

Develop DSD Synthesis as an independent method under **Field III: Construction & Transformation**. Synthesis consumes supplied admitted parts or typed component records plus an explicit composition rule and determines which larger constructions are legitimate while preserving component status, interface prerequisites, relations/support, information-loss conditions, and formation-model boundaries.

## Current source/interface lock / 현재 기준 잠금

```text
Formation Axiom System
Property Axiom System
Channel-Indexed Static Aggregation
Structural Reorganization Dynamics
DSD_INTERFACE_PROFILE.md
METHOD_BOUNDARY_MATRIX.md
```

Key constraints:

```text
Formation Clause VII finite composition != universal domain composability
component property != automatic whole property
aggregate equality/readout != structural synthesis equality
```

## Protocol lineage / 프로토콜 계보

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

Earlier artifacts and failed challenges remain historical and are not rewritten after later evidence.

## Output / terminal / ledger structure

```text
OUTPUT_LEVELS:
  SYNTHESIS_SPACE
  SYNTHESIZED_TARGET
  UNIQUE_SYNTHESIZED_TARGET
  PARTIAL_SYNTHESIS

TERMINAL:
  SYNTHESIS_ADMISSIBLE
  SYNTHESIS_INFEASIBLE
  SYNTHESIS_UNDERDETERMINED
  SYNTHESIS_BLOCKED

THREE LEDGERS:
  TERMINAL_SYNTHESIS_STATUS
  SYNTHESIS_PROTOCOL_CONFORMANCE
  SYNTHESIS_METHOD_GAIN_STATUS
```

## Development sequence / 개발 순서

1. ✅ Synthesis-specific task interface.
2. ✅ 16 pre-protocol boundary attacks — 11 no refinement, 5 non-breaking refinement, 0 collapse.
3. ✅ Boundary Amendment 001.
4. ✅ Executable `Synthesis Protocol v0.1` — commit `8787b24`.
5. ✅ `SYN-CH-001` positive — **28/28 PASS**.
6. ✅ `SYN-CH-002` negative/failure — **36/36 PASS**.
7. ✅ `SYN-CH-003` direct method-boundary — **46/46 PASS**.
8. ✅ First `NO_GAIN` stage — `SYN-CH-004` **33/35 FAIL** challenge-design defect preserved; corrected `SYN-CH-005` **37/37 PASS / NO_GAIN**.
9. ✅ `SYN-CH-006` broader strongest-reasonable-baseline comparison — **52/52 PASS / NO_GAIN**, category established at constructed-evidence level.
10. **Next:** first external/domain application with externally supplied composition legitimacy.
11. Dedicated reproducibility/retrace record.
12. DSD Audit maturity review after evidence architecture is materially populated.
13. Independent-evaluator infrastructure only when protocol/evidence stability justifies it.

## Step 5 — SYN-CH-001

```text
PRECOMMIT: 4eeba2a
RESULT: 71e5d5c
ADMISSIBLE_FAMILY: {K1,K2}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
SCORE: 28/28 PASS
```

## Step 6 — SYN-CH-002

```text
PRECOMMIT: 09fc616
RESULT: 7dac87c
I -> SYNTHESIS_INFEASIBLE
U -> SYNTHESIS_UNDERDETERMINED
B -> SYNTHESIS_BLOCKED
SCORE: 36/36 PASS
PROTOCOL_REVISION_REQUIRED: no
```

## Step 7 — SYN-CH-003

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

## Step 8 — first NO_GAIN stage

```text
SYN-CH-004
  PRECOMMIT: 1c77a0e
  FIRST RESULT: 29730a5
  POSTEXECUTION AUDIT: fe55899
  33/35 FAIL
  FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT

SYN-CH-005
  PRECOMMIT: 3c6f323
  RESULT: f062d3f
  DSD FAMILY = B0 FAMILY = {R1,R2}
  SYNTHESIS_ADMISSIBLE / CONFORMANT / NO_GAIN
  37/37 PASS
```

The failed predecessor was not rewritten. `SYN-CH-005` fixed the missing middle-role readiness record prospectively under a new Case ID.

## Step 9 — SYN-CH-006 broader strongest-reasonable-baseline

Precommit and result:

```text
PRECOMMIT: 4a6c1fe
RESULT: 8ad51b5
BASELINE: B1_TYPED_COMPOSITION_GRAPH_CHECKER
```

Activated simultaneously:

```text
supplied associativity + left/right grouping
canonical material-target equivalence
explicit L_READY whole-Property lift
DEFINED_ZERO / DEFINED_NONZERO / APPLICABLE_BUT_UNDEFINED
staged H1-H2 prerequisite -> H3-H5 NOT_REACHED discipline
adjacency-relation retention
same_background vs new_formation_required
raw-candidate vs canonical-class closure
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
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NO_GAIN
SCORE: 52/52 PASS
```

Gain criteria:

```text
G1 STATUS_AND_PROPERTY_LIFT_GAIN: NOT_ESTABLISHED
G2 FAILURE_TRACEABILITY_GAIN: NOT_ESTABLISHED
G3 GROUPING_EQUIVALENCE_GAIN: NOT_ESTABLISHED
G4 RELATION_RETENTION_GAIN: NOT_ESTABLISHED
G5 FORMATION_EFFECT_GAIN: NOT_ESTABLISHED
G6 COMPOSITION_CLOSURE_GAIN: NOT_ESTABLISHED
G7 RETRACEABILITY_GAIN: NOT_ESTABLISHED
```

The competent baseline was not weakened and matched DSD on every frozen claim-relevant dimension. Therefore the broader comparison legitimately returns a second `NO_GAIN`.

## Evidence state after Step 9 / 9단계 후 증거 상태

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 6
SUCCESSFUL_POSITIVE_SYNTHESIS_CASES: 1
SUCCESSFUL_NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
SUCCESSFUL_BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 1
PRESERVED_FAILED_BASELINE_CHALLENGE_DESIGNS: 1
SUCCESSFUL_NO_GAIN_SYNTHESIS_CASES: 2
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
REPRODUCIBILITY_CASES: 0
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

## Recording rule / 기록 규칙

- Shared-core and neighboring-method evidence does not automatically become direct Synthesis validation.
- Historical planning and failed challenge designs are preserved; corrections are prospective under new Case IDs.
- A competent baseline is not weakened to manufacture a DSD advantage.
- `NO_GAIN` is a legitimate result and is separate from correctness/conformance.
- Grouping/equivalence is activated only when supplied by composition law and target-resolution rules.
- Component Property does not become whole Property without explicit lift/redeclaration.
- Relation loss and formation effect remain claim-relevant when the task includes them.
- No Formation Clause VII or Static Aggregation result is upgraded into domain composability without explicit legitimacy.
- No static composability result is upgraded into time-resolved assembly feasibility without explicit process scope/model.
- Protocol v0.1 is revised only prospectively if direct evidence exposes a genuine protocol defect.

## Immediate next task / 다음

Precommit the first external Synthesis application `SYN-APP-001`. Prefer a stable public source that supplies its own component/interface compatibility or assembly grammar so that domain composability is not invented by this project. Keep external-source compliance separate from Synthesis protocol conformance. Method gain should remain `NOT_ASSESSED` unless a fair baseline is independently justified.
