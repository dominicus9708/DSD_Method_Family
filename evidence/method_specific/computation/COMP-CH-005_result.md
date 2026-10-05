# COMP-CH-005 — Strongest-Reasonable Non-DSD Computation Baseline Result

Status: **EXECUTED — 82/82 PASS / NO_GAIN**  
Date: **2026-10-05**  
Challenge ID: `COMP-CH-005`  
Method: **Computation / DSD 계산론**  
Protocol: **Computation Protocol v0.1**  
Baseline: **B1_STRONG_COMPUTATION_PLANNING_ENGINE**

## 1. Frozen references

~~~text
COMPUTATION_PROTOCOL_COMMIT:
  03b1b7463af6d3a34dc3693a19933e83a3917b4d

COMPUTATION_PROTOCOL_BLOB:
  4c4fe0b0616371b7df6aff9ce6a1ff7636c49da4

PRECOMMIT_COMMIT:
  c49c96fe0f54d7f492e21261b30af14450b6c437

PRECOMMIT_BLOB:
  086b6cce2d39bc76e901199dcaadfd40e4fdecd4
~~~

No Computation Protocol rule, B1 capability, strong subcase, gain axis, scoring item, or pass threshold changed after precommit.

## 2. Final result

~~~text
TOTAL_REQUIRED_CHECKS:
  82

PASSED:
  82

FAILED:
  0

EQUAL_INFORMATION_ACCESS:
  yes

COMPUTATION_HIDDEN_ADVANTAGE_INPUTS:
  0

BASELINE_WITHHELD_CLAIM_RELEVANT_INPUTS:
  0

BASELINE_WEAKENED_AFTER_PRECOMMIT:
  no

COMPUTATION_METHOD_GAIN_STATUS:
  COMPUTATION_NO_GAIN

STRONGEST_REASONABLE_BASELINE_COMPUTATION:
  established_at_constructed_evidence_level

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

The materially stronger non-DSD B1 engine matched every claim-relevant Computation result on the frozen strong workload.

The strongest-reasonable label is bounded to this constructed comparator class and workload.

## 3. R1 — versioned dependency registry

Both Computation and B1 bind `R1-v1` to `DEP-v1`, retain:

~~~text
required:
  {a,b,c,Y}

retroactive DEP-v2 substitution:
  prohibited

d from DEP-v2:
  not imported

version provenance:
  retained

terminal:
  ESTABLISHED
~~~

Result:

~~~text
MATCH
~~~

## 4. R2 — target slicing / semantic reuse / collision discipline

Both identify:

~~~text
p:
  required
  valid reuse

q:
  required
  stale mismatched-model record rejected
  current valid record used if supplied; otherwise fresh

r:
  target-irrelevant under frozen dependency closure
  soundly omitted
~~~

Both preserve:

~~~text
CACHE_HIT != SEMANTIC_REUSE_VALIDITY
SAME_REDUCED_READOUT != REUSE_EQUIVALENCE
NONINJECTIVE_REDUCTION_SIDECAR:
  retained
SEMANTIC_NECESSITY != EXECUTION_ACTION
~~~

Both produce the same bounded computation plan and return `ESTABLISHED`.

Result:

~~~text
MATCH
~~~

## 5. R3 — symbolic coverage / recursive closure

For `E={0..1000}`, both use the supplied all-integer theorem to establish complete declared coverage and symbolically discharge `P(n)`.

For the recursive graph, both identify:

~~~text
SCC:
  {u1,u2}

FINITE_DAG_SHORTCUT:
  not applicable to SCC

supplied fixed-point interface:
  monotone
  finite-height
  termination bound supplied

closure:
  established on declared scope only
~~~

Neither promotes one supplied closure interface to general fixed-point uniqueness or universal recursive termination.

Result:

~~~text
MATCH
~~~

## 6. R4 — end-to-end error / target resolution

Both preserve:

~~~text
A error:
  <=0.2

B error:
  <=0.3

composition:
  additive

total error:
  <=0.5

readout:
  11

admissible interval:
  [10.5,11.5]
~~~

Both conclude:

~~~text
target true value >10:
  established

resolution:
  sufficient for declared target

global accuracy:
  not claimed

minimal resolution:
  not claimed
~~~

Result:

~~~text
MATCH
~~~

## 7. R5 — transition invalidation / Optimization handoff / terminal pressure

Both detect the `REGIME-A -> REGIME-B` transition and reject cross-regime reuse because no explicit transition-equivalence is supplied.

Both determine:

~~~text
Q1:
  stale reuse rejected
  fresh q(2) required if evaluable

Q2:
  objective-based selection among sufficient plans
  Optimization handoff required
  Computation obligation OUT_OF_SCOPE

Q3:
  UNDERDETERMINED

Q4:
  BLOCKED
~~~

With the frozen precedence:

~~~text
OUT_OF_SCOPE > CONFLICTING > UNDERDETERMINED > BLOCKED >
ESTABLISHED/PARTIAL/NOT_ESTABLISHED
~~~

both return:

~~~text
task terminal:
  OUT_OF_SCOPE

Q3 lower state:
  retained

Q4 lower state:
  retained

deterministic ledger:
  emitted

rerun manifest:
  emitted
~~~

Result:

~~~text
MATCH
~~~

## 8. Gain-axis execution

~~~text
G1 VERSIONED_DEPENDENCY_AND_NONRETROACTIVITY_GAIN:
  BASELINE_MATCH

G2 TARGET_SLICING_REUSE_AND_COLLISION_DISCIPLINE_GAIN:
  BASELINE_MATCH

G3 SYMBOLIC_COVERAGE_AND_RECURSIVE_CLOSURE_GAIN:
  BASELINE_MATCH

G4 END_TO_END_ERROR_AND_TARGET_RESOLUTION_GAIN:
  BASELINE_MATCH

G5 TRANSITION_INVALIDATION_OPTIMIZATION_HANDOFF_AND_TERMINAL_GAIN:
  BASELINE_MATCH

G6 BOUNDED_MAXIMUM_CLAIM_GAIN:
  BASELINE_MATCH

G7 DETERMINISTIC_LEDGER_AND_RERUN_MANIFEST_GAIN:
  BASELINE_MATCH
~~~

Overall:

~~~text
COMPUTATION_METHOD_GAIN_STATUS:
  COMPUTATION_NO_GAIN
~~~

No claim-relevant DSD Computation performance or decision-quality advantage was established over B1 on this frozen constructed strong workload under equal-information access.

## 9. Execution of the 82 frozen checks

~~~text
A immutable fairness: 10/10 PASS
B R1 versioned dependency registry: 12/12 PASS
C R2 slicing / reuse / collision: 14/14 PASS
D R3 symbolic / recursive closure: 12/12 PASS
E R4 end-to-end error: 12/12 PASS
F R5 transition / handoff / terminal pressure: 14/14 PASS
G comparative conclusion: 8/8 PASS

TOTAL_REQUIRED_CHECKS:
  82

PASSED:
  82

FAILED:
  0
~~~

## 10. Counter update

~~~text
DIRECT_COMPUTATION_PILOTS_ATTEMPTED:
  5

SUCCESSFUL_DIRECT_COMPUTATION_PILOTS:
  5

POSITIVE_COMPUTATION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_COMPUTATION_CASES:
  1

METHOD_BOUNDARY_COMPUTATION_CASES:
  1

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  11

BASELINE_COMPUTATION_CASES:
  2

NO_GAIN_COMPUTATION_CASES:
  2

STRONGEST_REASONABLE_BASELINE_COMPUTATION:
  established_at_constructed_evidence_level

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

## 11. Interpretation lock

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

This result does not establish external applicability, independent validation, independent replication, method redundancy, or method superiority.

## 12. Maximum-supported claim

Supported:

~~~text
Within the frozen COMP-CH-005 constructed comparator class,
B1_STRONG_COMPUTATION_PLANNING_ENGINE matched Computation Protocol
v0.1 on versioned dependency semantics, target slicing, semantic
reuse/invalidation, noninjective reduction guards, symbolic coverage,
recursive closure, end-to-end error propagation, target-relative
resolution, transition invalidation, Optimization handoff, terminal
precedence, bounded claims, and deterministic replay metadata.

All seven frozen gain axes were BASELINE_MATCH.
~~~

Not established:

~~~text
universal baseline optimality
method redundancy
external applicability
independent validation
independent replication
method superiority
~~~

## 13. Next

Prospectively precommit and execute `COMP-CH-006` deterministic same-project retrace.

The retrace must reconstruct the frozen claim-relevant COMP-CH-001~005 evidence from repository artifacts, compare independently reconstructed outputs against recorded outputs, preserve every mismatch, prohibit post-comparison correction, and keep:

~~~text
SAME_PROJECT_RETRACE != INDEPENDENT_REPLICATION
DETERMINISTIC_MATCH != INDEPENDENT_VALIDATION
~~~
