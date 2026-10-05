# DSD Optimization — Serious Pre-Protocol Boundary Attack v0.1

Status: **EXECUTED — 18 ATTACKS / 12 PRESERVED / 6 NONBREAKING REFINEMENTS / 0 COLLAPSE**  
Date: **2026-10-05**  
Method: **Optimization / DSD 최적화론**  
Target: **Task Interface v0.1 Draft**

Frozen target:

~~~text
TASK_INTERFACE_COMMIT:
  753206b90421bb317462e3cd214a280faf95e317

TASK_INTERFACE_BLOB:
  a3e3490a6a24d0793c608c85e6e0cb6a120f78f6
~~~

The Task Interface is immutable from this point forward.

All refinements identified below must be recorded in a separate amendment.

## 1. Attack rule

Each attack asks whether the frozen Task Interface can distinguish a claim-relevant failure or boundary without inventing a new method identity.

Allowed attack outcomes:

~~~text
PRESERVED_NO_REFINEMENT
PRESERVED_WITH_NONBREAKING_REFINEMENT
BOUNDARY_COLLAPSE
FUNDAMENTAL_INTERFACE_FAILURE
~~~

A nonbreaking refinement may add an explicit ledger, status family, lock, or precedence rule while preserving the same Inputs / Operation / Outputs / Failure-or-NO_GAIN / Validation identity.

## 2. A1 — undefined objective coerced to zero

Pressure:

~~~text
candidate c1:
  objective value = 4

candidate c2:
  objective value = undefined

requested rule:
  minimize objective
~~~

Invalid shortcut:

~~~text
undefined(c2) -> 0
therefore choose c2
~~~

Frozen interface already preserves:

~~~text
UNDEFINED_OBJECTIVE_VALUE != ZERO_OBJECTIVE_VALUE
~~~

Outcome:

~~~text
A1:
  PRESERVED_NO_REFINEMENT
~~~

## 3. A2 — inadmissible candidate with favorable score

Pressure:

~~~text
c1:
  admissible
  score = 10

c2:
  inadmissible
  score = 0

minimize score
~~~

The score does not repair inadmissibility.

Outcome:

~~~text
A2:
  PRESERVED_NO_REFINEMENT
~~~

## 4. A3 — hard constraint converted to penalty

Pressure:

~~~text
hard constraint:
  mass <= 10

candidate c:
  mass = 12

proposal:
  add penalty +5 and retain c as feasible
~~~

The interface correctly states:

~~~text
HARD_CONSTRAINT_VIOLATION != FINITE_PENALTY_BY_DEFAULT
~~~

However, it allows an explicit penalty transformation without yet binding the transformation's identity, provenance, version, target scope, and whether it changes the original task into a new soft-constrained task.

Outcome:

~~~text
A3:
  PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

Required refinement:

~~~text
R1 EXPLICIT_CONSTRAINT_TRANSFORMATION_LOCK
~~~

## 5. A4 — silent scalarization of multiple objectives

Pressure:

~~~text
minimize latency
minimize energy
no weights
no lexicographic rule
no Pareto rule
~~~

Invalid shortcut:

~~~text
latency + energy
~~~

The interface already rejects silent scalarization.

Outcome:

~~~text
A4:
  PRESERVED_NO_REFINEMENT
~~~

## 6. A5 — tied optimum mislabeled underdetermined

Pressure:

~~~text
c1 objective = 5
c2 objective = 5
single objective
exact equality
both feasible
~~~

The correct result may be a positive tied optimum set.

The interface directly preserves:

~~~text
TIED_OPTIMA != UNDERDETERMINED_BY_DEFAULT
~~~

Outcome:

~~~text
A5:
  PRESERVED_NO_REFINEMENT
~~~

## 7. A6 — Pareto set mislabeled unique optimum

Pressure:

~~~text
c1 better on objective A
c2 better on objective B
no scalarization
Pareto semantics declared
~~~

Neither candidate dominates the other.

The interface retains Pareto-set semantics and rejects unique-optimum promotion.

Outcome:

~~~text
A6:
  PRESERVED_NO_REFINEMENT
~~~

## 8. A7 — equal score used as structural identity

Pressure:

~~~text
score(c1) = score(c2)
c1 and c2 have distinct source structure
~~~

Equal objective readout does not establish candidate identity.

Outcome:

~~~text
A7:
  PRESERVED_NO_REFINEMENT
~~~

## 9. A8 — incomplete candidate set used for global optimum

Pressure:

~~~text
declared candidate set:
  {c1,c2,c3}

candidate completeness:
  not claimed

c2 best within declared set
~~~

Invalid claim:

~~~text
c2 is globally best among all real alternatives
~~~

The interface already separates declared-set optimum from global completeness.

Outcome:

~~~text
A8:
  PRESERVED_NO_REFINEMENT
~~~

## 10. A9 — overlapping uncertainty intervals used for strict order

Pressure:

~~~text
minimize objective

c1:
  interval [9,11]

c2:
  interval [10,12]
~~~

A point-estimate or endpoint shortcut cannot establish a strict robust ordering without a declared uncertainty-order rule.

The interface blocks the shortcut but does not yet expose a dedicated pairwise ordering disposition distinguishing:

~~~text
strictly ordered
tied
incomparable by declared partial order
unresolved because uncertainty overlaps
blocked
conflicting
out of scope
~~~

Outcome:

~~~text
A9:
  PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

Required refinement:

~~~text
R2 EXPLICIT_PAIR_ORDER_AND_UNCERTAINTY_STATUS
~~~

## 11. A10 — stale optimum reused across regime transition

Pressure:

~~~text
REGIME-A:
  c1 optimal

transition:
  A -> B

REGIME-B:
  objective values or feasibility may differ
~~~

The interface already freezes regime and invalidation semantics.

Outcome:

~~~text
A10:
  PRESERVED_NO_REFINEMENT
~~~

## 12. A11 — sufficient Computation plan mislabeled optimal

Pressure:

~~~text
Computation returns:
  plan P1 sufficient

another admissible plan:
  P2 also sufficient

no objective supplied
~~~

Selecting P1 as "optimal" is not licensed.

The Computation/Optimization boundary survives.

Outcome:

~~~text
A11:
  PRESERVED_NO_REFINEMENT
~~~

## 13. A12 — Comparison ranking substituted for Optimization

Pressure:

~~~text
Comparison says:
  c1 differs less from reference r than c2

Optimization objective:
  not supplied
~~~

Similarity or difference ordering is not automatically an Optimization objective.

Outcome:

~~~text
A12:
  PRESERVED_NO_REFINEMENT
~~~

## 14. A13 — one-time optimum promoted to Control policy

Pressure:

~~~text
current state s0:
  action a1 is optimal

request:
  use a1 at all future states
~~~

One-state Optimization does not establish a state-dependent Control policy.

Outcome:

~~~text
A13:
  PRESERVED_NO_REFINEMENT
~~~

## 15. A14 — lifecycle objective with omitted lifecycle component

Pressure:

~~~text
declared objective:
  minimize total lifecycle cost

known:
  build cost
  operating cost

unknown required component:
  disposal / reset cost
~~~

The interface distinguishes static from lifecycle optimization but does not yet require an explicit objective-component completeness / required-interface status for a compound objective.

Without this, a missing required component could be silently omitted.

Outcome:

~~~text
A14:
  PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

Required refinement:

~~~text
R3 OBJECTIVE_CONSTRAINT_DEPENDENCY_COMPLETENESS
~~~

## 16. A15 — aggregate / compressed objective collision ignored

Pressure:

~~~text
R(c1) = R(c2)
but source-level objective-relevant sidecar differs
~~~

The frozen interface preserves information-loss limits.

However, for selection claims it should bind whether the reduction preserves the exact declared pairwise order / dominance relation, rather than merely recording generic collision or injectivity information.

Outcome:

~~~text
A15:
  PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

Required refinement:

~~~text
R4 SELECTION_PRESERVATION_UNDER_REDUCTION
~~~

## 17. A16 — unfair baseline with unequal candidate information

Pressure:

~~~text
DSD-side optimizer:
  sees candidate set {c1,c2,c3}

baseline:
  sees {c1,c2}

claim:
  DSD method produces a better optimum
~~~

The frozen interface already requires comparator fairness, but the comparator schema should explicitly bind target equivalence, candidate-set equivalence, objective/constraint equivalence, uncertainty semantics, and regime/environment equivalence.

Outcome:

~~~text
A16:
  PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

Required refinement:

~~~text
R5 COMPARATOR_EQUIVALENCE_AND_FAIRNESS_LOCK
~~~

## 18. A17 — sound Optimization with NO_GAIN

Pressure:

~~~text
DSD Optimization result:
  valid selected set

competent baseline:
  same selected set / same cost / same evidence burden
~~~

The frozen interface allows:

~~~text
OPTIMIZATION_NO_GAIN
~~~

without declaring method failure.

Outcome:

~~~text
A17:
  PRESERVED_NO_REFINEMENT
~~~

## 19. A18 — terminal precedence and PARTIAL pressure

Pressure:

~~~text
task contains several independently required optimization obligations

one obligation:
  established

one:
  evaluably not established

one:
  blocked
~~~

The draft says PARTIAL is not allowed when blocked, but terminal precedence is explicitly provisional.

A second pressure:

~~~text
one sub-obligation out of scope
another conflicting
another blocked
~~~

The final terminal must not erase subordinate states.

Outcome:

~~~text
A18:
  PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

Required refinement:

~~~text
R6 EXACT_PRIMARY_TASK_TERMINAL_PRECEDENCE_AND_PARTIAL
~~~

## 20. Additional cross-attack observations

The eighteen attacks expose two distinctions that must be bound by the amendment but do not require a new method identity:

~~~text
INCOMPARABLE_BY_DECLARED_PARTIAL_ORDER
  !=
UNDERDETERMINED_SELECTION_SEMANTICS

MISSING_REQUIRED_OBJECTIVE_COMPONENT
  !=
OBJECTIVE_COMPONENT_IRRELEVANT
~~~

The first belongs to R2.

The second belongs to R3.

No attack requires merging Optimization into Computation, Comparison, Control, Operation, or another method.

## 21. Aggregate attack result

~~~text
PRE_PROTOCOL_BOUNDARY_ATTACKS:
  18

PRESERVED_NO_REFINEMENT:
  12

PRESERVED_WITH_NONBREAKING_REFINEMENT:
  6

BOUNDARY_COLLAPSE_FOUND:
  0

FUNDAMENTAL_INTERFACE_FAILURE:
  0

REFINEMENT_GROUPS_REQUIRED:
  6

BOUNDARY_AMENDMENT_REQUIRED:
  yes

PROTOCOL_FREEZE_AUTHORIZED_BEFORE_AMENDMENT:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

Refinement groups:

~~~text
R1 EXPLICIT_CONSTRAINT_TRANSFORMATION_LOCK

R2 EXPLICIT_PAIR_ORDER_AND_UNCERTAINTY_STATUS

R3 OBJECTIVE_CONSTRAINT_DEPENDENCY_COMPLETENESS

R4 SELECTION_PRESERVATION_UNDER_REDUCTION

R5 COMPARATOR_EQUIVALENCE_AND_FAIRNESS_LOCK

R6 EXACT_PRIMARY_TASK_TERMINAL_PRECEDENCE_AND_PARTIAL
~~~

## 22. Method-identity audit

The frozen five-interface identity remains unchanged.

~~~text
INPUTS:
  admissible candidates
  explicit objectives / constraints
  ordering / selection semantics
  objective / constraint evidence
  optional uncertainty / transition / handoff evidence

OPERATION:
  filter feasibility
  apply explicit objective / constraint / ordering semantics
  preserve multiplicity / ties / incomparability
  select only to the supported scope

OUTPUTS:
  feasible / infeasible / unresolved sets
  order / dominance ledger
  optimum / tied / Pareto / bounded set
  status / terminal / gain / maximum claim

FAILURE_OR_NO_GAIN:
  invalid candidate selection
  invented objective / scalarization
  unsupported order
  stale regime data
  neighboring-method substitution
  fair-baseline NO_GAIN

VALIDATION_STANDARD:
  selection follows from frozen candidate,
  objective, constraint, selection, uncertainty,
  version, regime, and handoff semantics
~~~

Therefore:

~~~text
METHOD_IDENTITY_CHANGED:
  no

TASK_INTERFACE_CORE_REOPENED:
  no
~~~

## 23. Next

Create **Optimization Task Interface Boundary Amendment 001** and bind R1-R6.

Do not freeze the executable Optimization Protocol until the amendment is adopted.
