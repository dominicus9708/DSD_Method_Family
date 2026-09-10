# DSD Synthesis Protocol v0.1 / DSD 합성론 프로토콜 v0.1

Status: **first executable protocol / validation pending**  
Protocol date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Higher field: **III. Construction & Transformation / 구성·변환**

## 1. Protocol purpose / 프로토콜 목적

DSD Synthesis determines which larger constructions are legitimately synthesizable from **supplied components**, a **supplied composition rule**, and declared cross-component conditions.

It is a parts-to-whole method.
It does not invent missing architecture in order to satisfy goals, does not replace source-to-target Transformation, does not identify an aggregate readout with a synthesized whole, and does not choose an optimum among admissible compositions.

Core method form:

```text
supplied parts
+ supplied composition rule
+ declared interface/prerequisite/retention conditions
-> synthesis-admissible whole/composition space
```

The protocol preserves the following distinctions:

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

STATIC_COMPOSITION_ORDER
!= TEMPORAL_ASSEMBLY_SEQUENCE

CANDIDATE_ID_OR_SYNTAX_TREE_DIFFERENCE
!= MATERIAL_SYNTHESIZED_TARGET_DIFFERENCE
```

---

## 2. Protocol lineage / 프로토콜 계보

This protocol is frozen prospectively from the preserved planning artifacts:

```text
TASK_INTERFACE_v0.1-draft.md
+
TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
```

The amendment was triggered by `BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`.
Those planning artifacts remain historical records and are not rewritten by this protocol.

Step-2 planning result:

```text
BOUNDARY_ATTACKS_RUN: 16
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
```

This protocol incorporates the required non-breaking refinements:

```text
COMPOSITION_LAW_PROFILE
GROUPING_OR_PARENTHESIZATION_POLICY
COMPOSITION_EQUIVALENCE_OR_CANONICALIZATION_RULE
RESIDUAL_OPEN_INTERFACES_OR_OBLIGATIONS
ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE
```

Protocol establishment itself is infrastructure and does not count as a direct Synthesis pilot.

---

## 3. DSD source/interface lock / DSD 원천·인터페이스 잠금

Current protocol reference set:

```text
Formation Axiom System — 2026-08-06
Property Axiom System in DSD — 2026-09-01
Channel-Indexed Static Aggregation in DSD — 2026-09-02
Structural Reorganization Dynamics in DSD — 2026-08-12
methodology/DSD_INTERFACE_PROFILE.md — profile date 2026-09-05
methods/METHOD_BOUNDARY_MATRIX.md — 2026-09-06
```

Layer policy:

```text
FORMATION_LAYER:
  structural default / use when component or whole formation identity is claim-relevant

GENERAL_PROPERTY_LAYER:
  conditional / use only when typed property applicability, prerequisites, status, or assignment is claim-relevant

STATIC_AGGREGATION_LAYER:
  conditional / use only for declared analytic readouts

DYNAMICS_LAYER:
  conditional / use only when time-resolved assembly, transition, or formation-level identity change is claimed

OPTIONAL_SPECIALIZATION:
  only when explicitly supplied
```

No unused layer is inferred absent from DSD generally.

Formation Clause VII is not a universal domain assembly rule.
A domain-level synthesis claim requires an actual composition rule/bridge appropriate to the task.

---

## 4. Required task lock / 필수 과업 잠금

Before substantive evaluation, lock the following record.

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
COMPOSITION_LAW_PROFILE:
GROUPING_OR_PARENTHESIZATION_POLICY:

COMPOSITION_CANDIDATE_BASIS:
COMPOSITION_COVERAGE:
COMPOSITION_EQUIVALENCE_OR_CANONICALIZATION_RULE:

INTERFACE_MATCHING_RULES:
CROSS_COMPONENT_PREREQUISITES:
PROPERTY_LIFT_OR_REDECLARATION_RULE:

SUPPORT_RETENTION_REQUIREMENT:
RELATION_RETENTION_REQUIREMENT:
INFORMATION_LOSS_TOLERANCE:
NEW_FORMATION_MODEL_POLICY:
RESIDUAL_OPEN_INTERFACES_OR_OBLIGATIONS:
ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE:

TARGET_DSD_LAYER_SCOPE:
DSD_INTERFACE_PROFILE:
DOMAIN_BRIDGE:
EXTERNAL_STANDARD:
VALIDATION_OR_ACCEPTANCE_RULE:
AUXILIARY_METHODS_OR_HANDOFFS:
NONOPTIMIZATION_SELECTION_RULE_IF_NEEDED:
```

Conditional non-use must be explicit, for example `not_used`, `not_claimed`, or `not_applicable` rather than silently omitted when the field could affect the claim.

---

## 5. Composition-rule lock / 합성 규칙 잠금

`COMPOSITION_RULE` must identify the actual rule used to form a candidate whole.
The protocol does not infer a rule from coexistence, naming similarity, notation, or the mere availability of Formation Clause VII.

Record:

```text
COMPOSITION_RULE_SOURCE:
COMPOSITION_ARITY:
COMPOSITION_ORDER_SENSITIVITY:
MULTIPLICITY_POLICY:
```

### 5.1 Composition-law profile

Only algebraic laws actually supplied by the rule or domain authority may be activated.

```text
COMPOSITION_LAW_PROFILE:
  COMMUTATIVITY: supplied_true / supplied_false / unspecified / not_applicable
  ASSOCIATIVITY: supplied_true / supplied_false / unspecified / not_applicable
  IDENTITY_RULE: supplied / not_supplied / not_applicable
  IDEMPOTENCE_RULE: supplied / not_supplied / not_applicable
  OTHER_COMPOSITION_LAWS:
  LAW_SOURCE:
```

Notation does not establish algebraic law.

```text
A ⊙ B
!= proof of commutativity
!= proof of associativity
!= proof of identity
!= proof of idempotence
```

### 5.2 Grouping / parenthesization

For iterated binary or otherwise grouping-sensitive composition, lock:

```text
GROUPING_OR_PARENTHESIZATION_POLICY:
```

Do not replace:

```text
(A ⊙ B) ⊙ C
```

with:

```text
A ⊙ (B ⊙ C)
```

unless the supplied law and interface conditions justify the equivalence.

---

## 6. Composition candidate basis and coverage / 후보 기반·범위

Lock:

```text
COMPOSITION_CANDIDATE_BASIS:
COMPOSITION_COVERAGE:
  exhaustive
  non_exhaustive
  unknown
```

`COMPOSITION_COVERAGE` describes the covered **composition/arrangement space**, not merely whether the component inventory is complete.

Potentially distinct dimensions include:

```text
order
topology
connector choice
grouping / parenthesization
multiplicity
interface mapping
component role assignment
```

Therefore:

```text
EXHAUSTIVE_COMPONENT_LIST
!= EXHAUSTIVE_COMPOSITION_SPACE
```

`SYNTHESIS_INFEASIBLE` requires either exhaustive composition coverage with all materially relevant candidates rejected or an explicit impossibility argument sufficient for the frozen scope.

A non-exhaustive failure to find a valid composition cannot be upgraded to global infeasibility.

---

## 7. Composition equivalence and material target identity / 합성 동치·실질 표적 동일성

Before uniqueness, duplicate elimination, or composition-space cardinality claims, lock:

```text
COMPOSITION_EQUIVALENCE_OR_CANONICALIZATION_RULE:
```

Material synthesized-target distinctness is judged at the declared `TARGET_RESOLUTION` under this rule.

```text
candidate ID difference
!= material target difference

syntax-tree difference
!= material target difference
```

The converse also holds: syntactic similarity does not establish equivalence if the task preserves order, topology, interface, relation, grouping, history, or other claim-relevant distinctions.

An arbitrary canonicalization rule must not erase a distinction that is inside `TARGET_RESOLUTION`.

---

## 8. Component, interface, and prerequisite discipline / 구성요소·인터페이스·전제 규율

Each participating component must have an identity/status record sufficient for the claim.
Individual component admissibility does not establish composability.

Check, as applicable:

```text
COMPONENT_STATUS_OR_ADMISSION_SOURCE
INTERFACE_MATCHING_RULES
CROSS_COMPONENT_PREREQUISITES
```

If a required component identity, composition rule, bridge, or claim-required interface relation is unavailable before substantive testing, do not fabricate it.
Use `SYNTHESIS_BLOCKED` when the missing input prevents the requested synthesis claim.

If some candidates can be evaluated but unresolved information prevents the requested closure, use `SYNTHESIS_UNDERDETERMINED` as appropriate rather than fabricating completion.

---

## 9. Property lift / redeclaration discipline / 속성 승계·재선언 규율

A component property does not automatically become a whole-object property.

```text
p(A) defined
p(B) defined
!= p(W) automatically defined
```

When a whole-property claim is made, lock:

```text
PROPERTY_LIFT_OR_REDECLARATION_RULE:
```

The rule may be supplied by the domain, a declared bridge, or a newly formed whole-object Property profile.
Without it, component property data remain component property data.

If the synthesized result requires a new Formation model, old component Property records do not silently migrate into the new whole-object Property profile.

---

## 10. Retention and information-loss discipline / 보존·정보손실 규율

Successful construction does not imply lossless retention.
When claim-relevant, evaluate:

```text
SUPPORT_RETENTION_CHECK:
RELATION_RETENTION_CHECK:
STATUS_RETENTION_CHECK:
DECOMPOSITION_RETENTION_CHECK:
INFORMATION_LOSS_CHECK:
LOSS_ALLOWED_BY_TASK:
```

An explicitly allowed lossy synthesis may still be `SYNTHESIS_ADMISSIBLE` if the loss is compatible with the frozen task.

A claim-breaking undeclared loss rejects the affected candidate or leaves the requested claim unresolved.

An aggregate equality/readout is not a substitute for structural retention evidence.
Static Aggregation remains a separate handoff when used.

---

## 11. Formation-effect discipline / 형성 효과 규율

Lock:

```text
NEW_FORMATION_MODEL_POLICY:
  remain_within_inherited_formation_background
  require_new_formation_model
  allow_either_subject_to_explicit_test
```

Candidate-level `FORMATION_EFFECT` uses at least:

```text
same_background
new_formation_required
unresolved
not_applicable
```

If a new structural whole requires a new Formation model, record that obligation rather than pretending the inherited component formation identities are one unchanged whole-object identity.

This protocol does not itself establish the new Formation model; it records whether such a model is required for the claim and routes the necessary handoff.

---

## 12. Static composition versus assembly process / 정적 합성과 조립 과정

Lock:

```text
ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE:
  not_claimed
  static_order_only
  time_resolved_sequence_supplied
  dynamic_process_model_supplied
```

`COMPOSITION_ORDER_SENSITIVITY` concerns structural/operand semantics.
It does not by itself establish a temporal assembly order.

```text
STATIC_COMPOSITION_ORDER
!= TEMPORAL_ASSEMBLY_SEQUENCE
```

A static `SYNTHESIS_ADMISSIBLE` result is not automatically a process-feasibility result.

If transient states, timing, transition feasibility, or formation-level identity change during assembly are claim-relevant, activate an explicit domain process model and/or DSD Dynamics.
When formation-level identity changes across a dynamic process, record the required lineage/transition relation instead of writing it as ordinary value evolution of one unchanged Stage-VI channel identity.

---

## 13. Partial synthesis discipline / 부분 합성 규율

For `PARTIAL_SYNTHESIS`, preserve:

```text
RESIDUAL_OPEN_INTERFACES_OR_OBLIGATIONS:
```

This field may contain:

```text
open interfaces
omitted components
unresolved prerequisites
unresolved property lift/redeclaration
unresolved formation decision
downstream completion obligations
```

A valid subcomposition is not automatically a completed synthesized target.

---

## 14. Allowed claimed output levels / 허용 주장 산출 수준

```text
SYNTHESIS_SPACE
SYNTHESIZED_TARGET
UNIQUE_SYNTHESIZED_TARGET
PARTIAL_SYNTHESIS
```

### `SYNTHESIS_SPACE`

Return the complete synthesis-admissible family **within the frozen `COMPOSITION_COVERAGE`**.
The result must state the coverage class and must not imply unexamined compositions were evaluated.

### `SYNTHESIZED_TARGET`

Establish one declared synthesized target, or select one admissible target using a prelocked `NONOPTIMIZATION_SELECTION_RULE_IF_NEEDED`.
No optimality claim is implied.

### `UNIQUE_SYNTHESIZED_TARGET`

Establish exactly one materially distinct synthesized target at `TARGET_RESOLUTION`, under the frozen equivalence/canonicalization rule, with exhaustive coverage or an explicit uniqueness argument sufficient for the scope.

An arbitrary tie-breaker does not establish uniqueness.

### `PARTIAL_SYNTHESIS`

Validate only the declared subcomposition and preserve all residual open interfaces/obligations.
Do not relabel a partial result as a completed target.

---

## 15. Candidate-level execution record / 후보 실행 레코드

For every evaluated composition candidate, record as applicable:

```text
COMPOSITION_ID:
PARTICIPATING_COMPONENTS:
ORDER_OR_TOPOLOGY:
COMPOSITION_RULE_APPLIED:
GROUPING_OR_PARENTHESIZATION_USED:
INTERFACE_MATCH_RESULTS:
PREREQUISITE_RESULTS:
STATUS_DISTINCTIONS_PRESERVED:
PROPERTY_LIFT_RESULT:
SUPPORT_RETENTION_RESULT:
RELATION_RETENTION_RESULT:
INFORMATION_LOSS_RESULT:
FORMATION_EFFECT:
COMPOSITION_EQUIVALENCE_CLASS_OR_CANONICAL_ID:
RESIDUAL_OPEN_INTERFACES_OR_OBLIGATIONS:
ASSEMBLY_PROCESS_SCOPE_RESULT:
LINEAGE_OR_TRANSITION_CHECK:
SYNTHESIS_CANDIDATE_RESULT:
FAILURE_SET:
OUTPUT_ID_OR_TRACE:
```

Candidate result values:

```text
admissible
rejected
unresolved
blocked
```

Failure sets should preserve all claim-relevant failed constraints when the task requires full failure traceability rather than stopping at the first failure.

---

## 16. Executable operation sequence / 실행 연산 순서

Use the following sequence for new Protocol-v0.1 runs.

```text
S1  LOCK TASK, CLAIMED OUTPUT LEVEL, TARGET RESOLUTION, AND COMPONENT IDENTITIES

S2  LOCK COMPOSITION RULE, SOURCE, ARITY, ORDER, MULTIPLICITY,
    SUPPLIED COMPOSITION-LAW PROFILE, AND GROUPING/PARENTHESIZATION POLICY

S3  LOCK COMPOSITION CANDIDATE BASIS, COVERAGE,
    AND COMPOSITION EQUIVALENCE/CANONICALIZATION RULE

S4  LOCK ACTIVE DSD INTERFACES, DOMAIN BRIDGES, EXTERNAL STANDARDS,
    PROPERTY-LIFT/REDECLARATION RULES, FORMATION POLICY,
    AND ASSEMBLY SEQUENCE/PROCESS SCOPE

S5  CHECK REQUIRED COMPONENT IDENTITY, STATUS, AND ADMISSION RECORDS

S6  CHECK INTERFACE MATCHING AND CROSS-COMPONENT PREREQUISITES

S7  APPLY ONLY THE SUPPLIED COMPOSITION RULE TO COVERED CANDIDATES,
    RESPECTING DECLARED GROUPING AND ONLY SUPPLIED ALGEBRAIC LAWS

S8  CHECK PROPERTY LIFT/REDECLARATION WHEN CLAIMED

S9  CHECK SUPPORT, RELATION, STATUS, DECOMPOSITION, AND INFORMATION-LOSS REQUIREMENTS;
    RECORD RESIDUAL OPEN INTERFACES/OBLIGATIONS FOR PARTIAL SYNTHESIS

S10 CHECK INHERITED-FORMATION VERSUS NEW-FORMATION EFFECT;
    RECORD LINEAGE/TRANSITION OBLIGATIONS WHEN DYNAMIC FORMATION CHANGE IS CLAIMED

S11 BUILD THE SYNTHESIS-ADMISSIBLE FAMILY WITHIN THE FROZEN COVERAGE

S12 APPLY TARGET-RESOLUTION MATERIAL DISTINCTNESS UNDER THE FROZEN
    EQUIVALENCE/CANONICALIZATION RULE

S13 CHECK THE CLAIMED OUTPUT LEVEL

S14 ASSIGN TERMINAL SYNTHESIS STATUS

S15 RECORD SYNTHESIS PROTOCOL CONFORMANCE SEPARATELY

S16 RECORD METHOD-GAIN STATUS SEPARATELY

S17 RECORD LIMITS, AUXILIARY HANDOFFS, SOURCE LOCKS, AND REPRODUCIBILITY DATA
```

Do not reorder the sequence in a way that permits post-hoc changes to task scope, composition law, candidate coverage, target resolution, or equivalence rules after inspecting outcomes.

---

## 17. Terminal Synthesis status / 종결 합성 상태

```text
TERMINAL_SYNTHESIS_STATUS:
  SYNTHESIS_ADMISSIBLE
  SYNTHESIS_INFEASIBLE
  SYNTHESIS_UNDERDETERMINED
  SYNTHESIS_BLOCKED
```

### `SYNTHESIS_ADMISSIBLE`

The requested synthesis claim is supported within its declared output level, target resolution, candidate coverage, composition rule, and active validation scope.

### `SYNTHESIS_INFEASIBLE`

No admissible synthesis exists under exhaustive composition coverage, or an explicit impossibility argument closes the frozen scope.

### `SYNTHESIS_UNDERDETERMINED`

Available composition coverage, status information, equivalence basis, relation information, formation decision, or uniqueness basis is insufficient for the requested claim.

### `SYNTHESIS_BLOCKED`

A claim-required input is unavailable before substantive completion, including for example:

```text
required component identity unavailable
composition rule unavailable
required interface relation unavailable
required domain bridge unavailable
required source standard unavailable
```

A blocked result may still be protocol-conformant if the protocol correctly exposes the missing input rather than fabricating it.

---

## 18. Protocol-conformance ledger / 프로토콜 준수 장부

```text
SYNTHESIS_PROTOCOL_CONFORMANCE:
  CONFORMANT
  NONCONFORMANT
  UNDETERMINED
```

Representative nonconformance classes:

```text
UNSUPPLIED_COMPOSITION_RULE
COMPOSITION_RULE_DOMAIN_MISMATCH
IMPLICIT_COMPOSABILITY_FROM_COEXISTENCE
UNDECLARED_ARITY_OR_ORDER_ASSUMPTION
UNDECLARED_MULTIPLICITY_ASSUMPTION
UNDECLARED_GROUPING_OR_PARENTHESIZATION_ASSUMPTION
UNJUSTIFIED_ASSOCIATIVITY_ASSUMPTION
UNJUSTIFIED_COMMUTATIVITY_ASSUMPTION
UNDECLARED_COMPOSITION_EQUIVALENCE
CROSS_COMPONENT_PREREQUISITE_OMISSION
CLAIM_RELEVANT_STATUS_COLLAPSE
UNDECLARED_PROPERTY_LIFT
UNDECLARED_SUPPORT_LOSS
UNDECLARED_RELATION_LOSS
PARTIAL_SYNTHESIS_RESIDUAL_OMISSION
STATIC_COMPOSABILITY_PROMOTED_TO_PROCESS_FEASIBILITY
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
TARGET_RESOLUTION_POST_HOC_CHANGE
COMPOSITION_LAW_POST_HOC_CHANGE
CANDIDATE_COVERAGE_POST_HOC_CHANGE
EQUIVALENCE_RULE_POST_HOC_CHANGE
```

Protocol conformance is not the same as synthesis success.
For example, a correctly exposed missing composition rule may yield:

```text
SYNTHESIS_BLOCKED + CONFORMANT
```

---

## 19. Method-gain ledger / 방법 이득 장부

```text
SYNTHESIS_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

Rules:

```text
GAIN_ESTABLISHED
  requires a frozen baseline comparison and a precommitted gain criterion.

NO_GAIN
  is valid when a competent frozen baseline matches DSD Synthesis
  on all measured claim-relevant dimensions.

NOT_ASSESSED
  is required when no adequate baseline comparison is active.
```

Extra DSD terminology, fields, or bookkeeping do not count as method gain by themselves.

---

## 20. Method-boundary handoff rules / 방법 경계·인계 규칙

### Design -> Synthesis

```text
Design:
  goals + constraints -> target/parts/architecture basis

Synthesis:
  supplied parts + supplied composition rule -> admissible whole/composition space
```

If missing parts, connectors, or architecture must be invented to satisfy a goal, record a Design handoff.
Do not absorb that operation into Synthesis.

### Transformation -> Synthesis

If components require representation/regime conversion before composition:

```text
Transformation(A) -> A'
Transformation(B) -> B'
Synthesis(A', B') -> W
```

The Transformation verdict and validation standard remain separate.

### Synthesis -> Aggregation

A synthesized whole may later receive an aggregate readout.
The aggregate does not replace the whole's structural identity.

### Synthesis -> Optimization

Synthesis may return several admissible compositions.
Objective-based ranking/selection remains Optimization.

### Synthesis -> Dynamics / process model

Time-resolved assembly feasibility remains a Dynamics or domain-process handoff when actually claimed.

### Audit

Audit may retrace the execution or maturity of Synthesis.
Audit verdicts do not become Synthesis verdicts and do not increase Synthesis direct-pilot counts merely by existing.

---

## 21. Minimum valid output / 최소 유효 산출물

Every substantive Protocol-v0.1 execution must record, at minimum:

```text
SYNTHESIS_TASK_ID
METHOD_VERSION_OR_PROTOCOL
TASK_SCOPE
CLAIMED_OUTPUT_LEVEL
TARGET_RESOLUTION
COMPONENT_SET_OR_FAMILY
COMPONENT_IDENTITY_RECORDS
COMPONENT_STATUS_OR_ADMISSION_SOURCE
COMPOSITION_RULE + SOURCE
COMPOSITION_ARITY / ORDER / MULTIPLICITY
COMPOSITION_LAW_PROFILE
GROUPING_OR_PARENTHESIZATION_POLICY
COMPOSITION_CANDIDATE_BASIS + COVERAGE
COMPOSITION_EQUIVALENCE_OR_CANONICALIZATION_RULE
INTERFACE_MATCHING / CROSS_COMPONENT_PREREQUISITES
PROPERTY_LIFT_OR_REDECLARATION_RULE
ACTIVE_DSD_LAYERS
DOMAIN_BRIDGE / EXTERNAL_STANDARD
CANDIDATE-LEVEL SYNTHESIS RESULTS + FAILURE SETS
SYNTHESIS_ADMISSIBLE_FAMILY OR NON-SUCCESS BASIS
SUPPORT / RELATION / STATUS / INFORMATION-LOSS RESULT
FORMATION_EFFECT
RESIDUAL_OPEN_INTERFACES_OR_OBLIGATIONS
ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE
LINEAGE_OR_TRANSITION_CHECK WHEN APPLICABLE
TERMINAL_SYNTHESIS_STATUS
SYNTHESIS_PROTOCOL_CONFORMANCE
SYNTHESIS_METHOD_GAIN_STATUS
AUXILIARY_METHODS_OR_HANDOFFS
LIMITS
REPRODUCIBILITY_RECORD
```

---

## 22. Historical-record and precommit discipline / 역사 기록·사전동결 규율

New direct Synthesis evidence should be frozen prospectively.

Case convention:

```text
SYN-CH-###   constructed Synthesis challenges
SYN-APP-###  external or independently generated Synthesis applications
SYN-AUD-###  Synthesis-specific Audit/maturity records
SYN-IEP-###  independent-evaluator packet infrastructure
```

For a challenge whose expected result or scoring rule matters, create a separate precommit before evaluation.

A failed challenge is preserved as failed.
Corrections use a new case ID or prospective amendment rather than rewriting history.

Planning attacks `SYN-BND-DRAFT-*` remain pre-protocol planning evidence and are not retroactively counted as Protocol-v0.1 direct pilots.

---

## 23. Reproducibility record / 재현성 레코드

Each direct run should preserve enough information to retrace the claim-relevant result:

```text
PROTOCOL_VERSION_OR_COMMIT
CASE_PRECOMMIT_COMMIT_WHEN_USED
SOURCE_VERSION_OR_COMMIT
COMPONENT_INPUT_RECORD
COMPOSITION_RULE_RECORD
CANDIDATE_BASIS_AND_COVERAGE
TARGET_RESOLUTION
EQUIVALENCE_OR_CANONICALIZATION_RULE
DOMAIN_BRIDGE / EXTERNAL_STANDARD
EXPECTED_OR_ACTUAL CHECK LIST
OUTPUT_TRACE
KNOWN_LIMITATIONS
```

Same-project retrace does not substitute for independent replication.
Independent evaluation requires an actually separate evaluator or separately controlled execution with contamination/answer-exposure rules appropriate to the task.

---

## 24. Protocol establishment state / 프로토콜 동결 상태

At creation of this file:

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS: 0
POSITIVE_SYNTHESIS_CASES: 0
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 0
BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 0
NO_GAIN_SYNTHESIS_CASES: 0
BASELINE_COMPARISON_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_pending
```

Protocol establishment is not evidence that the protocol is correct, superior, externally applicable, or mature.

## 25. Immediate next evidence task / 다음 직접 증거 과업

Create a separate precommit for the first positive Protocol-v0.1 challenge:

```text
SYN-CH-001
CASE_CLASS: positive
```

The first challenge should contain at least:

- more than one individually admissible component;
- at least one composition candidate that is actually admissible;
- at least one rejected composition due to an explicit interface/prerequisite condition;
- a supplied noncommutative or otherwise order-sensitive composition rule if practical;
- a frozen target resolution and equivalence rule;
- no hidden Design, Transformation, Aggregation, or Optimization;
- separate terminal/conformance/gain ledgers;
- a precommitted check count.

Do not count the case until its precommit is frozen and the challenge is actually executed under this protocol.
