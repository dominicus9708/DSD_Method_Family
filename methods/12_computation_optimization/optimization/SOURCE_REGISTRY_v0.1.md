# DSD Optimization — Source / Registry Recovery v0.1

Status: **SOURCE / REGISTRY RECOVERY COMPLETE — PRE-TASK-INTERFACE**  
Date: **2026-10-05**  
Method: **Optimization / DSD 최적화론**  
Legacy path ID: `12B`  
Higher field: **VII. Computation & Selection / 계산·선택**

This document recovers source constraints and the current method-registry boundary for Optimization before any Task Interface is frozen.

It is not an Optimization protocol and does not itself authorize a protocol freeze.

## 1. Current registry identity

Current repository definition:

~~~text
Task:
  choose among admissible computational, structural,
  scheduling, or resource-allocation alternatives
  under explicit objectives and constraints

Candidate operations:
  objective / constraint declaration
  resource allocation across channels
  precision / lifetime / reuse / reset / scheduling trade-offs
  multi-objective comparison without collapsing incompatible costs prematurely
  optimization over only structurally admissible candidates

Boundary:
  Optimization begins after the feasible / admissible space
  and objective are justified

  DSD does not supply a universal objective function
~~~

Current GitHub path:

~~~text
methods/12_computation_optimization/optimization/
~~~

Registry boundary with Computation:

~~~text
COMPUTATION:
  determines what must be evaluated,
  which dependencies matter,
  and which evaluations may be omitted or reused soundly

OPTIMIZATION:
  selects among already admissible alternatives
  under explicit objectives and constraints

COMPUTATION != OPTIMIZATION
~~~

## 2. Source hierarchy used for recovery

### S1 — Formation Axiom System

Source:

~~~text
DSD_Formation_Axiom_System_EN(5).pdf
~~~

Recovered constraints relevant to Optimization:

~~~text
admission precedes operational-channel composition

undefined assignment
  !=
defined zero

channel absence
  !=
admitted channel with zero contribution

composite-output equality
  !=
source-level identity
~~~

Optimization consequence:

~~~text
an inadmissible or undefined candidate cannot be promoted
to a feasible zero-cost candidate merely for convenience

an absent channel cannot be treated as an available
zero-resource action

candidate identity cannot be collapsed from equal
aggregate outputs unless the declared objective and
constraint interface licenses that equivalence
~~~

Formation stage order may constrain structural admissibility, but it is not automatically an optimization priority or runtime objective.

### S2 — Property Axiom System

Source:

~~~text
DSD_Property_Axiom_System_EN(3).pdf
~~~

Recovered status discipline:

~~~text
UNDECLARED
PROFILE_UNAVAILABLE
INAPPLICABLE
PREREQUISITE_UNSATISFIED
APPLICABLE_BUT_UNDEFINED
DEFINED_ZERO
DEFINED_NONZERO_OR_VALUE
~~~

Optimization consequence:

~~~text
INAPPLICABLE != ZERO_COST
UNDEFINED_OBJECTIVE_VALUE != ZERO_OBJECTIVE_VALUE
UNSATISFIED_PREREQUISITE != FEASIBLE_WITH_PENALTY
~~~

A candidate is not comparable on a declared objective merely because the candidate itself exists.

Prerequisite satisfaction and objective-value definition remain separate questions.

### S3 — Channel-Indexed Static Aggregation

Source:

~~~text
DSD_Channel_Indexed_Static_Aggregation_EN(9).pdf
~~~

Recovered constraints:

~~~text
aggregation requires an explicit admitted support / channel interface

typed property aggregation requires an explicit bridge

aggregate equality
  !=
support equality

aggregate equality
  !=
source decomposition equality

countable extensions require their declared convergence conditions
~~~

Optimization consequence:

~~~text
a scalar aggregate may be used as an objective
only when the objective definition explicitly licenses it

equal aggregate score
  !=
candidate structural equivalence

multi-objective information may not be scalarized silently

lossy compression / aggregation of objective evidence
  requires a target-preservation justification
~~~

### S4 — Structural Reorganization Dynamics

Source:

~~~text
DSD_Structural_Reorganization_Dynamics_EN(20260904-092544).pdf
~~~

Recovered constraints:

~~~text
regular evolution
  !=
status transition
  !=
formation transition

regular-epoch support / interface assumptions
  are frozen only inside that epoch

claim-relevant transitions may invalidate inherited
support / interface / reuse assumptions
~~~

Optimization consequence:

~~~text
OPTIMUM_UNDER_REGIME_A
  !=
OPTIMUM_UNDER_REGIME_B

STATIC_OBJECTIVE_VALUE
  !=
LIFECYCLE_OR_DYNAMIC_COST

one-time selection
  !=
Control policy
  !=
Operation lifecycle management
~~~

A dynamic optimization task requires explicit time/regime semantics; the generic DSD layer does not supply a universal intertemporal objective.

### S5 — Method Family registry and shared interface

Project-internal sources:

~~~text
methods/README.md
methods/METHOD_BOUNDARY_MATRIX.md
methods/fields/07_computation_selection/README.md
methodology/DSD_METHOD_FAMILY_FRAMEWORK.md
methodology/DSD_INTERFACE_PROFILE.md
methodology/SHARED_CORE_EXTRACTION_RULE.md
~~~

Recovered method boundary:

~~~text
Optimization:
  choose among admissible alternatives
  under explicit objectives and constraints

Computation:
  determine required evaluation structure

COMPUTATION != OPTIMIZATION
~~~

Recovered family-wide constraints:

~~~text
preserve claim-relevant typed status distinctions
freeze source / interface / version semantics
make cross-structure mappings explicit
avoid unnecessary optional-interface requirements
respect information-loss limits
separate regular evolution / transition / lineage
preserve failures / NO_GAIN / precommit integrity
separate DSD-internal success from external-domain validation
~~~

Shared-core constraints restrict Optimization construction but do not directly validate Optimization.

### S6 — Computation internal-standard handoff

Project-internal source:

~~~text
methods/12_computation_optimization/computation/
evidence/method_specific/computation/
~~~

Recovered handoff boundary:

~~~text
a sufficient Computation plan
  does not become an optimal plan without
  an explicit objective / constraint selection problem

objective-based choice among sufficient plans
  is handed to Optimization

COMPUTATION_ESTABLISHED
  may coexist with
COMPUTATION_NO_GAIN
~~~

Optimization consequence:

~~~text
FEASIBLE_PLAN != OPTIMAL_PLAN

REQUIRED_EVALUATION_SET
  is an input or constraint sidecar when relevant,
  not an Optimization result by default

Computation evidence is not direct Optimization validation
~~~

### S7 — Audit outcome semantics

Project-internal source:

~~~text
methodology/AUDIT_OUTCOME_SEMANTICS.md
~~~

Recovered result discipline:

~~~text
VALID_IN_DOMAIN
NOT_SUFFICIENT_FOR_EXTENSION
NON_IDENTICAL
RECONSTRUCTION_LOSS
REJECTED
FAIL
NO_GAIN
INDETERMINATE
~~~

Optimization consequence:

~~~text
a valid optimum on one frozen feasible set
  is not automatically valid after scope / regime change

NO_GAIN against a competent optimizer
  does not imply method failure

an unresolved objective or constraint interface
  must remain unresolved rather than being filled post hoc
~~~

## 3. Source-derived Optimization constraints

These are recovered constraints, not new Optimization theorems.

~~~text
OR-01
  every candidate must retain claim-relevant DSD status
  and admissibility distinctions

OR-02
  INAPPLICABLE / UNDEFINED / ABSENT candidates or objective values
  must not be coerced into numerical zero

OR-03
  the feasible / admissible candidate space must be frozen
  or explicitly versioned before objective-based selection

OR-04
  Optimization may only select among candidates whose
  admissibility is established or supplied by an explicit interface

OR-05
  every objective and constraint must have an explicit
  identity, scope, direction, units / ordering semantics when relevant,
  version, and provenance

OR-06
  no universal DSD objective function is available by default

OR-07
  feasibility and optimality are separate:
  FEASIBLE != OPTIMAL

OR-08
  equal aggregate objective values do not establish
  structural identity of candidates

OR-09
  multi-objective values must not be silently scalarized
  when trade-off or preference semantics are absent

OR-10
  dominance, lexicographic priority, weighted sum,
  Pareto retention, or other selection semantics
  must be explicit rather than inferred

OR-11
  objective / constraint values inherited across a
  claim-relevant version or regime transition require revalidation

OR-12
  one-time Optimization selection must not silently become
  a Control policy or Operation lifecycle rule

OR-13
  Computation soundness and Optimization objective quality
  remain separate axes

OR-14
  an objective-based selection request is not answered
  by merely returning any sufficient Computation plan

OR-15
  approximation / aggregation / compression of objective evidence
  requires an explicit error or preservation condition
  sufficient for the declared selection claim

OR-16
  stronger performance, resource, or quality gain relative
  to a baseline requires a fair comparator and equal
  claim-relevant information

OR-17
  NO_GAIN must remain a valid Optimization result

OR-18
  shared-core, Computation, or neighboring-method evidence
  is not direct Optimization validation
~~~

## 4. Working atomic task — not yet frozen

Prospective formulation:

~~~text
Given:
  a declared Optimization task,
  a frozen candidate / feasible-set interface,
  explicit candidate admissibility status,
  one or more explicit objective functions or order relations,
  explicit hard / soft constraints,
  objective / constraint value provenance and uncertainty where relevant,
  declared trade-off / priority / dominance semantics,
  source / model / regime / version locks,
  and any required Computation / Measurement / Aggregation /
  Compression / Dynamics sidecars,

determine:
  which candidates remain feasible,
  which candidate comparisons are evaluable,
  which candidates dominate or are dominated under the
  frozen objective semantics,
  whether a unique optimum, tied optimum set, Pareto set,
  bounded optimum, partial selection, or unresolved result is supported,
  and the maximum selection claim justified by the frozen information.
~~~

This is prospective methodological construction, not a theorem supplied by the predecessor papers.

It remains open to serious pre-protocol boundary attack.

## 5. Candidate information classes for a future Task Interface

Not yet frozen:

~~~text
OPTIMIZATION_TASK_ID
TASK_VERSION

CANDIDATE_SET_ID
CANDIDATE_SET_VERSION
CANDIDATE_REPRESENTATION
CANDIDATE_COMPLETENESS_STATUS

ADMISSIBILITY_INTERFACE_ID
ADMISSIBILITY_STATUS_LEDGER

OBJECTIVE_ID
OBJECTIVE_VERSION
OBJECTIVE_DIRECTION_OR_ORDER
OBJECTIVE_SCOPE
OBJECTIVE_UNITS_OR_SCALE
OBJECTIVE_PROVENANCE

CONSTRAINT_ID
CONSTRAINT_VERSION
CONSTRAINT_TYPE
CONSTRAINT_SCOPE
CONSTRAINT_THRESHOLD_OR_RELATION
CONSTRAINT_PROVENANCE

MULTI_OBJECTIVE_COMBINATION_RULE
PRIORITY_OR_LEXICOGRAPHIC_RULE
PARETO_OR_DOMINANCE_RULE
TIE_RULE

OBJECTIVE_VALUE_LEDGER
CONSTRAINT_VALUE_LEDGER
UNCERTAINTY_OR_ERROR_LEDGER

SOURCE_MODEL_VERSION
REGIME_OR_EPOCH
TRANSITION_INVALIDATION_RULE

FEASIBLE_SET
INFEASIBLE_SET
BLOCKED_SET
CONFLICTING_SET
UNDERDETERMINED_SET
OUT_OF_SCOPE_SET

DOMINANCE_OR_ORDER_LEDGER
SELECTED_OPTIMUM_OR_SET
OPTIMIZATION_METHOD_GAIN_STATUS
COMPARATOR_FAIRNESS_LEDGER
MAXIMUM_SUPPORTED_CLAIM
~~~

These are recovery candidates only and are not yet required task fields.

## 6. Prospective guards to pressure before freezing

~~~text
FEASIBLE != OPTIMAL

UNDEFINED_OBJECTIVE_VALUE != ZERO_OBJECTIVE_VALUE

INAPPLICABLE_CANDIDATE != ZERO_COST_CANDIDATE

ABSENT_ACTION != AVAILABLE_ZERO_ACTION

ONE_BEST_ON_ONE_OBJECTIVE != GLOBAL_BEST

EQUAL_OBJECTIVE_VALUE != STRUCTURAL_EQUIVALENCE

WEIGHTED_SUM != UNIVERSAL_MULTI_OBJECTIVE_ORDER

PARETO_NONDOMINATED != UNIQUE_OPTIMUM

TIED_OPTIMA != UNDERDETERMINED_BY_DEFAULT

MULTIPLE_FEASIBLE != TASK_UNDERDETERMINED

OPTIMUM_UNDER_REGIME_A != OPTIMUM_UNDER_REGIME_B

COMPUTATION_PLAN != OPTIMAL_PLAN

COMPARISON_RESULT != OPTIMIZATION_SELECTION

SIMULATION_TRAJECTORY != OPTIMIZATION_OBJECTIVE

PREDICTION != OPTIMIZATION

CONTROL_POLICY != ONE_TIME_OPTIMIZATION_SELECTION

OPERATION_SCHEDULE != OPTIMIZATION_RESULT_BY_DEFAULT

NO_GAIN != METHOD_FAILURE
~~~

Every guard must be pressure-tested before protocol freeze.

## 7. Initial neighboring-method pressure map

Direct boundary pressure should include at least:

~~~text
Computation:
  sufficient / required evaluation structure
  vs objective-based selection among admissible alternatives

Comparison:
  cross-target difference / similarity report
  vs objective / constraint-based selection

Design:
  construct a target satisfying goals / constraints
  vs select among already declared admissible alternatives

Measurement:
  obtain / discriminate evidence
  vs choose using supplied evidence

Aggregation / Compression:
  form or reduce objective evidence
  vs select candidates

Simulation:
  evolve model-consistent states
  vs choose a candidate

Prediction:
  future claim
  vs selection under frozen objective information

Control:
  choose intervention policy over state evolution
  vs one optimization selection task

Operation:
  manage repeated execution / lifecycle / resources
  vs optimize a frozen selection problem

Audit:
  evaluate compliance / evidence / procedure
  vs perform the selection
~~~

Additional neighbors may be added during boundary attack.

## 8. Current recovery state

~~~text
SOURCE_REGISTRY_RECOVERY:
  complete

TASK_INTERFACE_DRAFT:
  not established

PRE_PROTOCOL_BOUNDARY_ATTACKS:
  0

DEDICATED_OPTIMIZATION_PROTOCOL:
  not established

DIRECT_OPTIMIZATION_PILOTS_ATTEMPTED:
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
  source_and_registry_recovery_complete

PROTOCOL_REVISION_REQUIRED:
  not applicable before protocol

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 9. Next

Establish the Optimization planning/worklog lane and draft Optimization Task Interface v0.1 before serious pre-protocol boundary attack.
