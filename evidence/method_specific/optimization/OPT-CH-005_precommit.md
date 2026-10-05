# OPT-CH-005 — Strongest-Reasonable Non-DSD Optimization Baseline Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-05**  
Challenge ID: `OPT-CH-005`  
Method: **Optimization / DSD 최적화론**  
Protocol: **Optimization Protocol v0.1**  
Case class: `strongest_reasonable_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen DSD comparator

~~~text
OPTIMIZATION_PROTOCOL_COMMIT:
  34584acd54af1bafef7dd176f795ed914eddc6b2

OPTIMIZATION_PROTOCOL_BLOB:
  5d2f9e37eab08bba27b0f416599df2e74a8c0c42

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  O1-O18
~~~

No Optimization Protocol rule may be changed in response to this baseline.

## 2. Baseline identity

~~~text
BASELINE_ID:
  B1_STRONG_OPTIMIZATION_ENGINE

BASELINE_CLASS:
  strongest_reasonable_non_DSD_constructed_optimizer

BASELINE_USES_DSD_AXIOMS:
  no

BASELINE_USES_DSD_METHOD_LABELS_INTERNALLY:
  no

BASELINE_RECEIVES_EQUAL_INFORMATION:
  yes

BASELINE_WEAKENING_AFTER_PRECOMMIT:
  prohibited
~~~

B1 is materially stronger than B0.

It may use ordinary, non-DSD mechanisms including:

~~~text
versioned candidate / objective / constraint registries
typed missing / conflicting / unresolved data states
finite exact enumeration
constraint propagation
branch-and-bound on supplied finite search spaces
lexicographic ordering
explicit weighted scalarization
Pareto-front extraction
partial-order / incomparability handling
exact tie-set retention
robust interval ordering
scenario-wise feasibility / objective evaluation
hard-to-soft transformation only when explicitly authorized
objective-component completeness checks
reduction/order-preservation sidecars
version/regime/transition invalidation
deterministic terminal-precedence engine
bounded maximum-claim generation
deterministic ledger / rerun manifest
fair-comparator metadata
~~~

B1 may choose any sound ordinary algorithm suitable for the frozen task.

It may not invoke Formation, Property, Static Aggregation, Dynamics, or DSD shared-core rules as theory.

## 3. Equal-information rule

Optimization and B1 receive exactly the same claim-relevant:

~~~text
task / version / primary claim / maximum claim
candidate set / representation / completeness
admissibility records
objective registries / values / directions / provenance
constraint registries / values / types / provenance
explicit constraint transformations
component completeness ledgers
selection / dominance / tie / priority semantics
uncertainty / interval / scenario semantics
reduction / collision / order-preservation sidecars
source/model/version/regime/transition records
Computation / Measurement / Simulation / Prediction /
Control / Operation handoffs when supplied
terminal precedence
~~~

No hidden favorable inputs are supplied to either side.

## 4. R1 — versioned non-retroactive optimization task

Frozen task v1:

~~~text
TASK_VERSION:
  v1

candidate set:
  {A,B,C}

objective O-v1:
  minimize monetary cost

cost:
  A=9
  B=6
  C=8

constraint:
  all three admissible
~~~

Expected v1:

~~~text
unique optimum:
  B
~~~

After v1 is frozen, a newer registry is supplied:

~~~text
O-v2:
  monetary cost + carbon penalty

score-v2:
  A=11
  B=13
  C=9
~~~

Expected:

~~~text
TASK-v1 remains bound to O-v1
v1 optimum remains B
O-v2 does not retroactively rewrite v1
new v2 task may select C
version provenance retained
~~~

Guards:

~~~text
NEWER_OBJECTIVE_VERSION != RETROACTIVE_REINTERPRETATION
TASK_VERSION_LOCK != LATEST_REGISTRY_WINS
~~~

## 5. R2 — finite constrained search with explicit transformation boundary

Frozen candidate family:

~~~text
x in integers 0..10
~~~

Hard constraints:

~~~text
3 <= x <= 8
~~~

Objective:

~~~text
minimize (x-6)^2
~~~

Expected:

~~~text
feasible x:
  {3,4,5,6,7,8}

unique optimum:
  x=6

objective value:
  0
~~~

A proposed alternate rule is also supplied:

~~~text
relax upper bound x<=8
into penalty 100*max(0,x-8)
~~~

but:

~~~text
TRANSFORMATION_AUTHORIZATION:
  not granted for task v1
~~~

Expected:

~~~text
v1 uses the hard constraint unchanged
unauthorized relaxation does not alter feasibility
unique optimum remains x=6
~~~

Both B1 and Optimization may use exact enumeration, branch-and-bound, or another sound finite method.

Algorithm choice itself is not a gain axis.

## 6. R3 — Pareto / partial-order multiplicity

Candidate values:

~~~text
a:
  cost=4
  risk=8
  latency=2

b:
  cost=5
  risk=5
  latency=5

c:
  cost=8
  risk=4
  latency=3
~~~

All three objectives are minimized.

Selection semantics:

~~~text
PARETO_DOMINANCE
no scalarization
no lexicographic priority
~~~

Expected:

~~~text
a, b, c are all nondominated

PARETO_SET:
  {a,b,c}

a vs b:
  incomparable

b vs c:
  incomparable

a vs c:
  incomparable

no unique optimum fabricated
terminal:
  ESTABLISHED
~~~

## 7. R4 — robust uncertainty + reduction-order preservation

Candidate objective intervals:

~~~text
u:
  [4.0,4.3]

v:
  [4.8,5.1]

w:
  [5.0,5.6]
~~~

Strict robust preference:

~~~text
L preferred to R iff upper(L) < lower(R)
~~~

Expected:

~~~text
u strictly preferred to v
u strictly preferred to w
v-vs-w strict order not established

u:
  unique robust optimum
~~~

Reduced representation:

~~~text
R = round interval midpoint to one decimal

R(u)=4.2
R(v)=5.0
R(w)=5.3
~~~

A collision sidecar for an alternate source pair is supplied to demonstrate that R is not globally injective.

Expected:

~~~text
selection relation for u over {v,w}:
  preserved

global injectivity:
  not claimed

source identity:
  not inferred
~~~

## 8. R5 — regime invalidation / handoffs / terminal pressure

### R5A — regime invalidation

~~~text
REGIME-A:
  P1 cost=4
  P2 cost=6
  P1 optimum

transition:
  A -> B

cross-regime equivalence:
  not supplied

REGIME-B:
  P1 cost=9
  P2 cost=5
~~~

Expected:

~~~text
stale A values rejected
P2 selected in B
~~~

### R5B — neighboring-method handoffs

Q1:

~~~text
request:
  choose best one-step action at frozen state s0

objective:
  supplied

expected:
  Optimization in scope
~~~

Q2:

~~~text
request:
  produce state-dependent future intervention policy

expected:
  Control handoff
  OUT_OF_SCOPE for Optimization
~~~

Q3:

~~~text
request:
  manage repeated execution / monitoring / reset / handoff
  over an operational lifecycle

expected:
  Operation handoff
  OUT_OF_SCOPE for Optimization
~~~

### R5C — terminal pressure

Independent required obligations:

~~~text
Q2:
  OUT_OF_SCOPE

Q4:
  CONFLICTING

Q5:
  UNDERDETERMINED

Q6:
  BLOCKED
~~~

Expected final task terminal:

~~~text
OPTIMIZATION_TASK_OUT_OF_SCOPE
~~~

with lower states retained.

## 9. Frozen gain axes

~~~text
G1 versioned task / objective / non-retroactivity discipline

G2 constrained-search / admissibility / transformation discipline

G3 multi-objective / Pareto / partial-order multiplicity discipline

G4 uncertainty / reduction / order-preservation discipline

G5 regime invalidation / Control-Operation handoff / terminal discipline

G6 bounded maximum claim / no hidden scalarization or globality

G7 deterministic ledger / rerun-manifest and equal-information discipline
~~~

Allowed axis result:

~~~text
DSD_ADVANTAGE_ESTABLISHED
BASELINE_MATCH
BASELINE_ADVANTAGE
UNRESOLVED
~~~

Overall rule:

~~~text
if all seven axes and claim-relevant outputs match:
  OPTIMIZATION_METHOD_GAIN_STATUS =
    OPTIMIZATION_NO_GAIN

if a frozen axis establishes a DSD advantage:
  OPTIMIZATION_GAIN_ESTABLISHED

if a frozen axis establishes a B1 advantage:
  preserve BASELINE_ADVANTAGE

otherwise:
  OPTIMIZATION_GAIN_UNDERDETERMINED
~~~

## 10. Strongest-reasonable interpretation rule

On full pass with equal-information access:

~~~text
STRONGEST_REASONABLE_BASELINE_OPTIMIZATION:
  established_at_constructed_evidence_level
~~~

This must not be interpreted as:

~~~text
UNIVERSALLY_STRONGEST_POSSIBLE_BASELINE
~~~

Required guards:

~~~text
STRONGEST_REASONABLE_AT_CONSTRUCTED_EVIDENCE_LEVEL
  !=
UNIVERSALLY_STRONGEST_POSSIBLE_BASELINE

NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
~~~

## 11. Frozen scoring — 82 checks

### A. Fairness / baseline strength / immutability — 12

~~~text
A1 Optimization Protocol commit/blob fixed
A2 B1 identity frozen
A3 B1 materially stronger than B0
A4 B1 operation frozen before execution
A5 R1-R5 frozen before execution
A6 equal-information access
A7 B1 receives every claim-relevant Optimization-visible input
A8 Optimization receives no hidden favorable input
A9 no baseline weakening after precommit
A10 no post-hoc gain axis
A11 external application remains no
A12 strongest-reasonable label bounded to constructed evidence
~~~

### B. R1 version / non-retroactivity — 12

~~~text
B1 v1 task frozen
B2 O-v1 frozen
B3 values 9/6/8 retained
B4 both select B under v1
B5 O-v2 arrives later
B6 O-v2 values retained
B7 neither retroactively rewrites v1
B8 new v2 task may select C
B9 version provenance retained
B10 latest-registry-wins rejected
B11 v1 bounded claim retained
B12 outputs match
~~~

### C. R2 constrained search / transformation — 12

~~~text
C1 integer class 0..10 frozen
C2 hard constraints 3<=x<=8 frozen
C3 objective frozen
C4 feasible set exactly {3,4,5,6,7,8}
C5 x=6 feasible
C6 objective at x=6 equals 0
C7 x=6 unique optimum
C8 proposed penalty transformation retained
C9 transformation unauthorized
C10 unauthorized transformation does not change feasibility
C11 algorithm choice not treated as method gain
C12 outputs match
~~~

### D. R3 Pareto / partial order — 12

~~~text
D1 candidate values frozen
D2 three objectives frozen
D3 Pareto rule frozen
D4 no scalarization supplied
D5 a nondominated
D6 b nondominated
D7 c nondominated
D8 Pareto set exactly {a,b,c}
D9 pairwise incomparability retained
D10 no unique optimum fabricated
D11 terminal ESTABLISHED
D12 outputs match
~~~

### E. R4 uncertainty / reduction — 12

~~~text
E1 intervals frozen
E2 robust-order rule frozen
E3 u strictly outranks v
E4 u strictly outranks w
E5 v-vs-w strict order not established
E6 u unique robust optimum
E7 reduced values retained
E8 top-selection relation preserved
E9 collision sidecar retained
E10 no global injectivity claim
E11 no source-identity inference
E12 outputs match
~~~

### F. R5 transition / handoffs / terminal — 12

~~~text
F1 REGIME-A values frozen
F2 A optimum P1
F3 transition A->B frozen
F4 no cross-regime equivalence
F5 stale A values rejected
F6 fresh B values select P2
F7 one-step Optimization remains in scope
F8 future policy handed to Control
F9 lifecycle execution handed to Operation
F10 lower CONFLICTING/UNDERDETERMINED/BLOCKED states retained
F11 final terminal OUT_OF_SCOPE
F12 outputs match
~~~

### G. Gain conclusion — 10

~~~text
G1 seven gain axes scored only from frozen outputs
G2 G1 axis BASELINE_MATCH
G3 G2 axis BASELINE_MATCH
G4 G3 axis BASELINE_MATCH
G5 G4 axis BASELINE_MATCH
G6 G5 axis BASELINE_MATCH
G7 G6 axis BASELINE_MATCH
G8 G7 axis BASELINE_MATCH
G9 overall OPTIMIZATION_NO_GAIN follows
G10 strongest-reasonable constructed-evidence status follows without universalization
~~~

~~~text
TOTAL_REQUIRED_CHECKS:
  82

PASS_THRESHOLD:
  82/82

PARTIAL_PASS_ALLOWED:
  no
~~~

## 12. Allowed counter changes on 82/82 PASS

~~~text
DIRECT_OPTIMIZATION_PILOTS_ATTEMPTED:
  4 -> 5

SUCCESSFUL_DIRECT_OPTIMIZATION_PILOTS:
  4 -> 5

BASELINE_OPTIMIZATION_CASES:
  1 -> 2
~~~

If all seven gain axes are `BASELINE_MATCH`:

~~~text
NO_GAIN_OPTIMIZATION_CASES:
  1 -> 2

STRONGEST_REASONABLE_BASELINE_OPTIMIZATION:
  established_at_constructed_evidence_level
~~~

Unchanged:

~~~text
POSITIVE_OPTIMIZATION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_OPTIMIZATION_CASES:
  1

METHOD_BOUNDARY_OPTIMIZATION_CASES:
  1

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  11

REPRODUCIBILITY_CASES:
  0

EXTERNAL_OPTIMIZATION_APPLICATIONS:
  0

INDEPENDENT_OPTIMIZATION_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established
~~~

## 13. Next

On full pass, prospectively precommit and execute `OPT-CH-006`, a deterministic same-project retrace of OPT-CH-001~005.

The retrace must freeze its reconstruction ledger before formal comparison with the historical result artifacts.
