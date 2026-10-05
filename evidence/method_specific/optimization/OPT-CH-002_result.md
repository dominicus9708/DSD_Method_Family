# OPT-CH-002 — Negative / Terminal-Coverage Optimization Challenge Result

Status: **EXECUTED — 80/80 PASS**  
Date: **2026-10-05**  
Challenge ID: `OPT-CH-002`  
Method: **Optimization / DSD 최적화론**  
Protocol: **Optimization Protocol v0.1**  
Case class: `negative_unresolved_terminal_coverage_constructed`

## 1. Frozen references

~~~text
PROTOCOL_COMMIT:
  34584acd54af1bafef7dd176f795ed914eddc6b2

PROTOCOL_BLOB:
  5d2f9e37eab08bba27b0f416599df2e74a8c0c42

PRECOMMIT_COMMIT:
  8d778da4289b0a4080e5f93ffecae5ae55256f62

PRECOMMIT_BLOB:
  393dbfa5bdc9040cfcd4a07e63899873293dffd9
~~~

Execution used the frozen precommit without changing candidate sets, objectives, constraints, selection semantics, reduction rules, terminal precedence, or scoring criteria.

## 2. N1 — evaluable false unique-optimum claim

Frozen values:

~~~text
cost(a)=7
cost(b)=4
cost(c)=9
~~~

All three candidates are admissible.

Therefore:

~~~text
true unique optimum:
  b

requested claim:
  a is unique optimum

requested claim status:
  false
~~~

Result:

~~~text
OPTIMIZATION_PRIMARY_STATUS:
  OPTIMIZATION_NOT_ESTABLISHED

OPTIMIZATION_TASK_TERMINAL:
  OPTIMIZATION_TASK_NOT_ESTABLISHED

OPTIMIZATION_PROTOCOL_CONFORMANCE:
  OPTIMIZATION_PROTOCOL_CONFORMANT
~~~

The result is evaluably false, not blocked and not underdetermined.

## 3. N2 — unavailable required lifecycle objective component

The declared objective is total lifecycle cost.

Required components:

~~~text
build
operate
disposal
~~~

The disposal component for candidate `q` is unavailable and no omission or irrelevance rule is supplied.

Result:

~~~text
OBJECTIVE_COMPONENT_COMPLETENESS_STATUS:
  incomplete

REQUIRED_OPTIMIZATION_INTERFACE_STATUS:
  REQUIRED_OPTIMIZATION_INTERFACE_UNAVAILABLE

OPTIMIZATION_PRIMARY_STATUS:
  OPTIMIZATION_BLOCKED

OPTIMIZATION_TASK_TERMINAL:
  OPTIMIZATION_TASK_BLOCKED

OPTIMIZATION_PROTOCOL_CONFORMANCE:
  OPTIMIZATION_PROTOCOL_CONFORMANT
~~~

The missing component is not converted into zero, irrelevance, infeasibility, or a finite penalty.

## 4. N3 — conflicting objective semantics

The frozen objective identity/version has two incompatible applicable records:

~~~text
R1:
  minimize
  -> x

R2:
  maximize
  -> y

resolver:
  none
~~~

Result:

~~~text
OPTIMIZATION_PRIMARY_STATUS:
  OPTIMIZATION_CONFLICTING

OPTIMIZATION_TASK_TERMINAL:
  OPTIMIZATION_TASK_CONFLICTING

OPTIMIZATION_PROTOCOL_CONFORMANCE:
  OPTIMIZATION_PROTOCOL_CONFORMANT
~~~

No record was selected arbitrarily.

## 5. N4 — Control request outside Optimization

The task supplies a one-step candidate/action set and one-step objective evidence, but requests a state-dependent policy for all future reachable states.

That request is outside one-time Optimization and requires a Control handoff.

Result:

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

No future-state policy was fabricated.

## 6. N5 — underdetermined multi-objective semantics

Frozen candidate values:

~~~text
m = (cost 3, emissions 9)
n = (cost 8, emissions 2)
~~~

Two admissible selection semantics remain:

~~~text
S1:
  cost-first lexicographic
  -> m

S2:
  emissions-first lexicographic
  -> n

resolver:
  none
~~~

Result:

~~~text
OPTIMIZATION_PRIMARY_STATUS:
  OPTIMIZATION_UNDERDETERMINED

OPTIMIZATION_TASK_TERMINAL:
  OPTIMIZATION_TASK_UNDERDETERMINED

OPTIMIZATION_PROTOCOL_CONFORMANCE:
  OPTIMIZATION_PROTOCOL_CONFORMANT
~~~

This is not Pareto incomparability under one frozen rule and is not conflict between records about one already-frozen rule.

## 7. N6 — exact PARTIAL semantics

The task contains two independently required in-scope obligations.

Q1:

~~~text
candidate set:
  {u,v}

cost(u)=2
cost(v)=5

result:
  u is optimum

status:
  OPTIMIZATION_ESTABLISHED
~~~

Q2:

~~~text
candidate set:
  {r,s}

cost(r)=7
cost(s)=3

requested claim:
  r is unique optimum

result:
  requested claim false

status:
  OPTIMIZATION_NOT_ESTABLISHED
~~~

No required obligation is blocked, conflicting, underdetermined, or out of scope.

Therefore:

~~~text
OPTIMIZATION_TASK_TERMINAL:
  OPTIMIZATION_TASK_PARTIAL

OPTIMIZATION_PROTOCOL_CONFORMANCE:
  OPTIMIZATION_PROTOCOL_CONFORMANT
~~~

PARTIAL is not used for an atomic false claim and is not used to mask a blocked obligation.

## 8. N7 — evaluable reduction not preserving selection relation

Frozen source values:

~~~text
c1 = 4.4
c2 = 4.6
~~~

Frozen reduction:

~~~text
R(value) = round to nearest integer

R(c1)=4
R(c2)=5
~~~

The precommitted claim-relevant preservation scope also contains the supplied perturbation witness:

~~~text
c1' = 4.49 -> 4
c2' = 4.41 -> 4
~~~

The source ordering in that witness is not preserved as a strict reduced-readout order.

Thus the reduced representation is not licensed as an order-preserving interface over the declared source-selection scope.

Result:

~~~text
SELECTION_PRESERVATION_STATUS:
  SELECTION_RELATION_NOT_PRESERVED

OPTIMIZATION_PRIMARY_STATUS:
  OPTIMIZATION_NOT_ESTABLISHED

OPTIMIZATION_TASK_TERMINAL:
  OPTIMIZATION_TASK_NOT_ESTABLISHED

OPTIMIZATION_PROTOCOL_CONFORMANCE:
  OPTIMIZATION_PROTOCOL_CONFORMANT
~~~

The result is evaluable non-preservation, not blocked.

No source-equivalence, global injectivity, or generic-low-error claim was substituted for the required selection-preservation condition.

## 9. N8 — terminal precedence with lower-level retention

Frozen subordinate results:

~~~text
Q1:
  OPTIMIZATION_OUT_OF_SCOPE

Q2:
  OPTIMIZATION_CONFLICTING

Q3:
  OPTIMIZATION_UNDERDETERMINED

Q4:
  OPTIMIZATION_BLOCKED
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
OPTIMIZATION_TASK_TERMINAL:
  OPTIMIZATION_TASK_OUT_OF_SCOPE
~~~

Lower-level states remain explicitly retained:

~~~text
LOWER_LEVEL_Q2_RETAINED:
  yes

LOWER_LEVEL_Q3_RETAINED:
  yes

LOWER_LEVEL_Q4_RETAINED:
  yes
~~~

Protocol conformance:

~~~text
OPTIMIZATION_PROTOCOL_CONFORMANCE:
  OPTIMIZATION_PROTOCOL_CONFORMANT
~~~

## 10. Terminal and primary-status coverage

OPT-CH-001 supplied direct positive ESTABLISHED examples.

OPT-CH-002 directly exercised:

~~~text
OPTIMIZATION_NOT_ESTABLISHED
OPTIMIZATION_BLOCKED
OPTIMIZATION_CONFLICTING
OPTIMIZATION_OUT_OF_SCOPE
OPTIMIZATION_UNDERDETERMINED
~~~

Therefore, across OPT-CH-001 and OPT-CH-002:

~~~text
ALL_SIX_OPTIMIZATION_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  yes
~~~

Task terminals directly exercised across the two challenges:

~~~text
OPTIMIZATION_TASK_ESTABLISHED
OPTIMIZATION_TASK_PARTIAL
OPTIMIZATION_TASK_NOT_ESTABLISHED
OPTIMIZATION_TASK_BLOCKED
OPTIMIZATION_TASK_CONFLICTING
OPTIMIZATION_TASK_OUT_OF_SCOPE
OPTIMIZATION_TASK_UNDERDETERMINED
~~~

Therefore:

~~~text
ALL_SEVEN_OPTIMIZATION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes
~~~

## 11. Method-gain state

No subcase requested a method-gain comparison.

~~~text
OPTIMIZATION_METHOD_GAIN_STATUS:
  OPTIMIZATION_GAIN_NOT_TESTED
~~~

No baseline or NO_GAIN counter is incremented by this challenge.

## 12. Frozen-score execution

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
N1-9 PASS
N1-10 PASS

N1: 10/10
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
N2-9 PASS
N2-10 PASS

N2: 10/10
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
N3-9 PASS
N3-10 PASS

N3: 10/10
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
N4-9 PASS
N4-10 PASS

N4: 10/10
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
N5-9 PASS
N5-10 PASS

N5: 10/10
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
N6-9 PASS
N6-10 PASS

N6: 10/10
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
N7-9 PASS
N7-10 PASS

N7: 10/10
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
N8-9 PASS
N8-10 PASS

N8: 10/10
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

## 13. Post-challenge state

~~~text
DIRECT_OPTIMIZATION_PILOTS_ATTEMPTED:
  2

SUCCESSFUL_DIRECT_OPTIMIZATION_PILOTS:
  2

POSITIVE_OPTIMIZATION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_OPTIMIZATION_CASES:
  1

ALL_SIX_OPTIMIZATION_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  yes

ALL_SEVEN_OPTIMIZATION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes

METHOD_BOUNDARY_OPTIMIZATION_CASES:
  0

BASELINE_OPTIMIZATION_CASES:
  0

NO_GAIN_OPTIMIZATION_CASES:
  0

REPRODUCIBILITY_CASES:
  0

EXTERNAL_OPTIMIZATION_APPLICATIONS:
  0

INDEPENDENT_OPTIMIZATION_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established

OPTIMIZATION_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_OPTIMIZATION_EVIDENCE_STATUS:
  validation_in_progress

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 14. Maximum supported conclusion

Optimization Protocol v0.1 has now directly exercised all six primary status classes and all seven task-terminal classes on frozen constructed evidence.

The evidence establishes terminal discrimination and negative-path handling at the constructed internal level.

It does not establish external validity, independent replication, global optimality, or method gain.

## 15. Next

Prospectively precommit and execute:

~~~text
OPT-CH-003
direct neighboring-method boundary challenge
~~~

The challenge should test Optimization against the most collision-prone neighboring methods using the five-interface identity, equal shared-artifact access, and explicit source-handoff separation.
