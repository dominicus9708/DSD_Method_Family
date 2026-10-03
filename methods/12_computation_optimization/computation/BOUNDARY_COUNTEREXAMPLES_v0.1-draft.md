# DSD Computation Boundary Counterexamples v0.1 Draft

Status: **EXECUTED — PRE-PROTOCOL BOUNDARY ATTACK COMPLETE**  
Date: **2026-10-03**  
Method: **Computation / DSD 계산론**

Task Interface basis:

~~~text
TASK_INTERFACE_COMMIT:
  e0376c35c9fd6c6ab2fc1a20a5bc0e329fc0fb71

TASK_INTERFACE_BLOB:
  0e307f2e6bb3b579a8bc161cb0a25bd76c28e69f
~~~

Source Registry basis:

~~~text
SOURCE_REGISTRY_COMMIT:
  af9951011d999aef3c29a2beba6093983c1546f6

SOURCE_REGISTRY_BLOB:
  6f5ad5731ee82fc9a6561a39ff6d66fc4bd82461
~~~

This is an internal constructed boundary attack.

It is not external validation.

## 1. Purpose

Attack the historical Computation Task Interface v0.1 draft before any executable protocol is frozen.

The attack pressures:

~~~text
typed status preservation
evaluation-class completeness
branch-family elimination
aggregate/readout collision
required-vs-reused semantics
reuse validity / invalidation
static-vs-dynamic dependency
conditional locality / finite propagation
resolution / approximation
finite-vs-countable / recursive computation
required dependency availability
symbolic class coverage
soundness-vs-performance
fair baseline comparison
Computation-vs-Optimization
Computation-vs-Simulation
Audit substitution
task-terminal precedence and PARTIAL semantics
~~~

Allowed verdicts:

~~~text
PRESERVED_NO_REFINEMENT
PRESERVED_WITH_NONBREAKING_REFINEMENT
BOUNDARY_COLLAPSE
FUNDAMENTAL_INTERFACE_FAILURE
~~~

## 2. Summary result

~~~text
BOUNDARY_ATTACKS_RUN:
  18

PRESERVED_NO_REFINEMENT:
  11

PRESERVED_WITH_NONBREAKING_REFINEMENT:
  7

BOUNDARY_COLLAPSE_FOUND:
  0

FUNDAMENTAL_INTERFACE_FAILURE:
  0

REFINEMENT_GROUPS_REQUIRED:
  7

BOUNDARY_AMENDMENT_REQUIRED:
  yes

PROTOCOL_FREEZE_AUTHORIZED_BEFORE_AMENDMENT:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

The Computation method identity survives.

The seven refined attacks expose execution semantics that should be bound prospectively before protocol freeze.

## 3. B01 — channel absent versus admitted zero-contribution channel

Fixture:

~~~text
case A:
  channel q is not admitted / absent

case B:
  channel q is admitted
  component term for the declared target = 0
~~~

Attack:

~~~text
treat A and B as the same computational state
and use either as justification for the same downstream pruning rule
~~~

Rejected.

The historical draft already preserves:

~~~text
NOT_ADMITTED != ZERO_CONTRIBUTION
CHANNEL_ABSENCE != ADMITTED_ZERO_CONTRIBUTION
~~~

A zero-valued term may still carry a different typed/channel identity from an absent channel.

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 4. B02 — inapplicable, undefined, and defined zero

Fixture:

~~~text
u1:
  property INAPPLICABLE

u2:
  property APPLICABLE_BUT_UNDEFINED

u3:
  property DEFINED_ZERO
~~~

Attack:

~~~text
map all three to numerical zero
then prune the same downstream branch
~~~

Rejected.

The draft already preserves the inherited typed statuses and forbids:

~~~text
INAPPLICABLE != COMPUTED_ZERO
APPLICABLE_BUT_UNDEFINED != ZERO
UNDEFINED != ZERO
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 5. B03 — one failed branch versus whole-family elimination

Fixture:

~~~text
branch family:
  {b1,b2,b3}

b1:
  fails one prerequisite

b2:
  admissible

b3:
  admissibility unresolved
~~~

Attack:

~~~text
b1 fails
  ->
entire branch family may be pruned
~~~

Rejected.

The draft already preserves:

~~~text
ONE_FAILED_BRANCH != GLOBAL_PRUNING_LICENSE
~~~

and requires dependency / relevance justification at the declared target scope.

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 6. B04 — same aggregate output, distinct support

Fixture:

~~~text
source S1:
  support {a,b}
  contributions +1,-1

source S2:
  support {c}
  contribution 0

aggregate(S1) = aggregate(S2) = 0
~~~

Attack:

~~~text
same aggregate
  ->
same source branch
  ->
safe merge / reuse
~~~

Rejected.

The draft already preserves:

~~~text
OUTPUT_EQUALITY != SOURCE_EQUIVALENCE
AGGREGATE_EQUALITY != CACHE_EQUIVALENCE
~~~

and requires information-loss / support-retention sidecars when claim-relevant.

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 7. B05 — same reduced readout, different component-resolved state

Fixture:

~~~text
U != V

O(U) = O(V)

future target:
  depends on a component distinction erased by O
~~~

Attack:

~~~text
same reduced readout
  ->
one component-resolved branch may be omitted permanently
~~~

Rejected.

The draft already preserves:

~~~text
EQUAL_REDUCED_READOUT != EQUAL_COMPONENT_STATE
AGGREGATE_INVISIBLE != COMPONENT_IRRELEVANT
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 8. B06 — a semantically required unit is satisfied by valid reuse

Fixture:

~~~text
target T:
  requires value f(x)

fresh evaluation unit:
  U_f

valid frozen cache:
  contains f(x)
  same input identity
  same source/model version
  same status / regime
  reuse validity established

therefore:
  semantic result f(x) is required
  fresh reevaluation is not required
  reuse is valid
~~~

Problem:

The historical draft lists:

~~~text
COMPUTATION_UNIT_REQUIRED
COMPUTATION_UNIT_SOUNDLY_OMITTABLE
COMPUTATION_UNIT_REUSABLE
...
~~~

as one working unit-disposition family.

But this fixture requires two independent questions:

~~~text
Is the semantic result required for the target?
How is that obligation satisfied in this execution plan?
~~~

A unit/result can be target-required while its fresh evaluation is replaced by reuse.

Required refinement R1:

Separate **obligation necessity** from **execution action**.

Prospective status families:

~~~text
COMPUTATION_OBLIGATION_STATUS:
  REQUIRED_FOR_TARGET
  NOT_REQUIRED_FOR_TARGET
  OBLIGATION_BLOCKED
  OBLIGATION_CONFLICTING
  OBLIGATION_UNDERDETERMINED
  OBLIGATION_OUT_OF_SCOPE

COMPUTATION_EXECUTION_ACTION:
  EVALUATE_FRESH
  REUSE_VALID_RESULT
  OMIT_AS_TARGET_IRRELEVANT
  SYMBOLICALLY_DISCHARGE
  ACTION_BLOCKED
  ACTION_CONFLICTING
  ACTION_UNDERDETERMINED
  ACTION_OUT_OF_SCOPE
~~~

The future protocol may still emit convenience sets, but it must not force semantic necessity and execution mode into one exclusive label.

Core guard:

~~~text
REQUIRED_RESULT
  !=
FRESH_EVALUATION_REQUIRED

REUSE
  !=
TARGET_IRRELEVANCE
~~~

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

## 9. B07 — reuse record conflicts with invalidation rule

Fixture:

~~~text
cache record:
  valid under model version v1
  regular regime R1

current task:
  model version v2
  transition R1 -> R2 occurred

record A:
  generic cache key says HIT

record B:
  frozen invalidation rule says
  version or regime transition invalidates reuse

no precedence / coherence status frozen
~~~

The historical draft freezes reuse validity scope and invalidation rules, but does not yet define task-level coherence semantics when claim-relevant reuse records conflict.

Required refinement R2:

Freeze:

~~~text
REUSE_INTERFACE_COHERENCE_STATUS:
  REUSE_INTERFACE_CONSISTENT
  REUSE_INTERFACE_CONFLICTING
  REUSE_INTERFACE_UNDERDETERMINED
  REUSE_INTERFACE_BLOCKED
  REUSE_INTERFACE_OUT_OF_SCOPE

REUSE_PRECEDENCE_RULE_OR_NONE
REUSE_INVALIDATION_EVALUATION_MODE
~~~

Consequences:

~~~text
explicit applicable invalidation
  defeats a stale generic cache-hit claim

mutually incompatible applicable reuse records
  ->
CONFLICTING

multiple admissible reuse semantics with different actions
  ->
UNDERDETERMINED

required reuse metadata unavailable
  ->
BLOCKED
~~~

Core guards:

~~~text
CACHE_HIT != SEMANTIC_REUSE_VALIDITY
STALE_REUSE_RECORD != CURRENT_VALID_REUSE
~~~

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

## 10. B08 — static dependency versus dynamic causal / propagation dependency

Fixture:

~~~text
static dependency graph:
  no edge A -> Z

dynamic transition:
  A changes B
  B later changes Z
~~~

Attack:

~~~text
no direct static edge A -> Z
  ->
A is irrelevant to Z
~~~

Rejected.

The historical draft already preserves:

~~~text
STATIC_DEPENDENCY != DYNAMIC_CAUSAL_DEPENDENCY
NO_DIRECT_EDGE != NO_INDIRECT_INFLUENCE
~~~

and requires dynamic / transition / locality handoffs when such reasoning is used.

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 11. B09 — finite-propagation pruning without a valid specialization

Fixture A:

~~~text
localization carrier:
  supplied

propagation theorem / bound:
  unavailable
~~~

Fixture B:

~~~text
finite-propagation bound:
  supplied for regime R1

current task:
  regime R2
~~~

Attack:

~~~text
outside the guessed/current cone
  ->
safe omission
~~~

Rejected.

The draft already requires explicit propagation-bound provenance, regime, metric/time, discrepancy, and support-faithfulness interfaces.

When such a required interface is unavailable, the relevant pruning claim is blocked rather than established.

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 12. B10 — local approximation passes but end-to-end target fails

Fixture:

~~~text
stage 1 local error <= epsilon
stage 2 local error <= epsilon

target requirement:
  final relational error <= epsilon

error composition:
  not supplied

actual admissible compositions:
  one stays <= epsilon
  another exceeds epsilon
~~~

Attack:

~~~text
each local stage passes
  ->
whole computation is target-safe
~~~

Rejected.

The draft already freezes:

~~~text
ERROR_COMPOSITION_RULE_IF_MULTISTAGE
TARGET_DISTINGUISHABILITY_REQUIREMENT
TARGET_EQUIVALENCE_OR_TOLERANCE
~~~

and preserves:

~~~text
SMALL_LOCAL_ERROR != BOUNDED_END_TO_END_ERROR
COMPONENTWISE_TOLERANCE != RELATIONAL_TARGET_PRESERVATION
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 13. B11 — countable / recursive computation without convergence or termination semantics

Fixture A:

~~~text
evaluation family:
  countably infinite

partial sums:
  order-sensitive unless an extra condition is supplied

convergence interface:
  unavailable
~~~

Fixture B:

~~~text
recursive dependency cycle:
  x -> y -> x

fixed-point / well-foundedness / termination rule:
  unavailable
~~~

The draft states that convergence, well-foundedness, and termination must not be manufactured, but it does not yet freeze the status semantics of these interfaces.

Required refinement R3:

Freeze:

~~~text
COMPUTATION_CLOSURE_INTERFACE_ID
COMPUTATION_CLOSURE_KIND:
  FINITE_TERMINATION
  COUNTABLE_CONVERGENCE
  RECURSION_WELL_FOUNDEDNESS
  FIXED_POINT
  EXTERNALLY_SUPPLIED_CLOSURE

COMPUTATION_CLOSURE_STATUS:
  CLOSURE_ESTABLISHED
  CLOSURE_NOT_ESTABLISHED
  CLOSURE_BLOCKED
  CLOSURE_CONFLICTING
  CLOSURE_UNDERDETERMINED
  CLOSURE_OUT_OF_SCOPE

ORDER_DEPENDENCE_STATUS
TERMINATION_OR_CONVERGENCE_PROVENANCE
~~~

Consequences:

~~~text
required closure interface unavailable
  ->
BLOCKED

several admissible orders / fixed-point semantics
yield different target outputs
  ->
UNDERDETERMINED

incompatible frozen closure records
  ->
CONFLICTING

fully evaluable closure condition fails
  ->
NOT_ESTABLISHED
~~~

Core guards:

~~~text
FINITE_CORRECTNESS != COUNTABLE_CORRECTNESS
FINITE_DAG_TERMINATION != GENERAL_RECURSIVE_TERMINATION
~~~

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

## 14. B12 — required dependency unavailable versus dependency established irrelevant

Fixture A:

~~~text
target T requires deciding whether D affects T

dependency record:
  unavailable
~~~

Fixture B:

~~~text
dependency record:
  supplied

proof:
  D cannot influence T under frozen scope
~~~

Attack:

~~~text
treat both as:
  D may be omitted
~~~

Rejected.

The historical draft already separates:

~~~text
UNAVAILABLE_REQUIRED_INTERFACE != BRANCH_IRRELEVANCE
MISSING_DEPENDENCY_RECORD != NEGATIVE_DEPENDENCY
BLOCKED != SOUNDLY_OMITTED
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 15. B13 — symbolic evaluator covers only part of an intensional class

Fixture:

~~~text
evaluation class:
  E = {x in R : P(x)}

symbolic theorem:
  proves omission sound for x satisfying P(x) and x >= 0

uncovered region:
  x < 0

task claim:
  SOUND_OMISSION_SET for all E
~~~

The historical draft permits symbolic/theorem-level evaluation and class-completeness statuses, but does not yet require a separate claim-relevant record of **evaluation coverage**.

Required refinement R4:

Freeze:

~~~text
EVALUATION_COVERAGE_SCOPE
EVALUATION_COVERAGE_STATUS:
  COVERAGE_COMPLETE_FOR_DECLARED_CLAIM
  COVERAGE_PARTIAL
  COVERAGE_BLOCKED
  COVERAGE_CONFLICTING
  COVERAGE_UNDERDETERMINED
  COVERAGE_OUT_OF_SCOPE

COVERED_SUBCLASS
UNCOVERED_OR_UNRESOLVED_SUBCLASS
COVERAGE_PROVENANCE
~~~

A symbolic theorem may discharge a whole class without enumeration only if its frozen applicability domain covers the entire declared claim scope.

Core guards:

~~~text
SYMBOLIC_RULE_FOUND
  !=
FULL_CLASS_COVERAGE

CLASS_DEFINITION_COMPLETE
  !=
EVALUATION_COVERAGE_COMPLETE
~~~

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

## 16. B14 — sound pruning with zero performance gain

Fixture:

~~~text
DSD computation plan:
  safely omits 20 expensive-looking units

implementation overhead:
  dependency analysis + cache validation costs more

baseline runtime:
  10 ms

DSD-plan runtime:
  12 ms

soundness:
  established
~~~

Attack:

~~~text
no speedup
  ->
Computation method failed
~~~

Rejected in principle, but the future protocol needs an explicit gain-status record rather than only a prose guard.

Required refinement R5:

Separate method validity from performance gain.

Freeze:

~~~text
COMPUTATION_METHOD_GAIN_STATUS:
  COMPUTATION_GAIN_ESTABLISHED
  COMPUTATION_NO_GAIN
  COMPUTATION_GAIN_NOT_TESTED
  COMPUTATION_GAIN_BLOCKED
  COMPUTATION_GAIN_CONFLICTING
  COMPUTATION_GAIN_UNDERDETERMINED
  COMPUTATION_GAIN_OUT_OF_SCOPE

GAIN_METRIC_SCOPE
GAIN_BASELINE_ID
GAIN_EVIDENCE_PROVENANCE
~~~

Core guards:

~~~text
COMPUTATION_ESTABLISHED
  may coexist with
COMPUTATION_NO_GAIN

NO_GAIN != METHOD_FAILURE
~~~

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

## 17. B15 — apparent speedup caused by changed target or information access

Fixture A:

~~~text
DSD plan:
  target tolerance = 1e-2

baseline:
  target tolerance = 1e-8

DSD plan is faster
~~~

Fixture B:

~~~text
DSD plan:
  receives hidden dependency / cache sidecar

baseline:
  does not receive it
~~~

Fixture C:

~~~text
same target
different input-family distribution
hardware / parallelism also changed
~~~

Attack:

~~~text
report speedup as Computation method gain
~~~

The historical draft requires a baseline and environment for empirical cost claims, but fair-comparison equivalence needs stronger binding before baseline challenges.

Required refinement R6:

Freeze a comparator-fairness record:

~~~text
COMPARATOR_TARGET_EQUIVALENCE:
  matched / not_matched / blocked / underdetermined

COMPARATOR_INFORMATION_ACCESS:
  equal / unequal / blocked / underdetermined

COMPARATOR_INPUT_FAMILY:
  frozen

COMPARATOR_ERROR_OR_TOLERANCE:
  frozen

COMPARATOR_HARDWARE_ENVIRONMENT:
  frozen_if_empirical

COMPARATOR_IMPLEMENTATION_SCOPE:
  declared

COMPARATOR_FAIRNESS_STATUS:
  FAIR
  NOT_FAIR
  BLOCKED
  CONFLICTING
  UNDERDETERMINED
  OUT_OF_SCOPE
~~~

A gain claim requires claim-relevant target and information-access comparability.

Core guards:

~~~text
CHANGED_TARGET_SPEEDUP
  !=
METHOD_GAIN

HIDDEN_INFORMATION_ADVANTAGE
  !=
METHOD_GAIN

UNCONTROLLED_ENVIRONMENT_DIFFERENCE
  !=
ALGORITHMIC_GAIN
~~~

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

## 18. B16 — Computation versus Optimization under apparent minimality

Fixture A:

~~~text
soundness theorem:
  proves every valid plan must evaluate units {a,b}
  and nothing else is required

therefore:
  {a,b} is mathematically minimal by inclusion
~~~

Fixture B:

~~~text
two sufficient plans:
  P1 runtime estimate 10
  P2 runtime estimate 8

task asks:
  choose faster plan
~~~

Attack:

~~~text
treat both as the same "minimal computation" operation
~~~

Rejected.

The draft already separates:

~~~text
minimality entailed by frozen mathematical necessity
  -> may remain a Computation theorem

choice by cost / utility objective
  -> Optimization handoff
~~~

Core guards:

~~~text
SUFFICIENT != OPTIMAL
COMPUTATION != OPTIMIZATION
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 19. B17 — Computation plan versus Simulation execution

Fixture:

~~~text
dynamic model:
  supplied

Computation result:
  update cells A,B,C
  omit cells D,E under a sound locality rule

requested next act:
  numerically evolve A,B,C through 1000 time steps
~~~

Attack:

~~~text
because Computation identified required updates,
it has already executed the simulation
~~~

Rejected.

The historical draft already preserves:

~~~text
COMPUTATION_PLAN != SIMULATION_EXECUTION
~~~

A Simulation task may consume the plan, but the plan and the actual state evolution remain different operations and outputs.

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 20. B18 — Audit substitution and mixed task-terminal pressure

### Fixture A — Audit substitution

~~~text
candidate plan P:
  already supplied

Audit asks:
  does P satisfy the frozen soundness obligations?

Computation asks:
  construct / determine the required-omitted-reused plan itself
~~~

Attack:

~~~text
because Audit can verify P,
Audit and Computation collapse
~~~

Rejected.

Five-interface identity remains different:

~~~text
AUDIT:
  evaluates conformance / evidence / process

COMPUTATION:
  determines target-relative evaluation obligations
  and assembles the computation plan
~~~

### Fixture B — mixed obligations

One task requires three independent obligations:

~~~text
Q1 required-evaluation set:
  ESTABLISHED

Q2 reuse claim:
  evaluable and NOT_ESTABLISHED

Q3 approximation obligation:
  BLOCKED
~~~

A second task has:

~~~text
Q1 ESTABLISHED
Q2 NOT_ESTABLISHED
no blocked / conflicting / underdetermined / out-of-scope obligation
~~~

The historical draft proposes terminal precedence and a PARTIAL meaning, but the final protocol needs exact binding to avoid using PARTIAL to hide a required blocked obligation.

Required refinement R7:

Freeze exact task-terminal precedence:

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

Freeze exact PARTIAL semantics:

~~~text
PARTIAL is permitted only when:

1. multiple independently required in-scope obligations exist
2. at least one is ESTABLISHED
3. at least one other independently required obligation
   is evaluably NOT_ESTABLISHED
4. no required obligation is BLOCKED
5. no higher-priority terminal applies
~~~

Therefore:

~~~text
Fixture B first task:
  BLOCKED

Fixture B second task:
  PARTIAL
~~~

Lower-level unit / obligation statuses remain visible under the task terminal.

Core guards:

~~~text
PARTIAL != BLOCKED_WITH_SOME_SUCCESS
PARTIAL != ATOMIC_FAILURE_RELABELED
~~~

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

## 21. Required refinement groups

The seven refined attacks collapse into seven prospective amendment groups.

### R1 — semantic necessity versus execution action

Separate whether a result/unit is required for the target from how the obligation is discharged.

A target-required result may be satisfied by valid reuse or symbolic discharge without fresh evaluation.

### R2 — reuse-interface coherence and invalidation

Freeze coherence / precedence semantics for cache/reuse validity, version changes, regime changes, and transition-triggered invalidation.

### R3 — countable / recursive closure interface

Freeze convergence, well-foundedness, fixed-point, termination, and order-dependence status semantics.

### R4 — symbolic evaluation coverage

Separate class-definition completeness from proof/evaluation coverage completeness.

A symbolic theorem that covers only a subclass may not close the whole task.

### R5 — explicit Computation method-gain status

Separate soundness / method validity from runtime, memory, evaluation-count, or other computational gain.

Preserve `NO_GAIN` as a valid outcome.

### R6 — comparator fairness

Freeze target, information access, input family, tolerance/error semantics, and empirical environment before claiming gain over a baseline.

### R7 — exact task-terminal precedence and PARTIAL semantics

Prevent PARTIAL from hiding BLOCKED, CONFLICTING, UNDERDETERMINED, or OUT_OF_SCOPE required obligations.

## 22. Surviving method boundary

No attack requires collapsing Computation into:

~~~text
Optimization
Aggregation
Compression
Analysis
Measurement
Simulation
Prediction
Transformation
Audit
Tracking
Lineage
~~~

The method boundary remains:

~~~text
COMPUTATION:
  determine target-relative evaluation obligations,
  sound omissions,
  scoped reuse,
  required resolution,
  and associated soundness obligations

OPTIMIZATION:
  select among admissible alternatives
  under an explicit objective / constraint system

SIMULATION:
  execute state evolution

AUDIT:
  evaluate conformance / evidence / process
~~~

Overlap of inputs or handoffs does not establish method identity.

## 23. Historical-draft preservation

The historical Task Interface:

~~~text
methods/12_computation_optimization/computation/TASK_INTERFACE_v0.1-draft.md
commit:
  e0376c35c9fd6c6ab2fc1a20a5bc0e329fc0fb71
blob:
  0e307f2e6bb3b579a8bc161cb0a25bd76c28e69f
~~~

must remain unchanged.

The seven refinements belong in a separate prospective amendment.

## 24. Final boundary verdict

~~~text
METHOD_IDENTITY_PRESERVED:
  yes

BOUNDARY_ATTACKS_RUN:
  18

PRESERVED_NO_REFINEMENT:
  11

PRESERVED_WITH_NONBREAKING_REFINEMENT:
  7

BOUNDARY_COLLAPSE_FOUND:
  0

FUNDAMENTAL_INTERFACE_FAILURE:
  0

BOUNDARY_AMENDMENT_001_REQUIRED:
  yes

REFINEMENT_GROUPS:
  7

PROTOCOL_FREEZE_AUTHORIZED_BEFORE_AMENDMENT:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

This is internal constructed boundary evidence.

It does not establish external applicability, independent validation, or practical performance gain.

## 25. Current state

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

BOUNDARY_COLLAPSE_FOUND:
  0

FUNDAMENTAL_INTERFACE_FAILURE:
  0

BOUNDARY_AMENDMENT_001:
  not yet established

REFINEMENT_GROUPS_REQUIRED:
  7

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
  pre_protocol_boundary_attack_complete

PROTOCOL_REVISION_REQUIRED:
  not applicable pre-protocol

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 26. Next

Establish **Computation Task Interface Boundary Amendment 001** prospectively.

The amendment must bind R1-R7 before an executable Computation Protocol v0.1 may be frozen.
