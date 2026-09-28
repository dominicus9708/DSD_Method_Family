# CPR-CH-002 — Negative / Unresolved-Terminal Compression Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-28**  
Challenge ID: `CPR-CH-002`  
Method: **Compression / DSD 압축론**  
Protocol: **Compression Protocol v0.1**  
Case class: `negative_unresolved_terminal_coverage_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen protocol identity

~~~text
PROTOCOL_COMMIT:
  b1efa06e4c715e08ce2558a608c7f09aa22172bd

PROTOCOL_BLOB:
  4d67d800e107229f91c16cf5b0235928124482b2

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  T1-T18
~~~

The frozen protocol may not be modified in response to this challenge.

## 2. Purpose

Directly exercise the negative and unresolved Compression task statuses and terminals that CPR-CH-001 intentionally did not claim.

This bundle contains ten independent constructed subcases.

A conformant negative, blocked, conflicting, out-of-scope, underdetermined, or partial result counts as successful protocol execution.

~~~text
CONFORMANT_NEGATIVE_TERMINAL != METHOD_FAILURE
~~~

The challenge is internal constructed validation only.

It is not external validation, independent replication, or method-gain evidence.

## 3. Frozen status and terminal targets

Across CPR-CH-001 and CPR-CH-002, directly exercise all six primary task statuses:

~~~text
COMPRESSION_ESTABLISHED
COMPRESSION_NOT_ESTABLISHED
COMPRESSION_BLOCKED
COMPRESSION_CONFLICTING
COMPRESSION_OUT_OF_SCOPE
COMPRESSION_UNDERDETERMINED
~~~

and all seven task terminals:

~~~text
COMPRESSION_TASK_ESTABLISHED
COMPRESSION_TASK_PARTIAL
COMPRESSION_TASK_NOT_ESTABLISHED
COMPRESSION_TASK_BLOCKED
COMPRESSION_TASK_CONFLICTING
COMPRESSION_TASK_OUT_OF_SCOPE
COMPRESSION_TASK_UNDERDETERMINED
~~~

CPR-CH-001 already directly exercised the ESTABLISHED status and terminal.

## 4. N1 — purpose-destructive collision

Frozen task:

~~~text
TASK_ID:
  CPR-CH-002-N1

PRIMARY_CLAIM_LEVEL:
  PURPOSE_BOUNDED_COMPRESSION

source:
  x1=(A,1)
  x2=(B,1)

purpose:
  group A/B must remain distinguishable

compression:
  C(group,value)=value
~~~

Execution gives:

~~~text
C(x1)=1
C(x2)=1
~~~

The source pair is required-distinct but collides.

Expected:

~~~text
COLLISION_WITNESS_ESTABLISHED
COLLISION_PURPOSE_DESTRUCTIVE
REDUCTION_ESTABLISHED
PRIMARY_TASK_STATUS:
  COMPRESSION_NOT_ESTABLISHED
TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_NOT_ESTABLISHED
~~~

Guard:

~~~text
ACTUAL_REDUCTION != PURPOSE_PRESERVATION
DESTRUCTIVE_COLLISION != BLOCKED
~~~

## 5. N2 — preservation succeeds but no frozen reduction occurs

Frozen task:

~~~text
TASK_ID:
  CPR-CH-002-N2

PRIMARY_CLAIM_LEVEL:
  PURPOSE_BOUNDED_COMPRESSION

source representation:
  two records x 2 fields
  source cost = 4

map:
  C(a,b)=(a,b)

required distinctions:
  all source distinctions

accounting metric:
  FIELD_UNIT_COUNT-v1

reduced package cost:
  4

reduction requirement:
  strict
~~~

All required distinctions are preserved but no strict reduction occurs.

Expected:

~~~text
NO_COLLISION_ON_TESTED_CLASS
REDUCTION_NOT_ESTABLISHED
PRIMARY_TASK_STATUS:
  COMPRESSION_NOT_ESTABLISHED
TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_NOT_ESTABLISHED
~~~

Guard:

~~~text
DISTINCTION_PRESERVATION != COMPRESSION_ESTABLISHED
IDENTITY_TRANSFORMATION != COMPRESSION_BY_DEFAULT
~~~

## 6. N3 — blocked required status sidecar

Frozen task:

~~~text
TASK_ID:
  CPR-CH-002-N3

PRIMARY_CLAIM_LEVEL:
  STATUS_PRESERVING_COMPRESSION

source reduced value:
  available

purpose:
  defined-zero must remain distinct from absent

required source-status sidecar:
  unavailable

compression map:
  otherwise executable
~~~

The required status interface is unavailable before the claim can be evaluated.

Expected:

~~~text
REQUIRED_INTERFACE_STATUS:
  unavailable

PRIMARY_TASK_STATUS:
  COMPRESSION_BLOCKED

TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_BLOCKED
~~~

Guard:

~~~text
UNAVAILABLE_REQUIRED_INTERFACE
  !=
EVALUABLE_DESTRUCTIVE_LOSS

BLOCKED != NOT_ESTABLISHED
~~~

## 7. N4 — conflicting purpose relation

Frozen task:

~~~text
TASK_ID:
  CPR-CH-002-N4

PRIMARY_CLAIM_LEVEL:
  PURPOSE_BOUNDED_COMPRESSION

source:
  x != y

same frozen purpose/version records:

R1:
  (x,y) required-distinct

R2:
  (x,y) explicitly safe-to-merge

precedence resolver:
  none
~~~

Expected:

~~~text
PURPOSE_RELATION_STATUS:
  PURPOSE_RELATION_CONFLICTING

PRIMARY_TASK_STATUS:
  COMPRESSION_CONFLICTING

TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_CONFLICTING
~~~

Guard:

~~~text
CONFLICTING_PURPOSE_RECORDS
  !=
LICENSE_TO_SELECT_ONE_POST_HOC
~~~

## 8. N5 — stochastic encoder outside current protocol scope

Frozen task:

~~~text
TASK_ID:
  CPR-CH-002-N5

PRIMARY_CLAIM_LEVEL:
  PURPOSE_BOUNDED_COMPRESSION

requested encoder:
  same source x may emit z1 or z2

seed:
  not frozen

probability kernel:
  not frozen

stochastic interface:
  not supplied
~~~

Compression Protocol v0.1 freezes a deterministic map or deterministic composed chain.

Expected:

~~~text
COMPRESSION_DOMAIN_STATUS:
  COMPRESSION_DOMAIN_OUT_OF_SCOPE

PRIMARY_TASK_STATUS:
  COMPRESSION_OUT_OF_SCOPE

TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_OUT_OF_SCOPE
~~~

Guard:

~~~text
OUT_OF_SCOPE != FALSE
OUT_OF_SCOPE != NOT_ESTABLISHED
~~~

## 9. N6 — resolution underdetermination

Frozen task:

~~~text
TASK_ID:
  CPR-CH-002-N6

PRIMARY_CLAIM_LEVEL:
  RESOLUTION_BOUNDED_COMPRESSION

two admissible frozen resolution branches:
  epsilon_1
  epsilon_2

compression outcome:
  passes at epsilon_1
  fails at epsilon_2

resolver:
  none
~~~

Expected:

~~~text
RESOLUTION_STATUS:
  RESOLUTION_UNDERDETERMINED

PRIMARY_TASK_STATUS:
  COMPRESSION_UNDERDETERMINED

TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_UNDERDETERMINED
~~~

Guard:

~~~text
MULTIPLE_ADMISSIBLE_RESOLUTIONS_WITH_DIFFERENT_OUTCOMES
  !=
CONFLICTING_RECORDS
~~~

## 10. N7 — partial multi-obligation Compression task

Frozen task has two independent required compression obligations.

~~~text
TASK_ID:
  CPR-CH-002-N7
~~~

Q1:

~~~text
source cost:
  6

reduced cost:
  4

required distinctions:
  preserved

result:
  COMPRESSION_ESTABLISHED
~~~

Q2:

~~~text
source cost:
  4

reduced cost:
  4

required distinctions:
  preserved

strict reduction required

result:
  COMPRESSION_NOT_ESTABLISHED
~~~

No higher-priority terminal is present.

Expected:

~~~text
TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_PARTIAL
~~~

Guard:

~~~text
PARTIAL requires multiple independent required obligations
PARTIAL does not rescue one failed atomic compression proposition
~~~

## 11. N8 — purpose-safe collision but required reconstruction destroyed

Frozen task:

~~~text
TASK_ID:
  CPR-CH-002-N8

PRIMARY_CLAIM_LEVEL:
  RECONSTRUCTION_AWARE_COMPRESSION

source:
  x1=(A,a1)
  x2=(A,a2)

immediate purpose:
  detail may merge

compression:
  C(group,detail)=group

reconstruction requirement:
  exact source-detail recovery on the frozen class

required source class and collision evidence:
  available
~~~

Execution:

~~~text
C(x1)=A
C(x2)=A
~~~

The collision is purpose-safe for the immediate readout but destructive for the required reconstruction claim.

Expected:

~~~text
COLLISION_PURPOSE_STATUS:
  COLLISION_PURPOSE_SAFE

COLLISION_RECONSTRUCTION_STATUS:
  COLLISION_RECONSTRUCTION_DESTRUCTIVE

RECONSTRUCTION_STATUS:
  RECONSTRUCTION_NOT_ESTABLISHED

PRIMARY_TASK_STATUS:
  COMPRESSION_NOT_ESTABLISHED

TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_NOT_ESTABLISHED
~~~

Guard:

~~~text
PURPOSE_SAFE_COLLISION
  !=
RECONSTRUCTION_SAFE_COLLISION

COMPRESSION_SUCCESS_FOR_ONE_PURPOSE_AXIS
  !=
RECONSTRUCTION_SUCCESS
~~~

## 12. N9 — lossless on declared class without global promotion

Frozen task:

~~~text
TASK_ID:
  CPR-CH-002-N9

PRIMARY_CLAIM_LEVEL:
  LOSSLESS_ON_DECLARED_CLASS

declared source class:
  A={u0,u1,u2}

source representation cost:
  9 field units

map:
  C(u0)=0
  C(u1)=1
  C(u2)=2

reduced package cost:
  3 field units

outside declared class:
  v0 != v1
  C(v0)=9
  C(v1)=9
~~~

On A, outputs are distinct and strict reduction is established.

Expected:

~~~text
NO_COLLISION_ON_TESTED_CLASS

LOSSLESSNESS_STATUS:
  LOSSLESS_ON_DECLARED_CLASS

REDUCTION_STATUS:
  REDUCTION_ESTABLISHED

PRIMARY_TASK_STATUS:
  COMPRESSION_ESTABLISHED

TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_ESTABLISHED

GLOBAL_INJECTIVITY:
  not claimed
~~~

Guard:

~~~text
LOSSLESS_ON_DECLARED_CLASS != GLOBAL_INJECTIVITY
~~~

This positive subcase exists only to pressure scope boundaries inside the negative/unresolved bundle.

## 13. N10 — terminal precedence with lower-level state retention

Frozen task has four independent required obligations.

Q1:

~~~text
requested stochastic encoder has no frozen stochastic interface

status:
  COMPRESSION_OUT_OF_SCOPE
~~~

Q2:

~~~text
same source pair is both required-distinct and safe-to-merge

status:
  COMPRESSION_CONFLICTING
~~~

Q3:

~~~text
two admissible resolutions produce different outcomes
no resolver

status:
  COMPRESSION_UNDERDETERMINED
~~~

Q4:

~~~text
required provenance sidecar unavailable

status:
  COMPRESSION_BLOCKED
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
TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_OUT_OF_SCOPE

LOWER_LEVEL_Q2_RETAINED:
  yes

LOWER_LEVEL_Q3_RETAINED:
  yes

LOWER_LEVEL_Q4_RETAINED:
  yes
~~~

No lower-level state may be erased merely because Q1 determines the task terminal.

## 14. Protocol-conformance expectation

Every subcase is expected to remain:

~~~text
COMPRESSION_PROTOCOL_CONFORMANT
~~~

including negative, blocked, conflicting, out-of-scope, underdetermined, partial, and bounded positive outcomes.

No subcase assesses method gain.

~~~text
COMPRESSION_METHOD_GAIN_STATUS:
  COMPRESSION_METHOD_GAIN_NOT_ASSESSED
~~~

## 15. Frozen scoring — 80 checks

Each subcase has eight frozen checks.

### N1 — 8 checks

~~~text
N1-1 source pair frozen
N1-2 required-distinction relation frozen
N1-3 collision witness established
N1-4 purpose consequence destructive
N1-5 reduction established
N1-6 primary NOT_ESTABLISHED
N1-7 terminal NOT_ESTABLISHED
N1-8 protocol CONFORMANT
~~~

### N2 — 8 checks

~~~text
N2-1 identity map frozen
N2-2 all required distinctions preserved
N2-3 no collision on tested class
N2-4 source cost = 4
N2-5 reduced package cost = 4
N2-6 reduction NOT_ESTABLISHED
N2-7 terminal NOT_ESTABLISHED
N2-8 protocol CONFORMANT
~~~

### N3 — 8 checks

~~~text
N3-1 status-preserving claim frozen
N3-2 zero/absence distinction required
N3-3 required sidecar unavailable
N3-4 no destructive-loss inference fabricated
N3-5 primary BLOCKED
N3-6 terminal BLOCKED
N3-7 BLOCKED != NOT_ESTABLISHED preserved
N3-8 protocol CONFORMANT
~~~

### N4 — 8 checks

~~~text
N4-1 one purpose/version frozen
N4-2 required-distinct record applicable
N4-3 safe-to-merge record applicable
N4-4 same source pair targeted
N4-5 no precedence resolver
N4-6 purpose relation CONFLICTING
N4-7 terminal CONFLICTING
N4-8 protocol CONFORMANT
~~~

### N5 — 8 checks

~~~text
N5-1 stochastic encoder requested
N5-2 seed not frozen
N5-3 probability kernel not frozen
N5-4 stochastic interface absent
N5-5 domain OUT_OF_SCOPE
N5-6 primary OUT_OF_SCOPE
N5-7 terminal OUT_OF_SCOPE
N5-8 protocol CONFORMANT
~~~

### N6 — 8 checks

~~~text
N6-1 resolution-bounded claim frozen
N6-2 epsilon_1 admissible
N6-3 epsilon_2 admissible
N6-4 outcomes differ
N6-5 no resolver
N6-6 resolution UNDERDETERMINED
N6-7 terminal UNDERDETERMINED
N6-8 protocol CONFORMANT
~~~

### N7 — 8 checks

~~~text
N7-1 two independent obligations frozen
N7-2 Q1 distinctions preserved
N7-3 Q1 strict reduction established
N7-4 Q1 COMPRESSION_ESTABLISHED
N7-5 Q2 distinctions preserved
N7-6 Q2 strict reduction fails
N7-7 terminal PARTIAL
N7-8 protocol CONFORMANT
~~~

### N8 — 8 checks

~~~text
N8-1 immediate purpose-safe merge frozen
N8-2 exact reconstruction required
N8-3 collision witness established
N8-4 purpose consequence SAFE
N8-5 reconstruction consequence DESTRUCTIVE
N8-6 reconstruction NOT_ESTABLISHED
N8-7 terminal NOT_ESTABLISHED
N8-8 protocol CONFORMANT
~~~

### N9 — 8 checks

~~~text
N9-1 declared class A frozen
N9-2 outputs on A distinct
N9-3 NO_COLLISION_ON_TESTED_CLASS
N9-4 LOSSLESS_ON_DECLARED_CLASS
N9-5 strict reduction 9 -> 3
N9-6 compression ESTABLISHED
N9-7 global injectivity not claimed
N9-8 protocol CONFORMANT
~~~

### N10 — 8 checks

~~~text
N10-1 Q1 OUT_OF_SCOPE retained
N10-2 Q2 CONFLICTING retained
N10-3 Q3 UNDERDETERMINED retained
N10-4 Q4 BLOCKED retained
N10-5 precedence frozen
N10-6 terminal OUT_OF_SCOPE
N10-7 lower-level states preserved
N10-8 protocol CONFORMANT
~~~

~~~text
TOTAL_REQUIRED_CHECKS:
  80

PASS_THRESHOLD:
  80/80

PARTIAL_PASS_ALLOWED:
  no
~~~

## 16. Counter rule

If all 80 checks pass:

~~~text
DIRECT_COMPRESSION_PILOTS_ATTEMPTED:
  2

SUCCESSFUL_DIRECT_COMPRESSION_PILOTS:
  2

POSITIVE_COMPRESSION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_COMPRESSION_CASES:
  1

ALL_SIX_COMPRESSION_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  yes

ALL_SEVEN_COMPRESSION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes

METHOD_BOUNDARY_COMPRESSION_CASES:
  0

BASELINE_COMPRESSION_CASES:
  0

NO_GAIN_COMPRESSION_CASES:
  0

REPRODUCIBILITY_CASES:
  0

CURRENT_COMPRESSION_EVIDENCE_STATUS:
  validation_in_progress

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 17. Next

If the frozen bundle passes, prospectively precommit the direct neighboring-method boundary challenge.
