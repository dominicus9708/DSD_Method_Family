# DSD Synthesis Planning / DSD 합성론 기획

Status: **planning / proposed / Step 2 boundary attack complete**  
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

## Current effective pre-protocol interface / 현재 유효 pre-protocol 인터페이스

Step 1 remains preserved as its historical draft.
Step 2 adds a separate non-breaking amendment rather than rewriting the pre-attack artifact.

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
```

Boundary-attack record:

```text
BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md
```

## Current task definition / 현재 과업 정의

**Input:** supplied components, their identities/status records, an explicit composition rule and its source, composition candidate basis/coverage, cross-component prerequisites, target resolution, active DSD layers, and domain validation criteria.

**Operation:** check component eligibility, lock arity/order/multiplicity and supplied composition laws, test interfaces/prerequisites, apply the supplied rule under the declared grouping policy, audit support/relation/status retention and information loss, preserve residual obligations for partial synthesis, determine formation effect, and construct the synthesis-admissible family.

**Output:** synthesis space or target, candidate rejection basis, retention/loss record, formation-effect record, residual-obligation record when partial, terminal Synthesis status, protocol conformance, method-gain status, handoffs, limits, and reproducibility data.

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

Maturity is evaluated separately by DSD Audit.

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

### Dynamics / process scope

Static Synthesis may establish a final composition without establishing the feasibility of a time-resolved assembly sequence.
If transient states or process timing are claim-relevant, Dynamics or an explicit domain process model is a separate activated interface/handoff.

### Audit

Audit retraces whether Synthesis followed the frozen rule; Audit does not become the Synthesis verdict.

## Development sequence / 개발 순서

1. ✅ Define the Synthesis-specific task interface and minimum valid output — `TASK_INTERFACE_v0.1-draft.md`.
2. ✅ Run pre-protocol boundary attacks — 16 cases; 11 preserved without refinement, 5 preserved with non-breaking refinement, 0 boundary collapse, 0 fundamental interface failure.
3. ✅ Record required non-breaking refinements separately — `TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`.
4. **Next:** freeze the first executable `Synthesis Protocol v0.1` from the effective Step-2 interface.
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

The initial task interface locked the supplied-part/composition-rule model, candidate coverage, component status, interface prerequisites, property-lift discipline, retention/loss checks, formation effect, output levels, terminal states, and three separate ledgers.

Important Step-1 guards:

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

## Step 2 result / 2단계 결과

The Step-1 interface was attacked with 16 pre-protocol cases spanning:

```text
Design handoff / hidden Design
Transformation-only and Transformation handoff
Aggregation-only and Aggregation handoff
Optimization selection
component-to-whole Property lifting
commutativity
associativity / parenthesization
identity / idempotence
composition equivalence / canonicalization
partial-synthesis residual obligations
static versus temporal assembly feasibility
component-list versus composition-space exhaustiveness
Formation Clause VII versus domain synthesis legitimacy
```

Aggregate result:

```text
BOUNDARY_ATTACKS_RUN: 16
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
DIRECT_SYNTHESIS_PILOT_INCREMENT: 0
```

Four refinement groups were required:

```text
R1 COMPOSITION_LAW_PROFILE
   GROUPING_OR_PARENTHESIZATION_POLICY

R2 COMPOSITION_EQUIVALENCE_OR_CANONICALIZATION_RULE

R3 RESIDUAL_OPEN_INTERFACES_OR_OBLIGATIONS

R4 ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE
```

Key new guards:

```text
A ⊙ B notation
!= supplied commutativity/associativity/identity/idempotence

candidate ID or syntax tree
!= material synthesized-target distinctness

PARTIAL_SYNTHESIS
!= completed synthesized target

STATIC_COMPOSITION_ORDER
!= TEMPORAL_ASSEMBLY_SEQUENCE
```

The attack did not force Synthesis to absorb a neighboring method.
The refinements improve explicitness while preserving the Step-1 method identity.

## Evidence state after Step 2 / 2단계 후 증거 상태

```text
DEDICATED_SYNTHESIS_PROTOCOL: not established
DIRECT_SYNTHESIS_PILOTS: 0
POSITIVE_SYNTHESIS_CASES: 0
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 0
BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 0
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
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
- Historical planning/boundary failures remain preserved and are corrected prospectively through amendment or new case records.
- The Step-1 task-interface file is not rewritten to hide the boundary-pressure chronology.
- No baseline superiority is claimed without a frozen baseline and gain criterion.
- No external authority is replaced by DSD terminology.
- No Formation Clause VII or Static Aggregation result is upgraded into domain composability without an explicit composition rule/bridge.
- No static composability result is upgraded into time-resolved assembly feasibility without an explicit process scope/model.
