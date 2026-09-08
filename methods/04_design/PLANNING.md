# DSD Design Planning / DSD 설계론 기획

Status: **planning / proposed**

Date opened: **2026-09-08**

## Purpose / 목적

Develop DSD Design as an independent method that constructs and filters target structures from declared goals and constraints, while preserving the current 22-method boundary discipline.

The method is not treated as mature merely because related DSD methods already have evidence. Shared-core evidence and neighboring-method results may be referenced, but direct Design validation must be accumulated separately.

## Task-interface status / 과업 인터페이스 상태

Planning Steps 1-2 are complete at draft level.

Current effective pre-protocol interface:

- [`TASK_INTERFACE_v0.1-draft.md`](TASK_INTERFACE_v0.1-draft.md)
- [`TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`](TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md)
- Boundary attack record: [`BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`](BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md)

The draft now fixes:

- the minimum well-formed Design input record;
- candidate/construction-basis requirements;
- candidate-coverage discipline;
- DSD layer activation rules;
- Design-specific operations D1-D8;
- minimum valid execution outputs;
- terminal Design statuses;
- separation of Design status from method-gain / `NO_GAIN` status;
- the boundary against Optimization when multiple admissible alternatives remain;
- constraint provenance and prohibition of silent soft-to-hard promotion;
- explicit auxiliary-method/handoff recording when Synthesis, Transformation, Optimization, Audit, or another method materially supplies a verdict.

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

The earlier provisional `DESIGN_ACCEPTED` label is retired in favor of `DESIGN_ADMISSIBLE`, because Design itself does not imply downstream approval, optimality, or external validation.

`NO_GAIN` is kept in a separate method-gain ledger:

```text
DESIGN_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

This prevents a structurally admissible design result from being confused with the question of whether DSD added methodological value over a reasonable baseline.

## Candidate-coverage guard / 후보 범위 보호 규칙

Record:

```text
CANDIDATE_COVERAGE: exhaustive / non_exhaustive / unknown
```

`DESIGN_INFEASIBLE` requires either exhaustive candidate coverage with all required candidates rejected or an explicit impossibility argument. Failure to find a candidate in a non-exhaustive search is not enough for a global infeasibility claim.

## Constraint-provenance guard / 제약 출처 보호 규칙

Design may consume hard constraints from an explicit task owner, Specification result, theorem, domain standard, physical/technical limit, or other declared source.

Design itself must not silently promote a soft preference into a hard constraint after seeing the candidate space merely to force a unique result.

Any such change must be a new/upstream task revision with provenance.

```text
SOFT_PREFERENCE != HARD_CONSTRAINT
```

## Output-level guard / 산출 수준 보호 규칙

Recommended output claims are:

```text
DESIGN_SPACE
ADMISSIBLE_TARGET
UNIQUE_TARGET
PARTIAL_TARGET
```

Multiple admissible targets are an ordinary Design success when the declared output is `DESIGN_SPACE` or `ADMISSIBLE_TARGET`.

If `UNIQUE_TARGET` is requested and multiple materially distinct admissible targets survive without a non-optimization determinacy rule, the Design result is `DESIGN_UNDERDETERMINED`; choosing the best surviving alternative belongs to DSD Optimization.

## Method boundary / 방법 경계

- **Specification** locks or exposes requirements, permissions, prohibitions, unresolved conditions, and review scope when used as an upstream input.
- **Design** constructs an admissible target structure or admissible target family under goals and hard constraints.
- **Synthesis** combines already admitted parts or components under a composition rule.
- **Transformation** records preservation, loss, or non-correspondence between source and target structures or regimes.
- **Optimization** selects among already admissible alternatives by an explicit objective or preference criterion.
- **Audit** later retraces the Design execution against its locked scope, inputs, bridges, evidence, and verdict rules.

One workflow may use several methods, but their method verdicts and direct evidence remain separately identifiable.

When a substantive neighboring-method verdict is needed, record it under:

```text
AUXILIARY_METHODS_OR_HANDOFFS:
```

Design may consume the result without absorbing the neighboring method.

## Boundary-counterexample result / 경계 반례 결과

The first boundary attack used eight pre-protocol cases.

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

No rewrite of the Design task identity was required.

## DSD layer policy / DSD 층위 정책

The minimum-layer principle overrides a fixed serial package.

1. **Formation** — active for new structural targets, or explicitly locked as the inherited Stage-VI predecessor for downstream target design.
2. **General Property** — activated only when typed property declaration, applicability, contextual prerequisites, or partial property assignment matter to the target.
3. **Static Aggregation** — activated only when a candidate is evaluated through a declared analytic readout or aggregate.
4. **Dynamics** — activated only when trajectory, transition, lineage, propagation, or other time-dependent requirements matter.
5. **Optional specialization** — activated only through explicit supplied specialization/domain data.

No bridge is inferred from a property name, intuition, or shared vocabulary alone.

## Independence questions / 독립성 판정 질문

1. Can the method construct or filter a target family from an explicit goal/constraint and candidate/construction interface?
2. Can candidate rejection be traced to explicit Formation, Property, bridge, or domain constraints?
3. Does the output include a target structure, admissible design family, or justified terminal non-success result rather than only an analysis report or specification table?
4. Can a minimal Design task exist without requiring Synthesis, Transformation, or Optimization?
5. Does the method explicitly stop where domain design knowledge or candidate-generation resources are absent rather than inventing domain rules?
6. Does the method distinguish failure to find a candidate from a justified infeasibility claim?
7. Does the method avoid turning multiple admissible alternatives into an implicit optimization problem?
8. Does it preserve constraint provenance rather than silently converting soft preferences into hard constraints?
9. When another method supplies a substantive verdict, is the handoff visible rather than absorbed into Design?

## Development sequence / 개발 순서

1. ✅ Lock the Design-specific task interface and minimum valid output at draft level.
2. ✅ Build boundary counterexamples against Specification, Synthesis, Transformation, and Optimization; incorporate non-breaking refinements.
3. **Next:** draft `PROTOCOL_v0.1.md` from the effective boundary-refined interface.
4. Run a positive constructed pilot.
5. Run a negative/failure pilot.
6. Run a boundary pilot under the protocol.
7. Run a `NO_GAIN` pilot.
8. Compare against a strongest reasonable baseline where applicable.
9. Run at least one external or independently generated application case.
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

These are minimum evidence categories, not an automatic maturity grant.

The task-interface and pre-protocol boundary artifacts are planning records and do not count as direct pilots.

## Recording rule / 기록 규칙

Each later execution should preserve at minimum:

```text
DESIGN_TASK_ID
TASK_SCOPE
CLAIMED_OUTPUT_LEVEL
GOALS
HARD_CONSTRAINTS
CONSTRAINT_SOURCE_OR_SPECIFICATION
BASE_STRUCTURE_OR_PREDECESSOR
TARGET_DSD_LAYER_SCOPE
TARGET_RESOLUTION
CANDIDATE_OR_CONSTRUCTION_BASIS
CANDIDATE_GENERATION_RULE
CANDIDATE_COVERAGE
DSD_INTERFACE_PROFILE
DOMAIN_BRIDGE
EXTERNAL_STANDARD
AUXILIARY_METHODS_OR_HANDOFFS
CANDIDATES_ACTUALLY_EVALUATED_OR_SYMBOLIC_FAMILY
CANDIDATE_STATUS_RECORD
ADMISSIBLE_TARGETS_OR_ADMISSIBLE_FAMILY
REJECTED_CANDIDATE_REASONS
UNRESOLVED_FIELDS
TERMINAL_DESIGN_STATUS
TERMINAL_STATUS_BASIS
DESIGN_METHOD_GAIN_STATUS
LIMITS
REPRODUCIBILITY_RECORD
```

Historical runs are preserved under the protocol version used at execution time; later protocol revisions do not rewrite earlier results.

## Next step / 다음 단계

Draft the first executable **`PROTOCOL_v0.1.md`** from the effective interface:

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
```
