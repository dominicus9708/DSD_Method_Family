# OPT-CH-002 — Negative / Terminal-Coverage Optimization Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-05**  
Challenge ID: `OPT-CH-002`  
Method: **Optimization / DSD 최적화론**  
Protocol: **Optimization Protocol v0.1**  
Case class: `negative_unresolved_terminal_coverage_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen protocol identity

~~~text
PROTOCOL_COMMIT:
  34584acd54af1bafef7dd176f795ed914eddc6b2

PROTOCOL_BLOB:
  5d2f9e37eab08bba27b0f416599df2e74a8c0c42

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  O1-O18
~~~

The protocol is immutable for this challenge.

No protocol rule may be edited in response to the result.

## 2. Challenge purpose

Directly exercise the remaining Optimization primary-status and task-terminal paths while preserving lower-level candidate, objective, constraint, interface, reduction, and handoff states.

The bundle contains eight prospectively frozen subcases:

~~~text
N1  evaluable false unique-optimum claim -> NOT_ESTABLISHED

N2  unavailable required lifecycle objective component -> BLOCKED

N3  incompatible applicable objective semantics -> CONFLICTING

N4  state-dependent intervention-policy request -> OUT_OF_SCOPE

N5  multiple admissible multi-objective selection semantics
    with different selections -> UNDERDETERMINED

N6  mixed independent required optimization obligations
    -> PARTIAL

N7  evaluable reduction that does not preserve the declared
    selection relation -> NOT_ESTABLISHED

N8  terminal-precedence bundle:
    OUT_OF_SCOPE + CONFLICTING + UNDERDETERMINED + BLOCKED
    -> OUT_OF_SCOPE with lower states retained
~~~

Together with OPT-CH-001, the intended coverage is all six Optimization primary statuses and all seven Optimization task terminals.

No subcase assesses method gain.

## 3. Frozen challenge-level locks

~~~text
CHALLENGE_ID:
  OPT-CH-002

CHALLENGE_VERSION:
  1

SUBCASES:
  OPT-CH-002-N1
  OPT-CH-002-N2
  OPT-CH-002-N3
  OPT-CH-002-N4
  OPT-CH-002-N5
  OPT-CH-002-N6
  OPT-CH-002-N7
  OPT-CH-002-N8

METHOD_GAIN_ASSESSMENT:
  not_requested

COMPARATOR:
  not_requested

POST_HOC_REPAIR:
  prohibited
~~~

## 4. N1 — evaluable false unique-optimum claim

Frozen task:

~~~text
TASK_ID:
  OPT-CH-002-N1

PRIMARY_CLAIM_LEVEL:
  OPTIMAL_CANDIDATE_OR_TIED_SET

requested claim:
  candidate a is the unique optimum

candidate set:
  {a,b,c}

all candidates:
  admissible

objective:
  minimize cost

cost(a):
  7

cost(b):
  4

cost(c):
  9
~~~

All required interfaces are available and coherent.

Expected:

~~~text
true unique optimum:
  b

requested claim "a is unique optimum":
  false

OPTIMIZATION_PRIMARY_STATUS:
  OPTIMIZATION_NOT_ESTABLISHED

OPTIMIZATION_TASK_TERMINAL:
  OPTIMIZATION_TASK_NOT_ESTABLISHED

OPTIMIZATION_PROTOCOL_CONFORMANCE:
  OPTIMIZATION_PROTOCOL_CONFORMANT
~~~

Guards:

~~~text
EVALUABLE_FALSE_CLAIM != BLOCKED
NOT_ESTABLISHED != UNDERDETERMINED
~~~

## 5. N2 — unavailable required lifecycle objective component

Frozen task:

~~~text
TASK_ID:
  OPT-CH-002-N2

PRIMARY_CLAIM_LEVEL:
  OPTIMAL_CANDIDATE_OR_TIED_SET

candidate set:
  {p,q}

objective:
  minimize total lifecycle cost

required objective components:
  build
  operate
  disposal

build / operate:
  available for p and q

disposal:
  required
  unavailable for q

OBJECTIVE_COMPONENT_COMPLETENESS_STATUS:
  incomplete

REQUIRED_OPTIMIZATION_INTERFACE_STATUS:
  REQUIRED_OPTIMIZATION_INTERFACE_UNAVAILABLE
~~~

No rule licenses omission of the disposal component.

Expected:

~~~text
q lifecycle objective:
  blocked

OPTIMIZATION_PRIMARY_STATUS:
  OPTIMIZATION_BLOCKED

OPTIMIZATION_TASK_TERMINAL:
  OPTIMIZATION_TASK_BLOCKED

OPTIMIZATION_PROTOCOL_CONFORMANCE:
  OPTIMIZATION_PROTOCOL_CONFORMANT
~~~

Guards:

~~~text
MISSING_REQUIRED_OBJECTIVE_COMPONENT
  !=
OBJECTIVE_COMPONENT_IRRELEVANT

BLOCKED
  !=
INFEASIBLE

UNAVAILABLE_REQUIRED_INTERFACE
  !=
NOT_ESTABLISHED
~~~

## 6. N3 — conflicting objective semantics

Frozen task:

~~~text
TASK_ID:
  OPT-CH-002-N3

PRIMARY_CLAIM_LEVEL:
  OPTIMAL_CANDIDATE_OR_TIED_SET

candidate set:
  {x,y}

objective identity:
  O-N3-v1

applicable objective record R1:
  direction = minimize
  value(x)=2
  value(y)=8

applicable objective record R2:
  direction = maximize
  value(x)=2
  value(y)=8

both records:
  same frozen objective identity/version
  applicable
  no precedence resolver
~~~

R1 selects x.

R2 selects y.

Expected:

~~~text
OBJECTIVE_INTERFACE:
  conflicting

OPTIMIZATION_PRIMARY_STATUS:
  OPTIMIZATION_CONFLICTING

OPTIMIZATION_TASK_TERMINAL:
  OPTIMIZATION_TASK_CONFLICTING

OPTIMIZATION_PROTOCOL_CONFORMANCE:
  OPTIMIZATION_PROTOCOL_CONFORMANT
~~~

Guard:

~~~text
CONFLICTING_APPLICABLE_OBJECTIVE_SEMANTICS
  !=
LICENSE_TO_PICK_ONE
~~~

## 7. N4 — Control request outside Optimization

Frozen request:

~~~text
TASK_ID:
  OPT-CH-002-N4

current state:
  s0

available actions at s0:
  {a1,a2}

one-step objective and values:
  fully supplied

requested output:
  a state-dependent intervention policy
  for all future reachable states
~~~

The supplied task does not contain a frozen state-transition/policy interface sufficient to turn a one-time Optimization selection into Control.

Expected:

~~~text
CONTROL_HANDOFF:
  required

OPTIMIZATION_PRIMARY_STATUS:
  OPTIMIZATION_OUT_OF_SCOPE

OPTIMIZATION_TASK_TERMINAL:
  OPTIMIZATION_TASK_OUT_OF_SCOPE

OPTIMIZATION_PROTOCOL_CONFORMANCE:
  OPTIMIZATION_PROTOCOL_CONFORMANT
~~~

Guards:

~~~text
ONE_TIME_OPTIMUM != CONTROL_POLICY
OUT_OF_SCOPE != NOT_ESTABLISHED
~~~

## 8. N5 — underdetermined multi-objective selection semantics

Frozen task:

~~~text
TASK_ID:
  OPT-CH-002-N5

PRIMARY_CLAIM_LEVEL:
  OPTIMAL_CANDIDATE_OR_TIED_SET

candidate set:
  {m,n}

objectives:
  minimize cost
  minimize emissions

values:
  m = (cost 3, emissions 9)
  n = (cost 8, emissions 2)
~~~

Two selection semantics are both admissible under the frozen metadata:

~~~text
S1:
  lexicographic cost first
  -> m

S2:
  lexicographic emissions first
  -> n

selection-semantics resolver:
  none
~~~

Expected:

~~~text
OPTIMIZATION_PRIMARY_STATUS:
  OPTIMIZATION_UNDERDETERMINED

OPTIMIZATION_TASK_TERMINAL:
  OPTIMIZATION_TASK_UNDERDETERMINED

OPTIMIZATION_PROTOCOL_CONFORMANCE:
  OPTIMIZATION_PROTOCOL_CONFORMANT
~~~

Guards:

~~~text
MULTIPLE_ADMISSIBLE_SELECTION_SEMANTICS_WITH_DIFFERENT_SELECTIONS
  !=
CONFLICTING_RECORDS_ABOUT_ONE_FROZEN_RULE

UNDERDETERMINED
  !=
PARETO_INCOMPARABLE
~~~

## 9. N6 — exact PARTIAL semantics

Frozen task contains two independently required in-scope Optimization obligations.

~~~text
TASK_ID:
  OPT-CH-002-N6
~~~

Q1:

~~~text
candidate set:
  {u,v}

objective:
  minimize cost

cost(u)=2
cost(v)=5

requested claim:
  identify the optimum

result:
  u

status:
  OPTIMIZATION_ESTABLISHED
~~~

Q2:

~~~text
candidate set:
  {r,s}

objective:
  minimize cost

cost(r)=7
cost(s)=3

requested claim:
  r is the unique optimum

all interfaces:
  available and coherent

result:
  requested claim false

status:
  OPTIMIZATION_NOT_ESTABLISHED
~~~

No required obligation is blocked, conflicting, underdetermined, or out of scope.

Expected:

~~~text
Q1:
  ESTABLISHED

Q2:
  NOT_ESTABLISHED

OPTIMIZATION_TASK_TERMINAL:
  OPTIMIZATION_TASK_PARTIAL

OPTIMIZATION_PROTOCOL_CONFORMANCE:
  OPTIMIZATION_PROTOCOL_CONFORMANT
~~~

Guards:

~~~text
PARTIAL != BLOCKED_WITH_SOME_SUCCESS
PARTIAL != ATOMIC_FAILURE_RELABELED
PARTIAL requires multiple independently required obligations
~~~

## 10. N7 — evaluable reduction not preserving selection relation

Frozen task:

~~~text
TASK_ID:
  OPT-CH-002-N7

PRIMARY_CLAIM_LEVEL:
  OPTIMAL_CANDIDATE_OR_TIED_SET

candidate set:
  {c1,c2}

true declared objective:
  minimize source-level loss

source-level loss:
  c1 = 4.4
  c2 = 4.6

required selection claim:
  identify unique optimum

reduced readout:
  R(value) = round to nearest integer

R(c1):
  4

R(c2):
  5
~~~

A second claim-relevant source perturbation within the frozen allowed reduction cell is supplied:

~~~text
c1' = 4.49 -> R=4
c2' = 4.41 -> R=4
~~~

The reduction is therefore not licensed as a general order-preserving interface for the declared source-level selection relation.

The preservation question is fully evaluable.

Expected:

~~~text
SELECTION_PRESERVATION_STATUS:
  SELECTION_RELATION_NOT_PRESERVED

requested reduced-readout-based unique-optimum claim:
  not established

OPTIMIZATION_PRIMARY_STATUS:
  OPTIMIZATION_NOT_ESTABLISHED

OPTIMIZATION_TASK_TERMINAL:
  OPTIMIZATION_TASK_NOT_ESTABLISHED

OPTIMIZATION_PROTOCOL_CONFORMANCE:
  OPTIMIZATION_PROTOCOL_CONFORMANT
~~~

Guards:

~~~text
GENERIC_LOW_ERROR != SELECTION_ORDER_PRESERVATION
EQUAL_OR_COARSE_REDUCED_READOUT != SOURCE_ORDER
EVALUABLE_NONPRESERVATION != BLOCKED
~~~

## 11. N8 — frozen terminal precedence with lower-level retention

Frozen task contains four independently required obligations.

~~~text
TASK_ID:
  OPT-CH-002-N8
~~~

Q1:

~~~text
requested output:
  full future-state Control policy

status:
  OPTIMIZATION_OUT_OF_SCOPE
~~~

Q2:

~~~text
same objective identity/version
two incompatible applicable directions
no resolver

status:
  OPTIMIZATION_CONFLICTING
~~~

Q3:

~~~text
two admissible multi-objective selection semantics
different selections
no resolver

status:
  OPTIMIZATION_UNDERDETERMINED
~~~

Q4:

~~~text
required objective component unavailable

status:
  OPTIMIZATION_BLOCKED
~~~

Frozen precedence:

~~~text
OPTIMIZATION_TASK_OUT_OF_SCOPE
>
OPTIMIZATION_TASK_CONFLICTING
>
OPTIMIZATION_TASK_UNDERDETERMINED
>
OPTIMIZATION_TASK_BLOCKED
>
OPTIMIZATION_TASK_ESTABLISHED /
OPTIMIZATION_TASK_PARTIAL /
OPTIMIZATION_TASK_NOT_ESTABLISHED
~~~

Expected:

~~~text
OPTIMIZATION_TASK_TERMINAL:
  OPTIMIZATION_TASK_OUT_OF_SCOPE

LOWER_LEVEL_Q2_RETAINED:
  yes

LOWER_LEVEL_Q3_RETAINED:
  yes

LOWER_LEVEL_Q4_RETAINED:
  yes

OPTIMIZATION_PROTOCOL_CONFORMANCE:
  OPTIMIZATION_PROTOCOL_CONFORMANT
~~~

No lower-level state may be erased by the task-terminal summary.

## 12. Challenge-level expected result

Every subcase is expected to be protocol-conformant.

~~~text
N1:
  OPTIMIZATION_TASK_NOT_ESTABLISHED

N2:
  OPTIMIZATION_TASK_BLOCKED

N3:
  OPTIMIZATION_TASK_CONFLICTING

N4:
  OPTIMIZATION_TASK_OUT_OF_SCOPE

N5:
  OPTIMIZATION_TASK_UNDERDETERMINED

N6:
  OPTIMIZATION_TASK_PARTIAL

N7:
  OPTIMIZATION_TASK_NOT_ESTABLISHED

N8:
  OPTIMIZATION_TASK_OUT_OF_SCOPE
  with CONFLICTING / UNDERDETERMINED / BLOCKED lower states retained

METHOD_GAIN_STATUS:
  OPTIMIZATION_GAIN_NOT_TESTED

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

Together with OPT-CH-001:

~~~text
ALL_SIX_OPTIMIZATION_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  expected yes

ALL_SEVEN_OPTIMIZATION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  expected yes
~~~

## 13. Frozen scoring — 80 checks

Each subcase has ten frozen checks.

### N1 — 10 checks

~~~text
N1-1 candidate set frozen
N1-2 objective frozen
N1-3 all candidates admissible
N1-4 costs 7/4/9 retained
N1-5 true optimum b
N1-6 requested claim about a false
N1-7 primary NOT_ESTABLISHED
N1-8 terminal NOT_ESTABLISHED
N1-9 not relabeled BLOCKED/UNDERDETERMINED
N1-10 protocol CONFORMANT
~~~

### N2 — 10 checks

~~~text
N2-1 lifecycle objective frozen
N2-2 build component required
N2-3 operate component required
N2-4 disposal component required
N2-5 q disposal unavailable
N2-6 no irrelevance fabricated
N2-7 primary BLOCKED
N2-8 terminal BLOCKED
N2-9 q not relabeled infeasible
N2-10 protocol CONFORMANT
~~~

### N3 — 10 checks

~~~text
N3-1 objective identity/version frozen
N3-2 R1 applicable
N3-3 R2 applicable
N3-4 R1 direction minimize
N3-5 R2 direction maximize
N3-6 selections differ
N3-7 no resolver
N3-8 primary CONFLICTING
N3-9 terminal CONFLICTING
N3-10 protocol CONFORMANT
~~~

### N4 — 10 checks

~~~text
N4-1 one-step candidates supplied
N4-2 one-step objective supplied
N4-3 requested output is future-state policy
N4-4 one-time optimum not promoted to Control
N4-5 Control handoff required
N4-6 no fabricated policy
N4-7 primary OUT_OF_SCOPE
N4-8 terminal OUT_OF_SCOPE
N4-9 not relabeled NOT_ESTABLISHED
N4-10 protocol CONFORMANT
~~~

### N5 — 10 checks

~~~text
N5-1 candidate set frozen
N5-2 two objectives frozen
N5-3 values retained
N5-4 S1 admissible
N5-5 S2 admissible
N5-6 S1/S2 selections differ
N5-7 no resolver
N5-8 primary UNDERDETERMINED
N5-9 terminal UNDERDETERMINED
N5-10 protocol CONFORMANT
~~~

### N6 — 10 checks

~~~text
N6-1 two independent required obligations frozen
N6-2 Q1 evaluable
N6-3 Q1 ESTABLISHED
N6-4 Q2 evaluable
N6-5 Q2 NOT_ESTABLISHED
N6-6 no BLOCKED obligation
N6-7 no higher-priority terminal
N6-8 terminal PARTIAL
N6-9 PARTIAL not used for atomic failure
N6-10 protocol CONFORMANT
~~~

### N7 — 10 checks

~~~text
N7-1 source-level objective frozen
N7-2 reduction rule frozen
N7-3 source values retained
N7-4 reduced values retained
N7-5 perturbation witness retained
N7-6 order-preservation failure evaluable
N7-7 preservation NOT_PRESERVED
N7-8 primary NOT_ESTABLISHED
N7-9 terminal NOT_ESTABLISHED
N7-10 protocol CONFORMANT
~~~

### N8 — 10 checks

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
DIRECT_OPTIMIZATION_PILOTS_ATTEMPTED:
  1 -> 2

SUCCESSFUL_DIRECT_OPTIMIZATION_PILOTS:
  1 -> 2

NEGATIVE_OR_UNRESOLVED_OPTIMIZATION_CASES:
  0 -> 1

ALL_SIX_OPTIMIZATION_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  yes

ALL_SEVEN_OPTIMIZATION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes
~~~

Do not change baseline, NO_GAIN, reproducibility, external, or independent-validation counters.

## 15. Next on full PASS

If all 80 checks pass, the next canonical step is:

~~~text
OPT-CH-003
direct neighboring-method boundary challenge
~~~
