# DSD Classification Protocol v0.1 / DSD 분류론 실행 프로토콜 v0.1

Status: **EXECUTABLE PROTOCOL — frozen**  
Date: **2026-09-12**  
Method: **DSD Classification / DSD 분류론**

## 1. Protocol lineage / 프로토콜 계보

This protocol prospectively integrates the preserved planning artifacts:

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

The historical draft and Amendment 001 remain preserved. This protocol does not retroactively rewrite either artifact.

Planning pressure tests incorporated into this protocol:

```text
BOUNDARY_ATTACKS_RUN: 18
PRESERVED_NO_REFINEMENT: 12
PRESERVED_WITH_NONBREAKING_REFINEMENT: 6
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
NONBREAKING_REFINEMENT_GROUPS: 6
```

Protocol establishment is infrastructure. It does **not** increment direct Classification evidence.

---

## 2. Core method form / 핵심 방법 형태

```text
supplied subject(s)
+ declared classification universe and target resolution
+ frozen class schema or class-generation policy
+ explicit class criteria and membership-decision logic
+ feature basis with provenance
-> criterion-traceable class assignment, boundary/nonassignment status, and class-relation record
```

Classification does not infer membership from names, create hidden criteria, silently normalize missing states, substitute comparison similarity for class membership, turn diagnostic hypotheses into labels, or treat a schema declaration as proof of exhaustive coverage.

---

## 3. Core guards / 핵심 가드

```text
CLASS_LABEL != CLASS_CRITERION
SUMMARY_COINCIDENCE != STRUCTURAL_CLASS_IDENTITY
PAIRWISE_SIMILARITY != EQUIVALENCE_CLASS_MEMBERSHIP
ORDERED_LABELS != PROVEN_PARTIAL_ORDER
CURRENT_CLASS_MATCH != TEMPORAL_LINEAGE_IDENTITY
MISSING_FEATURE != NEGATIVE_FEATURE
UNDEFINED != DEFINED_ZERO
OUT_OF_SCOPE != UNCLASSIFIED
BOUNDARY_CASE != CLASSIFICATION_FAILURE
MULTI_CLASS_MEMBERSHIP != CRITERION_CONFLICT
SCHEMA_STATUS_CLOSED != CLOSED_WORLD_COVERAGE_ESTABLISHED
CRITERION_LIST != MEMBERSHIP_LOGIC
PRE_GENERATION_SCHEMA != POST_GENERATION_SCHEMA
COMMON_CLASS != COMMON_CAUSE
CURRENT_CLASS_EQUALITY != OBJECT_IDENTITY
NO_CURRENT_MATCH_IN_OPEN_SCHEMA != UNIVERSAL_NONMEMBERSHIP
CASE_PASS != METHOD_SURVIVAL_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
```

---

## 4. Required task record / 필수 과업 레코드

Every Protocol-v0.1 run must freeze each claim-relevant field before substantive membership evaluation.

```text
CLASSIFICATION_TASK_ID
TASK_SCOPE
CLAIMED_OUTPUT_LEVEL
TARGET_RESOLUTION

SUBJECT_SET
SUBJECT_ID_POLICY
CLASSIFICATION_UNIVERSE

CLASS_SCHEMA_ID_AND_VERSION
CLASS_SCHEMA_OR_GENERATION_POLICY
CLASS_SCHEMA_STATUS
CLASS_LABELS_IF_PREDECLARED
CLASS_RELATION_SEMANTICS
MUTUAL_EXCLUSION_RULES
SCHEMA_COVERAGE_CLAIM
CLOSED_SCHEMA_CLOSURE_EVIDENCE

CLASS_CRITERIA
CRITERION_SOURCE
CRITERION_PRECEDENCE_OR_DEPENDENCY
CRITERION_COMPOSITION_RULE
DECISION_RULE

FEATURE_BASIS
FEATURE_SOURCE_AND_PROVENANCE
FEATURE_EXTRACTION_OR_MAPPING_RULE
FEATURE_UNCERTAINTY_OR_TOLERANCE_POLICY
BOUNDARY_DECISION_SEMANTICS

TARGET_DSD_LAYER_SCOPE
DSD_INTERFACE_PROFILE
DOMAIN_BRIDGE_IF_ANY
EXTERNAL_STANDARD_IF_ANY

MISSING_INFORMATION_POLICY
OUT_OF_SCOPE_POLICY
BOUNDARY_CASE_POLICY
MULTI_LABEL_POLICY
CRITERION_CONFLICT_POLICY

BASELINE_IF_GAIN_CLAIM
PRECOMMIT_OR_FREEZE_REFERENCE
AUXILIARY_METHODS_OR_HANDOFFS
```

A claim-relevant field may be `not_applicable` only when non-use is explicit and consistent with the requested output.

No run may manufacture a missing criterion, bridge, feature value, class relation, closure argument, uncertainty rule, or decision rule merely to obtain a terminal label.

---

## 5. Classification-schema semantics / 분류 스키마 의미론

### 5.1 Schema status

```text
CLASS_SCHEMA_STATUS:
  closed
  open
  partially_open
  externally_fixed
```

This is a declaration about how the schema is intended to operate. It is not by itself proof of coverage.

### 5.2 Coverage claim

```text
SCHEMA_COVERAGE_CLAIM:
  open_world_no_exhaustiveness_claim
  partial_coverage_claim
  closed_world_claim
  externally_fixed_scope_only
```

A `closed_world_claim` requires claim-relevant `CLOSED_SCHEMA_CLOSURE_EVIDENCE` at the target resolution.

```text
SCHEMA_STATUS_CLOSED
!= CLOSED_WORLD_COVERAGE_ESTABLISHED
```

### 5.3 Schema identity and version

Every assignment is relative to one identified schema state:

```text
CLASS_SCHEMA_ID_AND_VERSION
```

If a generated class or schema mutation occurs, all later assignments must identify the new active schema version.

---

## 6. Class-relation semantics / 클래스 간 관계 규율

`CLASS_RELATION_SEMANTICS` records any claim-relevant relation among classes, including:

```text
disjoint
overlapping
subsumption_or_refinement
ordered_by_declared_relation
independent
externally_fixed_relation
unspecified
```

`MUTUAL_EXCLUSION_RULES` applies whenever any classes are exclusive, regardless of whether multi-label output is allowed.

A subject satisfying criteria of two declared-disjoint classes does not authorize arbitrary tie-breaking. The run must use the frozen boundary/conflict rule or return a nonterminal status.

---

## 7. Criterion and decision semantics / 기준·판정 의미론

### 7.1 Criterion evaluation

Each class criterion must identify:

```text
CRITERION_ID
TARGET_CLASS_OR_RELATION
CRITERION_SOURCE
REQUIRED_FEATURES
APPLICABILITY_OR_PREREQUISITES
EVALUATION_RULE
EVALUATION_RESULT
UNRESOLVED_INPUTS
```

A criterion may be individually satisfied, not satisfied, unresolved, inapplicable, or blocked.

### 7.2 Criterion composition

A list of valid criteria is not yet a membership rule.

```text
CRITERION_LIST
!= MEMBERSHIP_LOGIC
```

`CRITERION_COMPOSITION_RULE` must be one explicit supplied rule, for example:

```text
conjunction
disjunction
k_of_n
veto_rule
weighted_threshold
ordered_rule_set
externally_fixed_decision_procedure
other_explicit_rule
```

`DECISION_RULE` specifies how composed results become one of the allowed membership statuses.

Criterion order, formatting, naming, or prose emphasis must not be used as an undeclared decision procedure.

---

## 8. Feature-state discipline / 특징 상태 규율

Each claim-relevant feature must preserve both value and status where relevant.

At minimum, the run must not collapse:

```text
missing
absent
inapplicable
applicable_but_undefined
defined_zero
defined_nonzero
out_of_scope
```

A feature may only be converted or mapped under an explicit `FEATURE_EXTRACTION_OR_MAPPING_RULE` or supplied bridge.

```text
MISSING != FALSE
UNDEFINED != ZERO
INAPPLICABLE != NEGATIVE
```

If the activated DSD Formation or General Property interface distinguishes additional statuses, those distinctions must be preserved when claim-relevant.

---

## 9. Uncertainty and boundary semantics / 불확실성·경계 규율

When a feature is measured, estimated, probabilistic, interval-valued, model-derived, or otherwise uncertain, the run must use:

```text
FEATURE_UNCERTAINTY_OR_TOLERANCE_POLICY
BOUNDARY_DECISION_SEMANTICS
```

If an uncertainty region intersects a class decision boundary, a central estimate alone cannot force membership unless the frozen rule explicitly justifies that operation.

Permitted outcomes include:

```text
CLASSIFIED_SINGLE
CLASSIFIED_MULTI
BOUNDARY_CASE
UNDERDETERMINED
BLOCKED_BY_MISSING_BRIDGE_OR_INFORMATION
```

`BOUNDARY_CASE` is a legitimate classification result. It is not automatically a protocol failure.

---

## 10. Generated-class and schema-mutation discipline / 생성 클래스·스키마 변이 규율

When `CLASS_SCHEMA_OR_GENERATION_POLICY` permits new classes, the following become mandatory:

```text
GENERATED_CLASS_PROVENANCE
CLASS_GENERATION_FREEZE_OR_MUTATION_POLICY
GENERATION_STOP_OR_CLOSURE_POLICY
```

Each generated class must record:

```text
GENERATED_CLASS_ID
PARENT_SCHEMA_ID_AND_VERSION
TRIGGERING_SUBJECT_OR_FEATURE_PATTERN
GENERATION_RULE_USED
GENERATION_TIME_OR_ORDER
NEW_SCHEMA_ID_AND_VERSION
```

A generated class is not retroactively treated as if it existed in the parent schema.

```text
PRE_GENERATION_SCHEMA
!= POST_GENERATION_SCHEMA
```

If generation has no supplied stopping/closure rule, the run cannot claim exhaustive class-space closure.

---

## 11. Special output obligations / 특수 산출 의무

### 11.1 Equivalence-class claims

Required fields:

```text
EQUIVALENCE_RELATION_OR_CRITERION
REFLEXIVITY_CHECK_SCOPE
SYMMETRY_CHECK_SCOPE
TRANSITIVITY_CHECK_SCOPE
EQUIVALENCE_COVERAGE
EQUIVALENCE_CLOSURE_REQUIREMENT
```

Pairwise similarities or a chain of successful pairwise comparisons do not establish an equivalence class unless the frozen closure requirement is satisfied.

### 11.2 Hierarchy or partial-order claims

Required fields:

```text
ORDER_RELATION
REFLEXIVITY_CHECK_SCOPE
ANTISYMMETRY_CHECK_SCOPE
TRANSITIVITY_CHECK_SCOPE
HIERARCHY_EDGE_PROVENANCE
```

Ordinal-looking names, numbers, severity levels, or presentation order do not prove an order relation.

### 11.3 Aggregate-based classification

Required fields:

```text
AGGREGATE_DEFINITION
AGGREGATE_SUPPORT
INFORMATION_LOSS_CHECK
COLLISION_POLICY
INJECTIVITY_OR_RECONSTRUCTION_CLAIM_IF_ANY
```

Equal aggregate/readout values cannot establish structural-class identity when distinct component states can collide under the readout.

### 11.4 Time-dependent classification

Required fields:

```text
TIME_OR_ORDER_DOMAIN
REGULAR_EPOCH_SCOPE
CLASS_EVALUATION_TIME
CLASS_TRANSITION_RULE
LINEAGE_REQUIREMENT
HISTORY_DEPENDENCE_POLICY
```

Class change does not automatically imply object/formation identity change. Shared current class does not establish shared lineage.

### 11.5 Multi-label or overlapping classes

Required fields:

```text
MULTI_MEMBERSHIP_SEMANTICS
OVERLAP_ALLOWED
MUTUAL_EXCLUSION_RULES
PRIORITY_RULE_IF_ANY
```

Multiple memberships are contradictory only if the frozen class-relation semantics make them contradictory.

---

## 12. Output levels / 산출 수준

```text
MEMBERSHIP_ASSIGNMENT
MULTI_MEMBERSHIP_PROFILE
CLASS_RELATION_PROFILE
EQUIVALENCE_CLASS_OUTPUT
HIERARCHY_OR_PARTIAL_ORDER_OUTPUT
TEMPORAL_CLASS_PROFILE
GENERATED_CLASS_OUTPUT
```

### MEMBERSHIP_ASSIGNMENT

Returns the strongest justified membership state for one subject under one frozen schema version.

### MULTI_MEMBERSHIP_PROFILE

Returns all simultaneously justified memberships when overlap is allowed and records any unresolved/exclusive conflicts.

### CLASS_RELATION_PROFILE

Returns declared and justified relations among classes without converting label order or proximity into relation semantics.

### EQUIVALENCE_CLASS_OUTPUT

Requires the equivalence closure obligations in Section 11.1.

### HIERARCHY_OR_PARTIAL_ORDER_OUTPUT

Requires the relation-law obligations in Section 11.2.

### TEMPORAL_CLASS_PROFILE

Records class membership by time/order and keeps class transition distinct from lineage or object identity.

### GENERATED_CLASS_OUTPUT

Records new-class provenance and schema-version transition; it is not a retroactive relabeling of the parent schema.

---

## 13. Membership statuses / 소속 상태

Protocol v0.1 uses the following status family:

```text
CLASSIFIED_SINGLE
CLASSIFIED_MULTI
BOUNDARY_CASE
UNDERDETERMINED
UNCLASSIFIED_WITHIN_DECLARED_SCHEMA
OUT_OF_SCOPE
CRITERION_CONFLICT
BLOCKED_BY_MISSING_BRIDGE_OR_INFORMATION
OPEN_WORLD_NO_CURRENT_MATCH
```

### CLASSIFIED_SINGLE

Exactly one class assignment is justified under the frozen decision semantics.

### CLASSIFIED_MULTI

Multiple assignments are simultaneously justified and permitted by the class-relation/multi-membership semantics.

### BOUNDARY_CASE

The subject lies on or crosses a declared decision boundary under the frozen uncertainty/tolerance semantics, or the class semantics explicitly designate the case as boundary.

### UNDERDETERMINED

Substantive evaluation is possible, but available evidence/coverage/decision closure is insufficient for a stronger membership claim.

### UNCLASSIFIED_WITHIN_DECLARED_SCHEMA

No class applies **and** the run has sufficient closed-world coverage evidence for the requested schema scope and resolution.

### OUT_OF_SCOPE

The subject is outside the declared classification universe or task scope.

### CRITERION_CONFLICT

Claim-relevant criteria or exclusive-class obligations conflict and the frozen resolution rules do not close the conflict.

### BLOCKED_BY_MISSING_BRIDGE_OR_INFORMATION

A claim-required bridge, criterion meaning, feature source, schema record, or prerequisite is unavailable before substantive evaluation can proceed.

### OPEN_WORLD_NO_CURRENT_MATCH

No currently registered class matches under an open or nonexhaustive schema. This is **not** universal nonmembership.

---

## 14. Validity gates / 유효성 게이트

Before any terminal assignment or closed-world nonmembership claim, evaluate:

```text
G1  schema identity/version is frozen where claim-relevant
G2  classification universe and target resolution are frozen
G3  class relation/exclusivity/overlap semantics are sufficient for the requested output
G4  schema coverage claim is explicit
G5  closed-world nonmembership has adequate closure evidence
G6  all required criteria have identifiable semantics and provenance
G7  criterion-composition and decision rules are explicit
G8  feature mappings/bridges are explicit and provenance-preserving
G9  missing/undefined/zero/inapplicable/out-of-scope states remain distinct where claim-relevant
G10 uncertainty/tolerance and boundary semantics are sufficient where required
G11 generated-class provenance and schema transition are recorded when generation occurs
G12 equivalence/hierarchy/aggregate/dynamic special claims satisfy their additional obligations
G13 neighboring-method outputs retain source-method and output-status provenance
G14 the requested output does not exceed evidence/coverage closure
```

Gate failure does not automatically mean `NONCONFORMANT`. A run that correctly returns a blocked, boundary, conflict, open-world-no-match, or underdetermined status may be protocol-conformant.

---

## 15. Executable operation sequence / 실행 순서

The following sequence is binding for Protocol v0.1:

```text
C1  LOCK TASK, TARGET RESOLUTION, SUBJECTS, CLASSIFICATION UNIVERSE, SCHEMA ID/VERSION, SCHEMA STATUS, AND COVERAGE CLAIM
C2  LOCK CLASS-RELATION SEMANTICS, OVERLAP/EXCLUSION RULES, AND CLAIMED OUTPUT LEVEL
C3  PRESERVE SUBJECT IDENTITY AND CLAIM-RELEVANT DSD/DOMAIN STATUSES AND TYPES
C4  READ OR DERIVE ONLY DECLARED CLASS-RELEVANT FEATURES THROUGH EXPLICIT MAPPINGS WITH PROVENANCE
C5  APPLY FROZEN UNCERTAINTY/TOLERANCE AND BOUNDARY POLICY WHERE CLAIM-RELEVANT
C6  CHECK CRITERION APPLICABILITY, PREREQUISITES, SOURCE, AND REQUIRED FEATURE AVAILABILITY
C7  EVALUATE EACH CRITERION WITHOUT LABEL-BASED OR NAME-BASED INFERENCE
C8  COMBINE CRITERION RESULTS ONLY THROUGH THE FROZEN COMPOSITION AND DECISION RULES
C9  RESOLVE PERMITTED OVERLAP, MUTUAL EXCLUSION, PRECEDENCE, DEPENDENCY, OR CONFLICT ONLY THROUGH SUPPLIED RULES
C10 ISSUE THE STRONGEST JUSTIFIED MEMBERSHIP STATUS WITHOUT FORCED TERMINAL LABELING
C11 RECORD BOUNDARY, MISSING INFORMATION, OPEN-WORLD NO-MATCH, UNCLASSIFIED-CLOSED-WORLD, AND OUT-OF-SCOPE CASES SEPARATELY
C12 VALIDATE EQUIVALENCE, HIERARCHY, AGGREGATE, TEMPORAL, AND OTHER SPECIAL CLAIMS UNDER THEIR ADDITIONAL CLOSURE OBLIGATIONS
C13 IF CLASS GENERATION IS PERMITTED AND TRIGGERED, RECORD GENERATION PROVENANCE, SCHEMA MUTATION, ACTIVE VERSION, AND STOP/CLOSURE STATUS
C14 RECORD JUSTIFICATION TRACE, LIMITS, HANDOFFS, PROTOCOL CONFORMANCE, BASELINE/NO_GAIN STATUS, AND REPRODUCIBILITY DATA
```

No step may silently add a criterion, bridge, class relation, hierarchy, equivalence relation, transformation, diagnostic explanation, lineage claim, or audit verdict.

---

## 16. Required result record / 필수 결과 레코드

Each subject-level result must record:

```text
CLASSIFICATION_RESULT_ID
CLASSIFICATION_TASK_ID
SUBJECT_ID
CLASS_SCHEMA_ID_AND_VERSION_USED
APPLICABLE_CLASS_SCHEMA
CLAIMED_OUTPUT_LEVEL

CLASS_ASSIGNMENT_OR_ASSIGNMENTS
MEMBERSHIP_STATUS

CRITERIA_SATISFIED
CRITERIA_NOT_SATISFIED
CRITERIA_UNRESOLVED
CRITERIA_INAPPLICABLE
CRITERION_COMPOSITION_RESULT
DECISION_RULE_RESULT

FEATURES_USED_WITH_PROVENANCE
FEATURE_STATUS_RECORD
UNCERTAINTY_OR_BOUNDARY_RECORD
BRIDGES_USED

BOUNDARY_RECORD
MISSING_INFORMATION_RECORD
OUT_OF_SCOPE_RECORD
OPEN_WORLD_NO_MATCH_RECORD
CONFLICT_RECORD

SCHEMA_COVERAGE_AND_CLOSURE_RECORD
INFORMATION_LOSS_CHECK_IF_ANY
TEMPORAL_OR_LINEAGE_RECORD_IF_ANY
GENERATED_CLASS_OR_SCHEMA_MUTATION_RECORD_IF_ANY

JUSTIFICATION_TRACE
BASELINE_RESULT_IF_ANY
NO_GAIN_STATUS_IF_ANY
LIMITS
REPRODUCIBILITY_RECORD
PROTOCOL_CONFORMANCE
```

No failed, unresolved, inapplicable, or missing claim-relevant condition may be erased merely because another criterion succeeds.

---

## 17. Protocol conformance ledger / 프로토콜 적합성

```text
CLASSIFICATION_PROTOCOL_CONFORMANCE:
  CONFORMANT
  NONCONFORMANT
  UNDETERMINED
```

A run may end in `BOUNDARY_CASE`, `UNDERDETERMINED`, `CRITERION_CONFLICT`, `OPEN_WORLD_NO_CURRENT_MATCH`, or `BLOCKED_BY_MISSING_BRIDGE_OR_INFORMATION` and still be `CONFORMANT` if that status correctly preserves the task limits.

Representative `NONCONFORMANT` conditions include:

```text
CLASS_LABEL_USED_AS_MEMBERSHIP_CRITERION
MISSING_FEATURE_COERCED_TO_NEGATIVE
UNDEFINED_COERCED_TO_DEFINED_ZERO
OUT_OF_SCOPE_RELABELLED_UNCLASSIFIED
OPEN_WORLD_NO_MATCH_RELABELLED_UNIVERSAL_NONMEMBERSHIP
SCHEMA_DECLARED_CLOSED_TREATED_AS_PROVEN_EXHAUSTIVE_WITHOUT_CLOSURE_EVIDENCE
CRITERION_LIST_USED_WITHOUT_COMPOSITION_OR_DECISION_RULE
HIDDEN_TIE_BREAKING_BETWEEN_EXCLUSIVE_CLASSES
MULTI_MEMBERSHIP_RELABELLED_CONFLICT_WITHOUT_EXCLUSION_RULE
PAIRWISE_SIMILARITY_UPGRADED_TO_EQUIVALENCE_CLASS
ORDINAL_LABEL_UPGRADED_TO_HIERARCHY_OR_PARTIAL_ORDER
AGGREGATE_EQUALITY_UPGRADED_TO_STRUCTURAL_CLASS_IDENTITY
CENTRAL_ESTIMATE_FORCED_ACROSS_UNRESOLVED_BOUNDARY
GENERATED_CLASS_USED_WITHOUT_PROVENANCE_OR_SCHEMA_VERSION_TRANSITION
CLASS_CHANGE_UPGRADED_TO_OBJECT_IDENTITY_CHANGE
CURRENT_CLASS_MATCH_UPGRADED_TO_COMMON_LINEAGE
NEIGHBORING_METHOD_OUTPUT_USED_WITHOUT SOURCE/STATUS PROVENANCE
UNDECLARED_BRIDGE_OR_FEATURE_TRANSFORMATION
UNRECORDED_SCHEMA_OR_CRITERION_REVISION
```

---

## 18. Method-gain ledger / 방법 이득 장부

```text
CLASSIFICATION_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

`GAIN_ESTABLISHED` or `NO_GAIN` requires a separately frozen competent baseline and gain criterion.

Both DSD Classification and the baseline must receive the same:

```text
task
subject records
schema/version
criteria
membership logic
feature evidence
external standards
claim-relevant bridges
```

Correct protocol execution alone does not establish comparative gain.

`NO_GAIN` is a valid result and is not evidence for method absorption or deletion.

---

## 19. Method boundaries / 방법 경계

```text
Analysis:
  supplied subject -> internal decomposition / structural re-expression

Comparison:
  supplied subjects -> cross-subject preservation / correspondence / divergence profile

Classification:
  supplied subject(s) + schema/criteria -> class-membership and class-relation result

Interpretation:
  supplied source/context -> context-sensitive interpretive reading

Specification:
  supplied target/requirements -> explicit requirement and status structure

Diagnosis:
  observations -> candidate cause / latent-state inference

Aggregation:
  component states -> declared aggregate/readout

Transformation:
  source representation/regime -> target representation/regime

Lineage/Provenance:
  records -> origin/successor/history relation

Audit:
  prior process/result -> conformance / defect retrace
```

Classification may consume outputs of neighboring methods only through explicit handoffs. Their outputs do not become native Classification findings by renaming.

---

## 20. Failure, nonterminal, and NO_GAIN interpretation / 실패·비종결·무이득 해석

The following distinctions are mandatory:

```text
PROTOCOL_NONCONFORMANCE
!= SUBJECT_NOT_IN_CLASS

BOUNDARY_CASE
!= METHOD_FAILURE

UNDERDETERMINED
!= NEGATIVE_MEMBERSHIP

OPEN_WORLD_NO_CURRENT_MATCH
!= UNIVERSAL_NONMEMBERSHIP

NO_GAIN
!= INVALID_METHOD

CASE_FAILURE
!= METHOD_DELETION_DECISION
```

Method survival, merger, absorption, and deletion are separate registry/governance questions and are not decided by one challenge outcome.

---

## 21. Reproducibility record / 재현성 레코드

A reproducible run must preserve enough information to rerun the classification at the same task resolution:

```text
PROTOCOL_VERSION
TASK_FREEZE_REFERENCE
SCHEMA_ID_AND_VERSION
SUBJECT_INPUT_IDENTIFIERS
CRITERION_SOURCE_IDENTIFIERS
FEATURE_SOURCE_IDENTIFIERS
MAPPING_OR_EXTRACTION_RULES
DECISION_RULE
EXTERNAL_STANDARD_VERSION_IF_ANY
AUXILIARY_METHOD_OUTPUT_IDENTIFIERS_IF_ANY
RUN_ORDER_IF_SCHEMA_MUTATION_IS_POSSIBLE
RESULT_RECORD_IDENTIFIERS
```

A same-project deterministic retrace is not independent replication.

---

## 22. Protocol versioning / 프로토콜 버전 관리

Protocol v0.1 is frozen for prospective use.

A future protocol revision is required only if execution exposes a semantic defect, missing required state, invalid closure rule, or other protocol-level flaw. A difficult case, `NO_GAIN`, blocked case, or unfavorable result does not by itself justify rewriting the protocol.

Historical runs remain associated with the protocol version under which they were executed.

---

## 23. Evidence status after protocol establishment / 프로토콜 구축 후 증거 상태

```text
DEDICATED_CLASSIFICATION_PROTOCOL: established v0.1
TASK_INTERFACE_DRAFT: v0.1 historical draft preserved
PRE_PROTOCOL_BOUNDARY_ATTACKS: 18 completed
BOUNDARY_AMENDMENT_001: established
DIRECT_CLASSIFICATION_PILOTS: 0
POSITIVE_DIRECT_CHALLENGES: 0
NEGATIVE_FAILURE_CHALLENGES: 0
METHOD_BOUNDARY_CHALLENGES: 0
EXTERNAL_CLASSIFICATION_APPLICATIONS: 0
REPRODUCIBILITY_CASES: 0
INDEPENDENT_CLASSIFICATION_VALIDATION: not established
CLASSIFICATION_METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_CLASSIFICATION_EVIDENCE_STATUS: pre_validation
```

Protocol maturity and evidence maturity remain separate axes.

---

## 24. Next / 다음

Freeze and execute the first **positive direct challenge** against Protocol v0.1.

The first challenge should require a justified terminal classification while simultaneously checking that the protocol preserves at least one claim-relevant distinction that a label-only classifier could collapse. The challenge must be frozen before execution and must not be designed so that success is guaranteed by construction.
