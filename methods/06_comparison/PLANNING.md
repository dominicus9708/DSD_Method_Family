# DSD Comparison Planning / DSD 비교론 기획

Status: **planning Step 2 complete / boundary amendment prepared / protocol not yet frozen**  
Date opened: **2026-09-10**

## Purpose / 목적

Develop DSD Comparison as an independent method under **Field I: Structural Description & Understanding**. Comparison consumes two or more supplied subjects together with an explicit comparison scope, map/correspondence family, and preservation/equivalence criteria, then returns a justified correspondence/divergence profile without collapsing comparison into final-output equality.

## Current source/interface lock / 현재 기준 잠금

```text
Formation Axiom System
Property Axiom System
Channel-Indexed Static Aggregation
Structural Reorganization Dynamics
DSD_INTERFACE_PROFILE.md
METHOD_BOUNDARY_MATRIX.md
```

Initial guards:

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

## Step 1 output / 1단계 산출

Created `TASK_INTERFACE_v0.1-draft.md` with subject identity/stage/status records, comparison domain, map-family source and coverage, feature/relation/property/status preservation, strict-equivalence criteria, encoding/bridge rules, first-branch search basis, aggregate-collision handling, dynamic-lineage guard, output levels, relation classes, terminal statuses, and three-ledger separation.

Draft output levels:

```text
COMPARISON_PROFILE
CORRESPONDENCE_CLASSIFICATION
STRICT_EQUIVALENCE_DECISION
FIRST_BRANCH_POINT
PARTIAL_COMPARISON
```

Draft relation classes:

```text
STRICT_EQUIVALENT
DIRECT_CORRESPONDENCE
PARTIAL_CORRESPONDENCE
ENCODED_CORRESPONDENCE
NONCORRESPONDENCE
UNDETERMINED_CORRESPONDENCE
```

Draft terminal statuses:

```text
COMPARISON_RESOLVED
COMPARISON_UNDERDETERMINED
COMPARISON_BLOCKED
```

## Step 2 — pre-protocol boundary attack / 경계 공격

Created:

```text
methods/06_comparison/BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md
methods/06_comparison/TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
```

Boundary result:

```text
BOUNDARY_ATTACKS_RUN: 16
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
DIRECT_COMPARISON_PILOT_INCREMENT: 0
```

The 16 attacks covered:

```text
1 aggregate equality -> strict equivalence inflation
2 one-map failure -> global noncorrespondence inflation
3 embedding -> strict equivalence inflation
4 common label -> semantic-coordinate inflation
5 partial element coverage -> global equivalence inflation
6 encoded -> direct correspondence inflation
7 first observed difference -> first branch inflation
8 non-exhaustive map family -> false closure
9 hidden Transformation
10 hidden Classification
11 hidden Audit
12 dynamic similarity -> lineage/identity inflation
13 aggregate collision -> support reconstruction inflation
14 direction-sensitive map -> false symmetry
15 Property/status collapse
16 missing bridge -> proven structural difference inflation
```

Four non-breaking refinement groups were actually forced:

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

The Step-1 draft remains historical and is not silently rewritten.

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> future PROTOCOL_v0.1.md
```

## Method boundaries / 방법 경계

```text
Analysis:
  internal decomposition / description

Comparison:
  cross-subject correspondence / preservation / divergence

Classification:
  taxonomy-based class assignment

Transformation:
  source -> target representation/regime

Audit:
  retrace/evaluate an existing result or process

Provenance/Lineage:
  historical/source/successor identity chain
```

Comparison may consume outputs from these methods but does not relabel their operations as Comparison.

## Development sequence / 개발 순서

1. ✅ Comparison-specific task interface draft.
2. ✅ 16 pre-protocol boundary attacks.
3. ✅ Non-breaking Boundary Amendment 001 from the five attacks that exposed missing explicit locks.
4. **Next:** freeze first executable `Comparison Protocol v0.1`.
5. Positive direct challenge.
6. Negative/failure challenge.
7. Direct method-boundary challenge.
8. `NO_GAIN` comparison against a competent baseline.
9. Strongest-reasonable-baseline comparison.
10. First external application.
11. Deterministic retrace/reproducibility record.
12. Additional materially different external domains.
13. Maturity audit after evidence architecture is materially populated.
14. Independent-evaluator infrastructure only after protocol/evidence stability justifies it.

## Step-2 refinements / 2단계 보강

### R1 map-property / directionality

```text
FORWARD_MAP_SUCCESS != REVERSE_MAP_SUCCESS
INJECTIVE_EMBEDDING != STRICT_EQUIVALENCE
```

Explicitly lock map-property requirements and reverse/inverse policy for the requested claim.

### R2 element coverage / closure

```text
MAP_FAMILY_COVERAGE != COMPARISON_ELEMENT_COVERAGE
```

Coordinates/features, relations, Properties, status classes, and stages/layers need their own claim-relevant coverage record. Output levels require explicit closure conditions.

### R3 precomparison transformation provenance

```text
UNSUPPLIED_NORMALIZATION_OR_CONVERSION != COMPARISON_MAP
```

Comparison may consume a supplied transformation output but does not invent/execute the transformation silently.

### R4 lineage identity gate

```text
DYNAMIC_TRAJECTORY_SIMILARITY != SHARED_LINEAGE_OR_IDENTITY
```

Lineage claims require supplied lineage evidence or an explicit handoff.

## Current evidence state / 현재 증거 상태

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

## Recording rule / 기록 규칙

- Planning artifacts are not direct Comparison evidence.
- Shared-core or neighboring-method evidence does not automatically become Comparison validation.
- Aggregate equality is never silently promoted to structural identity.
- First-branch claims require explicit earlier-stage coverage discipline.
- A single map failure or success does not close an untested map family.
- Map-family coverage and structural-element coverage remain separate.
- Precomparison transformations require provenance and remain Transformation operations.
- Dynamic similarity does not establish lineage identity.
- Case success/failure does not decide method survival, merger, absorption, or deletion.
- Later corrections are prospective under new artifact/version IDs rather than rewriting failed or superseded records.
