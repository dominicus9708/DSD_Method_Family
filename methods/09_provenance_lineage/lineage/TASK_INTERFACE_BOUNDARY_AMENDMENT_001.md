# DSD Lineage Task Interface Boundary Amendment 001

Status: **PROSPECTIVE AMENDMENT ESTABLISHED**  
Date: **2026-09-23**  
Method: **Lineage / DSD 계보론**

Historical inputs preserved:

- `TASK_INTERFACE_v0.1-draft.md`
- `BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`

This amendment does not rewrite the historical Task Interface.

It prospectively binds the nonbreaking refinements forced by the 18 pre-protocol boundary attacks and authorizes executable Lineage Protocol v0.1 only after this amendment is frozen.

## 1. Amendment purpose

The historical Task Interface correctly preserves the source Dynamics distinction between:

```text
literal equality
tracking continuity
numerical or aggregate similarity
secondary diagnostics
and
predecessor/successor lineage identity
```

The boundary attacks show that an executable protocol additionally requires exact operational rules for:

```text
identity-bearing-family selection provenance
family-coherence status
evaluated absence versus unavailable interface
multi-input auxiliary lineage
self-time / composition-coherence consequences
task-terminal precedence
```

The following eight refinement groups are binding for Lineage Protocol v0.1.

## 2. R1 — task, claim level, time direction, scope, and identity-bearing-family lock

Every executable Lineage task freezes before lineage evaluation:

```text
LINEAGE_TASK_ID
TASK_VERSION

LINEAGE_CLAIM_LEVEL
  CHANNEL_LINEAGE
  COMPONENT_LINEAGE
  STATE_SUCCESSION
  INTERVAL_IDENTITY_PRESERVATION

SOURCE_TIME_OR_EPOCH
TARGET_TIME_OR_EPOCH
TIME_DIRECTION

DECLARED_LINEAGE_SCOPE
REQUIRED_LINEAGE_QUERY_OR_OBLIGATION_SET
TASK_SCOPE_VERSION
```

For state- or interval-level identity questions, also freeze:

```text
IDENTITY_BEARING_FAMILY_ID
IDENTITY_BEARING_FAMILY_VERSION
IDENTITY_BEARING_FAMILY_PROVENANCE
IDENTITY_BEARING_FAMILY_SELECTION_RULE_OR_JUSTIFICATION
IDENTITY_BEARING_COMPONENT_SET_BY_TIME
```

The identity-bearing family must be selected before claim evaluation.

Changing the family after seeing a preferred result requires a new task version.

```text
POST_HOC_IDENTITY_BEARING_SELECTION != VALID_LINEAGE_EVALUATION
```

The amendment does not define a universal rule for which components must bear identity.

That designation remains supplied additional dynamical/application data.

## 3. R2 — predecessor/successor identity, type, formation, and status discipline

Every claim-relevant predecessor or successor record must preserve, where relevant:

```text
LINEAGE_OBJECT_ID
OBJECT_VERSION_IF_RELEVANT
OBJECT_TYPE
FORMATION_BACKGROUND_ID_OR_DESCRIPTOR
CHANNEL_TAG_OR_CHANNEL_ID_IF_RELEVANT
COMPONENT_TYPE_IF_RELEVANT
DECLARED_STATUS
IDENTITY_RECORD_PROVENANCE
OPTIONAL_HUMAN_READABLE_LABEL
```

Labels, filenames, names, numerical values, or reduced readouts are not sufficient identity keys.

```text
SAME_LABEL != SAME_ENTITY
SAME_VALUE != SAME_ENTITY
SAME_AGGREGATE != SAME_ENTITY
```

A candidate component-lineage relation that violates required declared types or inherited channel compatibility is not admissible merely because the objects are similar.

## 4. R3 — fixed-background canonical lineage versus transition lineage

When the frozen task establishes that all relevant times lie in one regular epoch with the same inherited Stage-VI formation background and fixed admitted channel family, Protocol v0.1 may use the source-defined canonical channel-lineage identity relation.

Prospectively:

```text
FIXED_BACKGROUND_CANONICAL_CHANNEL_LINEAGE:
  permitted only when its source preconditions are established
```

This canonical channel relation does not by itself establish component- or state-level succession.

Across a formation-level transition or a change in inherited channel identity:

```text
CANONICAL_FIXED_BACKGROUND_IDENTITY:
  not automatically transferable
```

A cross-transition successor claim then requires an admissible supplied lineage relation or other explicitly authorized lineage handoff.

```text
FORMATION_TRANSITION != AUTOMATIC_SUCCESSION
CHANNEL_CHANGE != AUTOMATIC_SUCCESSION
```

## 5. R4 — lineage-family coherence and direct-long-interval separation

Protocol v0.1 must record a family-level status whenever coherence is claim-relevant.

Prospective status family:

```text
LINEAGE_FAMILY_COHERENT
LINEAGE_FAMILY_INCOHERENT
LINEAGE_FAMILY_BLOCKED
LINEAGE_FAMILY_CONFLICTING
LINEAGE_FAMILY_OUT_OF_SCOPE
LINEAGE_FAMILY_UNDERDETERMINED
```

A supplied channel- or component-lineage family is `LINEAGE_FAMILY_COHERENT` only when all required frozen checks pass.

At minimum:

```text
SELF_TIME_IDENTITY_CHECK:
  relation at t,t equals the identity relation on the declared set

COMPOSITION_INCLUSION_CHECK:
  shorter-interval composition is a subset of the supplied
  direct long-interval lineage relation
```

For component lineage, coherence additionally preserves declared component types and inherited channel-lineage compatibility.

If self-time identity or required composition inclusion is evaluably violated:

```text
LINEAGE_FAMILY_COHERENCE_STATUS:
  LINEAGE_FAMILY_INCOHERENT
```

This means the claimed coherent-family property is not established.

It does not retroactively erase every pairwise relation record.

Direct long-interval lineage remains independently recorded.

```text
COMPOSED_INTERMEDIATE_RELATION
  !=
DIRECT_LONG_INTERVAL_RELATION_BY_DEFAULT
```

A stricter application may separately require equality, single-valuedness, or another stronger condition.

## 6. R5 — component lineage, auxiliary lineage, and identity-bearing coverage

For component-level claims, Protocol v0.1 must preserve:

```text
COMPONENT_TYPE
INHERITED_CHANNEL_TAG_OR_CHANNEL_ID
DECLARED_MULTI_INPUT_SORTS
REQUIRED_AUXILIARY_LINEAGE_SET
SUPPLIED_AUXILIARY_LINEAGE_RECORDS
```

If a claim explicitly requires lineage for an auxiliary input sort and the required lineage interface is unavailable:

```text
REQUIRED_AUXILIARY_LINEAGE_UNAVAILABLE
  -> LINEAGE_SUCCESSOR_BLOCKED
```

for the dependent component claim.

If that blocked component claim is required for a state- or interval-level claim, the higher-level task is blocked unless another frozen rule explicitly removes that dependency.

The evaluator may not silently ignore the missing auxiliary lineage.

For state succession, Protocol v0.1 must separately check:

```text
PREDECESSOR_TO_SUCCESSOR_COVERAGE
SUCCESSOR_TO_PREDECESSOR_COVERAGE
```

Both must pass for the state-succession proposition to be established.

An evaluable coverage failure yields:

```text
STATE_SUCCESSION:
  NOT_ESTABLISHED
```

not `BLOCKED`.

## 7. R6 — branching, merging, and optional stronger constraints

Base Lineage permits relation-valued succession including branching and merging when supported by admissible lineage data.

```text
ONE_PREDECESSOR_TO_MULTIPLE_SUCCESSORS:
  allowed

MULTIPLE_PREDECESSORS_TO_ONE_SUCCESSOR:
  allowed
```

The following are optional stronger application constraints only when explicitly declared:

```text
UNIQUE_SUCCESSOR_REQUIREMENT
BIJECTIVE_COMPONENT_TRANSPORT_REQUIREMENT
CARDINALITY_CONSERVATION_REQUIREMENT
OTHER_DECLARED_LINEAGE_CONSTRAINT
```

Each receives a separate status.

```text
OPTIONAL_CONSTRAINT_SATISFIED
OPTIONAL_CONSTRAINT_UNSATISFIED
OPTIONAL_CONSTRAINT_BLOCKED
OPTIONAL_CONSTRAINT_OUT_OF_SCOPE
OPTIONAL_CONSTRAINT_UNDERDETERMINED
```

Failure of an optional stronger constraint does not erase an otherwise established base lineage relation.

```text
BRANCHING != PROTOCOL_FAILURE
MERGING != PROTOCOL_FAILURE
BASE_LINEAGE != UNIQUE_SUCCESSOR_BY_DEFAULT
BASE_LINEAGE != BIJECTION_BY_DEFAULT
BASE_LINEAGE != CARDINALITY_CONSERVATION_BY_DEFAULT
```

## 8. R7 — exact successor-status semantics

Protocol v0.1 uses the following methodology-level status family:

```text
LINEAGE_SUCCESSOR_ESTABLISHED
LINEAGE_SUCCESSOR_EXPLICITLY_NEGATED
LINEAGE_SUCCESSOR_NOT_ESTABLISHED
LINEAGE_SUCCESSOR_AMBIGUOUS
LINEAGE_SUCCESSOR_CONFLICTING
LINEAGE_SUCCESSOR_BLOCKED
LINEAGE_SUCCESSOR_INAPPLICABLE
LINEAGE_SUCCESSOR_OUT_OF_SCOPE
LINEAGE_SUCCESSOR_UNDERDETERMINED
```

Semantics:

```text
ESTABLISHED
  the source-defined canonical condition or supplied admissible
  lineage relation supports the directed successor claim.

EXPLICITLY_NEGATED
  supplied applicable evidence or a frozen domain rule explicitly
  excludes the directed successor claim.
  Mere absence is insufficient.

NOT_ESTABLISHED
  the required in-scope lineage interface is available and evaluable,
  but the requested successor claim is not supported or a required
  evaluable coverage/coherence condition for that claim fails.

AMBIGUOUS
  a claim-relevant predecessor, successor, component, identity-bearing
  family member, type, or relation target is not uniquely identified.

CONFLICTING
  applicable supplied lineage records assert mutually incompatible
  outcomes under the same frozen identity/scope/semantics and no
  frozen precedence resolves them.

BLOCKED
  evaluation cannot proceed because a required lineage relation,
  identity-bearing-family record, component-type map, auxiliary-lineage
  relation, formation/transition record, schema, decoder, or handoff
  is absent or unavailable.

INAPPLICABLE
  the requested lineage relation does not apply to the declared
  object types or claim level.

OUT_OF_SCOPE
  the requested relation or identity question lies outside the
  frozen Lineage task.

UNDERDETERMINED
  multiple admissible lineage mappings, identity-bearing selections
  already frozen by the task, or relation semantics yield different
  claim-relevant outcomes and no frozen rule resolves them.
```

The boundary forced by B6 and B11 is therefore:

```text
EVALUABLE_ABSENCE_OR_EVALUABLE_FAILURE
  -> NOT_ESTABLISHED

UNAVAILABLE_REQUIRED_INTERFACE
  -> BLOCKED
```

Required guards:

```text
NOT_ESTABLISHED != EXPLICITLY_NEGATED
NOT_ESTABLISHED != BLOCKED
AMBIGUOUS != CONFLICTING
CONFLICTING != UNDERDETERMINED
INAPPLICABLE != OUT_OF_SCOPE
```

## 9. R8 — neighboring-method handoffs and diagnostic non-substitution

Lineage may consume typed handoffs from:

```text
Formation / Property
Dynamics
Tracking
Reconstruction
Transformation
Comparison
Classification
Aggregation / Compression
Measurement
Interpretation
Audit
other declared domain methods
```

but the handoff does not authorize Lineage to silently perform the neighboring method.

Required guards:

```text
TRACKING_LINK != LINEAGE_SUCCESSOR_DECISION
TRACE_CONTINUITY != LINEAGE_IDENTITY

RECONSTRUCTED_LINEAGE_CANDIDATE != ESTABLISHED_LINEAGE

TRANSFORMATION_MAPPING != SUCCESSOR_IDENTITY
COMPARISON_SIMILARITY != SUCCESSOR_IDENTITY
CLASS_MEMBERSHIP != INDIVIDUAL_SUCCESSOR_IDENTITY

AGGREGATE_EQUALITY != LINEAGE_IDENTITY
AGGREGATE_INEQUALITY != LINEAGE_NONIDENTITY

RANK_EQUALITY != LINEAGE_IDENTITY
RANK_CHANGE != LINEAGE_COLLAPSE

ENTROPY_OR_STABILITY_DIAGNOSTIC
  !=
PRIMARY_IDENTITY_CRITERION
```

A secondary diagnostic is recorded in a sidecar and may not create lineage.

## 10. Task-level terminal obligations

Protocol v0.1 must emit exactly one task-level terminal:

```text
LINEAGE_TASK_ESTABLISHED
LINEAGE_TASK_PARTIAL
LINEAGE_TASK_NOT_ESTABLISHED
LINEAGE_TASK_BLOCKED
LINEAGE_TASK_CONFLICTING
LINEAGE_TASK_OUT_OF_SCOPE
LINEAGE_TASK_UNDERDETERMINED
```

Prospective semantics:

```text
ESTABLISHED
  every required in-scope lineage obligation for the frozen claim
  is established and every required coherence/coverage condition passes.

PARTIAL
  the task contains multiple required lineage obligations;
  at least one is established and at least one other evaluable
  obligation is not established, while no higher-priority terminal
  below dominates.
  PARTIAL is not used to rescue a single state-succession proposition
  whose required bidirectional coverage fails.

NOT_ESTABLISHED
  the requested in-scope lineage proposition is evaluable but is not
  established, including explicit negation, absent admissible relation,
  evaluable type incompatibility, or failed required coverage/coherence.

BLOCKED
  at least one required in-scope lineage obligation cannot be evaluated
  because a required interface/handoff/identity-bearing/auxiliary record
  is unavailable.

CONFLICTING
  applicable required lineage records make mutually incompatible claims
  under the same frozen scope/semantics.

OUT_OF_SCOPE
  the requested operation is not a Lineage task or lies outside the
  frozen lineage scope.

UNDERDETERMINED
  multiple admissible claim-relevant lineage mappings or semantics
  produce different task outcomes with no frozen resolver.
```

Terminal precedence for one frozen run is:

```text
OUT_OF_SCOPE
-> CONFLICTING
-> UNDERDETERMINED
-> BLOCKED
-> ESTABLISHED / PARTIAL / NOT_ESTABLISHED
```

This precedence selects only the run summary.

It does not erase relation-level, family-level, coverage, or optional-constraint statuses.

## 11. Maximum-supported-claim discipline

A conformant Lineage result may assert only what the frozen claim level and supplied lineage interface support.

Protocol v0.1 must not silently upgrade a Lineage result into:

```text
literal equality
truth or authenticity
causality
correctness of a Transformation
Tracking completeness
reconstructed history truth
empirical or legal identity
Audit conformance
external-domain validity
unique successor
bijection
cardinality conservation
```

unless the corresponding stronger claim is separately supplied and validated by its own method/domain interface.

## 12. Prospective protocol obligations

Lineage Protocol v0.1 must contain:

```text
task / claim-level / time-direction / scope lock

identity-bearing-family ID/version/provenance/selection lock

predecessor/successor identity/type/formation/status register

fixed-background canonical-lineage gate

transition-lineage gate

channel/component lineage relation ledgers

lineage-family coherence status
self-time identity check
composition-inclusion check
direct-long-interval ledger

multi-input auxiliary-lineage obligations

state bidirectional-coverage record

branch / merge ledger

optional uniqueness / bijection / cardinality ledger

successor-status family
task-terminal semantics and precedence

neighboring-method handoff ledger
secondary-diagnostic sidecar

conformance record
method-gain record
maximum-supported-claim record
```

## 13. Amendment result

```text
BOUNDARY_AMENDMENT_001: established
REFINEMENT_GROUPS_ADOPTED: 8/8

HISTORICAL_TASK_INTERFACE_REWRITTEN: no
HISTORICAL_BOUNDARY_ATTACK_RECORD_REWRITTEN: no

BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0

PROTOCOL_FREEZE_AUTHORIZED: yes

DIRECT_LINEAGE_PILOTS_ATTEMPTED: 0
EXTERNAL_APPLICATION: no

SHARED_CORE_REOPEN_REQUIRED: no
```

Next: freeze executable Lineage Protocol v0.1 from the historical Task Interface plus this amendment.
