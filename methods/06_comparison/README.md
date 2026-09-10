# 06. DSD Comparison / DSD 비교론

Status: **planning Step 2 complete / 16 pre-protocol boundary attacks complete / protocol not yet frozen**

Task: compare two or more supplied structures without reducing comparison to final-output equality, and determine justified correspondence, preserved structure, divergence, strict-equivalence status, and earliest supported branching only within declared comparison/map/element coverage.

Primary DSD sources: strict equivalence, structure-preserving maps, stage comparison, first branching, Property-stage comparison, Channel-Indexed Static Aggregation as a separate readout source, and optional dynamic comparison with lineage claims gated separately.

## Core method form

```text
supplied subjects
+ declared comparison scope/resolution
+ supplied map/correspondence family
+ preservation/equivalence criteria
-> correspondence/divergence profile
```

## Core guards

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
EXHAUSTIVE_MAP_FAMILY_SEARCH != EXHAUSTIVE_STRUCTURAL_ELEMENT_COVERAGE
UNSUPPLIED_NORMALIZATION_OR_CONVERSION != COMPARISON_MAP
DYNAMIC_TRAJECTORY_SIMILARITY != SHARED_LINEAGE_OR_IDENTITY
MISSING_COMPARISON_BRIDGE != PROVEN_STRUCTURAL_DIFFERENCE
```

## Draft output levels

```text
COMPARISON_PROFILE
CORRESPONDENCE_CLASSIFICATION
STRICT_EQUIVALENCE_DECISION
FIRST_BRANCH_POINT
PARTIAL_COMPARISON
```

## Draft relation classes

```text
STRICT_EQUIVALENT
DIRECT_CORRESPONDENCE
PARTIAL_CORRESPONDENCE
ENCODED_CORRESPONDENCE
NONCORRESPONDENCE
UNDETERMINED_CORRESPONDENCE
```

## Draft terminal statuses

```text
COMPARISON_RESOLVED
COMPARISON_UNDERDETERMINED
COMPARISON_BLOCKED
```

A resolved comparison may resolve to equivalence, correspondence, or noncorrespondence. `UNDERDETERMINED` is used when partial comparison is possible but the requested closure is unsupported by data/map-family/element/search coverage. `BLOCKED` is used when a claim-required subject record, criterion, or bridge/map definition is unavailable before substantive comparison.

## Step-2 boundary result

```text
BOUNDARY_ATTACKS_RUN: 16
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
DIRECT_COMPARISON_PILOT_INCREMENT: 0
```

Five attacks required four non-breaking refinement groups:

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

Planning lineage is preserved as:

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> future PROTOCOL_v0.1.md
```

## Method boundaries

```text
Analysis:
  internal decomposition/description
Comparison:
  cross-subject preservation/correspondence/divergence
Classification:
  taxonomy-based class assignment
Transformation:
  source -> target representation/regime
Audit:
  retrace/evaluate an existing process or verdict
Provenance/Lineage:
  historical/source/successor identity chain
```

Comparison may consume outputs from neighboring methods but does not absorb their operations. A transformed representation must have provenance; a dynamic similarity comparison does not itself establish lineage identity.

## First-branch and coverage discipline

First branching requires sufficient coverage of all earlier claim-relevant stages under the frozen comparison family. Map-family coverage and structural-element coverage are separate.

```text
FIRST_DIFFERENCE_ENCOUNTERED_BY_ONE_TRAVERSAL
!= FIRST_JUSTIFIED_BRANCH_POINT

MAP_FAMILY_COVERAGE
!= COMPARISON_ELEMENT_COVERAGE
```

## Aggregate-collision discipline

Equal aggregate/readout output may coexist with structural difference. Without injectivity or another sufficient reconstruction condition:

```text
AGGREGATE_EQUAL
!= STRUCTURE_EQUAL
```

Static Aggregation remains a separate input/readout handoff rather than becoming Comparison's structural-equivalence rule.

## Planning artifacts

```text
methods/06_comparison/TASK_INTERFACE_v0.1-draft.md
methods/06_comparison/BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md
methods/06_comparison/TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
methods/06_comparison/PLANNING.md
methods/06_comparison/WORKLOG.md
evidence/method_specific/comparison/README.md
```

## Current evidence state

```text
DEDICATED_COMPARISON_PROTOCOL: not established
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
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

## Next development step

Integrate the historical Step-1 draft and Boundary Amendment 001 into the first executable `Comparison Protocol v0.1`. Protocol freeze itself will not count as direct Comparison evidence. The first direct evidence event must be separately precommitted after protocol freeze.

Planning PASS/FAIL does not decide method survival, merger, absorption, or deletion.
