# COMP-CH-004 — Competent Non-DSD Computation Baseline Result

Status: **EXECUTED — 64/64 PASS / NO_GAIN**  
Date: **2026-10-05**  
Challenge ID: `COMP-CH-004`  
Method: **Computation / DSD 계산론**  
Protocol: **Computation Protocol v0.1**  
Baseline: **B0_GENERIC_TYPED_COMPUTATION_PLANNER**

## 1. Frozen references

~~~text
COMPUTATION_PROTOCOL_COMMIT:
  03b1b7463af6d3a34dc3693a19933e83a3917b4d

COMPUTATION_PROTOCOL_BLOB:
  4c4fe0b0616371b7df6aff9ce6a1ff7636c49da4

PRECOMMIT_COMMIT:
  ba7cb32f760d6d7502cf1056fb20a02a7d830d93

PRECOMMIT_BLOB:
  f57876c7127953a7d5b81fdefa991f75fb4ebe30
~~~

No Computation Protocol rule, B0 operation, fixture, gain axis, scoring item, or pass threshold changed after precommit.

## 2. Final result

~~~text
TOTAL_REQUIRED_CHECKS:
  64

PASSED:
  64

FAILED:
  0

EQUAL_INFORMATION_ACCESS:
  yes

COMPUTATION_HIDDEN_ADVANTAGE_INPUTS:
  0

BASELINE_WITHHELD_CLAIM_RELEVANT_INPUTS:
  0

COMPUTATION_METHOD_GAIN_STATUS:
  COMPUTATION_NO_GAIN

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

The competent generic typed computation planner reproduced the claim-relevant Computation outcomes for every frozen fixture under equal-information access.

## 3. Q1 — mixed fresh / reuse / omission

Both evaluators receive the same target, graph, cache metadata, model/status/regime locks, and omission justification.

Both produce:

~~~text
required:
  {u_f,u_g,u_Y}

fresh:
  {u_f,u_Y}

reuse:
  {u_g}

sound omission:
  {u_h}

f(3):
  9

g(4):
  8

Y:
  17

terminal:
  ESTABLISHED
~~~

Both preserve:

~~~text
REQUIRED_RESULT != FRESH_EVALUATION_REQUIRED
CACHE_HIT != SEMANTIC_REUSE_VALIDITY
OMISSION_REQUIRES_TARGET_RELATIVE_JUSTIFICATION
~~~

Claim-relevant result:

~~~text
MATCH
~~~

## 4. Q2 — symbolic full-class discharge

Both receive the same class and theorem:

~~~text
E:
  integers 0..100

P(n):
  n(n+1) is even

theorem domain:
  all integers
~~~

Both determine:

~~~text
coverage:
  complete for declared class

action:
  symbolic discharge

literal enumeration:
  not required

terminal:
  ESTABLISHED

runtime gain:
  not inferred
~~~

Claim-relevant result:

~~~text
MATCH
~~~

## 5. Q3 — resolution sufficiency / information-loss guard

Both retain:

~~~text
c1:
  (4.4,6.2)

c2:
  (6.2,4.4)

c1 != c2:
  yes

R(c1)=R(c2):
  11

collision:
  retained

ordered-source injectivity:
  not established

error bound:
  0.5

admissible interval:
  [10.5,11.5]
~~~

Both conclude:

~~~text
target s>10:
  established

resolution:
  sufficient for declared target

source reconstruction:
  not claimed

terminal:
  ESTABLISHED
~~~

Claim-relevant result:

~~~text
MATCH
~~~

## 6. Q4 — blocked / conflicting / underdetermined states

### Q4A

Required dependency interface is unavailable.

Both return:

~~~text
obligation:
  BLOCKED

action:
  BLOCKED

task terminal:
  BLOCKED
~~~

Neither converts missing dependency information into irrelevance.

### Q4B

Two applicable cache records under identical frozen semantics disagree.

Both return:

~~~text
reuse coherence:
  CONFLICTING

selected cache value:
  none

task terminal:
  CONFLICTING
~~~

### Q4C

Two admissible dependency semantics yield different required sets and no resolver is supplied.

Both return:

~~~text
affected obligation:
  UNDERDETERMINED

task terminal:
  UNDERDETERMINED
~~~

The three states remain distinct.

Claim-relevant result:

~~~text
MATCH
~~~

## 7. Q5 — Optimization handoff / PARTIAL

### Q5A

Two sufficient plans and an explicit runtime objective are supplied.

Both determine:

~~~text
objective-based plan selection:
  separate Optimization task

Computation optimum:
  not fabricated

task terminal:
  OUT_OF_SCOPE
~~~

### Q5B

Two independently required in-scope obligations are supplied.

~~~text
Q1:
  ESTABLISHED

Q2:
  evaluably NOT_ESTABLISHED

blocked:
  no

conflicting:
  no

underdetermined:
  no

out_of_scope:
  no
~~~

Both return:

~~~text
task terminal:
  PARTIAL
~~~

Neither uses PARTIAL as an atomic-failure rescue label.

Claim-relevant result:

~~~text
MATCH
~~~

## 8. Q6 — transition-invalidated reuse

Frozen cache:

~~~text
q(2)=4
MODEL-Q-v1
REGIME-Q-A
defined/applicable
~~~

Current post-transition state:

~~~text
MODEL-Q-v1
REGIME-Q-B
~~~

The frozen transition rule invalidates cross-regime reuse unless explicit cross-transition equivalence is supplied.

No such equivalence is supplied.

Both evaluators therefore determine:

~~~text
q(2):
  REQUIRED_FOR_TARGET

cached result:
  not reusable on current scope

action:
  EVALUATE_FRESH

fresh result:
  4

terminal:
  ESTABLISHED
~~~

Both preserve:

~~~text
SAME_VALUE != VALID_REUSE
REGULAR_EPOCH_REUSE != CROSS_TRANSITION_REUSE
REUSE_INVALIDATION != LINEAGE_IDENTITY_PROOF
~~~

Claim-relevant result:

~~~text
MATCH
~~~

## 9. Gain-axis execution

~~~text
G1 obligation / execution-action separation:
  BASELINE_MATCH

G2 dependency / omission / required-interface soundness:
  BASELINE_MATCH

G3 reuse / version / regime / transition invalidation discipline:
  BASELINE_MATCH

G4 symbolic coverage / closure / resolution / information-loss discipline:
  BASELINE_MATCH

G5 task-terminal / Optimization-handoff / bounded-claim discipline:
  BASELINE_MATCH

G6 claim-relevant computation outcome and plan equivalence:
  BASELINE_MATCH
~~~

Overall:

~~~text
COMPUTATION_METHOD_GAIN_STATUS:
  COMPUTATION_NO_GAIN
~~~

This is a bounded constructed baseline result. It does not establish universal baseline equivalence or method redundancy.

## 10. Execution of the 64 frozen checks

### A — fairness and immutability

~~~text
A1 PASS
A2 PASS
A3 PASS
A4 PASS
A5 PASS
A6 PASS
A7 PASS
A8 PASS
A9 PASS
A10 PASS

A: 10/10
~~~

### B — Q1 mixed plan

~~~text
B1 PASS
B2 PASS
B3 PASS
B4 PASS
B5 PASS
B6 PASS
B7 PASS
B8 PASS
B9 PASS
B10 PASS
B11 PASS
B12 PASS

B: 12/12
~~~

### C — Q2 symbolic coverage

~~~text
C1 PASS
C2 PASS
C3 PASS
C4 PASS
C5 PASS
C6 PASS
C7 PASS
C8 PASS
C9 PASS
C10 PASS

C: 10/10
~~~

### D — Q3 resolution / information loss

~~~text
D1 PASS
D2 PASS
D3 PASS
D4 PASS
D5 PASS
D6 PASS
D7 PASS
D8 PASS
D9 PASS
D10 PASS

D: 10/10
~~~

### E — Q4 blocked / conflict / underdetermined

~~~text
E1 PASS
E2 PASS
E3 PASS
E4 PASS
E5 PASS
E6 PASS
E7 PASS
E8 PASS
E9 PASS
E10 PASS

E: 10/10
~~~

### F — Q5-Q6 handoff / partial / transition

~~~text
F1 PASS
F2 PASS
F3 PASS
F4 PASS
F5 PASS
F6 PASS
F7 PASS
F8 PASS

F: 8/8
~~~

### G — gain conclusion

~~~text
G1 PASS
G2 PASS
G3 PASS
G4 PASS

G: 4/4
~~~

Final:

~~~text
TOTAL_REQUIRED_CHECKS:
  64

PASSED:
  64

FAILED:
  0
~~~

## 11. Counter update

~~~text
DIRECT_COMPUTATION_PILOTS_ATTEMPTED:
  4

SUCCESSFUL_DIRECT_COMPUTATION_PILOTS:
  4

POSITIVE_COMPUTATION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_COMPUTATION_CASES:
  1

METHOD_BOUNDARY_COMPUTATION_CASES:
  1

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  11

BASELINE_COMPUTATION_CASES:
  1

NO_GAIN_COMPUTATION_CASES:
  1

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

## 12. Interpretation lock

The result means:

~~~text
No claim-relevant DSD Computation performance or decision-quality
advantage over B0_GENERIC_TYPED_COMPUTATION_PLANNER was established
for the frozen constructed tasks under equal-information access.
~~~

It does not mean:

~~~text
Computation Protocol failure
Computation method deletion
Computation must merge into Optimization
Computation must merge into Analysis
permanent redundancy
absence of theoretical or organizational value
future DSD gain is impossible
~~~

Required guards:

~~~text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
~~~

## 13. Maximum-supported claim

Supported:

~~~text
At the competent constructed baseline level and under equal
claim-relevant information, a generic typed computation planner
reproduced the frozen Computation outcomes for mixed
fresh/reuse/omission planning, symbolic coverage, resolution
sufficiency, information-loss discipline, blocked/conflicting/
underdetermined states, Optimization handoff, PARTIAL semantics,
and transition-invalidated reuse.

No DSD-specific gain was established on the six frozen gain axes.
~~~

Not established:

~~~text
strongest-reasonable baseline equivalence
universal baseline equivalence
external applicability
independent validation
independent replication
method redundancy
method superiority
~~~

## 14. Next

Prospectively precommit and execute a strongest-reasonable non-DSD Computation baseline challenge.

The next baseline must be materially stronger than B0 without importing DSD as theory, must receive equal claim-relevant information, and must preserve `COMPUTATION_NO_GAIN` as an allowed outcome.
