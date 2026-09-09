# DSD Synthesis Task Interface Boundary Amendment 001 / DSD 합성론 과업 인터페이스 경계 보강 001

Status: **planning amendment — non-breaking Step-2 refinement**  
Date: **2026-09-10**  
Base interface: `TASK_INTERFACE_v0.1-draft.md`  
Trigger artifact: `BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`

## 1. Purpose / 목적

This amendment records only the additional interface obligations actually required by the Step-2 boundary attacks.

It does not redefine Synthesis or merge it with neighboring methods.
The Step-1 draft remains preserved as the historical pre-attack artifact.

Effective pre-protocol interface:

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
```

## 2. Amendment A — composition-law and grouping lock / 합성 법칙·괄호화 잠금

Add to the minimum task record:

```text
COMPOSITION_LAW_PROFILE:
GROUPING_OR_PARENTHESIZATION_POLICY:
```

`COMPOSITION_LAW_PROFILE` records only laws actually supplied by the composition rule or domain authority.
When relevant, record:

```text
COMMUTATIVITY: supplied_true / supplied_false / unspecified / not_applicable
ASSOCIATIVITY: supplied_true / supplied_false / unspecified / not_applicable
IDENTITY_RULE: supplied / not_supplied / not_applicable
IDEMPOTENCE_RULE: supplied / not_supplied / not_applicable
OTHER_COMPOSITION_LAWS:
LAW_SOURCE:
```

`GROUPING_OR_PARENTHESIZATION_POLICY` records how n-ary or iterated compositions are grouped when the rule is not natively n-ary.

No algebraic law is inferred from notation alone.

```text
A ⊙ B notation
!= commutativity
!= associativity
!= identity
!= idempotence
```

## 3. Amendment B — composition equivalence and canonicalization / 합성 동치·정규화

Add:

```text
COMPOSITION_EQUIVALENCE_OR_CANONICALIZATION_RULE:
```

This rule determines when two composition records count as the same materially synthesized target at the declared `TARGET_RESOLUTION`.

It must be locked before:

```text
UNIQUE_SYNTHESIZED_TARGET
material-target counting
duplicate-candidate elimination
composition-space cardinality claims
```

Candidate IDs or syntax trees alone do not establish material distinctness.
Conversely, a syntactic similarity does not establish equivalence when the domain preserves interface, order, grouping, history, or relation distinctions.

## 4. Amendment C — residual obligations for partial synthesis / 부분 합성 잔여 의무

Add to the task/candidate/output records as applicable:

```text
RESIDUAL_OPEN_INTERFACES_OR_OBLIGATIONS:
```

For `PARTIAL_SYNTHESIS`, this field should preserve any claim-relevant:

```text
open interfaces
omitted components
unresolved prerequisites
unresolved property lift/redeclaration
unresolved formation decision
downstream completion obligations
```

A partial synthesis result must not be relabeled as a completed synthesized target merely because its current subcomposition is admissible.

## 5. Amendment D — static composition order versus temporal assembly process / 정적 합성 순서와 시간적 조립과정 분리

Add:

```text
ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE:
```

Initial values:

```text
not_claimed
static_order_only
time_resolved_sequence_supplied
dynamic_process_model_supplied
```

`COMPOSITION_ORDER_SENSITIVITY` concerns the structural/operand order semantics of the composition rule.
It does not by itself establish a temporal assembly sequence.

```text
STATIC_COMPOSITION_ORDER
!= TEMPORAL_ASSEMBLY_SEQUENCE
```

If a claim depends on transient states, process timing, transition feasibility, or formation-level identity change during assembly, the task must activate the appropriate Dynamics or explicit domain process model/bridge.

A static `SYNTHESIS_ADMISSIBLE` result is not automatically a process-feasibility result.

## 6. Updated minimum task interface / 보강 후 최소 입력

The effective pre-protocol task record is the Step-1 record plus the following fields:

```text
COMPOSITION_LAW_PROFILE
GROUPING_OR_PARENTHESIZATION_POLICY
COMPOSITION_EQUIVALENCE_OR_CANONICALIZATION_RULE
RESIDUAL_OPEN_INTERFACES_OR_OBLIGATIONS
ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE
```

The new fields are conditional when the relevant distinction is not claim-relevant, but their non-use should be explicit rather than silently assumed.

## 7. Updated candidate-level record / 후보 레코드 보강

Add as applicable:

```text
GROUPING_OR_PARENTHESIZATION_USED:
COMPOSITION_EQUIVALENCE_CLASS_OR_CANONICAL_ID:
RESIDUAL_OPEN_INTERFACES_OR_OBLIGATIONS:
ASSEMBLY_PROCESS_SCOPE_RESULT:
```

The candidate record still preserves the Step-1 fields for participating components, interface matching, property lift, retention/loss, formation effect, result, failure set, and trace.

## 8. Operation-sequence refinements / 연산 순서 보강

The future Protocol v0.1 should incorporate the following non-breaking changes:

```text
S2  lock composition rule/source/arity/order/multiplicity
    + supplied composition-law profile
    + grouping/parenthesization policy

S3  lock composition candidate basis/coverage
    + equivalence/canonicalization rule

S4  lock active DSD interfaces/domain bridges/property-lift rules
    + assembly sequence/process scope

S7  apply the supplied composition rule
    respecting declared grouping and supplied algebraic laws only

S8  check support/relation/status/information loss
    + residual open interfaces/obligations for partial synthesis

S11 check claimed output level
    using target-resolution material distinctness
    under the frozen equivalence/canonicalization rule
```

## 9. Added nonconformance classes / 추가 비준수 후보

Add:

```text
UNDECLARED_GROUPING_OR_PARENTHESIZATION_ASSUMPTION
UNDECLARED_COMPOSITION_EQUIVALENCE
PARTIAL_SYNTHESIS_RESIDUAL_OMISSION
STATIC_COMPOSABILITY_PROMOTED_TO_PROCESS_FEASIBILITY
```

Retain the existing classes:

```text
UNJUSTIFIED_ASSOCIATIVITY_ASSUMPTION
UNJUSTIFIED_COMMUTATIVITY_ASSUMPTION
```

## 10. Boundary preservation / 경계 유지

These additions do not alter the neighboring-method split.

```text
Design
  goals + constraints -> supplied target/parts/architecture basis

Synthesis
  supplied parts + supplied composition rule -> admissible whole/composition space

Transformation
  source -> target representation/regime

Aggregation
  structure/data -> declared readout

Optimization
  admissible alternatives -> objective-based selection

Dynamics / domain process model
  time-resolved assembly/transition behavior when actually claimed
```

The process-scope field does not turn Synthesis into Dynamics; it only prevents static Synthesis from silently claiming dynamic process validity.

## 11. Step-2 result / 2단계 결과

```text
BOUNDARY_ATTACKS_RUN: 16
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
REFINEMENT_GROUPS_ADDED: 4
DIRECT_SYNTHESIS_PILOT_INCREMENT: 0
```

The method remains at planning/proposed status.
The next technical step is to freeze the first executable `Synthesis Protocol v0.1` from the effective Step-2 interface.
