# DSD Synthesis Planning / DSD 합성론 기획

Status: **Protocol v0.1 established / Step 5 positive pilot complete / validation in progress**  
Date opened: **2026-09-10**

## Purpose / 목적

Develop DSD Synthesis as an independent method under **Field III: Construction & Transformation**.

Synthesis consumes supplied admitted parts, component structures, or typed component records and an explicit composition rule, then determines which larger constructions are legitimate while preserving component status, interface prerequisites, relation/support retention, information-loss conditions, and formation-model boundaries.

The method must remain distinct from Design, Transformation, Aggregation, Optimization, and Audit even when one workflow uses several of them together.

## Current source/interface lock / 현재 기준 잠금

Current DSD source interface:

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

`BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md` preserves the 16 pre-protocol attacks that motivated the amendment.
Earlier artifacts remain historical and are not rewritten after later evidence.

## Current task definition / 현재 과업 정의

**Input:** supplied components and identity/status records; explicit composition rule/source; arity/order/multiplicity and supplied composition-law profile; grouping; candidate basis/coverage; target resolution/equivalence; interface/prerequisite rules; property lift; retention/loss; formation policy; process scope; active DSD layers/domain criteria.

**Operation:** lock claim-relevant inputs before outcome inspection; verify component status; test interfaces/prerequisites; apply only the supplied rule/laws; evaluate property lift, retention/loss, formation effect, residual obligations, and process scope; construct admissible family; judge material target distinctness; assign terminal status, conformance, and gain separately.

**Output:** synthesis space/target or non-success basis; candidate failure sets; retention/loss and formation-effect records; residual/process/lineage records when applicable; three ledgers; handoffs, limits, and reproducibility data.

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
Non-exhaustive failure-to-find is not global infeasibility.

## Three-ledger separation / 3중 장부 분리

```text
TERMINAL_SYNTHESIS_STATUS
SYNTHESIS_PROTOCOL_CONFORMANCE
SYNTHESIS_METHOD_GAIN_STATUS
```

Maturity is evaluated separately by DSD Audit.

## Main method boundaries / 핵심 방법 경계

```text
Design: goals + constraints -> target/design space
Synthesis: supplied parts + supplied composition rule -> whole/composition space
Transformation: source -> target representation/regime
Aggregation: structure/data -> declared readout
Optimization: admissible alternatives -> objective-based selection
Dynamics/domain process model: time-resolved assembly/transition when claimed
Audit: retrace of frozen Synthesis execution
```

## Development sequence / 개발 순서

1. ✅ Define the Synthesis-specific task interface — `TASK_INTERFACE_v0.1-draft.md`.
2. ✅ Run 16 pre-protocol boundary attacks — 11 preserved without refinement, 5 with non-breaking refinement, 0 collapse, 0 fundamental failure.
3. ✅ Preserve required boundary refinements — `TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`.
4. ✅ Freeze executable `Synthesis Protocol v0.1` — commit `8787b24`.
5. ✅ Positive constructed challenge `SYN-CH-001` — precommit `4eeba2a`, result `71e5d5c`, **28/28 PASS**.
6. **Next:** negative/failure terminal-status challenge distinguishing `SYNTHESIS_INFEASIBLE`, `SYNTHESIS_UNDERDETERMINED`, and `SYNTHESIS_BLOCKED`.
7. Direct method-boundary challenge(s).
8. First `NO_GAIN` case with competent baseline and frozen gain criteria.
9. Broader strongest-reasonable-baseline comparison.
10. External/domain application with externally supplied composition legitimacy.
11. Dedicated reproducibility/retrace record.
12. DSD Audit maturity review only after evidence architecture is materially populated.
13. Independent-evaluator infrastructure only when protocol/evidence stability justifies it.

## Step 2 boundary result

```text
BOUNDARY_ATTACKS_RUN: 16
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
```

Four refinement groups entered Protocol v0.1:

```text
R1 COMPOSITION_LAW_PROFILE + GROUPING_OR_PARENTHESIZATION_POLICY
R2 COMPOSITION_EQUIVALENCE_OR_CANONICALIZATION_RULE
R3 RESIDUAL_OPEN_INTERFACES_OR_OBLIGATIONS
R4 ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE
```

## Protocol v0.1 establishment / 실행 프로토콜 동결

Protocol v0.1 uses an executable `S1-S17` sequence and freezes before outcome inspection:

```text
component identities/status sources
composition rule/source/arity/order/multiplicity
supplied composition-law profile
grouping/parenthesization
candidate basis and coverage
target resolution/equivalence rule
interface/prerequisite rules
property lift/redeclaration
retention/loss
formation policy
partial residual obligations
assembly process scope
active DSD layers/domain bridge/standard
non-optimization target selection if needed
```

## Step 5 result — SYN-CH-001

The first direct Protocol-v0.1 pilot used a separately committed precommit.

```text
CASE_ID: SYN-CH-001
CASE_CLASS: positive
CASE_ORIGIN: constructed_same_session
CLAIMED_OUTPUT_LEVEL: SYNTHESIS_SPACE
COMPOSITION_COVERAGE: exhaustive relative to frozen {K1,...,K6}
```

Candidate results:

```text
K1 -> admissible
K2 -> admissible
K3 -> rejected {H3 readiness undefined}
K4 -> rejected {H2 interface mismatch}
K5 -> rejected {H2 interface mismatch}
K6 -> rejected {H2 interface mismatch}

ADMISSIBLE_FAMILY: {K1,K2}
TERMINAL_SYNTHESIS_STATUS: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS: NOT_ASSESSED
PRECOMMITTED_REQUIRED_CHECKS: 28/28 PASS
```

The case preserves `DEFINED_ZERO != APPLICABLE_BUT_UNDEFINED`, rejects interface-incompatible arrangements even though all components are individually admitted, does not invent a whole-object Property, and makes no temporal process claim.

This is one constructed positive pilot only; it does not establish external applicability, baseline benefit, reproducibility, or maturity.

## Evidence state after Step 5 / 5단계 후 증거 상태

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS: 1
POSITIVE_SYNTHESIS_CASES: 1
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 0
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
- Protocol v0.1 is revised only prospectively if direct evidence exposes a genuine protocol defect.
