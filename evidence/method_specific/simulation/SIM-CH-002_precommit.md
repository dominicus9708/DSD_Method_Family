# SIM-CH-002 — Negative / Terminal-Coverage Simulation Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-05**  
Challenge ID: `SIM-CH-002`  
Method: **Simulation / DSD 시뮬레이션론**  
Protocol: **Simulation Protocol v0.1**  
Case class: `negative_unresolved_terminal_coverage_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen protocol identity

~~~text
PROTOCOL_COMMIT:
  ea271d04eb09d252299d9420d0fb1191564f5bc6

PROTOCOL_BLOB:
  c3d6f80d99dabb5b84c7a60fd2df3f58bf9dba35

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  S1-S18
~~~

The protocol is immutable for this challenge.

## 2. Challenge purpose

Directly exercise the remaining Simulation primary-status and task-terminal paths and verify lower-level state retention.

Frozen subcases:

~~~text
N1 known inadmissible initial state -> NOT_ESTABLISHED
N2 unavailable required evolution law -> BLOCKED
N3 incompatible applicable evolution laws -> CONFLICTING
N4 future external-target truth request -> OUT_OF_SCOPE
N5 multiple admissible unresolved model semantics -> UNDERDETERMINED
N6 independent ESTABLISHED + evaluably NOT_ESTABLISHED -> PARTIAL
N7 evaluable numerical adequacy failure -> NOT_ESTABLISHED
N8 precedence bundle:
   OUT_OF_SCOPE + CONFLICTING + UNDERDETERMINED + BLOCKED
   -> OUT_OF_SCOPE with lower states retained
~~~

Together with SIM-CH-001, the intended coverage is all six primary Simulation statuses and all seven Simulation task terminals.

No subcase assesses method gain.

## 3. Challenge locks

~~~text
CHALLENGE_ID:
  SIM-CH-002

CHALLENGE_VERSION:
  1

METHOD_GAIN_ASSESSMENT:
  not_requested

COMPARATOR:
  not_requested

POST_HOC_REPAIR:
  prohibited
~~~

## 4. N1 — known inadmissible initial state

Frozen task:

~~~text
TASK_ID:
  SIM-CH-002-N1

PRIMARY_CLAIM_LEVEL:
  DECLARED_TRAJECTORY_ON_FIXED_HORIZON

state class:
  x >= 0

initial state:
  x_0=-1

initial-state admissibility:
  evaluable
~~~

The initial state is known to violate the frozen state class.

Expected:

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

No trajectory execution is allowed to repair the invalid initial state.

Guard:

~~~text
KNOWN_INADMISSIBLE != BLOCKED
SOLVER_ACCEPTS_VECTOR != STATE_ADMISSIBLE
~~~

## 5. N2 — unavailable required evolution law

Frozen task:

~~~text
TASK_ID:
  SIM-CH-002-N2

initial state:
  admissible

horizon:
  n=0..3

required evolution interface:
  LAW-N2-v1

law status:
  EVOLUTION_LAW_UNAVAILABLE
~~~

Expected:

~~~text
no zero-dynamics default
no constant-trajectory substitution

SIMULATION_PRIMARY_STATUS:
  SIMULATION_BLOCKED

SIMULATION_TASK_TERMINAL:
  SIMULATION_TASK_BLOCKED

SIMULATION_PROTOCOL_CONFORMANCE:
  SIMULATION_PROTOCOL_CONFORMANT
~~~

Guard:

~~~text
MISSING_EVOLUTION_LAW != ZERO_DYNAMICS
BLOCKED != MODEL_NO_TRAJECTORY
~~~

## 6. N3 — conflicting applicable evolution laws

Frozen task:

~~~text
TASK_ID:
  SIM-CH-002-N3

model identity/version:
  MODEL-N3-v1

initial state:
  x_0=1

law record L1:
  x_(n+1)=x_n+1
  applicable=yes

law record L2:
  x_(n+1)=x_n-1
  applicable=yes

precedence resolver:
  none
~~~

The two applicable records generate materially different trajectories.

Expected:

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

No law may be chosen arbitrarily.

## 7. N4 — Prediction request outside Simulation

Frozen request:

~~~text
TASK_ID:
  SIM-CH-002-N4

model trajectory:
  supplied/generated and internally consistent

requested claim:
  establish that the external real-world state
  will equal the model state at future time T

empirical/domain validation interface:
  not part of Simulation task
~~~

Expected:

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

Guard:

~~~text
MODEL_CONSISTENT_FUTURE_STATE != FUTURE_WORLD_TRUTH
OUT_OF_SCOPE != NOT_ESTABLISHED
~~~

## 8. N5 — underdetermined model semantics

Frozen task:

~~~text
TASK_ID:
  SIM-CH-002-N5

initial state:
  x_0=0

horizon:
  one step

two admissible model semantics:
  M-A: x_1=1
  M-B: x_1=2

both:
  admissible under frozen metadata

model-semantics resolver:
  none

declared branching relation:
  none
~~~

Expected:

~~~text
SIMULATION_PRIMARY_STATUS:
  SIMULATION_UNDERDETERMINED

SIMULATION_TASK_TERMINAL:
  SIMULATION_TASK_UNDERDETERMINED

SIMULATION_PROTOCOL_CONFORMANCE:
  SIMULATION_PROTOCOL_CONFORMANT
~~~

Guard:

~~~text
MULTIPLE_ADMISSIBLE_UNRESOLVED_MODEL_SEMANTICS
  !=
DECLARED_BRANCHING_MODEL
~~~

## 9. N6 — exact PARTIAL semantics

Frozen task contains two independently required in-scope Simulation obligations.

Q1:

~~~text
model:
  x_(n+1)=x_n+1

initial:
  x_0=0

horizon:
  n=0..1

requested:
  generate trajectory

result:
  {0,1}

status:
  SIMULATION_ESTABLISHED
~~~

Q2:

~~~text
state class:
  y>=0

initial:
  y_0=1

evolution:
  y_1=-1

requested:
  trajectory whose required generated slice remains
  valid in the frozen state class

all interfaces:
  available

generated required slice:
  known nonconformant

status:
  SIMULATION_NOT_ESTABLISHED
~~~

No obligation is blocked, conflicting, underdetermined, or out of scope.

Expected:

~~~text
SIMULATION_TASK_TERMINAL:
  SIMULATION_TASK_PARTIAL

SIMULATION_PROTOCOL_CONFORMANCE:
  SIMULATION_PROTOCOL_CONFORMANT
~~~

Guard:

~~~text
PARTIAL != BLOCKED_WITH_SOME_SUCCESS
PARTIAL != ATOMIC_FAILURE_RELABELED
~~~

## 10. N7 — evaluable numerical adequacy failure

Frozen task:

~~~text
TASK_ID:
  SIM-CH-002-N7

PRIMARY_CLAIM_LEVEL:
  APPROXIMATE_TRAJECTORY_WITH_DECLARED_ERROR

requested acceptance:
  end-to-end absolute error <= 0.01

numerical result:
  supplied

certified end-to-end error bound:
  <= 0.05

all required error metadata:
  available
~~~

The certified bound is insufficient for the requested acceptance threshold.

Expected:

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

Guard:

~~~text
EVALUABLE_NUMERICAL_INADEQUACY != BLOCKED
SOLVER_TERMINATED != TRAJECTORY_ACCEPTED
~~~

## 11. N8 — terminal precedence with lower-level retention

Frozen task contains four independently required obligations.

Q1:

~~~text
request:
  external future-world truth claim

status:
  SIMULATION_OUT_OF_SCOPE
~~~

Q2:

~~~text
two incompatible applicable evolution laws
no resolver

status:
  SIMULATION_CONFLICTING
~~~

Q3:

~~~text
two admissible unresolved model semantics
different trajectory results
no resolver

status:
  SIMULATION_UNDERDETERMINED
~~~

Q4:

~~~text
required transition relation:
  unavailable

status:
  SIMULATION_BLOCKED
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
SIMULATION_TASK_TERMINAL:
  SIMULATION_TASK_OUT_OF_SCOPE

LOWER_LEVEL_Q2_RETAINED:
  yes

LOWER_LEVEL_Q3_RETAINED:
  yes

LOWER_LEVEL_Q4_RETAINED:
  yes

SIMULATION_PROTOCOL_CONFORMANCE:
  SIMULATION_PROTOCOL_CONFORMANT
~~~

## 12. Challenge-level expected result

~~~text
N1:
  SIMULATION_TASK_NOT_ESTABLISHED

N2:
  SIMULATION_TASK_BLOCKED

N3:
  SIMULATION_TASK_CONFLICTING

N4:
  SIMULATION_TASK_OUT_OF_SCOPE

N5:
  SIMULATION_TASK_UNDERDETERMINED

N6:
  SIMULATION_TASK_PARTIAL

N7:
  SIMULATION_TASK_NOT_ESTABLISHED

N8:
  SIMULATION_TASK_OUT_OF_SCOPE
  with CONFLICTING / UNDERDETERMINED / BLOCKED lower states retained

SIMULATION_METHOD_GAIN_STATUS:
  SIMULATION_GAIN_NOT_TESTED

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

Together with SIM-CH-001:

~~~text
ALL_SIX_SIMULATION_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  expected yes

ALL_SEVEN_SIMULATION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  expected yes
~~~

## 13. Frozen scoring — 80 checks

Each subcase has ten frozen checks.

### N1

~~~text
N1-1 state class frozen
N1-2 initial value -1 frozen
N1-3 admissibility evaluable
N1-4 initial state known inadmissible
N1-5 no solver-repair allowed
N1-6 no BLOCKED relabel
N1-7 primary NOT_ESTABLISHED
N1-8 terminal NOT_ESTABLISHED
N1-9 no trajectory-success fabrication
N1-10 protocol CONFORMANT
~~~

### N2

~~~text
N2-1 task/horizon frozen
N2-2 LAW-N2-v1 required
N2-3 law unavailable
N2-4 no zero-dynamics default
N2-5 no constant-trajectory substitution
N2-6 no model-no-trajectory inference
N2-7 primary BLOCKED
N2-8 terminal BLOCKED
N2-9 lower unavailable state retained
N2-10 protocol CONFORMANT
~~~

### N3

~~~text
N3-1 model version frozen
N3-2 L1 applicable
N3-3 L2 applicable
N3-4 L1/L2 outputs differ
N3-5 no resolver
N3-6 no arbitrary law selection
N3-7 primary CONFLICTING
N3-8 terminal CONFLICTING
N3-9 conflicting records retained
N3-10 protocol CONFORMANT
~~~

### N4

~~~text
N4-1 model trajectory available
N4-2 requested claim is future external truth
N4-3 Prediction handoff required
N4-4 no empirical truth fabricated
N4-5 Simulation success not Prediction success
N4-6 request not reinterpreted as trajectory failure
N4-7 primary OUT_OF_SCOPE
N4-8 terminal OUT_OF_SCOPE
N4-9 bounded handoff retained
N4-10 protocol CONFORMANT
~~~

### N5

~~~text
N5-1 initial state frozen
N5-2 M-A admissible
N5-3 M-B admissible
N5-4 results differ
N5-5 no resolver
N5-6 not a declared branching relation
N5-7 primary UNDERDETERMINED
N5-8 terminal UNDERDETERMINED
N5-9 no arbitrary semantic choice
N5-10 protocol CONFORMANT
~~~

### N6

~~~text
N6-1 two independent required obligations frozen
N6-2 Q1 evaluable
N6-3 Q1 ESTABLISHED
N6-4 Q2 evaluable
N6-5 Q2 required slice NONCONFORMANT
N6-6 Q2 NOT_ESTABLISHED
N6-7 no higher-priority status
N6-8 terminal PARTIAL
N6-9 PARTIAL not atomic-failure rescue
N6-10 protocol CONFORMANT
~~~

### N7

~~~text
N7-1 acceptance threshold frozen
N7-2 certified bound 0.05 frozen
N7-3 bound exceeds threshold 0.01
N7-4 all error metadata available
N7-5 numerical adequacy evaluable
N7-6 acceptance not established
N7-7 primary NOT_ESTABLISHED
N7-8 terminal NOT_ESTABLISHED
N7-9 not relabeled BLOCKED
N7-10 protocol CONFORMANT
~~~

### N8

~~~text
N8-1 Q1 OUT_OF_SCOPE retained
N8-2 Q2 CONFLICTING retained
N8-3 Q3 UNDERDETERMINED retained
N8-4 Q4 BLOCKED retained
N8-5 frozen precedence applied
N8-6 terminal OUT_OF_SCOPE
N8-7 Q2 remains visible
N8-8 Q3 remains visible
N8-9 Q4 remains visible
N8-10 protocol CONFORMANT
~~~

~~~text
TOTAL_REQUIRED_CHECKS:
  80

PASS_THRESHOLD:
  80/80

PARTIAL_PASS_ALLOWED:
  no
~~~

## 14. Counter rule on full PASS

If all 80 checks pass:

~~~text
DIRECT_SIMULATION_PILOTS_ATTEMPTED:
  1 -> 2

SUCCESSFUL_DIRECT_SIMULATION_PILOTS:
  1 -> 2

NEGATIVE_OR_UNRESOLVED_SIMULATION_CASES:
  0 -> 1

ALL_SIX_SIMULATION_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  yes

ALL_SEVEN_SIMULATION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes
~~~

Do not change baseline, NO_GAIN, reproducibility, external, or independent-validation counters.

## 15. Next on full PASS

Proceed to:

~~~text
SIM-CH-003
direct neighboring-method boundary challenge
~~~
