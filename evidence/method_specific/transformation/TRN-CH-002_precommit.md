# TRN-CH-002 — Negative / Loss / Blockage Transformation Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-16**  
Case ID: `TRN-CH-002`  
Case class: `negative_loss_blockage_constructed_transformation`  
Case origin: `constructed_internal`  
Evidence scope class: `method_specific`  
Protocol: **Transformation Protocol v0.1**  
Protocol blob: `f78393c188c513acb30a10f1b180d598138cea61`

## 1. Purpose

Test whether Transformation Protocol v0.1 can preserve materially different non-preserving and non-complete outcomes without collapsing them into one generic failure state.

The fixture pressures four distinct surfaces:

```text
L1 declared many-to-one loss + omission + target-only default
L2 blocked execution caused by a missing required bridge
L3 partial batch applicability with one in-domain and one out-of-domain record
L4 underdetermined execution caused by unresolved map-version identity
```

No external source, standard, benchmark, or evaluator is used.

Required guards:

```text
DECLARED_LOSS != METHOD_FAILURE
MANY_TO_ONE_MERGE != PRESERVATION
OMISSION != MISSING_SOURCE_VALUE
TARGET_DEFAULT != SOURCE_DERIVED_VALUE
PARTIAL_APPLICABILITY != TOTAL_FAILURE
OUTSIDE_DECLARED_DOMAIN != OMITTED_BY_TRANSFORMATION
MISSING_REQUIRED_BRIDGE != NEGATIVE_SOURCE_VALUE
UNRESOLVED_MAP_VERSION != LICENSE_TO_CHOOSE_POST_HOC
BLOCKED != UNDERDETERMINED
PARTIAL != COMPLETED_WITH_DECLARED_LOSS
```

## 2. L1 — declared-loss transformation

### Frozen identity

```text
SOURCE_OBJECT_ID: SRC-L1
SOURCE_SCHEMA: S_LOSS 1.0
TARGET_SCHEMA: T_LOSS 1.0
MAP: MAP_LOSS 1.0
```

### Frozen source

```text
x = 2      / integer / DEFINED_NONZERO
y = 5      / integer / DEFINED_NONZERO
note = "alpha" / string / DEFINED_NONZERO
retry_count = 0 / nonnegative_integer / DEFINED_ZERO
```

### Frozen map

```text
{x,y} -> total = x + y
relation: MANY_TO_ONE_MERGE

note -> OMITTED

retry_count -> retry_count
relation: ONE_TO_ONE

quality_flag -> target-only default 0
relation: TARGET_ADDED
provenance: DEFAULT_VALUE
```

Expected target:

```text
total = 7
retry_count = 0
quality_flag = 0
```

Expected loss state:

```text
{x,y} not uniquely reconstructible from total
note omitted by declared map
retry_count preserved as DEFINED_ZERO
quality_flag not source-derived
```

Expected terminal:

```text
TRANSFORMATION_COMPLETED_WITH_DECLARED_LOSS
CONFORMANT
NONINVERTIBLE_DUE_TO_COLLISION_OR_LOSS
```

## 3. L2 — blocked by missing bridge

### Frozen identity

```text
SOURCE_OBJECT_ID: SRC-L2
SOURCE_SCHEMA: S_TIME 1.0
TARGET_SCHEMA: T_TIME 1.0
MAP: MAP_TIME 1.0
```

Source:

```text
local_time = "2026-09-16 03:00"
timezone_id = MISSING
```

Map requirement:

```text
UTC conversion requires an explicit timezone bridge.
No default timezone is permitted.
```

Expected result:

```text
no UTC value emitted
TERMINAL_TRANSFORMATION_STATUS: TRANSFORMATION_BLOCKED
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

Required distinction:

```text
MISSING_TIMEZONE_BRIDGE != UTC_OFFSET_ZERO
MISSING_BRIDGE != NEGATIVE_TIMEZONE_VALUE
```

## 4. L3 — partial batch applicability

### Frozen identity

```text
SOURCE_BATCH_ID: BATCH-L3
SOURCE_SCHEMA: S_CODE 1.0
TARGET_SCHEMA: T_CODE 1.0
MAP: MAP_CODE 1.0
```

Declared map domain:

```text
code must match exactly two uppercase ASCII letters followed by two decimal digits
```

Frozen batch:

```text
R1.code = "AB12"  -> inside declared domain
R2.code = "ab12"  -> outside declared domain
```

No domain extension, normalization, or case folding is permitted.

Expected execution:

```text
R1 transformed under MAP_CODE 1.0
R2 left untransformed and explicitly recorded OUTSIDE_DECLARED_DOMAIN
```

Expected terminal:

```text
TRANSFORMATION_PARTIAL
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

Required distinction:

```text
OUTSIDE_DECLARED_DOMAIN != OMITTED_BY_TRANSFORMATION
PARTIAL_BATCH_SUCCESS != TOTAL_MAP_APPLICABILITY
```

## 5. L4 — underdetermined map-version identity

Frozen source and target identities are supplied, but task input provides:

```text
MAP_FAMILY: MAP_NORM
ALLOWED_VERSIONS: {1.0, 2.0}
SELECTED_MAP_VERSION: unresolved
```

The two versions differ claim-relevantly:

```text
MAP_NORM 1.0 -> preserves leading zeros in identifier text
MAP_NORM 2.0 -> removes leading zeros before target rendering
```

Source:

```text
identifier = "007"
```

No precedence, recency, default-version, or preference rule is supplied.

Expected result:

```text
no unique target record emitted
TERMINAL_TRANSFORMATION_STATUS: TRANSFORMATION_UNDERDETERMINED
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

Required distinction:

```text
UNRESOLVED_MAP_VERSION != LICENSE_TO_SELECT_LATEST
UNRESOLVED_MAP_VERSION != HIDDEN_NORMALIZATION
```

## 6. Frozen validity expectations

```text
L1: G1-G14 satisfied, with declared loss/reconstruction limits explicit
L2: task-data deficiency at required bridge is surfaced as BLOCKED rather than silently repaired
L3: applicability checked per record; no undeclared domain extension
L4: unresolved claim-relevant map identity surfaced as UNDERDETERMINED rather than post-hoc selection
```

No subcase may be made conformant by silently changing the map, source, target, domain, or bridge after execution begins.

## 7. Frozen expected ledger summary

```text
L1:
  MANY_TO_ONE_MERGE: {x,y} -> total
  OMITTED: note
  PRESERVED_EXACT: retry_count / DEFINED_ZERO
  TARGET_ADDED_NOT_SOURCE_DERIVED: quality_flag / DEFAULT_VALUE
  REVERSIBILITY: NONINVERTIBLE_DUE_TO_COLLISION_OR_LOSS

L2:
  REQUIRED_BRIDGE: timezone
  BRIDGE_STATE: missing
  TARGET_VALUE: not emitted

L3:
  R1: transformed
  R2: outside declared domain, not transformed

L4:
  map family known
  map version unresolved
  target unique value: unavailable
```

## 8. Precommitted scoring — 56 checks

### A. Freeze / anti-post-hoc discipline — 10 checks

1. Protocol v0.1 identity remains unchanged.
2. L1 source/target/map identities are frozen.
3. L2 source/target/map identities and missing bridge state are frozen.
4. L3 domain expression and both batch values are frozen.
5. L4 map family and unresolved version state are frozen.
6. No hidden normalization is added to L3.
7. No default timezone is added to L2.
8. No default/latest map-version rule is added to L4.
9. No target default is reclassified as source-derived in L1.
10. No criterion is weakened after execution.

### B. L1 declared-loss execution — 18 checks

11. total = 7.
12. `{x,y} -> total` is MANY_TO_ONE_MERGE.
13. x is not reported individually preserved.
14. y is not reported individually preserved.
15. reconstruction of ordered pair `(x,y)` from total alone is unavailable.
16. injectivity is rejected at the declared x/y scope.
17. note is recorded OMITTED.
18. omission is recorded as transformation behavior, not source missingness.
19. retry_count target value remains 0.
20. retry_count remains DEFINED_ZERO.
21. quality_flag target value equals 0.
22. quality_flag is TARGET_ADDED_NOT_SOURCE_DERIVED.
23. quality_flag provenance is DEFAULT_VALUE.
24. target default 0 is not confused with retry_count source zero.
25. information-loss ledger records merge loss.
26. information-loss ledger records note omission.
27. reversibility is NONINVERTIBLE_DUE_TO_COLLISION_OR_LOSS.
28. terminal status is TRANSFORMATION_COMPLETED_WITH_DECLARED_LOSS and CONFORMANT.

### C. L2 blockage execution — 10 checks

29. timezone_id remains MISSING.
30. missing timezone is not converted to UTC offset 0.
31. no UTC target value is emitted.
32. required timezone bridge is recorded missing.
33. no manual/default enrichment is silently introduced.
34. blockage is attributed to missing required bridge/task information.
35. terminal is TRANSFORMATION_BLOCKED.
36. conformance is CONFORMANT.
37. BLOCKED is not reported UNDERDETERMINED.
38. blockage does not trigger protocol/shared-core revision by itself.

### D. L3 partial applicability — 9 checks

39. R1 `AB12` is recognized inside domain.
40. R1 is transformed using MAP_CODE 1.0 only.
41. R2 `ab12` is recognized outside declared domain.
42. R2 is not case-folded or normalized.
43. R2 is not mislabeled OMITTED_BY_TRANSFORMATION.
44. R2 is explicitly recorded outside declared domain.
45. batch terminal is TRANSFORMATION_PARTIAL.
46. conformance is CONFORMANT.
47. partial success is not generalized to total-map applicability.

### E. L4 underdetermination and scope — 9 checks

48. MAP_NORM family identity is preserved.
49. selected map version remains unresolved.
50. neither v1.0 nor v2.0 is selected post hoc.
51. no unique target identifier is emitted.
52. hidden normalization is not performed.
53. terminal is TRANSFORMATION_UNDERDETERMINED.
54. conformance is CONFORMANT.
55. method gain remains NOT_ASSESSED.
56. no external-validation, baseline, NO_GAIN, reproducibility, protocol-revision, or shared-core-reopen claim is inferred.

```text
PRECOMMITTED_REQUIRED_CHECKS: 56
```

## 9. Evidence-count lock

If the case passes, increment only:

```text
DIRECT_TRANSFORMATION_PILOTS_ATTEMPTED +1
SUCCESSFUL_DIRECT_TRANSFORMATION_PILOTS +1
NEGATIVE_OR_FAILURE_TRANSFORMATION_CASES +1
```

Do not increment baseline, NO_GAIN, reproducibility, external-application, or independent-validation counters.

A PASS demonstrates terminal/status discrimination under one constructed internal fixture only. It does not establish external applicability, superiority, universal transformation semantics, or permanent method-registry survival.
