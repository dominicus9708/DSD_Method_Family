# DSD Synthesis Planning / DSD 합성론 기획

Status: **Protocol v0.1 established / Step 8 corrected NO_GAIN evidence complete / validation in progress**  
Date opened: **2026-09-10**

## Purpose / 목적

Develop DSD Synthesis as an independent method under **Field III: Construction & Transformation**.
Synthesis consumes supplied admitted parts or typed component records plus an explicit composition rule and determines which larger constructions are legitimate while preserving component status, interface prerequisites, relations/support, information-loss conditions, and formation-model boundaries.

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
8. ✅ First `NO_GAIN` stage: `SYN-CH-004` fixture defect preserved at **33/35 FAIL**; corrected prospective `SYN-CH-005` **37/37 PASS / NO_GAIN**.
9. **Next:** broader strongest-reasonable-baseline comparison.
10. External/domain application with externally supplied composition legitimacy.
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

Preserved:

```text
REJECTED_UNDER_EXHAUSTIVE_COVERAGE
!= INSUFFICIENT_COVERAGE_FOR_CLOSURE
!= MISSING_REQUIRED_INPUT

local admissibility
!= requested output-level closure
```

## Step 7 — SYN-CH-003 direct method-boundary

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

Preserved:

```text
SYNTHESIS_SUCCESS != MIXED_WORKFLOW_COMPLETION
SYNTHESIS_ADMISSIBLE_FAMILY != OPTIMIZED_SELECTION
SYNTHESIZED_WHOLE != AGGREGATE_READOUT
SYNTHESIZED_STRUCTURE != TRANSFORMED_REPRESENTATION
SUPPLIED_PARTS != DESIGN_LICENSE_TO_INVENT_MISSING_PARTS
```

## Step 8 — first NO_GAIN stage

### SYN-CH-004 preserved failed predecessor

```text
PRECOMMIT: 1c77a0e
FIRST RESULT: 29730a5
POSTEXECUTION AUDIT: fe55899
STRICT SCORE: 33/35
CHALLENGE_VERDICT: FAIL
FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
```

The frozen H4 required `readiness(Y)` to be defined, but candidate `Q5 = (M1 ⊙ SRC) ⊙ SNK` placed `SRC` in the middle position without a frozen readiness record. The precommitted expected `{H2,H3}` therefore omitted H4. No Protocol failure was inferred.

### SYN-CH-005 prospective correction

```text
PRECOMMIT: 3c6f323
RESULT: f062d3f
R1,R2 -> admissible
R3 -> rejected {H4}
R4 -> rejected {H2}
R5 -> rejected {H2,H3}
DSD FAMILY: {R1,R2}
B0 FAMILY: {R1,R2}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NO_GAIN
SCORE: 37/37 PASS
```

Frozen gain dimensions all returned `NOT_ESTABLISHED` because `B0_TYPED_CHAIN_CHECKER` preserved the same claim-relevant information:

```text
G1 STATUS_DISTINCTION_GAIN
G2 FAILURE_TRACEABILITY_GAIN
G3 COMPOSITION_CLOSURE_GAIN
G4 TARGET_DISTINCTNESS_GAIN
G5 RETRACEABILITY_GAIN
```

This fills the first successful dedicated NO_GAIN category and the first successful competent-baseline comparison at constructed-fixture level. It does not fill the broader strongest-reasonable-baseline category.

## Evidence state after Step 8 / 8단계 후 증거 상태

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 5
SUCCESSFUL_POSITIVE_SYNTHESIS_CASES: 1
SUCCESSFUL_NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
SUCCESSFUL_BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 1
PRESERVED_FAILED_BASELINE_CHALLENGE_DESIGNS: 1
SUCCESSFUL_NO_GAIN_SYNTHESIS_CASES: 1
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 1
STRONGEST_REASONABLE_BASELINE_COMPARISON: not established
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
REPRODUCIBILITY_CASES: 0
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

## Recording rule / 기록 규칙

- Shared-core and neighboring-method evidence may be referenced but does not automatically become direct Synthesis validation.
- Historical planning and failed challenge designs are preserved; corrections are prospective under new Case IDs.
- No baseline superiority is claimed without a frozen baseline and gain criterion.
- A competent baseline is not weakened to manufacture a DSD advantage.
- `NO_GAIN` is a legitimate result and is separate from correctness/conformance.
- No Formation Clause VII or Static Aggregation result is upgraded into domain composability without explicit legitimacy.
- No static composability result is upgraded into time-resolved assembly feasibility without explicit process scope/model.
- No goal-driven invention, representation mapping, aggregate readout, or objective-based selection is silently absorbed into Synthesis.
- Protocol v0.1 is revised only prospectively if direct evidence exposes a genuine protocol defect.

## Immediate next task / 다음

Precommit a materially richer strongest-reasonable-baseline comparison. The baseline should receive the same composition-relevant information and should be allowed to preserve sophisticated distinctions. Activate more than simple interface checking — preferably composition equivalence/grouping together with property lift/redeclaration, relation retention, partial residuals, or formation-effect bookkeeping. Do not force a DSD gain result.
