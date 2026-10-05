# DSD Control — Boundary Amendment 001

Status: **ESTABLISHED — 8/8 REFINEMENTS ADOPTED / PROTOCOL FREEZE AUTHORIZED**  
Date: **2026-10-06**

~~~text
TASK_INTERFACE_COMMIT:
  5a8d11191f0a76b0223a68155e34d8700927a651
TASK_INTERFACE_BLOB:
  037a03e6249b835d479e4498869a28cd7293838a

BOUNDARY_REVIEW_COMMIT:
  a74f3d6c663b6c26ed1c46909c9fa629a9adf394
BOUNDARY_REVIEW_BLOB:
  c9efeaeb76f612e1b757bff04d74205633a62532
~~~

The historical Task Interface is not rewritten.

## R1 action status

~~~text
known inadmissible/inapplicable action -> CONTROL_NOT_ESTABLISHED
required status interface unavailable -> CONTROL_BLOCKED
conflicting applicable action records -> CONTROL_CONFLICTING
unresolved admissible action semantics -> CONTROL_UNDERDETERMINED
~~~

## R2 prerequisite status

Freeze prerequisite identity, requiredness, satisfaction, provenance, and evaluation status.

Known unsatisfied required prerequisite maps to NOT_ESTABLISHED; unavailable check to BLOCKED; conflict to CONFLICTING; unresolved semantics to UNDERDETERMINED.

## R3 target reachability

Freeze:

~~~text
TARGET_REACHABILITY_INTERFACE
TARGET_REACHABILITY_STATUS
TARGET_REACH_SCOPE
TARGET_REACH_PROVENANCE
~~~

~~~text
TARGET_DECLARED != TARGET_REACHABLE
ONE_SIMULATED_SUCCESS != UNIVERSAL_TARGET_REACHABILITY
~~~

## R4 state-observation status

Required observation unavailable -> BLOCKED.  
Known invalid required observation -> NOT_ESTABLISHED.  
Conflict -> CONFLICTING.  
Unresolved admissible semantics -> UNDERDETERMINED.

## R5 effect uncertainty vs semantic underdetermination

Freeze uncertainty kind/scope and semantic-resolution alternatives.

~~~text
declared effect uncertainty
  may remain inside supported Control claim

unresolved effect/policy semantics producing different decisions
  -> CONTROL_UNDERDETERMINED
~~~

## R6 explicit constraint transformation

Any transformation of a hard constraint must identify source, target, scope, rule, authorization, and provenance.

Unregistered transformation cannot alter action admissibility.

## R7 required constraint completeness

Freeze required constraint components and completeness status.

A missing required component is not treated as irrelevant or zero-cost.

## R8 policy update lineage

Every claim-relevant update records parent policy version, new version, new information cutoff, trigger, supersession, and provenance.

Historical decision versions remain immutable.

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

Next: freeze executable Control Protocol v0.1.
