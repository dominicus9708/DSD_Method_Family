# DSD Synthesis Planning / DSD 합성론 기획

Status: **Protocol v0.1 established / Steps 5-7 direct pilots complete / validation in progress**  
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

Earlier artifacts remain historical and are not rewritten after later evidence.

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
5. ✅ `SYN-CH-001` positive — precommit `4eeba2a`, result `71e5d5c`, **28/28 PASS**.
6. ✅ `SYN-CH-002` negative/failure — precommit `09fc616`, result `7dac87c`, **36/36 PASS**.
7. ✅ `SYN-CH-003` direct method-boundary — precommit `2eea8ae`, result `cb55dba`, **46/46 PASS**.
8. **Next:** first `NO_GAIN` case with competent baseline and frozen gain criteria.
9. Broader strongest-reasonable-baseline comparison.
10. External/domain application with externally supplied composition legitimacy.
11. Dedicated reproducibility/retrace record.
12. DSD Audit maturity review after evidence architecture is materially populated.
13. Independent-evaluator infrastructure only when protocol/evidence stability justifies it.

## Step 5 — SYN-CH-001

```text
ADMISSIBLE_FAMILY: {K1,K2}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
SCORE: 28/28 PASS
```

Preserved `DEFINED_ZERO != APPLICABLE_BUT_UNDEFINED`, individual admission versus composability, no automatic whole-Property lift, and static-versus-temporal scope separation.

## Step 6 — SYN-CH-002

```text
I: exhaustive all rejected
   -> SYNTHESIS_INFEASIBLE / CONFORMANT / NOT_ASSESSED
U: non-exhaustive uniqueness closure
   -> SYNTHESIS_UNDERDETERMINED / CONFORMANT / NOT_ASSESSED
B: required composition rule unavailable
   -> SYNTHESIS_BLOCKED / CONFORMANT / NOT_ASSESSED
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

Shared frozen Synthesis family:

```text
S0 = (SRC ⊙ M0) ⊙ SNK
S1 = (SRC ⊙ M1) ⊙ SNK
ADMISSIBLE_FAMILY: {S0,S1}
```

Four mixed-workflow requests were pressured:

```text
D: invent missing monitoring architecture to satisfy an extra goal
   -> DESIGN_REQUIRED handoff
T: convert S0 to adjacency-matrix representation
   -> TRANSFORMATION_REQUIRED handoff
A: produce scalar readout from component weights
   -> AGGREGATION_REQUIRED handoff
O: choose lower-cost admissible composition
   -> OPTIMIZATION_REQUIRED handoff
```

Synthesis did not perform those neighboring operations and did not absorb their verdicts. In all four subcases:

```text
TERMINAL_SYNTHESIS_STATUS: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The objective in O would prefer `S0`, but Synthesis preserved `{S0,S1}` because objective-based choice belongs to Optimization.

```text
PRECOMMITTED_REQUIRED_CHECKS: 46
PASSED: 46
FAILED: 0
CHALLENGE_VERDICT: PASS
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

## Evidence state after Step 7 / 7단계 후 증거 상태

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS: 3
POSITIVE_SYNTHESIS_CASES: 1
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 1
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
NO_GAIN_SYNTHESIS_CASES: 0
BASELINE_COMPARISON_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

## Recording rule / 기록 규칙

- Shared-core and neighboring-method evidence may be referenced but does not automatically become direct Synthesis validation.
- Historical planning/boundary failures are preserved; corrections are prospective.
- No baseline superiority is claimed without frozen baseline and gain criterion.
- No Formation Clause VII or Static Aggregation result is upgraded into domain composability without explicit legitimacy.
- No static composability result is upgraded into time-resolved assembly feasibility without explicit process scope/model.
- No goal-driven invention, representation mapping, aggregate readout, or objective-based selection is silently absorbed into Synthesis.
- Protocol v0.1 is revised only prospectively if direct evidence exposes a genuine defect.
