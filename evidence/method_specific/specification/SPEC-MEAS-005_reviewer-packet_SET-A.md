# SPEC-MEAS-005 — Reviewer Packet SET-A

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
O-R01|SRC-O:R01|core sensor shall be present.|always||none
O-R02|SRC-O:R02|primary reading is numeric; zero is a valid defined value.|always||none
O-R03|SRC-O:R03|backup sensor is optional.|always||none
O-R04|SRC-O:R04|active alarm threshold = 70 units.|always||none
O-R05|SRC-O:R05|alarm HIGH when primary reading >= O-R04 threshold.|always|O-R04|none
O-R06|SRC-O:R06|calibration module required before reserve threshold is defined.|always||none
O-R07|SRC-O:R07|no primary-reading -> reserve-threshold transfer without explicit bridge.|always||none
O-R08|SRC-O:R08|conformance validated under External Standard E.|if conformance claimed||External Standard E
O-R09|SRC-O:R09|status report states active O-R04 threshold.|always|O-R04|none
O-R10|SRC-O:R10|boundary test vector uses active O-R04 threshold.|always|O-R04|none
O-R11|SRC-O:R11|if calibration module absent, reserve threshold unresolved.|if calibration module absent|O-R06|none
O-R12|SRC-O:R12|backup-sensor absence is not violation while O-R03 optional.|while O-R03 optional|O-R03|none
O-R13|SRC-O:R13|release certificate cites active validation standard from O-R08.|if conformance claimed|O-R08|External Standard E
O-R14|SRC-O:R14|redundancy test profile activates if O-R03 becomes required.|if O-R03 required|O-R03|none
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
REQUIREMENT_ID: H-R01
SOURCE_REFERENCE: SRC-H:R01
TARGET_ENTITY_OR_CARRIER: gateway_sensor
REQUIREMENT_TYPE: presence
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: always
REQUIRED_STRUCTURE_OR_VALUE: present
VIOLATION_CONDITION: gateway_sensor absent
UNRESOLVED_CONDITION: source status unavailable

REQUIREMENT_ID: H-R02
SOURCE_REFERENCE: SRC-H:R02
TARGET_ENTITY_OR_CARRIER: gateway_reading
REQUIREMENT_TYPE: value semantics
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: always
REQUIRED_STRUCTURE_OR_VALUE: numeric; zero remains defined_zero
VIOLATION_CONDITION: zero treated as missing or undefined
UNRESOLVED_CONDITION: value semantics unavailable

REQUIREMENT_ID: H-R03
SOURCE_REFERENCE: SRC-H:R03
TARGET_ENTITY_OR_CARRIER: reserve_sensor
REQUIREMENT_TYPE: optional presence
REQUIRED_OR_OPTIONAL: optional
ACTIVATION_CONDITION: always
REQUIRED_STRUCTURE_OR_VALUE: absence permitted
VIOLATION_CONDITION: none while optional
UNRESOLVED_CONDITION: optionality unavailable

REQUIREMENT_ID: H-R04
SOURCE_REFERENCE: SRC-H:R04
TARGET_ENTITY_OR_CARRIER: warning_threshold
REQUIREMENT_TYPE: threshold
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: always
REQUIRED_STRUCTURE_OR_VALUE: 45 units
VIOLATION_CONDITION: active threshold differs from 45
UNRESOLVED_CONDITION: threshold unavailable

REQUIREMENT_ID: H-R05
SOURCE_REFERENCE: SRC-H:R05
TARGET_ENTITY_OR_CARRIER: warning_state
REQUIREMENT_TYPE: activation rule
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: gateway_reading >= H-R04
REQUIRED_STRUCTURE_OR_VALUE: ALERT
VIOLATION_CONDITION: ALERT relation not preserved
UNRESOLVED_CONDITION: H-R04 unresolved
DEPENDENCIES: H-R04

REQUIREMENT_ID: H-R06
SOURCE_REFERENCE: SRC-H:R06
TARGET_ENTITY_OR_CARRIER: reserve_limit
REQUIREMENT_TYPE: prerequisite
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: always
REQUIRED_STRUCTURE_OR_VALUE: calibration_key before defined reserve_limit
VIOLATION_CONDITION: reserve_limit assigned despite unmet prerequisite
UNRESOLVED_CONDITION: calibration_key absent

REQUIREMENT_ID: H-R07
SOURCE_REFERENCE: SRC-H:R07
TARGET_ENTITY_OR_CARRIER: gateway_reading_to_reserve_limit
REQUIREMENT_TYPE: bridge constraint
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: cross-carrier transfer attempted
REQUIRED_STRUCTURE_OR_VALUE: explicit bridge
VIOLATION_CONDITION: transfer without bridge
UNRESOLVED_CONDITION: bridge status unavailable

REQUIREMENT_ID: H-R08
SOURCE_REFERENCE: SRC-H:R08
TARGET_ENTITY_OR_CARRIER: certification_claim
REQUIREMENT_TYPE: validation authority
REQUIRED_OR_OPTIONAL: conditional
ACTIVATION_CONDITION: certification claimed
REQUIRED_STRUCTURE_OR_VALUE: validate under External Standard E
VIOLATION_CONDITION: substitute internal consistency
UNRESOLVED_CONDITION: authority unavailable
VALIDATION_STANDARD: External Standard E

REQUIREMENT_ID: H-R09
SOURCE_REFERENCE: SRC-H:R09
TARGET_ENTITY_OR_CARRIER: operations_report_threshold
REQUIREMENT_TYPE: reporting
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: always
REQUIRED_STRUCTURE_OR_VALUE: active H-R04 threshold
VIOLATION_CONDITION: report stale threshold
UNRESOLVED_CONDITION: H-R04 unresolved
DEPENDENCIES: H-R04

REQUIREMENT_ID: H-R10
SOURCE_REFERENCE: SRC-H:R10
TARGET_ENTITY_OR_CARRIER: limit_test_vector
REQUIREMENT_TYPE: test input
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: always
REQUIRED_STRUCTURE_OR_VALUE: active H-R04 threshold
VIOLATION_CONDITION: stale test threshold
UNRESOLVED_CONDITION: H-R04 unresolved
DEPENDENCIES: H-R04

REQUIREMENT_ID: H-R11
SOURCE_REFERENCE: SRC-H:R11
TARGET_ENTITY_OR_CARRIER: reserve_limit_status
REQUIREMENT_TYPE: unresolved-state rule
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: calibration_key absent
REQUIRED_STRUCTURE_OR_VALUE: reserve_limit unresolved
VIOLATION_CONDITION: fabricated reserve_limit value
UNRESOLVED_CONDITION: prerequisite status unavailable
DEPENDENCIES: H-R06

REQUIREMENT_ID: H-R12
SOURCE_REFERENCE: SRC-H:R12
TARGET_ENTITY_OR_CARRIER: reserve_sensor_absence
REQUIREMENT_TYPE: optionality consequence
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: H-R03 optional
REQUIRED_STRUCTURE_OR_VALUE: absence is not violation
VIOLATION_CONDITION: absence treated as violation while optional
UNRESOLVED_CONDITION: H-R03 optionality unavailable
DEPENDENCIES: H-R03

REQUIREMENT_ID: H-R13
SOURCE_REFERENCE: SRC-H:R13
TARGET_ENTITY_OR_CARRIER: certification_record
REQUIREMENT_TYPE: validation reference
REQUIRED_OR_OPTIONAL: conditional
ACTIVATION_CONDITION: certification claimed
REQUIRED_STRUCTURE_OR_VALUE: cite active validation standard from H-R08
VIOLATION_CONDITION: stale or substituted validation authority
UNRESOLVED_CONDITION: H-R08 unresolved
DEPENDENCIES: H-R08
VALIDATION_STANDARD: External Standard E

REQUIREMENT_ID: H-R14
SOURCE_REFERENCE: SRC-H:R14
TARGET_ENTITY_OR_CARRIER: reserve_test_profile
REQUIREMENT_TYPE: conditional test activation
REQUIRED_OR_OPTIONAL: conditional
ACTIVATION_CONDITION: H-R03 required
REQUIRED_STRUCTURE_OR_VALUE: reserve test profile active
VIOLATION_CONDITION: required reserve sensor without activated test profile
UNRESOLVED_CONDITION: H-R03 requirement state unresolved
DEPENDENCIES: H-R03
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
