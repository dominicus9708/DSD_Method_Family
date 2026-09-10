# DSD Comparison Protocol v0.1 / DSD 비교론 실행 프로토콜 v0.1

Status: **EXECUTABLE PROTOCOL — frozen**  
Date: **2026-09-10**  
Method: **DSD Comparison / DSD 비교론**

## 1. Protocol lineage / 프로토콜 계보

This protocol prospectively integrates the historical planning artifacts:

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

The original draft and amendment remain preserved. This protocol does not retroactively rewrite them.

Planning attacks that informed this protocol:

```text
BOUNDARY_ATTACKS_RUN: 16
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
```

Protocol establishment itself is infrastructure, not direct Comparison validation.

---

## 2. Core method form / 핵심 방법 형태

```text
supplied comparison subjects
+ declared comparison scope and target resolution
+ supplied map/correspondence family
+ preservation/equivalence criteria
-> justified correspondence, preservation, divergence, and closure profile
```

Comparison does not create the compared subjects, silently transform them, assign them to a taxonomy, validate a prior process, or infer historical lineage from similarity.

---

## 3. Core guards / 핵심 가드

```text
AGGREGATE_EQUALITY != STRUCTURAL_EQUIVALENCE
ONE_MAP_FAILURE != GLOBAL_NONCORRESPONDENCE
COMMON_LABEL != COMMON_COORDINATE_OR_SEMANTIC_ROLE
EMBEDDING != STRICT_EQUIVALENCE
FIRST_OBSERVED_DIFFERENCE != FIRST_JUSTIFIED_BRANCH_POINT
PARTIAL_CORRESPONDENCE != GLOBAL_EQUIVALENCE
ENCODING_REQUIRED_CORRESPONDENCE != DIRECT_CORRESPONDENCE
SIMILAR_OUTPUT != SHARED_LINEAGE_OR_IDENTITY
FORWARD_MAP_SUCCESS != REVERSE_MAP_SUCCESS
MAP_FAMILY_COVERAGE != COMPARISON_ELEMENT_COVERAGE
UNSUPPLIED_NORMALIZATION_OR_CONVERSION != COMPARISON_MAP
DYNAMIC_TRAJECTORY_SIMILARITY != SHARED_LINEAGE_OR_IDENTITY
MISSING_COMPARISON_BRIDGE != PROVEN_STRUCTURAL_DIFFERENCE
CASE_PASS != METHOD_SURVIVAL_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
```

---

## 4. Required task record / 필수 과업 레코드

Every new Protocol-v0.1 run must lock the following before substantive comparison whenever the field is claim-relevant.

```text
COMPARISON_TASK_ID
TASK_SCOPE
CLAIMED_OUTPUT_LEVEL
TARGET_RESOLUTION

SUBJECT_SET
SUBJECT_IDENTITY_RECORDS
SUBJECT_STAGE_OR_LAYER_RECORDS
SUBJECT_STATUS_RECORDS

COMPARISON_DIRECTIONALITY
COMPARISON_DOMAIN_OR_SHARED_SCOPE
COMPARISON_DOMAIN_SOURCE

CORRESPONDENCE_OR_MAP_FAMILY
MAP_FAMILY_SOURCE
MAP_FAMILY_COVERAGE
MAP_DIRECTION
MAP_PROPERTY_REQUIREMENT_PROFILE
REVERSE_DIRECTION_OR_INVERSE_POLICY

COMPARISON_ELEMENT_COVERAGE
CLOSURE_REQUIREMENT_BY_OUTPUT_LEVEL

COORDINATE_OR_FEATURE_MATCHING_RULE
RELATION_PRESERVATION_RULE
PROPERTY_COMPARISON_RULE
STATUS_DISTINCTION_RULE
EQUIVALENCE_CRITERION

ENCODING_OR_BRIDGE_RULE
PRECOMPARISON_TRANSFORMATION_POLICY
REPRESENTATION_PROVENANCE

FIRST_BRANCH_CLAIM_POLICY
FIRST_BRANCH_SEARCH_BASIS
FIRST_BRANCH_SEARCH_COVERAGE

AGGREGATE_READOUTS_IF_ANY
AGGREGATE_COLLISION_POLICY

DYNAMIC_LINEAGE_SCOPE
LINEAGE_IDENTITY_CLAIM_POLICY
LINEAGE_EVIDENCE_SOURCE_OR_HANDOFF

TARGET_DSD_LAYER_SCOPE
DSD_INTERFACE_PROFILE
DOMAIN_BRIDGE
EXTERNAL_STANDARD
VALIDATION_OR_ACCEPTANCE_RULE
AUXILIARY_METHODS_OR_HANDOFFS
```

A claim-relevant field may be `not_applicable` only when non-use is explicit and consistent with the requested output.

---

## 5. Coverage vocabularies / 범위 어휘

### 5.1 Map-family coverage

```text
MAP_FAMILY_COVERAGE:
  exhaustive
  non_exhaustive
  unknown
```

This describes coverage of admissible maps/correspondences under the declared family.

### 5.2 Comparison-element coverage

For each claim-relevant element class:

```text
coordinates_or_features
relations
properties
status_classes
stages_or_layers
```

record one of:

```text
exhaustive
sufficient_by_argument
partial
unknown
not_applicable
```

Map-family coverage and element coverage are independent axes.

### 5.3 First-branch search coverage

```text
FIRST_BRANCH_SEARCH_COVERAGE:
  exhaustive
  sufficient_by_argument
  non_exhaustive
  unknown
```

A first-branch claim requires sufficient coverage of every earlier claim-relevant stage, not merely a difference observed first in traversal order.

---

## 6. Map-property and direction requirements / 대응 성질·방향 요구

`MAP_PROPERTY_REQUIREMENT_PROFILE` may require one or more supplied properties, for example:

```text
injective_required
surjective_required
bijective_required
inverse_preservation_required
isometric_required
homomorphic_required
embedding_sufficient_for_this_claim
custom_supplied_criterion
not_applicable
```

`REVERSE_DIRECTION_OR_INVERSE_POLICY` is one of:

```text
not_required
required_and_supplied
required_but_unverified
separate_reverse_search_required
```

A forward map satisfies only the claims justified by the frozen criterion. No inverse, surjectivity, symmetry, or equivalence property is supplied by implication.

---

## 7. Precomparison transformation policy / 사전 변환 규율

```text
PRECOMPARISON_TRANSFORMATION_POLICY:
  none_required
  supplied_transformed_representation
  external_transformation_handoff_required
  transformation_not_permitted_in_comparison
```

When a transformed representation is used, `REPRESENTATION_PROVENANCE` must identify, when relevant:

```text
original_subject_representation
supplied_transformed_representation_id
transformation_source_or_rule
transformation_output_identity
whether_transformation_was_completed_before_Comparison
```

Comparison may consume an already supplied transformation result. It must not invent or execute a claim-relevant conversion and then relabel that operation as a Comparison map.

---

## 8. Lineage-identity policy / 계보·동일성 규율

```text
LINEAGE_IDENTITY_CLAIM_POLICY:
  not_claimed
  supplied_external_lineage_record
  lineage_method_handoff_required
```

If historical/successor identity is claim-relevant, the run must either cite the supplied lineage evidence or hand the claim to the appropriate Lineage/Provenance method.

Static or dynamic similarity is a comparison result, not lineage evidence by itself.

---

## 9. Output levels / 산출 수준

```text
COMPARISON_PROFILE
CORRESPONDENCE_CLASSIFICATION
STRICT_EQUIVALENCE_DECISION
FIRST_BRANCH_POINT
PARTIAL_COMPARISON
```

### COMPARISON_PROFILE

May record a mixed result containing preserved, diverged, encoded, untested, blocked, or unresolved elements. Untested remainder must remain explicit.

### CORRESPONDENCE_CLASSIFICATION

Returns the strongest relation class supported at `TARGET_RESOLUTION` under the frozen map family, element coverage, and criteria.

### STRICT_EQUIVALENCE_DECISION

Returns a yes/no/underdetermined decision only when every claim-relevant equivalence condition is evaluated or a supplied sufficient criterion closes the claim.

### FIRST_BRANCH_POINT

Returns the earliest justified divergence only when earlier relevant stages are sufficiently covered and preserved.

### PARTIAL_COMPARISON

Closes only the declared subset and must retain the unresolved remainder.

---

## 10. Comparison relation classes / 비교 관계 분류

```text
STRICT_EQUIVALENT
DIRECT_CORRESPONDENCE
PARTIAL_CORRESPONDENCE
ENCODED_CORRESPONDENCE
NONCORRESPONDENCE
UNDETERMINED_CORRESPONDENCE
```

Rules:

- `STRICT_EQUIVALENT` requires the frozen strict-equivalence criterion and its coverage requirements.
- `DIRECT_CORRESPONDENCE` uses no claim-relevant encoding/representation bridge beyond the frozen direct map rule.
- `ENCODED_CORRESPONDENCE` must remain marked encoded when a supplied bridge is necessary.
- `PARTIAL_CORRESPONDENCE` may not be upgraded because every tested element happened to match.
- `NONCORRESPONDENCE` requires sufficient closure for the declared map/element family; failure of one map is insufficient when other admissible maps remain untested.
- `UNDETERMINED_CORRESPONDENCE` preserves unresolved map, bridge, or element coverage rather than converting uncertainty into difference.

---

## 11. Terminal status / 종결 상태

```text
COMPARISON_RESOLVED
COMPARISON_UNDERDETERMINED
COMPARISON_BLOCKED
```

### COMPARISON_RESOLVED

The requested output level is justified inside the frozen scope. A resolved result may be equivalence, direct/partial/encoded correspondence, justified noncorrespondence, or a supported first branch.

### COMPARISON_UNDERDETERMINED

Substantive comparison was possible, but the requested closure is not justified because required map-family, element, reverse-direction, or first-branch coverage remains unresolved.

### COMPARISON_BLOCKED

A claim-required subject record, semantic/shared domain, criterion, map/bridge definition, or precomparison representation is unavailable before the requested substantive comparison can be performed.

```text
MISSING_BRIDGE -> BLOCKED
```

when the bridge is required before substantive cross-domain comparison. It is not converted into `NONCORRESPONDENCE`.

---

## 12. Candidate map/correspondence record / 후보 레코드

For each evaluated candidate map/correspondence, record:

```text
MAP_OR_CORRESPONDENCE_ID
SUBJECTS_COMPARED
MAP_DEFINITION
MAP_DIRECTION
MAP_DOMAIN
MAP_CODOMAIN

COORDINATE_MATCH_RESULT
RELATION_PRESERVATION_RESULT
PROPERTY_COMPARISON_RESULT
STATUS_DISTINCTION_RESULT

ENCODING_OR_BRIDGE_USED
PRECOMPARISON_TRANSFORMATION_PROVENANCE

INJECTIVITY_SURJECTIVITY_OR_OTHER_REQUIRED_PROPERTIES
REQUIRED_MAP_PROPERTIES_RESULT
REVERSE_DIRECTION_OR_INVERSE_RESULT
ELEMENT_COVERAGE_RESULT

AGGREGATE_READOUT_COMPARISON_RESULT
STRUCTURAL_EQUIVALENCE_RESULT
CORRESPONDENCE_CLASS_RESULT
LINEAGE_IDENTITY_CLAIM_RESULT

FAILURE_SET
UNTESTED_OR_UNRESOLVED_SET
TRACE_OR_OUTPUT_ID
```

Do not remove an unresolved or failed condition merely because another map or coordinate succeeds.

---

## 13. First-branch record / 최초 분기 레코드

When `FIRST_BRANCH_POINT` is requested, record:

```text
BRANCH_CANDIDATE_STAGE
EARLIER_STAGE_PRESERVATION_RECORD
EARLIER_STAGE_COVERAGE
BRANCH_STAGE_DIFFERENCE_RECORD
ALTERNATIVE_MAPS_OR_BRIDGES_CHECKED
FIRST_BRANCH_RESULT:
  established
  not_established
  underdetermined
  blocked
```

A difference at stage `k` establishes only `difference_at_k` unless the earlier-stage closure requirement is also satisfied.

---

## 14. Aggregate-collision discipline / 집계 충돌 규율

Aggregate/readout results are recorded separately from structural comparison.

The following is a legitimate result:

```text
AGGREGATE_READOUT: equal
STRUCTURAL_SUPPORT_OR_RELATION: different
STRICT_EQUIVALENCE: not established
```

Equal finite or analytic aggregate output does not reconstruct support, decomposition, cause, channel identity, Property status, or structure without an independently supplied injective/sufficient reconstruction condition.

---

## 15. Output-level closure requirements / 산출별 폐쇄 규칙

Before a requested output is marked resolved:

```text
COMPARISON_PROFILE
  -> may retain explicitly untested/unresolved remainder.

CORRESPONDENCE_CLASSIFICATION
  -> enough map-property, direction, map-family, and element coverage for the claimed class.

STRICT_EQUIVALENCE_DECISION
  -> all claim-relevant equivalence conditions closed, or a supplied sufficient theorem/criterion.

FIRST_BRANCH_POINT
  -> branch-stage difference established AND every earlier relevant stage sufficiently covered/preserved.

PARTIAL_COMPARISON
  -> declared subset closed AND unresolved remainder explicitly retained.
```

If these conditions are not met after substantive comparison, use `COMPARISON_UNDERDETERMINED` rather than a stronger relation claim.

---

## 16. Executable operation sequence / 실행 순서

```text
C1  LOCK SUBJECTS, CLAIMED OUTPUT, TARGET RESOLUTION, AND COMPARISON SCOPE
C2  LOCK MAP/CORRESPONDENCE FAMILY, SOURCE, DIRECTION, AND MAP-FAMILY COVERAGE
C3  LOCK REQUIRED MAP PROPERTIES AND REVERSE/INVERSE POLICY
C4  LOCK CLAIM-RELEVANT ELEMENT COVERAGE AND OUTPUT-LEVEL CLOSURE REQUIREMENTS
C5  LOCK FEATURE/COORDINATE, RELATION, PROPERTY, STATUS, AND EQUIVALENCE RULES
C6  LOCK ENCODING/BRIDGE AND PRECOMPARISON-TRANSFORMATION POLICY/PROVENANCE
C7  LOCK FIRST-BRANCH SEARCH BASIS/COVERAGE AND LINEAGE-IDENTITY CLAIM POLICY
C8  LOCK OPTIONAL AGGREGATE READOUTS, DOMAIN BRIDGES, EXTERNAL STANDARDS, AND HANDOFFS
C9  CHECK REQUIRED SUBJECT RECORDS AND CLAIM-REQUIRED MAPS/BRIDGES/REPRESENTATIONS
C10 EVALUATE ONLY THE COVERED SUPPLIED MAPS/CORRESPONDENCES
C11 EVALUATE REQUIRED MAP PROPERTIES AND REVERSE/INVERSE CONDITIONS
C12 RECORD PRESERVED, DIVERGED, ENCODED, UNTESTED, AND UNRESOLVED ELEMENTS
C13 EVALUATE CORRESPONDENCE / STRICT-EQUIVALENCE CLOSURE AT TARGET RESOLUTION
C14 EVALUATE FIRST-BRANCH CLAIM ONLY UNDER SUFFICIENT EARLIER-STAGE COVERAGE
C15 RECORD AGGREGATE COLLISIONS WITHOUT STRUCTURAL UPGRADE
C16 RECORD DYNAMIC/STATIC SIMILARITY SEPARATELY FROM LINEAGE IDENTITY
C17 ASSIGN REQUESTED OUTPUT LEVEL AND TERMINAL COMPARISON STATUS
C18 RECORD COMPARISON PROTOCOL CONFORMANCE
C19 RECORD METHOD GAIN ONLY AGAINST A FROZEN COMPETENT BASELINE
C20 RECORD LIMITS, HANDOFFS, AND REPRODUCIBILITY DATA
```

No step may silently create a missing semantic bridge, transformation, taxonomy, audit verdict, or lineage record.

---

## 17. Protocol conformance ledger / 프로토콜 적합성

```text
COMPARISON_PROTOCOL_CONFORMANCE:
  CONFORMANT
  NONCONFORMANT
  UNDETERMINED
```

A run may be `COMPARISON_BLOCKED` and still be `CONFORMANT` if it correctly exposes a missing claim-required input instead of fabricating one.

Representative `NONCONFORMANT` conditions include:

```text
AGGREGATE_EQUALITY_UPGRADED_TO_STRUCTURAL_EQUIVALENCE
GLOBAL_NONCORRESPONDENCE_FROM_ONE_MAP_FAILURE
STRICT_EQUIVALENCE_FROM_INSUFFICIENT_EMBEDDING
COMMON_LABEL_TREATED_AS_SEMANTIC_MATCH_WITHOUT_RULE
PARTIAL_COVERAGE_UPGRADED_TO_GLOBAL_EQUIVALENCE
ENCODED_CORRESPONDENCE_RELABELLED_DIRECT
FIRST_OBSERVED_DIFFERENCE_RELABELLED_FIRST_BRANCH
FALSE_CLOSURE_FROM_NONEXHAUSTIVE_MAP_FAMILY
FALSE_CLOSURE_FROM_PARTIAL_ELEMENT_COVERAGE
UNDECLARED_REVERSE_OR_INVERSE_ASSUMPTION
HIDDEN_PRECOMPARISON_TRANSFORMATION
HIDDEN_CLASSIFICATION_SUBSTITUTION
HIDDEN_AUDIT_VERDICT
LINEAGE_OR_IDENTITY_FROM_SIMILARITY_ALONE
PROPERTY_STATUS_COLLAPSE
MISSING_BRIDGE_RELABELLED_STRUCTURAL_DIFFERENCE
UNRECORDED_TASK_OR_CRITERION_REVISION
NEIGHBORING_METHOD_VERDICT_ABSORPTION
```

---

## 18. Method-gain ledger / 방법 이득 장부

```text
COMPARISON_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

`GAIN_ESTABLISHED` or `NO_GAIN` requires a separately frozen competent baseline and criterion. Correct Comparison execution alone does not establish comparative gain.

Extra terminology or bookkeeping is not by itself a gain.

---

## 19. Method boundaries / 방법 경계

```text
Analysis:
  supplied subject -> internal decomposition / structure description

Comparison:
  supplied subjects -> cross-subject preservation / correspondence / divergence / equivalence profile

Classification:
  supplied subject(s) -> taxonomy-based class assignment

Transformation:
  source representation/regime -> target representation/regime

Audit:
  prior process/result -> conformance or defect retrace

Provenance/Lineage:
  source/successor/history records -> origin or identity-chain claim

Aggregation:
  admitted data/structure -> declared readout
```

Comparison may consume outputs from these methods but does not absorb their distinct operations or verdicts.

---

## 20. Reproducibility record / 재현성 레코드

Every direct Protocol-v0.1 evidence run should preserve enough data to retrace:

```text
PROTOCOL_VERSION_OR_COMMIT
CASE_ID
PRECOMMIT_ID_OR_COMMIT_WHEN_APPLICABLE
SUBJECT_RECORD_IDS
MAP_OR_BRIDGE_DEFINITIONS
MAP_AND_ELEMENT_COVERAGE
TARGET_RESOLUTION
CRITERIA_AND_OUTPUT_LEVEL
CANDIDATE_RESULTS
TERMINAL_STATUS
CONFORMANCE_LEDGER
GAIN_LEDGER
LIMITS_AND_HANDOFFS
```

Same-project deterministic retrace, external application, independent replication, and independent evaluation must remain separately labeled.

---

## 21. Evidence rule / 증거 규칙

The protocol freeze does **not** increment direct evidence counts.

The first direct Comparison challenge must be assigned a new `CMP-CH-###` ID and, when expected outputs matter, must be separately precommitted before execution.

```text
PROTOCOL_ESTABLISHED != METHOD_VALIDATED
PRE_PROTOCOL_BOUNDARY_PASS != DIRECT_EVIDENCE
DIRECT_CASE_PASS != PERMANENT_METHOD_INDEPENDENCE
```

## 22. Immediate next step / 다음

Precommit and execute `CMP-CH-001`, a positive constructed challenge that simultaneously tests:

```text
at least one strict-equivalence case with sufficient closure
at least one direct correspondence weaker than strict equivalence
at least one encoded correspondence
at least one aggregate collision where equal readout does not erase structural difference
explicit map-property and element-coverage records
three-ledger separation
```

The challenge must not be retrofitted after seeing its result.
