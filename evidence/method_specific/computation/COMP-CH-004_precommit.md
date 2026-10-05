# COMP-CH-004 — Competent Non-DSD Computation Baseline Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-05**  
Challenge ID: `COMP-CH-004`  
Method: **Computation / DSD 계산론**  
Protocol: **Computation Protocol v0.1**  
Case class: `competent_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen DSD comparator

~~~text
COMPUTATION_PROTOCOL_COMMIT:
  03b1b7463af6d3a34dc3693a19933e83a3917b4d

COMPUTATION_PROTOCOL_BLOB:
  4c4fe0b0616371b7df6aff9ce6a1ff7636c49da4

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  T1-T18
~~~

No Computation Protocol rule may be changed in response to this baseline.

## 2. Baseline identity

~~~text
BASELINE_ID:
  B0_GENERIC_TYPED_COMPUTATION_PLANNER

BASELINE_CLASS:
  competent_non_DSD_constructed_computation_planner

BASELINE_USES_DSD_AXIOMS:
  no

BASELINE_USES_DSD_METHOD_LABELS_INTERNALLY:
  no

BASELINE_RECEIVES_EQUAL_INFORMATION:
  yes
~~~

B0 is intentionally competent. It may use ordinary typed records, dependency graphs, version locks, cache-coherence rules, error bounds, symbolic-coverage declarations, finite-closure tests, transition metadata, deterministic terminal precedence, and bounded-claim reporting.

It may not invoke Formation, Property, Static Aggregation, Dynamics, or DSD shared-core rules as theory. Terminology or repository organization is never counted as method gain.

## 3. B0 generic operation

~~~text
B0-1  freeze task / target / source / model / interface versions
B0-2  retain claim-relevant typed status and applicability distinctions
B0-3  freeze evaluation class, representation mode, and completeness scope
B0-4  freeze dependency / bridge / required-interface records
B0-5  compute target-relative required versus not-required obligations
B0-6  assign fresh / reuse / symbolic / omit / unresolved actions
B0-7  require explicit justification for every omission
B0-8  validate reuse against key, model, status, regime, transition,
      precedence, and invalidation rules
B0-9  retain readout/reduction collision and injectivity sidecars
B0-10 evaluate resolution and end-to-end error against the target
B0-11 evaluate finite termination / supplied convergence or closure claims
B0-12 evaluate symbolic coverage only on its declared domain
B0-13 preserve dynamic transition/locality constraints when supplied
B0-14 hand objective-based selection among sufficient plans to a
      separate optimization task
B0-15 distinguish NOT_ESTABLISHED / BLOCKED / CONFLICT /
      UNRESOLVED / OUTSIDE_SCOPE
B0-16 apply frozen task-terminal precedence and preserve lower states
B0-17 emit bounded plan/result plus comparator fairness and gain status
~~~

## 4. Equal-information rule

Computation and B0 receive the same claim-relevant:

~~~text
task / target / primary claim / maximum claim
source-model-interface identities and versions
evaluation-class identity / representation / completeness
typed statuses and applicability
dependency graph / bridge registry
required-interface availability
target-relevance rules
reuse keys / cache records / invalidation rules
aggregation or reduction collision sidecars
resolution / error / tolerance semantics
closure / termination declarations
symbolic theorem domain and coverage
transition / regime / lineage handoff records
candidate sufficient plans
objective-function presence or absence
terminal precedence
~~~

Neither side receives hidden favorable information.

B0 is not required to derive DSD ontology from first principles. It executes the same already-frozen task information.

## 5. Frozen fixtures

### Q1 — mixed fresh / reuse / sound omission

Reuse `COMP-CH-001-A`.

~~~text
target:
  Y = f(3) + g(4)

f(x):
  x^2

g(x):
  2x

units:
  u_f = f(3)
  u_g = g(4)
  u_h = h(5)
  u_Y = add(u_f,u_g)

dependency:
  u_f -> u_Y
  u_g -> u_Y
  u_h has no path to u_Y

cache:
  g(4)=8
  model/status/regime all match
  no transition invalidation

expected:
  required = {u_f,u_g,u_Y}
  fresh = {u_f,u_Y}
  reuse = {u_g}
  omit = {u_h}
  Y=17
  task terminal = ESTABLISHED
~~~

Both must preserve:

~~~text
REQUIRED_RESULT != FRESH_EVALUATION_REQUIRED
OMITTED != PROVED_IRRELEVANT_WITHOUT_JUSTIFICATION
CACHE_HIT != SEMANTIC_REUSE_VALIDITY
~~~

### Q2 — symbolic full-class discharge

Reuse `COMP-CH-001-B`.

~~~text
class:
  E = {n in Z : 0 <= n <= 100}

target:
  P(n): n(n+1) is even for every n in E

supplied theorem:
  for every integer n, one of n,n+1 is even

theorem domain:
  all integers

expected:
  symbolic coverage complete for declared class
  action = symbolic discharge
  task terminal = ESTABLISHED
  no runtime-speedup claim
~~~

### Q3 — sufficient resolution with information-loss guard

Reuse `COMP-CH-001-C`.

~~~text
target:
  decide whether s > 10

source states:
  c1=(4.4,6.2)
  c2=(6.2,4.4)

both:
  s=10.6

reduced readout:
  R(c1)=R(c2)=11

error:
  |s-r| <= 0.5

admissible interval:
  [10.5,11.5]

expected:
  resolution sufficient for target
  c1 != c2 retained
  equal readout not promoted to source identity
  reconstruction not claimed
  task terminal = ESTABLISHED
~~~

### Q4 — blocked / conflict / underdetermined computation states

Q4A reuses `COMP-CH-002-N2`.

~~~text
required dependency interface:
  unavailable

expected:
  obligation BLOCKED
  action BLOCKED
  task terminal BLOCKED
~~~

Q4B reuses `COMP-CH-002-N3`.

~~~text
same reuse key/model/regime/status
two applicable cache values:
  4
  5
resolver:
  none

expected:
  reuse interface CONFLICTING
  task terminal CONFLICTING
~~~

Q4C reuses `COMP-CH-002-N5`.

~~~text
two admissible dependency semantics
different required sets
resolver:
  none

expected:
  affected obligation UNDERDETERMINED
  task terminal UNDERDETERMINED
~~~

### Q5 — Optimization handoff and exact PARTIAL semantics

Q5A reuses `COMP-CH-002-N4`.

~~~text
P1:
  sufficient

P2:
  sufficient

requested:
  choose lower-runtime plan

objective:
  runtime

expected:
  objective-based selection is handed to Optimization
  Computation task terminal OUT_OF_SCOPE
~~~

Q5B reuses `COMP-CH-002-N6`.

~~~text
two independently required in-scope obligations

Q1:
  ESTABLISHED

Q2:
  evaluably NOT_ESTABLISHED

no:
  blocked
  conflicting
  underdetermined
  out-of-scope

expected:
  task terminal PARTIAL
~~~

### Q6 — transition invalidates otherwise valid reuse

New prospective fixture.

~~~text
task:
  compute Z = q(2) after transition tau

cached result:
  q(2)=4

cache provenance:
  MODEL-Q-v1
  REGIME-Q-A
  status defined/applicable

current state after tau:
  MODEL-Q-v1
  REGIME-Q-B

transition rule:
  tau invalidates cross-regime reuse unless
  an explicit cross-transition equivalence is supplied

cross-transition equivalence:
  not supplied

q(x):
  x^2

expected:
  cached result not reusable across tau
  q(2) remains REQUIRED_FOR_TARGET
  action = EVALUATE_FRESH
  fresh result = 4
  task terminal = ESTABLISHED
~~~

Both must preserve:

~~~text
SAME_VALUE != VALID_REUSE
REGULAR_EPOCH_REUSE != CROSS_TRANSITION_REUSE
REUSE_INVALIDATION != LINEAGE_IDENTITY_PROOF
~~~

## 6. Frozen gain axes

~~~text
G1 obligation / execution-action separation

G2 dependency / omission / required-interface soundness

G3 reuse / version / regime / transition invalidation discipline

G4 symbolic coverage / closure / resolution / information-loss discipline

G5 task-terminal / Optimization-handoff / bounded-claim discipline

G6 claim-relevant computation outcome and plan equivalence
   under equal-information access
~~~

Allowed axis result:

~~~text
DSD_ADVANTAGE_ESTABLISHED
BASELINE_MATCH
BASELINE_ADVANTAGE
UNRESOLVED
~~~

Overall gain rule:

~~~text
if all claim-relevant outputs and all six axes match:
  COMPUTATION_METHOD_GAIN_STATUS =
    COMPUTATION_NO_GAIN

if one or more frozen claim-relevant axes establish a DSD advantage:
  COMPUTATION_METHOD_GAIN_STATUS =
    COMPUTATION_GAIN_ESTABLISHED

if one or more axes establish a baseline advantage:
  preserve BASELINE_ADVANTAGE
  do not relabel it as DSD gain

otherwise:
  COMPUTATION_METHOD_GAIN_STATUS =
    COMPUTATION_GAIN_UNDERDETERMINED
~~~

Vocabulary is not a gain axis.

## 7. Frozen scoring — 64 checks

### A. Fairness and immutability — 10

~~~text
A1 Computation Protocol commit/blob fixed
A2 B0 operation frozen before execution
A3 output mappings frozen
A4 Q1-Q6 frozen before execution
A5 equal-information rule respected
A6 B0 receives every claim-relevant Computation-visible input
A7 Computation receives no hidden favorable input
A8 no post-hoc gain axis added
A9 no baseline rule changed after result inspection
A10 external application remains no
~~~

### B. Q1 mixed plan — 12

~~~text
B1 same target and graph
B2 u_f required on both
B3 u_g required on both
B4 u_h not required on both
B5 same cache metadata
B6 both establish reuse validity for u_g
B7 both fresh-evaluate u_f
B8 both omit u_h only from frozen target-irrelevance
B9 both compute Y=17
B10 both preserve required-result / fresh-action distinction
B11 both return established terminal
B12 neither claims optimal execution order
~~~

### C. Q2 symbolic coverage — 10

~~~text
C1 same declared class
C2 same theorem
C3 theorem domain covers declared class
C4 both mark complete declared coverage
C5 both symbolically discharge
C6 neither requires literal enumeration
C7 both return established terminal
C8 neither infers runtime gain
C9 no uncovered subclass fabricated
C10 bounded claim preserved
~~~

### D. Q3 resolution / information loss — 10

~~~text
D1 c1 != c2 retained
D2 both readouts equal 11
D3 collision retained
D4 injectivity not claimed
D5 same error bound 0.5
D6 same admissible interval [10.5,11.5]
D7 both establish s>10
D8 both mark resolution sufficient
D9 neither reconstructs source identity
D10 both return established terminal
~~~

### E. Q4 blocked / conflict / underdetermined — 10

~~~text
E1 both preserve unavailable required interface as BLOCKED
E2 neither converts unavailable to irrelevance
E3 both detect conflicting reuse records
E4 neither selects one cache value without a resolver
E5 both return CONFLICTING for Q4B
E6 both retain two admissible dependency semantics in Q4C
E7 both detect different required sets
E8 both return UNDERDETERMINED for Q4C
E9 BLOCKED / CONFLICTING / UNDERDETERMINED remain distinct
E10 all three corresponding terminals match
~~~

### F. Q5-Q6 handoff / partial / transition — 8

~~~text
F1 both hand objective-based selection outside Computation
F2 both return OUT_OF_SCOPE for Q5A
F3 both apply exact PARTIAL semantics in Q5B
F4 neither uses PARTIAL as atomic-failure rescue
F5 both detect transition invalidation in Q6
F6 both reject stale cross-regime reuse
F7 both fresh-evaluate q(2)=4 after transition
F8 both return ESTABLISHED for Q6
~~~

### G. Gain conclusion — 4

~~~text
G1 six gain axes scored only from frozen outputs
G2 equal-information fairness remains visible
G3 NO_GAIN preserved if all six axes are BASELINE_MATCH
G4 NO_GAIN does not imply failure/deletion/merger/absorption/redundancy
~~~

~~~text
TOTAL_REQUIRED_CHECKS:
  64

PASS_THRESHOLD:
  64/64

PARTIAL_PASS_ALLOWED:
  no
~~~

## 8. Allowed counter changes on 64/64 PASS

~~~text
DIRECT_COMPUTATION_PILOTS_ATTEMPTED:
  3 -> 4

SUCCESSFUL_DIRECT_COMPUTATION_PILOTS:
  3 -> 4

BASELINE_COMPUTATION_CASES:
  0 -> 1
~~~

If all six gain axes are `BASELINE_MATCH`:

~~~text
NO_GAIN_COMPUTATION_CASES:
  0 -> 1
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

## 9. Interpretation lock

A fair `NO_GAIN` result means only:

~~~text
no claim-relevant DSD Computation performance or decision-quality
advantage over this competent constructed baseline was established
for these frozen Computation tasks under equal-information access
~~~

It does not mean:

~~~text
Computation Protocol failure
method deletion
merger into Optimization
merger into Analysis
permanent redundancy
absence of organizational value
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

## 10. Next

After execution, if all frozen outputs match and the result is NO_GAIN, proceed to a strongest-reasonable non-DSD Computation baseline challenge.
