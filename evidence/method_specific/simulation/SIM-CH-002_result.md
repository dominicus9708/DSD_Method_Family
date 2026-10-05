# SIM-CH-002 — Negative / Terminal-Coverage Simulation Challenge Result

Status: **EXECUTED — 80/80 PASS**  
Date: **2026-10-05**  
Challenge ID: `SIM-CH-002`  
Method: **Simulation / DSD 시뮬레이션론**  
Protocol: **Simulation Protocol v0.1**  
Case class: `negative_unresolved_terminal_coverage_constructed`

## 1. Frozen references

~~~text
PROTOCOL_COMMIT:
  ea271d04eb09d252299d9420d0fb1191564f5bc6

PROTOCOL_BLOB:
  c3d6f80d99dabb5b84c7a60fd2df3f58bf9dba35

PRECOMMIT_COMMIT:
  8db0d4fd374c5576acf4fc80809775d6ea1630f3

PRECOMMIT_BLOB:
  f76d39d1e9bd183f948237c4c12e8f7325edee49
~~~

Execution used the frozen precommit without changing model semantics, terminal precedence, status mapping, numerical criteria, or scoring.

## 2. N1 — known inadmissible initial state

Frozen state class:

~~~text
x >= 0
~~~

Frozen initial state:

~~~text
x_0=-1
~~~

The initial-state check is fully evaluable and fails.

Result:

~~~text
INITIAL_STATE_ADMISSIBILITY:
  INITIAL_STATE_INADMISSIBLE

SIMULATION_PRIMARY_STATUS:
  SIMULATION_NOT_ESTABLISHED

SIMULATION_TASK_TERMINAL:
  SIMULATION_TASK_NOT_ESTABLISHED

SIMULATION_PROTOCOL_CONFORMANCE:
  SIMULATION_PROTOCOL_CONFORMANT
~~~

This is an evaluable negative result, not a blocked result.

## 3. N2 — unavailable required evolution law

The required law `LAW-N2-v1` is unavailable.

No protocol rule permits treating missing law information as zero dynamics or substituting a constant trajectory.

Result:

~~~text
EVOLUTION_LAW_STATUS:
  EVOLUTION_LAW_UNAVAILABLE

SIMULATION_PRIMARY_STATUS:
  SIMULATION_BLOCKED

SIMULATION_TASK_TERMINAL:
  SIMULATION_TASK_BLOCKED

SIMULATION_PROTOCOL_CONFORMANCE:
  SIMULATION_PROTOCOL_CONFORMANT
~~~

No claim that the model has no trajectory was made.

## 4. N3 — conflicting evolution laws

Under the same frozen model identity/version:

~~~text
L1:
  x_(n+1)=x_n+1
  applicable=yes

L2:
  x_(n+1)=x_n-1
  applicable=yes

resolver:
  none
~~~

The applicable laws yield materially different requested trajectories.

Result:

~~~text
EVOLUTION_LAW_STATUS:
  EVOLUTION_LAW_CONFLICTING

SIMULATION_PRIMARY_STATUS:
  SIMULATION_CONFLICTING

SIMULATION_TASK_TERMINAL:
  SIMULATION_TASK_CONFLICTING

SIMULATION_PROTOCOL_CONFORMANCE:
  SIMULATION_PROTOCOL_CONFORMANT
~~~

No law was selected arbitrarily.

## 5. N4 — Prediction request outside Simulation

The internally model-consistent trajectory does not by itself establish future external-world truth.

Result:

~~~text
PREDICTION_HANDOFF:
  required

SIMULATION_PRIMARY_STATUS:
  SIMULATION_OUT_OF_SCOPE

SIMULATION_TASK_TERMINAL:
  SIMULATION_TASK_OUT_OF_SCOPE

SIMULATION_PROTOCOL_CONFORMANCE:
  SIMULATION_PROTOCOL_CONFORMANT
~~~

No empirical truth claim was fabricated.

## 6. N5 — underdetermined model semantics

Frozen admissible alternatives:

~~~text
M-A:
  x_1=1

M-B:
  x_1=2

resolver:
  none

declared branching relation:
  none
~~~

This multiplicity comes from unresolved admissible model semantics, not from an explicitly declared branching transition.

Result:

~~~text
SIMULATION_PRIMARY_STATUS:
  SIMULATION_UNDERDETERMINED

SIMULATION_TASK_TERMINAL:
  SIMULATION_TASK_UNDERDETERMINED

SIMULATION_PROTOCOL_CONFORMANCE:
  SIMULATION_PROTOCOL_CONFORMANT
~~~

## 7. N6 — exact PARTIAL semantics

Q1:

~~~text
x_0=0
x_1=1
status:
  SIMULATION_ESTABLISHED
~~~

Q2:

~~~text
required state class:
  y>=0

y_0=1
y_1=-1

generated required slice:
  STATIC_SLICE_NONCONFORMANT

status:
  SIMULATION_NOT_ESTABLISHED
~~~

Both obligations are independently required and evaluable.

No obligation is blocked, conflicting, underdetermined, or out of scope.

Therefore:

~~~text
SIMULATION_TASK_TERMINAL:
  SIMULATION_TASK_PARTIAL

SIMULATION_PROTOCOL_CONFORMANCE:
  SIMULATION_PROTOCOL_CONFORMANT
~~~

PARTIAL is not used as an atomic-failure rescue.

## 8. N7 — evaluable numerical adequacy failure

Frozen acceptance:

~~~text
required end-to-end absolute error:
  <=0.01

certified bound:
  <=0.05
~~~

All claim-relevant error metadata are available, but the bound is insufficient for the requested threshold.

Result:

~~~text
NUMERICAL_ACCEPTANCE_STATUS:
  not established for requested threshold

SIMULATION_PRIMARY_STATUS:
  SIMULATION_NOT_ESTABLISHED

SIMULATION_TASK_TERMINAL:
  SIMULATION_TASK_NOT_ESTABLISHED

SIMULATION_PROTOCOL_CONFORMANCE:
  SIMULATION_PROTOCOL_CONFORMANT
~~~

This is evaluable numerical inadequacy, not blocked execution.

## 9. N8 — terminal precedence with lower-level retention

Frozen subordinate states:

~~~text
Q1:
  SIMULATION_OUT_OF_SCOPE

Q2:
  SIMULATION_CONFLICTING

Q3:
  SIMULATION_UNDERDETERMINED

Q4:
  SIMULATION_BLOCKED
~~~

Applying the frozen precedence:

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

gives:

~~~text
SIMULATION_TASK_TERMINAL:
  SIMULATION_TASK_OUT_OF_SCOPE
~~~

Lower states remain visible:

~~~text
LOWER_LEVEL_Q2_RETAINED:
  yes

LOWER_LEVEL_Q3_RETAINED:
  yes

LOWER_LEVEL_Q4_RETAINED:
  yes
~~~

Protocol conformance remains:

~~~text
SIMULATION_PROTOCOL_CONFORMANCE:
  SIMULATION_PROTOCOL_CONFORMANT
~~~

## 10. Coverage result

SIM-CH-001 directly exercised `SIMULATION_ESTABLISHED`.

SIM-CH-002 directly exercised:

~~~text
SIMULATION_NOT_ESTABLISHED
SIMULATION_BLOCKED
SIMULATION_CONFLICTING
SIMULATION_OUT_OF_SCOPE
SIMULATION_UNDERDETERMINED
~~~

Therefore:

~~~text
ALL_SIX_SIMULATION_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  yes
~~~

Across SIM-CH-001 and SIM-CH-002 the task terminals directly exercised are:

~~~text
SIMULATION_TASK_ESTABLISHED
SIMULATION_TASK_PARTIAL
SIMULATION_TASK_NOT_ESTABLISHED
SIMULATION_TASK_BLOCKED
SIMULATION_TASK_CONFLICTING
SIMULATION_TASK_OUT_OF_SCOPE
SIMULATION_TASK_UNDERDETERMINED
~~~

Therefore:

~~~text
ALL_SEVEN_SIMULATION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes
~~~

## 11. Method-gain state

~~~text
SIMULATION_METHOD_GAIN_STATUS:
  SIMULATION_GAIN_NOT_TESTED
~~~

No baseline or NO_GAIN counter changes.

## 12. Frozen-score execution

~~~text
N1-1..N1-10: 10/10 PASS
N2-1..N2-10: 10/10 PASS
N3-1..N3-10: 10/10 PASS
N4-1..N4-10: 10/10 PASS
N5-1..N5-10: 10/10 PASS
N6-1..N6-10: 10/10 PASS
N7-1..N7-10: 10/10 PASS
N8-1..N8-10: 10/10 PASS

TOTAL_REQUIRED_CHECKS:
  80

PASSED:
  80

FAILED:
  0
~~~

## 13. Post-challenge state

~~~text
DIRECT_SIMULATION_PILOTS_ATTEMPTED:
  2

SUCCESSFUL_DIRECT_SIMULATION_PILOTS:
  2

POSITIVE_SIMULATION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_SIMULATION_CASES:
  1

ALL_SIX_SIMULATION_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  yes

ALL_SEVEN_SIMULATION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes

METHOD_BOUNDARY_SIMULATION_CASES:
  0

BASELINE_SIMULATION_CASES:
  0

NO_GAIN_SIMULATION_CASES:
  0

REPRODUCIBILITY_CASES:
  0

EXTERNAL_SIMULATION_APPLICATIONS:
  0

INDEPENDENT_SIMULATION_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established

SIMULATION_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_SIMULATION_EVIDENCE_STATUS:
  validation_in_progress

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 14. Maximum-supported conclusion

Simulation Protocol v0.1 has now directly exercised all six primary status classes and all seven task-terminal classes on frozen constructed evidence.

This establishes internal terminal discrimination and negative-path handling only.

It does not establish external model validity, predictive accuracy, independent replication, universal simulation correctness, or method gain.

## 15. Next

Prospectively precommit and execute:

~~~text
SIM-CH-003
direct neighboring-method boundary challenge
~~~
