# SYN-CH-003 Method-Boundary Separation Result / DSD 합성론 Direct Method-Boundary Challenge 결과

Status: **EXECUTED — PASS**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Protocol: **v0.1**  
Protocol commit: `8787b242cb6648c47396151dbac3aadc19e3d184`  
Precommit commit: `2eea8aea66c080785d04c8d70830e77b545b5a2e`  
Precommit blob: `8c31bab8cbe3868621520e92e04a1c522ea40bee`

## 1. Evidence identity

```text
CASE_ID: SYN-CH-003
CASE_CLASS: method_boundary
CASE_ORIGIN: constructed_same_session
EVIDENCE_SCOPE_CLASS: method_specific
METHOD_DIRECTLY_TESTED: DSD Synthesis
METHOD_VERSION_OR_PROTOCOL: Synthesis Protocol v0.1
SUBCASES: D, T, A, O
```

The immutable precommit was read after commit and before this result was created. No frozen component, rule, coverage, target resolution, expected handoff, or scoring criterion was modified.

## 2. Shared Synthesis execution

Frozen candidates:

```text
S0 = (SRC ⊙ M0) ⊙ SNK
S1 = (SRC ⊙ M1) ⊙ SNK
```

Under `R_CHAIN_3`:

```text
S0
  SRC.output alpha -> M0.input alpha: PASS
  M0.output beta -> SNK.input beta: PASS
  SYNTHESIS_CANDIDATE_RESULT: admissible

S1
  SRC.output alpha -> M1.input alpha: PASS
  M1.output beta -> SNK.input beta: PASS
  SYNTHESIS_CANDIDATE_RESULT: admissible
```

Therefore the Synthesis result common to all four mixed-workflow subcases is:

```text
SYNTHESIS_ADMISSIBLE_FAMILY: {S0,S1}
COMPOSITION_COVERAGE: exhaustive relative only to {S0,S1}
TERMINAL_SYNTHESIS_STATUS: SYNTHESIS_ADMISSIBLE
```

No neighboring operation changes this family unless it is executed as its own method/handoff.

---

## 3. Subcase D — Design boundary

Additional request:

```text
synthesized result must expose a monitoring output of type gamma
```

The supplied Synthesis inventory has no monitoring component, gamma connector, or rule for inventing such architecture.

Execution result:

```text
SYNTHESIS_ADMISSIBLE_FAMILY_D: {S0,S1}
TERMINAL_SYNTHESIS_STATUS_D: SYNTHESIS_ADMISSIBLE
BOUNDARY_HANDOFF_D: DESIGN_REQUIRED
NON_SYNTHESIS_OPERATION_D: not_executed
FABRICATED_MONITORING_COMPONENT: no
FABRICATED_GAMMA_CONNECTOR: no
MIXED_TASK_COMPLETION_D: pending_design_handoff
SYNTHESIS_PROTOCOL_CONFORMANCE_D: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS_D: NOT_ASSESSED
```

The Synthesis subtask succeeds on the supplied parts. The additional goal remains unresolved until a Design operation supplies a legitimate new part/architecture basis. Synthesis does not invent that basis.

---

## 4. Subcase T — Transformation boundary

Additional request:

```text
convert synthesized target S0 into an adjacency-matrix representation
```

Execution result:

```text
SYNTHESIS_ADMISSIBLE_FAMILY_T: {S0,S1}
S0_SYNTHESIS_STATUS: admissible
TERMINAL_SYNTHESIS_STATUS_T: SYNTHESIS_ADMISSIBLE
BOUNDARY_HANDOFF_T: TRANSFORMATION_REQUIRED
ADJACENCY_MATRIX_OUTPUT_FROM_SYNTHESIS: not_produced
TRANSFORMATION_VERDICT_ABSORBED: no
NON_SYNTHESIS_OPERATION_T: not_executed
SYNTHESIS_PROTOCOL_CONFORMANCE_T: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS_T: NOT_ASSESSED
```

The ordered-component/interface structure is retained and can be passed to a later Transformation method, but representation conversion is not relabeled as Synthesis.

---

## 5. Subcase A — Aggregation boundary

Additional request:

```text
produce a scalar readout equal to the sum of participating component readout_weight values
```

The frozen component metadata contain weights, but Synthesis does not compute or substitute the scalar readout for the synthesized whole.

Execution result:

```text
SYNTHESIS_ADMISSIBLE_FAMILY_A: {S0,S1}
TERMINAL_SYNTHESIS_STATUS_A: SYNTHESIS_ADMISSIBLE
BOUNDARY_HANDOFF_A: AGGREGATION_REQUIRED
SCALAR_READOUT_AS_SYNTHESIZED_WHOLE: no
AGGREGATION_RESULT_FROM_SYNTHESIS: not_produced
AGGREGATE_EQUALITY_USED_AS_STRUCTURAL_EQUIVALENCE: no
NON_SYNTHESIS_OPERATION_A: not_executed
SYNTHESIS_PROTOCOL_CONFORMANCE_A: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS_A: NOT_ASSESSED
```

The component weights remain metadata available for an Aggregation handoff. No scalar readout is treated as the structural whole or as evidence that two compositions are structurally equivalent.

---

## 6. Subcase O — Optimization boundary

Additional request:

```text
choose the lower-cost admissible composition
objective: minimize middle-component cost
```

The frozen costs are:

```text
cost(M0) = 1
cost(M1) = 3
```

Thus an Optimization method supplied with that objective would prefer `S0`. Synthesis itself does not use the objective to remove `S1` from the admissible family.

Execution result:

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

The fact that `S0` is cheaper is relevant to the downstream Optimization objective, not to Synthesis admissibility.

---

## 7. Cross-boundary result

The executable Protocol-v0.1 run preserved all four method boundaries:

```text
goal-driven invention of missing architecture
-> DESIGN handoff

source/whole -> alternate representation mapping
-> TRANSFORMATION handoff

structure/data -> scalar readout
-> AGGREGATION handoff

admissible family + objective -> preferred alternative
-> OPTIMIZATION handoff
```

Therefore:

```text
SYNTHESIS_SUCCESS
!= MIXED_WORKFLOW_COMPLETION

SYNTHESIS_ADMISSIBLE_FAMILY
!= OPTIMIZED_SELECTION

SYNTHESIZED_WHOLE
!= AGGREGATE_READOUT

SYNTHESIZED_STRUCTURE
!= TRANSFORMED_REPRESENTATION

SUPPLIED_PARTS
!= DESIGN-LICENSE_TO_INVENT_MISSING_PARTS
```

Neighboring-method handoffs are recorded without importing their verdicts into the Synthesis terminal ledger.

## 8. Three-ledger separation

All four Synthesis subcases retain:

```text
TERMINAL_SYNTHESIS_STATUS: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The differing handoff labels are workflow-boundary records, not alternate Synthesis terminal statuses.

## 9. Precommitted scoring

```text
A. common integrity                 8 / 8 PASS
B. Subcase D — Design               8 / 8 PASS
C. Subcase T — Transformation       8 / 8 PASS
D. Subcase A — Aggregation          8 / 8 PASS
E. Subcase O — Optimization         8 / 8 PASS
F. cross-boundary discipline        6 / 6 PASS

PRECOMMITTED_REQUIRED_CHECKS:      46
PASSED:                             46
FAILED:                              0
CHALLENGE_VERDICT:                PASS
```

No check was deleted, weakened, or reclassified after execution.

## 10. Direct-evidence increment

```text
DIRECT_EVIDENCE_RESULT: PASS
DIRECT_CONSTRUCTED_PILOT_INCREMENT: +1
BOUNDARY_SYNTHESIS_CASE_INCREMENT: +1
```

Post-run Synthesis evidence state:

```text
DIRECT_SYNTHESIS_PILOTS: 3
POSITIVE_SYNTHESIS_CASES: 1
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 1
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
```

## 11. Protocol-defect check

No Protocol-v0.1 defect was exposed by this challenge.

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

The result only shows that the current protocol handled these four frozen mixed-workflow pressures without method absorption.

## 12. Limits

This case does **not** establish:

```text
external applicability
method superiority over a competent baseline
NO_GAIN behavior
broader baseline comparison
reproducibility beyond this project
independent evaluator agreement
Synthesis method maturity
correctness of any neighboring method's downstream result
```

The next evidence task should be a separately precommitted `NO_GAIN` case against a competent baseline that is allowed to preserve the same component/interface information, followed later by a broader strongest-reasonable-baseline comparison.
