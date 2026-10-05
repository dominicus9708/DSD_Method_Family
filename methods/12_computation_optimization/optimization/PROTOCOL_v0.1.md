# DSD Optimization Protocol v0.1

Status: **EXECUTABLE INTERNAL PROTOCOL — FROZEN FOR DIRECT CHALLENGES**  
Date: **2026-10-05**  
Method: **Optimization / DSD 최적화론**  
Legacy path ID: `12B`  
Higher field: **VII. Computation & Selection / 계산·선택**

Historical basis:

~~~text
SOURCE_REGISTRY_COMMIT:
  f48856ae9df1e189cc08681c1492398e06341def
SOURCE_REGISTRY_BLOB:
  34ff4cd5ad9acb5a8d9c83a87e226c58d6675ef0

TASK_INTERFACE_COMMIT:
  753206b90421bb317462e3cd214a280faf95e317
TASK_INTERFACE_BLOB:
  a3e3490a6a24d0793c608c85e6e0cb6a120f78f6

BOUNDARY_ATTACK_COMMIT:
  108954715c1fb19ad2d12050bccb498d505e33a5
BOUNDARY_ATTACK_BLOB:
  6f1c855c7340d3e4c39d213576e43d7f61a6be40

BOUNDARY_AMENDMENT_001_COMMIT:
  49aa357dae124a2529d7be692d6e63855b95716e
BOUNDARY_AMENDMENT_001_BLOB:
  7ccbe5d6cac6f51ceef57bad6f1d51a9eaba9a2a
~~~

This protocol binds the historical Task Interface v0.1 and Boundary Amendment 001.

The historical Task Interface and boundary-attack record remain immutable development evidence.

## 1. Method task

Given:

~~~text
a frozen Optimization task
a declared candidate / feasible-set interface
candidate admissibility records
one or more explicit objectives or order relations
explicit hard / soft constraints
objective / constraint values and provenance
selection / dominance / tie semantics
uncertainty / approximation semantics when relevant
source / model / version / regime locks
and any explicit neighboring-method handoffs
~~~

determine:

~~~text
which candidates are feasible
which pairwise or set-level comparisons are evaluable
which candidates dominate, tie, or remain incomparable
whether a unique optimum, tied optimum set, Pareto set,
bounded optimum, partial result, or unresolved result is supported
and the maximum Optimization claim justified by the frozen information
~~~

Optimization does not invent missing objectives, constraints, admissibility, scalarization, or external validation criteria.

## 2. Method boundary

~~~text
COMPUTATION:
  determines required evaluation structure

OPTIMIZATION:
  selects among admissible alternatives
  under explicit objective / constraint semantics

COMPARISON:
  describes or judges cross-target difference / similarity

DESIGN:
  constructs a target under goals / constraints

MEASUREMENT:
  acquires or defines discriminating evidence

SIMULATION:
  evolves a model

PREDICTION:
  makes a future-target claim

CONTROL:
  selects state-dependent intervention policies

OPERATION:
  manages repeated lifecycle / execution / monitoring

AUDIT:
  evaluates conformance / evidence / procedure
~~~

Required guards:

~~~text
COMPUTATION_PLAN != OPTIMAL_PLAN
COMPARISON_RESULT != OPTIMIZATION_SELECTION
ONE_TIME_OPTIMUM != CONTROL_POLICY
ONE_TIME_OPTIMUM != OPERATION_PLAN
AUDIT_PASS != OPTIMUM
~~~

## 3. Primary claim levels

Exactly one primary claim level is frozen per task:

~~~text
FEASIBLE_CANDIDATE_SET
DOMINANCE_RELATION_ON_DECLARED_SET
PARETO_SET_ON_DECLARED_OBJECTIVES
OPTIMAL_CANDIDATE_OR_TIED_SET
BOUNDED_OPTIMUM_UNDER_DECLARED_UNCERTAINTY
SELECTION_PLAN_UNDER_DECLARED_PRIORITY_RULE
~~~

No primary claim implies:

~~~text
global completeness of all real alternatives
universal optimality
best result under unregistered objectives
best result under changed constraints
best result across unregistered regimes
universal performance superiority
~~~

## 4. Validity gates G1-G18

### G1 — task / version / primary claim / maximum-claim lock

Freeze:

~~~text
OPTIMIZATION_TASK_ID
TASK_VERSION
PRIMARY_CLAIM_LEVEL
MAXIMUM_SUPPORTED_CLAIM
~~~

Changing a claim-relevant lock after seeing selection outcomes requires a new task version.

### G2 — candidate-set identity / representation / completeness lock

Freeze:

~~~text
CANDIDATE_SET_ID
CANDIDATE_SET_VERSION_OR_DEFINITION
CANDIDATE_REPRESENTATION_MODE
CANDIDATE_COMPLETENESS_STATUS
~~~

Allowed representation modes:

~~~text
EXPLICIT_ENUMERATION
PARAMETRIC_CLASS
PREDICATE_DEFINED_CLASS
RELATION_DEFINED_CLASS
GRAPH_DEFINED_CANDIDATES
EXTERNALLY_SUPPLIED_CANDIDATE_INTERFACE
~~~

Completeness statuses:

~~~text
CANDIDATE_SET_DECLARED_BOUNDED
CANDIDATE_SET_CLAIMED_COMPLETE_WITHIN_SCOPE
CANDIDATE_SET_COMPLETENESS_UNDERDETERMINED
CANDIDATE_SET_COMPLETENESS_NOT_CLAIMED
~~~

Required guards:

~~~text
NON_ENUMERATED != UNDECLARED
DECLARED_SET != COMPLETE_REALITY_SET
UNIQUE_WITHIN_DECLARED_SET != GLOBAL_UNIQUENESS
~~~

### G3 — candidate admissibility / typed-status gate

For each claim-relevant candidate, record admissibility:

~~~text
CANDIDATE_ADMISSIBLE
CANDIDATE_INADMISSIBLE
CANDIDATE_ADMISSIBILITY_BLOCKED
CANDIDATE_ADMISSIBILITY_CONFLICTING
CANDIDATE_ADMISSIBILITY_UNDERDETERMINED
CANDIDATE_ADMISSIBILITY_OUT_OF_SCOPE
~~~

When Formation / Property statuses are claim-relevant, preserve native distinctions.

Required guards:

~~~text
INAPPLICABLE != ADMISSIBLE_ZERO_COST
UNDEFINED != ADMISSIBLE_ZERO_VALUE
CHANNEL_ABSENCE != AVAILABLE_ZERO_ACTION
PREREQUISITE_UNSATISFIED != SOFT_CONSTRAINT_VIOLATION
~~~

### G4 — objective registry lock

Freeze every claim-relevant objective:

~~~text
OBJECTIVE_ID
OBJECTIVE_VERSION_OR_DEFINITION
OBJECTIVE_DIRECTION_OR_ORDER
OBJECTIVE_SCOPE
OBJECTIVE_VALUE_TYPE
OBJECTIVE_UNITS_OR_SCALE_IF_RELEVANT
OBJECTIVE_PROVENANCE
OBJECTIVE_APPLICABILITY_RULE
OBJECTIVE_VALUE_SOURCE
~~~

Objective-value statuses:

~~~text
OBJECTIVE_VALUE_DEFINED
OBJECTIVE_VALUE_UNAVAILABLE
OBJECTIVE_VALUE_INAPPLICABLE
OBJECTIVE_VALUE_UNDEFINED
OBJECTIVE_VALUE_CONFLICTING
OBJECTIVE_VALUE_UNDERDETERMINED
OBJECTIVE_VALUE_OUT_OF_SCOPE
~~~

Required guards:

~~~text
UNDEFINED_OBJECTIVE_VALUE != ZERO_OBJECTIVE_VALUE
UNAVAILABLE_OBJECTIVE_VALUE != WORST_OBJECTIVE_VALUE
INAPPLICABLE_OBJECTIVE != SATISFIED_OBJECTIVE
DSD_STRUCTURE != UNIVERSAL_OBJECTIVE_FUNCTION
~~~

### G5 — constraint registry lock

Freeze every claim-relevant constraint:

~~~text
CONSTRAINT_ID
CONSTRAINT_VERSION_OR_DEFINITION
CONSTRAINT_TYPE
CONSTRAINT_SCOPE
CONSTRAINT_RELATION_OR_THRESHOLD
CONSTRAINT_VALUE_TYPE
CONSTRAINT_PROVENANCE
CONSTRAINT_APPLICABILITY_RULE
~~~

Constraint statuses:

~~~text
CONSTRAINT_SATISFIED
CONSTRAINT_VIOLATED
CONSTRAINT_BLOCKED
CONSTRAINT_CONFLICTING
CONSTRAINT_UNDERDETERMINED
CONSTRAINT_OUT_OF_SCOPE
~~~

Hard and soft constraints remain distinct.

### G6 — constraint-transformation gate

If any hard constraint is transformed into a soft penalty, surrogate, relaxation, or alternate rule, freeze:

~~~text
CONSTRAINT_TRANSFORMATION_ID
CONSTRAINT_TRANSFORMATION_VERSION_OR_DEFINITION
SOURCE_CONSTRAINT_ID
SOURCE_CONSTRAINT_TYPE
TARGET_CONSTRAINT_OR_PENALTY_ID
TRANSFORMATION_SCOPE
TRANSFORMATION_PROVENANCE
TRANSFORMATION_AUTHORIZATION
TASK_VERSION_AFTER_TRANSFORMATION
~~~

Required guards:

~~~text
HARD_CONSTRAINT_VIOLATION != FINITE_PENALTY_BY_DEFAULT
UNREGISTERED_TRANSFORMATION cannot alter feasibility
CLAIM_RELEVANT_TRANSFORMATION requires explicit task/version consequence
~~~

### G7 — objective / constraint component completeness and required-interface gate

For compound objectives or constraints, freeze:

~~~text
OBJECTIVE_COMPONENT_REGISTRY
OBJECTIVE_COMPONENT_REQUIREDNESS
OBJECTIVE_COMPONENT_COMPLETENESS_STATUS

CONSTRAINT_COMPONENT_REGISTRY
CONSTRAINT_COMPONENT_REQUIREDNESS
CONSTRAINT_COMPONENT_COMPLETENESS_STATUS

REQUIRED_OPTIMIZATION_INTERFACE_ID
REQUIRED_OPTIMIZATION_INTERFACE_ROLE
REQUIRED_OPTIMIZATION_INTERFACE_VERSION_OR_DEFINITION
REQUIRED_OPTIMIZATION_INTERFACE_STATUS
REQUIRED_OPTIMIZATION_INTERFACE_PROVENANCE
~~~

Required-interface statuses:

~~~text
REQUIRED_OPTIMIZATION_INTERFACE_AVAILABLE
REQUIRED_OPTIMIZATION_INTERFACE_UNAVAILABLE
REQUIRED_OPTIMIZATION_INTERFACE_CONFLICTING
REQUIRED_OPTIMIZATION_INTERFACE_UNDERDETERMINED
REQUIRED_OPTIMIZATION_INTERFACE_OUT_OF_SCOPE
~~~

Binding consequences:

~~~text
UNAVAILABLE -> BLOCKED
CONFLICTING -> CONFLICTING
UNDERDETERMINED -> UNDERDETERMINED
  when admissible alternatives alter the requested selection
OUT_OF_SCOPE -> OUT_OF_SCOPE
~~~

Required guards:

~~~text
MISSING_REQUIRED_COMPONENT != IRRELEVANT_COMPONENT
MISSING_REQUIRED_INTERFACE != NEGATIVE_EVIDENCE
BLOCKED != INFEASIBLE
~~~

### G8 — selection / multi-objective semantics lock

Freeze one explicit selection semantics family:

~~~text
SINGLE_OBJECTIVE_ORDER
LEXICOGRAPHIC_PRIORITY
EXPLICIT_WEIGHTED_SCALARIZATION
PARETO_DOMINANCE
EXPLICIT_PARTIAL_ORDER
MINIMAX_OR_MAXIMIN_IF_DECLARED
CONSTRAINT_FIRST_THEN_OBJECTIVE
EXTERNALLY_SUPPLIED_SELECTION_RULE
~~~

Also freeze, as applicable:

~~~text
SELECTION_RULE_ID
SELECTION_RULE_VERSION
MULTI_OBJECTIVE_COMBINATION_RULE
PRIORITY_OR_LEXICOGRAPHIC_RULE
PARETO_OR_DOMINANCE_RULE
TIE_RULE
~~~

Required guards:

~~~text
MULTIPLE_OBJECTIVES != WEIGHTED_SUM
WEIGHTED_SUM != UNIVERSAL_MULTI_OBJECTIVE_ORDER
PARETO_NONDOMINATED != UNIQUE_OPTIMUM
PARTIAL_ORDER != TOTAL_ORDER
~~~

### G9 — pair-order / incomparability / uncertainty gate

When pairwise comparison is claim-relevant, assign one relation/status:

~~~text
PAIR_STRICTLY_PREFERS_LEFT
PAIR_STRICTLY_PREFERS_RIGHT
PAIR_TIED_UNDER_DECLARED_RULE
PAIR_INCOMPARABLE_UNDER_DECLARED_PARTIAL_ORDER
PAIR_ORDER_BLOCKED
PAIR_ORDER_CONFLICTING
PAIR_ORDER_UNDERDETERMINED
PAIR_ORDER_OUT_OF_SCOPE
~~~

When uncertainty is claim-relevant, freeze:

~~~text
PAIR_UNCERTAINTY_INTERFACE_ID
PAIR_UNCERTAINTY_RULE
PAIR_ORDER_ROBUSTNESS_STATUS
PAIR_ORDER_PROVENANCE
~~~

Required guards:

~~~text
INCOMPARABLE_BY_DECLARED_PARTIAL_ORDER != UNDERDETERMINED_SELECTION_SEMANTICS
OVERLAPPING_INTERVALS != STRICT_ORDER_BY_DEFAULT
NO_STRICT_ORDER != TIE_BY_DEFAULT
~~~

### G10 — uncertainty / approximation / error gate

Freeze, when used:

~~~text
UNCERTAINTY_INTERFACE_ID
ERROR_OR_INTERVAL_SEMANTICS
ERROR_BOUND
ERROR_COMPOSITION_RULE
ORDER_ROBUSTNESS_RULE
TIE_TOLERANCE_IF_ANY
~~~

Required guards:

~~~text
POINT_ESTIMATE_ORDER != ROBUST_ORDER_UNDER_ERROR
OVERLAPPING_INTERVALS != STRICT_DOMINANCE
SMALL_LOCAL_ERROR != GLOBAL_SELECTION_PRESERVATION
~~~

### G11 — reduction / aggregation / compression selection-preservation gate

If a reduced representation is used in a selection claim, freeze:

~~~text
SELECTION_REDUCTION_ID
SELECTION_REDUCTION_VERSION
SOURCE_CANDIDATE_SCOPE
REDUCED_REPRESENTATION_SCOPE
DECLARED_SELECTION_RELATION
SELECTION_RELATION_PRESERVATION_RULE
SELECTION_PRESERVATION_STATUS
COLLISION_STATUS
ERROR_OR_SIDECAR_REQUIREMENTS
~~~

Statuses:

~~~text
SELECTION_RELATION_PRESERVED_ON_DECLARED_SCOPE
SELECTION_RELATION_NOT_PRESERVED
SELECTION_PRESERVATION_BLOCKED
SELECTION_PRESERVATION_CONFLICTING
SELECTION_PRESERVATION_UNDERDETERMINED
SELECTION_PRESERVATION_OUT_OF_SCOPE
~~~

Required guards:

~~~text
EQUAL_REDUCED_SCORE != STRUCTURAL_EQUIVALENCE
GENERIC_LOW_ERROR != SELECTION_ORDER_PRESERVATION
REDUCTION_SAFE_FOR_ONE_OBJECTIVE != SAFE_FOR_ALL_OBJECTIVES
SELECTION_RELATION_PRESERVED_ON_SCOPE != GLOBAL_INJECTIVITY
~~~

### G12 — regime / transition / value-invalidation gate

When time or regime matters, freeze:

~~~text
TEMPORAL_SCOPE
REGIME_ID
REGIME_VERSION
TRANSITION_INTERFACE
VALUE_INVALIDATION_RULE
FEASIBILITY_INVALIDATION_RULE
OBJECTIVE_INVALIDATION_RULE
~~~

Required guards:

~~~text
OPTIMUM_UNDER_REGIME_A != OPTIMUM_UNDER_REGIME_B
STATIC_OPTIMUM != LIFECYCLE_OPTIMUM
ONE_TIME_SELECTION != CONTROL_POLICY
ONE_TIME_SELECTION != OPERATION_PLAN
~~~

### G13 — neighboring-method handoff / non-substitution gate

Optimization may consume explicit handoffs from:

~~~text
Computation
Measurement
Aggregation
Compression
Dynamics
Tracking
Lineage
Comparison
Design
Simulation
Prediction
Control
Operation
Audit
~~~

But:

~~~text
COMPUTATION_PLAN != OPTIMAL_PLAN
COMPARISON_RESULT != OPTIMIZATION_SELECTION
DESIGN_OUTPUT != OPTIMIZATION_SELECTION
MEASUREMENT_RESULT != OPTIMUM
SIMULATION_TRAJECTORY != OPTIMUM
PREDICTION_RESULT != OPTIMUM
CONTROL_POLICY != ONE_TIME_OPTIMUM
OPERATION_SCHEDULE != OPTIMIZATION_RESULT_BY_DEFAULT
AUDIT_PASS != OPTIMUM
~~~

### G14 — feasible / infeasible / unresolved-set construction gate

Construct and preserve, as applicable:

~~~text
FEASIBLE_SET
INFEASIBLE_SET
BLOCKED_SET
CONFLICTING_SET
UNDERDETERMINED_SET
OUT_OF_SCOPE_SET
~~~

Required guards:

~~~text
FEASIBLE != OPTIMAL
INFEASIBLE != OBJECTIVE_WORST
BLOCKED != INFEASIBLE
UNDERDETERMINED != TIED_OPTIMUM
~~~

### G15 — dominance / tie / Pareto / optimum gate

Allowed selection-set outcomes:

~~~text
UNIQUE_OPTIMUM_ESTABLISHED
TIED_OPTIMUM_SET_ESTABLISHED
PARETO_SET_ESTABLISHED
BOUNDED_OPTIMUM_SET_ESTABLISHED
OPTIMUM_NOT_ESTABLISHED
OPTIMUM_BLOCKED
OPTIMUM_CONFLICTING
OPTIMUM_UNDERDETERMINED
OPTIMUM_OUT_OF_SCOPE
~~~

Required guards:

~~~text
TIED_OPTIMA != UNDERDETERMINED_BY_DEFAULT
MULTIPLE_FEASIBLE != TASK_UNDERDETERMINED
MULTIPLE_NONDOMINATED != OPTIMIZATION_FAILURE
UNIQUE_WITHIN_DECLARED_SET != GLOBAL_UNIQUENESS
~~~

### G16 — method-gain / comparator-fairness gate

Optimization validity and method gain are independent axes.

Method-gain status family:

~~~text
OPTIMIZATION_GAIN_ESTABLISHED
OPTIMIZATION_NO_GAIN
OPTIMIZATION_GAIN_NOT_TESTED
OPTIMIZATION_GAIN_BLOCKED
OPTIMIZATION_GAIN_CONFLICTING
OPTIMIZATION_GAIN_UNDERDETERMINED
OPTIMIZATION_GAIN_OUT_OF_SCOPE
~~~

When gain is tested, freeze:

~~~text
GAIN_METRIC_ID
GAIN_SCOPE
GAIN_BASELINE_ID

COMPARATOR_ID
COMPARATOR_VERSION
COMPARATOR_TASK_EQUIVALENCE
COMPARATOR_CANDIDATE_SET_EQUIVALENCE
COMPARATOR_ADMISSIBILITY_EQUIVALENCE
COMPARATOR_OBJECTIVE_EQUIVALENCE
COMPARATOR_CONSTRAINT_EQUIVALENCE
COMPARATOR_SELECTION_RULE_EQUIVALENCE
COMPARATOR_UNCERTAINTY_EQUIVALENCE
COMPARATOR_INFORMATION_ACCESS
COMPARATOR_REGIME_OR_ENVIRONMENT
COMPARATOR_IMPLEMENTATION_SCOPE
COMPARATOR_FAIRNESS_STATUS
COMPARATOR_FAIRNESS_PROVENANCE
~~~

Comparator-fairness statuses:

~~~text
COMPARATOR_FAIR
COMPARATOR_NOT_FAIR
COMPARATOR_BLOCKED
COMPARATOR_CONFLICTING
COMPARATOR_UNDERDETERMINED
COMPARATOR_OUT_OF_SCOPE
~~~

Required guards:

~~~text
OPTIMIZATION_ESTABLISHED may coexist with OPTIMIZATION_NO_GAIN
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
DIFFERENT_CANDIDATE_SET != FAIR_GAIN_COMPARISON
DIFFERENT_OBJECTIVE_OR_CONSTRAINT != FAIR_GAIN_COMPARISON
HIDDEN_INFORMATION_ADVANTAGE != METHOD_GAIN
COMPARATOR_NOT_FAIR != OPTIMIZATION_METHOD_FAILURE
~~~

### G17 — primary Optimization status gate

Assign one primary status:

~~~text
OPTIMIZATION_ESTABLISHED
OPTIMIZATION_NOT_ESTABLISHED
OPTIMIZATION_BLOCKED
OPTIMIZATION_CONFLICTING
OPTIMIZATION_OUT_OF_SCOPE
OPTIMIZATION_UNDERDETERMINED
~~~

Interpretation:

~~~text
ESTABLISHED:
  requested Optimization claim supported
  on frozen candidate / objective / constraint scope

NOT_ESTABLISHED:
  all required claim interfaces evaluable
  but requested claim does not hold

BLOCKED:
  one or more required in-scope candidate / objective /
  constraint / comparison interfaces unavailable

CONFLICTING:
  mutually incompatible applicable claim-relevant
  records remain unresolved

OUT_OF_SCOPE:
  requested operation lies outside Optimization

UNDERDETERMINED:
  multiple admissible claim-relevant semantics remain
  and produce different selections
~~~

### G18 — task terminal / conformance / maximum-claim gate

Assign exactly one task terminal:

~~~text
OPTIMIZATION_TASK_ESTABLISHED
OPTIMIZATION_TASK_PARTIAL
OPTIMIZATION_TASK_NOT_ESTABLISHED
OPTIMIZATION_TASK_BLOCKED
OPTIMIZATION_TASK_CONFLICTING
OPTIMIZATION_TASK_OUT_OF_SCOPE
OPTIMIZATION_TASK_UNDERDETERMINED
~~~

Frozen precedence:

~~~text
OPTIMIZATION_TASK_OUT_OF_SCOPE
>
OPTIMIZATION_TASK_CONFLICTING
>
OPTIMIZATION_TASK_UNDERDETERMINED
>
OPTIMIZATION_TASK_BLOCKED
>
OPTIMIZATION_TASK_ESTABLISHED /
OPTIMIZATION_TASK_PARTIAL /
OPTIMIZATION_TASK_NOT_ESTABLISHED
~~~

PARTIAL is permitted only when:

~~~text
1. multiple independently required in-scope optimization obligations exist
2. at least one required obligation is ESTABLISHED
3. at least one other required obligation is evaluably NOT_ESTABLISHED
4. no required obligation is BLOCKED
5. no higher-priority OUT_OF_SCOPE / CONFLICTING /
   UNDERDETERMINED condition applies
~~~

Required guards:

~~~text
PARTIAL != BLOCKED_WITH_SOME_SUCCESS
PARTIAL != ATOMIC_FAILURE_RELABELED
TIED_OPTIMUM_SET != PARTIAL
PARETO_SET != PARTIAL
OPTIMIZATION_NO_GAIN != OPTIMIZATION_TASK_PARTIAL_BY_DEFAULT
~~~

Then emit protocol conformance, method-gain status, and maximum-supported claim.

## 5. Binding operation O1-O18

### O1 — freeze task / primary claim / maximum claim

Instantiate G1.

### O2 — freeze candidate set / representation / completeness

Instantiate G2.

### O3 — evaluate candidate admissibility and typed statuses

Instantiate G3.

### O4 — freeze objective registry

Instantiate G4.

### O5 — freeze constraint registry

Instantiate G5.

### O6 — bind any explicit constraint transformations

Instantiate G6.

### O7 — evaluate objective / constraint component completeness and required interfaces

Instantiate G7.

### O8 — freeze selection / multi-objective semantics

Instantiate G8.

### O9 — evaluate pair-order / incomparability / uncertainty relations

Instantiate G9.

### O10 — evaluate uncertainty / approximation / error

Instantiate G10.

### O11 — evaluate selection preservation under any reduction / aggregation / compression

Instantiate G11.

### O12 — evaluate regime / transition invalidation

Instantiate G12.

### O13 — apply neighboring-method handoffs and non-substitution

Instantiate G13.

### O14 — construct feasible / infeasible / unresolved sets

Instantiate G14.

### O15 — construct dominance / tie / Pareto / optimum result

Instantiate G15.

### O16 — evaluate method gain / comparator fairness if requested

Instantiate G16.

If gain is not requested:

~~~text
OPTIMIZATION_GAIN_NOT_TESTED
~~~

is allowed.

### O17 — assign primary Optimization status

Instantiate G17.

### O18 — assign task terminal / conformance / maximum claim

Instantiate G18.

Preserve all subordinate statuses beneath the task terminal.

## 6. Protocol conformance

~~~text
OPTIMIZATION_PROTOCOL_CONFORMANT
OPTIMIZATION_PROTOCOL_NONCONFORMANT
OPTIMIZATION_PROTOCOL_INDETERMINATE
~~~

A negative, blocked, conflicting, underdetermined, tied, Pareto, partial, or out-of-scope result may still be protocol-conformant.

Protocol conformance concerns whether the frozen protocol was followed, not whether a unique optimum was found.

## 7. Required output schema

Every executable record must emit, as applicable:

~~~text
TASK_LOCK
CANDIDATE_SET_LOCK
ADMISSIBILITY_LEDGER

OBJECTIVE_REGISTRY
OBJECTIVE_VALUE_LEDGER
OBJECTIVE_COMPONENT_COMPLETENESS_LEDGER

CONSTRAINT_REGISTRY
CONSTRAINT_VALUE_LEDGER
CONSTRAINT_COMPONENT_COMPLETENESS_LEDGER
CONSTRAINT_TRANSFORMATION_LEDGER

REQUIRED_OPTIMIZATION_INTERFACE_LEDGER

SELECTION_RULE_LOCK
PAIR_ORDER_LEDGER
PAIR_UNCERTAINTY_LEDGER

UNCERTAINTY_OR_ERROR_LEDGER
SELECTION_REDUCTION_PRESERVATION_LEDGER

REGIME_OR_TRANSITION_LEDGER
NEIGHBORING_METHOD_HANDOFF_LEDGER

FEASIBLE_SET
INFEASIBLE_SET
BLOCKED_SET
CONFLICTING_SET
UNDERDETERMINED_SET
OUT_OF_SCOPE_SET

DOMINANCE_OR_ORDER_LEDGER
TIE_OR_MULTIPLICITY_LEDGER
SELECTED_OPTIMUM_OR_SET

COMPARATOR_EQUIVALENCE_AND_FAIRNESS_LEDGER_IF_GAIN_TESTED
OPTIMIZATION_METHOD_GAIN_STATUS

OPTIMIZATION_PRIMARY_STATUS
OPTIMIZATION_TASK_TERMINAL
OPTIMIZATION_PROTOCOL_CONFORMANCE

MAXIMUM_SUPPORTED_CLAIM
~~~

Every claim-relevant optional ledger must be explicitly:

~~~text
populated
NOT_APPLICABLE
NOT_REQUESTED
BLOCKED
~~~

rather than silently omitted.

## 8. Five-interface identity

~~~text
INPUTS:
  frozen candidate / admissibility interface
  explicit objective registry
  explicit constraint registry
  selection / dominance / tie semantics
  objective / constraint value evidence
  optional uncertainty / reduction / transition / neighboring-method handoffs

OPERATION:
  preserve candidate admissibility
  evaluate objective / constraint applicability and completeness
  bind explicit transformations
  construct feasible and unresolved sets
  apply declared ordering / dominance / priority semantics
  preserve ties / Pareto multiplicity / incomparability
  validate uncertainty and reduction effects
  select only to the maximum scope justified

OUTPUTS:
  feasible / infeasible / unresolved sets
  objective / constraint ledgers
  pair-order / dominance ledger
  selected optimum / tied set / Pareto set / bounded set
  primary status / task terminal / conformance
  separate method-gain status
  maximum-supported claim

FAILURE_OR_NO_GAIN:
  invented objective / scalarization
  inadmissible candidate selected
  hidden hard-to-soft conversion
  missing required objective / constraint component
  unsupported ordering under uncertainty
  reduction that does not preserve declared selection relation
  stale regime data
  neighboring-method substitution
  fair-baseline NO_GAIN

VALIDATION_STANDARD:
  every selection follows from frozen candidate,
  admissibility, objective, constraint, transformation,
  ordering, uncertainty, reduction, version / regime,
  and handoff semantics;
  ties / Pareto multiplicity / incomparability remain explicit;
  information-loss limits are preserved;
  method gain remains separate from Optimization validity;
  no universal objective, global optimum, or external validity is inferred
~~~

## 9. Core semantic guards

~~~text
FEASIBLE != OPTIMAL

INAPPLICABLE_CANDIDATE != ZERO_COST_CANDIDATE

UNDEFINED_OBJECTIVE_VALUE != ZERO_OBJECTIVE_VALUE

HARD_CONSTRAINT_VIOLATION != FINITE_PENALTY_BY_DEFAULT

MULTIPLE_OBJECTIVES != WEIGHTED_SUM

PARETO_NONDOMINATED != UNIQUE_OPTIMUM

TIED_OPTIMA != UNDERDETERMINED_BY_DEFAULT

INCOMPARABLE != UNDERDETERMINED

EQUAL_OBJECTIVE_VALUE != STRUCTURAL_EQUIVALENCE

OVERLAPPING_INTERVALS != STRICT_ORDER_BY_DEFAULT

MISSING_REQUIRED_COMPONENT != IRRELEVANT_COMPONENT

EQUAL_REDUCED_SCORE != SELECTION_RELATION_PRESERVATION

OPTIMUM_UNDER_REGIME_A != OPTIMUM_UNDER_REGIME_B

COMPUTATION_PLAN != OPTIMAL_PLAN

ONE_TIME_SELECTION != CONTROL_POLICY

ONE_TIME_SELECTION != OPERATION_PLAN

OPTIMIZATION_ESTABLISHED may coexist with OPTIMIZATION_NO_GAIN
~~~

## 10. Current protocol state

~~~text
DEDICATED_OPTIMIZATION_PROTOCOL:
  established v0.1

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  O1-O18

PRE_PROTOCOL_BOUNDARY_ATTACKS:
  18

BOUNDARY_AMENDMENT_001:
  established

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
  protocol_frozen

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 11. Next

Prospectively precommit and execute **OPT-CH-001**, the positive constructed Optimization challenge.

The first challenge should directly exercise at least:

~~~text
unique optimum
tied optimum set
Pareto set
explicit hard constraint
declared multi-objective semantics
incomparability distinct from underdetermination
reduction / uncertainty sidecar
Computation handoff without substitution
method gain not tested
bounded maximum-supported claim
~~~
