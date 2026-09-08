# DSD Design Planning / DSD 설계론 기획

Status: **Protocol v0.1 established / validation pending**

Date opened: **2026-09-08**

## Purpose / 목적

Develop DSD Design as an independent method that constructs and filters target structures from declared goals and constraints, while preserving the current 22-method boundary discipline.

The method is not treated as mature merely because a protocol now exists. Shared-core evidence and neighboring-method results may be referenced, but direct Design validation must be accumulated separately.

## Completed planning basis / 완료된 기획 기반

Planning Steps 1-2 are complete.

Pre-protocol sources:

- [`TASK_INTERFACE_v0.1-draft.md`](TASK_INTERFACE_v0.1-draft.md)
- [`TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`](TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md)
- [`BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`](BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md)

These established:

- minimum well-formed Design inputs;
- candidate/construction-basis requirements;
- candidate-coverage discipline;
- DSD layer activation rules;
- terminal Design statuses;
- separation of Design outcome, protocol conformance, and method gain;
- constraint provenance and prohibition of silent soft-to-hard promotion;
- auxiliary-method/handoff recording;
- method boundaries against Specification, Synthesis, Transformation, Optimization, and later Audit.

## Current executable protocol / 현재 실행 프로토콜

- [`PROTOCOL_v0.1.md`](PROTOCOL_v0.1.md)

Protocol v0.1 is the first executable Design protocol.
It is not a maturity or external-validity claim.

### Core task interface

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

Design does not assume a universal candidate generator. Domain-specific candidate or construction resources must be supplied explicitly enough to reproduce the covered space actually used.

### Claimed output levels

```text
DESIGN_SPACE
ADMISSIBLE_TARGET
UNIQUE_TARGET
PARTIAL_TARGET
```

A `DESIGN_SPACE` result is always relative to declared candidate coverage. A global completeness claim requires an independently justified exhaustive basis.

### Terminal Design status

```text
DESIGN_ADMISSIBLE
DESIGN_INFEASIBLE
DESIGN_UNDERDETERMINED
DESIGN_BLOCKED
```

### Protocol conformance

```text
DESIGN_PROTOCOL_CONFORMANCE:
  CONFORMANT
  NONCONFORMANT
  UNDETERMINED
```

### Method gain

```text
DESIGN_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

These three ledgers are intentionally distinct.

## Candidate-coverage guard / 후보 범위 보호 규칙

Record:

```text
CANDIDATE_COVERAGE: exhaustive / non_exhaustive / unknown
```

`DESIGN_INFEASIBLE` requires either exhaustive candidate coverage with all required candidates rejected or an explicit impossibility argument. Failure to find a candidate in a non-exhaustive or unknown search is not enough for a global infeasibility claim.

## Constraint-provenance guard / 제약 출처 보호 규칙

Design may consume hard constraints from an explicit task owner, Specification result, theorem, domain standard, physical/technical limit, or other declared source.

Design itself must not silently promote a soft preference into a hard constraint after seeing the candidate space merely to force a unique result.
Any such change must be a new/upstream task revision with provenance.

```text
SOFT_PREFERENCE != HARD_CONSTRAINT
```

## Method boundary / 방법 경계

- **Specification** locks or exposes requirements, permissions, prohibitions, unresolved conditions, and review scope when used as an upstream input.
- **Design** constructs an admissible target structure or admissible target family under goals and hard constraints.
- **Synthesis** combines already admitted parts or components under a composition rule.
- **Transformation** records preservation, loss, or non-correspondence between source and target structures or regimes.
- **Optimization** selects among already admissible alternatives by an explicit objective or preference criterion.
- **Audit** later retraces the Design execution against its locked scope, inputs, bridges, evidence, and verdict rules.

One workflow may use several methods, but method-specific verdicts and evidence remain separately identifiable.

## DSD layer policy / DSD 층위 정책

The minimum-layer principle overrides a fixed serial package.

1. **Formation** — active for new structural targets, or explicitly locked as an inherited Stage-VI predecessor for downstream target design.
2. **General Property** — activated only when typed property declaration, applicability, contextual prerequisites, or partial property assignment matter to the target.
3. **Static Aggregation** — activated only when a candidate is evaluated through a declared analytic readout or aggregate.
4. **Dynamics** — activated only when trajectory, transition, lineage, propagation, or other time-dependent requirements matter.
5. **Optional specialization** — activated only through explicit supplied specialization/domain data.

No bridge is inferred from a property name, intuition, or shared vocabulary alone.

## Protocol v0.1 procedure / 프로토콜 v0.1 절차

```text
D1  LOCK TASK AND CLAIM
D2  LOCK CONSTRAINT SOURCES
D3  LOCK CANDIDATE / CONSTRUCTION BASIS AND COVERAGE
D4  LOCK SELECTED DSD INTERFACES AND REQUIRED BRIDGES
D5  CONSTRUCT / ENUMERATE COVERED CANDIDATES
D6  RUN STATUS-SENSITIVE DSD ADMISSIBILITY CHECKS
D7  RUN DOMAIN / EXTERNAL / AUXILIARY-METHOD CHECKS WHEN ACTIVE
D8  CONSTRUCT ADMISSIBLE FAMILY
D9  CHECK CLAIMED OUTPUT LEVEL
D10 ASSIGN TERMINAL DESIGN STATUS
D11 RECORD PROTOCOL CONFORMANCE SEPARATELY
D12 RECORD METHOD-GAIN STATUS SEPARATELY
D13 RECORD LIMITS AND REPRODUCIBILITY DATA
```

## Evidence convention / 증거 규칙

Protocol v0.1 fixes:

```text
DES-CH-###   constructed Design challenges
DES-APP-###  external or independently generated Design applications
DES-AUD-###  Design-specific audit / maturity records
```

Every case additionally records `CASE_CLASS`, such as positive, negative/failure, boundary, no_gain, baseline comparison, reproducibility, or external application.

Direct Design evidence is stored under:

`evidence/method_specific/design/`

Planning artifacts remain planning records and are not retroactively counted as direct v0.1 pilots.

## Development sequence / 개발 순서

1. ✅ Lock the Design-specific task interface and minimum valid output at draft level.
2. ✅ Build boundary counterexamples and incorporate non-breaking refinements.
3. ✅ Establish executable `PROTOCOL_v0.1.md`.
4. **Next:** run the first positive constructed Design challenge under a frozen Protocol v0.1 task record.
5. Run a negative/failure pilot.
6. Run a boundary pilot under the protocol.
7. Run a `NO_GAIN` pilot.
8. Compare against a strongest reasonable baseline where applicable.
9. Run at least one external or independently generated application case.
10. Record reproducibility/retrace results.
11. Run a DSD Audit maturity review.

## Current evidence state / 현재 증거 상태

```text
DEDICATED_PROTOCOL: v0.1 established
DIRECT_CONSTRUCTED_PILOTS: 0
EXTERNAL_APPLICATIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
METHOD_EVIDENCE_STATUS: validation_pending
```

Protocol establishment is an infrastructure milestone, not direct validation.

## Next step / 다음 단계

Construct and pre-lock the first **positive Design challenge** so that Protocol v0.1 can be tested on a case where at least one admissible target should exist without invoking hidden Optimization.
