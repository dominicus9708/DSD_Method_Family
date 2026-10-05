# PRED-CH-002 — Prediction Status-Coverage Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-06**  
Challenge ID: `PRED-CH-002`  
Method: **Prediction / DSD 예측론**  
Protocol: **Prediction Protocol v0.1**  
Case origin: `constructed_same_project`

## 1. Frozen protocol

~~~text
PROTOCOL_COMMIT:
  1a03a96e270f0d975710f5d530a8b1dbf5105bb0
PROTOCOL_BLOB:
  54de0673e41fe46f88dd78a56c6150e8d97cfc3c
~~~

No protocol rule may change after this precommit.

## 2. N1 — known target inapplicability

~~~text
target applicability:
  evaluable
  inapplicable on requested scope
~~~

Expected:

~~~text
PREDICTION_PRIMARY_STATUS:
  PREDICTION_NOT_ESTABLISHED
PREDICTION_TASK_TERMINAL:
  PREDICTION_TASK_NOT_ESTABLISHED
~~~

Known inapplicability is not BLOCKED and is not a zero-valued target.

## 3. N2 — missing required domain bridge

~~~text
model output:
  available
target:
  declared
required model-to-target bridge:
  unavailable
~~~

Expected:

~~~text
PREDICTION_PRIMARY_STATUS:
  PREDICTION_BLOCKED
PREDICTION_TASK_TERMINAL:
  PREDICTION_TASK_BLOCKED
~~~

No zero prediction is invented.

## 4. N3 — conflicting applicable domain bridges

~~~text
bridge B1:
  applicable
  model value 4 -> target 8

bridge B2:
  applicable
  model value 4 -> target 12

precedence resolver:
  none
~~~

Expected:

~~~text
PREDICTION_PRIMARY_STATUS:
  PREDICTION_CONFLICTING
PREDICTION_TASK_TERMINAL:
  PREDICTION_TASK_CONFLICTING
~~~

No bridge is chosen arbitrarily.

## 5. N4 — Control request outside Prediction

~~~text
forecast:
  supplied
request:
  choose state-dependent intervention policy
~~~

Expected:

~~~text
CONTROL_HANDOFF:
  required
PREDICTION_PRIMARY_STATUS:
  PREDICTION_OUT_OF_SCOPE
PREDICTION_TASK_TERMINAL:
  PREDICTION_TASK_OUT_OF_SCOPE
~~~

## 6. N5 — unresolved admissible claim semantics

~~~text
same issue-time information:
  frozen

claim semantics C1:
  interval target [4,6]

claim semantics C2:
  point target 5

both:
  admissible under incomplete request metadata

resolver:
  none
~~~

Because the requested claim type itself remains unresolved and changes the required output:

~~~text
PREDICTION_PRIMARY_STATUS:
  PREDICTION_UNDERDETERMINED
PREDICTION_TASK_TERMINAL:
  PREDICTION_TASK_UNDERDETERMINED
~~~

This is semantic underdetermination, not ordinary uncertainty.

## 7. N6 — exact PARTIAL

Two independently required in-scope obligations:

~~~text
Q1:
  point claim supported
  -> PREDICTION_ESTABLISHED

Q2:
  target known inapplicable
  -> PREDICTION_NOT_ESTABLISHED
~~~

No obligation is BLOCKED, CONFLICTING, UNDERDETERMINED, or OUT_OF_SCOPE.

Expected:

~~~text
PREDICTION_TASK_TERMINAL:
  PREDICTION_TASK_PARTIAL
~~~

## 8. N7 — future-data leakage

~~~text
original issue cutoff:
  t0

target observation:
  available only at t1>t0

historical artifact:
  uses t1 observation while claiming issue at t0
~~~

Expected:

~~~text
FUTURE_DATA_LEAKAGE_STATUS:
  FUTURE_DATA_LEAKAGE_FOUND

CLAIM_MODE:
  cannot remain valid PROSPECTIVE_ISSUE under original version

PREDICTION_PRIMARY_STATUS:
  PREDICTION_NOT_ESTABLISHED

PREDICTION_TASK_TERMINAL:
  PREDICTION_TASK_NOT_ESTABLISHED
~~~

The artifact may be separately classified retrospectively, but the original prospective claim is not repaired.

## 9. N8 — horizon outside effective validity

~~~text
requested horizon:
  T=10
model valid:
  through T=8
bridge valid:
  through T=6
all validity scopes:
  known
~~~

Expected:

~~~text
effective validity:
  through T=6

requested T=10 claim:
  evaluably unsupported

PREDICTION_PRIMARY_STATUS:
  PREDICTION_NOT_ESTABLISHED
PREDICTION_TASK_TERMINAL:
  PREDICTION_TASK_NOT_ESTABLISHED
~~~

This is not BLOCKED because the relevant validity scopes are known.

## 10. N9 — validation not yet due

~~~text
issue-time Prediction:
  well formed and supported

target verification time:
  future

target observation:
  not yet due
~~~

Expected:

~~~text
PREDICTION_PRIMARY_STATUS:
  PREDICTION_ESTABLISHED

PREDICTION_TASK_TERMINAL:
  PREDICTION_TASK_ESTABLISHED

POST_OUTCOME_VALIDATION_STATUS:
  PREDICTION_VALIDATION_NOT_YET_DUE
~~~

The later validation axis does not demote the issue-time terminal.

## 11. N10 — terminal precedence with lower-state retention

Four independently required obligations:

~~~text
Q1:
  intervention choice request
  -> OUT_OF_SCOPE

Q2:
  conflicting applicable target bridges
  -> CONFLICTING

Q3:
  unresolved admissible claim semantics
  -> UNDERDETERMINED

Q4:
  required domain bridge unavailable
  -> BLOCKED
~~~

Expected precedence:

~~~text
OUT_OF_SCOPE
>
CONFLICTING
>
UNDERDETERMINED
>
BLOCKED
>
ESTABLISHED / PARTIAL / NOT_ESTABLISHED
~~~

Expected final terminal:

~~~text
PREDICTION_TASK_OUT_OF_SCOPE
~~~

Lower Q2-Q4 statuses must remain visible.

## 12. Frozen scoring — 100 checks

Each N1-N10 receives ten checks.

~~~text
TOTAL_REQUIRED_CHECKS:
  100
PASS_THRESHOLD:
  100/100
PARTIAL_PASS_ALLOWED:
  no
~~~

On full pass:

~~~text
DIRECT_PREDICTION_PILOTS_ATTEMPTED:
  1 -> 2
SUCCESSFUL_DIRECT_PREDICTION_PILOTS:
  1 -> 2
NEGATIVE_OR_UNRESOLVED_PREDICTION_CASES:
  0 -> 1

ALL_SIX_PREDICTION_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  yes

ALL_SEVEN_PREDICTION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes

PREDICTION_METHOD_GAIN_STATUS:
  PREDICTION_GAIN_NOT_TESTED

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 13. Next

On full pass proceed to PRED-CH-003 direct neighboring-method boundary challenge.
