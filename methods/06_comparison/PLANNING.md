# DSD Comparison Planning / DSD 비교론 기획

Status: **planning started / Step 1 complete**  
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

Created `TASK_INTERFACE_v0.1-draft.md` with:

```text
subject identity/stage/status locks
comparison scope and target resolution
map/correspondence family and coverage
coordinate/feature matching
relation/property/status preservation
strict-equivalence criterion
encoding/bridge discipline
first-branch search basis and coverage
aggregate-collision discipline
optional dynamic-lineage scope
three-ledger separation
```

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
2. **Next:** pre-protocol boundary attacks.
3. Apply only non-breaking refinements actually required by boundary attacks.
4. Freeze first executable `Comparison Protocol v0.1`.
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

## Step 2 boundary-attack targets / 다음 경계 공격 대상

At minimum pressure-test:

```text
1. aggregate equality falsely upgraded to strict equivalence
2. one-map failure falsely upgraded to global noncorrespondence
3. one successful embedding falsely upgraded to strict equivalence
4. common labels with nonmatching semantics
5. partial correspondence falsely upgraded to global equivalence
6. encoded correspondence mislabeled as direct correspondence
7. first observed difference mislabeled as first branch
8. non-exhaustive map family used for first-branch or noncorrespondence closure
9. hidden Transformation used to manufacture a comparison map
10. hidden Classification used to replace relation comparison with class labels
11. hidden Audit used to turn comparison into verdict validation
12. dynamic similarity falsely upgraded to lineage/identity
13. aggregate collision with structurally distinct subjects
14. direction-sensitive map falsely treated as symmetric
15. property status collapse during cross-subject comparison
16. missing common bridge treated as proven structural difference
```

## Current evidence state / 현재 증거 상태

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

## Recording rule / 기록 규칙

- Planning artifacts are not direct Comparison evidence.
- Shared-core, Analysis, Audit, Design, Synthesis, or other method evidence does not automatically become Comparison validation.
- Aggregate equality is never silently promoted to structural identity.
- First-branch claims require explicit earlier-stage coverage discipline.
- A single map failure or success does not close an untested map family.
- Case success/failure does not decide method survival, merger, absorption, or deletion.
- Later corrections are prospective under new artifact/version IDs rather than rewriting failed or superseded records.
