# DSD Comparison Direct Evidence / DSD 비교론 직접 증거

Status: **planning Step 2 complete / no executable Comparison protocol yet**

This lane records evidence that directly tests **DSD Comparison / DSD 비교론**.

## Current development state

```text
DEDICATED_COMPARISON_PROTOCOL: not established
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
BOUNDARY_PRESERVED_NO_REFINEMENT: 11
BOUNDARY_PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
DIRECT_COMPARISON_PILOTS: 0
POSITIVE_COMPARISON_CASES: 0
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 0
BOUNDARY_COMPARISON_CASES: 0
NO_GAIN_COMPARISON_CASES: 0
BASELINE_COMPARISON_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_COMPARISON_APPLICATIONS: 0
INDEPENDENT_COMPARISON_VALIDATION: not established
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_pending
```

## Planning artifacts

```text
methods/06_comparison/TASK_INTERFACE_v0.1-draft.md
methods/06_comparison/BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md
methods/06_comparison/TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
methods/06_comparison/PLANNING.md
methods/06_comparison/WORKLOG.md
```

These are infrastructure and planning records, not direct Comparison validation.

## Step-2 boundary result

```text
BOUNDARY_ATTACKS_RUN: 16
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
DIRECT_COMPARISON_PILOT_INCREMENT: 0
```

The five attacks requiring explicit refinement were:

```text
CMP-BND-DRAFT-003  embedding vs strict equivalence
CMP-BND-DRAFT-005  partial element coverage vs global equivalence
CMP-BND-DRAFT-009  hidden precomparison Transformation
CMP-BND-DRAFT-012  dynamic similarity vs lineage identity
CMP-BND-DRAFT-014  forward map vs reverse/symmetric claim
```

Forced non-breaking refinement groups:

```text
R1 MAP_PROPERTY_REQUIREMENT_PROFILE
   REVERSE_DIRECTION_OR_INVERSE_POLICY

R2 COMPARISON_ELEMENT_COVERAGE
   CLOSURE_REQUIREMENT_BY_OUTPUT_LEVEL

R3 PRECOMPARISON_TRANSFORMATION_POLICY
   REPRESENTATION_PROVENANCE

R4 LINEAGE_IDENTITY_CLAIM_POLICY
   LINEAGE_EVIDENCE_SOURCE_OR_HANDOFF
```

## Current evidence guards

```text
AGGREGATE_EQUALITY != STRUCTURAL_EQUIVALENCE
ONE_MAP_FAILURE != GLOBAL_NONCORRESPONDENCE
COMMON_LABEL != COMMON_COORDINATE_OR_SEMANTIC_ROLE
EMBEDDING != STRICT_EQUIVALENCE
FIRST_OBSERVED_DIFFERENCE != FIRST_JUSTIFIED_BRANCH_POINT
PARTIAL_CORRESPONDENCE != GLOBAL_EQUIVALENCE
ENCODING_REQUIRED_CORRESPONDENCE != DIRECT_CORRESPONDENCE
FORWARD_MAP_SUCCESS != REVERSE_MAP_SUCCESS
MAP_FAMILY_COVERAGE != COMPARISON_ELEMENT_COVERAGE
UNSUPPLIED_NORMALIZATION_OR_CONVERSION != COMPARISON_MAP
DYNAMIC_TRAJECTORY_SIMILARITY != SHARED_LINEAGE_OR_IDENTITY
MISSING_COMPARISON_BRIDGE != PROVEN_STRUCTURAL_DIFFERENCE
```

## Planned evidence IDs

```text
CMP-CH-###   constructed Comparison challenges
CMP-APP-###  external or independently generated Comparison applications
CMP-AUD-###  Comparison-specific audit/maturity records
CMP-IEP-###  independent-evaluator infrastructure
```

Pre-protocol boundary planning uses `CMP-BND-DRAFT-###` and must not be retroactively counted as direct evidence.

## Inheritance and method-survival rule

Analysis, Audit, Design, Synthesis, Static Aggregation, Transformation, Classification, Provenance, or Lineage evidence may inform boundary design but does not automatically validate Comparison.

```text
CASE_PASS != METHOD_SURVIVAL_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
```

## Immediate next task

Integrate the historical `TASK_INTERFACE_v0.1-draft.md` plus `TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md` into the first executable `Comparison Protocol v0.1`. Protocol creation itself will add no direct pilot.
