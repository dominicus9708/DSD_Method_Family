# TRN-CH-001 — Positive Constructed Transformation Challenge Result

Status: **EXECUTED — 48/48 PASS**  
Date: **2026-09-16**  
Case ID: `TRN-CH-001`  
Case class: `positive_constructed_transformation`  
Case origin: `constructed_internal`  
Evidence scope class: `method_specific`  
Protocol: **Transformation Protocol v0.1**  
Protocol blob: `f78393c188c513acb30a10f1b180d598138cea61`  
Precommit commit: `74eeb35287bd90b1306d746835d22996d4e07c2f`  
Precommit blob: `e45b6695406df35e1afbd7b861de40b0772f76f8`

## 1. Execution rule

Execution used only the frozen `SRC-001`, `S_POS 1.0`, `T_POS 1.0`, `MAP_POS 1.0`, declared equivalence/reconstruction rules, and frozen target-default policy.

No external source, hidden enrichment, neighboring-method operation, post-hoc map substitution, or criterion weakening was introduced.

## 2. Generated target record

Applying `MAP_POS 1.0` produced:

```text
TARGET_RECORD:
  record_id: R-017
  temperature_k: 298.15
  offset_x: 3
  offset_y: -2
  retry_count: 0
  schema_marker: T_POS_V1
```

The generated target exactly matches the frozen expected target record.

## 3. Carrier relation and preservation ledger

```text
record_id:
  source: R-017
  target: R-017
  relation: ONE_TO_ONE
  preservation: PRESERVED_EXACT

 temperature_c:
  source: 25.00 C
  target: 298.15 K
  relation: ONE_TO_ONE
  preservation: PRESERVED_UNDER_DECLARED_EQUIVALENCE
  inverse_check: 298.15 - 273.15 = 25.00

 offset_pair:
  source: (3, -2)
  target: {offset_x: 3, offset_y: -2}
  relation: ONE_TO_MANY_SPLIT
  preservation: SPLIT_IN_TARGET
  reconstruction_check: (offset_x, offset_y) = (3, -2)

 retry_count:
  source: 0
  target: 0
  relation: ONE_TO_ONE
  preservation: PRESERVED_EXACT
  source_status: DEFINED_ZERO
  target_status_interpretation: preserved defined zero; not missing

 schema_marker:
  source counterpart: none
  target: T_POS_V1
  relation: TARGET_ADDED
  preservation: TARGET_ADDED_NOT_SOURCE_DERIVED
  provenance: DEFAULT_VALUE
```

The target-only `schema_marker` was not counted as preserved source information.

## 4. Information-loss, collision, and reconstruction record

```text
MANY_TO_ONE_COLLISIONS: 0
CLAIM_RELEVANT_SOURCE_OMISSIONS: 0
CLAIM_RELEVANT_INFORMATION_LOSS: none detected at declared scope
```

Source reconstruction from the target record succeeds at the frozen scope:

```text
record_id      <- R-017
temperature_c  <- 298.15 - 273.15 = 25.00
offset_pair    <- (3, -2)
retry_count    <- 0
```

`schema_marker` is ignored during source reconstruction because the precommit classified it as target-added default data.

Therefore:

```text
INJECTIVITY_STATUS: injective on declared source domain under MAP_POS 1.0
RECONSTRUCTION_AVAILABILITY: available for all claim-relevant source carriers
REVERSIBILITY_STATUS: LEFT_INVERTIBLE_ON_DECLARED_DOMAIN
GLOBAL_BIJECTIVITY_CLAIM: not made
```

The one-to-many split did not create information loss because both ordered components remain available for exact reconstruction.

## 5. Source-status preservation

The zero-valued source carrier remained distinct from absence or missingness:

```text
retry_count = 0
SOURCE_STATUS = DEFINED_ZERO

DEFINED_ZERO != MISSING
DEFINED_ZERO != APPLICABLE_BUT_UNDEFINED
```

No status collapse was required by `T_POS 1.0`.

## 6. Optional-policy execution

```text
TRANSFORMATION_CHAIN: NOT_APPLICABLE / single stage
STOCHASTIC_POLICY: NOT_APPLICABLE / deterministic
TEMPORAL_MIGRATION_SCOPE: NOT_APPLICABLE
NEIGHBORING_METHOD_HANDOFFS: none
EXTERNAL_ENRICHMENT: none
MANUAL_SUPPLY: none
```

No hidden optional operation was used.

## 7. Validity gates

```text
G1  source identity/schema/version frozen                         PASS
G2  target identity/schema/version frozen                         PASS
G3  map identity/version frozen                                   PASS
G4  domain/codomain/applicability explicit                        PASS
G5  claim-relevant carrier set explicit                           PASS
G6  source statuses/types preserved                               PASS
G7  carrier relations explicit                                    PASS
G8  target additions/default provenance explicit                  PASS
G9  loss/collision/injectivity/reconstruction obligations explicit PASS
G10 reversibility claim scope explicit                            PASS
G11 chain semantics explicitly not applicable                     PASS
G12 stochastic semantics explicitly not applicable                PASS
G13 temporal/version migration explicitly not applicable          PASS
G14 output claim does not exceed map/reconstruction support       PASS

VALIDITY_GATES: 14/14 PASS
```

## 8. Precommitted scoring execution

### A. Freeze / identity / applicability

```text
10/10 PASS
```

### B. Transformation execution

```text
18/18 PASS
```

### C. Loss / reconstruction / reversibility

```text
12/12 PASS
```

### D. Scope / gates / conformance

```text
8/8 PASS
```

Overall:

```text
PRECOMMITTED_REQUIRED_CHECKS: 48
PASSED: 48
FAILED: 0
TOTAL: 48/48 PASS
```

No criterion was weakened or added after execution.

## 9. Terminal result

```text
TERMINAL_TRANSFORMATION_STATUS: TRANSFORMATION_COMPLETED_PRESERVING
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
TRANSFORMATION_METHOD_GAIN_STATUS: NOT_ASSESSED
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

The preserving terminal is justified at the declared claim-relevant scope because every source carrier is reconstructible and the target-only addition remains explicitly marked as non-source-derived.

## 10. Evidence accounting

This case increments only the positive direct Transformation evidence lane:

```text
DIRECT_TRANSFORMATION_PILOTS_ATTEMPTED: 1
SUCCESSFUL_DIRECT_TRANSFORMATION_PILOTS: 1
SUCCESSFUL_POSITIVE_TRANSFORMATION_CASES: 1
```

It does not increment:

```text
BASELINE_TRANSFORMATION_CASES: 0
NO_GAIN_TRANSFORMATION_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_TRANSFORMATION_APPLICATIONS: 0
INDEPENDENT_TRANSFORMATION_VALIDATION: not established
```

## 11. Bounded conclusion

`TRN-CH-001` shows that Protocol v0.1 can execute one internally constructed preserving transformation while keeping exact preservation, declared equivalence, split representation, defined zero, target-only default provenance, reconstruction, and scoped reversibility distinct.

It does not establish external applicability, superiority over a competent baseline, independent replication, full target-space bijectivity, or permanent method-registry survival.

## 12. Next

Precommit and execute a negative/loss/blockage Transformation challenge. The next fixture should pressure many-to-one collision, omission, target-default/source-derived confusion, incomplete map applicability, and a non-preserving or blocked terminal without external data.
