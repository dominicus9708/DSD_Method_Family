# DSD Operation — Boundary Amendment 001

Status: **ESTABLISHED — 8/8 REFINEMENTS ADOPTED / PROTOCOL FREEZE AUTHORIZED**  
Date: **2026-10-06**

~~~text
TASK_INTERFACE_COMMIT:
  830b8ad7e1ea9d9ff98b6ea0119695472fa7842b
TASK_INTERFACE_BLOB:
  e8beafd45dee9715df32ae83445e12ea1b11941b

BOUNDARY_REVIEW_COMMIT:
  c578928b1eab3655551b2ca745db856640b0888e
BOUNDARY_REVIEW_BLOB:
  fc28b83f874af7676765128d144c0e54172fbcd9
~~~

The historical Task Interface is not rewritten.

## R1 — actor/resource status binding

Freeze actor/resource identity, requiredness, availability, provenance, and evaluation status.

~~~text
known unavailable required actor/resource -> OPERATION_NOT_ESTABLISHED
required availability interface unavailable -> OPERATION_BLOCKED
conflicting availability records -> OPERATION_CONFLICTING
unresolved admissible availability semantics -> OPERATION_UNDERDETERMINED
~~~

## R2 — readiness/prerequisite status binding

Freeze readiness criterion identity, prerequisite identity, satisfaction status, and evaluation provenance.

Known unmet required readiness/prerequisite -> NOT_ESTABLISHED.  
Unavailable evaluation -> BLOCKED.  
Conflict -> CONFLICTING.  
Unresolved semantics -> UNDERDETERMINED.

## R3 — monitoring status and definedness

Freeze monitoring interface version, observation status, definedness, and provenance.

~~~text
UNAVAILABLE_MONITOR != OBSERVED_ZERO
UNDEFINED_OBSERVATION != DEFINED_ZERO
~~~

Required monitoring unavailable -> BLOCKED.

## R4 — handoff trigger / acceptance separation

Freeze separately:

~~~text
HANDOFF_TRIGGER_STATUS
HANDOFF_ACCEPTANCE_STATUS
HANDOFF_ACCEPTANCE_EVIDENCE
~~~

~~~text
HANDOFF_TRIGGERED != HANDOFF_ACCEPTED
~~~

## R5 — target-side readiness

Freeze target-side readiness criterion, status, scope, and provenance.

~~~text
SOURCE_STEP_COMPLETE != TARGET_READY_BY_DEFAULT
HANDOFF_ACCEPTED != TARGET_READY_UNLESS_DECLARED
~~~

## R6 — exception class / precedence

Freeze exception action class and precedence.

~~~text
RETRY
RECOVERY
ESCALATION
STOP
~~~

No class may be substituted for another without an explicit rule.

## R7 — operational readout sufficiency

Freeze readout map, decision scope, collision/injectivity information, and sufficiency rule.

~~~text
DASHBOARD_EQUALITY != FULL_OPERATIONAL_STATE_EQUALITY
~~~

A reduced readout may support only the declared operational decision scope.

## R8 — Operation update lineage

Every claim-relevant update records:

~~~text
parent operation version
new operation version
new information cutoff
trigger
supersession relation
provenance
~~~

Historical execution/decision bases remain immutable.

## Aggregate

~~~text
REFINEMENT_GROUPS_ADOPTED:
  8/8
METHOD_IDENTITY_CHANGED:
  no
HISTORICAL_TASK_INTERFACE_REWRITTEN:
  no
BOUNDARY_COLLAPSE:
  0
FUNDAMENTAL_INTERFACE_FAILURE:
  0
SHARED_CORE_REOPEN_REQUIRED:
  no
PROTOCOL_FREEZE_AUTHORIZED:
  yes
~~~

Next: freeze executable Operation Protocol v0.1.
