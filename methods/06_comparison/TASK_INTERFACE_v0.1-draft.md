# DSD Comparison Task Interface v0.1-draft / DSD 비교론 과업 인터페이스 초안

Status: **planning draft / not executable protocol**  
Date: **2026-09-10**  
Method: **DSD Comparison / DSD 비교론**

## 1. Core method form / 핵심 방법 형태

```text
supplied comparison subjects
+ declared comparison scope/resolution
+ supplied correspondence/bridge family
+ preservation/equivalence criteria
-> comparison relation/profile and justified divergence claims
```

Comparison does not reduce structural comparison to final-output equality.
It records what is preserved, what diverges, at what declared layer/resolution the divergence is supported, and what remains untested.

## 2. Core guards / 핵심 가드

```text
AGGREGATE_EQUALITY
!= STRUCTURAL_EQUIVALENCE

ONE_MAP_FAILURE
!= GLOBAL_NONCORRESPONDENCE

COMMON_LABEL
!= COMMON_COORDINATE_OR_SEMANTIC_ROLE

EMBEDDING
!= STRICT_EQUIVALENCE

FIRST_OBSERVED_DIFFERENCE
!= FIRST_JUSTIFIED_BRANCH_POINT

PARTIAL_CORRESPONDENCE
!= GLOBAL_EQUIVALENCE

ENCODING_REQUIRED_CORRESPONDENCE
!= DIRECT_CORRESPONDENCE

SIMILAR_OUTPUT
!= SHARED_LINEAGE_OR_IDENTITY
```

## 3. Minimum task fields / 최소 과업 필드

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

COORDINATE_OR_FEATURE_MATCHING_RULE
RELATION_PRESERVATION_RULE
PROPERTY_COMPARISON_RULE
STATUS_DISTINCTION_RULE
EQUIVALENCE_CRITERION
ENCODING_OR_BRIDGE_RULE

FIRST_BRANCH_CLAIM_POLICY
FIRST_BRANCH_SEARCH_BASIS
FIRST_BRANCH_SEARCH_COVERAGE

AGGREGATE_READOUTS_IF_ANY
AGGREGATE_COLLISION_POLICY

DYNAMIC_LINEAGE_SCOPE
TARGET_DSD_LAYER_SCOPE
DSD_INTERFACE_PROFILE
DOMAIN_BRIDGE
EXTERNAL_STANDARD
VALIDATION_OR_ACCEPTANCE_RULE
AUXILIARY_METHODS_OR_HANDOFFS
```

Conditional non-use must be explicit rather than silently omitted when it affects the claim.

## 4. Output levels / 주장 산출 수준

```text
COMPARISON_PROFILE
CORRESPONDENCE_CLASSIFICATION
STRICT_EQUIVALENCE_DECISION
FIRST_BRANCH_POINT
PARTIAL_COMPARISON
```

### COMPARISON_PROFILE
Records the compared coordinates/features/relations/statuses, preserved subset, diverged subset, untested subset, and active bridge/map family.

### CORRESPONDENCE_CLASSIFICATION
Assigns the strongest supported relation class at target resolution under the declared map/bridge family.

### STRICT_EQUIVALENCE_DECISION
Makes an explicit strict-equivalence yes/no/underdetermined claim under the frozen criterion. Aggregate equality is insufficient.

### FIRST_BRANCH_POINT
Claims the earliest supported divergence stage/layer only when all earlier claim-relevant stages are sufficiently covered and preserved under the frozen search basis.

### PARTIAL_COMPARISON
Returns a declared subcomparison while explicitly preserving unresolved coordinates, relations, map families, or stages.

## 5. Comparison relation classes / 비교 관계 분류

```text
STRICT_EQUIVALENT
DIRECT_CORRESPONDENCE
PARTIAL_CORRESPONDENCE
ENCODED_CORRESPONDENCE
NONCORRESPONDENCE
UNDETERMINED_CORRESPONDENCE
```

These classes are interpreted at `TARGET_RESOLUTION` and under the frozen criterion.
`STRICT_EQUIVALENT` is stronger than merely sharing a final scalar/vector output.
`ENCODED_CORRESPONDENCE` means a declared bridge/encoding is required; it is not relabeled as direct correspondence.

## 6. Terminal comparison status / 종결 상태

```text
COMPARISON_RESOLVED
COMPARISON_UNDERDETERMINED
COMPARISON_BLOCKED
```

`COMPARISON_RESOLVED` means the requested output level is justified within the declared scope.
It may resolve to strict equivalence, partial/direct/encoded correspondence, or noncorrespondence.

`COMPARISON_UNDERDETERMINED` means some comparison can be performed but the requested closure is not justified by current map/search coverage or data.

`COMPARISON_BLOCKED` means a claim-required subject record, comparison scope, criterion, or bridge/map definition is unavailable before substantive comparison.

## 7. Coverage discipline / 범위 규율

```text
MAP_FAMILY_COVERAGE:
  exhaustive
  non_exhaustive
  unknown

FIRST_BRANCH_SEARCH_COVERAGE:
  exhaustive
  sufficient_by_argument
  non_exhaustive
  unknown
```

Failure of one chosen map does not establish noncorrespondence if other admissible maps remain untested.
Likewise, a first-branch claim cannot be inferred from the first difference encountered by an arbitrary traversal order.

## 8. Candidate map record / 후보 대응 레코드

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
INJECTIVITY_SURJECTIVITY_OR_OTHER_REQUIRED_PROPERTIES
AGGREGATE_READOUT_COMPARISON_RESULT
STRUCTURAL_EQUIVALENCE_RESULT
CORRESPONDENCE_CLASS_RESULT
FAILURE_SET
UNTESTED_OR_UNRESOLVED_SET
TRACE_OR_OUTPUT_ID
```

## 9. First-branch record / 최초 분기 레코드

```text
BRANCH_CANDIDATE_STAGE
EARLIER_STAGE_PRESERVATION_RECORD
EARLIER_STAGE_COVERAGE
BRANCH_STAGE_DIFFERENCE_RECORD
ALTERNATIVE_MAPS_OR_BRIDGES_CHECKED
FIRST_BRANCH_RESULT:
  established / not_established / underdetermined / blocked
```

A supported difference at stage k is not enough to call k the first branch unless all earlier relevant stages are sufficiently preserved/closed for the claim.

## 10. Aggregate collision discipline / 집계 충돌 규율

When aggregate/readout values are available, record them separately.

```text
AGGREGATE_EQUAL
STRUCTURE_DIFFERENT
```

is a valid comparison outcome.
Do not infer reconstruction or structural identity from equal aggregate output unless injectivity or another sufficient condition is independently supplied.

## 11. Method boundaries / 방법 경계

```text
Analysis:
  one/few subjects -> internal decomposition/structure description

Comparison:
  two or more supplied subjects -> correspondence, preservation, divergence, equivalence profile

Classification:
  subject(s) -> class assignment under supplied taxonomy

Transformation:
  source -> target representation/regime

Audit:
  retrace/evaluate an existing process or verdict against criteria

Provenance/Lineage:
  source/successor history and identity-chain claims
```

Comparison may consume Analysis or Transformation outputs but does not absorb their operations.
A dynamic similarity comparison does not itself establish lineage identity.

## 12. Three-ledger draft / 3중 장부 초안

```text
TERMINAL_COMPARISON_STATUS:
  COMPARISON_RESOLVED
  COMPARISON_UNDERDETERMINED
  COMPARISON_BLOCKED

COMPARISON_PROTOCOL_CONFORMANCE:
  CONFORMANT
  NONCONFORMANT
  UNDETERMINED

COMPARISON_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

Correctness/closure, protocol conformance, and comparative method gain remain separate.

## 13. Draft operation sequence / 실행순서 초안

```text
C1  LOCK SUBJECTS, CLAIM, TARGET RESOLUTION, AND COMPARISON SCOPE
C2  LOCK MAP/CORRESPONDENCE FAMILY, SOURCE, DIRECTION, AND COVERAGE
C3  LOCK FEATURE/COORDINATE, RELATION, PROPERTY, STATUS, AND EQUIVALENCE RULES
C4  LOCK BRIDGE/ENCODING RULES AND OPTIONAL AGGREGATE READOUTS
C5  CHECK REQUIRED SUBJECT IDENTITY/STAGE/STATUS RECORDS
C6  EVALUATE COVERED MAPS/CORRESPONDENCES
C7  RECORD PRESERVED, DIVERGED, UNTESTED, AND ENCODED ELEMENTS
C8  EVALUATE STRICT-EQUIVALENCE CLAIM IF REQUESTED
C9  EVALUATE FIRST-BRANCH CLAIM ONLY UNDER SUFFICIENT EARLIER-STAGE COVERAGE
C10 RECORD AGGREGATE COLLISIONS WITHOUT STRUCTURAL UPGRADE
C11 ASSIGN REQUESTED OUTPUT LEVEL
C12 ASSIGN TERMINAL STATUS
C13 RECORD PROTOCOL CONFORMANCE
C14 RECORD METHOD GAIN ONLY AGAINST A FROZEN COMPETENT BASELINE
C15 RECORD LIMITS, HANDOFFS, AND REPRODUCIBILITY DATA
```

## 14. Planning evidence rule / 기획 증거 규칙

This draft is not executable Comparison evidence.
Boundary attacks may require non-breaking amendment before the first protocol is frozen.
No planning PASS/FAIL is to be interpreted as method survival, merger, absorption, or deletion.
