# DSD Lineage Task Interface v0.1 — historical draft

Status: **draft established / pre-protocol boundary attack next**  
Date: **2026-09-23**  
Method: **Lineage / DSD 계보론**  
Higher field: **IV. Evidence & Lineage / 증거·계보**

## 1. Source lock

This Task Interface is grounded in the current DSD Structural Reorganization Dynamics interface, especially:

```text
Section 4.1  lineage as additional cross-time data
Section 4.2  channel-lineage relation and coherent family
Section 4.3  canonical fixed-background lineage
Section 4.4  component-lineage relation and coherence
Section 4.5  lineage-connected component/state succession
Section 12.1 lineage identity preservation as the primary identity criterion
Section 12.2 secondary diagnostics do not create lineage
Section 17.7 finite lineage branching
```

The method-family interface operationalizes those distinctions for repeatable tasks.
It does not replace or silently strengthen the source definitions.

## 2. Task identity

DSD Lineage receives a declared predecessor/successor or identity-preservation question across one or more ordered times, the relevant formation/channel/component records, supplied candidate lineage relations, and the evidence or handoffs that authorize those relations.

It returns a typed record of which predecessor-successor claims are established, explicitly negated, not established, ambiguous, conflicting, blocked, inapplicable, out of scope, or underdetermined under the frozen task.

Lineage decides **succession identity across change**.

It does not infer identity from label continuity, numerical similarity, temporal adjacency, trace continuity, equal aggregates, equal rank, small entropy change, or another diagnostic alone.

## 3. Required task inputs

```text
LINEAGE_TASK_ID
TASK_VERSION

LINEAGE_CLAIM_LEVEL
  one of:
    CHANNEL_LINEAGE
    COMPONENT_LINEAGE
    STATE_SUCCESSION
    INTERVAL_IDENTITY_PRESERVATION

SOURCE_TIME_OR_EPOCH
TARGET_TIME_OR_EPOCH
TIME_DIRECTION

DECLARED_LINEAGE_SCOPE
DECLARED_PREDECESSOR_SET
DECLARED_SUCCESSOR_SET

SOURCE_FORMATION_BACKGROUND_OR_IDENTITY_RECORD
TARGET_FORMATION_BACKGROUND_OR_IDENTITY_RECORD

CANDIDATE_LINEAGE_RELATION_SET
LINEAGE_RELATION_TYPE_AND_DIRECTION
LINEAGE_RELATION_PROVENANCE
```

For state-succession or interval-identity tasks, the following is required:

```text
IDENTITY_BEARING_COMPONENT_FAMILY
```

and it must be nonempty at every relevant time for which the state-identity claim is evaluated.

## 4. Conditionally required inputs

```text
REGULAR_EPOCH_RECORD
REGULAR_SUPPORT_SIGNATURE

CHANNEL_SET_C(t)
CHANNEL_LINEAGE_RELATION_LAMBDA_s_t

COMPONENT_SET_Xcmp(t)
COMPONENT_LINEAGE_RELATION_L_s_t

COMPONENT_TYPE_RECORD
INHERITED_CHANNEL_TAG_RECORD
MULTI_INPUT_SORT_RECORD

TRANSITION_CLASS_RECORD
FORMATION_LEVEL_TRANSITION_RECORD
STATUS_OR_DOMAIN_TRANSITION_RECORD

DIRECT_LONG_INTERVAL_LINEAGE_RECORD
INTERMEDIATE_LINEAGE_RELATIONS

UNIQUE_SUCCESSOR_REQUIREMENT
BIJECTIVE_COMPONENT_TRANSPORT_REQUIREMENT
CARDINALITY_CONSERVATION_REQUIREMENT
OTHER_DECLARED_LINEAGE_CONSTRAINTS

TRACKING_HANDOFF
RECONSTRUCTION_HANDOFF
TRANSFORMATION_HANDOFF
COMPARISON_OR_SIMILARITY_RECORD
AGGREGATION_OR_COMPRESSION_SIDECAR
DYNAMIC_DIAGNOSTIC_RECORD
CONFLICT_OR_PRECEDENCE_POLICY
```

An optional handoff becomes required only when the frozen claim depends on it.

## 5. Source-derived relation semantics

For channel lineage between admitted channel sets at times (s \le t):

```text
Lambda_s_t subset C(s) x C(t)
```

A pair in the relation means only that the target channel is declared an admissible successor of the source channel.
It does not mean literal equality of the Stage-VI tuples.

A coherent channel-lineage family preserves:

```text
Lambda_t_t = identity relation on C(t)

Lambda_s_t o Lambda_r_s
  subset
Lambda_r_t
for r <= s <= t
```

For component lineage:

```text
L_s_t subset Xcmp(s) x Xcmp(t)
```

and a coherent component-lineage family preserves:

```text
L_t_t = identity relation on Xcmp(t)

L_s_t o L_r_s
  subset
L_r_t
```

together with declared component types and compatibility with supplied channel lineage on inherited channel-tag coordinates.

The inclusion rule does not authorize replacing a supplied direct long-interval relation by equality with the composed intermediate relation.

## 6. Canonical fixed-background channel lineage

When the frozen task establishes that all relevant times lie in one regular epoch with the same inherited Stage-VI formation background and fixed admitted channel family (C_L), the canonical channel-lineage relation is the identity relation on that fixed channel family.

This canonical rule is limited to the channel identity inherited on the fixed formation background.

It does not automatically establish:

```text
component-level succession
state-level succession
identity-bearing-family selection
unique successor
bijective component transport
cardinality conservation
```

unless those claims are separately supported.

Across a formation-level transition, fixed-background identification is no longer automatic.

## 7. Binding operation

Lineage must:

```text
1 lock task identity, task version, claim level, source/target times,
  time direction, and declared lineage scope;

2 lock predecessor and successor identifiers, types, formation identities,
  channel identities, and supplied status distinctions;

3 determine whether the claim lies within one fixed-background regular epoch
  or crosses a status/domain or formation-level transition;

4 use the canonical fixed-background channel relation only when its
  preconditions are actually satisfied;

5 otherwise admit predecessor-successor relations only from supplied
  lineage relations or explicit method/domain handoffs that authorize them;

6 check relation typing and direction before treating a pair as a
  candidate successor relation;

7 for a claimed coherent family, check self-time identity and
  composition-inclusion obligations over the supplied time set;

8 preserve direct long-interval lineage information separately from
  relations obtained by composition through intermediate times;

9 for component lineage, preserve declared component types,
  multi-input sorts, inherited channel-tag compatibility, and any
  required auxiliary-input lineage;

10 for state succession, use the supplied nonempty identity-bearing
   component families and check predecessor-to-successor and
   successor-to-predecessor coverage;

11 allow branching and merging unless the task separately declares
   uniqueness, bijectivity, or cardinality conservation;

12 evaluate separately any declared uniqueness, bijectivity, or
   cardinality constraints rather than treating them as universal
   lineage requirements;

13 keep literal equality, similarity, aggregate equality,
   rank equality, entropy/stability diagnostics, labels, and temporal
   adjacency separate from lineage identity;

14 record Tracking, Reconstruction, Transformation, Comparison,
   Aggregation/Compression, Dynamics, and Audit handoffs without
   silently replacing Lineage with those neighboring methods;

15 emit relation-level status, family/coherence status,
   state-coverage status, optional-constraint status,
   task terminal, conformance, method-gain, and maximum-claim records.
```

## 8. Lineage-successor status family

The following status family is methodology-level bookkeeping for executing Lineage tasks.
It does not add a new foundational DSD axiom.

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

Interpretation:

```text
ESTABLISHED
  the frozen lineage interface or supplied admissible relation supports
  the claimed directed succession.

EXPLICITLY_NEGATED
  supplied applicable evidence or a frozen domain rule explicitly
  excludes the claimed succession.
  Mere absence of a lineage relation is insufficient.

NOT_ESTABLISHED
  the evaluator can inspect the required in-scope lineage data but the
  requested succession is not supported.

AMBIGUOUS
  a claim-relevant predecessor, successor, type, identity-bearing
  component, or relation target is not uniquely identified.

CONFLICTING
  applicable supplied lineage records make mutually incompatible
  claims under the same frozen scope and relation semantics.

BLOCKED
  evaluation cannot proceed because a required lineage relation,
  identity-bearing family, type map, formation/transition record,
  schema, or handoff is unavailable.

INAPPLICABLE
  the requested lineage relation does not apply to the declared
  source/target types or claim level.

OUT_OF_SCOPE
  the requested relation or identity claim lies outside the frozen task.

UNDERDETERMINED
  multiple admissible lineage mappings or lineage semantics produce
  different claim-relevant outcomes and no frozen precedence resolves them.
```

Required guards:

```text
NOT_ESTABLISHED != EXPLICITLY_NEGATED
AMBIGUOUS != CONFLICTING
CONFLICTING != UNDERDETERMINED
BLOCKED != NOT_ESTABLISHED
INAPPLICABLE != OUT_OF_SCOPE
```

## 9. State-succession coverage

For a state-level question with supplied identity-bearing families (I(s)) and (I(t)), state succession is established only when:

```text
every predecessor identity-bearing component in I(s)
  has at least one successor in I(t)

and

every successor identity-bearing component in I(t)
  has at least one predecessor in I(s)
```

through the supplied coherent component-lineage relation.

This is a coverage condition.

It does not require a one-to-one map.

```text
STATE_SUCCESSION != LITERAL_STATE_EQUALITY
STATE_SUCCESSION != BIJECTION_BY_DEFAULT
STATE_SUCCESSION != EQUAL_CARDINALITY_BY_DEFAULT
```

## 10. Interval identity preservation

For an interval-level identity claim, the source Dynamics interface requires lineage-connected state succession for every ordered pair of relevant times under the coherent lineage family and the supplied identity-bearing component family.

A secondary stability or entropy diagnostic may be recorded, but it does not create or replace the primary lineage criterion.

```text
SMALL_DIAGNOSTIC_CHANGE != LINEAGE_IDENTITY
LOW_ENTROPY_RATE != LINEAGE_IDENTITY
RANK_EQUALITY != LINEAGE_IDENTITY
RANK_CHANGE != AUTOMATIC_LINEAGE_COLLAPSE
```

## 11. Branching, merging, and optional stronger constraints

Branching and merging are admissible Lineage structures when supported by the supplied relation.

```text
ONE_PREDECESSOR -> MULTIPLE_SUCCESSORS
  allowed unless a unique-successor rule is separately declared

MULTIPLE_PREDECESSORS -> ONE_SUCCESSOR
  allowed unless a separate constraint forbids it
```

A declared stronger constraint is recorded independently:

```text
UNIQUE_SUCCESSOR_STATUS
BIJECTIVE_TRANSPORT_STATUS
CARDINALITY_CONSERVATION_STATUS
OTHER_LINEAGE_CONSTRAINT_STATUS
```

Failure of one optional stronger constraint does not retroactively erase a base lineage relation that is otherwise supported.

## 12. Task-level terminal status family

```text
LINEAGE_TASK_ESTABLISHED
LINEAGE_TASK_PARTIAL
LINEAGE_TASK_NOT_ESTABLISHED
LINEAGE_TASK_BLOCKED
LINEAGE_TASK_CONFLICTING
LINEAGE_TASK_OUT_OF_SCOPE
LINEAGE_TASK_UNDERDETERMINED
```

A task terminal summarizes the frozen lineage question.

It is distinct from:

```text
protocol conformance
truth/authenticity
causality
Transformation correctness
Tracking completeness
Audit success
external-domain validity
```

## 13. Outputs

```text
LOCKED_LINEAGE_TASK_AND_SCOPE

PREDECESSOR_SUCCESSOR_REGISTER
FORMATION_AND_EPOCH_LEDGER
CHANNEL_LINEAGE_RELATION_LEDGER
COMPONENT_LINEAGE_RELATION_LEDGER

LINEAGE_RELATION_PROVENANCE_LEDGER
LINEAGE_SUCCESSOR_STATUS_LEDGER

COHERENCE_SELF_TIME_LEDGER
COHERENCE_COMPOSITION_LEDGER
DIRECT_LONG_INTERVAL_LINEAGE_LEDGER

IDENTITY_BEARING_COMPONENT_LEDGER
STATE_SUCCESSION_COVERAGE_LEDGER
INTERVAL_IDENTITY_PRESERVATION_LEDGER

BRANCH_MERGE_LEDGER
OPTIONAL_UNIQUENESS_BIJECTION_CARDINALITY_LEDGER

NEIGHBORING_METHOD_HANDOFF_LEDGER
SECONDARY_DIAGNOSTIC_SIDECAR

LINEAGE_TASK_TERMINAL_STATUS
LINEAGE_PROTOCOL_CONFORMANCE
LINEAGE_METHOD_GAIN_STATUS
MAXIMUM_SUPPORTED_CLAIM
```

## 14. Core guards

```text
SUCCESSOR_RELATION != LITERAL_EQUALITY

SAME_LABEL != SAME_ENTITY
TEMPORAL_ADJACENCY != LINEAGE
TRACE_CONTINUITY != LINEAGE_IDENTITY
VERSION_CONTINUITY != LINEAGE_IDENTITY

NUMERICAL_SIMILARITY != LINEAGE_IDENTITY
AGGREGATE_EQUALITY != LINEAGE_IDENTITY
AGGREGATE_INEQUALITY != LINEAGE_NONIDENTITY
RANK_EQUALITY != LINEAGE_IDENTITY
RANK_CHANGE != LINEAGE_COLLAPSE
ENTROPY_OR_STABILITY_DIAGNOSTIC != PRIMARY_IDENTITY_CRITERION

FORMATION_TRANSITION != AUTOMATIC_SUCCESSION
CHANNEL_CHANGE != AUTOMATIC_SUCCESSION

BRANCHING != PROTOCOL_FAILURE
MERGING != PROTOCOL_FAILURE
LINEAGE_RELATION != UNIQUE_SUCCESSOR_BY_DEFAULT
LINEAGE_RELATION != BIJECTION_BY_DEFAULT
LINEAGE_RELATION != CARDINALITY_CONSERVATION_BY_DEFAULT

COMPOSED_INTERMEDIATE_RELATION != DIRECT_LONG_INTERVAL_RELATION_BY_DEFAULT

TRACKING_LINK != LINEAGE_SUCCESSOR_DECISION
RECONSTRUCTED_LINEAGE_CANDIDATE != ESTABLISHED_LINEAGE
TRANSFORMATION_MAPPING != SUCCESSOR_IDENTITY
COMPARISON_SIMILARITY != SUCCESSOR_IDENTITY

NOT_ESTABLISHED != EXPLICITLY_NEGATED
```

## 15. Failure / no-gain criteria

Protocol nonconformance includes:

```text
changing the identity question or identity-bearing family after seeing
  a preferred lineage outcome;

merging distinct predecessor/successor objects by label alone;

treating temporal adjacency or Tracking continuity as successor identity;

using fixed-background canonical identity across a formation-level
  transition whose inherited channel identity changed;

accepting a type-incompatible component-lineage relation;

claiming coherent-family status while violating self-time identity
  or composition inclusion;

replacing direct long-interval lineage by equality with composed
  intermediate lineage without a declared stronger rule;

claiming state succession when one direction of identity-bearing
  coverage fails;

rejecting branching or merging merely because the relation is not
  one-to-one;

silently treating uniqueness, bijection, or cardinality conservation
  as universal requirements;

using aggregate equality/inequality, numerical similarity, rank,
  entropy rate, or another secondary diagnostic as the primary
  lineage criterion;

promoting a Reconstruction candidate to established lineage without
  the required handoff/evidence;

treating a lineage result as proof of causality, correctness,
  authenticity, or Audit conformance.
```

`NO_GAIN` is allowed when a fair non-DSD typed relation/identity evaluator receives the same predecessor/successor identities, formation/transition records, relation data, component types, identity-bearing families, constraints, and provenance and produces the same claim-relevant result.

```text
NO_GAIN != METHOD_FAILURE
CASE_FAIL != METHOD_DELETION_PROOF
```

## 16. Method boundaries

```text
Tracking:
  records supported origin/version/process/location/reference/evidence links.
  Lineage decides predecessor/successor identity across change.

Dynamics:
  supplies regular epochs, transition classes, and foundational lineage
  primitives. Lineage method execution evaluates a declared identity question;
  it does not derive a constitutive evolution law or causal mechanism.

Reconstruction:
  may infer compatible missing/past lineage candidates.
  A reconstructed candidate is not established lineage by itself.

Transformation:
  characterizes source-to-target mapping and preservation/loss.
  A valid mapping does not by itself decide successor identity.

Comparison:
  evaluates similarities and differences.
  Similarity does not establish lineage; difference does not automatically
  destroy lineage.

Aggregation / Compression:
  may supply reduced readouts.
  Equality or inequality of reduced readouts is not the primary lineage criterion.

Classification:
  may assign the same or different class labels.
  Class membership does not decide individual predecessor/successor identity.

Audit:
  evaluates conformance to criteria.
  Lineage emits a lineage result but does not replace a general Audit.
```

## 17. Internal validation standard

An internal Lineage run is checked against the frozen task by verifying:

```text
task / claim-level / time-direction / scope lock

predecessor and successor identity/type lock

regular-epoch versus transition classification

canonical fixed-background rule preconditions where used

lineage relation provenance

relation direction and type compatibility

self-time identity and composition-inclusion coherence where claimed

component type and inherited-channel compatibility

identity-bearing family nonemptiness

bidirectional state-succession coverage

branch / merge preservation

optional uniqueness / bijection / cardinality constraints kept separate

neighboring-method handoff discipline

secondary-diagnostic non-substitution

task terminal and conformance

bounded maximum-supported claim
```

External historical, biological, legal, provenance-authentication, causal, or empirical identity standards are not established by this draft.

## 18. Current draft state

```text
DEDICATED_LINEAGE_PROTOCOL: not established
TASK_INTERFACE_DRAFT: v0.1 established

PRE_PROTOCOL_BOUNDARY_ATTACKS: 0

DIRECT_LINEAGE_PILOTS_ATTEMPTED: 0
BASELINE_LINEAGE_CASES: 0
NO_GAIN_LINEAGE_CASES: 0
REPRODUCIBILITY_CASES: 0

EXTERNAL_LINEAGE_APPLICATIONS: 0
INDEPENDENT_LINEAGE_VALIDATION: not established
INDEPENDENT_REPLICATION: not established

LINEAGE_INTERNAL_STANDARDIZATION_STATUS: developing
CURRENT_LINEAGE_EVIDENCE_STATUS: task_interface_draft

PROTOCOL_REVISION_REQUIRED: not applicable pre-protocol
SHARED_CORE_REOPEN_REQUIRED: no
```

Next: perform a pre-protocol boundary attack before freezing any executable Lineage protocol.
