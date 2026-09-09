# DSD Synthesis Planning / DSD 합성론 기획

Status: **planning / proposed / Step 1 complete**  
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

Key source-derived constraints:

```text
Formation Clause VII finite composition
!= universal domain composability

component property
!= automatic whole property

aggregate equality/readout
!= structural synthesis equality
```

The Synthesis method must record explicit bridges and composition rules rather than infer them from names or coexistence.

## Current task definition / 현재 과업 정의

**Input:** supplied components, their identities/status records, an explicit composition rule and its source, composition candidate basis/coverage, cross-component prerequisites, target resolution, active DSD layers, and domain validation criteria.

**Operation:** check component eligibility, lock arity/order/multiplicity, test interfaces/prerequisites, apply the supplied composition rule, audit support/relation/status retention and information loss, determine formation effect, and construct the synthesis-admissible family.

**Output:** synthesis space or target, candidate rejection basis, retention/loss record, formation-effect record, terminal Synthesis status, protocol conformance, method-gain status, handoffs, limits, and reproducibility data.

## Initial output levels / 초기 산출 수준

```text
SYNTHESIS_SPACE
SYNTHESIZED_TARGET
UNIQUE_SYNTHESIZED_TARGET
PARTIAL_SYNTHESIS
```

## Initial terminal statuses / 초기 종결 상태

```text
SYNTHESIS_ADMISSIBLE
SYNTHESIS_INFEASIBLE
SYNTHESIS_UNDERDETERMINED
SYNTHESIS_BLOCKED
```

`SYNTHESIS_INFEASIBLE` requires exhaustive composition coverage or an explicit impossibility argument.
Non-exhaustive failure-to-find is not global infeasibility.

## Three-ledger separation / 3중 장부 분리

```text
TERMINAL_SYNTHESIS_STATUS

SYNTHESIS_PROTOCOL_CONFORMANCE:
  CONFORMANT
  NONCONFORMANT
  UNDETERMINED

SYNTHESIS_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

Maturity is a later DSD Audit decision and is not inferred from these ledgers.

## Main method boundaries / 핵심 방법 경계

### Design

Design creates or filters a target/design space from goals and constraints.
Synthesis consumes supplied parts and a supplied composition rule to build a larger whole/composition space.

### Transformation

Transformation maps a source to a target representation/regime.
Synthesis combines multiple parts into one larger construction.

### Aggregation

Aggregation produces a declared readout.
Synthesis requires substantive composition legitimacy, not merely a finite sum or shared scalar output.

### Optimization

Synthesis forms legitimate compositions.
Optimization ranks or selects among already legitimate alternatives under an objective.

### Audit

Audit retraces whether Synthesis followed the frozen rule; Audit does not become the Synthesis verdict.

## Development sequence / 개발 순서

1. ✅ Define the Synthesis-specific task interface and minimum valid output — `TASK_INTERFACE_v0.1-draft.md`.
2. **Next:** construct boundary counterexamples against Design, Transformation, Aggregation, Optimization, and implicit component-to-whole property lifting.
3. Apply only counterexample-required non-breaking interface refinements.
4. Freeze the first executable `Synthesis Protocol v0.1`.
5. Run a separately precommitted positive constructed Synthesis challenge.
6. Run negative/failure terminal-status challenge(s).
7. Run direct method-boundary challenge(s).
8. Run first `NO_GAIN` case with a competent baseline and precommitted gain criterion.
9. Run a broader strongest-reasonable-baseline comparison.
10. Run at least one external/domain application where composition legitimacy is supplied by an external rule/artifact.
11. Add a dedicated reproducibility/retrace record.
12. Perform DSD Audit maturity review only after the method-specific evidence architecture is materially populated.
13. Prepare independent-evaluator infrastructure only when a stable protocol and sufficient direct evidence justify it.

## Step 1 result / 1단계 결과

The initial task interface now locks:

```text
SYNTHESIS_TASK_ID
TASK_SCOPE
CLAIMED_OUTPUT_LEVEL
TARGET_RESOLUTION
COMPONENT_SET_OR_FAMILY
COMPONENT_IDENTITY_RECORDS
COMPONENT_STATUS_OR_ADMISSION_SOURCE
COMPOSITION_RULE
COMPOSITION_RULE_SOURCE
COMPOSITION_ARITY
COMPOSITION_ORDER_SENSITIVITY
MULTIPLICITY_POLICY
COMPOSITION_CANDIDATE_BASIS
COMPOSITION_COVERAGE
INTERFACE_MATCHING_RULES
CROSS_COMPONENT_PREREQUISITES
PROPERTY_LIFT_OR_REDECLARATION_RULE
SUPPORT_RETENTION_REQUIREMENT
RELATION_RETENTION_REQUIREMENT
INFORMATION_LOSS_TOLERANCE
NEW_FORMATION_MODEL_POLICY
TARGET_DSD_LAYER_SCOPE
DSD_INTERFACE_PROFILE
DOMAIN_BRIDGE
EXTERNAL_STANDARD
VALIDATION_OR_ACCEPTANCE_RULE
AUXILIARY_METHODS_OR_HANDOFFS
```

Important distinctions established at planning level:

```text
INDIVIDUAL_COMPONENT_ADMISSIBILITY
!= AUTOMATIC_COMPOSABILITY

EXHAUSTIVE_COMPONENT_LIST
!= EXHAUSTIVE_COMPOSITION_SPACE

FORMATION_CLAUSE_VII_COMPOSITION
!= DOMAIN_SYNTHESIS_LEGITIMACY

AGGREGATE_READOUT
!= SYNTHESIZED_WHOLE

COMPONENT_PROPERTY
!= WHOLE_PROPERTY
```

These distinctions are hypotheses/guards for the upcoming boundary attacks; they are not yet direct validation evidence.

## Evidence state after Step 1 / 1단계 후 증거 상태

```text
DEDICATED_SYNTHESIS_PROTOCOL: not established
DIRECT_SYNTHESIS_PILOTS: 0
POSITIVE_SYNTHESIS_CASES: 0
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 0
BOUNDARY_SYNTHESIS_CASES: 0
NO_GAIN_SYNTHESIS_CASES: 0
BASELINE_COMPARISON_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_pending
```

## Recording rule / 기록 규칙

- Shared-core and neighboring-method evidence may be referenced but do not automatically become direct Synthesis validation.
- Historical planning/boundary failures remain preserved and are corrected prospectively under new case IDs or amendment records.
- No baseline superiority is claimed without a frozen baseline and gain criterion.
- No external authority is replaced by DSD terminology.
- No Formation Clause VII or Static Aggregation result is upgraded into domain composability without an explicit composition rule/bridge.
