# COMP-CH-005 — Strongest-Reasonable Non-DSD Computation Baseline Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-05**  
Challenge ID: `COMP-CH-005`  
Method: **Computation / DSD 계산론**  
Protocol: **Computation Protocol v0.1**  
Case class: `strongest_reasonable_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen comparator identities

~~~text
COMPUTATION_PROTOCOL_VERSION:
  v0.1

COMPUTATION_PROTOCOL_COMMIT:
  03b1b7463af6d3a34dc3693a19933e83a3917b4d

COMPUTATION_PROTOCOL_BLOB:
  4c4fe0b0616371b7df6aff9ce6a1ff7636c49da4

PREVIOUS_COMPETENT_BASELINE:
  COMP-CH-004
  B0_GENERIC_TYPED_COMPUTATION_PLANNER
  64/64 PASS / COMPUTATION_NO_GAIN
~~~

No Computation Protocol revision is allowed in response to this baseline.

## 2. Strong baseline identity

~~~text
BASELINE_ID:
  B1_STRONG_COMPUTATION_PLANNING_ENGINE

BASELINE_CLASS:
  strongest_reasonable_non_DSD_constructed_computation_planning_engine

BASELINE_USES_DSD_AXIOMS:
  no

BASELINE_USES_DSD_METHOD_LABELS_INTERNALLY:
  no

BASELINE_RECEIVES_EQUAL_INFORMATION:
  yes
~~~

B1 is materially stronger than B0.

B1 may use ordinary:

~~~text
versioned task / source / model / interface registries
program slicing and dependency-closure analysis
DAG and graph reachability
incremental-computation invalidation
content-addressed or semantic cache keys
memoization with version / regime / status locks
symbolic simplification and theorem discharge
abstract interpretation and interval propagation
finite-termination and supplied convergence checks
strongly connected component decomposition
fixed-point iteration only when supplied by the task
error-budget propagation and target-relative tolerance checks
representation-loss / collision sidecars
partial-order execution plans
dynamic transition invalidation
deterministic terminal-precedence engines
bounded maximum-claim generation
full deterministic evaluation ledgers
rerun manifests
~~~

B1 may derive consequences algorithmically from the same supplied records.

B1 may not receive hidden factual information unavailable to Computation and may not be weakened after precommit.

## 3. Strong baseline operation

~~~text
B1-1  freeze task/target/source/model/interface identities and versions
B1-2  freeze evaluation class, representation, completeness, and primary claim
B1-3  preserve typed status/applicability distinctions and unavailable-interface states
B1-4  compute exact or conservative dependency closure for the target
B1-5  separate semantic necessity from execution action
B1-6  assign fresh/reuse/symbolic/omit only from explicit validity rules
B1-7  require proof/justification records for omission, reuse, approximation,
      symbolic discharge, and locality pruning
B1-8  validate cache reuse by input/model/status/regime/transition/invalidation
B1-9  preserve aggregate/reduced-readout collisions and injectivity limits
B1-10 propagate interval/error budgets to the frozen target
B1-11 evaluate finite termination, SCC structure, and supplied closure conditions
B1-12 evaluate theorem/symbolic coverage only on its declared domain
B1-13 preserve transition/locality/propagation restrictions when supplied
B1-14 keep objective-based selection among sufficient plans as a separate
      optimization problem
B1-15 distinguish evaluable failure / blocked / conflict / unresolved / outside scope
B1-16 apply frozen terminal precedence while preserving subordinate states
B1-17 emit bounded computation plan/result and gain/fairness records
B1-18 emit deterministic ledgers and rerun manifest
~~~

## 4. Equal-information and fairness rule

Computation and B1 receive exactly the same claim-relevant records.

~~~text
EQUAL_INFORMATION_REQUIRED:
  yes

HIDDEN_FAVORABLE_INPUT_ALLOWED:
  no

BASELINE_WEAKENING_ALLOWED:
  no

POST_HOC_RULE_CHANGE_ALLOWED:
  no
~~~

B1 is not required to reconstruct DSD ontology or terminology.

Extra computational competence is allowed. Extra hidden factual information is not.

## 5. Strong subcase R1 — versioned dependency registry and non-retroactivity

Frozen task:

~~~text
TASK:
  R1-v1

target:
  Y

DEP-v1:
  a -> c -> Y
  b -> Y

DEP-v2:
  a -> c -> Y
  b has no path to Y
  d -> Y

task R1-v1 is bound to:
  DEP-v1
~~~

Expected both:

~~~text
required under R1-v1:
  {a,b,c,Y}

retroactive use of DEP-v2:
  prohibited

version provenance:
  retained

task terminal:
  ESTABLISHED
~~~

## 6. Strong subcase R2 — dependency slicing, semantic reuse, and collision guard

Frozen task:

~~~text
target:
  Z = p + q

dependency graph:
  p -> Z
  q -> Z
  r has no path to Z

cached p:
  value=7
  matching input/model/status/regime

cached q:
  value=5
  same reduced readout signature as a stale q record
  but stale record has mismatched model version

aggregation sidecar:
  reduced readout equality is noninjective on source states
~~~

Expected both:

~~~text
p:
  REUSE_VALID_RESULT

q:
  stale record rejected
  current valid record used if supplied
  otherwise fresh evaluation

r:
  OMIT_AS_TARGET_IRRELEVANT

aggregate/readout equality:
  not promoted to semantic reuse equivalence

task terminal:
  ESTABLISHED
~~~

Required guards:

~~~text
CACHE_HIT != SEMANTIC_REUSE_VALIDITY
SAME_REDUCED_READOUT != REUSE_EQUIVALENCE
OMITTED != PROVED_IRRELEVANT_WITHOUT_DEPENDENCY_JUSTIFICATION
~~~

## 7. Strong subcase R3 — symbolic coverage plus SCC/closure pressure

Frozen class:

~~~text
E:
  integers 0..1000

target:
  P(n): n(n+1) is even for all n in E

theorem:
  valid for all integers
~~~

Frozen graph side-task:

~~~text
graph:
  u1 -> u2
  u2 -> u1
  u2 -> out

SCC:
  {u1,u2}

closure interface:
  fixed-point iteration supplied
  monotone finite-height lattice supplied
  termination bound supplied
~~~

Expected both:

~~~text
P over E:
  symbolically discharged with complete declared coverage

SCC:
  preserved as recursive component

closure:
  established only from supplied fixed-point/termination interface

finite-DAG shortcut:
  not falsely applied to SCC

task terminal:
  ESTABLISHED
~~~

## 8. Strong subcase R4 — end-to-end error budget and target-relative sufficiency

Frozen pipeline:

~~~text
x -> A -> B -> decision

A approximation error:
  <= 0.2

B additional error:
  <= 0.3

error composition:
  additive upper bound

total error:
  <= 0.5

final readout:
  r = 11

target:
  decide whether true value > 10
~~~

Expected both:

~~~text
admissible interval:
  [10.5,11.5]

target:
  established true

resolution:
  sufficient for declared target

global numeric accuracy:
  not claimed

minimal resolution:
  not claimed
~~~

## 9. Strong subcase R5 — transition invalidation, objective handoff, and terminal pressure

Frozen obligations:

~~~text
Q1:
  cached q(2)=4 from REGIME-A
  current REGIME-B after transition tau
  no cross-transition equivalence supplied

Q2:
  two sufficient computation plans P1/P2
  runtime objective supplied
  choose faster plan requested

Q3:
  two admissible dependency interpretations
  required sets differ
  no resolver

Q4:
  required interface unavailable
~~~

Expected both:

~~~text
Q1:
  stale cross-regime reuse rejected
  q(2) fresh-evaluated if otherwise evaluable

Q2:
  objective-based choice handed to Optimization
  Computation state OUT_OF_SCOPE for that obligation

Q3:
  UNDERDETERMINED

Q4:
  BLOCKED

frozen precedence:
  OUT_OF_SCOPE > CONFLICTING > UNDERDETERMINED > BLOCKED >
  ESTABLISHED/PARTIAL/NOT_ESTABLISHED

task terminal:
  OUT_OF_SCOPE

lower Q3/Q4 states:
  retained

deterministic ledger:
  emitted

rerun manifest:
  emitted
~~~

## 10. Frozen gain axes

~~~text
G1 VERSIONED_DEPENDENCY_AND_NONRETROACTIVITY_GAIN
G2 TARGET_SLICING_REUSE_AND_COLLISION_DISCIPLINE_GAIN
G3 SYMBOLIC_COVERAGE_AND_RECURSIVE_CLOSURE_GAIN
G4 END_TO_END_ERROR_AND_TARGET_RESOLUTION_GAIN
G5 TRANSITION_INVALIDATION_OPTIMIZATION_HANDOFF_AND_TERMINAL_GAIN
G6 BOUNDED_MAXIMUM_CLAIM_GAIN
G7 DETERMINISTIC_LEDGER_AND_RERUN_MANIFEST_GAIN
~~~

Allowed per-axis result:

~~~text
DSD_ADVANTAGE_ESTABLISHED
BASELINE_MATCH
BASELINE_ADVANTAGE
UNRESOLVED
~~~

Overall rule:

~~~text
if Computation is protocol-nonconformant or wrong:
  FAIL

if one or more frozen axes establish a real DSD advantage
against the still-fair B1:
  COMPUTATION_GAIN_ESTABLISHED

if all seven axes are BASELINE_MATCH:
  COMPUTATION_NO_GAIN

if a baseline advantage appears:
  preserve BASELINE_ADVANTAGE
  do not relabel it as DSD gain

otherwise:
  COMPUTATION_GAIN_UNDERDETERMINED
~~~

## 11. Frozen scoring — 82 checks

### A. Immutable fairness — 10

~~~text
A1 Computation protocol identity frozen
A2 B1 identity/capabilities frozen
A3 R1-R5 frozen before execution
A4 equal-information rule frozen
A5 Computation hidden favorable inputs = 0
A6 B1 claim-relevant withheld inputs = 0
A7 B1 not weakened after precommit
A8 output/gain mapping frozen
A9 scoring frozen
A10 external application/evaluator not counted
~~~

### B. R1 versioned dependency registry — 12

~~~text
B1 Computation binds DEP-v1
B2 B1 binds DEP-v1
B3 Computation required set={a,b,c,Y}
B4 B1 same required set
B5 Computation retains b as required
B6 B1 retains b as required
B7 Computation does not import d from v2
B8 B1 does not import d from v2
B9 Computation prohibits retroactive v2 substitution
B10 B1 prohibits retroactive v2 substitution
B11 both retain dependency/version provenance
B12 corresponding terminals match
~~~

### C. R2 slicing / reuse / collision — 14

~~~text
C1 both identify p required
C2 both identify q required
C3 both identify r not required
C4 both validate p reuse
C5 both reject stale q record on model mismatch
C6 both do not equate reduced-readout equality with reuse validity
C7 both preserve noninjective sidecar
C8 both omit r only from target-relative dependency closure
C9 both preserve omission soundness record
C10 both preserve reuse invalidation provenance
C11 both keep semantic necessity separate from execution action
C12 both produce matching bounded plan
C13 both return ESTABLISHED
C14 neither infers performance gain
~~~

### D. R3 symbolic / recursive closure — 12

~~~text
D1 both freeze E=0..1000
D2 both use theorem domain all integers
D3 both establish complete declared coverage
D4 both symbolically discharge P
D5 both identify SCC {u1,u2}
D6 neither treats SCC as finite DAG
D7 both use supplied monotone finite-height fixed-point interface
D8 both establish supplied closure/termination only on declared scope
D9 neither generalizes fixed-point uniqueness
D10 both retain recursive closure provenance
D11 both return ESTABLISHED
D12 neither claims runtime gain
~~~

### E. R4 end-to-end error — 12

~~~text
E1 both retain A error <=0.2
E2 both retain B error <=0.3
E3 both use additive composition
E4 both derive total <=0.5
E5 both use readout 11
E6 both derive interval [10.5,11.5]
E7 both establish true value >10
E8 both mark resolution sufficient
E9 neither claims global accuracy
E10 neither claims minimal resolution
E11 both preserve error provenance
E12 corresponding terminals match
~~~

### F. R5 transition / handoff / terminal pressure — 14

~~~text
F1 both detect REGIME-A -> REGIME-B transition
F2 both reject stale cross-regime reuse
F3 both require fresh q(2) if evaluable
F4 both identify objective-based P1/P2 choice
F5 both hand Q2 to Optimization
F6 both mark Q2 OUT_OF_SCOPE for Computation
F7 both retain Q3 UNDERDETERMINED
F8 both retain Q4 BLOCKED
F9 both apply frozen terminal precedence
F10 both choose task terminal OUT_OF_SCOPE
F11 lower Q3 retained by both
F12 lower Q4 retained by both
F13 Computation deterministic ledger/rerun identifiers retained
F14 B1 deterministic ledger/rerun manifest emitted
~~~

### G. Comparative conclusion — 8

~~~text
G1 all five strong subcases scored from frozen evidence only
G2 seven gain axes scored from frozen outputs only
G3 terminology differences not counted as gain
G4 B1 extra unused competence not counted as baseline advantage
G5 DSD advantage recorded only if claim-relevant
G6 baseline advantage preserved if claim-relevant
G7 NO_GAIN preserved if all seven axes BASELINE_MATCH
G8 strongest-reasonable status limited to constructed-evidence level
   and no merger/deletion/absorption/permanent-redundancy conclusion inferred
~~~

~~~text
TOTAL_REQUIRED_CHECKS:
  82

PASS_THRESHOLD:
  82/82

PARTIAL_PASS_ALLOWED:
  no
~~~

Any mismatch remains visible.

## 12. Allowed counter changes on 82/82 PASS

~~~text
DIRECT_COMPUTATION_PILOTS_ATTEMPTED:
  4 -> 5

SUCCESSFUL_DIRECT_COMPUTATION_PILOTS:
  4 -> 5

BASELINE_COMPUTATION_CASES:
  1 -> 2
~~~

If all seven gain axes are `BASELINE_MATCH`:

~~~text
NO_GAIN_COMPUTATION_CASES:
  1 -> 2

STRONGEST_REASONABLE_BASELINE_COMPUTATION:
  established_at_constructed_evidence_level
~~~

Unchanged:

~~~text
POSITIVE_COMPUTATION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_COMPUTATION_CASES:
  1

METHOD_BOUNDARY_COMPUTATION_CASES:
  1

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  11

REPRODUCIBILITY_CASES:
  0

EXTERNAL_COMPUTATION_APPLICATIONS:
  0

INDEPENDENT_COMPUTATION_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established
~~~

## 13. Interpretation lock

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

A strongest-reasonable NO_GAIN result would mean only that a materially strong non-DSD computation-planning engine matched the claim-relevant Computation outputs on this frozen constructed workload under equal-information access.

## 14. Next

If the frozen strong workload completes without unresolved comparator weakness, proceed to deterministic same-project retrace as COMP-CH-006.
