# RECON-CH-002 — Terminal-Coverage Reconstruction Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-01**  
Challenge ID: `RECON-CH-002`  
Method: **Reconstruction / DSD 복원론**  
Protocol: **Reconstruction Protocol v0.1**  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen protocol

~~~text
PROTOCOL_COMMIT: 2d4cdcab4b646a9d75f96dcc2ef301722eb612ad
PROTOCOL_BLOB: 1f009e81b9992fbdec75abbd9551e9d06f0a170e
VALIDITY_GATES: G1-G18
BINDING_OPERATION: T1-T18
POST_HOC_REPAIR: prohibited
~~~

## 2. Purpose

Directly exercise the remaining Reconstruction primary statuses and all seven task terminals.

~~~text
SUBCASES:
  N1 uniqueness evaluably fails
  N2 required sidecar unavailable
  N3 conflicting bridge rules
  N4 underdetermined bridge semantics
  N5 requested relation outside scope
  N6 valid PARTIAL multi-obligation task
  N7 conflicting evidence packet
  N8 coherent zero-compatible declared class
  N9 unrecoverability claim evaluably fails
  N10 terminal precedence

INFERENCE_MODE: DETERMINISTIC_COMPATIBILITY
METHOD_GAIN_ASSESSMENT: not_requested
~~~

## 3. N1 — uniqueness claim not established

~~~text
PRIMARY_CLAIM_LEVEL:
  UNIQUE_WITHIN_DECLARED_RECONSTRUCTION_CLASS

class:
  {h1,h2}

forward/evidence:
  F(h1)=0
  F(h2)=0
  observed y=0

evidence:
  coherent

bridge:
  available
~~~

Expected:

~~~text
both candidates compatible
RECONSTRUCTION_SET_MULTIPLE_COMPATIBLE
RECONSTRUCTION_NOT_ESTABLISHED
RECONSTRUCTION_TASK_NOT_ESTABLISHED
RECONSTRUCTION_PROTOCOL_CONFORMANT
~~~

## 4. N2 — required sidecar unavailable

~~~text
PRIMARY_CLAIM_LEVEL:
  DECLARED_SCOPE_SOURCE_RECONSTRUCTION

requested distinction:
  retained support structure

main readout:
  available

required support-retention sidecar:
  unavailable

replacement:
  none
~~~

Expected:

~~~text
REQUIRED_RECONSTRUCTION_INTERFACE_UNAVAILABLE
RECONSTRUCTION_BLOCKED
RECONSTRUCTION_TASK_BLOCKED
RECONSTRUCTION_PROTOCOL_CONFORMANT
~~~

Required:

~~~text
unavailable interface != evaluable loss
BLOCKED != NOT_ESTABLISHED
~~~

## 5. N3 — conflicting bridge

~~~text
same bridge identity/version/scope:
  yes

rule A:
  pair compatible

rule B:
  pair incompatible

resolver:
  none
~~~

Expected:

~~~text
BRIDGE_RELATION_CONFLICTING
RECONSTRUCTION_PAIR_CONFLICTING
RECONSTRUCTION_CANDIDATE_CONFLICTING
RECONSTRUCTION_CONFLICTING
RECONSTRUCTION_TASK_CONFLICTING
RECONSTRUCTION_PROTOCOL_CONFORMANT
~~~

## 6. N4 — underdetermined bridge semantics

~~~text
interpretation A:
  pair compatible

interpretation B:
  pair incompatible

both interpretations:
  admissible alternatives

resolver:
  none
~~~

Expected:

~~~text
BRIDGE_RELATION_UNDERDETERMINED
RECONSTRUCTION_PAIR_UNDERDETERMINED
RECONSTRUCTION_CANDIDATE_UNDERDETERMINED
RECONSTRUCTION_UNDERDETERMINED
RECONSTRUCTION_TASK_UNDERDETERMINED
RECONSTRUCTION_PROTOCOL_CONFORMANT
~~~

## 7. N5 — relation outside frozen scope

~~~text
PRIMARY_CLAIM_LEVEL:
  HISTORY_COMPATIBILITY_SET

requested regime:
  R2

bridge scope:
  R1 only

declared extension:
  none
~~~

Expected:

~~~text
BRIDGE_RELATION_OUT_OF_SCOPE
RECONSTRUCTION_OUT_OF_SCOPE
RECONSTRUCTION_TASK_OUT_OF_SCOPE
RECONSTRUCTION_PROTOCOL_CONFORMANT
~~~

## 8. N6 — valid PARTIAL task

Two independently required in-scope obligations:

~~~text
Q1:
  compatibility-set claim
  compatible set {p1}
  RECONSTRUCTION_ESTABLISHED

Q2:
  uniqueness claim
  compatible set {q1,q2}
  RECONSTRUCTION_NOT_ESTABLISHED

higher-priority terminal:
  none
~~~

Expected:

~~~text
RECONSTRUCTION_TASK_PARTIAL
RECONSTRUCTION_PROTOCOL_CONFORMANT
~~~

Required:

~~~text
PARTIAL != one-claim rescue
PARTIAL != BLOCKED rescue
~~~

## 9. N7 — conflicting evidence packet

~~~text
same carrier/time/regime/schema:
  yes

e1:
  Y=0
  valid

e2:
  Y=1
  valid

exact single-valued semantics:
  yes

resolver:
  none
~~~

Expected:

~~~text
EVIDENCE_SET_CONFLICTING
RECONSTRUCTION_CONFLICTING
RECONSTRUCTION_TASK_CONFLICTING
zero-compatible set not asserted
RECONSTRUCTION_PROTOCOL_CONFORMANT
~~~

## 10. N8 — coherent zero-compatible declared class

~~~text
class:
  {n1,n2}

evidence:
  y=2

bridge:
  n1 -> y=0
  n2 -> y=1

evidence:
  coherent

bridge:
  available
~~~

Expected:

~~~text
n1 excluded
n2 excluded
RECONSTRUCTION_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS
RECONSTRUCTION_ESTABLISHED
RECONSTRUCTION_TASK_ESTABLISHED
RECONSTRUCTION_PROTOCOL_CONFORMANT
~~~

The supported statement is bounded to the declared class.

## 11. N9 — unrecoverability claim evaluably fails

~~~text
PRIMARY_CLAIM_LEVEL:
  UNRECOVERABLE_INFORMATION_ON_FROZEN_INTERFACE

class:
  {k1,k2}

main readout:
  F(k1)=1
  F(k2)=1

support sidecar:
  k1 -> S1
  k2 -> S2

frozen evidence:
  readout=1
  support=S1

interface closure:
  INTERFACE_COMPLETE_FOR_DECLARED_CLAIM
~~~

Expected:

~~~text
k1 compatible
k2 excluded
RECONSTRUCTION_SET_UNIQUE_WITHIN_DECLARED_CLASS
RECOVERABLE_ON_DECLARED_SCOPE
RECONSTRUCTION_NOT_ESTABLISHED
RECONSTRUCTION_TASK_NOT_ESTABLISHED
RECONSTRUCTION_PROTOCOL_CONFORMANT
~~~

## 12. N10 — terminal precedence

Four independent required obligations:

~~~text
Q1: RECONSTRUCTION_OUT_OF_SCOPE
Q2: RECONSTRUCTION_CONFLICTING
Q3: RECONSTRUCTION_UNDERDETERMINED
Q4: RECONSTRUCTION_BLOCKED
~~~

Frozen precedence:

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

Expected:

~~~text
RECONSTRUCTION_TASK_OUT_OF_SCOPE
Q2 retained
Q3 retained
Q4 retained
RECONSTRUCTION_PROTOCOL_CONFORMANT
~~~

## 13. Frozen scoring

Each N1-N10 has 8 checks.

~~~text
N1:
  claim frozen
  coherent evidence
  bridge available
  both candidates compatible
  MULTIPLE_COMPATIBLE
  primary NOT_ESTABLISHED
  terminal NOT_ESTABLISHED
  protocol CONFORMANT

N2:
  distinction claim-relevant
  required sidecar unavailable
  no negative-evidence conversion
  no loss claim fabricated
  primary BLOCKED
  terminal BLOCKED
  BLOCKED distinct from NOT_ESTABLISHED
  protocol CONFORMANT

N3:
  same bridge/version/scope
  rule A applies
  rule B applies
  outcomes incompatible
  no resolver
  CONFLICTING status
  CONFLICTING terminal
  protocol CONFORMANT

N4:
  two admissible interpretations
  A compatible
  B incompatible
  no internal contradiction fabricated
  no resolver
  UNDERDETERMINED status
  UNDERDETERMINED terminal
  protocol CONFORMANT

N5:
  requested R2 frozen
  bridge R1 frozen
  no extension
  outside scope
  primary OUT_OF_SCOPE
  terminal OUT_OF_SCOPE
  OUT_OF_SCOPE distinct from BLOCKED
  protocol CONFORMANT

N6:
  two independent obligations
  Q1 evaluable
  Q1 established
  Q2 evaluable
  Q2 not established
  no higher-priority terminal
  terminal PARTIAL
  protocol CONFORMANT

N7:
  same evidence schema
  e1 valid
  e2 valid
  no resolver
  evidence CONFLICTING
  zero-compatible set not asserted
  terminal CONFLICTING
  protocol CONFORMANT

N8:
  evidence frozen
  evidence coherent
  bridge available
  n1 excluded
  n2 excluded
  NONE_COMPATIBLE_IN_DECLARED_CLASS
  task ESTABLISHED with bounded claim
  protocol CONFORMANT

N9:
  unrecoverability claim frozen
  complete-for-claim interface
  main-readout collision retained
  support sidecar distinguishes
  k1 compatible
  k2 excluded
  terminal NOT_ESTABLISHED
  protocol CONFORMANT

N10:
  Q1 retained
  Q2 retained
  Q3 retained
  Q4 retained
  precedence frozen
  terminal OUT_OF_SCOPE
  subordinate states preserved
  protocol CONFORMANT
~~~

~~~text
TOTAL_REQUIRED_CHECKS: 80
PASS_THRESHOLD: 80/80
PARTIAL_PASS_ALLOWED: no
~~~

## 14. Counter rule

If all checks pass:

~~~text
DIRECT_RECONSTRUCTION_PILOTS_ATTEMPTED: 2
SUCCESSFUL_DIRECT_RECONSTRUCTION_PILOTS: 2
POSITIVE_RECONSTRUCTION_CASES: 1
NEGATIVE_OR_UNRESOLVED_RECONSTRUCTION_CASES: 1
UNRECOVERABILITY_RECONSTRUCTION_CASES: 2

ALL_SIX_RECONSTRUCTION_PRIMARY_STATUSES_DIRECTLY_EXERCISED: yes
ALL_SEVEN_RECONSTRUCTION_TASK_TERMINALS_DIRECTLY_EXERCISED: yes

METHOD_BOUNDARY_RECONSTRUCTION_CASES: 0
BASELINE_RECONSTRUCTION_CASES: 0
NO_GAIN_RECONSTRUCTION_CASES: 0
REPRODUCIBILITY_CASES: 0

CURRENT_RECONSTRUCTION_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
~~~

The unrecoverability counter counts direct cases whose primary claim concerns frozen-interface recoverability, whether the requested unrecoverability claim is established or evaluably not established.

## 15. Next

If this frozen bundle passes, prospectively precommit the direct neighboring-method boundary challenge.
