# DSD Computation Task Interface Boundary Amendment 001

Status: **PROSPECTIVE AMENDMENT ESTABLISHED**  
Date: **2026-10-03**  
Method: **Computation / DSD 계산론**  
Legacy path ID: `12A`  
Higher field: **VII. Computation & Selection / 계산·선택**

Frozen historical basis:

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
~~~

The historical Task Interface and boundary-attack record are not rewritten.

This Amendment prospectively binds the seven nonbreaking refinements forced by the 18 pre-protocol boundary attacks.

## 1. Amendment result

~~~text
BOUNDARY_AMENDMENT_001:
  established

REFINEMENT_GROUPS_ADOPTED:
  7/7

METHOD_IDENTITY_CHANGED:
  no

TASK_INTERFACE_CORE_REOPENED:
  no

HISTORICAL_TASK_INTERFACE_REWRITTEN:
  no

HISTORICAL_BOUNDARY_ATTACK_RECORD_REWRITTEN:
  no

BOUNDARY_COLLAPSE_FOUND:
  0

FUNDAMENTAL_INTERFACE_FAILURE:
  0

PROTOCOL_FREEZE_AUTHORIZED:
  yes

DIRECT_COMPUTATION_PILOTS_ATTEMPTED:
  0

EXTERNAL_APPLICATION:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 2. R1 — semantic necessity versus execution action

Protocol v0.1 must separate:

~~~text
whether a semantic result / obligation is required for the target
from
how that obligation is discharged in the execution plan
~~~

Required obligation record:

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

Required execution-action record:

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
REQUIRED_FOR_TARGET
  may be discharged by:
    EVALUATE_FRESH
    REUSE_VALID_RESULT
    SYMBOLICALLY_DISCHARGE

REQUIRED_FOR_TARGET
  may not be justified by:
    OMIT_AS_TARGET_IRRELEVANT

NOT_REQUIRED_FOR_TARGET
  may support:
    OMIT_AS_TARGET_IRRELEVANT
~~~

A plan may still evaluate a non-required unit for engineering convenience, but such extra evaluation is not evidence that the unit was target-required.

Required guards:

~~~text
REQUIRED_RESULT
  !=
FRESH_EVALUATION_REQUIRED

REUSE
  !=
TARGET_IRRELEVANCE

SYMBOLIC_DISCHARGE
  !=
NON_EVALUATION_BY_DEFAULT

EXTRA_EVALUATION
  !=
TARGET_NECESSITY
~~~

The future protocol may emit convenience sets such as required, fresh-evaluated, reused, symbolically discharged, and omitted units.

Those convenience sets must be derivable from the two-axis obligation/action ledger and must not collapse the axes.

## 3. R2 — reuse-interface coherence and invalidation

Before any reuse action is accepted, Protocol v0.1 must evaluate the coherence of the frozen claim-relevant reuse interface.

Required record:

~~~text
REUSE_INTERFACE_ID
REUSE_INTERFACE_VERSION
REUSE_INTERFACE_SCOPE
REUSE_INTERFACE_COHERENCE_STATUS
REUSE_PRECEDENCE_RULE_OR_NONE
REUSE_INVALIDATION_EVALUATION_MODE
REUSE_INTERFACE_PROVENANCE
~~~

Status family:

~~~text
REUSE_INTERFACE_CONSISTENT
REUSE_INTERFACE_CONFLICTING
REUSE_INTERFACE_UNDERDETERMINED
REUSE_INTERFACE_BLOCKED
REUSE_INTERFACE_OUT_OF_SCOPE
~~~

The underlying reuse record must continue to freeze:

~~~text
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

Binding consequences:

~~~text
explicit applicable invalidation:
  defeats a stale generic cache-hit claim

mutually incompatible applicable reuse records
under the same frozen semantics:
  REUSE_INTERFACE_CONFLICTING

multiple admissible reuse semantics
with different execution actions:
  REUSE_INTERFACE_UNDERDETERMINED

required reuse metadata unavailable:
  REUSE_INTERFACE_BLOCKED

requested reuse operation outside the frozen interface:
  REUSE_INTERFACE_OUT_OF_SCOPE
~~~

Reuse action consequences:

~~~text
REUSE_INTERFACE_CONSISTENT
  + reuse validity established
  ->
REUSE_VALID_RESULT may be used

REUSE_INTERFACE_CONFLICTING
  ->
claim-relevant reuse obligation CONFLICTING

REUSE_INTERFACE_UNDERDETERMINED
  ->
claim-relevant reuse obligation UNDERDETERMINED

REUSE_INTERFACE_BLOCKED
  ->
claim-relevant reuse obligation BLOCKED
~~~

Required guards:

~~~text
CACHE_HIT != SEMANTIC_REUSE_VALIDITY

STALE_REUSE_RECORD != CURRENT_VALID_REUSE

SAME_VALUE != VALID_REUSE

REUSE_ON_VERSION_V
  !=
REUSE_ON_VERSION_V_PLUS_1

REGULAR_EPOCH_REUSE
  !=
CROSS_TRANSITION_REUSE
~~~

## 4. R3 — countable / recursive closure interface

If a claim requires countable evaluation, recursion, cyclic dependency resolution, fixed-point semantics, or another nontrivial closure condition, Protocol v0.1 must freeze an explicit closure interface.

Required record:

~~~text
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

Status family:

~~~text
CLOSURE_ESTABLISHED
CLOSURE_NOT_ESTABLISHED
CLOSURE_BLOCKED
CLOSURE_CONFLICTING
CLOSURE_UNDERDETERMINED
CLOSURE_OUT_OF_SCOPE
~~~

Binding consequences:

~~~text
required closure interface unavailable:
  -> BLOCKED

incompatible applicable closure records:
  -> CONFLICTING

multiple admissible order / fixed-point / convergence semantics
that yield different claim-relevant outcomes:
  -> UNDERDETERMINED

closure condition fully evaluable but false:
  -> NOT_ESTABLISHED

closure condition established under the frozen scope:
  -> dependent computation may proceed
~~~

No protocol step may manufacture absolute summability, convergence, well-foundedness, termination, or fixed-point uniqueness.

Required guards:

~~~text
FINITE_CORRECTNESS
  !=
COUNTABLE_CORRECTNESS

FINITE_DAG_TERMINATION
  !=
GENERAL_RECURSIVE_TERMINATION

ONE_FIXED_POINT_FOUND
  !=
UNIQUE_FIXED_POINT

CONVERGENCE_UNDER_ONE_ORDER
  !=
ORDER_INDEPENDENCE
~~~

## 5. R4 — symbolic evaluation coverage

Protocol v0.1 must distinguish:

~~~text
the declared evaluation-class definition/completeness
from
the domain actually covered by the evaluator / theorem / symbolic rule
~~~

Required record:

~~~text
EVALUATION_COVERAGE_SCOPE
EVALUATION_COVERAGE_STATUS
COVERED_SUBCLASS_OR_RELATION
UNCOVERED_OR_UNRESOLVED_SUBCLASS
COVERAGE_PROVENANCE
COVERAGE_VALIDITY_SCOPE
~~~

Status family:

~~~text
COVERAGE_COMPLETE_FOR_DECLARED_CLAIM
COVERAGE_PARTIAL
COVERAGE_BLOCKED
COVERAGE_CONFLICTING
COVERAGE_UNDERDETERMINED
COVERAGE_OUT_OF_SCOPE
~~~

Binding rules:

~~~text
a symbolic / theorem-level evaluator may discharge
a non-enumerated class without literal enumeration

only if:
  its frozen applicability domain covers the whole
  declared claim scope required by that result

COVERAGE_PARTIAL:
  preserves the covered and uncovered subclasses separately

uncovered required region:
  must still receive an executable disposition
  under the frozen task interface

required coverage interface unavailable:
  BLOCKED

several admissible coverage interpretations
that change the claim:
  UNDERDETERMINED

incompatible applicable coverage records:
  CONFLICTING
~~~

Coverage status alone does not automatically determine the final task terminal.

It feeds the required-obligation ledger.

Required guards:

~~~text
SYMBOLIC_RULE_FOUND
  !=
FULL_CLASS_COVERAGE

CLASS_DEFINITION_COMPLETE
  !=
EVALUATION_COVERAGE_COMPLETE

PARAMETRIC_CLASS
  !=
UNEVALUATED_CLASS

PARTIAL_THEOREM_DOMAIN
  !=
GLOBAL_OMISSION_LICENSE
~~~

## 6. R5 — explicit Computation method-gain status

Computation validity and computational gain must remain separate.

Protocol v0.1 must emit:

~~~text
COMPUTATION_METHOD_GAIN_STATUS
~~~

Status family:

~~~text
COMPUTATION_GAIN_ESTABLISHED
COMPUTATION_NO_GAIN
COMPUTATION_GAIN_NOT_TESTED
COMPUTATION_GAIN_BLOCKED
COMPUTATION_GAIN_CONFLICTING
COMPUTATION_GAIN_UNDERDETERMINED
COMPUTATION_GAIN_OUT_OF_SCOPE
~~~

When a gain claim is evaluated, freeze:

~~~text
GAIN_METRIC_SCOPE
GAIN_METRIC_ID
GAIN_BASELINE_ID
GAIN_EVIDENCE_PROVENANCE
GAIN_INPUT_FAMILY
GAIN_ERROR_OR_TOLERANCE_SCOPE
GAIN_ENVIRONMENT_IF_EMPIRICAL
~~~

Binding rules:

~~~text
COMPUTATION_ESTABLISHED
  may coexist with
COMPUTATION_NO_GAIN

COMPUTATION_ESTABLISHED
  may coexist with
COMPUTATION_GAIN_NOT_TESTED

NO_GAIN:
  means the frozen gain claim did not exceed
  the frozen fair baseline under the declared metric

NO_GAIN:
  does not negate soundness of the computation plan
~~~

Required guards:

~~~text
NO_GAIN != METHOD_FAILURE

NO_GAIN != METHOD_DELETION_PROOF

NO_GAIN != METHOD_MERGER_PROOF

NO_GAIN != METHOD_ABSORPTION_PROOF

SOUND_PRUNING != PERFORMANCE_GAIN

FEWER_EVALUATIONS != LOWER_WALL_CLOCK_TIME
~~~

## 7. R6 — comparator fairness

A Computation method-gain claim against a baseline is admissible only after comparator fairness is frozen and evaluated.

Required comparator record:

~~~text
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

Allowed target-equivalence status:

~~~text
TARGET_MATCHED
TARGET_NOT_MATCHED
TARGET_MATCH_BLOCKED
TARGET_MATCH_UNDERDETERMINED
TARGET_MATCH_CONFLICTING
~~~

Allowed information-access status:

~~~text
INFORMATION_ACCESS_EQUAL
INFORMATION_ACCESS_UNEQUAL
INFORMATION_ACCESS_BLOCKED
INFORMATION_ACCESS_UNDERDETERMINED
INFORMATION_ACCESS_CONFLICTING
~~~

Overall comparator-fairness status:

~~~text
COMPARATOR_FAIR
COMPARATOR_NOT_FAIR
COMPARATOR_BLOCKED
COMPARATOR_CONFLICTING
COMPARATOR_UNDERDETERMINED
COMPARATOR_OUT_OF_SCOPE
~~~

Binding consequences:

~~~text
COMPARATOR_FAIR:
  permits the declared gain comparison

COMPARATOR_NOT_FAIR:
  does not permit a method-gain claim from that comparison

COMPARATOR_BLOCKED:
  gain claim BLOCKED

COMPARATOR_CONFLICTING:
  gain claim CONFLICTING

COMPARATOR_UNDERDETERMINED:
  gain claim UNDERDETERMINED

COMPARATOR_OUT_OF_SCOPE:
  gain comparison OUT_OF_SCOPE
~~~

A non-fair comparison does not invalidate the underlying Computation soundness result.

Required guards:

~~~text
CHANGED_TARGET_SPEEDUP
  !=
METHOD_GAIN

HIDDEN_INFORMATION_ADVANTAGE
  !=
METHOD_GAIN

DIFFERENT_TOLERANCE
  !=
FAIR_SPEEDUP

UNCONTROLLED_ENVIRONMENT_DIFFERENCE
  !=
ALGORITHMIC_GAIN

COMPARATOR_NOT_FAIR
  !=
COMPUTATION_METHOD_FAILURE
~~~

## 8. R7 — exact task-terminal precedence and PARTIAL semantics

Computation Protocol v0.1 must emit exactly one task-level terminal:

~~~text
COMPUTATION_TASK_ESTABLISHED

COMPUTATION_TASK_PARTIAL

COMPUTATION_TASK_NOT_ESTABLISHED

COMPUTATION_TASK_BLOCKED

COMPUTATION_TASK_CONFLICTING

COMPUTATION_TASK_OUT_OF_SCOPE

COMPUTATION_TASK_UNDERDETERMINED
~~~

Binding terminal precedence:

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

Semantics:

~~~text
OUT_OF_SCOPE:
  the requested operation, claim level, target, comparator,
  evaluator, closure mode, or required interface lies outside
  the frozen Computation task

CONFLICTING:
  mutually incompatible applicable claim-relevant status,
  dependency, reuse, coverage, closure, resolution, comparator,
  or other frozen interface records exist under the same semantics
  and no frozen resolver applies

UNDERDETERMINED:
  multiple admissible claim-relevant interpretations remain
  and yield different computation dispositions or task outcomes

BLOCKED:
  one or more required in-scope dependency/interface/proof/
  closure/coverage/reuse/comparator records are unavailable,
  preventing completion of a required obligation

ESTABLISHED:
  the requested frozen Computation claim level is supported
  after all required obligations are validly discharged

PARTIAL:
  the frozen task contains multiple independently required
  in-scope Computation obligations;
  at least one obligation is ESTABLISHED;
  at least one other independently required obligation is
  evaluably NOT_ESTABLISHED;
  no required obligation is BLOCKED;
  and no OUT_OF_SCOPE / CONFLICTING / UNDERDETERMINED condition dominates

NOT_ESTABLISHED:
  the requested in-scope claim is evaluable under all required
  interfaces but the requested claim level fails
~~~

PARTIAL may not be used:

~~~text
to rescue one failed atomic claim

to hide a blocked required dependency

to hide a conflict

to hide underdetermined semantics

to combine an out-of-scope obligation
with an in-scope obligation and call the run partly successful

to relabel a gain failure when the primary Computation plan itself
is otherwise established
~~~

The terminal summarizes the task only.

It does not erase:

~~~text
obligation status
execution action
unit disposition
dependency status
required-interface status
reuse-interface status
closure status
coverage status
resolution status
soundness-obligation status
gain status
comparator-fairness status
subordinate obligation results
~~~

Required guards:

~~~text
PARTIAL != BLOCKED_WITH_SOME_SUCCESS

PARTIAL != ATOMIC_FAILURE_RELABELED

COMPUTATION_NO_GAIN
  !=
COMPUTATION_TASK_PARTIAL_BY_DEFAULT
~~~

## 9. Evaluation-set outcome remains separate

Protocol v0.1 may emit convenience sets derived from the obligation/action ledger:

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

The set-level plan outcome remains distinct from the task terminal.

Required set-level outcomes:

~~~text
COMPUTATION_SET_FULLY_PLANNED
COMPUTATION_SET_PARTIALLY_PLANNED
COMPUTATION_SET_BLOCKED
COMPUTATION_SET_CONFLICTING
COMPUTATION_SET_UNDERDETERMINED
COMPUTATION_SET_OUT_OF_SCOPE
~~~

Important:

~~~text
FULLY_PLANNED
  may include many soundly omitted units

FULLY_PLANNED
  may include valid reuse

REQUIRED_RESULT
  may be absent from FRESH_EVALUATION_SET
  when discharged by valid reuse or symbolic evaluation
~~~

## 10. Existing historical guards remain binding

The seven refinements do not weaken the historical Task Interface.

Protocol v0.1 must continue to preserve at least:

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

## 11. Neighboring-method non-substitution remains binding

The boundary attack does not collapse Computation into neighboring methods.

Protocol v0.1 must preserve at least:

~~~text
ANALYSIS_DECOMPOSITION
  !=
COMPUTATION_PLAN

AGGREGATION_OUTPUT
  !=
COMPUTATION_PLAN

COMPRESSION_REDUCTION
  !=
COMPUTATION_OMISSION

MEASUREMENT_RESOLUTION
  !=
COMPUTATION_RESOLUTION_DECISION

SIMULATION_EXECUTION
  !=
COMPUTATION_PLAN

PREDICTION_CLAIM
  !=
COMPUTATION_RESULT_BY_DEFAULT

TRANSFORMATION_RESULT
  !=
REUSE_VALIDITY

AUDIT_PASS
  !=
COMPUTATION_PLAN

TRACKING_OR_LINEAGE_HANDOFF
  !=
COMPUTATION_EXECUTION

SUFFICIENT_COMPUTATION_PLAN
  !=
OPTIMAL_PLAN
~~~

Optimization may consume a set of sufficient computation plans and resource descriptors as a separate handed-off task.

## 12. Maximum-supported-claim discipline

A conformant Computation result may assert only what the frozen target, evaluation class, dependency interface, closure semantics, coverage, reuse rules, resolution, and claim level support.

Protocol v0.1 may not silently upgrade:

~~~text
target-relative irrelevance
  -> universal irrelevance

valid reuse under one version/regime
  -> permanent reuse

local omission theorem
  -> whole-class omission

symbolic subclass proof
  -> full-class coverage

bounded finite-propagation exclusion
  -> universal DSD locality

sufficient resolution
  -> globally minimal resolution

sound plan
  -> optimal plan

fewer evaluation units
  -> lower runtime

one empirical speedup
  -> universal complexity improvement

fair-baseline NO_GAIN
  -> method failure
~~~

## 13. Prospective Protocol v0.1 obligations

Computation Protocol v0.1 must contain, at minimum:

~~~text
task identity / version / primary-claim lock

target identity / output scope /
equivalence / tolerance / error semantics

source/model/interface version lock

evaluation-class identity /
representation / mode / completeness

evaluation-coverage status

typed Formation / Property /
channel / applicability handoffs

dependency-interface register

required-interface status

semantic obligation-status ledger

execution-action ledger

target-relevance and omission rules

reuse-interface coherence /
equivalence / validity / invalidation

aggregation / compression /
collision / injectivity handoffs when used

resolution / approximation /
error-composition semantics

countable / recursive closure interface when used

dynamic / transition / locality /
propagation handoffs when used

soundness-obligation ledger

evaluation-set outcome

Computation primary status

exact task-terminal precedence /
PARTIAL semantics

method-gain status

comparator-fairness gate for gain claims

Optimization handoff when objective-based
selection is requested

protocol-conformance record

maximum-supported-claim record
~~~

The protocol must preserve the distinction between source-derived constraints and prospective method rules.

## 14. Amendment interpretation lock

~~~text
BOUNDARY_AMENDMENT
  !=
PROTOCOL_VALIDATION

PROTOCOL_FREEZE_AUTHORIZED
  !=
PROTOCOL_INTERNALLY_STANDARDIZED

NO_BOUNDARY_COLLAPSE
  !=
PERMANENT_METHOD_IRREDUCIBILITY

METHOD_IDENTITY_PRESERVED
  !=
METHOD_SUPERIORITY

SOUND_COMPUTATION_PLAN
  !=
COMPUTATIONAL_GAIN

COMPUTATION_NO_GAIN
  !=
METHOD_FAILURE
~~~

## 15. Post-amendment state

~~~text
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

METHOD_IDENTITY_CHANGED:
  no

TASK_INTERFACE_CORE_REOPENED:
  no

DEDICATED_COMPUTATION_PROTOCOL:
  not established

PROTOCOL_FREEZE_AUTHORIZED:
  yes

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
  boundary_amendment_complete

PROTOCOL_REVISION_REQUIRED:
  not applicable pre-protocol

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 16. Protocol-freeze authorization

All seven refinement groups are prospective and preserve the method identity.

~~~text
METHOD_IDENTITY_PRESERVED:
  yes

HISTORICAL_TASK_INTERFACE_REWRITTEN:
  no

HISTORICAL_BOUNDARY_ATTACK_RECORD_REWRITTEN:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no

PROTOCOL_FREEZE_AUTHORIZED:
  yes
~~~

## 17. Next

Freeze executable **Computation Protocol v0.1** from:

~~~text
SOURCE_REGISTRY_v0.1
+
historical TASK_INTERFACE_v0.1-draft
+
BOUNDARY_COUNTEREXAMPLES_v0.1-draft
+
TASK_INTERFACE_BOUNDARY_AMENDMENT_001
~~~

Do not rewrite the historical Task Interface or boundary-attack record during Protocol construction.
