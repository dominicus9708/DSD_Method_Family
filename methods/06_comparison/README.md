# 06. DSD Comparison / DSD 비교론

Status: **planning started / Step 1 task interface complete / protocol not yet frozen**

Task: compare two or more supplied structures without reducing comparison to final-output equality, and determine justified correspondence, preserved structure, divergence, strict-equivalence status, and earliest supported branching only within declared comparison/map coverage.

Primary DSD sources: strict equivalence, structure-preserving maps, stage comparison, first branching, Property-stage comparison, Channel-Indexed Static Aggregation as a separate readout source, and optional dynamic lineage comparison when explicitly activated.

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

A resolved comparison may resolve to equivalence, correspondence, or noncorrespondence. `UNDERDETERMINED` is used when partial comparison is possible but the requested closure is unsupported by data/map-family/search coverage. `BLOCKED` is used when a claim-required subject record, criterion, or bridge/map definition is unavailable before substantive comparison.

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

Comparison may consume outputs from neighboring methods but does not absorb their operations. A dynamic similarity comparison does not itself establish lineage identity.

## First-branch discipline

First branching requires sufficient coverage of all earlier claim-relevant stages under the frozen comparison family. Therefore:

```text
FIRST_DIFFERENCE_ENCOUNTERED_BY_ONE_TRAVERSAL
!= FIRST_JUSTIFIED_BRANCH_POINT
```

Failure of one arbitrarily chosen map also does not establish global noncorrespondence.

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
methods/06_comparison/PLANNING.md
methods/06_comparison/WORKLOG.md
evidence/method_specific/comparison/README.md
```

## Current evidence state

```text
DEDICATED_COMPARISON_PROTOCOL: not established
PRE_PROTOCOL_BOUNDARY_ATTACKS: 0
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

Run pre-protocol boundary attacks against aggregate-equality inflation, one-map closure, embedding/equivalence inflation, common-label mismatch, partial/encoded correspondence, first-branch coverage, hidden Transformation/Classification/Audit, dynamic-lineage confusion, directionality, status collapse, and missing-bridge cases. Apply only refinements actually forced by these attacks before freezing an executable `Comparison Protocol v0.1`.

A planning PASS or FAIL does not decide method survival, merger, absorption, or deletion.
