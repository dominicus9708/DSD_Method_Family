# DSD Computation — Task Interface v0.1 Draft

Status: **PRE-PROTOCOL HISTORICAL DRAFT — NOT AN EXECUTABLE STANDARD**  
Date: **2026-10-03**  
Method: **Computation / DSD 계산론**  
Legacy path ID: `12A`  
Higher field: **VII. Computation & Selection / 계산·선택**

Source basis:

~~~text
SOURCE_REGISTRY_v0.1.md
commit:
  af9951011d999aef3c29a2beba6093983c1546f6
blob:
  6f5ad5731ee82fc9a6561a39ff6d66fc4bd82461
~~~

This draft is a prospective method interface built from recovered source constraints.

It is not a theorem of the predecessor papers.

Once direct boundary attack begins, this file must remain immutable historical development evidence. Refinements must be recorded in a separate amendment.

## 1. Atomic task

Working atomic Computation task:

~~~text
Given:
  a declared computational target,
  frozen source / model / interface versions,
  a declared family of evaluation units / branches / channels,
  typed status / applicability / dependency records,
  explicit cross-layer and dependency bridges,
  declared resolution / tolerance / distinguishability requirements,
  optional aggregation / compression / transition / locality handoffs,
  and any claim-relevant reuse / equivalence / invalidation rules,

determine:
  which evaluations are required,
  which evaluations may be omitted with a soundness justification,
  which subcomputations may be reused under a frozen validity scope,
  which required dependencies or interfaces are blocked,
  which relevance / dependency relations remain unresolved,
  which resolution is sufficient for the declared target,
  and which correctness obligations remain for every omission,
  reuse, approximation, or symbolic evaluation decision,

without:
  inventing dependencies,
  converting absence / inapplicability / undefinedness into zero,
  treating aggregate equality as source equivalence,
  treating one failed branch as global elimination,
  importing an objective function or cheapest-choice rule from Optimization,
  or converting a target-relative soundness result into a universal
  complexity or runtime claim.
~~~

The phrase `required evaluation` is always relative to the frozen target, interface, equivalence/tolerance, and declared dependency semantics.

## 2. Method boundary

Computation asks:

~~~text
What must actually be evaluated for this declared target,
what may be omitted soundly,
what may be reused soundly,
and at what declared resolution?
~~~

It does not by itself answer:

~~~text
Which sufficient plan is cheapest or best?
Which resource allocation maximizes an objective?
What future physical state occurs?
What simulation trajectory should be executed?
What measurement was observed?
What compressed representation should be stored?
What aggregate summary should be produced?
Is a soundness audit itself the computation plan?
~~~

Working distinctions:

~~~text
COMPUTATION:
  required evaluation / sound omission / scoped reuse

OPTIMIZATION:
  choice among admissible alternatives
  under explicit objective and constraints

ANALYSIS:
  structural decomposition / re-expression

AGGREGATION:
  construction of a summary / composite readout

COMPRESSION:
  intentional representation reduction

MEASUREMENT:
  evidence acquisition / discrimination interface

SIMULATION:
  execution of a supplied dynamic model

PREDICTION:
  future-target claim

AUDIT:
  evaluation of conformance / soundness evidence
~~~

## 3. Primary claim levels

A task freezes one primary claim level.

~~~text
REQUIRED_EVALUATION_SET

SOUND_OMISSION_SET

SCOPED_REUSE_PLAN

SUFFICIENT_RESOLUTION_FOR_DECLARED_TARGET

COMPUTATION_PLAN_FOR_DECLARED_TARGET

SYMBOLIC_OR_CLASS_LEVEL_EVALUATION_PLAN
~~~

Interpretation:

~~~text
REQUIRED_EVALUATION_SET:
  determine units that cannot be omitted under the frozen target
  and dependency semantics

SOUND_OMISSION_SET:
  determine units that need not be evaluated because
  a frozen rule establishes target-relative irrelevance or equivalence

SCOPED_REUSE_PLAN:
  determine which already-computed or common subcomputations
  may be reused under a frozen reuse equivalence and validity scope

SUFFICIENT_RESOLUTION_FOR_DECLARED_TARGET:
  determine a resolution / tolerance sufficient to preserve
  the declared target distinctions or error bound

COMPUTATION_PLAN_FOR_DECLARED_TARGET:
  combine required / omitted / reused / blocked / unresolved units
  into a bounded plan without claiming global cost optimality

SYMBOLIC_OR_CLASS_LEVEL_EVALUATION_PLAN:
  represent an intensional / parametric / theorem-described family
  without requiring literal enumeration of every unit
~~~

No claim level implies a globally minimum evaluation count, runtime, memory use, energy use, or cost unless a separate theorem or Optimization task establishes it.

## 4. Required task lock

Every future executable Computation task should freeze at least:

~~~text
COMPUTATION_TASK_ID
TASK_VERSION

PRIMARY_CLAIM_LEVEL
COMPUTATIONAL_TARGET_ID
TARGET_VERSION_OR_DEFINITION
TARGET_OUTPUT_SCOPE

TARGET_EQUIVALENCE_OR_TOLERANCE
TARGET_ERROR_SEMANTICS
MAXIMUM_SUPPORTED_CLAIM

SOURCE_MODEL_ID
SOURCE_MODEL_VERSION
ACTIVE_DSD_LAYERS

EVALUATION_CLASS_ID
EVALUATION_CLASS_VERSION_OR_DEFINITION
EVALUATION_CLASS_REPRESENTATION_MODE
EVALUATION_MODE
EVALUATION_CLASS_COMPLETENESS_STATUS

DEPENDENCY_INTERFACE_ID
DEPENDENCY_INTERFACE_VERSION_OR_DEFINITION
DEPENDENCY_SEMANTICS

REQUIRED_INTERFACE_POLICY

RESOLUTION_REQUIREMENT
DISTINGUISHABILITY_REQUIREMENT
~~~

Conditionally required when claim-relevant:

~~~text
FORMATION_STATUS_HANDOFF
PROPERTY_STATUS_HANDOFF
CHANNEL_REGISTRY
BRANCH_REGISTRY

CROSS_LAYER_BRIDGE_ID
CROSS_LAYER_BRIDGE_VERSION

AGGREGATION_HANDOFF
COMPRESSION_HANDOFF
COLLISION_OR_INJECTIVITY_HANDOFF

REUSE_EQUIVALENCE_ID
REUSE_EQUIVALENCE_VERSION
REUSE_VALIDITY_SCOPE
REUSE_INVALIDATION_RULE

OMISSION_RULE_ID
OMISSION_RULE_VERSION
OMISSION_VALIDITY_SCOPE

APPROXIMATION_RULE_ID
APPROXIMATION_ERROR_BOUND

DYNAMIC_REGIME
TRANSITION_HANDOFF
LINEAGE_HANDOFF
LOCALITY_OR_PROPAGATION_HANDOFF

COST_EVIDENCE_SCHEMA
COMPLEXITY_EVIDENCE_SCHEMA
~~~

Changing a claim-relevant lock after seeing an evaluation disposition opens a new task version.

## 5. Evaluation-class representation

The interface must not require every computation family to be finitely enumerated.

Working representation modes:

~~~text
EXPLICIT_ENUMERATION
PARAMETRIC_CLASS
PREDICATE_DEFINED_CLASS
RELATION_DEFINED_CLASS
SYMBOLIC_EXPRESSION_FAMILY
GRAPH_OR_DAG_DEFINED_CLASS
EXTERNALLY_SUPPLIED_CLASS_INTERFACE
~~~

Working evaluation modes:

~~~text
ELEMENTWISE
SYMBOLIC_SET
DEPENDENCY_CLOSURE
THEOREM_OR_RELATION_BASED
GRAPH_PROPAGATION
FIXED_POINT_IF_EXPLICITLY_SUPPLIED
EXTERNALLY_SUPPLIED_EVALUATOR
~~~

Class completeness status:

~~~text
EVALUATION_CLASS_DECLARED_BOUNDED
EVALUATION_CLASS_CLAIMED_COMPLETE_WITHIN_SCOPE
EVALUATION_CLASS_COMPLETENESS_UNDERDETERMINED
EVALUATION_CLASS_COMPLETENESS_NOT_CLAIMED
~~~

Draft guards:

~~~text
NON_ENUMERATED
  !=
UNDECLARED

SYMBOLIC_EVALUATION
  !=
UNEXECUTED_GUESS

DECLARED_BOUNDED_CLASS
  !=
COMPLETE_REALITY_CLASS
~~~

## 6. Typed status and applicability discipline

When Formation or Property status affects whether an evaluation is meaningful, preserve the inherited distinctions.

Formation-side examples:

~~~text
UNDEFINED_ASSIGNMENT
DEFINED_ZERO
DEFINED_NONZERO_OR_OTHER_VALUE
CHANNEL_ABSENCE
ADMITTED_CHANNEL_WITH_ZERO_COMPONENT_TERM
~~~

Property-side examples:

~~~text
UNDECLARED
PROFILE_UNAVAILABLE
INAPPLICABLE
PREREQUISITE_UNSATISFIED
APPLICABLE_BUT_UNDEFINED
DEFINED_ZERO
DEFINED_NONZERO_OR_OTHER_VALUE
~~~

Draft guards:

~~~text
NOT_ADMITTED != ZERO_CONTRIBUTION
INAPPLICABLE != COMPUTED_ZERO
PREREQUISITE_UNSATISFIED != FALSE_NUMERICAL_OUTPUT
APPLICABLE_BUT_UNDEFINED != ZERO
UNDEFINED != ZERO
~~~

A status may justify that one declared operation is inapplicable. It does not automatically establish that every downstream computational target is unaffected.

## 7. Dependency interface

A Computation task must freeze a claim-relevant dependency interface.

Allowed working forms may include:

~~~text
directed dependency graph
directed acyclic graph
relation-valued dependency family
hypergraph / multi-input dependency relation
typed prerequisite relation
functional composition graph
externally supplied dependency interface
~~~

For every dependency edge or relation used in a pruning/reuse decision, retain:

~~~text
DEPENDENCY_ID
SOURCE_UNIT_OR_CLASS
TARGET_UNIT_OR_CLASS
DEPENDENCY_TYPE
APPLICABILITY_SCOPE
VERSION_OR_DEFINITION
PROVENANCE_OR_JUSTIFICATION
REQUIRED_OR_OPTIONAL_ROLE
~~~

Draft guards:

~~~text
STATIC_DEPENDENCY != DYNAMIC_CAUSAL_DEPENDENCY

STRUCTURAL_NEIGHBORHOOD != COMPUTATIONAL_DEPENDENCY

SHARED_LABEL != SHARED_DEPENDENCY

ONE_FAILED_EDGE_OR_BRANCH
  !=
WHOLE_CLASS_IRRELEVANCE
~~~

A multi-input Property datum may not be assigned to a unary channel dependency unless an explicit association/selector is supplied.

## 8. Required-interface status

Each claim-relevant required interface should receive one working status:

~~~text
REQUIRED_COMPUTATION_INTERFACE_AVAILABLE
REQUIRED_COMPUTATION_INTERFACE_UNAVAILABLE
REQUIRED_COMPUTATION_INTERFACE_CONFLICTING
REQUIRED_COMPUTATION_INTERFACE_UNDERDETERMINED
REQUIRED_COMPUTATION_INTERFACE_OUT_OF_SCOPE
~~~

Working consequences:

~~~text
UNAVAILABLE:
  required evaluation / omission / reuse disposition is BLOCKED

CONFLICTING:
  mutually incompatible frozen interface records exist
  with no declared precedence

UNDERDETERMINED:
  several admissible interface semantics remain
  and produce different dispositions

OUT_OF_SCOPE:
  requested interface operation lies outside the declared task
~~~

Draft guards:

~~~text
UNAVAILABLE_REQUIRED_INTERFACE
  !=
BRANCH_IRRELEVANCE

MISSING_DEPENDENCY_RECORD
  !=
NEGATIVE_DEPENDENCY

BLOCKED
  !=
SOUNDLY_OMITTED
~~~

## 9. Influence / relevance discipline

Omission requires a positive justification relative to the target.

Working relevance status:

~~~text
TARGET_RELEVANT_ESTABLISHED
TARGET_IRRELEVANT_ESTABLISHED
TARGET_RELEVANCE_BLOCKED
TARGET_RELEVANCE_CONFLICTING
TARGET_RELEVANCE_UNDERDETERMINED
TARGET_RELEVANCE_OUT_OF_SCOPE
~~~

A target-irrelevance proof may use, when explicitly supplied:

~~~text
dependency closure
zero sensitivity / derivative theorem
support separation
exact equivalence
symmetry / invariance
algebraic cancellation with source-level side conditions
finite-propagation exclusion
declared tolerance / error bound
domain-specific theorem
~~~

But:

~~~text
OMITTED
  !=
PROVED_IRRELEVANT

AGGREGATE_INVISIBLE
  !=
COMPONENT_IRRELEVANT

NO_DIRECT_EDGE
  !=
NO_INDIRECT_INFLUENCE

CURRENTLY_ZERO
  !=
ALWAYS_IRRELEVANT
~~~

## 10. Omission discipline

Working evaluation-unit disposition includes:

~~~text
COMPUTATION_UNIT_REQUIRED
COMPUTATION_UNIT_SOUNDLY_OMITTABLE
COMPUTATION_UNIT_REUSABLE
COMPUTATION_UNIT_BLOCKED
COMPUTATION_UNIT_CONFLICTING
COMPUTATION_UNIT_OUT_OF_SCOPE
COMPUTATION_UNIT_UNDERDETERMINED
~~~

`SOUNDLY_OMITTABLE` requires a frozen omission rule and claim-relevant justification.

The omission record should retain:

~~~text
OMITTED_UNIT_ID
OMISSION_RULE_ID
OMISSION_JUSTIFICATION
TARGET_SCOPE
VALIDITY_SCOPE
DEPENDENCY_CLOSURE_STATUS
ERROR_OR_EQUIVALENCE_BOUND
INVALIDATION_CONDITIONS
~~~

A unit may be omitted for one target and required for another.

## 11. Reuse / common-subcomputation discipline

Reuse is not licensed by naming or output coincidence alone.

Freeze:

~~~text
REUSE_CLASS_ID
REUSE_EQUIVALENCE
REUSE_KEY
REUSE_INPUT_SCOPE
REUSE_OUTPUT_SCOPE
REUSE_VALIDITY_SCOPE
REUSE_INVALIDATION_RULE
VERSION / REGIME / STATUS LOCKS
~~~

Working reuse status:

~~~text
REUSE_ESTABLISHED_ON_DECLARED_SCOPE
REUSE_NOT_ESTABLISHED
REUSE_BLOCKED
REUSE_CONFLICTING
REUSE_UNDERDETERMINED
REUSE_OUT_OF_SCOPE
~~~

Draft guards:

~~~text
SAME_LABEL_OR_SHAPE
  !=
REUSABLE_SUBCOMPUTATION

SAME_AGGREGATE_OUTPUT
  !=
REUSE_EQUIVALENCE

EQUAL_CURRENT_VALUE
  !=
EQUAL_FUTURE_COMPUTATION

CACHE_HIT
  !=
SEMANTIC_REUSE_VALIDITY

REUSE_ON_VERSION_V
  !=
REUSE_ON_VERSION_V_PLUS_1
~~~

## 12. Information-loss / aggregation / compression discipline

If an omission or reuse argument consumes an aggregate, compressed representation, projection, or reduced readout, record:

~~~text
READOUT_OR_REDUCTION_ID
VERSION
COLLISION_STATUS
INJECTIVITY_SCOPE
SUPPORT_RETENTION_STATUS
RECONSTRUCTION_SCOPE_IF_RELEVANT
REQUIRED_SIDECARS
~~~

Draft guards:

~~~text
OUTPUT_EQUALITY != SOURCE_EQUIVALENCE

AGGREGATE_EQUALITY != CACHE_EQUIVALENCE

EQUAL_REDUCED_READOUT
  !=
EQUAL_COMPONENT_STATE

LOSSLESS_ON_DECLARED_CLASS
  !=
GLOBAL_EQUIVALENCE
~~~

Computation may consume a valid Aggregation/Compression handoff.

It does not convert the forward reduction operation into Computation itself.

## 13. Resolution / approximation discipline

If the task uses reduced resolution, approximation, truncation, discretization, thresholding, sampling, or early stopping, freeze:

~~~text
RESOLUTION_ID
RESOLUTION_VERSION_OR_DEFINITION
TARGET_DISTINGUISHABILITY_REQUIREMENT
APPROXIMATION_RULE
ERROR_METRIC_OR_RELATION
ERROR_BOUND
ERROR_COMPOSITION_RULE_IF_MULTISTAGE
ACCEPTANCE_THRESHOLD
VALIDITY_SCOPE
~~~

Working resolution outcome:

~~~text
RESOLUTION_SUFFICIENT_FOR_DECLARED_TARGET
RESOLUTION_NOT_SUFFICIENT
RESOLUTION_ASSESSMENT_BLOCKED
RESOLUTION_ASSESSMENT_CONFLICTING
RESOLUTION_ASSESSMENT_UNDERDETERMINED
RESOLUTION_ASSESSMENT_OUT_OF_SCOPE
~~~

Draft guards:

~~~text
LOWER_RESOLUTION
  !=
SAFE_COMPUTATION

SMALL_LOCAL_ERROR
  !=
BOUNDED_END_TO_END_ERROR

COMPONENTWISE_TOLERANCE
  !=
RELATIONAL_TARGET_PRESERVATION

NUMERIC_CONVERGENCE
  !=
SEMANTIC_TARGET_EQUIVALENCE
~~~

## 14. Finite / countable / recursive computation boundary

The source layers distinguish finite composition from optional countable extension.

A Computation task should therefore freeze:

~~~text
EVALUATION_CARDINALITY_MODE
FINITE_FAMILY
COUNTABLE_FAMILY
OTHER_SYMBOLIC_FAMILY

CONVERGENCE_OR_TERMINATION_INTERFACE
ORDER_DEPENDENCE_STATUS
FIXED_POINT_OR_RECURSION_RULE_IF_ANY
~~~

Draft guards:

~~~text
FINITE_CORRECTNESS
  !=
COUNTABLE_CORRECTNESS

ABSOLUTE_SUMMABILITY_OR_OTHER_DECLARED_CONDITION
  must not be silently omitted

FINITE_DAG_TERMINATION
  !=
GENERAL_RECURSIVE_TERMINATION
~~~

The future protocol must not manufacture well-foundedness, convergence, or termination where no such interface is supplied.

## 15. Dynamic / transition / locality discipline

If computation uses dynamic support, temporal locality, finite propagation, or cache reuse across time, freeze:

~~~text
TEMPORAL_SCOPE
ACTIVE_REGIME
REGULAR_SUPPORT_SIGNATURE
TRANSITION_RELATION_ID
TRANSITION_RELATION_VERSION
LINEAGE_HANDOFF_IF_USED

LOCALIZATION_CARRIER
PROPAGATION_METRIC
METRIC_TIME_SCALE
DISCREPANCY_CONVENTION
PROPAGATION_BOUND
PROPAGATION_BOUND_PROVENANCE
SUPPORT_FAITHFULNESS_STATUS
~~~

Draft guards:

~~~text
FINITE_PROPAGATION_SPECIALIZATION
  !=
UNIVERSAL_DSD_PROPAGATION

PROPAGATION_BOUND
  !=
COMPUTATION_COST_BOUND

OUTSIDE_CURRENT_CONE
  !=
PERMANENT_IRRELEVANCE

REGULAR_EPOCH_REUSE
  !=
CROSS_TRANSITION_REUSE

RANK_OR_DIMENSION_LABEL
  !=
UNIVERSAL_COMPLEXITY_BOUND
~~~

Claim-relevant transition invalidates inherited reuse unless a frozen transition/equivalence bridge licenses reuse across that transition.

## 16. Computation vs Optimization boundary

Computation may determine several sufficient plans.

It does not select the cheapest / fastest / lowest-memory / lowest-energy plan merely because cost evidence is available.

Working handoff:

~~~text
SUFFICIENT_COMPUTATION_PLAN_SET
COST_OR_RESOURCE_DESCRIPTORS
OPTIMIZATION_HANDOFF_IF_REQUESTED
~~~

Draft guards:

~~~text
SUFFICIENT
  !=
OPTIMAL

MINIMAL_BY_PROOF
  may be a Computation theorem
  only when minimality follows from frozen mathematical constraints

CHEAPEST_AMONG_ADMISSIBLE
  is Optimization when a cost objective is supplied

MEASURED_SPEEDUP
  !=
SOUNDNESS_PROOF

SOUNDNESS_PROOF
  !=
MEASURED_SPEEDUP
~~~

## 17. Complexity / performance evidence

Complexity or performance is a separate ledger.

Possible evidence:

~~~text
EVALUATION_COUNT
ASYMPTOTIC_BOUND
RUNTIME
MEMORY
COMMUNICATION
ENERGY
IO_VOLUME
CACHE_HIT_RATE
PARALLEL_EFFICIENCY
~~~

Every such claim should freeze:

~~~text
COST_METRIC_ID
MEASUREMENT_OR_PROOF_METHOD
HARDWARE_OR_EXECUTION_ENVIRONMENT_IF_EMPIRICAL
INPUT_FAMILY
BASELINE
UNCERTAINTY_OR_VARIABILITY_IF_RELEVANT
~~~

Draft guards:

~~~text
SOUND_PRUNING
  !=
COMPLEXITY_IMPROVEMENT

FEWER_EVALUATION_UNITS
  !=
LOWER_WALL_CLOCK_TIME

LOWER_RUNTIME_ON_ONE_MACHINE
  !=
UNIVERSAL_COMPLEXITY_GAIN

NO_GAIN
  !=
METHOD_FAILURE
~~~

A Computation method result may be valid and still have `NO_GAIN` relative to a competent baseline.

## 18. Evaluation-set outcome

After unit-level evaluation, record one working set outcome:

~~~text
COMPUTATION_SET_FULLY_PLANNED

COMPUTATION_SET_PARTIALLY_PLANNED

COMPUTATION_SET_BLOCKED

COMPUTATION_SET_CONFLICTING

COMPUTATION_SET_UNDERDETERMINED

COMPUTATION_SET_OUT_OF_SCOPE
~~~

Separate unit counts:

~~~text
REQUIRED_EVALUATION_SET
SOUNDLY_OMITTED_EVALUATION_SET
REUSED_EVALUATION_SET
BLOCKED_EVALUATION_SET
CONFLICTING_EVALUATION_SET
UNDERDETERMINED_EVALUATION_SET
OUT_OF_SCOPE_EVALUATION_SET
~~~

A task may be fully planned even if many units are soundly omitted.

## 19. Working primary Computation status

Overall primary status family:

~~~text
COMPUTATION_ESTABLISHED
COMPUTATION_NOT_ESTABLISHED
COMPUTATION_BLOCKED
COMPUTATION_CONFLICTING
COMPUTATION_OUT_OF_SCOPE
COMPUTATION_UNDERDETERMINED
~~~

Interpretation:

~~~text
ESTABLISHED:
  requested claim level is supported under
  the frozen target / interface / evaluation semantics

NOT_ESTABLISHED:
  all required claim-evaluation information is present
  but the requested claim level fails evaluably

BLOCKED:
  required dependency / interface / proof obligation is unavailable

CONFLICTING:
  frozen claim-relevant rules or dependency records are incompatible
  and no precedence resolves them

OUT_OF_SCOPE:
  requested operation is not a Computation task
  or lies outside the declared target/evaluation interface

UNDERDETERMINED:
  multiple admissible claim-relevant semantics remain
  and produce different computation dispositions
~~~

Important:

~~~text
NO_GAIN
  may coexist with
COMPUTATION_ESTABLISHED
~~~

when soundness is established but no computational improvement over the frozen baseline is demonstrated.

## 20. Working task terminal

The future protocol is expected to emit exactly one task terminal:

~~~text
COMPUTATION_TASK_ESTABLISHED

COMPUTATION_TASK_PARTIAL

COMPUTATION_TASK_NOT_ESTABLISHED

COMPUTATION_TASK_BLOCKED

COMPUTATION_TASK_CONFLICTING

COMPUTATION_TASK_OUT_OF_SCOPE

COMPUTATION_TASK_UNDERDETERMINED
~~~

Draft meaning of `PARTIAL`:

~~~text
multiple independently required computation obligations exist,
at least one is validly established,
at least one other independently required obligation
is validly not established,
and no required obligation is blocked
and no higher-priority terminal applies
~~~

Draft terminal precedence candidate:

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

This precedence is **not frozen**.

It is a direct boundary-attack target.

## 21. Soundness-obligation ledger

Every omission, reuse, approximation, or symbolic class-level replacement should create an explicit obligation record:

~~~text
OBLIGATION_ID
OBLIGATION_TYPE

AFFECTED_UNIT_OR_CLASS
CLAIMED_SHORTCUT_OR_REUSE

TARGET_SCOPE
VALIDITY_SCOPE

REQUIRED_ASSUMPTIONS
SUPPORTING_THEOREM_OR_RULE
SUPPORTING_INTERFACE_VERSION

STATUS:
  ESTABLISHED
  NOT_ESTABLISHED
  BLOCKED
  CONFLICTING
  UNDERDETERMINED
  OUT_OF_SCOPE

INVALIDATION_CONDITIONS
PROVENANCE
~~~

No shortcut is valid merely because it was executed successfully once.

## 22. Binding-operation draft

Working operation:

~~~text
C1
  freeze task identity, primary claim, target,
  target equivalence/tolerance, scope, and maximum claim

C2
  freeze source/model/interface versions and active DSD layers

C3
  freeze evaluation class representation,
  evaluation mode, and class-completeness status

C4
  freeze typed status/applicability and branch/channel registries

C5
  freeze dependency interfaces and cross-layer bridges

C6
  freeze required-interface policy

C7
  freeze resolution / distinguishability /
  approximation / error semantics

C8
  register aggregation / compression /
  collision / injectivity handoffs when used

C9
  register omission rules and target-relevance rules

C10
  register reuse equivalence, validity scope,
  and invalidation rules

C11
  register dynamic regime / transition /
  locality / propagation handoffs when used

C12
  evaluate unit-level required / omittable /
  reusable / blocked / conflicting / underdetermined dispositions

C13
  evaluate every soundness obligation

C14
  construct evaluation-set outcome and bounded computation plan

C15
  separate soundness result from cost / complexity evidence

C16
  emit Optimization handoff only when objective-based selection is requested

C17
  assign primary Computation status and task terminal

C18
  emit protocol-conformance placeholder,
  method-gain placeholder, and maximum-supported claim
~~~

No future protocol may silently change C1-C11 after observing computation-plan outcomes.

## 23. Output contract draft

A future executable run should emit:

~~~text
LOCKED_COMPUTATION_TASK_RECORD

TARGET_AND_EQUIVALENCE_RECORD

EVALUATION_CLASS_RECORD
EVALUATION_UNIT_REGISTRY

STATUS_AND_APPLICABILITY_LEDGER
DEPENDENCY_AND_BRIDGE_REGISTER
REQUIRED_INTERFACE_REGISTER

REQUIRED_EVALUATION_SET
SOUNDLY_OMITTED_EVALUATION_SET
REUSED_EVALUATION_SET
BLOCKED_EVALUATION_SET
CONFLICTING_EVALUATION_SET
UNDERDETERMINED_EVALUATION_SET
OUT_OF_SCOPE_EVALUATION_SET

OMISSION_JUSTIFICATION_LEDGER
REUSE_VALIDITY_LEDGER
SOUNDNESS_OBLIGATION_LEDGER

RESOLUTION_AND_ERROR_LEDGER
INFORMATION_LOSS_HANDOFF_LEDGER
DYNAMIC_TRANSITION_LOCALITY_LEDGER_IF_USED

COMPUTATION_SET_OUTCOME
COMPUTATION_PLAN

COST_COMPLEXITY_EVIDENCE_LEDGER
OPTIMIZATION_HANDOFF_IF_ANY

COMPUTATION_PRIMARY_STATUS
COMPUTATION_TASK_TERMINAL
COMPUTATION_PROTOCOL_CONFORMANCE
COMPUTATION_METHOD_GAIN_STATUS

MAXIMUM_SUPPORTED_CLAIM
~~~

## 24. Five-interface identity

~~~text
INPUTS:
  declared computational target and equivalence/tolerance
  frozen source/model/interface versions
  evaluation class / units / branches / channels
  typed statuses and applicability
  explicit dependency and bridge records
  optional reduction / dynamic / locality / resolution handoffs

OPERATION:
  determine target-relative required evaluations;
  justify sound omissions;
  validate scoped reuse;
  preserve blocked/conflicting/underdetermined dependencies;
  evaluate resolution and approximation obligations;
  assemble a bounded computation plan

OUTPUTS:
  required/omitted/reused/blocked/unresolved evaluation sets
  soundness-obligation ledger
  resolution/error ledger
  bounded computation plan
  separate cost/complexity evidence
  optional Optimization handoff

FAILURE_OR_NO_GAIN:
  unsound omission
  invalid reuse
  missing required dependency/interface
  unresolved conflicting semantics
  unsupported resolution/approximation
  hidden neighboring-method substitution
  no measured/proved gain over fair baseline

VALIDATION_STANDARD:
  every omission/reuse/approximation follows from frozen target,
  dependency, interface, and validity semantics;
  typed status distinctions are preserved;
  information-loss and transition limits are preserved;
  no objective-based Optimization is smuggled in;
  soundness and performance claims are separately supported
~~~

## 25. Core draft guards

~~~text
NOT_ADMITTED != ZERO_CONTRIBUTION

INAPPLICABLE != COMPUTED_ZERO

APPLICABLE_BUT_UNDEFINED != FALSE_RESULT

ONE_FAILED_BRANCH != GLOBAL_PRUNING_LICENSE

OUTPUT_EQUALITY != SOURCE_EQUIVALENCE

AGGREGATE_EQUALITY != CACHE_EQUIVALENCE

SAME_LABEL_OR_SHAPE != REUSABLE_SUBCOMPUTATION

OMITTED != PROVED_IRRELEVANT

STATIC_DEPENDENCY != DYNAMIC_CAUSAL_DEPENDENCY

FORMATION_STAGE_ORDER != RUNTIME_SCHEDULE

FIRST_BRANCH != AUTOMATIC_EXECUTION_CUTOFF

FINITE_PROPAGATION_BOUND != UNIVERSAL_DSD_PRUNING_RULE

LOWER_RESOLUTION != SAFE_COMPUTATION

FINITE_CORRECTNESS != COUNTABLE_CORRECTNESS

SOUND_PRUNING != COMPLEXITY_IMPROVEMENT

FEWER_EVALUATIONS != LOWER_WALL_CLOCK_TIME

COMPUTATION != OPTIMIZATION

COMPUTATION_PLAN != SIMULATION_EXECUTION

SOUNDNESS_AUDIT != COMPUTATION_PLAN

NO_GAIN != METHOD_FAILURE
~~~

## 26. Current state

~~~text
SOURCE_REGISTRY_RECOVERY:
  complete

TASK_INTERFACE_DRAFT:
  v0.1 established

PRE_PROTOCOL_BOUNDARY_ATTACKS:
  0

BOUNDARY_AMENDMENT:
  not established

DEDICATED_COMPUTATION_PROTOCOL:
  not established

DIRECT_COMPUTATION_PILOTS_ATTEMPTED:
  0

BASELINE_COMPUTATION_CASES:
  0

NO_GAIN_COMPUTATION_CASES:
  0

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
  source_and_interface_recovery

PROTOCOL_REVISION_REQUIRED:
  not applicable

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 27. Next

Freeze this draft as historical development evidence and execute a serious pre-protocol boundary attack.

Boundary review must especially pressure:

~~~text
evaluation-class completeness
symbolic / infinite-family evaluation
required vs omittable semantics
blocked vs conflicting vs underdetermined
one failed branch vs family elimination
aggregate/readout equality vs source equivalence
reuse equivalence and invalidation
version / status / regime transitions
approximation and end-to-end error
finite vs countable / recursive computation
finite-propagation pruning assumptions
Computation vs Optimization
Computation vs Simulation
soundness vs performance gain
task-terminal precedence
PARTIAL semantics
~~~
