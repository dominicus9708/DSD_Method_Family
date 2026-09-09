# DSD Synthesis Task Interface v0.1 Draft / DSD 합성론 과업 인터페이스 v0.1 초안

Status: **planning draft — not yet executable protocol**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Higher field: **III. Construction & Transformation / 구성·변환**

## 1. Method purpose / 방법 목적

DSD Synthesis composes supplied admitted components, component structures, or typed component data into a larger declared construction under an **explicit composition rule**.

The method answers:

```text
Given these parts,
this composition rule,
and these cross-part conditions,
which larger constructions are legitimately synthesizable,
and what structure/relations/statuses are retained or lost?
```

It does not infer composability merely because parts coexist, have similar names, or are individually admissible.

```text
INDIVIDUAL_COMPONENT_ADMISSIBILITY
!= AUTOMATIC_COMPOSABILITY
```

---

## 2. DSD source discipline / DSD 원천 규율

The current source interface is the project `DSD_INTERFACE_PROFILE.md` and its reference set:

- Formation Axiom System;
- General Property Axiom System;
- Channel-Indexed Static Aggregation;
- Structural Reorganization Dynamics.

Synthesis may use the following interfaces conditionally.

### 2.1 Formation

Formation is the structural default.
A synthesis may consume already admitted component/channel structures and may produce a composition that remains within an inherited formation background or requires a new formation model.

Formation Clause VII finite composition is a valid **formal composition interface** only after its post-Stage-VI term data are supplied.
It is not, by itself, a proof that arbitrary domain parts may be assembled into one substantive whole.

```text
FORMATION_CLAUSE_VII_COMPOSITION
!= DOMAIN_SYNTHESIS_LEGITIMACY
```

### 2.2 General Property

General Property is activated only when typed property applicability, prerequisites, assignments, or cross-part conditions are claim-relevant.

A property attached to one component is not automatically a property of the synthesized whole.
If component property data are lifted, transferred, combined, or redeclared on the whole, the task must supply an explicit rule or domain bridge.

```text
COMPONENT_PROPERTY
!= WHOLE_PROPERTY
```

### 2.3 Static Aggregation

Static Aggregation may be used when component analytic outputs are combined into a readout.
An aggregate readout is not automatically the synthesized structural whole.

```text
AGGREGATE_READOUT
!= SYNTHESIZED_WHOLE
```

Equal aggregates do not establish equal decomposition, support, topology, interface structure, or synthesis history.

### 2.4 Dynamics

Dynamics is optional.
Use it only when assembly order, temporal sequence, transition, or formation-level identity change is part of the claim.
A static Synthesis record must not silently imply a time-resolved assembly process.

---

## 3. Minimum task record / 최소 과업 레코드

A new Synthesis task should lock the following fields before substantive evaluation.

```text
SYNTHESIS_TASK_ID:
TASK_SCOPE:
CLAIMED_OUTPUT_LEVEL:
TARGET_RESOLUTION:

COMPONENT_SET_OR_FAMILY:
COMPONENT_IDENTITY_RECORDS:
COMPONENT_STATUS_OR_ADMISSION_SOURCE:

COMPOSITION_RULE:
COMPOSITION_RULE_SOURCE:
COMPOSITION_ARITY:
COMPOSITION_ORDER_SENSITIVITY:
MULTIPLICITY_POLICY:

COMPOSITION_CANDIDATE_BASIS:
COMPOSITION_COVERAGE:

INTERFACE_MATCHING_RULES:
CROSS_COMPONENT_PREREQUISITES:
PROPERTY_LIFT_OR_REDECLARATION_RULE:

SUPPORT_RETENTION_REQUIREMENT:
RELATION_RETENTION_REQUIREMENT:
INFORMATION_LOSS_TOLERANCE:
NEW_FORMATION_MODEL_POLICY:

TARGET_DSD_LAYER_SCOPE:
DSD_INTERFACE_PROFILE:
DOMAIN_BRIDGE:
EXTERNAL_STANDARD:
VALIDATION_OR_ACCEPTANCE_RULE:
AUXILIARY_METHODS_OR_HANDOFFS:
```

`PROPERTY_LIFT_OR_REDECLARATION_RULE` may be `not used` when no component-to-whole property transfer is claimed.

`NEW_FORMATION_MODEL_POLICY` must state whether the composition is expected to:

```text
remain_within_inherited_formation_background
require_new_formation_model
allow_either_subject_to_explicit_test
```

---

## 4. Claimed output levels / 주장 산출 수준

Allowed initial output levels are:

```text
SYNTHESIS_SPACE
SYNTHESIZED_TARGET
UNIQUE_SYNTHESIZED_TARGET
PARTIAL_SYNTHESIS
```

### `SYNTHESIS_SPACE`

Return the complete set of synthesis-admissible composition candidates within the declared `COMPOSITION_COVERAGE`.

### `SYNTHESIZED_TARGET`

Establish one declared synthesized target or one admissible target selected by a prelocked non-optimization rule.
No optimality claim is implied.

### `UNIQUE_SYNTHESIZED_TARGET`

Establish that exactly one materially distinct synthesized target exists at the declared `TARGET_RESOLUTION` within exhaustive coverage or under an explicit uniqueness argument.

An arbitrary tie-breaker does not prove uniqueness.

### `PARTIAL_SYNTHESIS`

Construct and validate only a declared subcomposition while preserving unresolved interfaces, omitted parts, and downstream obligations explicitly.

---

## 5. Composition coverage / 합성 후보 범위

Use:

```text
COMPOSITION_COVERAGE:
  exhaustive
  non_exhaustive
  unknown
```

This field refers to the covered **composition/arrangement space**, not merely the list of parts.

A complete component list does not imply exhaustive composition coverage when order, topology, multiplicity, connector choice, grouping, or interface mapping can vary.

```text
EXHAUSTIVE_COMPONENT_LIST
!= EXHAUSTIVE_COMPOSITION_SPACE
```

`SYNTHESIS_INFEASIBLE` requires either:

1. exhaustive composition coverage with all candidates rejected; or
2. an explicit impossibility argument sufficient for the declared scope.

A non-exhaustive failure to find a valid composition must not be promoted to global infeasibility.

---

## 6. Candidate-level record / 후보 단위 레코드

Each evaluated composition candidate should preserve:

```text
COMPOSITION_ID:
PARTICIPATING_COMPONENTS:
ORDER_OR_TOPOLOGY:
COMPOSITION_RULE_APPLIED:
INTERFACE_MATCH_RESULTS:
PREREQUISITE_RESULTS:
STATUS_DISTINCTIONS_PRESERVED:
PROPERTY_LIFT_RESULT:
SUPPORT_RETENTION_RESULT:
RELATION_RETENTION_RESULT:
INFORMATION_LOSS_RESULT:
FORMATION_EFFECT:
SYNTHESIS_CANDIDATE_RESULT:
FAILURE_SET:
OUTPUT_ID_OR_TRACE:
```

Allowed candidate results:

```text
admissible
rejected
unresolved
blocked
```

`FORMATION_EFFECT` should use, at minimum:

```text
same_background
new_formation_required
unresolved
not_applicable
```

---

## 7. Draft Synthesis operation / 합성 연산 초안

The first protocol draft should refine the following operation sequence.

```text
S1  LOCK TASK, CLAIM, TARGET RESOLUTION, AND COMPONENT IDENTITIES
S2  LOCK COMPOSITION RULE, SOURCE, ARITY, ORDER, AND MULTIPLICITY
S3  LOCK COMPOSITION CANDIDATE BASIS AND COVERAGE
S4  LOCK ACTIVE DSD INTERFACES, DOMAIN BRIDGES, AND PROPERTY-LIFT RULES
S5  CHECK REQUIRED COMPONENT STATUS / ADMISSION RECORDS
S6  CHECK INTERFACE MATCHING AND CROSS-COMPONENT PREREQUISITES
S7  APPLY THE SUPPLIED COMPOSITION RULE TO COVERED CANDIDATES
S8  CHECK SUPPORT, RELATION, STATUS, AND INFORMATION-LOSS REQUIREMENTS
S9  CHECK WHETHER THE RESULT REMAINS IN THE INHERITED FORMATION OR REQUIRES A NEW FORMATION MODEL
S10 BUILD THE SYNTHESIS-ADMISSIBLE FAMILY
S11 CHECK THE CLAIMED OUTPUT LEVEL
S12 ASSIGN TERMINAL SYNTHESIS STATUS
S13 RECORD SYNTHESIS PROTOCOL CONFORMANCE SEPARATELY
S14 RECORD METHOD-GAIN STATUS SEPARATELY
S15 RECORD LIMITS, HANDOFFS, AND REPRODUCIBILITY DATA
```

This sequence is still a planning artifact and may receive non-breaking refinements after boundary attacks.

---

## 8. Terminal Synthesis status / 종결 합성 상태

Initial terminal statuses:

```text
SYNTHESIS_ADMISSIBLE
SYNTHESIS_INFEASIBLE
SYNTHESIS_UNDERDETERMINED
SYNTHESIS_BLOCKED
```

### `SYNTHESIS_ADMISSIBLE`

The declared output-level claim is supported for at least one synthesis result or the requested synthesis space within the frozen scope.

### `SYNTHESIS_INFEASIBLE`

No admissible synthesis exists within exhaustive coverage or under an explicit impossibility argument.

### `SYNTHESIS_UNDERDETERMINED`

The available composition coverage, status information, relation information, or uniqueness basis is insufficient for the requested claim.

### `SYNTHESIS_BLOCKED`

A claim-required input is unavailable before the substantive composition test can be completed, for example:

```text
required component identity missing
composition rule missing
required bridge missing
required interface relation unavailable
```

A blocked result may still be protocol-conformant if the method correctly exposes the missing requirement instead of fabricating it.

---

## 9. Independent protocol-conformance ledger / 프로토콜 준수 장부

Initial values:

```text
SYNTHESIS_PROTOCOL_CONFORMANCE:
  CONFORMANT
  NONCONFORMANT
  UNDETERMINED
```

Representative nonconformance classes to pressure-test:

```text
UNSUPPLIED_COMPOSITION_RULE
COMPOSITION_RULE_DOMAIN_MISMATCH
IMPLICIT_COMPOSABILITY_FROM_COEXISTENCE
UNDECLARED_ARITY_OR_ORDER_ASSUMPTION
UNDECLARED_MULTIPLICITY_ASSUMPTION
CROSS_COMPONENT_PREREQUISITE_OMISSION
CLAIM_RELEVANT_STATUS_COLLAPSE
UNDECLARED_PROPERTY_LIFT
UNDECLARED_SUPPORT_LOSS
UNDECLARED_RELATION_LOSS
UNJUSTIFIED_ASSOCIATIVITY_ASSUMPTION
UNJUSTIFIED_COMMUTATIVITY_ASSUMPTION
UNSUPPORTED_EXHAUSTIVENESS_CLAIM
INFEASIBLE_FROM_NONEXHAUSTIVE_FAILURE_TO_FIND
NEW_FORMATION_MODEL_OMISSION
HIDDEN_DESIGN
HIDDEN_TRANSFORMATION
HIDDEN_AGGREGATION_SUBSTITUTION
HIDDEN_OPTIMIZATION
NEIGHBORING_METHOD_VERDICT_ABSORPTION
UNRECORDED_TASK_REVISION
UNSUPPORTED_UNIQUENESS_CLAIM
```

---

## 10. Method-gain ledger / 방법 이득 장부

Initial values:

```text
SYNTHESIS_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

As with the other developed DSD methods:

- `GAIN_ESTABLISHED` requires an actual declared baseline comparison and a frozen gain criterion;
- `NO_GAIN` is a legitimate outcome when a competent baseline matches DSD Synthesis on the measured claim-relevant dimensions;
- without a baseline comparison, use `NOT_ASSESSED`.

Extra DSD bookkeeping is not method gain by itself.

---

## 11. Information-loss and relation discipline / 정보손실·관계 보존 규율

Synthesis may create a larger whole while losing some source-side distinctions.
The method must not silently equate successful output construction with lossless retention.

Minimum checks when claim-relevant:

```text
SUPPORT_RETENTION_CHECK:
RELATION_RETENTION_CHECK:
STATUS_RETENTION_CHECK:
DECOMPOSITION_RETENTION_CHECK:
INFORMATION_LOSS_CHECK:
LOSS_ALLOWED_BY_TASK:
```

An allowed lossy synthesis may still be `SYNTHESIS_ADMISSIBLE` when the loss is declared and compatible with the task.
A claim-breaking undeclared loss should reject the candidate or make the claim unresolved.

---

## 12. Formation-model boundary / 형성모델 경계

A synthesized whole may not fit the inherited component formation identities unchanged.

The task must explicitly determine whether:

```text
component identities remain as admitted substructure within one inherited background
or
composition creates a new structural object requiring a new Formation model/record
```

When a new formation model is required, old component Property records do not automatically become whole-object Property records.
Any property propagation or redeclaration must be explicit.

---

## 13. Method boundaries / 방법 경계

### Synthesis vs Design

```text
Design:
  goals + constraints -> target/design space

Synthesis:
  supplied parts + supplied composition rule -> admissible whole/composition space
```

If the task invents required parts, connectors, interfaces, or target architecture in order to meet a goal, that operation belongs to Design or a Design handoff.
Synthesis may consume the resulting parts and rules afterward.

### Synthesis vs Transformation

Synthesis is parts-to-whole composition.
Transformation is a source-to-target mapping between representations, schemas, models, or regimes.

Transforming a component before composition does not make Transformation part of Synthesis; record the handoff separately.

### Synthesis vs Aggregation

Aggregation constructs a declared readout.
Synthesis constructs a larger composition under a composition rule.

A finite sum or analytic output is not a substantive synthesized whole unless the task/domain explicitly supplies that interpretation.

### Synthesis vs Optimization

Synthesis forms the set of legitimate compositions.
Optimization chooses among already legitimate alternatives under an objective.

### Synthesis vs Audit

Audit may retrace whether a synthesis followed the frozen rule, but Audit verdicts do not become Synthesis verdicts.

---

## 14. Minimum valid output / 최소 유효 산출물

Every substantive Synthesis execution should produce, at minimum:

```text
SYNTHESIS_TASK_ID
METHOD_VERSION_OR_PROTOCOL
TASK_SCOPE
CLAIMED_OUTPUT_LEVEL
TARGET_RESOLUTION
COMPONENT_SET_OR_FAMILY
COMPOSITION_RULE + SOURCE
COMPOSITION_CANDIDATE_BASIS + COVERAGE
ACTIVE_DSD_LAYERS
DOMAIN_BRIDGE / EXTERNAL_STANDARD
CANDIDATE-LEVEL SYNTHESIS RESULTS
SYNTHESIS_ADMISSIBLE_FAMILY OR NON-SUCCESS BASIS
SUPPORT / RELATION / INFORMATION-LOSS RESULT
FORMATION_EFFECT
TERMINAL_SYNTHESIS_STATUS
SYNTHESIS_PROTOCOL_CONFORMANCE
SYNTHESIS_METHOD_GAIN_STATUS
AUXILIARY_METHODS_OR_HANDOFFS
LIMITS
REPRODUCIBILITY_RECORD
```

---

## 15. Initial development plan / 초기 개발 계획

This draft is planning Step 1.
It is not yet direct Synthesis evidence.

Next development stages:

1. pressure-test the interface with boundary counterexamples against Design, Transformation, Aggregation, Optimization, and whole-property lifting;
2. apply only non-breaking refinements that the counterexamples actually require;
3. freeze the first executable `Synthesis Protocol v0.1`;
4. run separately precommitted positive, negative/failure, boundary, `NO_GAIN`, competent-baseline, external, and reproducibility cases;
5. perform DSD Audit maturity review only after the method-specific evidence architecture is materially populated.

Current evidence state:

```text
DEDICATED_SYNTHESIS_PROTOCOL: not established
DIRECT_SYNTHESIS_PILOTS: 0
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_pending
```
