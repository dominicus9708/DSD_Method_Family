# DSD Optimization — Task Interface v0.1 Draft

Status: **PRE-PROTOCOL HISTORICAL DRAFT — NOT AN EXECUTABLE STANDARD**  
Date: **2026-10-05**  
Method: **Optimization / DSD 최적화론**  
Legacy path ID: `12B`  
Higher field: **VII. Computation & Selection / 계산·선택**

Source basis:

~~~text
SOURCE_REGISTRY_v0.1.md
commit:
  f48856ae9df1e189cc08681c1492398e06341def
blob:
  34ff4cd5ad9acb5a8d9c83a87e226c58d6675ef0
~~~

This draft is prospective method construction from recovered source constraints.

It is not a theorem of the predecessor papers.

Once serious direct boundary attack begins, this file becomes immutable historical development evidence. Any refinement after that point must be recorded in a separate amendment rather than by rewriting this draft.

## 1. Atomic task

Working atomic Optimization task:

~~~text
Given:
  a declared selection task,
  a frozen candidate / feasible-set interface,
  explicit candidate admissibility records,
  one or more explicit objectives or order relations,
  explicit hard / soft constraints,
  objective / constraint values and provenance,
  declared multi-objective / priority / dominance / tie semantics,
  source / model / regime / version locks,
  declared uncertainty / approximation semantics where relevant,
  and any required Computation / Measurement / Aggregation /
  Compression / Dynamics handoffs,

determine:
  which candidates are feasible,
  which objective / constraint comparisons are evaluable,
  which candidates dominate or tie under the frozen rules,
  whether a unique optimum, tied optimum set, Pareto set,
  bounded optimum, partial result, or unresolved result is supported,
  and the maximum optimization claim justified by the frozen information,

without:
  inventing an objective,
  coercing undefined / inapplicable / absent states to zero,
  treating feasibility as optimality,
  silently scalarizing incompatible objectives,
  treating equal objective values as candidate identity,
  importing a Computation, Control, Operation, Simulation,
  Prediction, Measurement, or Audit result as Optimization itself,
  or converting a bounded optimum into a universal optimum.
~~~

## 2. Method boundary

Optimization asks:

~~~text
Among the explicitly admissible alternatives,
which alternative or set is selected under
the explicitly declared objective and constraint semantics?
~~~

It does not by itself answer:

~~~text
What must be evaluated for the target?
What evidence should be measured?
What aggregate should be constructed?
What representation should be compressed?
What dynamic trajectory should be simulated?
What future state will occur?
What intervention policy should be executed over time?
How should an operation be managed repeatedly?
Does an audit standard pass?
~~~

Working distinction:

~~~text
COMPUTATION:
  determine required evaluation / sound omission / scoped reuse

OPTIMIZATION:
  choose among admissible alternatives under
  explicit objectives and constraints

COMPARISON:
  identify cross-target similarities / differences

DESIGN:
  construct a target satisfying goals / constraints

CONTROL:
  select interventions as a state-dependent policy

OPERATION:
  manage lifecycle / execution / monitoring / handoff
~~~

## 3. Primary claim levels

A task freezes one primary claim level:

~~~text
FEASIBLE_CANDIDATE_SET

DOMINANCE_RELATION_ON_DECLARED_SET

PARETO_SET_ON_DECLARED_OBJECTIVES

OPTIMAL_CANDIDATE_OR_TIED_SET

BOUNDED_OPTIMUM_UNDER_DECLARED_UNCERTAINTY

SELECTION_PLAN_UNDER_DECLARED_PRIORITY_RULE
~~~

No claim level implies universal optimality, global completeness of all real alternatives, or superiority under unregistered objectives.

## 4. Required task lock

Every future executable Optimization task should freeze at least:

~~~text
OPTIMIZATION_TASK_ID
TASK_VERSION

PRIMARY_CLAIM_LEVEL

CANDIDATE_SET_ID
CANDIDATE_SET_VERSION_OR_DEFINITION
CANDIDATE_REPRESENTATION_MODE
CANDIDATE_COMPLETENESS_STATUS

ADMISSIBILITY_INTERFACE_ID
ADMISSIBILITY_INTERFACE_VERSION
ADMISSIBILITY_SEMANTICS

OBJECTIVE_REGISTRY_ID
OBJECTIVE_REGISTRY_VERSION

CONSTRAINT_REGISTRY_ID
CONSTRAINT_REGISTRY_VERSION

SELECTION_RULE_ID
SELECTION_RULE_VERSION

MAXIMUM_SUPPORTED_CLAIM

SOURCE_MODEL_ID
SOURCE_MODEL_VERSION
ACTIVE_DSD_LAYERS
~~~

Conditionally required when claim-relevant:

~~~text
COMPUTATION_HANDOFF
MEASUREMENT_HANDOFF
AGGREGATION_HANDOFF
COMPRESSION_HANDOFF
DYNAMICS_HANDOFF

UNCERTAINTY_OR_ERROR_INTERFACE
TRANSITION_OR_REGIME_INTERFACE
LINEAGE_HANDOFF

COMPARATOR_ID
COMPARATOR_VERSION
COMPARATOR_INFORMATION_ACCESS
COMPARATOR_FAIRNESS_STATUS
~~~

Changing a claim-relevant lock after seeing selection outcomes opens a new task version.

## 5. Candidate-set representation and completeness

Working representation modes:

~~~text
EXPLICIT_ENUMERATION
PARAMETRIC_CLASS
PREDICATE_DEFINED_CLASS
RELATION_DEFINED_CLASS
GRAPH_DEFINED_CANDIDATES
EXTERNALLY_SUPPLIED_CANDIDATE_INTERFACE
~~~

Working completeness statuses:

~~~text
CANDIDATE_SET_DECLARED_BOUNDED
CANDIDATE_SET_CLAIMED_COMPLETE_WITHIN_SCOPE
CANDIDATE_SET_COMPLETENESS_UNDERDETERMINED
CANDIDATE_SET_COMPLETENESS_NOT_CLAIMED
~~~

Draft guards:

~~~text
NON_ENUMERATED != UNDECLARED
DECLARED_CANDIDATE_SET != COMPLETE_REALITY_SET
ONE_SELECTED_CANDIDATE != GLOBALLY_BEST_REAL_CANDIDATE
~~~

## 6. Candidate admissibility

Every candidate relevant to the task receives an admissibility status:

~~~text
CANDIDATE_ADMISSIBLE
CANDIDATE_INADMISSIBLE
CANDIDATE_ADMISSIBILITY_BLOCKED
CANDIDATE_ADMISSIBILITY_CONFLICTING
CANDIDATE_ADMISSIBILITY_UNDERDETERMINED
CANDIDATE_ADMISSIBILITY_OUT_OF_SCOPE
~~~

Inherited Formation / Property distinctions remain visible when relevant.

Draft guards:

~~~text
INAPPLICABLE != ADMISSIBLE_ZERO_COST
UNDEFINED != ADMISSIBLE_ZERO_VALUE
CHANNEL_ABSENCE != AVAILABLE_ZERO_ACTION
PREREQUISITE_UNSATISFIED != SOFT_CONSTRAINT_VIOLATION_BY_DEFAULT
~~~

Optimization cannot repair an inadmissible candidate merely by assigning a favorable score.

## 7. Objective registry

Every objective must record:

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

Draft guards:

~~~text
UNDEFINED_OBJECTIVE_VALUE != ZERO_OBJECTIVE_VALUE
UNAVAILABLE_OBJECTIVE_VALUE != WORST_OBJECTIVE_VALUE
INAPPLICABLE_OBJECTIVE != SATISFIED_OBJECTIVE
DSD_STRUCTURE != UNIVERSAL_OBJECTIVE_FUNCTION
~~~

## 8. Constraint registry

Every hard or soft constraint must record:

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

Working constraint statuses:

~~~text
CONSTRAINT_SATISFIED
CONSTRAINT_VIOLATED
CONSTRAINT_BLOCKED
CONSTRAINT_CONFLICTING
CONSTRAINT_UNDERDETERMINED
CONSTRAINT_OUT_OF_SCOPE
~~~

Hard and soft constraints remain distinct unless an explicit penalty transformation is supplied.

~~~text
HARD_CONSTRAINT_VIOLATION
  !=
FINITE_PENALTY_BY_DEFAULT
~~~

## 9. Selection semantics

The task must freeze exactly how objective information becomes a selection relation.

Allowed working families include:

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

Draft guards:

~~~text
MULTIPLE_OBJECTIVES != WEIGHTED_SUM
WEIGHTED_SUM != UNIVERSAL_MULTI_OBJECTIVE_ORDER
PARETO_NONDOMINATED != UNIQUE_OPTIMUM
ONE_BEST_ON_ONE_OBJECTIVE != GLOBAL_BEST
PARTIAL_ORDER != TOTAL_ORDER
~~~

If no selection semantics resolves the supplied objective family, the result remains underdetermined rather than silently choosing a scalarization.

## 10. Tie and multiplicity semantics

Working selection-set statuses:

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

Draft guards:

~~~text
TIED_OPTIMA != UNDERDETERMINED_BY_DEFAULT
MULTIPLE_FEASIBLE != TASK_UNDERDETERMINED
MULTIPLE_NONDOMINATED != OPTIMIZATION_FAILURE
UNIQUE_WITHIN_DECLARED_SET != GLOBAL_UNIQUENESS
~~~

A tied optimum set is a positive result when the frozen rule genuinely leaves multiple equal optima.

## 11. Uncertainty / approximation / information loss

If objective or constraint values are approximate, aggregated, compressed, sampled, or interval-valued, freeze:

~~~text
UNCERTAINTY_INTERFACE_ID
ERROR_OR_INTERVAL_SEMANTICS
ERROR_BOUND
ERROR_COMPOSITION_RULE
ORDER_ROBUSTNESS_RULE
TIE_TOLERANCE_IF_ANY
COLLISION_OR_INJECTIVITY_HANDOFF
REQUIRED_SIDECARS
~~~

Draft guards:

~~~text
POINT_ESTIMATE_ORDER != ROBUST_ORDER_UNDER_ERROR
OVERLAPPING_INTERVALS != STRICT_DOMINANCE
EQUAL_AGGREGATE_SCORE != STRUCTURAL_EQUIVALENCE
LOSSY_OBJECTIVE_READOUT != LOSSLESS_CANDIDATE_IDENTITY
~~~

A reduced readout may support a selection claim only to the extent justified by its frozen error / preservation interface.

## 12. Dynamic / regime discipline

When values, constraints, or feasibility depend on time or regime, freeze:

~~~text
TEMPORAL_SCOPE
REGIME_ID
REGIME_VERSION
TRANSITION_INTERFACE
VALUE_INVALIDATION_RULE
FEASIBILITY_INVALIDATION_RULE
OBJECTIVE_INVALIDATION_RULE
~~~

Draft guards:

~~~text
OPTIMUM_UNDER_REGIME_A != OPTIMUM_UNDER_REGIME_B
STATIC_OPTIMUM != LIFECYCLE_OPTIMUM
ONE_TIME_SELECTION != CONTROL_POLICY
ONE_TIME_SELECTION != OPERATION_PLAN
~~~

A transition may invalidate prior objective values, constraints, or candidate admissibility.

## 13. Computation handoff

Optimization may consume a valid Computation handoff, including:

~~~text
sufficient computation plans
required evaluation sets
sound omission sets
reuse-validity records
cost / complexity evidence
resolution / error ledgers
~~~

But:

~~~text
COMPUTATION_PLAN != OPTIMAL_PLAN
COMPUTATION_ESTABLISHED != OPTIMIZATION_ESTABLISHED
COMPUTATION_NO_GAIN != OPTIMIZATION_NO_GAIN
~~~

Optimization must not silently alter the Computation target, tolerance, or candidate information in order to manufacture gain.

## 14. Neighboring-method non-substitution

Draft guards:

~~~text
COMPARISON_RESULT != OPTIMIZATION_SELECTION
DESIGN_OUTPUT != OPTIMIZATION_SELECTION
MEASUREMENT_RESULT != OPTIMUM
AGGREGATION_RESULT != OPTIMUM
COMPRESSION_RESULT != OPTIMUM
SIMULATION_TRAJECTORY != OPTIMUM
PREDICTION_RESULT != OPTIMUM
CONTROL_POLICY != ONE_TIME_OPTIMUM
OPERATION_SCHEDULE != OPTIMIZATION_RESULT_BY_DEFAULT
AUDIT_PASS != OPTIMUM
~~~

Neighboring methods may provide inputs or validate specific interfaces but do not become Optimization by handoff.

## 15. Optimization gain and comparator fairness

Optimization validity and method gain are separate.

Working method-gain statuses:

~~~text
OPTIMIZATION_GAIN_ESTABLISHED
OPTIMIZATION_NO_GAIN
OPTIMIZATION_GAIN_NOT_TESTED
OPTIMIZATION_GAIN_BLOCKED
OPTIMIZATION_GAIN_CONFLICTING
OPTIMIZATION_GAIN_UNDERDETERMINED
OPTIMIZATION_GAIN_OUT_OF_SCOPE
~~~

If a gain claim is tested, freeze:

~~~text
GAIN_METRIC_ID
GAIN_SCOPE
GAIN_BASELINE_ID
COMPARATOR_ID
COMPARATOR_VERSION
COMPARATOR_INFORMATION_ACCESS
COMPARATOR_CANDIDATE_SET
COMPARATOR_OBJECTIVES
COMPARATOR_CONSTRAINTS
COMPARATOR_UNCERTAINTY_SEMANTICS
COMPARATOR_ENVIRONMENT_IF_EMPIRICAL
COMPARATOR_FAIRNESS_STATUS
~~~

Draft guards:

~~~text
OPTIMIZATION_ESTABLISHED may coexist with OPTIMIZATION_NO_GAIN
NO_GAIN != METHOD_FAILURE
DIFFERENT_CANDIDATE_SET != FAIR_GAIN_COMPARISON
DIFFERENT_OBJECTIVE != FAIR_GAIN_COMPARISON
HIDDEN_INFORMATION_ADVANTAGE != METHOD_GAIN
~~~

## 16. Working primary statuses

Exactly one primary Optimization status:

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
  the requested optimization claim is supported
  on the frozen candidate / objective / constraint scope

NOT_ESTABLISHED:
  the required interfaces are evaluable,
  but the requested claim does not hold

BLOCKED:
  required in-scope candidate / objective / constraint /
  comparison information is unavailable

CONFLICTING:
  mutually incompatible applicable claim-relevant
  records remain unresolved

OUT_OF_SCOPE:
  the requested operation lies outside Optimization

UNDERDETERMINED:
  multiple admissible claim-relevant semantics remain
  and yield different selections
~~~

## 17. Working task terminals

Exactly one task terminal:

~~~text
OPTIMIZATION_TASK_ESTABLISHED
OPTIMIZATION_TASK_PARTIAL
OPTIMIZATION_TASK_NOT_ESTABLISHED
OPTIMIZATION_TASK_BLOCKED
OPTIMIZATION_TASK_CONFLICTING
OPTIMIZATION_TASK_OUT_OF_SCOPE
OPTIMIZATION_TASK_UNDERDETERMINED
~~~

Provisional precedence to attack:

~~~text
OUT_OF_SCOPE
>
CONFLICTING
>
UNDERDETERMINED
>
BLOCKED
>
ESTABLISHED / PARTIAL / NOT_ESTABLISHED
~~~

PARTIAL is provisionally restricted to a task with multiple independently required in-scope optimization obligations where at least one is established and at least one is evaluably not established, with no blocked or higher-priority state.

This is a draft rule and must be boundary-attacked before protocol freeze.

## 18. Required output schema

Every future executable record should emit, as applicable:

~~~text
TASK_LOCK
CANDIDATE_SET_LOCK
ADMISSIBILITY_LEDGER
OBJECTIVE_REGISTRY
OBJECTIVE_VALUE_LEDGER
CONSTRAINT_REGISTRY
CONSTRAINT_VALUE_LEDGER
SELECTION_RULE_LOCK
UNCERTAINTY_OR_ERROR_LEDGER
REGIME_OR_TRANSITION_LEDGER
COMPUTATION_HANDOFF_IF_ANY

FEASIBLE_SET
INFEASIBLE_SET
BLOCKED_SET
CONFLICTING_SET
UNDERDETERMINED_SET
OUT_OF_SCOPE_SET

DOMINANCE_OR_ORDER_LEDGER
TIE_OR_MULTIPLICITY_LEDGER
SELECTED_OPTIMUM_OR_SET

COMPARATOR_FAIRNESS_LEDGER_IF_GAIN_TESTED
OPTIMIZATION_METHOD_GAIN_STATUS

OPTIMIZATION_PRIMARY_STATUS
OPTIMIZATION_TASK_TERMINAL
OPTIMIZATION_PROTOCOL_CONFORMANCE
MAXIMUM_SUPPORTED_CLAIM
~~~

Every claim-relevant optional ledger must be explicitly populated or marked:

~~~text
NOT_APPLICABLE
NOT_REQUESTED
BLOCKED
~~~

rather than silently omitted.

## 19. Five-interface identity

~~~text
INPUTS:
  frozen admissible candidate interface
  explicit objective registry
  explicit constraint registry
  selection / dominance / tie semantics
  objective / constraint value evidence
  optional uncertainty / transition / neighboring-method handoffs

OPERATION:
  preserve admissibility
  evaluate objective / constraint applicability
  build feasible set
  apply frozen ordering / dominance / priority semantics
  preserve ties / Pareto multiplicity
  handle blocked / conflicting / underdetermined information
  select only to the maximum scope justified by the frozen information

OUTPUTS:
  feasible / infeasible / unresolved sets
  objective / constraint ledgers
  dominance / ordering ledger
  selected optimum, tied set, Pareto set, or bounded set
  terminal / conformance / gain status
  maximum-supported claim

FAILURE_OR_NO_GAIN:
  invented objective or scalarization
  inadmissible candidate selected
  hidden constraint conversion
  unsupported ordering under uncertainty
  stale regime values
  neighboring-method substitution
  fair-baseline NO_GAIN

VALIDATION_STANDARD:
  selection follows only from frozen admissibility,
  objective, constraint, ordering, uncertainty,
  version / regime, and handoff semantics;
  information-loss limits and candidate distinctions are preserved;
  no universal objective or external validity is inferred
~~~

## 20. Draft binding-operation skeleton O1-O18

~~~text
O1  freeze task / primary claim / maximum claim
O2  freeze candidate set / representation / completeness
O3  freeze admissibility interface and typed statuses
O4  freeze objective registry
O5  freeze constraint registry
O6  freeze selection / ordering / dominance semantics
O7  evaluate required-interface availability / coherence
O8  construct feasible / infeasible / unresolved candidate sets
O9  evaluate objective applicability and values
O10 evaluate constraint statuses
O11 evaluate uncertainty / approximation / information-loss effects
O12 apply dominance / order relation
O13 preserve ties / Pareto multiplicity / partial order
O14 evaluate dynamic regime / transition invalidation
O15 apply neighboring-method non-substitution and handoffs
O16 evaluate method gain / comparator fairness if requested
O17 assign primary status and task terminal
O18 emit ledgers, protocol conformance, and maximum-supported claim
~~~

This skeleton is not yet a protocol.

## 21. Boundary-attack targets

Serious pre-protocol attack must include at least:

~~~text
A1  undefined objective value coerced to zero
A2  inadmissible candidate assigned favorable score
A3  hard constraint silently converted to penalty
A4  multiple objectives silently scalarized
A5  tied optimum mislabeled underdetermined
A6  Pareto set mislabeled unique optimum
A7  equal objective score used as structural identity
A8  incomplete candidate set used for global optimum claim
A9  overlapping uncertainty intervals used for strict order
A10 stale regime-A optimum reused after regime transition
A11 sufficient Computation plan mislabeled optimal
A12 Comparison ranking substituted for Optimization
A13 one-time optimum promoted to Control policy
A14 operation lifecycle cost omitted from a lifecycle objective
A15 aggregate / compressed objective collision ignored
A16 fair-baseline comparison with unequal candidate information
A17 sound optimization result with NO_GAIN
A18 terminal precedence / PARTIAL pressure
~~~

The attack may add cases if new boundary pressure emerges.

## 22. Current state

~~~text
SOURCE_REGISTRY_RECOVERY:
  complete

TASK_INTERFACE_DRAFT:
  v0.1 established

TASK_INTERFACE_STATUS:
  PRE-PROTOCOL HISTORICAL DRAFT
  NOT AN EXECUTABLE STANDARD

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

OPTIMIZATION_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_OPTIMIZATION_EVIDENCE_STATUS:
  source_and_interface_recovery

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 23. Next

Execute a serious pre-protocol boundary attack against the 18 frozen attack targets.

Once that attack begins, this Task Interface v0.1 draft must remain immutable historical evidence.
