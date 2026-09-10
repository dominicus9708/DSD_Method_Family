# DSD Synthesis Planning / DSD 합성론 기획

Status: **Protocol v0.1 established / Steps 5-6 direct pilots complete / validation in progress**  
Date opened: **2026-09-10**

## Purpose / 목적

Develop DSD Synthesis as an independent method under **Field III: Construction & Transformation**.

Synthesis consumes supplied admitted parts, component structures, or typed component records and an explicit composition rule, then determines which larger constructions are legitimate while preserving component status, interface prerequisites, relation/support retention, information-loss conditions, and formation-model boundaries.

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

## Output levels / 산출 수준

```text
SYNTHESIS_SPACE
SYNTHESIZED_TARGET
UNIQUE_SYNTHESIZED_TARGET
PARTIAL_SYNTHESIS
```

## Terminal statuses / 종결 상태

```text
SYNTHESIS_ADMISSIBLE
SYNTHESIS_INFEASIBLE
SYNTHESIS_UNDERDETERMINED
SYNTHESIS_BLOCKED
```

`SYNTHESIS_INFEASIBLE` requires exhaustive composition coverage or an explicit impossibility argument sufficient for the frozen scope.
Non-exhaustive closure failure remains underdetermined.
Missing claim-required inputs may yield a conformant blocked result.

## Three-ledger separation / 3중 장부 분리

```text
TERMINAL_SYNTHESIS_STATUS
SYNTHESIS_PROTOCOL_CONFORMANCE
SYNTHESIS_METHOD_GAIN_STATUS
```

## Development sequence / 개발 순서

1. ✅ Define Synthesis-specific task interface — `TASK_INTERFACE_v0.1-draft.md`.
2. ✅ Run 16 pre-protocol boundary attacks — 11 preserved without refinement, 5 with non-breaking refinement, 0 collapse, 0 fundamental failure.
3. ✅ Preserve required boundary refinements — `TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`.
4. ✅ Freeze executable `Synthesis Protocol v0.1` — commit `8787b24`.
5. ✅ Positive constructed challenge `SYN-CH-001` — precommit `4eeba2a`, result `71e5d5c`, **28/28 PASS**.
6. ✅ Negative/failure terminal-status challenge `SYN-CH-002` — precommit `09fc616`, result `7dac87c`, **36/36 PASS**.
7. **Next:** direct method-boundary challenge(s) under Protocol v0.1.
8. First `NO_GAIN` case with competent baseline and frozen gain criteria.
9. Broader strongest-reasonable-baseline comparison.
10. External/domain application with externally supplied composition legitimacy.
11. Dedicated reproducibility/retrace record.
12. DSD Audit maturity review only after evidence architecture is materially populated.
13. Independent-evaluator infrastructure only when protocol/evidence stability justifies it.

## Step 5 result — SYN-CH-001

```text
CASE_CLASS: positive
PRECOMMIT: 4eeba2a
RESULT: 71e5d5c
ADMISSIBLE_FAMILY: {K1,K2}
TERMINAL_SYNTHESIS_STATUS: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS: NOT_ASSESSED
PRECOMMITTED_REQUIRED_CHECKS: 28/28 PASS
```

The case preserves `DEFINED_ZERO != APPLICABLE_BUT_UNDEFINED`, rejects interface-incompatible arrangements despite individual admission, avoids automatic whole-Property lift, and makes no temporal process claim.

## Step 6 result — SYN-CH-002

Three subcases were frozen under one Case ID.

```text
CASE_CLASS: negative_failure
PRECOMMIT: 09fc616
RESULT: 7dac87c
```

Results:

```text
Subcase I
  exhaustive candidate universe {I1,I2}
  both rejected {H2}
  -> SYNTHESIS_INFEASIBLE / CONFORMANT / NOT_ASSESSED

Subcase U
  non-exhaustive candidate basis {U1,U2}
  U1 admissible, U2 rejected {H2}
  UNIQUE_SYNTHESIZED_TARGET requested
  -> SYNTHESIS_UNDERDETERMINED / CONFORMANT / NOT_ASSESSED

Subcase B
  required composition rule unavailable
  no substantive candidate evaluation fabricated
  -> SYNTHESIS_BLOCKED / CONFORMANT / NOT_ASSESSED
```

Scoring:

```text
PRECOMMITTED_REQUIRED_CHECKS: 36
PASSED: 36
FAILED: 0
CHALLENGE_VERDICT: PASS
PROTOCOL_REVISION_REQUIRED: no
```

The case directly demonstrates:

```text
REJECTED_UNDER_EXHAUSTIVE_COVERAGE
!= INSUFFICIENT_COVERAGE_FOR_CLOSURE
!= MISSING_REQUIRED_INPUT

local admissibility
!= requested output-level closure
```

## Evidence state after Step 6 / 6단계 후 증거 상태

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS: 2
POSITIVE_SYNTHESIS_CASES: 1
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 0
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

- Shared-core and neighboring-method evidence may be referenced but do not automatically become direct Synthesis validation.
- Historical planning/boundary failures remain preserved; corrections are prospective.
- No baseline superiority is claimed without a frozen baseline and gain criterion.
- No external authority is replaced by DSD terminology.
- No Formation Clause VII or Static Aggregation result is upgraded into domain composability without explicit composition legitimacy.
- No static composability result is upgraded into time-resolved assembly feasibility without explicit process scope/model.
- Local candidate success does not establish a stronger requested closure such as uniqueness when coverage is insufficient.
- Protocol v0.1 is revised only prospectively if direct evidence exposes a genuine protocol defect.
