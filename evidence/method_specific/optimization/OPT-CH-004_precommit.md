# OPT-CH-004 — Competent Non-DSD Optimization Baseline Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-05**  
Challenge ID: `OPT-CH-004`  
Method: **Optimization / DSD 최적화론**  
Protocol: **Optimization Protocol v0.1**  
Case class: `competent_baseline_constructed`  
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
  B0_GENERIC_TYPED_CONSTRAINED_SELECTOR

BASELINE_CLASS:
  competent_non_DSD_constructed_optimizer

BASELINE_USES_DSD_AXIOMS:
  no

BASELINE_USES_DSD_METHOD_LABELS_INTERNALLY:
  no

BASELINE_RECEIVES_EQUAL_INFORMATION:
  yes
~~~

B0 is intentionally competent.

It may use ordinary:

~~~text
typed candidate records
hard/soft constraints
explicit objective registries
single-objective sorting
lexicographic ordering
weighted scalarization when explicitly supplied
Pareto dominance
partial orders
tie handling
missing/conflicting/ambiguous-data states
interval uncertainty
robust pair-order rules
version/regime invalidation
reduced-readout preservation checks
deterministic terminal precedence
bounded-claim reporting
~~~

It may not invoke Formation, Property, Static Aggregation, Dynamics, or DSD shared-core rules as theory.

Terminology, file organization, or DSD naming is never counted as gain.

## 3. B0 generic operation

~~~text
B0-1  freeze task / candidate set / version / maximum claim
B0-2  retain candidate admissibility and nonnumeric missing states
B0-3  freeze objective definitions / directions / units / provenance
B0-4  freeze hard/soft constraint definitions and transformations
B0-5  verify required objective/constraint component completeness
B0-6  freeze single-/multi-objective selection semantics
B0-7  evaluate feasible / infeasible / unresolved candidate sets
B0-8  apply pairwise order / tie / Pareto / partial-order semantics
B0-9  propagate supplied uncertainty/error bounds into ordering
B0-10 verify reduced representation preserves the requested order
B0-11 preserve version/regime transition invalidation
B0-12 keep one-time selection separate from Control/Operation
B0-13 distinguish NOT_ESTABLISHED / BLOCKED / CONFLICTING /
      UNDERDETERMINED / OUT_OF_SCOPE
B0-14 apply frozen task-terminal precedence and exact PARTIAL rules
B0-15 emit selected set, bounded claim, fairness, and gain status
~~~

## 4. Equal-information rule

Optimization and B0 receive the same claim-relevant:

~~~text
task / primary claim / maximum claim
candidate set / representation / completeness
candidate admissibility and typed statuses
objective registry / direction / values / provenance
constraint registry / hard-soft status / transformations
required objective/constraint component registers
selection / dominance / tie / priority rules
uncertainty / interval / error semantics
reduction / collision / selection-preservation sidecars
source/model/version/regime/transition records
neighboring-method handoffs
terminal precedence
~~~

Neither side receives hidden favorable information.

B0 need not derive the DSD ontology from first principles. It executes the same already-frozen task information.

## 5. Frozen fixtures

### Q1 — unique optimum under hard constraint

Reuse `OPT-CH-001-A`.

~~~text
candidate set:
  {a,b,c,d}

hard constraint:
  resource <= 8

loss:
  a=9
  b=5
  c=1
  d=6

resource:
  a=6
  b=8
  c=10
  d=7

expected:
  feasible = {a,b,d}
  infeasible = {c}
  unique optimum = b
  terminal = ESTABLISHED
~~~

Both must preserve:

~~~text
FEASIBLE != OPTIMAL
HARD_CONSTRAINT_VIOLATION != FINITE_PENALTY_BY_DEFAULT
~~~

### Q2 — tied optimum and Pareto set

Q2A reuses `OPT-CH-001-B`.

~~~text
single objective:
  minimize cost

p=4
q=4
r=7

expected:
  tied optimum set = {p,q}
  terminal = ESTABLISHED
~~~

Q2B reuses `OPT-CH-001-C`.

~~~text
objectives:
  minimize latency
  minimize energy

x=(2,8)
y=(5,5)
z=(8,2)

selection rule:
  Pareto dominance

expected:
  Pareto set = {x,y,z}
  pairwise incomparability retained
  terminal = ESTABLISHED
~~~

Both must preserve:

~~~text
TIED_OPTIMA != UNDERDETERMINED
PARETO_NONDOMINATED != UNIQUE_OPTIMUM
INCOMPARABLE != UNDERDETERMINED
MULTIPLE_OBJECTIVES != WEIGHTED_SUM
~~~

### Q3 — uncertainty and reduction preservation

Reuse `OPT-CH-001-D`.

~~~text
u=[9.0,9.4]
v=[10.0,10.3]
w=[10.1,10.8]

strict robust rule:
  L preferred to R iff upper(L) < lower(R)

expected:
  u strictly outranks v
  u strictly outranks w
  v-vs-w strict order not established
  u unique robust optimum
~~~

Reduced readout:

~~~text
R(u)=9
R(v)=10
R(w)=10

preservation scope:
  top-selection claim for u over {v,w}
~~~

Expected:

~~~text
top-selection relation preserved
v/w readout collision not source equivalence
global injectivity not claimed
terminal = ESTABLISHED
~~~

### Q4 — blocked / conflicting / underdetermined states

Q4A reuses `OPT-CH-002-N2`.

~~~text
required lifecycle objective component:
  unavailable

expected:
  BLOCKED
~~~

Q4B reuses `OPT-CH-002-N3`.

~~~text
same objective identity/version
two incompatible applicable directions
no resolver

expected:
  CONFLICTING
~~~

Q4C reuses `OPT-CH-002-N5`.

~~~text
two admissible selection semantics
different selections
no resolver

expected:
  UNDERDETERMINED
~~~

Both evaluators must preserve the three states as distinct.

### Q5 — Control handoff and exact PARTIAL

Q5A reuses `OPT-CH-002-N4`.

~~~text
one-step action values:
  supplied

requested:
  state-dependent future policy

expected:
  handoff to Control
  Optimization terminal OUT_OF_SCOPE
~~~

Q5B reuses `OPT-CH-002-N6`.

~~~text
two independent required Optimization obligations

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

### Q6 — regime transition invalidates stale optimum

New prospective fixture.

~~~text
task:
  select lower-cost plan after transition tau

candidate set:
  {P1,P2}

REGIME-A values:
  P1 cost=4
  P2 cost=7
  -> P1 optimum

transition:
  REGIME-A -> REGIME-B

transition rule:
  claim-relevant cost values are invalidated
  unless explicit cross-regime value equivalence is supplied

cross-regime equivalence:
  not supplied

REGIME-B fresh values:
  P1 cost=8
  P2 cost=5

expected:
  REGIME-A values not reusable for REGIME-B selection
  fresh REGIME-B values used
  P2 unique optimum
  terminal = ESTABLISHED
~~~

Both must preserve:

~~~text
OPTIMUM_UNDER_REGIME_A != OPTIMUM_UNDER_REGIME_B
SAME_CANDIDATES != SAME_OBJECTIVE_VALUES_ACROSS_TRANSITION
STALE_VALUE != VALID_CURRENT_VALUE
~~~

## 6. Frozen gain axes

~~~text
G1 candidate-admissibility / objective / constraint discipline

G2 multi-objective / tie / Pareto / incomparability discipline

G3 uncertainty / reduction-selection-preservation discipline

G4 terminal / neighboring-method handoff / PARTIAL discipline

G5 version / regime / transition / bounded-claim discipline

G6 claim-relevant selection outcome equivalence
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
  OPTIMIZATION_METHOD_GAIN_STATUS =
    OPTIMIZATION_NO_GAIN

if one or more frozen claim-relevant axes establish a DSD advantage:
  OPTIMIZATION_METHOD_GAIN_STATUS =
    OPTIMIZATION_GAIN_ESTABLISHED

if one or more axes establish a baseline advantage:
  preserve BASELINE_ADVANTAGE
  do not relabel it as DSD gain

otherwise:
  OPTIMIZATION_METHOD_GAIN_STATUS =
    OPTIMIZATION_GAIN_UNDERDETERMINED
~~~

Vocabulary is not a gain axis.

## 7. Frozen scoring — 64 checks

### A. Fairness and immutability — 10

~~~text
A1 Optimization Protocol commit/blob fixed
A2 B0 operation frozen before execution
A3 output mappings frozen
A4 Q1-Q6 frozen before execution
A5 equal-information rule respected
A6 B0 receives every claim-relevant Optimization-visible input
A7 Optimization receives no hidden favorable input
A8 no post-hoc gain axis added
A9 no baseline rule changed after result inspection
A10 external application remains no
~~~

### B. Q1 hard constraint / unique optimum — 10

~~~text
B1 same candidate set
B2 same hard constraint
B3 same objective values
B4 a feasible on both
B5 b feasible on both
B6 c infeasible on both
B7 d feasible on both
B8 both select b
B9 both return established terminal
B10 neither converts c violation into finite penalty
~~~

### C. Q2 tie / Pareto — 10

~~~text
C1 same tied-objective fixture
C2 both retain p/q tie
C3 both return tied set {p,q}
C4 neither relabels tie underdetermined
C5 same two-objective Pareto fixture
C6 both retain all three nondominated candidates
C7 both preserve pairwise incomparability
C8 neither invents scalarization
C9 both return established terminal
C10 bounded claims match
~~~

### D. Q3 uncertainty / reduction — 10

~~~text
D1 same intervals
D2 same robust-order rule
D3 both establish u>v preference
D4 both establish u>w preference
D5 neither establishes strict v/w order
D6 both select u
D7 same reduced readout
D8 both establish top-selection preservation only
D9 neither infers v=w/source equivalence
D10 both avoid global-injectivity claim
~~~

### E. Q4 blocked / conflict / underdetermined — 10

~~~text
E1 both preserve missing required component as BLOCKED
E2 neither converts missing component to irrelevance/zero
E3 both detect conflicting objective semantics
E4 neither picks one conflicting objective record
E5 both return CONFLICTING for Q4B
E6 both retain two admissible selection semantics in Q4C
E7 both detect different selections
E8 both return UNDERDETERMINED for Q4C
E9 BLOCKED / CONFLICTING / UNDERDETERMINED remain distinct
E10 corresponding task terminals match
~~~

### F. Q5-Q6 handoff / partial / transition — 10

~~~text
F1 both hand future-state policy request to Control
F2 both return OUT_OF_SCOPE for Q5A
F3 both apply exact PARTIAL semantics in Q5B
F4 neither uses PARTIAL as atomic-failure rescue
F5 both detect REGIME-A -> REGIME-B invalidation
F6 neither reuses stale A costs without equivalence
F7 both use fresh B values
F8 both select P2 in REGIME-B
F9 both return ESTABLISHED for Q6
F10 bounded regime-specific claim retained
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
DIRECT_OPTIMIZATION_PILOTS_ATTEMPTED:
  3 -> 4

SUCCESSFUL_DIRECT_OPTIMIZATION_PILOTS:
  3 -> 4

BASELINE_OPTIMIZATION_CASES:
  0 -> 1
~~~

If all six gain axes are `BASELINE_MATCH`:

~~~text
NO_GAIN_OPTIMIZATION_CASES:
  0 -> 1
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

## 9. Interpretation lock

A fair `NO_GAIN` result means only:

~~~text
no claim-relevant DSD Optimization performance or
decision-quality advantage over this competent constructed
baseline was established for the frozen tasks under
equal-information access
~~~

It does not mean:

~~~text
Optimization Protocol failure
method deletion
merger into Computation
merger into Comparison
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

After execution, if all frozen outputs match and the result is NO_GAIN, proceed to a strongest-reasonable non-DSD Optimization baseline challenge.
