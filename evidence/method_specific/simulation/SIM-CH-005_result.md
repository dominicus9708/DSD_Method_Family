# SIM-CH-005 — Strongest-Reasonable Non-DSD Simulation Baseline Result

Status: **EXECUTED — 82/82 PASS / SIMULATION_NO_GAIN**  
Date: **2026-10-06**  
Challenge ID: `SIM-CH-005`  
Method: **Simulation / DSD 시뮬레이션론**  
Protocol: **Simulation Protocol v0.1**  
Baseline: **B1_STRONG_HYBRID_SIMULATION_ENGINE**

## 1. Frozen references

~~~text
SIMULATION_PROTOCOL_COMMIT:
  ea271d04eb09d252299d9420d0fb1191564f5bc6

SIMULATION_PROTOCOL_BLOB:
  c3d6f80d99dabb5b84c7a60fd2df3f58bf9dba35

PRECOMMIT_COMMIT:
  da364f3999558c71fb705a8bd87b734c0132a8d6

PRECOMMIT_BLOB:
  5a980110d8e2cab5b9fbef654bc4acfe0dbce16b
~~~

No protocol rule, B1 capability, fixture, gain axis, scoring item, or pass threshold changed after precommit.

## 2. Fairness and strength result

~~~text
BASELINE_ID:
  B1_STRONG_HYBRID_SIMULATION_ENGINE

BASELINE_MATERIALLY_STRONGER_THAN_B0:
  yes

EQUAL_INFORMATION_ACCESS:
  yes

SIMULATION_HIDDEN_ADVANTAGE_INPUTS:
  0

BASELINE_WITHHELD_CLAIM_RELEVANT_INPUTS:
  0

BASELINE_WEAKENED_AFTER_PRECOMMIT:
  no
~~~

B1 used ordinary non-DSD simulation machinery only.

## 3. R1 — versioned model non-retroactivity

Frozen v1 model:

~~~text
x_0=1
x_(n+1)=2*x_n
n=0..2
~~~

Both evaluators generated:

~~~text
{1,2,4}
~~~

After M-v2 was supplied:

~~~text
x_(n+1)=3*x_n
~~~

both preserved:

~~~text
TASK-v1:
  still bound to M-v1

v1 trajectory:
  {1,2,4}

new v2 task:
  may generate {1,3,9}

retroactive rewrite:
  no
~~~

Result:

~~~text
BASELINE_MATCH
~~~

## 4. R2 — branch-complete hybrid transition with supplied lineage

Frozen relation:

~~~text
s0 -> p
J(p)={q1,q2}
q1 -> r1
q2 -> r2
~~~

Both generated:

~~~text
s0->p->q1->r1
s0->p->q2->r2
~~~

Both retained:

~~~text
BRANCH_COVERAGE:
  complete on declared scope

UNIQUENESS:
  not established

DECLARED_BRANCHING:
  not semantic underdetermination

SUPPLIED_LINEAGE_RELATION:
  retained

LINEAGE_GENERATED_BY_SIMULATION:
  no
~~~

Result:

~~~text
BASELINE_MATCH
~~~

## 5. R3 — bounded numerical enclosure

Frozen enclosure:

~~~text
x(1) in [0.367,0.369]
~~~

Both computed/retained:

~~~text
enclosure width:
  0.002

reference exp(-1):
  inside enclosure

acceptance width threshold:
  <=0.003
  satisfied

NUMERICAL_ACCEPTANCE:
  established on frozen horizon

EXACTNESS:
  not claimed

UNBOUNDED_TIME_CLAIM:
  not made
~~~

Result:

~~~text
BASELINE_MATCH
~~~

## 6. R4 — stochastic finite ensemble

Frozen sample paths:

~~~text
A:
  {0,0,1,1}

B:
  {0,1,2,2}

C:
  {0,0,0,1}
~~~

Both retained:

~~~text
SAMPLE_COUNT:
  3

EMPIRICAL_FINAL_STATE_MEAN:
  4/3

FINITE_ENSEMBLE_SUMMARY:
  established

EXACT_PROBABILITY_LAW:
  not claimed

DISTRIBUTIONAL_CONVERGENCE:
  not claimed

SEMANTIC_UNDERDETERMINATION:
  no
~~~

Result:

~~~text
BASELINE_MATCH
~~~

## 7. R5 — readout/status-transition/neighboring-method boundaries

R5A:

~~~text
O(2,5)=7
O(3,4)=7

(2,5)!=(3,4)

state identity from readout:
  not inferred
~~~

R5B:

~~~text
pre:
  APPLICABLE_BUT_UNDEFINED

post:
  DEFINED_ZERO

transition:
  retained as typed status/domain transition

undefined replaced by numeric zero before transition:
  no
~~~

R5C:

~~~text
simulate supplied policy:
  Simulation in scope

choose policy:
  Control handoff

future-world truth:
  Prediction handoff

live repeated lifecycle:
  Operation handoff
~~~

Result:

~~~text
BASELINE_MATCH
~~~

## 8. R6 — terminal pressure

Frozen subordinate states:

~~~text
OUT_OF_SCOPE
CONFLICTING
UNDERDETERMINED
BLOCKED
~~~

Both applied the frozen precedence and retained all lower states.

Final:

~~~text
SIMULATION_TASK_OUT_OF_SCOPE
~~~

Result:

~~~text
BASELINE_MATCH
~~~

## 9. Gain-axis execution

~~~text
G1 versioned task/model non-retroactivity:
  BASELINE_MATCH

G2 branch-complete hybrid/lineage discipline:
  BASELINE_MATCH

G3 numerical enclosure/error/maximum-claim discipline:
  BASELINE_MATCH

G4 stochastic ensemble/sample-coverage discipline:
  BASELINE_MATCH

G5 readout/status-transition/neighboring-method boundary discipline:
  BASELINE_MATCH

G6 terminal-precedence and lower-state retention discipline:
  BASELINE_MATCH

G7 deterministic ledger / equal-information / bounded-claim discipline:
  BASELINE_MATCH
~~~

Therefore:

~~~text
SIMULATION_METHOD_GAIN_STATUS:
  SIMULATION_NO_GAIN

STRONGEST_REASONABLE_BASELINE_SIMULATION:
  established_at_constructed_evidence_level
~~~

## 10. Frozen-score execution

~~~text
A1-A12:
  12/12 PASS

B1-B10:
  10/10 PASS

C1-C12:
  12/12 PASS

D1-D10:
  10/10 PASS

E1-E12:
  12/12 PASS

F1-F14:
  14/14 PASS

G1-G12:
  12/12 PASS

TOTAL_REQUIRED_CHECKS:
  82

PASSED:
  82

FAILED:
  0
~~~

## 11. Post-challenge state

~~~text
DIRECT_SIMULATION_PILOTS_ATTEMPTED:
  5

SUCCESSFUL_DIRECT_SIMULATION_PILOTS:
  5

POSITIVE_SIMULATION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_SIMULATION_CASES:
  1

METHOD_BOUNDARY_SIMULATION_CASES:
  1

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  12

BASELINE_SIMULATION_CASES:
  2

NO_GAIN_SIMULATION_CASES:
  2

STRONGEST_REASONABLE_BASELINE_SIMULATION:
  established_at_constructed_evidence_level

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

## 12. Interpretation lock

~~~text
STRONGEST_REASONABLE_BASELINE_AT_CONSTRUCTED_EVIDENCE_LEVEL
  !=
UNIVERSALLY_STRONGEST_POSSIBLE_BASELINE

NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
~~~

The result establishes only that the frozen strongest-reasonable constructed non-DSD baseline matched the frozen Simulation outputs under equal-information access.

It does not establish universal baseline equivalence, external validity, independent replication, method redundancy, or method superiority.

## 13. Next

Prospectively precommit and execute:

~~~text
SIM-CH-006
deterministic same-project retrace of SIM-CH-001~005
~~~

The retrace must construct and commit its reconstruction ledger before formal comparison against the historical result artifacts.
