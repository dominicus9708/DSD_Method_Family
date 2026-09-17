# TRN-CH-007 Precommit / DSD Transformation Out-of-Scope Terminal Remediation Challenge

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-18**  
Method: **DSD Transformation / DSD 변환론**  
Protocol: **Transformation Protocol v0.1**  
Protocol commit at freeze: `b5e292ff89b1a2529a9f1fde98ad13d9af692e90`  
Protocol blob at freeze: `f78393c188c513acb30a10f1b180d598138cea61`

## 1. Case identity

```text
CASE_ID: TRN-CH-007
CASE_CLASS: out_of_scope_terminal_remediation
CASE_ORIGIN: constructed_same_project
EVIDENCE_SCOPE_CLASS: method_specific
EXTERNAL_APPLICATION: no
BASELINE: none
AUDIT_TRIGGER: TRN-AUD-001 / M2 INSUFFICIENT
```

Purpose: directly exercise the task-level `TRANSFORMATION_OUT_OF_SCOPE` terminal that Protocol v0.1 declares but the pre-audit corpus had not yet executed as an overall task outcome.

This case is not a protocol repair. It tests an existing frozen terminal under a new prospective fixture.

## 2. Frozen distinction target

The challenge must preserve:

```text
TRANSFORMATION_OUT_OF_SCOPE
!= TRANSFORMATION_BLOCKED
!= TRANSFORMATION_PARTIAL
!= OUT_OF_SCOPE_FOR_TRANSFORMATION carrier status inside an otherwise valid task
```

The primary remediation target is O1. O2 and O3 are controls to prevent collapse into neighboring terminals.

## 3. O1 — entire task outside declared transformation domain

Frozen map:

```text
MAP_TEMP_V1
SOURCE_SCHEMA: SENSOR_TEMP_V1
TARGET_SCHEMA: CANONICAL_TEMP_V1
DECLARED_DOMAIN:
  records whose record_type = TEMPERATURE_READING
required source carrier:
  temperature_c
map:
  temperature_c -> temperature_k = temperature_c + 273.15
```

Frozen supplied task:

```text
TASK_ID: O1
SOURCE_RECORD:
  record_type = IMAGE_FRAME
  frame_id = F7
  pixel_hash = H123
REQUESTED_TRANSFORMATION:
  apply MAP_TEMP_V1 to this record as supplied
DOMAIN_EXTENSION_POLICY: prohibited
SCHEMA_COERCION_POLICY: none supplied
NEIGHBORING_BRIDGE: none supplied and none required for an in-domain temperature record
```

Expected execution:

```text
MAP_APPLICABILITY: outside_declared_domain
MAP_APPLICATION_ATTEMPTED: no
TARGET_TEMPERATURE_RECORD_EMITTED: no
HIDDEN_SCHEMA_COERCION: no
HIDDEN_DOMAIN_EXTENSION: no
TERMINAL_TRANSFORMATION_STATUS: TRANSFORMATION_OUT_OF_SCOPE
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

Reason: the requested operation is defined, but the supplied object class is outside the declared transformation domain. This is not blockage by a missing prerequisite within an applicable task.

## 4. O2 — in-domain task blocked by missing required bridge

Control map:

```text
MAP_LOCALTIME_V1
SOURCE_SCHEMA: LOCALTIME_RECORD_V1
TARGET_SCHEMA: UTC_RECORD_V1
DECLARED_DOMAIN:
  LOCALTIME_RECORD_V1
REQUIRED_BRIDGE:
  timezone_id
DEFAULT_TIMEZONE: prohibited
```

Frozen supplied task:

```text
record_type = LOCALTIME_RECORD_V1
local_time = "2026-09-18 00:30"
timezone_id = MISSING
```

Expected execution:

```text
MAP_APPLICABILITY: inside_declared_domain
REQUIRED_BRIDGE_STATE: missing
TARGET_UTC_VALUE: not emitted
TERMINAL_TRANSFORMATION_STATUS: TRANSFORMATION_BLOCKED
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

This prevents `OUT_OF_SCOPE` from becoming a generic label for missing task prerequisites.

## 5. O3 — mixed batch partial applicability

Control map:

```text
MAP_CODE_V1
DECLARED_DOMAIN:
  exactly two uppercase ASCII letters followed by two decimal digits
```

Frozen batch:

```text
R1.code = "AB12" -> inside domain
R2.code = "ab12" -> outside domain
NORMALIZATION_OR_CASEFOLD: prohibited
```

Expected execution:

```text
R1 -> transformed
R2 -> not transformed / outside declared domain
BATCH_TERMINAL_TRANSFORMATION_STATUS: TRANSFORMATION_PARTIAL
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

A mixed task with at least one valid transformed member is not relabeled as whole-task `TRANSFORMATION_OUT_OF_SCOPE`.

## 6. Carrier-level scope control

The challenge also freezes this distinction from prior `TRN-CH-005` R5:

```text
one nonclaim carrier can be OUT_OF_SCOPE_FOR_TRANSFORMATION
while the declared task itself is valid and terminates TRANSFORMATION_COMPLETED_PRESERVING.
```

Therefore:

```text
CARRIER_OUT_OF_SCOPE != TASK_OUT_OF_SCOPE
```

## 7. Frozen scoring

```text
A. immutable / anti-post-hoc discipline     8
B. O1 out-of-scope execution               12
C. O2 blocked control                       6
D. O3 partial control                       6
E. scope / evidence accounting              4
TOTAL                                      36
```

Detailed lock:

```text
A1 protocol commit/blob fixed
A2 O1 source/map/domain fixed
A3 O2 control fixed
A4 O3 control fixed
A5 no domain extension after execution starts
A6 no schema coercion after execution starts
A7 terminal expectations fixed
A8 scoring fixed

B1 O1 map applicability = outside_declared_domain
B2 O1 map not executed
B3 O1 target not emitted
B4 O1 no hidden schema coercion
B5 O1 no hidden domain extension
B6 O1 not classified BLOCKED
B7 O1 not classified PARTIAL
B8 O1 not classified UNDERDETERMINED
B9 O1 terminal exactly TRANSFORMATION_OUT_OF_SCOPE
B10 O1 protocol conformance CONFORMANT
B11 O1 carrier-level scope not substituted for task terminal
B12 O1 reason ledger identifies object/domain mismatch

C1 O2 is inside declared domain
C2 O2 required bridge missing
C3 O2 target not emitted
C4 O2 terminal exactly TRANSFORMATION_BLOCKED
C5 O2 not relabeled OUT_OF_SCOPE
C6 O2 conformance CONFORMANT

D1 O3 R1 transformed
D2 O3 R2 outside domain and not transformed
D3 no casefold/normalization
D4 batch terminal exactly TRANSFORMATION_PARTIAL
D5 O3 not relabeled OUT_OF_SCOPE
D6 O3 conformance CONFORMANT

E1 external application remains 0
E2 no baseline/NO_GAIN/reproducibility increment
E3 protocol revision only if existing terminal semantics contradict fixture
E4 case result does not establish external validity or method survival
```

Decision:

```text
36/36 -> CHALLENGE_VERDICT: PASS
otherwise -> CHALLENGE_VERDICT: FAIL
```

## 8. Evidence-count lock

Before execution:

```text
DIRECT_TRANSFORMATION_PILOTS_ATTEMPTED: 5
SUCCESSFUL_DIRECT_TRANSFORMATION_PILOTS: 5
NEGATIVE_OR_FAILURE_TRANSFORMATION_CASES: 1
REPRODUCIBILITY_CASES: 1
EXTERNAL_TRANSFORMATION_APPLICATIONS: 0
TRANSFORMATION_INTERNAL_STANDARDIZATION_STATUS: developing
```

A 36/36 PASS may add exactly:

```text
DIRECT_TRANSFORMATION_PILOTS_ATTEMPTED: +1
SUCCESSFUL_DIRECT_TRANSFORMATION_PILOTS: +1
NEGATIVE_OR_FAILURE_TRANSFORMATION_CASES: +1
TASK_LEVEL_OUT_OF_SCOPE_TERMINAL_COVERAGE: established_once
```

It does not change baseline, NO_GAIN, reproducibility, external, independent-validation, or internal-standardization status by itself.

## 9. Next if passed

Preserve `TRN-AUD-001` as historical `HOLD_DEVELOPING`, then create a **new audit ID** to reassess the frozen internal-standardization axes including this remedial evidence.