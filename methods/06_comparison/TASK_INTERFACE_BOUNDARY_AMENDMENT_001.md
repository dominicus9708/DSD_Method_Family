# DSD Comparison Task Interface Boundary Amendment 001 / DSD 비교론 경계 보강 001

Status: **planning amendment / not executable protocol**  
Date: **2026-09-10**  
Applies to: `TASK_INTERFACE_v0.1-draft.md`  
Evidence source: `BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`

## 1. Amendment rule / 보강 원칙

This file preserves the Step-1 task-interface draft as historical lineage and adds only refinements actually forced by the 16 pre-protocol boundary attacks.

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> future COMPARISON_PROTOCOL_v0.1
```

This amendment is planning infrastructure and does not count as direct Comparison validation.

## 2. Forced refinement R1 — map-property and reverse-direction requirements

Add the following task fields:

```text
MAP_PROPERTY_REQUIREMENT_PROFILE
REVERSE_DIRECTION_OR_INVERSE_POLICY
```

`MAP_PROPERTY_REQUIREMENT_PROFILE` records which map properties are required by the claimed output, for example:

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

Multiple requirements may be active.

`REVERSE_DIRECTION_OR_INVERSE_POLICY` records whether a reverse map or inverse property is part of the claim:

```text
not_required
required_and_supplied
required_but_unverified
separate_reverse_search_required
```

Rules:

```text
FORWARD_MAP_SUCCESS
!= REVERSE_MAP_SUCCESS

INJECTIVE_EMBEDDING
!= STRICT_EQUIVALENCE
```

unless the frozen equivalence criterion explicitly supplies sufficient conditions.

## 3. Forced refinement R2 — element coverage and output-level closure

Add:

```text
COMPARISON_ELEMENT_COVERAGE
CLOSURE_REQUIREMENT_BY_OUTPUT_LEVEL
```

`COMPARISON_ELEMENT_COVERAGE` must separately describe coverage of claim-relevant:

```text
coordinates_or_features
relations
properties
status_classes
stages_or_layers
```

Recommended coverage values:

```text
exhaustive
sufficient_by_argument
partial
unknown
not_applicable
```

This is distinct from `MAP_FAMILY_COVERAGE`.

```text
EXHAUSTIVE_MAP_FAMILY_SEARCH
!= EXHAUSTIVE_STRUCTURAL_ELEMENT_COVERAGE
```

`CLOSURE_REQUIREMENT_BY_OUTPUT_LEVEL` locks what must be covered before each requested output can be called resolved.

At minimum:

```text
COMPARISON_PROFILE
  may explicitly retain untested elements.

CORRESPONDENCE_CLASSIFICATION
  requires enough element/map coverage for the claimed relation class.

STRICT_EQUIVALENCE_DECISION
  requires every claim-relevant equivalence condition to be evaluated or a supplied sufficient theorem/criterion.

FIRST_BRANCH_POINT
  requires sufficient earlier-stage coverage plus branch-stage difference evidence.

PARTIAL_COMPARISON
  may close only the declared subset and must retain the unresolved remainder.
```

## 4. Forced refinement R3 — precomparison transformation provenance

Add:

```text
PRECOMPARISON_TRANSFORMATION_POLICY
REPRESENTATION_PROVENANCE
```

Allowed policy values:

```text
none_required
supplied_transformed_representation
external_transformation_handoff_required
transformation_not_permitted_in_comparison
```

`REPRESENTATION_PROVENANCE` records, when relevant:

```text
original_subject_representation
supplied_transformed_representation_id
transformation_source_or_rule
transformation_output_identity
whether_transformation_was_completed_before_Comparison
```

Rules:

```text
UNSUPPLIED_NORMALIZATION_OR_CONVERSION
!= COMPARISON_MAP
```

Comparison may consume a transformation result, but if it must invent or execute the conversion itself, that operation is a Transformation handoff and must not be hidden inside a comparison verdict.

## 5. Forced refinement R4 — lineage/identity claim gate

Add:

```text
LINEAGE_IDENTITY_CLAIM_POLICY
LINEAGE_EVIDENCE_SOURCE_OR_HANDOFF
```

Policy values:

```text
not_claimed
supplied_external_lineage_record
lineage_method_handoff_required
```

Rules:

```text
STATIC_SIMILARITY
!= SHARED_LINEAGE

DYNAMIC_TRAJECTORY_SIMILARITY
!= SHARED_LINEAGE_OR_IDENTITY
```

If lineage identity is claim-relevant, the comparison record must name the supplied lineage evidence or explicitly hand the claim to the Lineage/Provenance method. `DYNAMIC_LINEAGE_SCOPE` alone is not enough to infer historical identity.

## 6. Candidate record additions / 후보 레코드 보강

Extend the candidate map/correspondence record with:

```text
REQUIRED_MAP_PROPERTIES_RESULT
REVERSE_DIRECTION_OR_INVERSE_RESULT
ELEMENT_COVERAGE_RESULT
PRECOMPARISON_TRANSFORMATION_PROVENANCE
LINEAGE_IDENTITY_CLAIM_RESULT
```

These additions do not replace the existing:

```text
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
```

## 7. Draft operation-sequence integration / 실행순서 통합 지침

When the first executable protocol is frozen, integrate the amendment approximately as follows:

```text
C1 lock subjects, claim, target resolution, comparison scope
C2 lock map/correspondence family, direction, coverage
C3 lock required map properties and reverse/inverse policy
C4 lock claim-relevant element coverage and output-level closure requirements
C5 lock feature/relation/property/status/equivalence rules
C6 lock encoding/bridge and precomparison-transformation policy/provenance
C7 lock first-branch search basis/coverage and lineage-claim policy
C8 check required subject records and claim-required bridges
C9 evaluate covered maps/correspondences
C10 evaluate map-property and reverse/inverse requirements
C11 record preserved/diverged/untested/encoded elements and element coverage
C12 evaluate requested correspondence/equivalence closure
C13 evaluate first branch only under sufficient earlier-stage coverage
C14 record aggregate collisions without structural upgrade
C15 record lineage similarity separately from lineage identity
C16 assign requested output level and terminal status
C17 record protocol conformance
C18 record method gain only against frozen competent baseline
C19 record limits, handoffs, and reproducibility data
```

The exact numbering may be refined at protocol freeze, but no amendment field may be silently dropped.

## 8. Amendment effect / 보강 효과

The four refinement groups close the five planning attacks that exposed missing explicit locks:

```text
CMP-BND-DRAFT-003 -> R1
CMP-BND-DRAFT-005 -> R2
CMP-BND-DRAFT-009 -> R3
CMP-BND-DRAFT-012 -> R4
CMP-BND-DRAFT-014 -> R1
```

All other attacks were handled by the Step-1 draft without new fields.

```text
BOUNDARY_ATTACKS_RUN: 16
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
```

No conclusion about permanent method independence follows from these planning results.

## 9. Next / 다음

Freeze the first executable `Comparison Protocol v0.1` by integrating the original Step-1 draft and this amendment while preserving both as historical planning lineage.
