# TRN-CH-002 — Negative / Loss / Blockage Transformation Challenge Result

Status: **EXECUTED — 56/56 PASS**  
Date: **2026-09-16**  
Case ID: `TRN-CH-002`  
Case class: `negative_loss_blockage_constructed_transformation`  
Case origin: `constructed_internal`  
Evidence scope class: `method_specific`  
Protocol: **Transformation Protocol v0.1**  
Protocol blob: `f78393c188c513acb30a10f1b180d598138cea61`  
Precommit commit: `f1b0f82639b15d083c24e3f406095aab0ab4ef91`  
Precommit blob: `f0bd6fe3b0686fe5650be1d911aed14e412f4d06`

## 1. Execution discipline

Execution used only the frozen four-subcase fixture and Transformation Protocol v0.1. No external material, hidden normalization, default timezone, default map version, undeclared domain extension, or post-hoc criterion weakening was introduced.

## 2. L1 — declared many-to-one loss

Applying `MAP_LOSS 1.0` to `SRC-L1` produced:

```text
TARGET_L1:
  total: 7
  retry_count: 0
  quality_flag: 0
```

Carrier ledger:

```text
{x,y}:
  source: {2,5}
  target: total=7
  relation: MANY_TO_ONE_MERGE
  preservation: MERGED_IN_TARGET
  ordered-pair reconstruction from total alone: unavailable
  injectivity: rejected at declared x/y scope

note:
  source: "alpha"
  relation: OMITTED
  preservation: OMITTED_BY_TRANSFORMATION
  source_missing: no

retry_count:
  source: 0 / DEFINED_ZERO
  target: 0
  relation: ONE_TO_ONE
  preservation: PRESERVED_EXACT
  status: DEFINED_ZERO preserved

quality_flag:
  source counterpart: none
  target: 0
  relation: TARGET_ADDED
  preservation: TARGET_ADDED_NOT_SOURCE_DERIVED
  provenance: DEFAULT_VALUE
```

Information-loss ledger:

```text
merge_loss: x and y cannot be uniquely reconstructed from total=7
omission_loss: note is absent from target by declared transformation rule
```

The target default zero was not confused with the source-derived `retry_count=0`.

```text
REVERSIBILITY_STATUS: NONINVERTIBLE_DUE_TO_COLLISION_OR_LOSS
TERMINAL_TRANSFORMATION_STATUS: TRANSFORMATION_COMPLETED_WITH_DECLARED_LOSS
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

This is a successful execution of a lossy map, not a preserving transformation.

## 3. L2 — blocked by missing required bridge

Frozen input:

```text
local_time = "2026-09-16 03:00"
timezone_id = MISSING
```

`MAP_TIME 1.0` requires an explicit timezone bridge and forbids a default timezone. Therefore no UTC value was emitted.

```text
REQUIRED_BRIDGE: timezone
BRIDGE_STATE: missing
UTC_TARGET_VALUE: not emitted
DEFAULT_UTC_OFFSET: not introduced
MANUAL_ENRICHMENT: not introduced
TERMINAL_TRANSFORMATION_STATUS: TRANSFORMATION_BLOCKED
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

The blocked result is attributable to missing required task information, not to a negative timezone value and not to a protocol defect.

```text
MISSING_TIMEZONE_BRIDGE != UTC_OFFSET_ZERO
MISSING_BRIDGE != NEGATIVE_TIMEZONE_VALUE
BLOCKED != UNDERDETERMINED
```

## 4. L3 — partial batch applicability

Declared domain requires two uppercase ASCII letters followed by two decimal digits.

```text
R1.code = "AB12"
  domain_status: inside
  execution: transformed under MAP_CODE 1.0

R2.code = "ab12"
  domain_status: outside declared domain
  execution: not transformed
  case_folding: not performed
  normalization: not performed
```

`R2` was not recorded as `OMITTED_BY_TRANSFORMATION`; it was outside the map's declared domain before map application.

```text
TERMINAL_TRANSFORMATION_STATUS: TRANSFORMATION_PARTIAL
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

Partial batch success was not generalized to total applicability.

## 5. L4 — underdetermined map-version identity

Frozen task state supplied the map family but no selected claim-relevant version:

```text
MAP_FAMILY: MAP_NORM
ALLOWED_VERSIONS: {1.0,2.0}
SELECTED_MAP_VERSION: unresolved
SOURCE_IDENTIFIER: "007"
```

Because version 1.0 preserves leading zeros and version 2.0 removes them, target output is version-dependent. No precedence/default/latest-version rule was supplied.

Execution therefore emitted no unique target identifier and did not select a map version post hoc.

```text
SELECTED_MAP_VERSION: unresolved
UNIQUE_TARGET_IDENTIFIER: unavailable
HIDDEN_NORMALIZATION: none
TERMINAL_TRANSFORMATION_STATUS: TRANSFORMATION_UNDERDETERMINED
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

```text
UNRESOLVED_MAP_VERSION != LICENSE_TO_SELECT_LATEST
UNRESOLVED_MAP_VERSION != HIDDEN_NORMALIZATION
```

## 6. Terminal-state discrimination

The four subcases remained distinct:

```text
L1 -> TRANSFORMATION_COMPLETED_WITH_DECLARED_LOSS
L2 -> TRANSFORMATION_BLOCKED
L3 -> TRANSFORMATION_PARTIAL
L4 -> TRANSFORMATION_UNDERDETERMINED
```

None was collapsed into generic failure.

Required guards were preserved:

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

## 7. Precommitted scoring

### A. Freeze / anti-post-hoc discipline

```text
10/10 PASS
```

### B. L1 declared-loss execution

```text
18/18 PASS
```

### C. L2 blockage execution

```text
10/10 PASS
```

### D. L3 partial applicability

```text
9/9 PASS
```

### E. L4 underdetermination and scope

```text
9/9 PASS
```

Overall:

```text
PRECOMMITTED_REQUIRED_CHECKS: 56
PASSED: 56
FAILED: 0
TOTAL: 56/56 PASS
```

No scoring rule was added, removed, or weakened after execution.

## 8. Protocol and scope result

```text
TRANSFORMATION_METHOD_GAIN_STATUS: NOT_ASSESSED
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
EXTERNAL_APPLICATION: no
INDEPENDENT_VALIDATION: not established
```

The missing bridge and unresolved map version are supplied-task limitations handled by existing Protocol-v0.1 terminal semantics. They do not expose a contradiction requiring protocol reopening.

## 9. Evidence accounting

This case increments only the direct negative/failure-state lane:

```text
DIRECT_TRANSFORMATION_PILOTS_ATTEMPTED: 2
SUCCESSFUL_DIRECT_TRANSFORMATION_PILOTS: 2
SUCCESSFUL_POSITIVE_TRANSFORMATION_CASES: 1
NEGATIVE_OR_FAILURE_TRANSFORMATION_CASES: 1
```

Unchanged:

```text
METHOD_BOUNDARY_TRANSFORMATION_CASES: 0
BASELINE_TRANSFORMATION_CASES: 0
NO_GAIN_TRANSFORMATION_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_TRANSFORMATION_APPLICATIONS: 0
INDEPENDENT_TRANSFORMATION_VALIDATION: not established
```

## 10. Bounded conclusion

`TRN-CH-002` establishes only that one constructed internal fixture can be processed by Protocol v0.1 while preserving declared-loss, blocked, partial, and underdetermined terminals and their distinct causes.

It does not establish external applicability, practical superiority, independent replication, universal invertibility semantics, or permanent method-registry survival.

## 11. Next

Precommit and execute a direct Transformation method-boundary challenge against neighboring methods such as Design, Synthesis, Aggregation, Compression, Comparison, Interpretation, and Computation. The test must ask whether shared maps, target records, summaries, or computed values imply exact method collapse. External validation remains deferred.
