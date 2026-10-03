# COMP-CH-001 — Positive Constructed Computation Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-03**  
Challenge ID: `COMP-CH-001`  
Method: **Computation / DSD 계산론**  
Protocol: **Computation Protocol v0.1**  
Case class: `positive_constructed_computation_challenge`  
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

Test whether frozen Computation Protocol v0.1 can execute one positive constructed challenge pack containing three prospectively frozen Computation tasks that collectively exercise:

~~~text
semantic obligation versus execution action

fresh evaluation

valid reuse under matching version / status / regime

sound target-relative omission

finite-DAG closure / termination

symbolic class-level discharge without literal enumeration

complete symbolic evaluator coverage

resolution sufficiency under an explicit end-to-end error bound

information-loss guard:
  equal reduced readout != source identity

bounded computation-plan claim

Computation / Optimization non-substitution

protocol conformance

maximum-supported-claim bounding
~~~

This challenge deliberately does not request:

~~~text
global source equivalence

global irrelevance

global minimality

optimal execution ordering

runtime speedup

memory reduction

energy reduction

method superiority

external applicability

independent validation
~~~

Challenge-level counters count this pack as one direct Computation pilot.

## 3. Frozen challenge pack identity

~~~text
CHALLENGE_ID:
  COMP-CH-001

CHALLENGE_VERSION:
  1

SUBTASKS:
  COMP-CH-001-A
  COMP-CH-001-B
  COMP-CH-001-C

METHOD_GAIN_ASSESSMENT:
  not_requested

COMPARATOR:
  not_requested

OPTIMIZATION_OBJECTIVE:
  not_supplied

POST_HOC_REPAIR:
  prohibited
~~~

Each subtask has exactly one frozen primary claim level.

## 4. Subtask A — mixed fresh / reuse / omission computation plan

### 4.1 Task lock

~~~text
COMPUTATION_TASK_ID:
  COMP-CH-001-A

TASK_VERSION:
  1

PRIMARY_CLAIM_LEVEL:
  COMPUTATION_PLAN_FOR_DECLARED_TARGET

COMPUTATIONAL_TARGET_ID:
  TARGET-A-v1

TARGET_DEFINITION:
  Y = f(3) + g(4)

f(x):
  x^2

g(x):
  2x

TARGET_OUTPUT_SCOPE:
  scalar Y

TARGET_EQUIVALENCE_OR_TOLERANCE:
  exact equality

TARGET_ERROR_SEMANTICS:
  exact

MAXIMUM_SUPPORTED_CLAIM:
  under graph DEP-A-v1 and reuse interface REUSE-A-v1,
  f(3) is required and fresh-evaluated,
  g(4) is required and discharged by valid reuse,
  h(5) is target-irrelevant and soundly omitted,
  finite closure is established,
  and Y=17;
  no execution-order optimality or performance gain is claimed
~~~

### 4.2 Evaluation class and dependency graph

~~~text
EVALUATION_CLASS_ID:
  E-A-v1

EVALUATION_CLASS_REPRESENTATION_MODE:
  GRAPH_OR_DAG_DEFINED_CLASS

EVALUATION_MODE:
  DEPENDENCY_CLOSURE

EVALUATION_CLASS_COMPLETENESS_STATUS:
  EVALUATION_CLASS_CLAIMED_COMPLETE_WITHIN_SCOPE

units:
  u_f = f(3)
  u_g = g(4)
  u_h = h(5)
  u_Y = add(u_f,u_g)

h(x):
  x^2

DEPENDENCY_INTERFACE_ID:
  DEP-A-v1

DEPENDENCY_SEMANTICS:
  directed exact functional dependency
~~~

Frozen dependency edges:

~~~text
u_f -> u_Y
u_g -> u_Y

u_h:
  no path to u_Y
~~~

No hidden dependency is supplied.

### 4.3 Typed status / applicability

~~~text
u_f:
  applicable
  defined input
  computation result not yet available

u_g:
  applicable
  defined input
  valid cached result supplied

u_h:
  applicable
  defined input
  target-irrelevant under DEP-A-v1

u_Y:
  applicable
  depends exactly on u_f and u_g
~~~

No absent / undefined / inapplicable state is encoded as zero.

### 4.4 Semantic obligations

Expected obligation statuses:

~~~text
u_f:
  REQUIRED_FOR_TARGET

u_g:
  REQUIRED_FOR_TARGET

u_h:
  NOT_REQUIRED_FOR_TARGET

u_Y:
  REQUIRED_FOR_TARGET
~~~

Required distinction:

~~~text
REQUIRED_RESULT
  !=
FRESH_EVALUATION_REQUIRED
~~~

### 4.5 Reuse interface

Frozen cache record:

~~~text
REUSE_INTERFACE_ID:
  REUSE-A-v1

REUSE_INTERFACE_COHERENCE_STATUS_EXPECTED:
  REUSE_INTERFACE_CONSISTENT

REUSE_CLASS_ID:
  CACHE-G-v1

REUSE_KEY:
  g(4)

CACHED_VALUE:
  8

SOURCE_MODEL_VERSION:
  MODEL-A-v1

CURRENT_MODEL_VERSION:
  MODEL-A-v1

STATUS_LOCK:
  defined / applicable

REGIME_LOCK:
  REGIME-A-v1

CURRENT_REGIME:
  REGIME-A-v1

TRANSITION_INVALIDATION:
  none

REUSE_INVALIDATION_RULE:
  invalidate on input/model/status/regime mismatch
~~~

Expected:

~~~text
REUSE_ESTABLISHED_ON_DECLARED_SCOPE
~~~

### 4.6 Execution actions

Expected actions:

~~~text
u_f:
  EVALUATE_FRESH

u_g:
  REUSE_VALID_RESULT

u_h:
  OMIT_AS_TARGET_IRRELEVANT

u_Y:
  EVALUATE_FRESH
~~~

Fresh evaluation:

~~~text
f(3) = 9
~~~

Reuse:

~~~text
g(4) = 8
~~~

Target:

~~~text
Y = 9 + 8 = 17
~~~

The omitted unit:

~~~text
h(5) = 25
~~~

is intentionally not evaluated for the task because DEP-A-v1 establishes no path from u_h to u_Y.

The literal value 25 is supplied only as fixture definition metadata and must not be used as a computed task result.

### 4.7 Closure

~~~text
COMPUTATION_CLOSURE_INTERFACE_ID:
  CLOSURE-A-v1

COMPUTATION_CLOSURE_KIND:
  FINITE_TERMINATION

COMPUTATION_CLOSURE_STATUS_EXPECTED:
  CLOSURE_ESTABLISHED

ORDER_DEPENDENCE_STATUS:
  target value order-independent under exact addition

TERMINATION_OR_CONVERGENCE_PROVENANCE:
  frozen finite acyclic graph DEP-A-v1
~~~

### 4.8 Computation / Optimization boundary

Two sufficient execution orders exist:

~~~text
P1:
  fresh f(3)
  reuse g(4)
  add

P2:
  reuse g(4)
  fresh f(3)
  add
~~~

No cost objective is supplied.

Expected:

~~~text
both orders:
  sufficient

OPTIMIZATION_HANDOFF:
  NOT_REQUESTED

OPTIMAL_ORDER:
  not selected
~~~

### 4.9 Expected Subtask A result

~~~text
REQUIRED_RESULT_OR_OBLIGATION_SET:
  {u_f,u_g,u_Y}

FRESH_EVALUATION_SET:
  {u_f,u_Y}

REUSED_RESULT_SET:
  {u_g}

SYMBOLICALLY_DISCHARGED_SET:
  {}

SOUNDLY_OMITTED_SET:
  {u_h}

BLOCKED_SET:
  {}

CONFLICTING_SET:
  {}

UNDERDETERMINED_SET:
  {}

OUT_OF_SCOPE_SET:
  {}

COMPUTATION_SET_OUTCOME:
  COMPUTATION_SET_FULLY_PLANNED

COMPUTATION_PRIMARY_STATUS:
  COMPUTATION_ESTABLISHED

COMPUTATION_TASK_TERMINAL:
  COMPUTATION_TASK_ESTABLISHED

COMPUTATION_PROTOCOL_CONFORMANCE:
  COMPUTATION_PROTOCOL_CONFORMANT

COMPUTATION_METHOD_GAIN_STATUS:
  COMPUTATION_GAIN_NOT_TESTED
~~~

## 5. Subtask B — symbolic full-class discharge

### 5.1 Task lock

~~~text
COMPUTATION_TASK_ID:
  COMP-CH-001-B

TASK_VERSION:
  1

PRIMARY_CLAIM_LEVEL:
  SYMBOLIC_OR_CLASS_LEVEL_EVALUATION_PLAN

COMPUTATIONAL_TARGET_ID:
  TARGET-B-v1

TARGET_DEFINITION:
  establish P(n) for every n in E-B-v1

P(n):
  n(n+1) is even

TARGET_OUTPUT_SCOPE:
  bounded integer class E-B-v1

TARGET_EQUIVALENCE_OR_TOLERANCE:
  exact logical truth

MAXIMUM_SUPPORTED_CLAIM:
  THM-EVEN-v1 symbolically discharges P(n)
  for every integer n with 0 <= n <= 100;
  no claim is made about unrelated predicates
~~~

### 5.2 Evaluation class

~~~text
EVALUATION_CLASS_ID:
  E-B-v1

EVALUATION_CLASS_VERSION_OR_DEFINITION:
  { n in Z : 0 <= n <= 100 }

EVALUATION_CLASS_REPRESENTATION_MODE:
  PREDICATE_DEFINED_CLASS

EVALUATION_MODE:
  THEOREM_OR_RELATION_BASED

EVALUATION_CLASS_COMPLETENESS_STATUS:
  EVALUATION_CLASS_CLAIMED_COMPLETE_WITHIN_SCOPE
~~~

Literal enumeration of 101 elements is not required by the challenge.

### 5.3 Symbolic theorem and coverage

Frozen symbolic rule:

~~~text
THEOREM_ID:
  THM-EVEN-v1

THEOREM_STATEMENT:
  for every integer n,
  n and n+1 are consecutive;
  one of them is even;
  therefore n(n+1) is even

THEOREM_DOMAIN:
  all integers
~~~

Coverage:

~~~text
EVALUATION_COVERAGE_SCOPE:
  E-B-v1

EVALUATION_COVERAGE_STATUS_EXPECTED:
  COVERAGE_COMPLETE_FOR_DECLARED_CLAIM

COVERED_SUBCLASS_OR_RELATION:
  all n in E-B-v1

UNCOVERED_OR_UNRESOLVED_SUBCLASS:
  empty
~~~

Semantic obligation:

~~~text
P(n) over whole E-B-v1:
  REQUIRED_FOR_TARGET
~~~

Execution action:

~~~text
P(n) over whole E-B-v1:
  SYMBOLICALLY_DISCHARGE
~~~

Required guards:

~~~text
SYMBOLIC_RULE_FOUND
  !=
FULL_CLASS_COVERAGE

but here:

theorem domain:
  all integers

declared class:
  bounded subset of integers

therefore:
  full declared coverage is expected
~~~

### 5.4 Expected Subtask B result

~~~text
REQUIRED_RESULT_OR_OBLIGATION_SET:
  {P over E-B-v1}

FRESH_EVALUATION_SET:
  {}

REUSED_RESULT_SET:
  {}

SYMBOLICALLY_DISCHARGED_SET:
  {P over E-B-v1}

SOUNDLY_OMITTED_SET:
  {}

COMPUTATION_SET_OUTCOME:
  COMPUTATION_SET_FULLY_PLANNED

COMPUTATION_PRIMARY_STATUS:
  COMPUTATION_ESTABLISHED

COMPUTATION_TASK_TERMINAL:
  COMPUTATION_TASK_ESTABLISHED

COMPUTATION_PROTOCOL_CONFORMANCE:
  COMPUTATION_PROTOCOL_CONFORMANT

COMPUTATION_METHOD_GAIN_STATUS:
  COMPUTATION_GAIN_NOT_TESTED
~~~

No claim of faster runtime versus enumeration is requested.

## 6. Subtask C — resolution sufficiency with information-loss guard

### 6.1 Task lock

~~~text
COMPUTATION_TASK_ID:
  COMP-CH-001-C

TASK_VERSION:
  1

PRIMARY_CLAIM_LEVEL:
  SUFFICIENT_RESOLUTION_FOR_DECLARED_TARGET

COMPUTATIONAL_TARGET_ID:
  TARGET-C-v1

TARGET_DEFINITION:
  decide whether s > 10

s:
  x1 + x2

TARGET_OUTPUT_SCOPE:
  Boolean threshold classification

TARGET_EQUIVALENCE_OR_TOLERANCE:
  exact classification of s > 10

TARGET_ERROR_SEMANTICS:
  readout interval must lie entirely on one side
  of threshold 10

MAXIMUM_SUPPORTED_CLAIM:
  for the frozen readout r=11 with absolute error <=0.5,
  the declared target s>10 is safely true;
  ordered source identity is not recovered or claimed
~~~

### 6.2 Source / reduced-readout fixture

Two distinct ordered source states are supplied:

~~~text
c1:
  (x1,x2) = (4.4,6.2)

c2:
  (x1,x2) = (6.2,4.4)

source identity:
  c1 != c2
~~~

Both satisfy:

~~~text
s = x1+x2 = 10.6
~~~

Frozen reduced readout:

~~~text
READOUT_OR_REDUCTION_ID:
  ROUND-SUM-v1

R(x1,x2):
  nearest integer to x1+x2

R(c1):
  11

R(c2):
  11
~~~

Information-loss handoff:

~~~text
COLLISION_STATUS:
  collision witness established on ordered source states

INJECTIVITY_SCOPE:
  not established on ordered source class

SUPPORT_RETENTION_STATUS:
  not required for TARGET-C-v1

RECONSTRUCTION_SCOPE_IF_RELEVANT:
  reconstruction not claimed

REQUIRED_SIDECARS:
  error bound only
~~~

Required guard:

~~~text
EQUAL_REDUCED_READOUT
  !=
EQUAL_COMPONENT_STATE
~~~

### 6.3 Resolution / error lock

~~~text
RESOLUTION_ID:
  ROUND-1-v1

RESOLUTION_VERSION_OR_DEFINITION:
  nearest-integer readout

TARGET_DISTINGUISHABILITY_REQUIREMENT:
  determine side of threshold 10

APPROXIMATION_RULE:
  |s-r| <= 0.5

ERROR_METRIC_OR_RELATION:
  absolute scalar error

ERROR_BOUND:
  0.5

ERROR_COMPOSITION_RULE_IF_MULTISTAGE:
  not applicable

ACCEPTANCE_THRESHOLD:
  readout interval must not cross 10

VALIDITY_SCOPE:
  this frozen scalar-threshold task
~~~

From:

~~~text
r = 11
|s-r| <= 0.5
~~~

the admissible interval is:

~~~text
10.5 <= s <= 11.5
~~~

and therefore every admissible s satisfies:

~~~text
s > 10
~~~

Expected:

~~~text
RESOLUTION_SUFFICIENT_FOR_DECLARED_TARGET
~~~

### 6.4 Expected Subtask C result

~~~text
INFORMATION_LOSS_HANDOFF:
  populated

RESOLUTION_STATUS:
  RESOLUTION_SUFFICIENT_FOR_DECLARED_TARGET

COMPUTATION_SET_OUTCOME:
  COMPUTATION_SET_FULLY_PLANNED

COMPUTATION_PRIMARY_STATUS:
  COMPUTATION_ESTABLISHED

COMPUTATION_TASK_TERMINAL:
  COMPUTATION_TASK_ESTABLISHED

COMPUTATION_PROTOCOL_CONFORMANCE:
  COMPUTATION_PROTOCOL_CONFORMANT

COMPUTATION_METHOD_GAIN_STATUS:
  COMPUTATION_GAIN_NOT_TESTED
~~~

Preserve:

~~~text
R(c1) = R(c2)
  !=
c1 = c2

TARGET-SAFE READOUT
  !=
SOURCE-IDENTITY RECOVERY

SUFFICIENT RESOLUTION FOR TARGET-C-v1
  !=
GLOBALLY MINIMAL RESOLUTION
~~~

## 7. Frozen optional-ledger expectations

Across the challenge pack:

~~~text
DYNAMIC_TRANSITION_LOCALITY_LEDGER:
  NOT_REQUESTED

COMPARATOR_FAIRNESS_LEDGER:
  NOT_REQUESTED

COST_COMPLEXITY_EVIDENCE_LEDGER:
  NOT_REQUESTED

OPTIMIZATION_HANDOFF:
  NOT_REQUESTED

METHOD_GAIN_STATUS:
  COMPUTATION_GAIN_NOT_TESTED

EXTERNAL_APPLICATION:
  no

INDEPENDENT_VALIDATION:
  not established
~~~

## 8. Frozen challenge-level expected result

~~~text
DIRECT_COMPUTATION_PILOT:
  positive

SUBTASK_A:
  COMPUTATION_TASK_ESTABLISHED
  COMPUTATION_SET_FULLY_PLANNED
  mixed fresh/reuse/omission plan established

SUBTASK_B:
  COMPUTATION_TASK_ESTABLISHED
  COMPUTATION_SET_FULLY_PLANNED
  symbolic full-class discharge established

SUBTASK_C:
  COMPUTATION_TASK_ESTABLISHED
  RESOLUTION_SUFFICIENT_FOR_DECLARED_TARGET
  information-loss guard preserved

PROTOCOL_CONFORMANCE:
  conformant on all three subtasks

METHOD_GAIN_STATUS:
  COMPUTATION_GAIN_NOT_TESTED

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 9. Frozen scoring — 84 checks

### A. Protocol / challenge immutability — 12

~~~text
A1 protocol commit/blob frozen
A2 G1-G18 identity frozen
A3 T1-T18 identity frozen
A4 challenge ID/version frozen
A5 all three subtask IDs frozen
A6 exactly one primary claim per subtask
A7 method gain not requested
A8 comparator not requested
A9 Optimization objective not supplied
A10 external application not claimed
A11 post-hoc task repair prohibited
A12 protocol edit after result prohibited
~~~

### B. Subtask A locks / obligation-action separation — 14

~~~text
B1 target Y=f(3)+g(4) frozen
B2 evaluation class E-A-v1 frozen
B3 dependency graph DEP-A-v1 frozen
B4 u_f required
B5 u_g required
B6 u_h not required
B7 u_Y required
B8 required-result / fresh-evaluation distinction retained
B9 reuse interface REUSE-A-v1 frozen
B10 cache key g(4) frozen
B11 model version matches
B12 regime matches
B13 invalidation rule frozen
B14 no absent/undefined state converted to zero
~~~

### C. Subtask A execution / closure / Optimization boundary — 14

~~~text
C1 f(3)=9
C2 g(4)=8 reused
C3 reuse validity established
C4 u_f action EVALUATE_FRESH
C5 u_g action REUSE_VALID_RESULT
C6 u_h action OMIT_AS_TARGET_IRRELEVANT
C7 u_Y action EVALUATE_FRESH
C8 Y=17
C9 omitted set exactly {u_h}
C10 finite-DAG closure established
C11 no hidden path u_h -> u_Y
C12 both P1 and P2 sufficient
C13 no optimal order selected
C14 Computation not promoted to Optimization
~~~

### D. Subtask B symbolic coverage — 12

~~~text
D1 E-B-v1 predicate-defined class frozen
D2 class exactly integers 0..100
D3 theorem THM-EVEN-v1 frozen
D4 theorem domain all integers
D5 evaluation mode theorem/relation based
D6 literal enumeration not required
D7 coverage scope E-B-v1
D8 coverage complete for declared claim
D9 uncovered subclass empty
D10 action SYMBOLICALLY_DISCHARGE
D11 task terminal ESTABLISHED
D12 no speedup claim inferred
~~~

### E. Subtask C resolution / information-loss discipline — 14

~~~text
E1 c1 != c2
E2 both source sums equal 10.6
E3 R(c1)=11
E4 R(c2)=11
E5 collision witness retained
E6 ordered-source injectivity not claimed
E7 error bound 0.5 frozen
E8 admissible interval [10.5,11.5]
E9 interval does not cross threshold 10
E10 target s>10 established
E11 resolution SUFFICIENT
E12 equal readout not promoted to equal source
E13 reconstruction not claimed
E14 global minimal-resolution claim not made
~~~

### F. Cross-cutting protocol discipline — 10

~~~text
F1 all three subtasks preserve maximum-supported-claim bounds
F2 no method-gain claim
F3 no comparator claim
F4 no external validation claim
F5 no independent replication claim
F6 no global irrelevance claim
F7 no global source-equivalence claim
F8 no hidden neighboring-method substitution
F9 protocol revision remains unnecessary if expected outputs match
F10 shared core reopen remains unnecessary if expected outputs match
~~~

### G. Final protocol results — 8

~~~text
G1 Subtask A COMPUTATION_ESTABLISHED
G2 Subtask A COMPUTATION_TASK_ESTABLISHED
G3 Subtask B COMPUTATION_ESTABLISHED
G4 Subtask B COMPUTATION_TASK_ESTABLISHED
G5 Subtask C COMPUTATION_ESTABLISHED
G6 Subtask C COMPUTATION_TASK_ESTABLISHED
G7 all three protocol-conformant
G8 challenge-level direct positive pilot established
~~~

~~~text
TOTAL_REQUIRED_CHECKS:
  84

PASS_THRESHOLD:
  84/84

PARTIAL_PASS_ALLOWED:
  no
~~~
