# DSD Design Planning / DSD 설계론 기획

Status: **Protocol v0.1 / validation in progress**

Date opened: **2026-09-08**

## Purpose / 목적

Develop DSD Design as an independent method that constructs and filters target structures from declared goals and constraints, while preserving the current 22-method boundary discipline.

The method is not treated as mature merely because related DSD methods already have evidence. Shared-core evidence and neighboring-method results may be referenced, but direct Design validation must be accumulated separately.

## Current protocol / 현재 프로토콜

The first executable protocol is established:

- [`PROTOCOL_v0.1.md`](PROTOCOL_v0.1.md)

Its pre-protocol basis is preserved in:

- [`TASK_INTERFACE_v0.1-draft.md`](TASK_INTERFACE_v0.1-draft.md)
- [`TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`](TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md)
- [`BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`](BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md)

## Current task interface / 현재 과업 인터페이스

```text
GOALS
+ HARD_CONSTRAINTS
+ CONSTRAINT_SOURCE_OR_SPECIFICATION
+ BASE_STRUCTURE_OR_PREDECESSOR
+ TARGET_DSD_LAYER_SCOPE
+ TARGET_RESOLUTION
+ CANDIDATE_OR_CONSTRUCTION_BASIS
+ CANDIDATE_GENERATION_RULE
+ CANDIDATE_COVERAGE
+ selected DSD interface
+ explicit DOMAIN_BRIDGE when required
+ EXTERNAL_STANDARD when an external-domain claim is made
+ AUXILIARY_METHODS_OR_HANDOFFS when materially used
-> candidate design family
-> status-sensitive admissibility evaluation
-> admissible target family OR terminal non-success result
```

Design does not assume a universal candidate generator. Domain-specific candidate or construction resources must be supplied explicitly enough to reproduce the space actually used.

## Current terminal-status ledger / 현재 종결 상태 장부

```text
DESIGN_ADMISSIBLE
DESIGN_INFEASIBLE
DESIGN_UNDERDETERMINED
DESIGN_BLOCKED
```

Method gain remains separate:

```text
DESIGN_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

Protocol conformance is a third independent ledger:

```text
DESIGN_PROTOCOL_CONFORMANCE:
  CONFORMANT
  NONCONFORMANT
  UNDETERMINED
```

## Candidate-coverage guard / 후보 범위 보호 규칙

```text
CANDIDATE_COVERAGE: exhaustive / non_exhaustive / unknown
```

`DESIGN_INFEASIBLE` requires either exhaustive candidate coverage with all required candidates rejected or an explicit impossibility argument. Failure to find a candidate in a non-exhaustive search is not enough for a global infeasibility claim.

`DES-CH-002` directly exercises both sides of this rule:

```text
exhaustive + all rejected -> DESIGN_INFEASIBLE
non_exhaustive + none found -> DESIGN_UNDERDETERMINED
```

## Constraint-provenance guard / 제약 출처 보호 규칙

```text
SOFT_PREFERENCE != HARD_CONSTRAINT
```

Design must not silently promote a soft preference into a hard constraint after candidate inspection merely to force a unique result. Any such change must be a new/upstream task revision with provenance.

## Output-level and target-resolution guard / 산출 수준·해상도 보호 규칙

```text
DESIGN_SPACE
ADMISSIBLE_TARGET
UNIQUE_TARGET
PARTIAL_TARGET
```

Multiple admissible targets are an ordinary Design success when the declared output is `DESIGN_SPACE` or `ADMISSIBLE_TARGET`.

If `UNIQUE_TARGET` is requested and multiple materially distinct admissible targets survive without a non-optimization determinacy rule, the Design result is `DESIGN_UNDERDETERMINED`; choosing the best surviving alternative belongs to DSD Optimization.

`DES-CH-003` exposed an additional guardrail that was already implicit in Protocol v0.1 but had not yet been pressure-tested directly:

```text
material target distinctness must be judged at TARGET_RESOLUTION
```

Candidate IDs or downstream-only metadata do not by themselves establish multiple distinct Design targets.
This was preserved as a failed challenge rather than repaired post hoc.

## Method boundary / 방법 경계

- **Specification** locks or exposes requirements, permissions, prohibitions, unresolved conditions, and review scope when used as an upstream input.
- **Design** constructs an admissible target structure or admissible target family under goals and hard constraints.
- **Synthesis** combines already admitted parts or components under a composition rule.
- **Transformation** records preservation, loss, or non-correspondence between source and target structures or regimes.
- **Optimization** selects among already admissible alternatives by an explicit objective or preference criterion.
- **Audit** later retraces the Design execution against its locked scope, inputs, bridges, evidence, and verdict rules.

One workflow may use several methods, but their method verdicts and direct evidence remain separately identifiable.

## Boundary-counterexample result / 경계 반례 결과

```text
BOUNDARY_CASES_RUN: 8
BOUNDARY_PRESERVED_WITHOUT_REFINEMENT: 5
BOUNDARY_PRESERVED_WITH_NONBREAKING_REFINEMENT: 3
EXACT_METHOD_COLLAPSE_FOUND: 0
FUNDAMENTAL_TASK_INTERFACE_FAILURE: 0
DIRECT_EVIDENCE_COUNT_INCREMENT: 0
```

Two non-breaking refinements were required:

1. `CONSTRAINT_SOURCE_OR_SPECIFICATION`
2. `AUXILIARY_METHODS_OR_HANDOFFS`

## Direct pilots / 직접 파일럿

### `DES-CH-001` — positive Design-space pilot

```text
ADMISSIBLE_FAMILY: {T1,T2}
PRECOMMITTED_REQUIRED_CHECKS: 11/11 PASS
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

### `DES-CH-002` — negative/failure terminal-status pilot

```text
Case I -> DESIGN_INFEASIBLE
Case U -> DESIGN_UNDERDETERMINED
Case B -> DESIGN_BLOCKED
PRECOMMITTED_REQUIRED_CHECKS: 20/20 PASS
```

### `DES-CH-003` — first executable Design/Optimization boundary attempt

```text
PRECOMMITTED_REQUIRED_CHECKS: 20/21
CHALLENGE_VERDICT: FAIL_AS_PRECOMMITTED_CHALLENGE
FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
PROTOCOL_FAILURE_INFERRED: no
```

The failed case was preserved without post-hoc repair.

### `DES-CH-004` — corrected Design/Optimization boundary pilot

```text
Case S -> {C1,C2,C3} / DESIGN_ADMISSIBLE
Case U -> DESIGN_UNDERDETERMINED
PRECOMMITTED_REQUIRED_CHECKS: 23/23 PASS
```

### `DES-CH-005` — first NO_GAIN pilot

Baseline:

```text
B0_EXPLICIT_CONSTRAINT_MATRIX
```

Both B0 and DSD returned `{N1,N2}`, rejected `N3` on H2, and preserved N1/N2 distinctness.

```text
G1-G4: not established
DESIGN_ADMISSIBLE / CONFORMANT / NO_GAIN
PRECOMMITTED_REQUIRED_CHECKS: 25/25 PASS
```

This filled the `NO_GAIN` evidence category but remained intentionally simple.

### `DES-CH-006` — broader strongest-reasonable-baseline comparison

Precommit:

```text
DES-CH-006_precommit.md
commit: 3a44350
```

Result:

```text
DES-CH-006_broader-typed-baseline-comparison.md
commit: c3708c3
```

Frozen comparator:

```text
B1_TYPED_ADMISSIBILITY_TABLE
```

Pressure increase over DES-CH-005:

```text
Formation + General Property
15 candidates
seven baseline property-state classes
multi-constraint failure sets
DESIGN_SPACE + UNIQUE_TARGET subcases
explicit structure/property separation
```

Observed result:

```text
Case S:
  B1  -> {A1,A2}
  DSD -> {A1,A2} / DESIGN_ADMISSIBLE

Case U:
  B1  -> NOT_UNIQUE_AT_DECLARED_RESOLUTION
  DSD -> DESIGN_UNDERDETERMINED

candidate failure sets:
  B1 == DSD for A3-A15

G1 status distinction: NOT_ESTABLISHED
G2 rejection traceability: NOT_ESTABLISHED
G3 structure/property separation: NOT_ESTABLISHED
G4 output-level closure: NOT_ESTABLISHED
G5 retraceability: NOT_ESTABLISHED

DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NO_GAIN
PRECOMMITTED_REQUIRED_CHECKS: 54/54 PASS
```

This fills the `baseline_comparison` evidence category at the constructed-evidence level.
It does not establish DSD superiority; the competent baseline matched DSD on all measured frozen dimensions.

Evidence limit for all current pilots: same-project constructed evidence; independent validation remains absent.

## DSD layer policy / DSD 층위 정책

The minimum-layer principle overrides a fixed serial package.

1. **Formation** — active for new structural targets, or explicitly locked as the inherited Stage-VI predecessor for downstream target design.
2. **General Property** — activated only when typed property declaration, applicability, contextual prerequisites, or partial property assignment matter to the target.
3. **Static Aggregation** — activated only when a candidate is evaluated through a declared analytic readout or aggregate.
4. **Dynamics** — activated only when trajectory, transition, lineage, propagation, or other time-dependent requirements matter.
5. **Optional specialization** — activated only through explicit supplied specialization/domain data.

No bridge is inferred from a property name, intuition, or shared vocabulary alone.

## Development sequence / 개발 순서

1. ✅ Lock the Design-specific task interface and minimum valid output at draft level.
2. ✅ Build boundary counterexamples against Specification, Synthesis, Transformation, and Optimization; incorporate non-breaking refinements.
3. ✅ Establish `PROTOCOL_v0.1.md`.
4. ✅ Run first positive constructed pilot: `DES-CH-001` PASS.
5. ✅ Run first negative/failure constructed pilot: `DES-CH-002` PASS.
6. ✅ Run executable boundary stage: `DES-CH-003` failed test design preserved; corrected `DES-CH-004` PASS.
7. ✅ Run first `NO_GAIN` pilot: `DES-CH-005` PASS.
8. ✅ Run broader strongest-reasonable-baseline comparison: `DES-CH-006` PASS / `NO_GAIN`.
9. **Next:** run at least one external or independently generated application case.
10. Record reproducibility/retrace results.
11. Run a DSD Audit maturity review.

## Evidence rule / 증거 규칙

Direct Design evidence is stored under:

`evidence/method_specific/design/`

The minimum promotion architecture follows the repository-wide method-specific evidence rule:

- dedicated protocol;
- positive case;
- negative/failure case;
- boundary case;
- `NO_GAIN` case;
- reproducibility record;
- at least one external or independently generated application;
- strongest-reasonable-baseline comparison when applicable.

Current architecture status:

```text
DEDICATED_PROTOCOL: established
POSITIVE_CASE: established
NEGATIVE_OR_FAILURE_CASE: established
BOUNDARY_CASE: established with one preserved failed predecessor test
NO_GAIN_CASE: established
STRONGEST_REASONABLE_BASELINE_COMPARISON: established at constructed level
EXTERNAL_OR_INDEPENDENT_APPLICATION: not established
REPRODUCIBILITY_RECORD: case-level records exist; dedicated retrace stage not yet completed
MATURITY_AUDIT: not performed
```

Current direct evidence state:

```text
DEDICATED_PROTOCOL: v0.1 established
DIRECT_CONSTRUCTED_PILOTS: 6
POSITIVE_CASES: 1
NEGATIVE_OR_FAILURE_CASES: 1
BOUNDARY_CASES_UNDER_PROTOCOL: 2 attempted
BOUNDARY_VALIDATION_PASSES: 1
BOUNDARY_TEST_DESIGN_FAILURES: 1
NO_GAIN_CASES: 1
NO_GAIN_VALIDATION_PASSES: 1
BASELINE_COMPARISON_CASES: 1
BASELINE_COMPARISON_PASSES: 1
BASELINE_COMPARISON_RESULT: NO_GAIN
EXTERNAL_APPLICATIONS: 0
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

## Recording rule / 기록 규칙

Historical runs are preserved under the protocol version used at execution time; later protocol revisions or corrected challenges do not rewrite earlier results.

`DES-CH-003 -> DES-CH-004` is the current explicit example of this rule.

## Next step / 다음 단계

Run the first **external or independently generated Design application** under Protocol v0.1.

The case should freeze an external source corpus and its actual requirements before Design execution, identify a reproducible candidate/construction basis, and keep source/domain authority separate from DSD-internal admissibility and method-gain ledgers.
