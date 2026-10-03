# DSD Computation — Source / Registry Recovery v0.1

Status: **SOURCE / REGISTRY RECOVERY COMPLETE — PRE-TASK-INTERFACE**  
Date: **2026-10-03**  
Method: **Computation / DSD 계산론**  
Legacy path ID: `12A`  
Higher field: **VII. Computation & Selection / 계산·선택**

This document recovers the source constraints and current method-registry boundary for Computation before any Task Interface is frozen.

It is not a Computation protocol and does not itself authorize a protocol freeze.

## 1. Current registry identity

Current repository / Notion definition:

~~~text
Task:
  determine which structural branches, channels,
  dependencies, resolutions, and reusable common parts
  must actually be evaluated for a declared computational target

Candidate operations:
  eliminate impossible or inapplicable branches before expensive evaluation
  identify common prefixes / reusable subcomputations
  select channels capable of affecting the declared output
  choose calculation resolution from required distinguishability
  preserve soundness conditions for every omitted computation

Boundary:
  DSD structure may organize computation,
  but correctness of pruning and any complexity / runtime improvement
  must be justified separately
~~~

Current Notion method root:

~~~text
DSD 계산론
Notion page:
  3d281f51-e7fa-817b-9804-fbd0d3e57a7d
~~~

Current GitHub path:

~~~text
methods/12_computation_optimization/computation/
~~~

Registry boundary with Optimization:

~~~text
COMPUTATION:
  determines what must be evaluated,
  what may be omitted under a soundness argument,
  and what computation may be reused

OPTIMIZATION:
  selects among admissible alternatives
  under explicit objectives and constraints

COMPUTATION != OPTIMIZATION
~~~

## 2. Source hierarchy used for recovery

### S1 — Formation Axiom System

Source:

~~~text
DSD_Formation_Axiom_System_EN(5).pdf
~~~

Recovered constraints:

- the seven Formation stages distinguish admission, restriction, realization, describability, partial assignment, operational-channel formation, and finite composition;
- the assigned value participates in operational-channel identity;
- undefined assignment, defined zero, channel absence, and admitted zero contribution remain distinct;
- only after the admitted operational-channel set is determined is finite composition introduced;
- nested stage-comparison sets locate the earliest stage at which no compatible full comparison tuple survives;
- one failed candidate map is not sufficient to establish first branching of the whole comparison problem;
- equality of composite outputs is weaker than equality of the full formation source.

Computation consequence:

~~~text
UNDEFINED_ASSIGNMENT
  !=
DEFINED_ZERO

CHANNEL_ABSENCE
  !=
ADMITTED_ZERO_CONTRIBUTION

ONE_FAILED_BRANCH_OR_MAP
  !=
ALL_BRANCHES_EXCLUDED

COMPOSITE_OUTPUT_EQUALITY
  !=
SOURCE_LEVEL_EQUIVALENCE
~~~

Formation stage order may organize structural dependency, but it is not automatically a wall-clock execution schedule.

### S2 — Property Axiom System

Source:

~~~text
DSD_Property_Axiom_System_EN(3).pdf
~~~

Recovered Property status family:

~~~text
UNDECLARED
PROFILE_UNAVAILABLE
INAPPLICABLE
PREREQUISITE_UNSATISFIED
APPLICABLE_BUT_UNDEFINED
DEFINED_ZERO
DEFINED_NONZERO_OR_VALUE
~~~

Defined property records retain:

~~~text
property kind
complete ordered typed input
assigned value
~~~

The Property system also preserves:

~~~text
defined assignment
  requires applicability
  and satisfied declared prerequisites

but

applicable
  does not imply defined

prerequisite-satisfied
  does not imply defined
~~~

The explicit completion uniquely derives status/domain records from a fully supplied primitive core, but does not supply a recursive dependency evaluator for arbitrary later extensions.

Computation consequence:

~~~text
INAPPLICABLE
  !=
COMPUTED_ZERO

PREREQUISITE_UNSATISFIED
  !=
FALSE_NUMERICAL_OUTPUT

APPLICABLE_BUT_UNDEFINED
  !=
ZERO

PROPERTY_DEPENDENCY
  must preserve typed prerequisite scope
~~~

A later Computation method may use these statuses to avoid invalid evaluations, but any omission rule must still be tied to a declared computational target and dependency interface.

### S3 — Channel-Indexed Static Aggregation

Source:

~~~text
DSD_Channel_Indexed_Static_Aggregation_EN(9).pdf
~~~

Recovered constraints:

~~~text
channel component terms
  are evaluated on admitted formation channels

finite sums
  realize the supplied post-Stage-VI composition interface

optional countable extension
  requires absolute summability

typed property aggregation
  requires an explicit bridge

multi-input property data
  have no automatic unary channel owner
~~~

Support-retaining data and exact kernel criteria show:

~~~text
aggregate equality
  !=
support equality

aggregate equality
  !=
source decomposition equality

zero aggregate difference
  !=
no component-level difference
~~~

Computation consequence:

~~~text
AGGREGATE_EQUALITY
  !=
LICENSE_TO_MERGE_SOURCE_BRANCHES

SAME_REDUCED_READOUT
  !=
SAME_REUSABLE_SUBCOMPUTATION

PROPERTY_TO_CHANNEL_DEPENDENCY
  requires an explicit association / bridge

COUNTABLE_EVALUATION
  cannot inherit finite-sum guarantees
  without the declared extension hypotheses
~~~

Any computation shortcut that uses aggregate equality is bounded to the exact target and equivalence relation for which that equality is sufficient.

### S4 — Structural Reorganization Dynamics

Source:

~~~text
DSD_Structural_Reorganization_Dynamics_EN(20260904-092544).pdf
~~~

Recovered regular-epoch discipline:

~~~text
during a regular epoch:
  Stage-VI formation background and inherited channel identities are fixed
  declared support types are fixed
  selected property signature/profile data are fixed
  required analytic carrier types are fixed

a change invalidating the regular support signature
  ends the regular epoch
~~~

Recovered interface discipline:

~~~text
missing optional interface
  is omitted

missing optional interface
  !=
numerical zero object

undefined property state
  !=
defined zero
~~~

Recovered dynamic boundary:

~~~text
transport
  !=
coupling transfer
  !=
property-status transition
  !=
formation transition
~~~

Finite propagation is available only under explicit localization, metric-time, discrepancy, constitutive, regularity, and support-faithfulness assumptions; the general DSD dynamic layer does not supply a universal propagation speed.

Reduced readouts need not classify the complete component-resolved state, and aggregate-invisible component discrepancies may still propagate.

Computation consequence:

~~~text
REGULAR_EPOCH_REUSE
  must be invalidated or re-justified across claim-relevant transitions

FINITE_PROPAGATION_PRUNING
  requires the exact specialization hypotheses

PROJECTED_OR_AGGREGATE_INVISIBILITY
  !=
STRUCTURAL_IRRELEVANCE

RANK_OR_DIMENSIONAL_LABEL
  !=
UNIVERSAL_COMPLEXITY_OR_PROPAGATION_BOUND
~~~

### S5 — DSD Method Family registry and shared interface discipline

Project-internal sources:

~~~text
methods/README.md
methodology/DSD_METHOD_FAMILY_FRAMEWORK.md
methodology/DSD_INTERFACE_PROFILE.md
methodology/SHARED_CORE_EXTRACTION_RULE.md
~~~

Recovered method boundary:

~~~text
COMPUTATION != OPTIMIZATION

Computation:
  determine required evaluation

Optimization:
  select among admissible alternatives
  under explicit objectives / constraints
~~~

Recovered family-wide rules:

~~~text
preserve claim-relevant typed status distinctions
lock source / interface / version semantics
make cross-layer mappings explicit
avoid optional-interface overconstraint
respect information-loss limits
separate regular evolution / transition / lineage
preserve failures / NO_GAIN / precommit integrity
separate DSD-internal success from external-domain validation
~~~

Shared-core constraints restrict Computation construction but do not directly validate Computation.

### S6 — Audit / outcome semantics

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

Computation consequence:

~~~text
a pruning rule that is valid only for one target / regime / resolution
must remain bounded to that scope

NO_GAIN in runtime / memory / evaluation count
does not imply method failure

a correct computation plan with no complexity improvement
may still be structurally valid
~~~

## 3. Source-derived Computation constraints

The following are recovered constraints rather than new Computation theorems.

~~~text
CR-01
  preserve claim-relevant Formation / Property typed statuses;
  do not replace undefined / absent / inapplicable states by zero

CR-02
  every evaluated map or assignment must be used only on its declared domain

CR-03
  admitted-channel identity and channel absence must be distinguished
  from a zero-valued / zero-term channel

CR-04
  one failed branch / comparison / candidate does not justify
  global branch elimination

CR-05
  any omitted dependency must be justified relative to
  a frozen computational target and explicit dependency / influence interface

CR-06
  aggregate / projection / reduced-readout equality does not justify
  source-level branch merging unless the declared target equivalence permits it

CR-07
  multi-input Property data require an explicit association
  before they can be treated as one channel's computational dependency

CR-08
  finite and countable evaluation regimes remain distinct;
  countable reuse / aggregation inherits only the explicitly supplied convergence conditions

CR-09
  regular-epoch reuse / caching is bounded by frozen identity,
  support-type, interface-version, and regime assumptions

CR-10
  a claim-relevant transition invalidates inherited reuse
  unless an explicit transition / lineage / equivalence bridge licenses it

CR-11
  finite-propagation or locality-based pruning requires
  the exact specialization assumptions that establish the bound

CR-12
  projected / aggregate invisibility does not establish
  component-level irrelevance

CR-13
  Formation stage order / first branching may guide structural evaluation,
  but neither is automatically a physical-time or runtime schedule

CR-14
  Computation output remains distinct from Optimization choice;
  no objective-function selection is imported silently

CR-15
  pruning soundness and computational complexity improvement are separate claims;
  speedup / memory reduction / evaluation-count reduction must be measured or proved separately

CR-16
  shared-core or neighboring-method evidence is not direct Computation validation
~~~

## 4. Working atomic task — not yet frozen

The current working formulation is:

~~~text
Given:
  a declared computational target,
  a frozen source / model / interface version,
  candidate evaluation units or branches,
  admitted channels and typed statuses where relevant,
  explicit dependency and cross-layer bridge information,
  available aggregation / compression / transition sidecars,
  declared resolution / distinguishability requirements,
  and any dynamic regime / locality assumptions,

determine:
  which evaluations are required,
  which evaluations may be omitted with a soundness justification,
  which subcomputations may be reused under a frozen equivalence / validity scope,
  which dependencies or interfaces block evaluation,
  which resolution is sufficient for the declared target,
  and what correctness obligations remain for every omission or reuse decision.
~~~

This formulation is **prospective methodological construction**, not a theorem supplied by the predecessor papers.

It remains open to direct boundary attack before protocol freeze.

The word "required" means required under the declared target/interface, not globally minimal cost.

## 5. Candidate information classes for the future Task Interface

Not yet frozen:

~~~text
COMPUTATION_TASK_ID
TASK_VERSION

COMPUTATIONAL_TARGET_ID
TARGET_VERSION
TARGET_OUTPUT_SCOPE
TARGET_EQUIVALENCE_OR_TOLERANCE

SOURCE_MODEL_ID
SOURCE_MODEL_VERSION
ACTIVE_DSD_LAYERS

EVALUATION_UNIT_REGISTRY
BRANCH_REGISTRY
CHANNEL_REGISTRY

STATUS_SIDECARS
APPLICABILITY_SIDECARS
DEPENDENCY_GRAPH_OR_RELATION
CROSS_LAYER_BRIDGES

REQUIRED_INTERFACE_REGISTER
REQUIRED_INTERFACE_STATUS

INFLUENCE_OR_RELEVANCE_RULE
OMISSION_RULE
OMISSION_JUSTIFICATION

REUSE_CLASS_ID
REUSE_EQUIVALENCE
REUSE_VALIDITY_SCOPE
CACHE_OR_MEMOIZATION_INVALIDATION_RULE

RESOLUTION_REQUIREMENT
DISTINGUISHABILITY_REQUIREMENT
APPROXIMATION_OR_ERROR_BOUND

DYNAMIC_REGIME
TRANSITION_HANDOFF
LOCALITY_OR_PROPAGATION_HANDOFF

REQUIRED_EVALUATION_SET
OMITTED_EVALUATION_SET
REUSED_EVALUATION_SET
BLOCKED_EVALUATION_SET
UNRESOLVED_EVALUATION_SET

SOUNDNESS_OBLIGATION_LEDGER
COMPLEXITY_OR_COST_EVIDENCE
MAXIMUM_SUPPORTED_CLAIM
~~~

These are recovery candidates only.

They do not yet constitute a required task record.

## 6. Prospective guards to pressure before freezing

Not yet protocol rules:

~~~text
NOT_ADMITTED
  !=
ZERO_CONTRIBUTION

INAPPLICABLE
  !=
COMPUTED_ZERO

APPLICABLE_BUT_UNDEFINED
  !=
FALSE_RESULT

ONE_FAILED_BRANCH
  !=
GLOBAL_PRUNING_LICENSE

OUTPUT_EQUALITY
  !=
SOURCE_EQUIVALENCE

AGGREGATE_EQUALITY
  !=
CACHE_EQUIVALENCE

SAME_LABEL_OR_SHAPE
  !=
REUSABLE_SUBCOMPUTATION

OMITTED
  !=
PROVED_IRRELEVANT

STATIC_DEPENDENCY
  !=
DYNAMIC_CAUSAL_DEPENDENCY

FORMATION_STAGE_ORDER
  !=
RUNTIME_SCHEDULE

FIRST_BRANCH
  !=
AUTOMATIC_EXECUTION_CUTOFF

FINITE_PROPAGATION_BOUND
  !=
UNIVERSAL_DSD_PRUNING_RULE

LOWER_RESOLUTION
  !=
SAFE_COMPUTATION

SOUND_PRUNING
  !=
COMPLEXITY_IMPROVEMENT

COMPUTATION
  !=
OPTIMIZATION
~~~

Each guard must be attacked by pre-protocol counterexamples before adoption.

## 7. Open interface questions

Intentionally unresolved before Task Interface drafting:

~~~text
Q1
  What exact evidence authorizes omission:
  inapplicability, proven non-influence, dependency closure,
  equivalence, locality bound, or another typed condition?

Q2
  Must evaluation units be explicitly enumerable,
  or may symbolic / theorem-level evaluation represent
  large or infinite branch families?

Q3
  What exact relation licenses reusable common computation,
  and what version / regime / status changes invalidate reuse?

Q4
  How should required-interface unavailability be distinguished from
  evaluable but unnecessary branches?

Q5
  How should approximate resolution / tolerance interact with
  typed status distinctions and downstream target equivalence?

Q6
  What task terminals distinguish:
  established sufficient plan,
  partially evaluable plan,
  blocked dependency,
  conflicting dependency semantics,
  underdetermined relevance,
  out-of-scope target?

Q7
  Which cost fields are merely descriptive evidence,
  and which would cross the boundary into Optimization?

Q8
  How should dynamic transition boundaries invalidate cached or
  reused computation without silently executing Lineage or Simulation?

Q9
  Does "minimal evaluation set" belong to Computation only when
  minimality is theorem-proved, or does selecting the cheapest
  sufficient set become Optimization?

Q10
  How should NO_GAIN be recorded when a sound DSD computation plan
  performs no better than a competent non-DSD dependency evaluator?
~~~

## 8. Initial neighboring-method pressure map

The first Task Interface / boundary phase should directly pressure at least:

~~~text
Optimization
  required evaluation
  vs objective / constraint-based strategy selection

Aggregation
  evaluating / reusing component contributions
  vs producing a summary readout

Compression
  omitting computation
  vs intentionally reducing representation

Analysis
  structural decomposition
  vs deciding which decomposed parts must be evaluated

Measurement
  required resolution / distinguishability
  vs executing or defining measurement evidence

Simulation
  determining which state-update operations are needed
  vs actually evolving a model

Prediction
  computing a declared target
  vs making a future-world claim

Transformation
  reusing a map / common subcomputation
  vs transforming a source object

Audit
  soundness / conformance checking
  vs producing the computation plan

Tracking / Lineage
  reuse invalidation provenance / identity
  vs computation itself
~~~

Additional neighboring pairs may be added during boundary attack if the Task Interface exposes further collision risk.

## 9. Current recovery state

~~~text
SOURCE_REGISTRY_RECOVERY:
  complete

TASK_INTERFACE_DRAFT:
  not established

PRE_PROTOCOL_BOUNDARY_ATTACKS:
  0

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
  source_and_registry_recovery_complete

PROTOCOL_REVISION_REQUIRED:
  not applicable before protocol

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 10. Next

Create the Computation planning/worklog lane and then draft Task Interface v0.1 from this recovery artifact.

Do not freeze a Computation protocol before direct boundary attack.
