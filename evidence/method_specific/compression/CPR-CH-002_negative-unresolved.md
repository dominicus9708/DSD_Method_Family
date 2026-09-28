# CPR-CH-002 — Negative / Unresolved-Terminal Compression Challenge Result

Status: **EXECUTED — 80/80 PASS**  
Date: **2026-09-28**  
Challenge ID: `CPR-CH-002`  
Method: **Compression / DSD 압축론**  
Protocol: **Compression Protocol v0.1**  
Case class: `negative_unresolved_terminal_coverage_constructed`

## 1. Frozen references

~~~text
PROTOCOL_COMMIT:
  b1efa06e4c715e08ce2558a608c7f09aa22172bd

PROTOCOL_BLOB:
  4d67d800e107229f91c16cf5b0235928124482b2

PRECOMMIT_COMMIT:
  865b195e37375c3e5132236018f0ba6b466c596e

PRECOMMIT_BLOB:
  f6ce63ef7bc453c3ebc30cf676f49e2d28be4c7e
~~~

No protocol rule, fixture, expected terminal, scoring item, or pass threshold was changed after precommit.

## 2. Final bundle result

~~~text
TOTAL_REQUIRED_CHECKS:
  80

PASSED:
  80

FAILED:
  0

ALL_SIX_COMPRESSION_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  yes

ALL_SEVEN_COMPRESSION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

Every subcase remained:

~~~text
COMPRESSION_PROTOCOL_CONFORMANT
~~~

A negative or unresolved terminal was treated as a valid protocol output rather than a protocol failure.

## 3. N1 — purpose-destructive collision

Frozen source:

~~~text
x1=(A,1)
x2=(B,1)

C(group,value)=value
~~~

Execution:

~~~text
C(x1)=1
C(x2)=1
~~~

The pair is frozen as required-distinct.

Result:

~~~text
COLLISION_STATUS:
  COLLISION_WITNESS_ESTABLISHED

COLLISION_PURPOSE_STATUS:
  COLLISION_PURPOSE_DESTRUCTIVE

REDUCTION_STATUS:
  REDUCTION_ESTABLISHED

PRIMARY_TASK_STATUS:
  COMPRESSION_NOT_ESTABLISHED

TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_NOT_ESTABLISHED

PROTOCOL_CONFORMANCE:
  COMPRESSION_PROTOCOL_CONFORMANT
~~~

Preserved:

~~~text
ACTUAL_REDUCTION != PURPOSE_PRESERVATION
DESTRUCTIVE_COLLISION != BLOCKED
~~~

## 4. N2 — preservation without reduction

Frozen map:

~~~text
C(a,b)=(a,b)
~~~

All required distinctions survive.

Accounting:

~~~text
SOURCE_COST:
  4

REDUCED_PACKAGE_COST:
  4

REDUCTION_REQUIREMENT:
  strict
~~~

Result:

~~~text
COLLISION_STATUS:
  NO_COLLISION_ON_TESTED_CLASS

REDUCTION_STATUS:
  REDUCTION_NOT_ESTABLISHED

PRIMARY_TASK_STATUS:
  COMPRESSION_NOT_ESTABLISHED

TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_NOT_ESTABLISHED

PROTOCOL_CONFORMANCE:
  COMPRESSION_PROTOCOL_CONFORMANT
~~~

Preserved:

~~~text
DISTINCTION_PRESERVATION != COMPRESSION_ESTABLISHED
IDENTITY_TRANSFORMATION != COMPRESSION_BY_DEFAULT
~~~

## 5. N3 — blocked required status sidecar

The purpose requires:

~~~text
DEFINED_ZERO != ABSENCE
~~~

but the required source-status sidecar is unavailable before evaluation.

Result:

~~~text
REQUIRED_INTERFACE_STATUS:
  unavailable

PRIMARY_TASK_STATUS:
  COMPRESSION_BLOCKED

TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_BLOCKED

PROTOCOL_CONFORMANCE:
  COMPRESSION_PROTOCOL_CONFORMANT
~~~

No destructive-loss verdict was fabricated.

Preserved:

~~~text
UNAVAILABLE_REQUIRED_INTERFACE
  !=
EVALUABLE_DESTRUCTIVE_LOSS

BLOCKED != NOT_ESTABLISHED
~~~

## 6. N4 — conflicting purpose relation

Applicable records under one frozen purpose/version:

~~~text
R1:
  (x,y) required-distinct

R2:
  (x,y) safe-to-merge

resolver:
  none
~~~

Result:

~~~text
PURPOSE_RELATION_STATUS:
  PURPOSE_RELATION_CONFLICTING

PRIMARY_TASK_STATUS:
  COMPRESSION_CONFLICTING

TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_CONFLICTING

PROTOCOL_CONFORMANCE:
  COMPRESSION_PROTOCOL_CONFORMANT
~~~

No record was selected post hoc.

## 7. N5 — stochastic encoder outside v0.1 scope

Frozen request:

~~~text
same x may emit z1 or z2

seed:
  not frozen

probability kernel:
  not frozen

stochastic interface:
  absent
~~~

Result:

~~~text
COMPRESSION_DOMAIN_STATUS:
  COMPRESSION_DOMAIN_OUT_OF_SCOPE

PRIMARY_TASK_STATUS:
  COMPRESSION_OUT_OF_SCOPE

TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_OUT_OF_SCOPE

PROTOCOL_CONFORMANCE:
  COMPRESSION_PROTOCOL_CONFORMANT
~~~

Preserved:

~~~text
OUT_OF_SCOPE != FALSE
OUT_OF_SCOPE != NOT_ESTABLISHED
~~~

## 8. N6 — resolution underdetermination

Frozen branches:

~~~text
epsilon_1:
  compression passes

epsilon_2:
  compression fails

resolver:
  none
~~~

Both resolution branches are admissible.

Result:

~~~text
RESOLUTION_STATUS:
  RESOLUTION_UNDERDETERMINED

PRIMARY_TASK_STATUS:
  COMPRESSION_UNDERDETERMINED

TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_UNDERDETERMINED

PROTOCOL_CONFORMANCE:
  COMPRESSION_PROTOCOL_CONFORMANT
~~~

Preserved:

~~~text
UNDERDETERMINED != CONFLICTING
~~~

## 9. N7 — partial multi-obligation task

Q1:

~~~text
required distinctions:
  preserved

source cost:
  6

reduced cost:
  4

result:
  COMPRESSION_ESTABLISHED
~~~

Q2:

~~~text
required distinctions:
  preserved

source cost:
  4

reduced cost:
  4

strict reduction:
  failed

result:
  COMPRESSION_NOT_ESTABLISHED
~~~

The obligations are independent and no higher-priority terminal is present.

Result:

~~~text
TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_PARTIAL

PROTOCOL_CONFORMANCE:
  COMPRESSION_PROTOCOL_CONFORMANT
~~~

Preserved:

~~~text
PARTIAL requires multiple independent required obligations
PARTIAL does not rescue one failed atomic compression proposition
~~~

## 10. N8 — purpose-safe but reconstruction-destructive collision

Frozen source:

~~~text
x1=(A,a1)
x2=(A,a2)

C(group,detail)=group
~~~

Immediate purpose permits detail merging.

Reconstruction-aware primary claim requires exact detail recovery.

Execution:

~~~text
C(x1)=A
C(x2)=A
~~~

Result:

~~~text
COLLISION_STATUS:
  COLLISION_WITNESS_ESTABLISHED

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

PROTOCOL_CONFORMANCE:
  COMPRESSION_PROTOCOL_CONFORMANT
~~~

Preserved:

~~~text
PURPOSE_SAFE_COLLISION != RECONSTRUCTION_SAFE_COLLISION
COMPRESSION_SUCCESS_FOR_ONE_PURPOSE_AXIS != RECONSTRUCTION_SUCCESS
~~~

## 11. N9 — lossless on declared class only

Declared source class:

~~~text
A={u0,u1,u2}
~~~

Frozen outputs:

~~~text
C(u0)=0
C(u1)=1
C(u2)=2
~~~

Accounting:

~~~text
SOURCE_COST:
  9

REDUCED_PACKAGE_COST:
  3
~~~

No collision occurs on A.

Outside A, the frozen witness remains:

~~~text
v0 != v1
C(v0)=9
C(v1)=9
~~~

Result:

~~~text
COLLISION_STATUS:
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

PROTOCOL_CONFORMANCE:
  COMPRESSION_PROTOCOL_CONFORMANT
~~~

Preserved:

~~~text
LOSSLESS_ON_DECLARED_CLASS != GLOBAL_INJECTIVITY
~~~

## 12. N10 — terminal precedence

Four independent required obligations retain:

~~~text
Q1:
  COMPRESSION_OUT_OF_SCOPE

Q2:
  COMPRESSION_CONFLICTING

Q3:
  COMPRESSION_UNDERDETERMINED

Q4:
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

Result:

~~~text
TASK_TERMINAL_STATUS:
  COMPRESSION_TASK_OUT_OF_SCOPE

LOWER_LEVEL_Q2_RETAINED:
  yes

LOWER_LEVEL_Q3_RETAINED:
  yes

LOWER_LEVEL_Q4_RETAINED:
  yes

PROTOCOL_CONFORMANCE:
  COMPRESSION_PROTOCOL_CONFORMANT
~~~

The higher-priority terminal did not erase lower-level states.

## 13. Primary-status and terminal coverage

Across CPR-CH-001 and CPR-CH-002:

~~~text
PRIMARY TASK STATUSES

COMPRESSION_ESTABLISHED:
  directly exercised

COMPRESSION_NOT_ESTABLISHED:
  directly exercised

COMPRESSION_BLOCKED:
  directly exercised

COMPRESSION_CONFLICTING:
  directly exercised

COMPRESSION_OUT_OF_SCOPE:
  directly exercised

COMPRESSION_UNDERDETERMINED:
  directly exercised
~~~

Therefore:

~~~text
ALL_SIX_COMPRESSION_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  yes
~~~

Task terminals:

~~~text
COMPRESSION_TASK_ESTABLISHED:
  directly exercised

COMPRESSION_TASK_PARTIAL:
  directly exercised

COMPRESSION_TASK_NOT_ESTABLISHED:
  directly exercised

COMPRESSION_TASK_BLOCKED:
  directly exercised

COMPRESSION_TASK_CONFLICTING:
  directly exercised

COMPRESSION_TASK_OUT_OF_SCOPE:
  directly exercised

COMPRESSION_TASK_UNDERDETERMINED:
  directly exercised
~~~

Therefore:

~~~text
ALL_SEVEN_COMPRESSION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes
~~~

## 14. Execution of the 80 frozen checks

### N1

~~~text
N1-1 PASS
N1-2 PASS
N1-3 PASS
N1-4 PASS
N1-5 PASS
N1-6 PASS
N1-7 PASS
N1-8 PASS
~~~

### N2

~~~text
N2-1 PASS
N2-2 PASS
N2-3 PASS
N2-4 PASS
N2-5 PASS
N2-6 PASS
N2-7 PASS
N2-8 PASS
~~~

### N3

~~~text
N3-1 PASS
N3-2 PASS
N3-3 PASS
N3-4 PASS
N3-5 PASS
N3-6 PASS
N3-7 PASS
N3-8 PASS
~~~

### N4

~~~text
N4-1 PASS
N4-2 PASS
N4-3 PASS
N4-4 PASS
N4-5 PASS
N4-6 PASS
N4-7 PASS
N4-8 PASS
~~~

### N5

~~~text
N5-1 PASS
N5-2 PASS
N5-3 PASS
N5-4 PASS
N5-5 PASS
N5-6 PASS
N5-7 PASS
N5-8 PASS
~~~

### N6

~~~text
N6-1 PASS
N6-2 PASS
N6-3 PASS
N6-4 PASS
N6-5 PASS
N6-6 PASS
N6-7 PASS
N6-8 PASS
~~~

### N7

~~~text
N7-1 PASS
N7-2 PASS
N7-3 PASS
N7-4 PASS
N7-5 PASS
N7-6 PASS
N7-7 PASS
N7-8 PASS
~~~

### N8

~~~text
N8-1 PASS
N8-2 PASS
N8-3 PASS
N8-4 PASS
N8-5 PASS
N8-6 PASS
N8-7 PASS
N8-8 PASS
~~~

### N9

~~~text
N9-1 PASS
N9-2 PASS
N9-3 PASS
N9-4 PASS
N9-5 PASS
N9-6 PASS
N9-7 PASS
N9-8 PASS
~~~

### N10

~~~text
N10-1 PASS
N10-2 PASS
N10-3 PASS
N10-4 PASS
N10-5 PASS
N10-6 PASS
N10-7 PASS
N10-8 PASS
~~~

Final:

~~~text
TOTAL_REQUIRED_CHECKS:
  80

PASSED:
  80

FAILED:
  0
~~~

## 15. Counter update

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

EXTERNAL_COMPRESSION_APPLICATIONS:
  0

INDEPENDENT_COMPRESSION_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established

COMPRESSION_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_COMPRESSION_EVIDENCE_STATUS:
  validation_in_progress

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 16. Maximum-supported claim

Supported:

~~~text
Within the constructed CPR-CH-002 bundle,
Compression Protocol v0.1 preserves the frozen distinctions among
destructive collision, failed reduction, blocked required interface,
conflicting purpose semantics, out-of-scope stochastic request,
resolution underdetermination, partial multi-obligation execution,
reconstruction-destructive loss, declared-class losslessness,
and terminal precedence without turning those outcomes into
protocol failure.
~~~

Not established:

~~~text
external applicability
independent validation
independent replication
method superiority
permanent method irreducibility
~~~

## 17. Next

Prospectively precommit and execute the direct neighboring-method Compression boundary challenge under fair shared-artifact access.
