# CTRL-CH-002 — Control Status / Terminal Coverage Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-06**  
Challenge ID: `CTRL-CH-002`

~~~text
PROTOCOL_COMMIT:
  cda84e4298be81993a571f8f1277b3c7530c6057
PROTOCOL_BLOB:
  bb22a9b8ebca8d11fd29ae9eb072021e45130881
~~~

No protocol rule or expected status mapping may change after this precommit.

## N1 — known inadmissible action

~~~text
action:
  a1
admissibility:
  evaluable
  inadmissible
~~~

Expected:

~~~text
CONTROL_NOT_ESTABLISHED
CONTROL_TASK_NOT_ESTABLISHED
~~~

Known inadmissibility is not BLOCKED and is not a zero action.

## N2 — missing required action-effect bridge

~~~text
state:
  available
action:
  admissible
required action-effect interface:
  unavailable
~~~

Expected:

~~~text
CONTROL_BLOCKED
CONTROL_TASK_BLOCKED
~~~

No zero effect is invented.

## N3 — conflicting applicable effect models

~~~text
same state/action:
  fixed
effect model E1:
  x' = 1
effect model E2:
  x' = 3
both applicable
resolver:
  none
~~~

Expected:

~~~text
CONTROL_CONFLICTING
CONTROL_TASK_CONFLICTING
~~~

## N4 — live execution request outside Control

~~~text
policy:
  supplied
request:
  actuate real system, monitor completion, manage handoff
~~~

Expected:

~~~text
OPERATION_HANDOFF:
  required
CONTROL_OUT_OF_SCOPE
CONTROL_TASK_OUT_OF_SCOPE
~~~

## N5 — unresolved policy semantics

~~~text
same state/target:
  frozen
policy semantics P1:
  open-loop sequence
policy semantics P2:
  feedback rule
both admissible under incomplete request metadata
resolver:
  none
~~~

Expected:

~~~text
CONTROL_UNDERDETERMINED
CONTROL_TASK_UNDERDETERMINED
~~~

This is not ordinary effect uncertainty.

## N6 — exact PARTIAL

Two independently required in-scope obligations:

~~~text
Q1:
  supported action
  -> CONTROL_ESTABLISHED

Q2:
  known inadmissible required action
  -> CONTROL_NOT_ESTABLISHED
~~~

No BLOCKED or higher-priority state.

Expected:

~~~text
CONTROL_TASK_PARTIAL
~~~

## N7 — known unsatisfied prerequisite

~~~text
required prerequisite:
  known unsatisfied
action effect:
  otherwise available
~~~

Expected:

~~~text
CONTROL_NOT_ESTABLISHED
CONTROL_TASK_NOT_ESTABLISHED
~~~

Known unsatisfied prerequisite is not an unavailable prerequisite check.

## N8 — unavailable required state observation

~~~text
current-state observation:
  required
status:
  unavailable
~~~

Expected:

~~~text
CONTROL_BLOCKED
CONTROL_TASK_BLOCKED
~~~

No observed zero is substituted.

## N9 — declared target known unreachable on frozen scope

~~~text
target:
  declared
target-reachability interface:
  available
reachability result:
  target unreachable on declared horizon
~~~

Expected:

~~~text
CONTROL_NOT_ESTABLISHED
CONTROL_TASK_NOT_ESTABLISHED
~~~

This is not BLOCKED because reachability is evaluable.

## N10 — terminal precedence / lower-state retention

Independent obligations:

~~~text
Q1 live execution request:
  OUT_OF_SCOPE
Q2 conflicting effect models:
  CONFLICTING
Q3 unresolved policy semantics:
  UNDERDETERMINED
Q4 missing required effect bridge:
  BLOCKED
~~~

Expected final terminal:

~~~text
CONTROL_TASK_OUT_OF_SCOPE
~~~

Lower Q2-Q4 states remain visible.

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
DIRECT_CONTROL_PILOTS_ATTEMPTED:
  1 -> 2
SUCCESSFUL_DIRECT_CONTROL_PILOTS:
  1 -> 2
NEGATIVE_OR_UNRESOLVED_CONTROL_CASES:
  0 -> 1

ALL_SIX_CONTROL_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  yes
ALL_SEVEN_CONTROL_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes

CONTROL_METHOD_GAIN_STATUS:
  CONTROL_GAIN_NOT_TESTED
PROTOCOL_REVISION_REQUIRED:
  no
SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

Next on full pass: CTRL-CH-003 direct neighboring-method boundary challenge.
