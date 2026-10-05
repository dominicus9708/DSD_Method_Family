# OPR-CH-002 — Operation Status / Terminal Coverage Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-06**

~~~text
PROTOCOL_COMMIT:
  f732733fd871cbfed930abe44c6970e8ec34fed6
PROTOCOL_BLOB:
  5c6df2773f57ecad85d7ddbc4f06e607b79cc02e
~~~

No protocol rule or expected status mapping may change after this precommit.

## N1 — known not-ready state

~~~text
required readiness:
  evaluable
  unmet
~~~

Expected:

~~~text
OPERATION_NOT_ESTABLISHED
OPERATION_TASK_NOT_ESTABLISHED
~~~

## N2 — required resource availability interface missing

Expected:

~~~text
OPERATION_BLOCKED
OPERATION_TASK_BLOCKED
~~~

No zero-load substitution is allowed.

## N3 — conflicting required monitoring records

Two applicable monitoring records support incompatible next-step decisions and no resolver exists.

Expected:

~~~text
OPERATION_CONFLICTING
OPERATION_TASK_CONFLICTING
~~~

## N4 — request to create domain authority

Request:

~~~text
invent legal/clinical/organizational authority
then execute procedure
~~~

Expected:

~~~text
OPERATION_OUT_OF_SCOPE
OPERATION_TASK_OUT_OF_SCOPE
~~~

## N5 — unresolved exception semantics

Same fault admits both RETRY and RECOVERY under incomplete rule metadata; no precedence/resolver exists.

Expected:

~~~text
OPERATION_UNDERDETERMINED
OPERATION_TASK_UNDERDETERMINED
~~~

## N6 — exact PARTIAL

Two independent in-scope obligations:

~~~text
Q1:
  ready and supported
  -> OPERATION_ESTABLISHED

Q2:
  known not-ready
  -> OPERATION_NOT_ESTABLISHED
~~~

No BLOCKED or higher-priority state.

Expected:

~~~text
OPERATION_TASK_PARTIAL
~~~

## N7 — unavailable required monitor

Expected:

~~~text
OPERATION_BLOCKED
OPERATION_TASK_BLOCKED
~~~

No observed zero is substituted.

## N8 — handoff triggered but target known not ready

All required readiness checks are available and target readiness is false.

Expected:

~~~text
HANDOFF_TRIGGER_STATUS:
  triggered
HANDOFF_ACCEPTANCE_STATUS:
  not established
OPERATION_NOT_ESTABLISHED
OPERATION_TASK_NOT_ESTABLISHED
~~~

## N9 — required actor known unavailable

Expected:

~~~text
OPERATION_NOT_ESTABLISHED
OPERATION_TASK_NOT_ESTABLISHED
~~~

Known unavailability is not BLOCKED.

## N10 — terminal precedence / lower-state retention

Independent obligations:

~~~text
Q1 authority creation request:
  OUT_OF_SCOPE
Q2 conflicting monitoring:
  CONFLICTING
Q3 unresolved exception semantics:
  UNDERDETERMINED
Q4 required monitor unavailable:
  BLOCKED
~~~

Expected final terminal:

~~~text
OPERATION_TASK_OUT_OF_SCOPE
~~~

Lower states remain visible.

## Frozen score

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
DIRECT_OPERATION_PILOTS_ATTEMPTED:
  1 -> 2
SUCCESSFUL_DIRECT_OPERATION_PILOTS:
  1 -> 2
NEGATIVE_OR_UNRESOLVED_OPERATION_CASES:
  0 -> 1

ALL_SIX_OPERATION_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  yes
ALL_SEVEN_OPERATION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes

OPERATION_METHOD_GAIN_STATUS:
  OPERATION_GAIN_NOT_TESTED
PROTOCOL_REVISION_REQUIRED:
  no
SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

Next on full pass: OPR-CH-003 direct neighboring-method boundary challenge.
