# DSD Comparison Direct Evidence / DSD 비교론 직접 증거

Status: **planning opened / no executable Comparison protocol yet**

This lane records evidence that directly tests **DSD Comparison / DSD 비교론**.

## Current development state

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

## Planning artifacts

```text
methods/06_comparison/TASK_INTERFACE_v0.1-draft.md
methods/06_comparison/PLANNING.md
methods/06_comparison/WORKLOG.md
```

These are infrastructure and planning records, not direct Comparison validation.

## Initial evidence guards

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

## Planned evidence IDs

```text
CMP-CH-###   constructed Comparison challenges
CMP-APP-###  external or independently generated Comparison applications
CMP-AUD-###  Comparison-specific audit/maturity records
CMP-IEP-###  independent-evaluator infrastructure
```

Pre-protocol boundary planning should use a clearly draft namespace and must not be retroactively counted as direct evidence.

## Inheritance rule

Analysis, Audit, Design, Synthesis, Static Aggregation, Transformation, Classification, Provenance, or Lineage evidence may inform boundary design but does not automatically validate Comparison.

Case success or failure also does not decide whether Comparison must survive, merge, be absorbed, or be deleted from the method registry.

## Immediate next task

Run pre-protocol boundary attacks against map-family coverage, strict-equivalence inflation, aggregate collision, first-branch claims, hidden neighboring methods, status collapse, directionality, encoding, and missing-bridge cases. Apply only non-breaking refinements that the attacks actually require before freezing `Comparison Protocol v0.1`.
