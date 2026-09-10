# SYN-CH-003 Precommit / DSD 합성론 Direct Method-Boundary Challenge 사전동결

Status: **PRECOMMITTED — evaluation not yet executed at commit time**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Protocol: **v0.1**  
Protocol commit: `8787b242cb6648c47396151dbac3aadc19e3d184`  
Protocol blob: `7367818f2d93125c84db7d559ac1409ed0e8d2e5`

## 1. Evidence identity

```text
CASE_ID: SYN-CH-003
CASE_CLASS: method_boundary
CASE_ORIGIN: constructed_same_session
METHOD_VERSION_OR_PROTOCOL: Synthesis Protocol v0.1
EVIDENCE_SCOPE_CLASS: method_specific
SUBCASES: D, T, A, O
```

This file freezes four mixed-workflow boundary subcases before execution. The Synthesis subtask remains fixed; neighboring operations must be exposed as handoffs rather than absorbed into Synthesis.

## 2. Shared base fixture

Formation-admitted components:

```text
SRC
  input_port: NONE
  output_port: alpha

M0
  input_port: alpha
  output_port: beta
  cost: 1
  readout_weight: 2

M1
  input_port: alpha
  output_port: beta
  cost: 3
  readout_weight: 5

SNK
  input_port: beta
  output_port: NONE
```

Supplied composition rule:

```text
R_CHAIN_3
(X ⊙ Y) ⊙ Z is composition-admissible iff:
  X.output and Y.input both exist and type-match;
  Y.output and Z.input both exist and type-match.
```

Rule profile:

```text
COMPOSITION_ARITY: ternary through fixed binary nesting
COMPOSITION_ORDER_SENSITIVITY: order_sensitive
COMMUTATIVITY: supplied_false
ASSOCIATIVITY: unspecified
GROUPING_OR_PARENTHESIZATION_POLICY: fixed_left_associated_only
MULTIPLICITY_POLICY: one occurrence of each listed component in a candidate
ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE: static_order_only
```

Frozen Synthesis candidates:

```text
S0 = (SRC ⊙ M0) ⊙ SNK
S1 = (SRC ⊙ M1) ⊙ SNK
```

Both are expected to be composition-admissible under `R_CHAIN_3`.

Shared Synthesis fields:

```text
CLAIMED_OUTPUT_LEVEL: SYNTHESIS_SPACE
TARGET_RESOLUTION:
  exact ordered component identities
  exact adjacent interface relations
COMPOSITION_CANDIDATE_BASIS: {S0,S1}
COMPOSITION_COVERAGE: exhaustive relative only to {S0,S1}
PROPERTY_LIFT_OR_REDECLARATION_RULE: not_used
NEW_FORMATION_MODEL_POLICY: remain_within_inherited_formation_background
DOMAIN_BRIDGE: not_used
EXTERNAL_STANDARD: not_used
SYNTHESIS_METHOD_GAIN_STATUS: NOT_ASSESSED
```

## 3. Boundary principle

The challenge tests the executable separation:

```text
Design: goals + constraints -> parts/architecture basis
Synthesis: supplied parts + supplied composition rule -> whole/composition space
Transformation: source -> target representation/regime
Aggregation: structure/data -> declared readout
Optimization: admissible alternatives -> objective-based choice
```

A neighboring handoff may be recorded, but its operation/result must not be silently produced as a Synthesis result.

---

# SUBCASE D — hidden Design pressure

Mixed request adds:

```text
EXTRA_GOAL:
  synthesized result must expose a monitoring output of type gamma
```

No monitoring component, gamma connector, or rule for creating such architecture is supplied.

Expected Synthesis behavior:

```text
SYNTHESIS_ADMISSIBLE_FAMILY_D: {S0,S1}
TERMINAL_SYNTHESIS_STATUS_D: SYNTHESIS_ADMISSIBLE
BOUNDARY_HANDOFF_D: DESIGN_REQUIRED
NON_SYNTHESIS_OPERATION_D: not_executed
FABRICATED_MONITORING_COMPONENT_OR_CONNECTOR: no
MIXED_TASK_COMPLETION_D: pending_design_handoff
SYNTHESIS_PROTOCOL_CONFORMANCE_D: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS_D: NOT_ASSESSED
```

The extra goal does not authorize Synthesis to invent a new component or architecture.

---

# SUBCASE T — Transformation pressure

Mixed request adds:

```text
POST_SYNTHESIS_REQUEST:
  convert synthesized target S0 into an adjacency-matrix representation
```

No Transformation protocol/result is supplied to Synthesis.

Expected Synthesis behavior:

```text
SYNTHESIS_ADMISSIBLE_FAMILY_T: {S0,S1}
S0_SYNTHESIS_STATUS: admissible
TERMINAL_SYNTHESIS_STATUS_T: SYNTHESIS_ADMISSIBLE
BOUNDARY_HANDOFF_T: TRANSFORMATION_REQUIRED
ADJACENCY_MATRIX_OUTPUT_FROM_SYNTHESIS: not_produced
NON_SYNTHESIS_OPERATION_T: not_executed
SYNTHESIS_PROTOCOL_CONFORMANCE_T: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS_T: NOT_ASSESSED
```

Synthesis may preserve the structure needed for a later mapping, but it must not relabel representation conversion as parts-to-whole composition.

---

# SUBCASE A — Aggregation pressure

Mixed request adds:

```text
POST_SYNTHESIS_REQUEST:
  produce a scalar readout equal to the sum of participating component readout_weight values
```

The scalar is a declared readout and is not the synthesized whole.

Expected Synthesis behavior:

```text
SYNTHESIS_ADMISSIBLE_FAMILY_A: {S0,S1}
TERMINAL_SYNTHESIS_STATUS_A: SYNTHESIS_ADMISSIBLE
BOUNDARY_HANDOFF_A: AGGREGATION_REQUIRED
SCALAR_READOUT_AS_SYNTHESIZED_WHOLE: no
AGGREGATION_RESULT_FROM_SYNTHESIS: not_produced
NON_SYNTHESIS_OPERATION_A: not_executed
SYNTHESIS_PROTOCOL_CONFORMANCE_A: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS_A: NOT_ASSESSED
```

The supplied component weights remain available metadata, but Synthesis does not use their sum as proof of structural identity or as a substitute for the composition record.

---

# SUBCASE O — Optimization pressure

Mixed request adds:

```text
POST_SYNTHESIS_REQUEST:
  choose the lower-cost admissible composition
OBJECTIVE:
  minimize total listed middle-component cost
```

The objective is explicit and would prefer `S0` because `cost(M0)=1 < cost(M1)=3`, but objective-based choice belongs to Optimization.

Expected Synthesis behavior:

```text
SYNTHESIS_ADMISSIBLE_FAMILY_O: {S0,S1}
TERMINAL_SYNTHESIS_STATUS_O: SYNTHESIS_ADMISSIBLE
BOUNDARY_HANDOFF_O: OPTIMIZATION_REQUIRED
UNIQUE_SYNTHESIZED_TARGET_FROM_COST_OBJECTIVE: not_established
OPTIMIZATION_SELECTION_FROM_SYNTHESIS: not_performed
NONOPTIMIZATION_SELECTION_RULE_IF_NEEDED: not_used
SYNTHESIS_PROTOCOL_CONFORMANCE_O: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS_O: NOT_ASSESSED
```

The fact that S0 is cheaper must not be used by Synthesis to reduce `{S0,S1}` to one target.

---

## 4. Precommitted scoring

Total required checks: **46**.

```text
A. common integrity: 8
  A1 Protocol commit/blob fixed
  A2 four subcase identities fixed
  A3 base components fixed
  A4 composition rule/law/grouping fixed
  A5 candidate basis {S0,S1} fixed
  A6 coverage exhaustive relative only to {S0,S1}
  A7 both S0 and S1 expected composition-admissible
  A8 no post-hoc task/rule/coverage/boundary revision

B. Subcase D: 8
  D1 Synthesis family exactly {S0,S1}
  D2 terminal Synthesis status = SYNTHESIS_ADMISSIBLE
  D3 Design handoff recorded
  D4 no monitoring component fabricated
  D5 no gamma connector fabricated
  D6 mixed-task completion remains pending Design handoff
  D7 conformance = CONFORMANT
  D8 gain = NOT_ASSESSED

C. Subcase T: 8
  T1 Synthesis family exactly {S0,S1}
  T2 S0 remains admissible as synthesized structure
  T3 terminal Synthesis status = SYNTHESIS_ADMISSIBLE
  T4 Transformation handoff recorded
  T5 no adjacency-matrix representation produced as Synthesis output
  T6 no Transformation verdict absorbed
  T7 conformance = CONFORMANT
  T8 gain = NOT_ASSESSED

D. Subcase A: 8
  G1 Synthesis family exactly {S0,S1}
  G2 terminal Synthesis status = SYNTHESIS_ADMISSIBLE
  G3 Aggregation handoff recorded
  G4 no scalar readout substituted for whole identity
  G5 no aggregate equality used as structural equivalence evidence
  G6 no Aggregation result produced as Synthesis output
  G7 conformance = CONFORMANT
  G8 gain = NOT_ASSESSED

E. Subcase O: 8
  O1 Synthesis family exactly {S0,S1}
  O2 terminal Synthesis status = SYNTHESIS_ADMISSIBLE
  O3 Optimization handoff recorded
  O4 cost objective does not remove S1 from Synthesis family
  O5 no unique target established from objective ranking
  O6 no Optimization selection performed inside Synthesis
  O7 conformance = CONFORMANT
  O8 gain = NOT_ASSESSED

F. cross-boundary discipline: 6
  F1 Design operation not absorbed
  F2 Transformation operation not absorbed
  F3 Aggregation operation not absorbed
  F4 Optimization operation not absorbed
  F5 neighboring-method verdicts remain separate from Synthesis terminal status
  F6 no external validity, superiority, reproducibility, independence, or maturity claim inferred
```

Decision rule:

```text
46/46 -> CHALLENGE_VERDICT: PASS
otherwise -> CHALLENGE_VERDICT: FAIL
```

No failed check may be deleted or weakened after execution.

## 5. Evidence-count lock

Before execution:

```text
DIRECT_SYNTHESIS_PILOTS: 2
POSITIVE_SYNTHESIS_CASES: 1
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 0
```

A completed execution may add exactly one direct constructed pilot and one boundary case.

Even a PASS does not establish external applicability, method superiority, `NO_GAIN` behavior, reproducibility, independent validation, or method maturity.
