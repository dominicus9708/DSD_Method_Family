# DSD Synthesis Planning / DSD 합성론 기획

Status: **Protocol v0.1 established / proposed maturity / validation pending**  
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

The Synthesis method records explicit bridges and composition rules rather than inferring them from names or coexistence.

## Protocol lineage / 프로토콜 계보

Historical planning artifacts remain preserved:

```text
TASK_INTERFACE_v0.1-draft.md
BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md
TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
```

The executable protocol is now:

```text
PROTOCOL_v0.1.md
```

Lineage:

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

The protocol integrates the four refinement groups revealed by the 16 pre-protocol attacks without rewriting the earlier artifacts.

## Current task definition / 현재 과업 정의

**Input:** supplied components and identity/status records; an explicit composition rule and source; arity/order/multiplicity and supplied composition-law profile; grouping policy; composition candidate basis/coverage; target resolution and equivalence rule; interface/prerequisite rules; property-lift rules; retention/loss criteria; formation policy; process scope; active DSD layers and domain criteria.

**Operation:** lock all claim-relevant inputs before outcome inspection; verify component status; test interfaces/prerequisites; apply only the supplied composition rule and supplied algebraic laws; evaluate property lift, retention/loss, formation effect, residual obligations, and process scope; build the admissible family; judge material target distinctness under the frozen equivalence rule; assign terminal status, conformance, and gain separately.

**Output:** synthesis space/target or non-success basis; candidate failure sets; retention/loss and formation-effect records; residual obligations when partial; process-scope/lineage record when applicable; three separate ledgers; handoffs, limits, and reproducibility record.

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
4. ✅ Freeze the first executable `Synthesis Protocol v0.1` — `PROTOCOL_v0.1.md`, commit `8787b24`.
5. **Next:** run a separately precommitted positive constructed Synthesis challenge `SYN-CH-001`.
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

The Step-1 interface was attacked with 16 pre-protocol cases spanning Design, Transformation, Aggregation, Optimization, component-to-whole Property lifting, composition-law assumptions, target equivalence, partial residuals, process scope, exhaustiveness, and Formation/domain-composition separation.

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

## Protocol v0.1 establishment / 실행 프로토콜 동결

Protocol v0.1 incorporates the effective Step-2 interface into an executable S1-S17 sequence.
It additionally operationalizes the already stated non-optimization target-selection rule as:

```text
NONOPTIMIZATION_SELECTION_RULE_IF_NEEDED
```

and conditionally records:

```text
LINEAGE_OR_TRANSITION_CHECK
```

when a time-resolved assembly process contains formation-level identity change.

Key protocol locks before outcome inspection include:

```text
component identities/status sources
composition rule and source
arity/order/multiplicity
supplied algebraic-law profile
grouping/parenthesization
candidate basis and composition coverage
target resolution
equivalence/canonicalization rule
interface/prerequisite rules
property-lift/redeclaration rule
retention/loss conditions
formation-model policy
assembly process scope
active DSD layers and domain bridge/standard
```

No direct evidence is credited merely for protocol establishment.

## Evidence state after Protocol v0.1 / 프로토콜 동결 후 증거 상태

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
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
- The Step-1 task-interface and Step-2 attack/amendment files are not rewritten to hide chronology.
- No baseline superiority is claimed without a frozen baseline and gain criterion.
- No external authority is replaced by DSD terminology.
- No Formation Clause VII or Static Aggregation result is upgraded into domain composability without an explicit composition rule/bridge.
- No static composability result is upgraded into time-resolved assembly feasibility without an explicit process scope/model.
- Protocol v0.1 is revised only prospectively if direct evidence exposes a genuine protocol defect.
