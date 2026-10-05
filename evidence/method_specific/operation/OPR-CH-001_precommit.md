# OPR-CH-001 — Positive Constructed Operation Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-06**  
Challenge ID: `OPR-CH-001`  
Method: **Operation / DSD 운영론**

~~~text
PROTOCOL_COMMIT:
  f732733fd871cbfed930abe44c6970e8ec34fed6
PROTOCOL_BLOB:
  5c6df2773f57ecad85d7ddbc4f06e607b79cc02e
~~~

No protocol rule, fixture, scoring item, or threshold may change after this precommit.

## A — one-shot procedure readiness

~~~text
procedure:
  STEP-A
required readiness:
  R1=yes
required actor:
  operator available
required resource:
  tool available
monitor:
  defined value 1
~~~

Expected:

~~~text
OPERATION_PRIMARY_STATUS:
  OPERATION_ESTABLISHED
OPERATION_TASK_TERMINAL:
  OPERATION_TASK_ESTABLISHED
supported step:
  execute STEP-A
~~~

## B — event-triggered handoff

~~~text
source:
  STEP-A
target:
  STEP-B
trigger:
  source completion
acceptance:
  target readiness=yes
~~~

Expected:

~~~text
HANDOFF_TRIGGER_STATUS:
  triggered
HANDOFF_ACCEPTANCE_STATUS:
  accepted
handoff:
  established
~~~

Trigger and acceptance remain separate records.

## C — repeated cycle

~~~text
cycle:
  inspect -> process -> verify
reset condition:
  verify pass
repeat condition:
  remaining batch > 0
stop condition:
  remaining batch = 0
initial remaining batch:
  2
~~~

Expected two cycles and then stop. The cycle is not relabeled one-shot.

## D — recovery route

~~~text
primary step:
  process
constructed recoverable condition:
  temporary resource fault
retry rule:
  not selected
recovery rule:
  switch to declared backup resource
escalation:
  only if backup unavailable
stop:
  only if escalation rule orders stop
backup:
  available
~~~

Expected recovery, no escalation, no stop.

## E — typed lifecycle transition / lineage

~~~text
pre operational mode:
  A
handoff action:
  activate successor process
post operational mode:
  B
typed transition:
  supplied
lineage:
  supplied
~~~

Expected typed transition and successor identity retained.

## F — reduced dashboard

~~~text
full states:
  u=(ready=1, queue=2)
  v=(ready=1, queue=3)
dashboard readout:
  ready
operational decision scope:
  whether STEP-A may begin
sufficiency rule:
  readiness only is sufficient for this decision
~~~

Expected the dashboard may support this bounded decision while u!=v remains visible.

## G — operation update / non-retroactivity

~~~text
O1:
  decision basis at d0
new monitoring information:
  arrives at d1
O2:
  parent O1
  new information cutoff d1
  supersedes O1 for subsequent decisions
~~~

Expected O1 retained as historical basis; O2 is new version.

## H — neighboring-method handoff discipline

Use supplied handoffs:

~~~text
Control:
  policy supplied
Prediction:
  risk claim supplied
Measurement:
  current observation supplied
Tracking:
  provenance supplied
Audit:
  re-audit trigger rule supplied
~~~

Expected guards:

~~~text
CONTROL_POLICY != OPERATION_EXECUTION
PREDICTION_CLAIM != OPERATION_DECISION
MEASUREMENT_RESULT != OPERATION_ACTION
TRACKING_TRACE != OPERATION_DECISION
AUDIT_VERDICT != OPERATION_ACTION
~~~

Method gain is not tested.

## Frozen scoring

~~~text
A one-shot readiness:
  10
B handoff:
  12
C repeated cycle:
  12
D recovery route:
  12
E typed transition/lineage:
  10
F dashboard scope:
  8
G version update:
  10
H neighboring handoffs:
  10

TOTAL_REQUIRED_CHECKS:
  84
PASS_THRESHOLD:
  84/84
PARTIAL_PASS_ALLOWED:
  no
~~~

On full pass:

~~~text
DIRECT_OPERATION_PILOTS_ATTEMPTED:
  0 -> 1
SUCCESSFUL_DIRECT_OPERATION_PILOTS:
  0 -> 1
POSITIVE_OPERATION_CASES:
  0 -> 1
OPERATION_METHOD_GAIN_STATUS:
  OPERATION_GAIN_NOT_TESTED
PROTOCOL_REVISION_REQUIRED:
  no
SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

Next on full pass: OPR-CH-002 status / terminal coverage.
