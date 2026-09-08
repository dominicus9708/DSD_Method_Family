# DSD Design Planning / DSD 설계론 기획

Status: **planning / proposed**

Date opened: **2026-09-08**

## Purpose / 목적

Develop DSD Design as an independent method that constructs and filters target structures from declared goals and constraints, while preserving the current 22-method boundary discipline.

The method is not treated as mature merely because related DSD methods already have evidence. Shared-core evidence and neighboring-method results may be referenced, but direct Design validation must be accumulated separately.

## Initial task interface / 초기 과업 인터페이스

```text
GOAL
+ CONSTRAINTS
+ INPUTS
+ selected DSD layers
+ explicit DOMAIN_BRIDGE when required
+ EXTERNAL_STANDARD when an external-domain claim is made
-> CANDIDATE DESIGN SPACE
-> admissibility / describability checks
-> applicability / prerequisite checks
-> property and channel / bridge requirements
-> output / trajectory requirements
-> selected target design, rejected-candidate reasons, or failure / NO_GAIN result
```

## Initial method boundary / 초기 방법 경계

- **Specification** locks or exposes requirements, permissions, prohibitions, unresolved conditions, and review scope when used as an upstream input.
- **Design** constructs a target structure under goals and constraints.
- **Synthesis** combines already admitted parts or components.
- **Transformation** records preservation, loss, or non-correspondence between source and target structures or regimes.
- **Optimization** selects among candidates by an explicit objective or preference criterion.

One workflow may use several methods, but their method verdicts and direct evidence remain separately identifiable.

## DSD layer policy / DSD 층위 정책

Primary layers:

1. Formation
2. General Property

Optional layers:

3. Static Aggregation — only when candidate evaluation or reduced readout is actually required.
4. Dynamics — only when trajectory, transition, lineage, control-related, or time-dependent requirements are part of the design task.
5. Optional specialization — only through an explicit domain or geometric bridge.

No bridge is inferred from a property name, intuition, or shared vocabulary alone.

## Initial design-state candidates / 초기 판정 상태 후보

These labels are provisional until Protocol v0.1 is tested against counterexamples.

```text
DESIGN_ACCEPTED
DESIGN_INFEASIBLE
DESIGN_UNDERDETERMINED
DESIGN_BLOCKED
DESIGN_NO_GAIN
```

Working meanings:

- `DESIGN_ACCEPTED`: a target structure is selected under the declared goal, constraints, and validation conditions.
- `DESIGN_INFEASIBLE`: no candidate in the declared design space satisfies the required conditions.
- `DESIGN_UNDERDETERMINED`: the available goal, constraints, or evaluation criteria do not distinguish admissible candidates sufficiently for the claimed selection.
- `DESIGN_BLOCKED`: required input, prerequisite, domain bridge, or external standard is unavailable for the claimed task.
- `DESIGN_NO_GAIN`: DSD structuring adds no material discrimination, traceability, or reproducibility gain over a strongest reasonable baseline for the declared task.

## Independence questions / 독립성 판정 질문

1. Can the method generate or distinguish more than one target candidate from the same declared goal/constraint interface?
2. Can candidate rejection be traced to explicit Formation, Property, bridge, or domain constraints?
3. Does the output include a target structure or design-space result rather than only an analysis report or specification table?
4. Can a minimal Design task exist without requiring Synthesis, Transformation, or Optimization?
5. Does the method explicitly stop where domain design knowledge is absent rather than inventing domain rules?

## Development sequence / 개발 순서

1. Lock the Design-specific task interface and minimum output.
2. Build boundary counterexamples against Specification, Synthesis, Transformation, and Optimization.
3. Draft `PROTOCOL_v0.1.md`.
4. Run a positive constructed pilot.
5. Run a negative/failure pilot.
6. Run a boundary pilot.
7. Run a `NO_GAIN` pilot.
8. Compare against a strongest reasonable baseline where applicable.
9. Run at least one external or independently generated application case.
10. Record reproducibility/retrace results.
11. Run a DSD Audit maturity review.

## Evidence rule / 증거 규칙

Direct Design evidence will be stored under:

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

## Recording rule / 기록 규칙

Each development step should preserve:

```text
METHOD_VERSION_OR_PROTOCOL
TASK
GOAL
CONSTRAINTS
INPUTS
DSD_LAYERS_USED
DOMAIN_BRIDGE
EXTERNAL_STANDARD
CANDIDATE_GENERATION_RULE
ADMISSIBILITY_CHECK
PROPERTY_AND_PREREQUISITE_CHECK
CHANNEL_OR_BRIDGE_REQUIREMENTS
OUTPUT_OR_TRAJECTORY_REQUIREMENTS
SELECTION_RULE
REJECTED_CANDIDATE_REASONS
INFORMATION_LOSS_CHECK
LINEAGE_OR_TRANSITION_CHECK
FAILURE_OR_NO_GAIN_CRITERIA
RESULT
LIMITS
REPRODUCIBILITY_RECORD
```

Historical runs are preserved under the protocol version used at execution time; later protocol revisions do not rewrite earlier results.

## First next step / 첫 다음 단계

Define the **Design-specific task interface and minimum valid output** before drafting Protocol v0.1.
