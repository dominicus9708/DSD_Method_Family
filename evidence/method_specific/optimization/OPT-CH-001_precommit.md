# OPT-CH-001 — Positive Constructed Optimization Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-05**  
Challenge ID: `OPT-CH-001`  
Method: **Optimization / DSD 최적화론**  
Protocol: **Optimization Protocol v0.1**  
Case class: `positive_constructed_multi-form_selection`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Purpose

Directly exercise Optimization Protocol v0.1 on several positive constructed selection forms without using external evidence.

The challenge must test that Optimization can establish valid selections while preserving:

~~~text
unique optimum
tied optimum set
Pareto set
incomparability distinct from underdetermination
hard-constraint exclusion
uncertainty-aware ordering
selection preservation under a reduced readout
Computation handoff without substitution
bounded maximum claim
~~~

Method gain is not tested in this challenge.

## 2. Frozen protocol

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

## 3. Subtask A — unique optimum with hard constraint

Candidate set:

~~~text
A = {a,b,c,d}
CANDIDATE_SET_COMPLETENESS:
  claimed complete within declared scope
~~~

Hard constraint:

~~~text
resource <= 8
~~~

Candidate records:

~~~text
a:
  resource = 6
  loss = 9

b:
  resource = 8
  loss = 5

c:
  resource = 10
  loss = 1

d:
  resource = 7
  loss = 6
~~~

Selection semantics:

~~~text
constraint first
then minimize loss
~~~

Expected:

~~~text
FEASIBLE_SET:
  {a,b,d}

INFEASIBLE_SET:
  {c}

UNIQUE_OPTIMUM:
  b

c is not rescued by its better loss score

PRIMARY_STATUS:
  OPTIMIZATION_ESTABLISHED

TASK_TERMINAL:
  OPTIMIZATION_TASK_ESTABLISHED
~~~

Maximum claim:

~~~text
b is the unique optimum within the declared complete candidate set
under the frozen hard constraint and single objective
~~~

No global claim beyond the declared set.

## 4. Subtask B — tied optimum is a positive result

Candidate set:

~~~text
B = {p,q,r}
~~~

All candidates admissible.

Single objective:

~~~text
minimize cost
~~~

Values:

~~~text
p = 4
q = 4
r = 7
~~~

Expected:

~~~text
TIED_OPTIMUM_SET:
  {p,q}

PAIR(p,q):
  PAIR_TIED_UNDER_DECLARED_RULE

OPTIMIZATION_PRIMARY_STATUS:
  OPTIMIZATION_ESTABLISHED

TASK_TERMINAL:
  OPTIMIZATION_TASK_ESTABLISHED

TIED_OPTIMUM_SET != UNDERDETERMINED
~~~

No arbitrary tie-breaking is allowed.

## 5. Subtask C — Pareto set and incomparability

Candidate set:

~~~text
C = {x,y,z}
~~~

Objectives:

~~~text
O1 minimize latency
O2 minimize energy
~~~

Values:

~~~text
x = (2,8)
y = (5,5)
z = (8,2)
~~~

Selection semantics:

~~~text
PARETO_DOMINANCE
no weights
no lexicographic priority
~~~

Expected:

~~~text
PARETO_SET:
  {x,y,z}

no candidate dominates another

PAIR(x,y):
  PAIR_INCOMPARABLE_UNDER_DECLARED_PARTIAL_ORDER

PAIR(y,z):
  PAIR_INCOMPARABLE_UNDER_DECLARED_PARTIAL_ORDER

PAIR(x,z):
  PAIR_INCOMPARABLE_UNDER_DECLARED_PARTIAL_ORDER

OPTIMIZATION_PRIMARY_STATUS:
  OPTIMIZATION_ESTABLISHED

TASK_TERMINAL:
  OPTIMIZATION_TASK_ESTABLISHED

PAIR_INCOMPARABLE_UNDER_DECLARED_PARTIAL_ORDER
  !=
OPTIMIZATION_UNDERDETERMINED
~~~

No weighted-sum scalarization may be invented.

## 6. Subtask D — uncertainty and reduction-preservation

Candidate set:

~~~text
D = {u,v,w}
~~~

Declared single objective:

~~~text
minimize physical cost
~~~

Frozen uncertainty intervals:

~~~text
u:
  [9.0,9.4]

v:
  [10.0,10.3]

w:
  [10.1,10.8]
~~~

Robust ordering rule:

~~~text
candidate L strictly preferred to R
iff upper(L) < lower(R)
~~~

Expected pair relations:

~~~text
u vs v:
  PAIR_STRICTLY_PREFERS_LEFT

u vs w:
  PAIR_STRICTLY_PREFERS_LEFT

v vs w:
  no strict robust order
  PAIR_ORDER_UNDERDETERMINED
  under the declared uncertainty rule
~~~

Expected selection claim:

~~~text
u is uniquely robustly optimal
within D under the frozen interval rule
~~~

Reduced readout:

~~~text
R(candidate) = rounded midpoint to nearest integer

R(u)=9
R(v)=10
R(w)=10
~~~

Frozen preservation claim:

~~~text
R is used only to preserve the fact that u outranks {v,w}
for this declared selection claim

R does not preserve v-vs-w strict order
R(v)=R(w) does not imply v=w
~~~

Expected:

~~~text
SELECTION_RELATION_PRESERVED_ON_DECLARED_SCOPE
  for the top-selection claim only

GLOBAL_INJECTIVITY:
  not claimed

SOURCE_EQUIVALENCE:
  not claimed
~~~

## 7. Subtask E — Computation handoff without substitution

A frozen Computation handoff provides two sufficient plans:

~~~text
P1:
  correct
  estimated resource = 9

P2:
  correct
  estimated resource = 6

COMPUTATION_HANDOFF:
  both plans sufficient for the same computational target
  no optimality claim
~~~

Optimization task:

~~~text
candidate set = {P1,P2}
hard constraint = both admissible
objective = minimize declared resource
~~~

Expected:

~~~text
P2:
  unique optimum

COMPUTATION_PLAN != OPTIMAL_PLAN

Optimization uses the Computation handoff as candidate/evidence input
but performs the objective-based selection itself

OPTIMIZATION_PRIMARY_STATUS:
  OPTIMIZATION_ESTABLISHED

TASK_TERMINAL:
  OPTIMIZATION_TASK_ESTABLISHED
~~~

Method gain:

~~~text
OPTIMIZATION_GAIN_NOT_TESTED
~~~

## 8. Global challenge guards

Across all subtasks preserve:

~~~text
FEASIBLE != OPTIMAL
UNDEFINED != ZERO
INAPPLICABLE != ZERO_COST
HARD_CONSTRAINT_VIOLATION != FINITE_PENALTY
MULTIPLE_OBJECTIVES != WEIGHTED_SUM
PARETO_NONDOMINATED != UNIQUE_OPTIMUM
TIED_OPTIMA != UNDERDETERMINED
INCOMPARABLE != UNDERDETERMINED
EQUAL_REDUCED_SCORE != STRUCTURAL_EQUIVALENCE
COMPUTATION_PLAN != OPTIMAL_PLAN
OPTIMIZATION_ESTABLISHED may coexist with OPTIMIZATION_GAIN_NOT_TESTED
~~~

No external validation, runtime superiority, or global optimum outside the frozen candidate set may be claimed.

## 9. Frozen scoring — 72 checks

### A. Unique optimum / hard constraint — 14

~~~text
A1 candidate set frozen
A2 candidate completeness frozen
A3 hard constraint frozen
A4 objective frozen
A5 selection rule frozen
A6 a feasible
A7 b feasible
A8 c infeasible
A9 d feasible
A10 infeasible c not rescued by objective score
A11 feasible set exactly {a,b,d}
A12 b unique optimum
A13 established primary/status terminal
A14 maximum claim bounded to declared set
~~~

### B. Tied optimum — 10

~~~text
B1 candidate set frozen
B2 objective frozen
B3 p and q both objective value 4
B4 r value 7
B5 p/q pair tied
B6 tied set exactly {p,q}
B7 no arbitrary tie-break
B8 tie not underdetermination
B9 primary established
B10 terminal established
~~~

### C. Pareto / incomparability — 14

~~~text
C1 candidate set frozen
C2 two objectives frozen
C3 Pareto rule frozen
C4 no weight rule supplied
C5 x values retained
C6 y values retained
C7 z values retained
C8 x does not dominate y
C9 y does not dominate z
C10 x does not dominate z
C11 all three retained in Pareto set
C12 pair incomparability distinct from underdetermination
C13 primary established
C14 terminal established without invented scalarization
~~~

### D. Uncertainty / reduction — 14

~~~text
D1 interval semantics frozen
D2 robust-order rule frozen
D3 u interval retained
D4 v interval retained
D5 w interval retained
D6 u strictly outranks v
D7 u strictly outranks w
D8 v-vs-w strict order not established
D9 v-vs-w pair order underdetermined under rule
D10 u unique robust optimum
D11 reduced readout values 9/10/10 retained
D12 top-selection relation preservation established
D13 v/w readout collision not source equivalence
D14 no global injectivity or stronger preservation claim
~~~

### E. Computation handoff — 12

~~~text
E1 P1/P2 Computation sufficiency retained
E2 Computation handoff contains no optimality claim
E3 Optimization candidate set frozen
E4 objective minimize resource frozen
E5 P1 resource 9 retained
E6 P2 resource 6 retained
E7 both admissible
E8 P2 unique optimum
E9 Computation not substituted for Optimization
E10 primary established
E11 terminal established
E12 method gain = OPTIMIZATION_GAIN_NOT_TESTED
~~~

### F. Protocol / global limits — 8

~~~text
F1 protocol v0.1 identity preserved
F2 all claim-relevant optional ledgers populated or explicitly marked
F3 no hidden hard-to-soft transformation
F4 no hidden scalarization
F5 no global candidate-completeness overclaim
F6 no external-validation upgrade
F7 no method-gain claim
F8 no protocol revision or shared-core reopen required if all prior checks pass
~~~

~~~text
TOTAL_REQUIRED_CHECKS:
  72

PASS_THRESHOLD:
  72/72

PARTIAL_PASS_ALLOWED:
  no
~~~

## 10. Allowed post-challenge counter changes on 72/72 PASS

~~~text
DIRECT_OPTIMIZATION_PILOTS_ATTEMPTED:
  0 -> 1

SUCCESSFUL_DIRECT_OPTIMIZATION_PILOTS:
  0 -> 1

POSITIVE_OPTIMIZATION_CASES:
  0 -> 1

BASELINE_OPTIMIZATION_CASES:
  remain 0

NO_GAIN_OPTIMIZATION_CASES:
  remain 0

REPRODUCIBILITY_CASES:
  remain 0
~~~

## 11. Next on PASS

If 72/72 PASS:

~~~text
OPT-CH-002
negative / blocked / conflicting / underdetermined /
out-of-scope / partial terminal coverage
~~~
