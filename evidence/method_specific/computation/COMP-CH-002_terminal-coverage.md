# COMP-CH-002 — Negative / Unresolved-Terminal Computation Challenge Result

Status: **EXECUTED — 80/80 PASS**  
Date: **2026-10-04**  
Challenge ID: `COMP-CH-002`  
Method: **Computation / DSD 계산론**  
Protocol: **Computation Protocol v0.1**  
Case class: `negative_unresolved_terminal_coverage_constructed`

## 1. Frozen references

~~~text
PROTOCOL_COMMIT:
  03b1b7463af6d3a34dc3693a19933e83a3917b4d

PROTOCOL_BLOB:
  4c4fe0b0616371b7df6aff9ce6a1ff7636c49da4

PRECOMMIT_COMMIT:
  4b2c1478a1776ba5aeb5fb4d897a3ea4ca1e8bde

PRECOMMIT_BLOB:
  b988deeff6500175682e120abb1436d3672dfeec
~~~

No protocol rule, fixture, expected status, scoring item, or pass threshold was changed after precommit.

## 2. Final result

~~~text
TOTAL_REQUIRED_CHECKS:
  80

PASSED:
  80

FAILED:
  0

COMPUTATION_PROTOCOL_CONFORMANCE:
  COMPUTATION_PROTOCOL_CONFORMANT

COMPUTATION_METHOD_GAIN_STATUS:
  COMPUTATION_GAIN_NOT_TESTED

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

A negative, blocked, conflicting, underdetermined, out-of-scope, or partial task result remains a valid protocol result when produced by the frozen rules.

~~~text
CONFORMANT_NONPOSITIVE_TERMINAL
  !=
METHOD_FAILURE
~~~

## 3. N1 — evaluable insufficient resolution

Frozen:

~~~text
target:
  determine whether s > 10

readout:
  10

error bound:
  1
~~~

Execution:

~~~text
9 <= s <= 11
~~~

The admissible interval crosses threshold 10.

Therefore:

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

Preserved:

~~~text
EVALUABLE_INSUFFICIENCY != BLOCKED
RESOLUTION_NOT_SUFFICIENT != OUT_OF_SCOPE
~~~

## 4. N2 — blocked required dependency interface

Frozen required interface:

~~~text
REQUIRED_COMPUTATION_INTERFACE_ID:
  DEP-N2-v1

REQUIRED_COMPUTATION_INTERFACE_STATUS:
  REQUIRED_COMPUTATION_INTERFACE_UNAVAILABLE
~~~

No dependency relation was invented.

The protocol therefore could not decide the claim-relevant action for g.

Execution:

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

Preserved:

~~~text
UNAVAILABLE_REQUIRED_INTERFACE != TARGET_IRRELEVANCE
BLOCKED != NOT_ESTABLISHED
MISSING_DEPENDENCY_RECORD != NEGATIVE_DEPENDENCY
~~~

## 5. N3 — conflicting reuse records

Two applicable records under the same frozen reuse semantics remained:

~~~text
R1:
  q(2) = 4

R2:
  q(2) = 5

precedence resolver:
  none
~~~

Both use the same model version, regime, status, and key.

Therefore:

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

Neither cache value was selected post hoc.

## 6. N4 — Optimization request outside Computation task

Frozen request:

~~~text
P1:
  sufficient

P2:
  sufficient

requested operation:
  choose runtime-minimizing plan

objective:
  runtime
~~~

This is objective-based selection among sufficient plans.

Therefore:

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

Preserved:

~~~text
SUFFICIENT_COMPUTATION_PLAN != OPTIMAL_PLAN
COMPUTATION != OPTIMIZATION
OUT_OF_SCOPE != NOT_ESTABLISHED
~~~

## 7. N5 — underdetermined dependency semantics

Frozen alternatives:

~~~text
DEP-N5-A:
  required set = {u1,Y}

DEP-N5-B:
  required set = {u2,u1,Y}

resolver:
  none
~~~

Both dependency interfaces are admissible under the frozen metadata.

Therefore:

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

This is unresolved admissible semantics, not conflicting evidence about one already-frozen graph.

## 8. N6 — exact PARTIAL semantics

The task contains two independently required obligations.

Q1:

~~~text
A = 2 + 3 = 5

status:
  COMPUTATION_ESTABLISHED
~~~

Q2:

~~~text
readout:
  10

error bound:
  1

admissible interval:
  [9,11]

target:
  s > 10

status:
  COMPUTATION_NOT_ESTABLISHED
~~~

Both obligations are evaluable.

There is no blocked, conflicting, underdetermined, or out-of-scope condition.

Therefore:

~~~text
COMPUTATION_TASK_TERMINAL:
  COMPUTATION_TASK_PARTIAL

COMPUTATION_PROTOCOL_CONFORMANCE:
  COMPUTATION_PROTOCOL_CONFORMANT
~~~

Preserved:

~~~text
PARTIAL != BLOCKED_WITH_SOME_SUCCESS
PARTIAL != ATOMIC_FAILURE_RELABELED
~~~

## 9. N7 — partial symbolic coverage with evaluable uncovered failure

Frozen class:

~~~text
E-N7:
  { n in Z : 0 <= n <= 10 }

P(n):
  n < 5
~~~

Frozen symbolic coverage:

~~~text
covered:
  {0,1,2,3,4}

uncovered:
  {5,6,7,8,9,10}
~~~

The uncovered region was fully evaluable and contains false predicate values.

Therefore:

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

Preserved:

~~~text
COVERAGE_PARTIAL != BLOCKED_BY_DEFAULT
CLASS_DEFINITION_COMPLETE != EVALUATION_COVERAGE_COMPLETE
SYMBOLIC_RULE_FOUND != FULL_CLASS_COVERAGE
~~~

## 10. N8 — terminal precedence with lower-level retention

Lower-level states:

~~~text
Q1:
  COMPUTATION_OUT_OF_SCOPE

Q2:
  COMPUTATION_CONFLICTING

Q3:
  COMPUTATION_UNDERDETERMINED

Q4:
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

Execution:

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

No subordinate state was erased.

## 11. Direct terminal coverage after COMP-CH-001 + COMP-CH-002

Directly exercised:

~~~text
COMPUTATION_TASK_ESTABLISHED:
  COMP-CH-001 A/B/C

COMPUTATION_TASK_PARTIAL:
  COMP-CH-002-N6

COMPUTATION_TASK_NOT_ESTABLISHED:
  COMP-CH-002-N1
  COMP-CH-002-N7

COMPUTATION_TASK_BLOCKED:
  COMP-CH-002-N2

COMPUTATION_TASK_CONFLICTING:
  COMP-CH-002-N3

COMPUTATION_TASK_OUT_OF_SCOPE:
  COMP-CH-002-N4
  COMP-CH-002-N8

COMPUTATION_TASK_UNDERDETERMINED:
  COMP-CH-002-N5
~~~

Therefore:

~~~text
ALL_SEVEN_COMPUTATION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes
~~~

## 12. Execution of the 80 frozen checks

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

## 13. Counter update

~~~text
DIRECT_COMPUTATION_PILOTS_ATTEMPTED:
  2

SUCCESSFUL_DIRECT_COMPUTATION_PILOTS:
  2

POSITIVE_COMPUTATION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_COMPUTATION_CASES:
  1

ALL_SEVEN_COMPUTATION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes

METHOD_BOUNDARY_COMPUTATION_CASES:
  0

BASELINE_COMPUTATION_CASES:
  0

NO_GAIN_COMPUTATION_CASES:
  0

REPRODUCIBILITY_CASES:
  0

EXTERNAL_COMPUTATION_APPLICATIONS:
  0

INDEPENDENT_COMPUTATION_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established

COMPUTATION_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_COMPUTATION_EVIDENCE_STATUS:
  validation_in_progress

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 14. Interpretation lock

~~~text
NEGATIVE_OR_UNRESOLVED_TERMINAL
  !=
PROTOCOL_FAILURE

BLOCKED
  !=
NOT_ESTABLISHED

OUT_OF_SCOPE
  !=
FALSE

PARTIAL
  !=
BLOCKED_WITH_SOME_SUCCESS

CONFLICTING
  !=
UNDERDETERMINED

ALL_TERMINALS_EXERCISED
  !=
INTERNAL_STANDARDIZATION

PASS
  !=
METHOD_SUPERIORITY
~~~

## 15. Next

Prospectively precommit and execute the direct neighboring-method boundary challenge for Computation.

Primary neighboring candidates:

~~~text
Optimization
Simulation
Audit
Aggregation
Compression
Measurement
Tracking
Reconstruction
~~~

Use the five-interface test:

~~~text
INPUTS
OPERATION
OUTPUTS
FAILURE_OR_NO_GAIN_CRITERIA
VALIDATION_STANDARD
~~~

Fixture-bounded separation must not be promoted to permanent irreducibility.
