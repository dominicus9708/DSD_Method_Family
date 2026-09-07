# SPEC-MEAS-004 — Change-Propagation Benchmark Precommit

Date: 2026-09-08
Status: PRECOMMITTED_BEFORE_EXECUTION
Method under test: DSD Specification v1.0
Benchmark rule: `PRACTICAL_BENCHMARK_RULE_v0.1.md`
Benchmark class: paired same-project practical carrier benchmark

## 1. Locked question

When a versioned requirement source changes after a carrier has been frozen, can a strong conventional requirements carrier and a DSD Specification v1.0 carrier identify the exact change-impact closure, update every affected item, avoid stale values and false impact expansion, preserve source/standard boundaries, and avoid reopening unrelated requirements?

This benchmark tests change propagation and review-scope localization. It does not measure human time, cognitive load, productivity, or independent evaluator agreement.

## 2. Anti-strawman baseline lock

The conventional route must use a strong requirements traceability carrier, not a prose-only or intentionally weak baseline.

It receives the same stable requirement IDs and includes:

```text
REQUIREMENT_ID
SOURCE_REFERENCE
REQUIREMENT_TEXT_OR_VALUE
ACTIVATION_CONDITION
DEPENDENCIES
VALIDATION_STANDARD_IF_ACTIVE
```

The DSD route uses the corresponding v1.0 Specification atom/interface fields.

Both routes receive the same dependency relations. DSD is not allowed to claim advantage merely because the conventional baseline was denied explicit traceability.

## 3. Locked source inventory v1

```text
CP-R01  sensor_A shall be present.
CP-R02  reading_A is numeric; zero is a valid defined value.
CP-R03  sensor_B is optional.
CP-R04  active alarm threshold = 70 units.
CP-R05  alarm is HIGH when reading_A >= CP-R04 threshold.
CP-R06  calibration_C is required before threshold_C has a defined value.
CP-R07  reading_A shall not be transferred into threshold_C without an explicit bridge.
CP-R08  conformance, when claimed, is validated under External Standard E.
CP-R09  the report shall state the active alarm-threshold value from CP-R04.
CP-R10  the boundary test vector shall use the active CP-R04 threshold.
CP-R11  if calibration_C is absent, threshold_C remains unresolved.
CP-R12  absence of sensor_B is not a violation while CP-R03 remains optional.
```

Locked dependency graph:

```text
CP-R05 -> CP-R04
CP-R09 -> CP-R04
CP-R10 -> CP-R04
CP-R11 -> CP-R06
CP-R12 -> CP-R03
```

No other dependency edge may be added after execution begins unless recorded as a protocol/source defect; adding an edge to improve a route post hoc is prohibited.

## 4. Locked change events

### CHANGE-01

```text
CP-R04 threshold: 70 -> 75 units
EXPECTED_IMPACT_CLOSURE:
  CP-R04
  CP-R05
  CP-R09
  CP-R10
EXPECTED_COUNT: 4
```

### CHANGE-02

```text
CP-R06 changes from unconditional calibration prerequisite to:
  calibration_C is required before threshold_C has a defined value only when MODE=precision.
EXPECTED_IMPACT_CLOSURE:
  CP-R06
  CP-R11
EXPECTED_COUNT: 2
```

### CHANGE-03

```text
CP-R03 changes from optional sensor_B to:
  sensor_B is required when MODE=redundant; otherwise optional.
EXPECTED_IMPACT_CLOSURE:
  CP-R03
  CP-R12
EXPECTED_COUNT: 2
```

The three expected closures are locked before route execution.

## 5. Locked execution procedure

For each route and each change event:

1. start from the frozen v1 carrier;
2. supply only the explicit change notice plus the frozen carrier;
3. identify direct changed requirement IDs;
4. traverse only declared dependency edges to form the impact closure;
5. update affected carrier entries;
6. do not rewrite unaffected entries merely for stylistic consistency;
7. check for stale pre-change values/conditions;
8. check for false impact additions;
9. check source fidelity and External Standard E preservation.

No full-source reread is required by the benchmark after carrier freeze because the explicit change notice is the new source input.

## 6. Locked measurements

Per change and per route:

```text
EXPECTED_IMPACT_COUNT
IDENTIFIED_IMPACT_COUNT
EXPECTED_IMPACT_IDS_MATCHED
FALSE_IMPACT_IDS
MISSED_IMPACT_IDS
STALE_AFFECTED_ENTRIES_AFTER_UPDATE
UNAFFECTED_ENTRIES_REOPENED
```

Aggregate measurements:

```text
TOTAL_EXPECTED_IMPACT_ENTRY_INSTANCES: 8
TOTAL_CORRECT_IMPACT_ENTRY_INSTANCES
TOTAL_FALSE_IMPACT_ENTRY_INSTANCES
TOTAL_MISSED_IMPACT_ENTRY_INSTANCES
TOTAL_STALE_AFFECTED_ENTRIES
TOTAL_UNAFFECTED_ENTRIES_REOPENED
FROZEN_CARRIER_UTF8_BYTES
```

`FROZEN_CARRIER_UTF8_BYTES` is a representation-burden proxy only.

## 7. Required result vector

Following `PRACTICAL_BENCHMARK_RULE_v0.1`:

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

For this benchmark:

```text
MEASURED_WORKLOAD_OR_TIME_AXIS: not_measured
INDEPENDENCE_AXIS: same_project_not_independent
SCALAR_WINNER_REQUIRED: no
```

## 8. Interpretation lock

A route has a change-propagation accuracy advantage only if it has fewer missed impacted entries, fewer false impacted entries, or fewer stale affected entries after update.

A route has a review-scope localization advantage only if it correctly covers all expected impacted entries while reopening fewer unrelated entries.

A smaller byte count is only a representation-burden advantage; it is not human-time or cognitive-load evidence.

If both routes identify the same exact closures with zero stale entries and zero unrelated reopenings, the change-propagation/review-scope axes are a tie even if one representation is larger.

## 9. Non-claims

This benchmark cannot by itself establish:

```text
GENERAL_ENGINEERING_PRODUCTIVITY_GAIN
HUMAN_TIME_SAVING
COGNITIVE_LOAD_REDUCTION
INDEPENDENT_EVALUATOR_VALIDATION
EXTERNAL_SPECIFICATION_SUPERIORITY
ALL_METHOD_INTEROPERABILITY
```

Negative, tied, or baseline-favorable results must be preserved without post-hoc repair.
