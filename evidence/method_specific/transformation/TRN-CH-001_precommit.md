# TRN-CH-001 — Positive Constructed Transformation Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-16**  
Case ID: `TRN-CH-001`  
Case class: `positive_constructed_transformation`  
Case origin: `constructed_internal`  
Evidence scope class: `method_specific`  
Audited method: **DSD Transformation / DSD 변환론**  
Protocol: **Transformation Protocol v0.1**  
Protocol blob: `f78393c188c513acb30a10f1b180d598138cea61`

## 1. Purpose

Test whether Protocol v0.1 can execute one fully supplied, deterministic transformation in which claim-relevant source information is preserved through a mixture of exact preservation, declared-equivalence preservation, one-to-many splitting, and one explicit target-only default.

The challenge is positive, but it is not allowed to infer faithfulness merely from target-value existence or endpoint coincidence.

```text
SAME_TARGET_OUTPUT != FAITHFUL_TRANSFORMATION
TARGET_DEFAULT != SOURCE_DERIVED_VALUE
DEFINED_ZERO != MISSING
SPLIT_IN_TARGET != AUTOMATIC_INFORMATION_LOSS
FORWARD_SUCCESS != GLOBAL_BIJECTIVITY
```

No external source, external standard, or independent evaluator is used.

## 2. Frozen task identity

```text
TASK_ID: TRN-CH-001
SOURCE_OBJECT_ID: SRC-001
SOURCE_SCHEMA_ID: S_POS
SOURCE_SCHEMA_VERSION: 1.0
TARGET_SCHEMA_ID: T_POS
TARGET_SCHEMA_VERSION: 1.0
TRANSFORMATION_MAP_ID: MAP_POS
TRANSFORMATION_MAP_VERSION: 1.0
TARGET_RESOLUTION: claim-relevant carrier level
```

## 3. Frozen source record

```text
SRC-001:
  record_id:
    value: R-017
    type: string
    status: DEFINED_NONZERO

  temperature_c:
    value: 25.00
    type: real_temperature_celsius
    status: DEFINED_NONZERO

  offset_pair:
    value: (3, -2)
    type: ordered_pair_integer
    status: DEFINED_NONZERO

  retry_count:
    value: 0
    type: nonnegative_integer
    status: DEFINED_ZERO
```

All four carriers are claim-relevant.

## 4. Frozen target schema

```text
T_POS v1.0 carriers:
  record_id: string
  temperature_k: real_temperature_kelvin
  offset_x: integer
  offset_y: integer
  retry_count: nonnegative_integer
  schema_marker: string
```

`schema_marker` has no source counterpart and is governed only by the frozen target-default policy below.

## 5. Frozen map and carrier rules

```text
M1 record_id -> record_id
   rule: identity
   relation: ONE_TO_ONE

M2 temperature_c -> temperature_k
   rule: temperature_k = temperature_c + 273.15
   relation: ONE_TO_ONE
   declared equivalence E_TEMP:
     values are equivalent iff K = C + 273.15
   declared inverse on mapped values:
     temperature_c = temperature_k - 273.15

M3 offset_pair=(x,y) -> {offset_x=x, offset_y=y}
   relation: ONE_TO_MANY_SPLIT
   declared reconstruction:
     offset_pair = (offset_x, offset_y)

M4 retry_count -> retry_count
   rule: identity
   relation: ONE_TO_ONE
   source status DEFINED_ZERO must remain distinguishable from MISSING

M5 target schema_marker
   source relation: none
   target relation: TARGET_ADDED
   frozen value: T_POS_V1
   provenance: DEFAULT_VALUE
```

## 6. Frozen domain, codomain, applicability

Declared source domain:

```text
record_id: any nonempty string
temperature_c: any finite real number
offset_pair: ordered pair of integers
retry_count: integer >= 0
```

Declared codomain is `T_POS v1.0` with the six carriers listed above.

`SRC-001` is precommitted as inside the declared domain.

No extension outside the declared domain is permitted in this case.

## 7. Frozen loss, injectivity, reconstruction, and inverse policy

Expected information-loss state:

```text
NO_CLAIM_RELEVANT_SOURCE_INFORMATION_LOSS_EXPECTED
```

Expected collision state:

```text
NO_MANY_TO_ONE_COLLISION_EXPECTED
```

Expected reconstruction obligations:

```text
record_id <- exact target record_id
temperature_c <- temperature_k - 273.15
offset_pair <- (offset_x, offset_y)
retry_count <- exact target retry_count
schema_marker is ignored for source reconstruction because it is target-added
```

Expected reversibility classification:

```text
LEFT_INVERTIBLE_ON_DECLARED_DOMAIN
```

The case does **not** precommit global bijectivity on the full target codomain.

## 8. Frozen optional policies

```text
TRANSFORMATION_CHAIN: NOT_APPLICABLE / single-stage map
STOCHASTIC_OR_NONDETERMINISTIC_POLICY: NOT_APPLICABLE / deterministic
TEMPORAL_MIGRATION_SCOPE: NOT_APPLICABLE
NEIGHBORING_METHOD_HANDOFFS: none
EXTERNAL_ENRICHMENT: none
MANUAL_SUPPLY: none
```

## 9. Frozen expected target record

```text
TARGET_RECORD_EXPECTED:
  record_id: R-017
  temperature_k: 298.15
  offset_x: 3
  offset_y: -2
  retry_count: 0
  schema_marker: T_POS_V1
```

## 10. Frozen expected preservation ledger

```text
record_id:
  relation: ONE_TO_ONE
  preservation: PRESERVED_EXACT

temperature_c:
  relation: ONE_TO_ONE
  preservation: PRESERVED_UNDER_DECLARED_EQUIVALENCE

offset_pair:
  relation: ONE_TO_MANY_SPLIT
  preservation: SPLIT_IN_TARGET
  reconstruction: available_exactly_at_declared_scope

retry_count:
  relation: ONE_TO_ONE
  preservation: PRESERVED_EXACT
  source_status_after_transform: DEFINED_ZERO

schema_marker:
  relation: TARGET_ADDED
  preservation: TARGET_ADDED_NOT_SOURCE_DERIVED
  provenance: DEFAULT_VALUE
```

## 11. Frozen expected terminal result

```text
TERMINAL_TRANSFORMATION_STATUS: TRANSFORMATION_COMPLETED_PRESERVING
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
TRANSFORMATION_METHOD_GAIN_STATUS: NOT_ASSESSED
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

`TRANSFORMATION_COMPLETED_PRESERVING` is justified only if all claim-relevant source carriers remain reconstructible at the declared scope and the target-only default remains explicitly non-source-derived.

## 12. Precommitted validity-gate expectations

```text
G1-G10: required and expected PASS
G11: PASS by explicit NOT_APPLICABLE single-stage record
G12: PASS by explicit deterministic record
G13: PASS by explicit NOT_APPLICABLE temporal scope
G14: required and expected PASS
```

No gate may be weakened after execution.

## 13. Precommitted scoring — 48 checks

### A. Freeze / identity / applicability — 10 checks

1. source object identity matches `SRC-001`
2. source schema/version matches `S_POS 1.0`
3. target schema/version matches `T_POS 1.0`
4. map identity/version matches `MAP_POS 1.0`
5. source domain is frozen before execution
6. target codomain is frozen before execution
7. all four source carriers are claim-relevant and frozen
8. source statuses/types are frozen
9. target default policy is frozen
10. optional chain/stochastic/temporal/handoff policies are explicitly frozen

### B. Transformation execution — 18 checks

11. `record_id` target value equals `R-017`
12. `record_id` relation is ONE_TO_ONE
13. `record_id` preservation is PRESERVED_EXACT
14. `temperature_k` equals 298.15
15. temperature relation is ONE_TO_ONE
16. temperature preservation is PRESERVED_UNDER_DECLARED_EQUIVALENCE
17. temperature inverse reconstructs 25.00
18. `offset_x` equals 3
19. `offset_y` equals -2
20. offset relation is ONE_TO_MANY_SPLIT
21. offset preservation is SPLIT_IN_TARGET
22. offset reconstruction returns `(3,-2)` exactly
23. target `retry_count` equals 0
24. retry relation is ONE_TO_ONE
25. retry preservation is PRESERVED_EXACT
26. retry source status remains DEFINED_ZERO rather than MISSING
27. `schema_marker` equals `T_POS_V1`
28. `schema_marker` is TARGET_ADDED_NOT_SOURCE_DERIVED with DEFAULT_VALUE provenance

### C. Loss / reconstruction / reversibility — 12 checks

29. no many-to-one collision is introduced
30. no claim-relevant source carrier is omitted
31. no target default is misreported as source-derived
32. no DEFINED_ZERO/MISSING collapse occurs
33. exact source reconstruction succeeds for record_id
34. declared-equivalence reconstruction succeeds for temperature
35. exact source reconstruction succeeds for offset_pair
36. exact source reconstruction succeeds for retry_count
37. source reconstruction does not depend on schema_marker
38. information-loss ledger records no claim-relevant source loss
39. reversibility is no stronger than LEFT_INVERTIBLE_ON_DECLARED_DOMAIN
40. no global-bijectivity claim is emitted

### D. Scope / gates / conformance — 8 checks

41. all G1-G14 obligations are satisfied or explicitly not-applicable as frozen
42. only MAP_POS v1.0 rules are used
43. no hidden target enrichment occurs
44. no neighboring-method operation is silently performed
45. terminal status is TRANSFORMATION_COMPLETED_PRESERVING
46. protocol conformance is CONFORMANT
47. method gain remains NOT_ASSESSED
48. no protocol/shared-core revision is inferred from a passing positive fixture

```text
PRECOMMITTED_REQUIRED_CHECKS: 48
```

## 14. Evidence-count lock

If the case passes, increment only the applicable positive direct-pilot counters.

Do not increment baseline, NO_GAIN, reproducibility, external-application, or independent-validation counters.

A PASS does not prove external applicability, superiority, global invertibility, or permanent method-registry survival.
