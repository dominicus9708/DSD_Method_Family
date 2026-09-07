# SPEC-MEAS-004 — Change-Propagation Benchmark

Date: 2026-09-08
Status: COMPLETED
Precommit: `SPEC-MEAS-004_change-propagation_precommit.md`
Precommit commit: `4ca6d4a3c3d1f12c11662ea291a4a056e8fdecb6`
Method under test: DSD Specification v1.0
Benchmark rule: `PRACTICAL_BENCHMARK_RULE_v0.1.md`
Evidence class: paired same-project practical carrier benchmark

## 1. Result in one line

On three prospectively locked requirement changes, the strong conventional traceability carrier and the DSD Specification carrier produced the same exact impact closures, zero missed or false impacts, zero stale affected entries, and zero unrelated reopenings. DSD showed no change-propagation or review-scope advantage on this benchmark and used about 4.223x the frozen UTF-8 representation size.

```text
BENCHMARK_STATUS: COMPLETED
CHANGE_EVENTS: 3
TOTAL_EXPECTED_IMPACT_ENTRY_INSTANCES: 8

BASELINE_CORRECT_IMPACT_ENTRY_INSTANCES: 8/8
DSD_CORRECT_IMPACT_ENTRY_INSTANCES: 8/8

BASELINE_FALSE_IMPACT_ENTRY_INSTANCES: 0
DSD_FALSE_IMPACT_ENTRY_INSTANCES: 0

BASELINE_MISSED_IMPACT_ENTRY_INSTANCES: 0
DSD_MISSED_IMPACT_ENTRY_INSTANCES: 0

BASELINE_STALE_AFFECTED_ENTRIES: 0
DSD_STALE_AFFECTED_ENTRIES: 0

BASELINE_UNAFFECTED_ENTRIES_REOPENED: 0
DSD_UNAFFECTED_ENTRIES_REOPENED: 0

BASELINE_FROZEN_CARRIER_UTF8_BYTES: 1006
DSD_FROZEN_CARRIER_UTF8_BYTES: 4248
DSD_TO_BASELINE_BYTE_RATIO: 4.223

CHANGE_PROPAGATION_ACCURACY: tie
REVIEW_SCOPE_LOCALIZATION: tie
REPRESENTATION_BURDEN_AXIS: baseline_advantage
MEASURED_HUMAN_TIME: not_measured
SCALAR_WINNER: not_assigned
OVERALL_SUMMARY: FUNCTIONAL_TIE_WITH_BASELINE_REPRESENTATION_ADVANTAGE
```

## 2. Frozen conventional carrier

The baseline is intentionally a strong traceability carrier with stable IDs, source references, activation conditions, explicit dependencies, and validation-standard metadata where active.

Canonical field order:

```text
REQUIREMENT_ID|SOURCE_REFERENCE|REQUIREMENT_TEXT_OR_VALUE|ACTIVATION_CONDITION|DEPENDENCIES|VALIDATION_STANDARD_IF_ACTIVE
```

Frozen v1 content used for byte measurement:

```text
CP-R01|SRC-v1:R01|sensor_A shall be present.|always||none
CP-R02|SRC-v1:R02|reading_A numeric; zero is a valid defined value.|always||none
CP-R03|SRC-v1:R03|sensor_B is optional.|always||none
CP-R04|SRC-v1:R04|active alarm threshold = 70 units.|always||none
CP-R05|SRC-v1:R05|alarm HIGH when reading_A >= CP-R04 threshold.|always|CP-R04|none
CP-R06|SRC-v1:R06|calibration_C required before threshold_C is defined.|always||none
CP-R07|SRC-v1:R07|no reading_A -> threshold_C transfer without explicit bridge.|always||none
CP-R08|SRC-v1:R08|conformance validated under External Standard E.|if conformance claimed||External Standard E
CP-R09|SRC-v1:R09|report states active CP-R04 threshold.|always|CP-R04|none
CP-R10|SRC-v1:R10|boundary test vector uses active CP-R04 threshold.|always|CP-R04|none
CP-R11|SRC-v1:R11|if calibration_C absent, threshold_C unresolved.|if calibration_C absent|CP-R06|none
CP-R12|SRC-v1:R12|sensor_B absence is not violation while CP-R03 optional.|while CP-R03 optional|CP-R03|none
```

```text
BASELINE_FROZEN_CARRIER_UTF8_BYTES: 1006
```

## 3. Frozen DSD Specification carrier

The DSD route uses the v1.0 atom structure and only activates conditional fields used by the case.

Frozen v1 content used for byte measurement:

```text
REQUIREMENT_ID: CP-R01
SOURCE_REFERENCE: SRC-v1:R01
TARGET_ENTITY_OR_CARRIER: sensor_A
REQUIREMENT_TYPE: presence
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: always
REQUIRED_STRUCTURE_OR_VALUE: present
VIOLATION_CONDITION: sensor_A absent
UNRESOLVED_CONDITION: source status unavailable

REQUIREMENT_ID: CP-R02
SOURCE_REFERENCE: SRC-v1:R02
TARGET_ENTITY_OR_CARRIER: reading_A
REQUIREMENT_TYPE: value semantics
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: always
REQUIRED_STRUCTURE_OR_VALUE: numeric; zero remains defined_zero
VIOLATION_CONDITION: zero treated as missing/undefined
UNRESOLVED_CONDITION: value semantics unavailable

REQUIREMENT_ID: CP-R03
SOURCE_REFERENCE: SRC-v1:R03
TARGET_ENTITY_OR_CARRIER: sensor_B
REQUIREMENT_TYPE: optional presence
REQUIRED_OR_OPTIONAL: optional
ACTIVATION_CONDITION: always
REQUIRED_STRUCTURE_OR_VALUE: absence permitted
VIOLATION_CONDITION: none while optional
UNRESOLVED_CONDITION: optionality unavailable

REQUIREMENT_ID: CP-R04
SOURCE_REFERENCE: SRC-v1:R04
TARGET_ENTITY_OR_CARRIER: alarm_threshold
REQUIREMENT_TYPE: threshold
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: always
REQUIRED_STRUCTURE_OR_VALUE: 70 units
VIOLATION_CONDITION: active threshold differs from 70
UNRESOLVED_CONDITION: threshold unavailable

REQUIREMENT_ID: CP-R05
SOURCE_REFERENCE: SRC-v1:R05
TARGET_ENTITY_OR_CARRIER: alarm_state
REQUIREMENT_TYPE: activation rule
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: reading_A >= CP-R04
REQUIRED_STRUCTURE_OR_VALUE: HIGH
VIOLATION_CONDITION: HIGH relation not preserved
UNRESOLVED_CONDITION: CP-R04 unresolved
DEPENDENCIES: CP-R04

REQUIREMENT_ID: CP-R06
SOURCE_REFERENCE: SRC-v1:R06
TARGET_ENTITY_OR_CARRIER: threshold_C
REQUIREMENT_TYPE: prerequisite
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: always
REQUIRED_STRUCTURE_OR_VALUE: calibration_C before defined threshold_C
VIOLATION_CONDITION: threshold_C assigned despite unmet prerequisite
UNRESOLVED_CONDITION: calibration_C absent

REQUIREMENT_ID: CP-R07
SOURCE_REFERENCE: SRC-v1:R07
TARGET_ENTITY_OR_CARRIER: reading_A_to_threshold_C
REQUIREMENT_TYPE: bridge constraint
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: cross-carrier transfer attempted
REQUIRED_STRUCTURE_OR_VALUE: explicit bridge
VIOLATION_CONDITION: transfer without bridge
UNRESOLVED_CONDITION: bridge status unavailable

REQUIREMENT_ID: CP-R08
SOURCE_REFERENCE: SRC-v1:R08
TARGET_ENTITY_OR_CARRIER: conformance_claim
REQUIREMENT_TYPE: validation authority
REQUIRED_OR_OPTIONAL: conditional
ACTIVATION_CONDITION: conformance claimed
REQUIRED_STRUCTURE_OR_VALUE: validate under External Standard E
VIOLATION_CONDITION: substitute DSD internal consistency
UNRESOLVED_CONDITION: authority unavailable
VALIDATION_STANDARD: External Standard E

REQUIREMENT_ID: CP-R09
SOURCE_REFERENCE: SRC-v1:R09
TARGET_ENTITY_OR_CARRIER: report_threshold
REQUIREMENT_TYPE: reporting
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: always
REQUIRED_STRUCTURE_OR_VALUE: active CP-R04 threshold
VIOLATION_CONDITION: report stale threshold
UNRESOLVED_CONDITION: CP-R04 unresolved
DEPENDENCIES: CP-R04

REQUIREMENT_ID: CP-R10
SOURCE_REFERENCE: SRC-v1:R10
TARGET_ENTITY_OR_CARRIER: boundary_test_vector
REQUIREMENT_TYPE: test input
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: always
REQUIRED_STRUCTURE_OR_VALUE: active CP-R04 threshold
VIOLATION_CONDITION: stale test threshold
UNRESOLVED_CONDITION: CP-R04 unresolved
DEPENDENCIES: CP-R04

REQUIREMENT_ID: CP-R11
SOURCE_REFERENCE: SRC-v1:R11
TARGET_ENTITY_OR_CARRIER: threshold_C_status
REQUIREMENT_TYPE: unresolved-state rule
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: calibration_C absent
REQUIRED_STRUCTURE_OR_VALUE: threshold_C unresolved
VIOLATION_CONDITION: fabricated threshold_C value
UNRESOLVED_CONDITION: prerequisite status unavailable
DEPENDENCIES: CP-R06

REQUIREMENT_ID: CP-R12
SOURCE_REFERENCE: SRC-v1:R12
TARGET_ENTITY_OR_CARRIER: sensor_B_absence
REQUIREMENT_TYPE: optionality consequence
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: CP-R03 optional
REQUIRED_STRUCTURE_OR_VALUE: absence is not violation
VIOLATION_CONDITION: absence treated as violation while optional
UNRESOLVED_CONDITION: CP-R03 optionality unavailable
DEPENDENCIES: CP-R03
```

```text
DSD_FROZEN_CARRIER_UTF8_BYTES: 4248
DSD_TO_BASELINE_BYTE_RATIO: 4.223
```

The byte ratio is a representation-size measurement only. It is not a human-time or cognitive-load measurement.

## 4. CHANGE-01 — alarm threshold 70 -> 75

Precommitted closure:

```text
CP-R04
CP-R05
CP-R09
CP-R10
```

Both routes traverse the same declared dependency edges from CP-R04.

```text
BASELINE_IDENTIFIED_IMPACT_COUNT: 4
DSD_IDENTIFIED_IMPACT_COUNT: 4
BASELINE_EXPECTED_IMPACT_IDS_MATCHED: 4/4
DSD_EXPECTED_IMPACT_IDS_MATCHED: 4/4
BASELINE_FALSE_IMPACT_IDS: 0
DSD_FALSE_IMPACT_IDS: 0
BASELINE_MISSED_IMPACT_IDS: 0
DSD_MISSED_IMPACT_IDS: 0
BASELINE_STALE_AFFECTED_ENTRIES_AFTER_UPDATE: 0
DSD_STALE_AFFECTED_ENTRIES_AFTER_UPDATE: 0
BASELINE_UNAFFECTED_ENTRIES_REOPENED: 0
DSD_UNAFFECTED_ENTRIES_REOPENED: 0
```

Required updates include the CP-R04 threshold itself and the dependent alarm, reporting, and boundary-test references. Neither route has to reopen unrelated CP-R01/02/03/06/07/08/11/12 entries.

## 5. CHANGE-02 — conditional calibration prerequisite

Precommitted change:

```text
CP-R06:
  calibration_C required before threshold_C is defined only when MODE=precision
```

Precommitted closure:

```text
CP-R06
CP-R11
```

Results:

```text
BASELINE_IDENTIFIED_IMPACT_COUNT: 2
DSD_IDENTIFIED_IMPACT_COUNT: 2
BASELINE_EXPECTED_IMPACT_IDS_MATCHED: 2/2
DSD_EXPECTED_IMPACT_IDS_MATCHED: 2/2
BASELINE_FALSE_IMPACT_IDS: 0
DSD_FALSE_IMPACT_IDS: 0
BASELINE_MISSED_IMPACT_IDS: 0
DSD_MISSED_IMPACT_IDS: 0
BASELINE_STALE_AFFECTED_ENTRIES_AFTER_UPDATE: 0
DSD_STALE_AFFECTED_ENTRIES_AFTER_UPDATE: 0
BASELINE_UNAFFECTED_ENTRIES_REOPENED: 0
DSD_UNAFFECTED_ENTRIES_REOPENED: 0
```

Both carriers already expose activation/dependency information strongly enough to localize this change. DSD's richer prerequisite/unresolved semantics are preserved, but they do not reduce the number of affected entries relative to the strong baseline on this locked case.

## 6. CHANGE-03 — conditional sensor_B requirement

Precommitted change:

```text
CP-R03:
  sensor_B required when MODE=redundant; otherwise optional
```

Precommitted closure:

```text
CP-R03
CP-R12
```

Results:

```text
BASELINE_IDENTIFIED_IMPACT_COUNT: 2
DSD_IDENTIFIED_IMPACT_COUNT: 2
BASELINE_EXPECTED_IMPACT_IDS_MATCHED: 2/2
DSD_EXPECTED_IMPACT_IDS_MATCHED: 2/2
BASELINE_FALSE_IMPACT_IDS: 0
DSD_FALSE_IMPACT_IDS: 0
BASELINE_MISSED_IMPACT_IDS: 0
DSD_MISSED_IMPACT_IDS: 0
BASELINE_STALE_AFFECTED_ENTRIES_AFTER_UPDATE: 0
DSD_STALE_AFFECTED_ENTRIES_AFTER_UPDATE: 0
BASELINE_UNAFFECTED_ENTRIES_REOPENED: 0
DSD_UNAFFECTED_ENTRIES_REOPENED: 0
```

Again, a strong conventional traceability carrier handles the conditional change without rereading or reopening unrelated requirements.

## 7. Aggregate comparison

```text
TOTAL_EXPECTED_IMPACT_ENTRY_INSTANCES: 8

ROUTE_BASELINE:
  correct impact entry instances: 8/8
  false impact entry instances: 0
  missed impact entry instances: 0
  stale affected entries: 0
  unaffected entries reopened: 0
  frozen carrier UTF-8 bytes: 1006

ROUTE_DSD:
  correct impact entry instances: 8/8
  false impact entry instances: 0
  missed impact entry instances: 0
  stale affected entries: 0
  unaffected entries reopened: 0
  frozen carrier UTF-8 bytes: 4248
```

The functional change-propagation result is therefore a tie.

## 8. Required result vector

```text
OUTCOME_ACCURACY_AXIS:
  tie
  baseline = 8/8 exact impact instances
  DSD = 8/8 exact impact instances

ERROR_OR_FALSE_POSITIVE_AXIS:
  tie
  baseline false/missed/stale = 0/0/0
  DSD false/missed/stale = 0/0/0

SOURCE_FIDELITY_AXIS:
  tie
  both preserve the locked source changes without invented values or edges

EXTERNAL_STANDARD_BOUNDARY_AXIS:
  tie
  External Standard E remains conditional authority in both carriers

STRUCTURAL_HANDOFF_AXIS:
  tie_for_this_change_propagation_task
  both frozen carriers contain the stable IDs and dependency edges needed by the update procedure

REPRESENTATION_BURDEN_AXIS:
  baseline_advantage
  baseline = 1006 UTF-8 bytes
  DSD = 4248 UTF-8 bytes
  DSD/baseline = 4.223

MEASURED_WORKLOAD_OR_TIME_AXIS:
  not_measured

REUSE_AXIS:
  tie_on_three_update_events
  the same frozen v1 carrier was reused for all three change notices in both routes

INDEPENDENCE_AXIS:
  same_project_not_independent
```

No scalar winner is assigned.

## 9. Finding

This benchmark weakens a simple claim that DSD Specification automatically improves requirement-change propagation merely because it has typed requirement atoms.

A competent conventional traceability carrier with stable IDs, activation conditions, and explicit dependency links can provide the same exact impact closure and stale-entry avoidance on this case.

The defensible case-level conclusion is:

```text
DSD_TYPED_REQUIREMENT_ATOMS:
  sufficient_for_exact_change_propagation_on_this_case

STRONG_CONVENTIONAL_TRACEABILITY_CARRIER:
  also_sufficient_for_exact_change_propagation_on_this_case

DSD_CHANGE_PROPAGATION_SUPERIORITY:
  not_demonstrated

DSD_REVIEW_SCOPE_SUPERIORITY:
  not_demonstrated
```

The richer DSD record still exposes violation/unresolved/type distinctions that may matter to other receiving tasks, but that possible downstream utility is not counted as a change-propagation advantage here.

## 10. Maturity effect

```text
PRACTICAL_COMPARATIVE_BENCHMARKS_BEFORE: 3
PRACTICAL_COMPARATIVE_BENCHMARKS_AFTER: 4
NEW_MEASUREMENT_AXIS: requirement_change_propagation_and_review_scope

POSITIVE_MEASURED_PRACTICAL_BENEFIT:
  still_not_demonstrated

GENERAL_MEASURED_PRACTICAL_BENEFIT:
  not_established

PROTOCOL_V1_0_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no

METHOD_EVIDENCE_STATUS:
  developing
```

This result is informative even though it is not favorable to DSD: the new measurement axis does not resolve the practical-benefit blocker and should remain visible in the evidence record.

## 11. Limits

This is a constructed same-project benchmark with a deliberately strong baseline.

It does not measure human review time, authoring time, cognitive load, real organizational change cost, or error rates under independent human maintenance.

It does not establish that DSD can never improve change propagation on a more complex task; it establishes only that no such advantage appears in this locked benchmark when the conventional carrier already has competent traceability and dependency structure.
