# DSD Specification Practical Benchmark Rule v0.1

Date: 2026-09-08
Status: prospective for future `SPEC-MEAS-*` runs
Applies to: practical comparative evidence for DSD Specification
Does not retroactively rescore: `SPEC-MEAS-001`, `SPEC-MEAS-002`

## 1. Purpose

Prevent future practical benchmarks from forcing a single winner when accuracy, structural handoff, representation burden, and measured workload point in different directions.

`SPEC-MEAS-002` exposed an overlap between `TIE_WITH_DSD_TRACEABILITY_ADVANTAGE` and `TIE_WITH_DSD_OVERHEAD`. This rule fixes that benchmark-design problem prospectively without altering that historical result.

## 2. Required result vector

Every future paired benchmark must report at least:

```text
OUTCOME_ACCURACY_AXIS:
ERROR_OR_FALSE_POSITIVE_AXIS:
SOURCE_FIDELITY_AXIS:
EXTERNAL_STANDARD_BOUNDARY_AXIS:
STRUCTURAL_HANDOFF_AXIS:
REPRESENTATION_BURDEN_AXIS:
MEASURED_WORKLOAD_OR_TIME_AXIS:
REUSE_AXIS:
INDEPENDENCE_AXIS:
```

An inactive or unmeasured axis must be marked `not_measured` or `not_applicable`, not silently treated as equal.

## 3. No automatic scalar winner

Default result is multidimensional.

```text
SCALAR_WINNER_REQUIRED: no
```

A scalar result such as `DSD_PREFERRED` or `BASELINE_PREFERRED` may be used only when the precommit defines a mutually exclusive decision rule before results are known.

## 4. If a scalar winner is requested

The precommit must define either:

1. a lexicographic priority ordering; or
2. explicit non-overlapping predicates.

Recommended default priority when appropriate:

```text
1. hard correctness / source-fidelity failure
2. outcome accuracy / false-positive or false-negative difference
3. actually measured workload or time difference
4. demonstrated repeated-use handoff benefit
5. structural handoff advantage
6. representation burden
```

This ordering is not mandatory for every task; it must still be locked before the run.

## 5. Structural handoff is not practical-time gain

```text
NO_REEXTRACTION_AT_RECEIVING_BOUNDARY
!= MEASURED_TIME_SAVING

REUSABLE_TYPED_CARRIER
!= MEASURED_TOTAL_WORK_REDUCTION
```

Structural handoff differences may be recorded as positive method-family evidence without being promoted to practical superiority.

## 6. Representation burden is not cognitive burden

Byte count, atom count, field count, and document length are burden proxies only.

They must not be presented as direct measurements of:

```text
human review time
human authoring time
cognitive load
error probability
engineering productivity
```

unless those quantities are actually measured.

## 7. Reuse claims

Potential reuse across multiple downstream methods or repeated audits must remain hypothetical unless the benchmark executes repeated downstream use.

For an actual reuse benchmark, record:

```text
NUMBER_OF_DOWNSTREAM_USES:
REBUILD_OR_REEXTRACTION_COUNT_PER_ROUTE:
CARRIER_REUSE_COUNT:
MEASURED_TIME_IF_AVAILABLE:
ERRORS_INTRODUCED_DURING_HANDOFF:
```

## 8. Negative and indeterminate outcomes

All are valid:

```text
DSD_ADVANTAGE_ON_ONE_OR_MORE_AXES
BASELINE_ADVANTAGE_ON_ONE_OR_MORE_AXES
MIXED_RESULT
TIE
NO_GAIN
INDETERMINATE
```

No benchmark must be repaired after reveal merely to produce a favorable scalar result.

## 9. Historical note

```text
SPEC-MEAS-001:
  TIE_WITH_DSD_OVERHEAD
  preserved as originally scored

SPEC-MEAS-002:
  INDETERMINATE
  cause = overlapping precommitted scalar categories
  preserved without rescore
```

## 10. Relationship to DSD Specification v1.0

This is an evidence-evaluation rule, not a change to Specification semantics.

```text
PROTOCOL_V1_0_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```
