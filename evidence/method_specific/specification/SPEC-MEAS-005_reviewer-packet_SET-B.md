# SPEC-MEAS-005 — Reviewer Packet SET-B

Status: AWAITING HUMAN EVALUATOR
Do not consult other `SPEC-MEAS-005` evidence files while completing this packet.
Do not browse the web.
Do not ask another person or model for help.

## Instructions

Complete exactly one form unless the study coordinator explicitly assigns a crossover run.

Start a stopwatch immediately before reading the assigned form.

For each change notice, record:

```text
CHANGE_ID:
IMPACT_IDS: comma-separated sorted IDs
EXTERNAL_STANDARD_REVIEW: yes | no
```

Stop the stopwatch immediately after your final answer is frozen and add:

```text
ELAPSED_TASK_TIME_SECONDS:
INTERRUPTED: yes | no
RESULT_FROZEN: yes
```

An impacted requirement is one whose own content, activation, dependency-sensitive consequence, report/test reference, or validation-authority reference must be reviewed or updated because of the change notice.

Do not include unrelated requirements merely because they are in the same corpus.

---

# FORM_1 — ORBIT

## Carrier

```text
REQUIREMENT_ID: O-R01
SOURCE_REFERENCE: SRC-O:R01
TARGET_ENTITY_OR_CARRIER: core_sensor
REQUIREMENT_TYPE: presence
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: always
REQUIRED_STRUCTURE_OR_VALUE: present
VIOLATION_CONDITION: core_sensor absent
UNRESOLVED_CONDITION: source status unavailable

REQUIREMENT_ID: O-R02
SOURCE_REFERENCE: SRC-O:R02
TARGET_ENTITY_OR_CARRIER: primary_reading
REQUIREMENT_TYPE: value semantics
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: always
REQUIRED_STRUCTURE_OR_VALUE: numeric; zero remains defined_zero
VIOLATION_CONDITION: zero treated as missing or undefined
UNRESOLVED_CONDITION: value semantics unavailable

REQUIREMENT_ID: O-R03
SOURCE_REFERENCE: SRC-O:R03
TARGET_ENTITY_OR_CARRIER: backup_sensor
REQUIREMENT_TYPE: optional presence
REQUIRED_OR_OPTIONAL: optional
ACTIVATION_CONDITION: always
REQUIRED_STRUCTURE_OR_VALUE: absence permitted
VIOLATION_CONDITION: none while optional
UNRESOLVED_CONDITION: optionality unavailable

REQUIREMENT_ID: O-R04
SOURCE_REFERENCE: SRC-O:R04
TARGET_ENTITY_OR_CARRIER: alarm_threshold
REQUIREMENT_TYPE: threshold
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: always
REQUIRED_STRUCTURE_OR_VALUE: 70 units
VIOLATION_CONDITION: active threshold differs from 70
UNRESOLVED_CONDITION: threshold unavailable

REQUIREMENT_ID: O-R05
SOURCE_REFERENCE: SRC-O:R05
TARGET_ENTITY_OR_CARRIER: alarm_state
REQUIREMENT_TYPE: activation rule
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: primary_reading >= O-R04
REQUIRED_STRUCTURE_OR_VALUE: HIGH
VIOLATION_CONDITION: HIGH relation not preserved
UNRESOLVED_CONDITION: O-R04 unresolved
DEPENDENCIES: O-R04

REQUIREMENT_ID: O-R06
SOURCE_REFERENCE: SRC-O:R06
TARGET_ENTITY_OR_CARRIER: reserve_threshold
REQUIREMENT_TYPE: prerequisite
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: always
REQUIRED_STRUCTURE_OR_VALUE: calibration_module before defined reserve_threshold
VIOLATION_CONDITION: reserve_threshold assigned despite unmet prerequisite
UNRESOLVED_CONDITION: calibration_module absent

REQUIREMENT_ID: O-R07
SOURCE_REFERENCE: SRC-O:R07
TARGET_ENTITY_OR_CARRIER: primary_reading_to_reserve_threshold
REQUIREMENT_TYPE: bridge constraint
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: cross-carrier transfer attempted
REQUIRED_STRUCTURE_OR_VALUE: explicit bridge
VIOLATION_CONDITION: transfer without bridge
UNRESOLVED_CONDITION: bridge status unavailable

REQUIREMENT_ID: O-R08
SOURCE_REFERENCE: SRC-O:R08
TARGET_ENTITY_OR_CARRIER: conformance_claim
REQUIREMENT_TYPE: validation authority
REQUIRED_OR_OPTIONAL: conditional
ACTIVATION_CONDITION: conformance claimed
REQUIRED_STRUCTURE_OR_VALUE: validate under External Standard E
VIOLATION_CONDITION: substitute internal consistency
UNRESOLVED_CONDITION: authority unavailable
VALIDATION_STANDARD: External Standard E

REQUIREMENT_ID: O-R09
SOURCE_REFERENCE: SRC-O:R09
TARGET_ENTITY_OR_CARRIER: status_report_threshold
REQUIREMENT_TYPE: reporting
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: always
REQUIRED_STRUCTURE_OR_VALUE: active O-R04 threshold
VIOLATION_CONDITION: report stale threshold
UNRESOLVED_CONDITION: O-R04 unresolved
DEPENDENCIES: O-R04

REQUIREMENT_ID: O-R10
SOURCE_REFERENCE: SRC-O:R10
TARGET_ENTITY_OR_CARRIER: boundary_test_vector
REQUIREMENT_TYPE: test input
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: always
REQUIRED_STRUCTURE_OR_VALUE: active O-R04 threshold
VIOLATION_CONDITION: stale test threshold
UNRESOLVED_CONDITION: O-R04 unresolved
DEPENDENCIES: O-R04

REQUIREMENT_ID: O-R11
SOURCE_REFERENCE: SRC-O:R11
TARGET_ENTITY_OR_CARRIER: reserve_threshold_status
REQUIREMENT_TYPE: unresolved-state rule
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: calibration_module absent
REQUIRED_STRUCTURE_OR_VALUE: reserve_threshold unresolved
VIOLATION_CONDITION: fabricated reserve_threshold value
UNRESOLVED_CONDITION: prerequisite status unavailable
DEPENDENCIES: O-R06

REQUIREMENT_ID: O-R12
SOURCE_REFERENCE: SRC-O:R12
TARGET_ENTITY_OR_CARRIER: backup_sensor_absence
REQUIREMENT_TYPE: optionality consequence
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: O-R03 optional
REQUIRED_STRUCTURE_OR_VALUE: absence is not violation
VIOLATION_CONDITION: absence treated as violation while optional
UNRESOLVED_CONDITION: O-R03 optionality unavailable
DEPENDENCIES: O-R03

REQUIREMENT_ID: O-R13
SOURCE_REFERENCE: SRC-O:R13
TARGET_ENTITY_OR_CARRIER: release_certificate
REQUIREMENT_TYPE: validation reference
REQUIRED_OR_OPTIONAL: conditional
ACTIVATION_CONDITION: conformance claimed
REQUIRED_STRUCTURE_OR_VALUE: cite active validation standard from O-R08
VIOLATION_CONDITION: stale or substituted validation authority
UNRESOLVED_CONDITION: O-R08 unresolved
DEPENDENCIES: O-R08
VALIDATION_STANDARD: External Standard E

REQUIREMENT_ID: O-R14
SOURCE_REFERENCE: SRC-O:R14
TARGET_ENTITY_OR_CARRIER: redundancy_test_profile
REQUIREMENT_TYPE: conditional test activation
REQUIRED_OR_OPTIONAL: conditional
ACTIVATION_CONDITION: O-R03 required
REQUIRED_STRUCTURE_OR_VALUE: redundancy test profile active
VIOLATION_CONDITION: required backup sensor without activated test profile
UNRESOLVED_CONDITION: O-R03 requirement state unresolved
DEPENDENCIES: O-R03
```

## Change notices

### O-CH1
The active alarm threshold in O-R04 changes from 70 units to 75 units.

### O-CH2
O-R06 changes so that the calibration module is required before the reserve threshold is defined only when `MODE=precision`.

### O-CH3
O-R03 changes so that the backup sensor is required when `MODE=redundant`; otherwise it remains optional.

### O-CH4
For any conformance claim, O-R08 changes the required validation authority from External Standard E to External Standard F.

## Answer sheet

```text
O-CH1
IMPACT_IDS:
EXTERNAL_STANDARD_REVIEW:

O-CH2
IMPACT_IDS:
EXTERNAL_STANDARD_REVIEW:

O-CH3
IMPACT_IDS:
EXTERNAL_STANDARD_REVIEW:

O-CH4
IMPACT_IDS:
EXTERNAL_STANDARD_REVIEW:

ELAPSED_TASK_TIME_SECONDS:
INTERRUPTED:
RESULT_FROZEN: yes
```

---

# FORM_2 — HARBOR

## Carrier

```text
H-R01|SRC-H:R01|gateway sensor shall be present.|always||none
H-R02|SRC-H:R02|gateway reading is numeric; zero is a valid defined value.|always||none
H-R03|SRC-H:R03|reserve sensor is optional.|always||none
H-R04|SRC-H:R04|active warning threshold = 45 units.|always||none
H-R05|SRC-H:R05|warning ALERT when gateway reading >= H-R04 threshold.|always|H-R04|none
H-R06|SRC-H:R06|calibration key required before reserve limit is defined.|always||none
H-R07|SRC-H:R07|no gateway-reading -> reserve-limit transfer without explicit bridge.|always||none
H-R08|SRC-H:R08|certification validated under External Standard E.|if certification claimed||External Standard E
H-R09|SRC-H:R09|operations report states active H-R04 threshold.|always|H-R04|none
H-R10|SRC-H:R10|limit test vector uses active H-R04 threshold.|always|H-R04|none
H-R11|SRC-H:R11|if calibration key absent, reserve limit unresolved.|if calibration key absent|H-R06|none
H-R12|SRC-H:R12|reserve-sensor absence is not violation while H-R03 optional.|while H-R03 optional|H-R03|none
H-R13|SRC-H:R13|certification record cites active validation standard from H-R08.|if certification claimed|H-R08|External Standard E
H-R14|SRC-H:R14|reserve test profile activates if H-R03 becomes required.|if H-R03 required|H-R03|none
```

Field order:

```text
REQUIREMENT_ID
|SOURCE_REFERENCE
|REQUIREMENT_TEXT_OR_VALUE
|ACTIVATION_CONDITION
|DEPENDENCIES
|VALIDATION_STANDARD_IF_ACTIVE
```

## Change notices

### H-CH1
The active warning threshold in H-R04 changes from 45 units to 50 units.

### H-CH2
H-R06 changes so that the calibration key is required before the reserve limit is defined only when `MODE=precision`.

### H-CH3
H-R03 changes so that the reserve sensor is required when `MODE=redundant`; otherwise it remains optional.

### H-CH4
For any certification claim, H-R08 changes the required validation authority from External Standard E to External Standard F.

## Answer sheet

```text
H-CH1
IMPACT_IDS:
EXTERNAL_STANDARD_REVIEW:

H-CH2
IMPACT_IDS:
EXTERNAL_STANDARD_REVIEW:

H-CH3
IMPACT_IDS:
EXTERNAL_STANDARD_REVIEW:

H-CH4
IMPACT_IDS:
EXTERNAL_STANDARD_REVIEW:

ELAPSED_TASK_TIME_SECONDS:
INTERRUPTED:
RESULT_FROZEN: yes
```
