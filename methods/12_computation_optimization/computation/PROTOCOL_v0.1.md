# DSD Computation Protocol v0.1

Status: **FROZEN EXECUTABLE INTERNAL PROTOCOL — NOT YET INTERNALLY STANDARDIZED**  
Date: **2026-10-03**  
Method: **Computation / DSD 계산론**  
Legacy path ID: `12A`  
Higher field: **VII. Computation & Selection / 계산·선택**

## 1. Frozen lineage of this protocol

This Protocol is frozen from the following immutable development lineage.

~~~text
SOURCE_REGISTRY_COMMIT:
  af9951011d999aef3c29a2beba6093983c1546f6

SOURCE_REGISTRY_BLOB:
  6f5ad5731ee82fc9a6561a39ff6d66fc4bd82461

TASK_INTERFACE_COMMIT:
  e0376c35c9fd6c6ab2fc1a20a5bc0e329fc0fb71

TASK_INTERFACE_BLOB:
  0e307f2e6bb3b579a8bc161cb0a25bd76c28e69f

BOUNDARY_ATTACK_COMMIT:
  addbcb62647e5dca82255d9bd978eee9ec76b8c1

BOUNDARY_ATTACK_BLOB:
  8e1ea692251835b1cb58c68f6598d9f8f7695e86

BOUNDARY_AMENDMENT_COMMIT:
  a5dacd3e80544d4a5058c1497cb2062124717c72

BOUNDARY_AMENDMENT_BLOB:
  1490548c203f70db5054007a27456e2073f1a7da
~~~

Historical Task Interface and boundary-attack records are not rewritten by this Protocol.

This Protocol operationalizes the seven prospective refinements of Boundary Amendment 001.

It does not establish internal standardization by itself.

## 2. Atomic method task

A Computation task receives:

~~~text
a declared computational target

frozen source / model / interface versions

a declared evaluation class,
branch family, channel family,
or symbolic evaluation family

typed Formation / Property /
status / applicability handoffs

explicit dependency interfaces
and cross-layer bridges

resolution / tolerance /
distinguishability requirements

optional aggregation / compression /
transition / locality / propagation handoffs

optional reuse / cache /
equivalence / invalidation interfaces

optional complexity / performance comparator
~~~

and determines:

~~~text
which semantic results are required for the target

which required obligations must be evaluated fresh

which required obligations may be discharged by valid reuse

which required obligations may be discharged symbolically

which units are target-irrelevant and may be omitted soundly

which dependencies or interfaces are blocked,
conflicting, underdetermined, or out of scope

which resolution / approximation is sufficient
for the frozen target

which closure / convergence / termination
conditions are required

which soundness obligations remain attached
to omission, reuse, approximation,
symbolic evaluation, or locality pruning

and the bounded computation plan supported
by the frozen task interface
~~~

The Protocol does not silently optimize among sufficient plans.

~~~text
COMPUTATION != OPTIMIZATION
~~~

## 3. Primary claim levels

Exactly one primary claim level is frozen per task.

~~~text
REQUIRED_EVALUATION_SET

SOUND_OMISSION_SET

SCOPED_REUSE_PLAN

SUFFICIENT_RESOLUTION_FOR_DECLARED_TARGET

COMPUTATION_PLAN_FOR_DECLARED_TARGET

SYMBOLIC_OR_CLASS_LEVEL_EVALUATION_PLAN
~~~

A primary claim does not imply global runtime, memory, energy, communication, evaluation-count, or complexity optimality.

## 4. Validity gates G1-G18

### G1 — task / version / primary-claim / target lock

Freeze:

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
~~~

Changing a claim-relevant lock after seeing task outcomes requires a new task version.

### G2 — source / model / interface lock

Freeze:

~~~text
SOURCE_MODEL_ID
SOURCE_MODEL_VERSION
ACTIVE_DSD_LAYERS

SOURCE_INTERFACE_ID
SOURCE_INTERFACE_VERSION_OR_DEFINITION
SOURCE_INTERFACE_PROVENANCE
~~~

No source/model/interface substitution is permitted under the same task identity after results are observed.

### G3 — evaluation-class representation / mode / completeness lock

Freeze:

~~~text
EVALUATION_CLASS_ID
EVALUATION_CLASS_VERSION_OR_DEFINITION

EVALUATION_CLASS_REPRESENTATION_MODE

EVALUATION_MODE

EVALUATION_CLASS_COMPLETENESS_STATUS
~~~

Allowed representation modes:

~~~text
EXPLICIT_ENUMERATION
PARAMETRIC_CLASS
PREDICATE_DEFINED_CLASS
RELATION_DEFINED_CLASS
SYMBOLIC_EXPRESSION_FAMILY
GRAPH_OR_DAG_DEFINED_CLASS
EXTERNALLY_SUPPLIED_CLASS_INTERFACE
~~~

Allowed evaluation modes:

~~~text
ELEMENTWISE
SYMBOLIC_SET
DEPENDENCY_CLOSURE
THEOREM_OR_RELATION_BASED
GRAPH_PROPAGATION
FIXED_POINT_IF_EXPLICITLY_SUPPLIED
EXTERNALLY_SUPPLIED_EVALUATOR
~~~

Class-completeness statuses:

~~~text
EVALUATION_CLASS_DECLARED_BOUNDED
EVALUATION_CLASS_CLAIMED_COMPLETE_WITHIN_SCOPE
EVALUATION_CLASS_COMPLETENESS_UNDERDETERMINED
EVALUATION_CLASS_COMPLETENESS_NOT_CLAIMED
~~~

Required guards:

~~~text
NON_ENUMERATED != UNDECLARED
DECLARED_BOUNDED_CLASS != COMPLETE_REALITY_CLASS
~~~

### G4 — typed status / applicability / channel lock

When claim-relevant, freeze and preserve native typed statuses.

Formation-side distinctions include:

~~~text
UNDEFINED_ASSIGNMENT
DEFINED_ZERO
DEFINED_NONZERO_OR_OTHER_VALUE
CHANNEL_ABSENCE
ADMITTED_CHANNEL_WITH_ZERO_COMPONENT_TERM
~~~

Property-side distinctions include:

~~~text
UNDECLARED
PROFILE_UNAVAILABLE
INAPPLICABLE
PREREQUISITE_UNSATISFIED
APPLICABLE_BUT_UNDEFINED
DEFINED_ZERO
DEFINED_NONZERO_OR_OTHER_VALUE
~~~

Required guards:

~~~text
NOT_ADMITTED != ZERO_CONTRIBUTION
INAPPLICABLE != COMPUTED_ZERO
PREREQUISITE_UNSATISFIED != FALSE_NUMERICAL_OUTPUT
APPLICABLE_BUT_UNDEFINED != ZERO
UNDEFINED != ZERO
~~~

### G5 — dependency / bridge lock

Freeze every claim-relevant dependency or bridge:

~~~text
DEPENDENCY_INTERFACE_ID
DEPENDENCY_INTERFACE_VERSION_OR_DEFINITION
DEPENDENCY_SEMANTICS

DEPENDENCY_ID
SOURCE_UNIT_OR_CLASS
TARGET_UNIT_OR_CLASS
DEPENDENCY_TYPE
APPLICABILITY_SCOPE
VERSION_OR_DEFINITION
PROVENANCE_OR_JUSTIFICATION
REQUIRED_OR_OPTIONAL_ROLE

CROSS_LAYER_BRIDGE_ID
CROSS_LAYER_BRIDGE_VERSION
CROSS_LAYER_BRIDGE_SCOPE
~~~

Supported dependency structures may be graph-, DAG-, relation-, hypergraph-, typed-prerequisite-, functional-composition-, or externally supplied.

Required guards:

~~~text
STATIC_DEPENDENCY != DYNAMIC_CAUSAL_DEPENDENCY
STRUCTURAL_NEIGHBORHOOD != COMPUTATIONAL_DEPENDENCY
SHARED_LABEL != SHARED_DEPENDENCY
ONE_FAILED_EDGE_OR_BRANCH != WHOLE_CLASS_IRRELEVANCE
ONE_FAILED_BRANCH != GLOBAL_PRUNING_LICENSE
~~~

### G6 — required-interface availability / coherence gate

For each claim-relevant required interface freeze:

~~~text
REQUIRED_COMPUTATION_INTERFACE_ID
REQUIRED_COMPUTATION_INTERFACE_ROLE
REQUIRED_COMPUTATION_INTERFACE_VERSION_OR_DEFINITION
REQUIRED_COMPUTATION_INTERFACE_STATUS
REQUIRED_COMPUTATION_INTERFACE_PROVENANCE
~~~

Status family:

~~~text
REQUIRED_COMPUTATION_INTERFACE_AVAILABLE
REQUIRED_COMPUTATION_INTERFACE_UNAVAILABLE
REQUIRED_COMPUTATION_INTERFACE_CONFLICTING
REQUIRED_COMPUTATION_INTERFACE_UNDERDETERMINED
REQUIRED_COMPUTATION_INTERFACE_OUT_OF_SCOPE
~~~

Binding consequences:

~~~text
UNAVAILABLE -> BLOCKED

CONFLICTING -> CONFLICTING
when claim-relevant and unresolved

UNDERDETERMINED -> UNDERDETERMINED
when admissible alternatives alter the requested claim

OUT_OF_SCOPE -> OUT_OF_SCOPE
for the dependent claim
~~~

Required guards:

~~~text
UNAVAILABLE_REQUIRED_INTERFACE != BRANCH_IRRELEVANCE
MISSING_DEPENDENCY_RECORD != NEGATIVE_DEPENDENCY
BLOCKED != SOUNDLY_OMITTED
BLOCKED != NOT_ESTABLISHED
~~~

### G7 — target-relevance / semantic-obligation gate

Every claim-relevant semantic obligation receives:

~~~text
COMPUTATION_OBLIGATION_ID
OBLIGATION_TARGET_SCOPE
OBLIGATION_RESULT_OR_UNIT
COMPUTATION_OBLIGATION_STATUS
OBLIGATION_JUSTIFICATION
OBLIGATION_PROVENANCE
~~~

Status family:

~~~text
REQUIRED_FOR_TARGET
NOT_REQUIRED_FOR_TARGET
OBLIGATION_BLOCKED
OBLIGATION_CONFLICTING
OBLIGATION_UNDERDETERMINED
OBLIGATION_OUT_OF_SCOPE
~~~

Target irrelevance may be established only through a frozen applicable justification such as:

~~~text
dependency closure
zero-sensitivity or derivative theorem
support separation
exact equivalence
symmetry or invariance
algebraic cancellation with required source side conditions
finite-propagation exclusion
declared tolerance or error bound
domain-specific theorem
~~~

Required guards:

~~~text
OMITTED != PROVED_IRRELEVANT
NO_DIRECT_EDGE != NO_INDIRECT_INFLUENCE
CURRENTLY_ZERO != ALWAYS_IRRELEVANT
AGGREGATE_INVISIBLE != COMPONENT_IRRELEVANT
~~~

### G8 — execution-action gate

Every required or considered obligation receives an execution action.

Required record:

~~~text
COMPUTATION_ACTION_ID
COMPUTATION_OBLIGATION_ID
COMPUTATION_EXECUTION_ACTION
ACTION_VALIDITY_SCOPE
ACTION_JUSTIFICATION
ACTION_PROVENANCE
~~~

Action family:

~~~text
EVALUATE_FRESH
REUSE_VALID_RESULT
SYMBOLICALLY_DISCHARGE
OMIT_AS_TARGET_IRRELEVANT
ACTION_BLOCKED
ACTION_CONFLICTING
ACTION_UNDERDETERMINED
ACTION_OUT_OF_SCOPE
~~~

Binding compatibility:

~~~text
REQUIRED_FOR_TARGET:
  may use EVALUATE_FRESH
  may use REUSE_VALID_RESULT
  may use SYMBOLICALLY_DISCHARGE
  may not use OMIT_AS_TARGET_IRRELEVANT

NOT_REQUIRED_FOR_TARGET:
  may use OMIT_AS_TARGET_IRRELEVANT
~~~

Required guards:

~~~text
REQUIRED_RESULT != FRESH_EVALUATION_REQUIRED
REUSE != TARGET_IRRELEVANCE
SYMBOLIC_DISCHARGE != NON_EVALUATION_BY_DEFAULT
EXTRA_EVALUATION != TARGET_NECESSITY
~~~

### G9 — omission-rule / soundness-obligation gate

A sound omission requires:

~~~text
OMISSION_RULE_ID
OMISSION_RULE_VERSION
OMISSION_VALIDITY_SCOPE

OMITTED_UNIT_ID
OMISSION_JUSTIFICATION
TARGET_SCOPE
DEPENDENCY_CLOSURE_STATUS
ERROR_OR_EQUIVALENCE_BOUND
INVALIDATION_CONDITIONS
~~~

Every omission, reuse, approximation, symbolic discharge, or locality shortcut creates a soundness-obligation record:

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

No shortcut is validated merely because a previous execution happened to succeed.

### G10 — reuse coherence / equivalence / invalidation gate

Freeze:

~~~text
REUSE_INTERFACE_ID
REUSE_INTERFACE_VERSION
REUSE_INTERFACE_SCOPE
REUSE_INTERFACE_COHERENCE_STATUS
REUSE_PRECEDENCE_RULE_OR_NONE
REUSE_INVALIDATION_EVALUATION_MODE
REUSE_INTERFACE_PROVENANCE

REUSE_CLASS_ID
REUSE_EQUIVALENCE
REUSE_KEY
REUSE_INPUT_SCOPE
REUSE_OUTPUT_SCOPE
REUSE_VALIDITY_SCOPE
REUSE_INVALIDATION_RULE

SOURCE_MODEL_VERSION
STATUS_LOCK
REGIME_LOCK
TRANSITION_LOCK_IF_RELEVANT
~~~

Reuse-interface statuses:

~~~text
REUSE_INTERFACE_CONSISTENT
REUSE_INTERFACE_CONFLICTING
REUSE_INTERFACE_UNDERDETERMINED
REUSE_INTERFACE_BLOCKED
REUSE_INTERFACE_OUT_OF_SCOPE
~~~

Reuse-result statuses:

~~~text
REUSE_ESTABLISHED_ON_DECLARED_SCOPE
REUSE_NOT_ESTABLISHED
REUSE_BLOCKED
REUSE_CONFLICTING
REUSE_UNDERDETERMINED
REUSE_OUT_OF_SCOPE
~~~

Required guards:

~~~text
CACHE_HIT != SEMANTIC_REUSE_VALIDITY
STALE_REUSE_RECORD != CURRENT_VALID_REUSE
SAME_LABEL_OR_SHAPE != REUSABLE_SUBCOMPUTATION
SAME_AGGREGATE_OUTPUT != REUSE_EQUIVALENCE
SAME_VALUE != VALID_REUSE
EQUAL_CURRENT_VALUE != EQUAL_FUTURE_COMPUTATION
REUSE_ON_VERSION_V != REUSE_ON_VERSION_V_PLUS_1
REGULAR_EPOCH_REUSE != CROSS_TRANSITION_REUSE
~~~

### G11 — information-loss / aggregation / compression handoff gate

If omission or reuse consumes an aggregate, compressed representation, projection, or reduced readout, freeze:

~~~text
READOUT_OR_REDUCTION_ID
VERSION
COLLISION_STATUS
INJECTIVITY_SCOPE
SUPPORT_RETENTION_STATUS
RECONSTRUCTION_SCOPE_IF_RELEVANT
REQUIRED_SIDECARS
~~~

Required guards:

~~~text
OUTPUT_EQUALITY != SOURCE_EQUIVALENCE
AGGREGATE_EQUALITY != CACHE_EQUIVALENCE
EQUAL_REDUCED_READOUT != EQUAL_COMPONENT_STATE
LOSSLESS_ON_DECLARED_CLASS != GLOBAL_EQUIVALENCE
~~~

Aggregation/Compression may supply sidecars.

Their forward operations are not silently reclassified as Computation.

### G12 — resolution / approximation / end-to-end error gate

When claim-relevant, freeze:

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

Resolution status family:

~~~text
RESOLUTION_SUFFICIENT_FOR_DECLARED_TARGET
RESOLUTION_NOT_SUFFICIENT
RESOLUTION_ASSESSMENT_BLOCKED
RESOLUTION_ASSESSMENT_CONFLICTING
RESOLUTION_ASSESSMENT_UNDERDETERMINED
RESOLUTION_ASSESSMENT_OUT_OF_SCOPE
~~~

Required guards:

~~~text
LOWER_RESOLUTION != SAFE_COMPUTATION
SMALL_LOCAL_ERROR != BOUNDED_END_TO_END_ERROR
COMPONENTWISE_TOLERANCE != RELATIONAL_TARGET_PRESERVATION
NUMERIC_CONVERGENCE != SEMANTIC_TARGET_EQUIVALENCE
~~~

### G13 — finite / countable / recursive closure gate

Freeze:

~~~text
EVALUATION_CARDINALITY_MODE

FINITE_FAMILY
COUNTABLE_FAMILY
OTHER_SYMBOLIC_FAMILY

COMPUTATION_CLOSURE_INTERFACE_ID
COMPUTATION_CLOSURE_INTERFACE_VERSION
COMPUTATION_CLOSURE_KIND
COMPUTATION_CLOSURE_STATUS
ORDER_DEPENDENCE_STATUS
TERMINATION_OR_CONVERGENCE_PROVENANCE
CLOSURE_VALIDITY_SCOPE
~~~

Closure kinds:

~~~text
FINITE_TERMINATION
COUNTABLE_CONVERGENCE
RECURSION_WELL_FOUNDEDNESS
FIXED_POINT
EXTERNALLY_SUPPLIED_CLOSURE
~~~

Closure statuses:

~~~text
CLOSURE_ESTABLISHED
CLOSURE_NOT_ESTABLISHED
CLOSURE_BLOCKED
CLOSURE_CONFLICTING
CLOSURE_UNDERDETERMINED
CLOSURE_OUT_OF_SCOPE
~~~

Required guards:

~~~text
FINITE_CORRECTNESS != COUNTABLE_CORRECTNESS
FINITE_DAG_TERMINATION != GENERAL_RECURSIVE_TERMINATION
ONE_FIXED_POINT_FOUND != UNIQUE_FIXED_POINT
CONVERGENCE_UNDER_ONE_ORDER != ORDER_INDEPENDENCE
~~~

The Protocol does not manufacture convergence, termination, well-foundedness, fixed-point existence, or fixed-point uniqueness.

### G14 — symbolic evaluation coverage gate

Freeze:

~~~text
EVALUATION_COVERAGE_SCOPE
EVALUATION_COVERAGE_STATUS
COVERED_SUBCLASS_OR_RELATION
UNCOVERED_OR_UNRESOLVED_SUBCLASS
COVERAGE_PROVENANCE
COVERAGE_VALIDITY_SCOPE
~~~

Coverage statuses:

~~~text
COVERAGE_COMPLETE_FOR_DECLARED_CLAIM
COVERAGE_PARTIAL
COVERAGE_BLOCKED
COVERAGE_CONFLICTING
COVERAGE_UNDERDETERMINED
COVERAGE_OUT_OF_SCOPE
~~~

A symbolic evaluator may discharge a non-enumerated class only to the extent that its frozen applicability domain covers the required claim scope.

Required guards:

~~~text
SYMBOLIC_RULE_FOUND != FULL_CLASS_COVERAGE
CLASS_DEFINITION_COMPLETE != EVALUATION_COVERAGE_COMPLETE
PARAMETRIC_CLASS != UNEVALUATED_CLASS
PARTIAL_THEOREM_DOMAIN != GLOBAL_OMISSION_LICENSE
~~~

### G15 — dynamic / transition / locality / propagation gate

If dynamic locality or cross-time reuse is claim-relevant, freeze:

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

Required guards:

~~~text
STATIC_DEPENDENCY != DYNAMIC_CAUSAL_DEPENDENCY
FINITE_PROPAGATION_SPECIALIZATION != UNIVERSAL_DSD_PROPAGATION
PROPAGATION_BOUND != COMPUTATION_COST_BOUND
OUTSIDE_CURRENT_CONE != PERMANENT_IRRELEVANCE
REGULAR_EPOCH_REUSE != CROSS_TRANSITION_REUSE
RANK_OR_DIMENSION_LABEL != UNIVERSAL_COMPLEXITY_BOUND
FORMATION_STAGE_ORDER != RUNTIME_SCHEDULE
FIRST_BRANCH != AUTOMATIC_EXECUTION_CUTOFF
~~~

### G16 — neighboring-method non-substitution / Optimization handoff gate

Computation may consume sidecars from neighboring methods, but does not collapse into them.

Required guards:

~~~text
ANALYSIS_DECOMPOSITION != COMPUTATION_PLAN
AGGREGATION_OUTPUT != COMPUTATION_PLAN
COMPRESSION_REDUCTION != COMPUTATION_OMISSION
MEASUREMENT_RESOLUTION != COMPUTATION_RESOLUTION_DECISION
SIMULATION_EXECUTION != COMPUTATION_PLAN
PREDICTION_CLAIM != COMPUTATION_RESULT_BY_DEFAULT
TRANSFORMATION_RESULT != REUSE_VALIDITY
AUDIT_PASS != COMPUTATION_PLAN
TRACKING_OR_LINEAGE_HANDOFF != COMPUTATION_EXECUTION
SUFFICIENT_COMPUTATION_PLAN != OPTIMAL_PLAN
COMPUTATION != OPTIMIZATION
COMPUTATION_PLAN != SIMULATION_EXECUTION
SOUNDNESS_AUDIT != COMPUTATION_PLAN
~~~

If an objective-function choice among sufficient plans is requested, emit an Optimization handoff.

A mathematical proof that one plan is uniquely necessary or inclusion-minimal under frozen necessity constraints may remain a Computation result.

### G17 — method-gain / comparator-fairness gate

Computation validity and gain are independent axes.

Method-gain status family:

~~~text
COMPUTATION_GAIN_ESTABLISHED
COMPUTATION_NO_GAIN
COMPUTATION_GAIN_NOT_TESTED
COMPUTATION_GAIN_BLOCKED
COMPUTATION_GAIN_CONFLICTING
COMPUTATION_GAIN_UNDERDETERMINED
COMPUTATION_GAIN_OUT_OF_SCOPE
~~~

When a gain claim is tested, freeze:

~~~text
GAIN_METRIC_SCOPE
GAIN_METRIC_ID
GAIN_BASELINE_ID
GAIN_EVIDENCE_PROVENANCE
GAIN_INPUT_FAMILY
GAIN_ERROR_OR_TOLERANCE_SCOPE
GAIN_ENVIRONMENT_IF_EMPIRICAL

COMPARATOR_ID
COMPARATOR_VERSION
COMPARATOR_TARGET_EQUIVALENCE
COMPARATOR_INFORMATION_ACCESS
COMPARATOR_INPUT_FAMILY
COMPARATOR_ERROR_OR_TOLERANCE
COMPARATOR_HARDWARE_ENVIRONMENT
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
COMPUTATION_ESTABLISHED may coexist with COMPUTATION_NO_GAIN
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
SOUND_PRUNING != COMPLEXITY_IMPROVEMENT
FEWER_EVALUATIONS != LOWER_WALL_CLOCK_TIME
CHANGED_TARGET_SPEEDUP != METHOD_GAIN
HIDDEN_INFORMATION_ADVANTAGE != METHOD_GAIN
DIFFERENT_TOLERANCE != FAIR_SPEEDUP
UNCONTROLLED_ENVIRONMENT_DIFFERENCE != ALGORITHMIC_GAIN
COMPARATOR_NOT_FAIR != COMPUTATION_METHOD_FAILURE
~~~

### G18 — primary status / task terminal / conformance / maximum-claim gate

Assign one primary Computation status:

~~~text
COMPUTATION_ESTABLISHED
COMPUTATION_NOT_ESTABLISHED
COMPUTATION_BLOCKED
COMPUTATION_CONFLICTING
COMPUTATION_OUT_OF_SCOPE
COMPUTATION_UNDERDETERMINED
~~~

Assign exactly one task terminal:

~~~text
COMPUTATION_TASK_ESTABLISHED
COMPUTATION_TASK_PARTIAL
COMPUTATION_TASK_NOT_ESTABLISHED
COMPUTATION_TASK_BLOCKED
COMPUTATION_TASK_CONFLICTING
COMPUTATION_TASK_OUT_OF_SCOPE
COMPUTATION_TASK_UNDERDETERMINED
~~~

Frozen precedence:

~~~text
COMPUTATION_TASK_OUT_OF_SCOPE
>
COMPUTATION_TASK_CONFLICTING
>
COMPUTATION_TASK_UNDERDETERMINED
>
COMPUTATION_TASK_BLOCKED
>
COMPUTATION_TASK_ESTABLISHED /
COMPUTATION_TASK_PARTIAL /
COMPUTATION_TASK_NOT_ESTABLISHED
~~~

PARTIAL is permitted only when:

~~~text
1. multiple independently required in-scope obligations exist

2. at least one required obligation is ESTABLISHED

3. at least one other independently required obligation
   is evaluably NOT_ESTABLISHED

4. no required obligation is BLOCKED

5. no higher-priority OUT_OF_SCOPE / CONFLICTING /
   UNDERDETERMINED condition applies
~~~

Required guards:

~~~text
PARTIAL != BLOCKED_WITH_SOME_SUCCESS
PARTIAL != ATOMIC_FAILURE_RELABELED
COMPUTATION_NO_GAIN != COMPUTATION_TASK_PARTIAL_BY_DEFAULT
~~~

Then emit protocol conformance, method-gain status, and maximum-supported claim.

## 5. Binding operation T1-T18

### T1 — freeze task / target / primary claim

Instantiate G1.

### T2 — freeze source / model / interface versions

Instantiate G2.

### T3 — freeze evaluation class / representation / mode / completeness

Instantiate G3.

### T4 — build typed status / applicability / channel ledger

Instantiate G4.

### T5 — freeze dependency and bridge interfaces

Instantiate G5.

### T6 — evaluate required-interface availability / coherence

Instantiate G6.

Do not infer irrelevance from an unavailable interface.

### T7 — assign semantic-obligation necessity

Instantiate G7.

Determine target-relative required versus not-required obligations before choosing how to execute them.

### T8 — assign execution actions

Instantiate G8.

Keep semantic necessity separate from fresh evaluation, reuse, symbolic discharge, or omission.

### T9 — register omission rules and soundness obligations

Instantiate G9.

No omission/reuse/approximation/symbolic/locality shortcut proceeds without its obligation ledger.

### T10 — evaluate reuse coherence / validity / invalidation

Instantiate G10.

Apply version, status, regime, transition, and precedence locks before any reuse action.

### T11 — evaluate information-loss / reduction handoffs

Instantiate G11.

Do not use aggregate/readout equality as source equivalence unless the frozen target and supplied sidecars justify it.

### T12 — evaluate resolution / approximation / end-to-end error

Instantiate G12.

### T13 — evaluate finite / countable / recursive closure

Instantiate G13.

### T14 — evaluate symbolic class coverage

Instantiate G14.

### T15 — evaluate dynamic / transition / locality / propagation obligations

Instantiate G15.

### T16 — apply neighboring-method non-substitution and Optimization handoff rules

Instantiate G16.

### T17 — evaluate method gain and comparator fairness when requested

Instantiate G17.

If gain is not requested:

~~~text
COMPUTATION_GAIN_NOT_TESTED
~~~

is allowed.

### T18 — assemble plan and assign status / terminal / conformance / maximum claim

Instantiate G18.

Emit all required ledgers and preserve subordinate statuses beneath the task terminal.

## 6. Required-interface statuses

~~~text
REQUIRED_COMPUTATION_INTERFACE_AVAILABLE
REQUIRED_COMPUTATION_INTERFACE_UNAVAILABLE
REQUIRED_COMPUTATION_INTERFACE_CONFLICTING
REQUIRED_COMPUTATION_INTERFACE_UNDERDETERMINED
REQUIRED_COMPUTATION_INTERFACE_OUT_OF_SCOPE
~~~

## 7. Obligation statuses

~~~text
REQUIRED_FOR_TARGET
NOT_REQUIRED_FOR_TARGET
OBLIGATION_BLOCKED
OBLIGATION_CONFLICTING
OBLIGATION_UNDERDETERMINED
OBLIGATION_OUT_OF_SCOPE
~~~

## 8. Execution actions

~~~text
EVALUATE_FRESH
REUSE_VALID_RESULT
SYMBOLICALLY_DISCHARGE
OMIT_AS_TARGET_IRRELEVANT
ACTION_BLOCKED
ACTION_CONFLICTING
ACTION_UNDERDETERMINED
ACTION_OUT_OF_SCOPE
~~~

## 9. Reuse-interface and reuse-result statuses

Reuse-interface:

~~~text
REUSE_INTERFACE_CONSISTENT
REUSE_INTERFACE_CONFLICTING
REUSE_INTERFACE_UNDERDETERMINED
REUSE_INTERFACE_BLOCKED
REUSE_INTERFACE_OUT_OF_SCOPE
~~~

Reuse result:

~~~text
REUSE_ESTABLISHED_ON_DECLARED_SCOPE
REUSE_NOT_ESTABLISHED
REUSE_BLOCKED
REUSE_CONFLICTING
REUSE_UNDERDETERMINED
REUSE_OUT_OF_SCOPE
~~~

## 10. Resolution statuses

~~~text
RESOLUTION_SUFFICIENT_FOR_DECLARED_TARGET
RESOLUTION_NOT_SUFFICIENT
RESOLUTION_ASSESSMENT_BLOCKED
RESOLUTION_ASSESSMENT_CONFLICTING
RESOLUTION_ASSESSMENT_UNDERDETERMINED
RESOLUTION_ASSESSMENT_OUT_OF_SCOPE
~~~

## 11. Closure statuses

~~~text
CLOSURE_ESTABLISHED
CLOSURE_NOT_ESTABLISHED
CLOSURE_BLOCKED
CLOSURE_CONFLICTING
CLOSURE_UNDERDETERMINED
CLOSURE_OUT_OF_SCOPE
~~~

## 12. Evaluation-coverage statuses

~~~text
COVERAGE_COMPLETE_FOR_DECLARED_CLAIM
COVERAGE_PARTIAL
COVERAGE_BLOCKED
COVERAGE_CONFLICTING
COVERAGE_UNDERDETERMINED
COVERAGE_OUT_OF_SCOPE
~~~

## 13. Soundness-obligation statuses

~~~text
SOUNDNESS_OBLIGATION_ESTABLISHED
SOUNDNESS_OBLIGATION_NOT_ESTABLISHED
SOUNDNESS_OBLIGATION_BLOCKED
SOUNDNESS_OBLIGATION_CONFLICTING
SOUNDNESS_OBLIGATION_UNDERDETERMINED
SOUNDNESS_OBLIGATION_OUT_OF_SCOPE
~~~

These are protocol-level normalized aliases for the obligation-ledger status family.

## 14. Computation-set outcomes

~~~text
COMPUTATION_SET_FULLY_PLANNED
COMPUTATION_SET_PARTIALLY_PLANNED
COMPUTATION_SET_BLOCKED
COMPUTATION_SET_CONFLICTING
COMPUTATION_SET_UNDERDETERMINED
COMPUTATION_SET_OUT_OF_SCOPE
~~~

Convenience sets may include:

~~~text
REQUIRED_RESULT_OR_OBLIGATION_SET
FRESH_EVALUATION_SET
REUSED_RESULT_SET
SYMBOLICALLY_DISCHARGED_SET
SOUNDLY_OMITTED_SET
BLOCKED_SET
CONFLICTING_SET
UNDERDETERMINED_SET
OUT_OF_SCOPE_SET
~~~

Required guards:

~~~text
FULLY_PLANNED may include sound omissions
FULLY_PLANNED may include valid reuse
REQUIRED_RESULT may be absent from FRESH_EVALUATION_SET
when discharged by valid reuse or symbolic evaluation
~~~

## 15. Primary Computation statuses

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
  the frozen requested Computation claim is supported

NOT_ESTABLISHED:
  all required claim interfaces are evaluable
  but the requested claim fails

BLOCKED:
  one or more required in-scope interfaces /
  dependencies / proof obligations are unavailable

CONFLICTING:
  mutually incompatible applicable claim-relevant
  records remain unresolved

OUT_OF_SCOPE:
  the requested operation / claim lies outside
  the frozen Computation task

UNDERDETERMINED:
  multiple admissible claim-relevant semantics
  remain and produce different outcomes
~~~

## 16. Task terminals

~~~text
COMPUTATION_TASK_ESTABLISHED
COMPUTATION_TASK_PARTIAL
COMPUTATION_TASK_NOT_ESTABLISHED
COMPUTATION_TASK_BLOCKED
COMPUTATION_TASK_CONFLICTING
COMPUTATION_TASK_OUT_OF_SCOPE
COMPUTATION_TASK_UNDERDETERMINED
~~~

Frozen precedence:

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

Lower-level statuses remain visible beneath the task terminal.

## 17. Protocol conformance

~~~text
COMPUTATION_PROTOCOL_CONFORMANT
COMPUTATION_PROTOCOL_NONCONFORMANT
COMPUTATION_PROTOCOL_INDETERMINATE
~~~

A negative, blocked, conflicting, underdetermined, or out-of-scope task result may still be protocol-conformant.

Protocol conformance concerns whether the frozen protocol was followed, not whether the task claim was positive.

## 18. Method-gain and comparator-fairness statuses

Method gain:

~~~text
COMPUTATION_GAIN_ESTABLISHED
COMPUTATION_NO_GAIN
COMPUTATION_GAIN_NOT_TESTED
COMPUTATION_GAIN_BLOCKED
COMPUTATION_GAIN_CONFLICTING
COMPUTATION_GAIN_UNDERDETERMINED
COMPUTATION_GAIN_OUT_OF_SCOPE
~~~

Comparator fairness:

~~~text
COMPARATOR_FAIR
COMPARATOR_NOT_FAIR
COMPARATOR_BLOCKED
COMPARATOR_CONFLICTING
COMPARATOR_UNDERDETERMINED
COMPARATOR_OUT_OF_SCOPE
~~~

Method gain never replaces the primary Computation status.

## 19. Required output schema

Every executable record must emit, as applicable:

~~~text
TASK_LOCK

TARGET_AND_EQUIVALENCE_LOCK
SOURCE_MODEL_INTERFACE_LOCK

EVALUATION_CLASS_LOCK
EVALUATION_COVERAGE_LEDGER

STATUS_AND_APPLICABILITY_LEDGER
CHANNEL_BRANCH_REGISTRY

DEPENDENCY_AND_BRIDGE_REGISTER
REQUIRED_INTERFACE_LEDGER

SEMANTIC_OBLIGATION_LEDGER
EXECUTION_ACTION_LEDGER

OMISSION_RULE_LEDGER
SOUNDNESS_OBLIGATION_LEDGER

REUSE_INTERFACE_LEDGER
REUSE_VALIDITY_LEDGER

INFORMATION_LOSS_HANDOFF_LEDGER

RESOLUTION_APPROXIMATION_ERROR_LEDGER

CLOSURE_TERMINATION_CONVERGENCE_LEDGER

DYNAMIC_TRANSITION_LOCALITY_LEDGER_IF_USED

REQUIRED_RESULT_OR_OBLIGATION_SET
FRESH_EVALUATION_SET
REUSED_RESULT_SET
SYMBOLICALLY_DISCHARGED_SET
SOUNDLY_OMITTED_SET
BLOCKED_SET
CONFLICTING_SET
UNDERDETERMINED_SET
OUT_OF_SCOPE_SET

COMPUTATION_SET_OUTCOME
COMPUTATION_PLAN

COST_COMPLEXITY_EVIDENCE_LEDGER
COMPARATOR_FAIRNESS_LEDGER_IF_GAIN_TESTED
OPTIMIZATION_HANDOFF_IF_ANY

COMPUTATION_PRIMARY_STATUS
COMPUTATION_TASK_TERMINAL

COMPUTATION_PROTOCOL_CONFORMANCE
COMPUTATION_METHOD_GAIN_STATUS

MAXIMUM_SUPPORTED_CLAIM
~~~

Every claim-relevant optional ledger must be explicitly marked:

~~~text
NOT_APPLICABLE
NOT_REQUESTED
BLOCKED
or
populated
~~~

rather than silently omitted.

## 20. Five-interface identity

~~~text
INPUTS:
  declared computational target / equivalence / tolerance
  frozen source/model/interface
  evaluation class / branches / channels
  typed statuses / applicability
  explicit dependency / bridge interfaces
  optional reduction / transition / locality /
  resolution / reuse / comparator handoffs

OPERATION:
  determine target-relative semantic obligations;
  assign execution actions;
  justify sound omissions;
  validate scoped reuse;
  discharge symbolic classes only over proven coverage;
  preserve blocked/conflicting/underdetermined interfaces;
  validate resolution, closure, approximation,
  locality, and soundness obligations;
  assemble bounded computation plan

OUTPUTS:
  semantic-obligation ledger
  execution-action ledger
  required / fresh / reused / symbolic / omitted /
  blocked / conflicting / unresolved sets
  bounded computation plan
  soundness ledger
  resolution/error ledger
  closure/coverage ledger
  separate gain/comparator ledger
  optional Optimization handoff

FAILURE_OR_NO_GAIN:
  unsound omission
  invalid reuse
  missing required dependency/interface
  unresolved conflicting semantics
  unsupported closure/resolution/coverage
  hidden neighboring-method substitution
  fair-baseline NO_GAIN

VALIDATION_STANDARD:
  every shortcut follows from frozen target,
  dependency, interface, status, validity,
  coverage, closure, resolution, and transition semantics;
  source-level distinctions and information-loss limits are preserved;
  soundness and performance claims remain separate;
  no objective-based Optimization is smuggled into Computation
~~~

## 21. Core semantic guards

~~~text
NOT_ADMITTED != ZERO_CONTRIBUTION

INAPPLICABLE != COMPUTED_ZERO

PREREQUISITE_UNSATISFIED != FALSE_NUMERICAL_OUTPUT

APPLICABLE_BUT_UNDEFINED != FALSE_RESULT

ONE_FAILED_BRANCH != GLOBAL_PRUNING_LICENSE

OUTPUT_EQUALITY != SOURCE_EQUIVALENCE

AGGREGATE_EQUALITY != CACHE_EQUIVALENCE

SAME_LABEL_OR_SHAPE != REUSABLE_SUBCOMPUTATION

OMITTED != PROVED_IRRELEVANT

REQUIRED_RESULT != FRESH_EVALUATION_REQUIRED

REUSE != TARGET_IRRELEVANCE

CACHE_HIT != SEMANTIC_REUSE_VALIDITY

STATIC_DEPENDENCY != DYNAMIC_CAUSAL_DEPENDENCY

FORMATION_STAGE_ORDER != RUNTIME_SCHEDULE

FIRST_BRANCH != AUTOMATIC_EXECUTION_CUTOFF

FINITE_PROPAGATION_BOUND != UNIVERSAL_DSD_PRUNING_RULE

LOWER_RESOLUTION != SAFE_COMPUTATION

SMALL_LOCAL_ERROR != BOUNDED_END_TO_END_ERROR

FINITE_CORRECTNESS != COUNTABLE_CORRECTNESS

FINITE_DAG_TERMINATION != GENERAL_RECURSIVE_TERMINATION

SYMBOLIC_RULE_FOUND != FULL_CLASS_COVERAGE

CLASS_DEFINITION_COMPLETE != EVALUATION_COVERAGE_COMPLETE

SOUND_PRUNING != COMPLEXITY_IMPROVEMENT

FEWER_EVALUATIONS != LOWER_WALL_CLOCK_TIME

CHANGED_TARGET_SPEEDUP != METHOD_GAIN

HIDDEN_INFORMATION_ADVANTAGE != METHOD_GAIN

COMPUTATION != OPTIMIZATION

COMPUTATION_PLAN != SIMULATION_EXECUTION

SOUNDNESS_AUDIT != COMPUTATION_PLAN

PARTIAL != BLOCKED_WITH_SOME_SUCCESS

COMPUTATION_NO_GAIN != COMPUTATION_TASK_PARTIAL_BY_DEFAULT

NO_GAIN != METHOD_FAILURE
~~~

## 22. Protocol integrity rules

~~~text
historical Task Interface:
  immutable

historical boundary attack:
  immutable

Boundary Amendment 001:
  prospective binding source

Protocol v0.1:
  frozen executable standard for subsequent
  internal constructed challenges

post-freeze core correction:
  requires explicit protocol revision artifact

challenge failure:
  must be preserved

NO_GAIN:
  must be preserved

blocked/conflicting/underdetermined result:
  must not be rewritten into success or ordinary failure

same-project retrace:
  must not be called independent replication

internal standardization:
  must not be called external validation
~~~

Protocol freeze does not increment direct challenge counters.

## 23. Maximum-supported claim rule

A conformant Computation result may assert only what follows from the frozen:

~~~text
target
equivalence / tolerance
source/model/interface version
evaluation class
typed status/applicability
dependency and bridge interface
semantic-obligation status
execution action
omission justification
reuse validity
coverage
closure / convergence / termination
resolution / error semantics
dynamic / transition / locality assumptions
soundness obligations
comparator fairness if gain is claimed
~~~

Not automatically allowed:

~~~text
global irrelevance from target-relative irrelevance

global source equivalence from equal output

permanent reuse from one version/regime

whole-class omission from subclass coverage

general recursive termination from finite-DAG termination

universal locality from one finite-propagation specialization

global minimality from sufficiency

optimality from a sufficient plan

lower runtime from fewer evaluation units

universal complexity improvement from one empirical speedup

external validity

independent validation

independent replication

method superiority

permanent method irreducibility
~~~

## 24. Current protocol state

~~~text
DEDICATED_COMPUTATION_PROTOCOL:
  established v0.1

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  T1-T18

SOURCE_REGISTRY_RECOVERY:
  complete

TASK_INTERFACE_DRAFT:
  v0.1 historical draft preserved

PRE_PROTOCOL_BOUNDARY_ATTACKS:
  18

PRESERVED_NO_REFINEMENT:
  11

PRESERVED_WITH_NONBREAKING_REFINEMENT:
  7

BOUNDARY_AMENDMENT_001:
  established

REFINEMENT_GROUPS_ADOPTED:
  7/7

PROTOCOL_FREEZE_AUTHORIZED:
  yes

DIRECT_COMPUTATION_PILOTS_ATTEMPTED:
  0

SUCCESSFUL_DIRECT_COMPUTATION_PILOTS:
  0

POSITIVE_COMPUTATION_CASES:
  0

NEGATIVE_OR_UNRESOLVED_COMPUTATION_CASES:
  0

METHOD_BOUNDARY_COMPUTATION_CASES:
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
  protocol_frozen

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 25. Interpretation lock

~~~text
PROTOCOL_FROZEN
  !=
INTERNALLY_STANDARDIZED

PROTOCOL_CONFORMANT_RESULT
  !=
POSITIVE_RESULT

COMPUTATION_ESTABLISHED
  !=
COMPUTATIONAL_GAIN

COMPUTATION_NO_GAIN
  !=
METHOD_FAILURE

FIXTURE_BOUNDED_BOUNDARY_SURVIVAL
  !=
PERMANENT_METHOD_IRREDUCIBILITY

INTERNAL_CONSTRUCTED_EVIDENCE
  !=
EXTERNAL_VALIDATION
~~~

## 26. Next

Prospectively precommit and execute the first positive constructed Computation challenge.

The first challenge should directly exercise, in one bounded fixture pack where feasible:

~~~text
required-result versus fresh-evaluation separation
valid reuse
sound target-relative omission
symbolic discharge with complete coverage
resolution sufficiency
a simple closure / termination obligation
an information-loss guard
and Computation / Optimization non-substitution
~~~

Do not rewrite this protocol in response to the first challenge.
