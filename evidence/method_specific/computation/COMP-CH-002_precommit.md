# COMP-CH-002 — Negative / Unresolved-Terminal Computation Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-04**  
Challenge ID: `COMP-CH-002`  
Method: **Computation / DSD 계산론**  
Protocol: **Computation Protocol v0.1**  
Case class: `negative_unresolved_terminal_coverage_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen protocol identity

~~~text
PROTOCOL_COMMIT:
  03b1b7463af6d3a34dc3693a19933e83a3917b4d

PROTOCOL_BLOB:
  4c4fe0b0616371b7df6aff9ce6a1ff7636c49da4

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  T1-T18
~~~

The protocol is immutable for this challenge.

No protocol rule may be edited in response to the result.

## 2. Challenge purpose

Directly exercise the remaining Computation task-terminal paths and verify that lower-level obligation/action/interface statuses remain visible beneath the selected task terminal.

The bundle contains eight prospectively frozen subcases:

~~~text
N1  evaluable resolution failure -> NOT_ESTABLISHED

N2  unavailable required dependency interface -> BLOCKED

N3  incompatible applicable reuse records -> CONFLICTING

N4  objective-based plan selection request -> OUT_OF_SCOPE

N5  multiple admissible dependency semantics -> UNDERDETERMINED

N6  mixed independent required obligations -> PARTIAL

N7  symbolic coverage partial with evaluable uncovered failure
    -> NOT_ESTABLISHED

N8  terminal-precedence bundle:
    OUT_OF_SCOPE + CONFLICTING + UNDERDETERMINED + BLOCKED
    -> OUT_OF_SCOPE with lower states retained
~~~

Together with COMP-CH-001, the intended coverage is all seven Computation task terminals.

No subcase assesses method gain.

## 3. Frozen challenge-level locks

~~~text
CHALLENGE_ID:
  COMP-CH-002

CHALLENGE_VERSION:
  1

SUBCASES:
  COMP-CH-002-N1
  COMP-CH-002-N2
  COMP-CH-002-N3
  COMP-CH-002-N4
  COMP-CH-002-N5
  COMP-CH-002-N6
  COMP-CH-002-N7
  COMP-CH-002-N8

METHOD_GAIN_ASSESSMENT:
  not_requested

COMPARATOR:
  not_requested

POST_HOC_REPAIR:
  prohibited
~~~

## 4. N1 — evaluable insufficient resolution

Frozen task:

~~~text
TASK_ID:
  COMP-CH-002-N1

PRIMARY_CLAIM_LEVEL:
  SUFFICIENT_RESOLUTION_FOR_DECLARED_TARGET

target:
  determine whether s > 10

readout:
  r = 10

error bound:
  |s-r| <= 1

admissible interval:
  9 <= s <= 11

all required resolution metadata:
  available
~~~

The interval crosses threshold 10.

Expected:

~~~text
RESOLUTION_STATUS:
  RESOLUTION_NOT_SUFFICIENT

COMPUTATION_PRIMARY_STATUS:
  COMPUTATION_NOT_ESTABLISHED

COMPUTATION_TASK_TERMINAL:
  COMPUTATION_TASK_NOT_ESTABLISHED

COMPUTATION_PROTOCOL_CONFORMANCE:
  COMPUTATION_PROTOCOL_CONFORMANT
~~~

Guards:

~~~text
EVALUABLE_INSUFFICIENCY != BLOCKED
RESOLUTION_NOT_SUFFICIENT != OUT_OF_SCOPE
~~~

## 5. N2 — blocked required dependency interface

Frozen task:

~~~text
TASK_ID:
  COMP-CH-002-N2

PRIMARY_CLAIM_LEVEL:
  COMPUTATION_PLAN_FOR_DECLARED_TARGET

target:
  Y = f(x) + g(x)

f(x):
  available

g(x):
  value definition available

required dependency relation
between upstream source z and g:
  unavailable

REQUIRED_COMPUTATION_INTERFACE_ID:
  DEP-N2-v1

REQUIRED_COMPUTATION_INTERFACE_STATUS:
  REQUIRED_COMPUTATION_INTERFACE_UNAVAILABLE
~~~

The primary plan cannot determine whether g is validly reusable, fresh-required, or invalidated without DEP-N2-v1.

Expected:

~~~text
g obligation:
  OBLIGATION_BLOCKED

g action:
  ACTION_BLOCKED

COMPUTATION_PRIMARY_STATUS:
  COMPUTATION_BLOCKED

COMPUTATION_TASK_TERMINAL:
  COMPUTATION_TASK_BLOCKED

COMPUTATION_PROTOCOL_CONFORMANCE:
  COMPUTATION_PROTOCOL_CONFORMANT
~~~

Guards:

~~~text
UNAVAILABLE_REQUIRED_INTERFACE != TARGET_IRRELEVANCE
BLOCKED != NOT_ESTABLISHED
MISSING_DEPENDENCY_RECORD != NEGATIVE_DEPENDENCY
~~~

## 6. N3 — conflicting reuse records

Frozen task:

~~~text
TASK_ID:
  COMP-CH-002-N3

PRIMARY_CLAIM_LEVEL:
  SCOPED_REUSE_PLAN

REUSE_INTERFACE_ID:
  REUSE-N3-v1

REUSE_KEY:
  q(2)

same model version:
  MODEL-N3-v1

same regime:
  REGIME-N3-v1

same status:
  defined / applicable
~~~

Two applicable records under the same frozen semantics:

~~~text
R1:
  cached value = 4
  valid = yes

R2:
  cached value = 5
  valid = yes

precedence resolver:
  none
~~~

Expected:

~~~text
REUSE_INTERFACE_COHERENCE_STATUS:
  REUSE_INTERFACE_CONFLICTING

reuse obligation:
  OBLIGATION_CONFLICTING

reuse action:
  ACTION_CONFLICTING

COMPUTATION_PRIMARY_STATUS:
  COMPUTATION_CONFLICTING

COMPUTATION_TASK_TERMINAL:
  COMPUTATION_TASK_CONFLICTING

COMPUTATION_PROTOCOL_CONFORMANCE:
  COMPUTATION_PROTOCOL_CONFORMANT
~~~

Guard:

~~~text
CONFLICTING_REUSE_RECORDS != LICENSE_TO_PICK_ONE_CACHE_VALUE
~~~

## 7. N4 — Optimization request outside Computation task

Frozen request:

~~~text
TASK_ID:
  COMP-CH-002-N4

declared sufficient plans:
  P1
  P2

both plans:
  sound for target

requested claim:
  select the plan minimizing runtime

objective function:
  runtime

candidate costs:
  supplied
~~~

This is explicit objective-based selection among sufficient plans.

Expected:

~~~text
OPTIMIZATION_HANDOFF:
  required

COMPUTATION_PRIMARY_STATUS:
  COMPUTATION_OUT_OF_SCOPE

COMPUTATION_TASK_TERMINAL:
  COMPUTATION_TASK_OUT_OF_SCOPE

COMPUTATION_PROTOCOL_CONFORMANCE:
  COMPUTATION_PROTOCOL_CONFORMANT
~~~

The task is not reinterpreted as a failed Computation plan.

Guards:

~~~text
SUFFICIENT_COMPUTATION_PLAN != OPTIMAL_PLAN
COMPUTATION != OPTIMIZATION
OUT_OF_SCOPE != NOT_ESTABLISHED
~~~

## 8. N5 — underdetermined dependency semantics

Frozen task:

~~~text
TASK_ID:
  COMP-CH-002-N5

PRIMARY_CLAIM_LEVEL:
  REQUIRED_EVALUATION_SET

target:
  Y
~~~

Two admissible dependency interfaces are supplied and no resolver exists.

~~~text
DEP-N5-A:
  u1 -> Y
  u2 has no path to Y

DEP-N5-B:
  u1 -> Y
  u2 -> u1

both:
  admissible under frozen metadata

resolver:
  none
~~~

Consequences:

~~~text
under DEP-N5-A:
  required set = {u1,Y}

under DEP-N5-B:
  required set = {u2,u1,Y}
~~~

Expected:

~~~text
u2 obligation:
  OBLIGATION_UNDERDETERMINED

u2 action:
  ACTION_UNDERDETERMINED

COMPUTATION_PRIMARY_STATUS:
  COMPUTATION_UNDERDETERMINED

COMPUTATION_TASK_TERMINAL:
  COMPUTATION_TASK_UNDERDETERMINED

COMPUTATION_PROTOCOL_CONFORMANCE:
  COMPUTATION_PROTOCOL_CONFORMANT
~~~

Guard:

~~~text
MULTIPLE_ADMISSIBLE_DEPENDENCY_SEMANTICS_WITH_DIFFERENT_PLANS
  !=
CONFLICTING_EVIDENCE_ABOUT_ONE_FROZEN_GRAPH
~~~

## 9. N6 — exact PARTIAL semantics

Frozen task contains two independently required in-scope obligations.

~~~text
TASK_ID:
  COMP-CH-002-N6

PRIMARY_CLAIM_LEVEL:
  COMPUTATION_PLAN_FOR_DECLARED_TARGET
~~~

Q1:

~~~text
target:
  A = 2 + 3

all interfaces:
  available

result:
  A = 5

status:
  COMPUTATION_ESTABLISHED
~~~

Q2:

~~~text
target:
  decide whether s > 10

readout:
  10

error bound:
  1

admissible interval:
  [9,11]

all interfaces:
  available

resolution result:
  RESOLUTION_NOT_SUFFICIENT

status:
  COMPUTATION_NOT_ESTABLISHED
~~~

No obligation is blocked, conflicting, underdetermined, or out of scope.

Expected:

~~~text
Q1:
  ESTABLISHED

Q2:
  NOT_ESTABLISHED

COMPUTATION_TASK_TERMINAL:
  COMPUTATION_TASK_PARTIAL

COMPUTATION_PROTOCOL_CONFORMANCE:
  COMPUTATION_PROTOCOL_CONFORMANT
~~~

Guards:

~~~text
PARTIAL != BLOCKED_WITH_SOME_SUCCESS
PARTIAL != ATOMIC_FAILURE_RELABELED
PARTIAL requires multiple independently required obligations
~~~

## 10. N7 — partial symbolic coverage with evaluable uncovered failure

Frozen task:

~~~text
TASK_ID:
  COMP-CH-002-N7

PRIMARY_CLAIM_LEVEL:
  SYMBOLIC_OR_CLASS_LEVEL_EVALUATION_PLAN

declared class:
  E-N7 = { n in Z : 0 <= n <= 10 }

target predicate:
  P(n): n < 5

symbolic theorem coverage:
  n in {0,1,2,3,4}

uncovered region:
  {5,6,7,8,9,10}

uncovered region evaluation:
  available and exact
~~~

Execution:

~~~text
covered region:
  symbolically established true

uncovered region:
  contains values with P(n)=false
~~~

Expected:

~~~text
EVALUATION_COVERAGE_STATUS:
  COVERAGE_PARTIAL

COMPUTATION_PRIMARY_STATUS:
  COMPUTATION_NOT_ESTABLISHED

COMPUTATION_TASK_TERMINAL:
  COMPUTATION_TASK_NOT_ESTABLISHED

COMPUTATION_PROTOCOL_CONFORMANCE:
  COMPUTATION_PROTOCOL_CONFORMANT
~~~

Guards:

~~~text
COVERAGE_PARTIAL != BLOCKED_BY_DEFAULT
CLASS_DEFINITION_COMPLETE != EVALUATION_COVERAGE_COMPLETE
SYMBOLIC_RULE_FOUND != FULL_CLASS_COVERAGE
~~~

## 11. N8 — frozen terminal precedence with lower-level retention

Frozen task contains four independent required obligations.

~~~text
TASK_ID:
  COMP-CH-002-N8
~~~

Q1:

~~~text
requested operation:
  objective-based optimal-plan selection

status:
  COMPUTATION_OUT_OF_SCOPE
~~~

Q2:

~~~text
same reuse key / same frozen semantics
two incompatible applicable cache values
no resolver

status:
  COMPUTATION_CONFLICTING
~~~

Q3:

~~~text
two admissible dependency semantics
different required sets
no resolver

status:
  COMPUTATION_UNDERDETERMINED
~~~

Q4:

~~~text
required dependency interface unavailable

status:
  COMPUTATION_BLOCKED
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
COMPUTATION_TASK_TERMINAL:
  COMPUTATION_TASK_OUT_OF_SCOPE

LOWER_LEVEL_Q2_RETAINED:
  yes

LOWER_LEVEL_Q3_RETAINED:
  yes

LOWER_LEVEL_Q4_RETAINED:
  yes

COMPUTATION_PROTOCOL_CONFORMANCE:
  COMPUTATION_PROTOCOL_CONFORMANT
~~~

No lower-level state may be erased by the task-terminal summary.

## 12. Challenge-level expected result

Every subcase is expected to be protocol-conformant.

~~~text
N1:
  COMPUTATION_TASK_NOT_ESTABLISHED

N2:
  COMPUTATION_TASK_BLOCKED

N3:
  COMPUTATION_TASK_CONFLICTING

N4:
  COMPUTATION_TASK_OUT_OF_SCOPE

N5:
  COMPUTATION_TASK_UNDERDETERMINED

N6:
  COMPUTATION_TASK_PARTIAL

N7:
  COMPUTATION_TASK_NOT_ESTABLISHED

N8:
  COMPUTATION_TASK_OUT_OF_SCOPE
  with CONFLICTING / UNDERDETERMINED / BLOCKED lower states retained

METHOD_GAIN_STATUS:
  COMPUTATION_GAIN_NOT_TESTED

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

Together with COMP-CH-001:

~~~text
ALL_SEVEN_COMPUTATION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  expected yes
~~~

## 13. Frozen scoring — 80 checks

Each subcase has ten frozen checks.

### N1 — 10 checks

~~~text
N1-1 target threshold frozen
N1-2 readout 10 frozen
N1-3 error bound 1 frozen
N1-4 interval [9,11] derived
N1-5 interval crosses threshold
N1-6 resolution NOT_SUFFICIENT
N1-7 primary NOT_ESTABLISHED
N1-8 terminal NOT_ESTABLISHED
N1-9 not relabeled BLOCKED
N1-10 protocol CONFORMANT
~~~

### N2 — 10 checks

~~~text
N2-1 target frozen
N2-2 DEP-N2-v1 required
N2-3 DEP-N2-v1 unavailable
N2-4 no fabricated negative dependency
N2-5 g obligation BLOCKED
N2-6 g action BLOCKED
N2-7 primary BLOCKED
N2-8 terminal BLOCKED
N2-9 not relabeled NOT_ESTABLISHED
N2-10 protocol CONFORMANT
~~~

### N3 — 10 checks

~~~text
N3-1 reuse key frozen
N3-2 model version frozen and common
N3-3 regime frozen and common
N3-4 R1 applicable
N3-5 R2 applicable
N3-6 values conflict
N3-7 no resolver
N3-8 primary CONFLICTING
N3-9 terminal CONFLICTING
N3-10 protocol CONFORMANT
~~~

### N4 — 10 checks

~~~text
N4-1 P1 sufficient
N4-2 P2 sufficient
N4-3 objective runtime supplied
N4-4 request is objective-based selection
N4-5 no Computation-side optimum fabricated
N4-6 Optimization handoff required
N4-7 primary OUT_OF_SCOPE
N4-8 terminal OUT_OF_SCOPE
N4-9 not relabeled NOT_ESTABLISHED
N4-10 protocol CONFORMANT
~~~

### N5 — 10 checks

~~~text
N5-1 DEP-N5-A frozen
N5-2 DEP-N5-B frozen
N5-3 both admissible
N5-4 required sets differ
N5-5 no resolver
N5-6 u2 obligation UNDERDETERMINED
N5-7 u2 action UNDERDETERMINED
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
N7-1 declared class frozen
N7-2 theorem coverage frozen
N7-3 coverage PARTIAL
N7-4 uncovered region explicit
N7-5 uncovered region evaluable
N7-6 predicate false on uncovered members
N7-7 primary NOT_ESTABLISHED
N7-8 terminal NOT_ESTABLISHED
N7-9 no full-coverage promotion
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
DIRECT_COMPUTATION_PILOTS_ATTEMPTED:
  1 -> 2

SUCCESSFUL_DIRECT_COMPUTATION_PILOTS:
  1 -> 2

NEGATIVE_OR_UNRESOLVED_COMPUTATION_CASES:
  0 -> 1

ALL_SEVEN_COMPUTATION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes
~~~

Do not change baseline, NO_GAIN, reproducibility, external, or independent-validation counters.
