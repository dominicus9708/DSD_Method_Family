# DSD Lineage Protocol v0.1

Status: **FROZEN EXECUTABLE INTERNAL PROTOCOL**  
Date: **2026-09-23**  
Method: **Lineage / DSD 계보론**

Protocol lineage:

```text
TASK_INTERFACE_v0.1-draft.md
  commit: e233916530e8824427411d070ba0881160648618
  blob:   05cdbe5ff0c408b044b699d0d3b261d3fca4ab4b

BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md
  commit: 3a8e860b7ea04eb321bb10c99922b224a58ff3dd
  blob:   26b53e26aa41ca3236afc7fdba0a620428133a66

TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
  commit: a448ac1ab49faddb97968ff5987d3c75ac77b6e0
  blob:   35568d0a27a8537347600efff87064b6b4ad177f
```

This protocol freezes the project-internal operational semantics of DSD Lineage.

It operationalizes the current DSD Structural Reorganization Dynamics lineage interface without replacing or strengthening the source definitions.

It does not establish literal equality, truth, authenticity, causality, Transformation correctness, Tracking completeness, reconstructed-history truth, empirical/legal identity, Audit success, external validity, unique succession, bijection, or cardinality conservation unless separately supplied by the corresponding method/domain interface.

## 1. Method form

An executable Lineage task has the form:

```text
(
  lineage task identity/version,
  claim level,
  source/target time or epoch,
  time direction,
  bounded lineage scope,
  required lineage queries/obligations,

  typed predecessor/successor records,
  formation/background records,

  channel/component lineage relations,
  relation provenance,

  optional regular-epoch / transition records,

  optional identity-bearing component family,
  optional auxiliary-lineage requirements,

  optional uniqueness / bijection / cardinality constraints,

  optional neighboring-method handoffs,
  optional secondary diagnostics
)
->
(
  locked task/scope record,

  predecessor/successor register,
  formation/epoch ledger,

  channel/component lineage relation ledgers,
  successor-status ledger,

  family-coherence record,
  self-time identity record,
  composition-inclusion record,
  direct-long-interval record,

  identity-bearing-family ledger,
  state-succession coverage ledger,
  interval-identity record,

  branch/merge ledger,
  optional-constraint ledger,

  neighboring-method handoff ledger,
  secondary-diagnostic sidecar,

  task terminal,
  protocol conformance,
  method-gain status,
  maximum-supported-claim record
)
```

Lineage determines evidence-bounded predecessor/successor identity across change.

It does not manufacture a succession relation from continuity or similarity.

## 2. Source-layer discipline

Protocol v0.1 may consume, when supplied and claim-relevant:

```text
Formation:
  formation background,
  admitted channel identities,
  formation transitions.

Property:
  typed component/property records,
  multi-input sort information,
  applicability/status records.

Dynamics:
  regular epochs,
  transition classes,
  channel-lineage relations,
  component-lineage relations,
  coherent-family data,
  identity-bearing component families,
  lineage-connected succession records,
  secondary diagnostics.

Tracking:
  trace records and relation provenance.

Reconstruction:
  candidate missing/past lineage hypotheses.

Transformation:
  source-target mapping and preservation/loss records.

Comparison / Classification:
  similarity/difference or class records.

Aggregation / Compression:
  reduced readouts and loss sidecars.

Other methods/domains:
  explicitly typed lineage-relevant handoffs.
```

No optional source is mandatory unless the frozen claim depends on it.

Source roles remain distinct.

```text
TRACKING_TRACE != LINEAGE_DECISION
RECONSTRUCTION_CANDIDATE != ESTABLISHED_LINEAGE
TRANSFORMATION_MAPPING != SUCCESSOR_IDENTITY
AGGREGATE_READOUT != LINEAGE_IDENTITY
SECONDARY_DIAGNOSTIC != PRIMARY_LINEAGE_CRITERION
```

## 3. Required task record

Every executable run freezes:

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

DECLARED_PREDECESSOR_SET
DECLARED_SUCCESSOR_SET

SOURCE_FORMATION_BACKGROUND_OR_IDENTITY_RECORD
TARGET_FORMATION_BACKGROUND_OR_IDENTITY_RECORD

CANDIDATE_LINEAGE_RELATION_SET
LINEAGE_RELATION_TYPE_AND_DIRECTION
LINEAGE_RELATION_PROVENANCE
```

Conditionally required when claim-relevant:

```text
REGULAR_EPOCH_RECORD
REGULAR_SUPPORT_SIGNATURE

CHANNEL_SET_C(t)
CHANNEL_LINEAGE_RELATION_LAMBDA_s_t

COMPONENT_SET_Xcmp(t)
COMPONENT_LINEAGE_RELATION_L_s_t

COMPONENT_TYPE_RECORD
INHERITED_CHANNEL_TAG_RECORD
DECLARED_MULTI_INPUT_SORTS
REQUIRED_AUXILIARY_LINEAGE_SET
SUPPLIED_AUXILIARY_LINEAGE_RECORDS

TRANSITION_CLASS_RECORD
FORMATION_LEVEL_TRANSITION_RECORD
STATUS_OR_DOMAIN_TRANSITION_RECORD

DIRECT_LONG_INTERVAL_LINEAGE_RECORD
INTERMEDIATE_LINEAGE_RELATIONS

IDENTITY_BEARING_FAMILY_ID
IDENTITY_BEARING_FAMILY_VERSION
IDENTITY_BEARING_FAMILY_PROVENANCE
IDENTITY_BEARING_FAMILY_SELECTION_RULE_OR_JUSTIFICATION
IDENTITY_BEARING_COMPONENT_SET_BY_TIME

UNIQUE_SUCCESSOR_REQUIREMENT
BIJECTIVE_COMPONENT_TRANSPORT_REQUIREMENT
CARDINALITY_CONSERVATION_REQUIREMENT
OTHER_DECLARED_LINEAGE_CONSTRAINTS

TRACKING_HANDOFF
RECONSTRUCTION_HANDOFF
TRANSFORMATION_HANDOFF
COMPARISON_OR_CLASSIFICATION_HANDOFF
AGGREGATION_OR_COMPRESSION_SIDECAR
DYNAMIC_DIAGNOSTIC_RECORD
CONFLICT_OR_PRECEDENCE_POLICY
OTHER_TYPED_HANDOFFS
```

Required records may be explicitly absent.

The protocol distinguishes evaluable absence from unavailable required interface.

## 4. Claim-level gate

Before relation evaluation, assign exactly one frozen claim level.

```text
CHANNEL_LINEAGE
COMPONENT_LINEAGE
STATE_SUCCESSION
INTERVAL_IDENTITY_PRESERVATION
```

A lower-level established result does not automatically establish a higher-level result.

```text
CHANNEL_LINEAGE
  !=
COMPONENT_LINEAGE

COMPONENT_LINEAGE
  !=
STATE_SUCCESSION

STATE_SUCCESSION_AT_ONE_PAIR
  !=
INTERVAL_IDENTITY_PRESERVATION
```

If a task contains several independent claims, each receives its own query/obligation ID while the run still emits one overall terminal.

## 5. Identity descriptor

For every claim-relevant predecessor/successor object, record where applicable:

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

Human-readable labels, numerical values, aggregate values, filenames, or class labels do not replace identity records.

```text
SAME_LABEL != SAME_ENTITY
SAME_VALUE != SAME_ENTITY
SAME_AGGREGATE != SAME_ENTITY
SAME_CLASS != SAME_ENTITY
```

## 6. Fixed-background canonical channel-lineage gate

The source-defined canonical fixed-background channel lineage may be used only if the frozen task establishes:

```text
ONE_REGULAR_EPOCH
SAME_INHERITED_STAGE_VI_FORMATION_BACKGROUND
SAME_FIXED_ADMITTED_CHANNEL_FAMILY
CLAIM_LEVEL_INCLUDES_CHANNEL_LINEAGE
```

Then, for source and target times inside that epoch, the canonical channel relation is the identity relation on the fixed channel family.

This rule establishes only the channel-lineage relation licensed by the source condition.

It does not by itself establish:

```text
component succession
state succession
interval identity preservation
unique successor beyond identity relation scope
auxiliary component lineage
```

Across a formation-level transition or changed inherited channel identity, this gate is closed.

## 7. Transition-lineage gate

When fixed-background canonical lineage is unavailable, a successor relation is established only from:

```text
an admissible supplied lineage relation
or
an explicit lineage-authorizing handoff recognized by the frozen task
```

Temporal adjacency, a Tracking edge/path, version continuity, source-target transformation, numerical similarity, aggregate equality, class equality, rank equality, or a secondary diagnostic cannot by themselves satisfy this gate.

```text
FORMATION_TRANSITION != AUTOMATIC_SUCCESSION
TEMPORAL_ADJACENCY != LINEAGE
TRACE_CONTINUITY != LINEAGE_IDENTITY
```

## 8. Channel-lineage relation ledger

For each required channel-lineage query, record:

```text
LINEAGE_QUERY_ID
SOURCE_CHANNEL_ID
TARGET_CHANNEL_ID
SOURCE_TIME
TARGET_TIME
RELATION_SOURCE
RELATION_DIRECTION
RELATION_PROVENANCE
LINEAGE_SUCCESSOR_STATUS
```

The method treats the channel-lineage relation as directed and relation-valued.

A declared successor relation does not mean literal Stage-VI tuple equality.

## 9. Component-lineage relation ledger

For each required component-lineage query, record:

```text
LINEAGE_QUERY_ID
SOURCE_COMPONENT_ID
TARGET_COMPONENT_ID
SOURCE_COMPONENT_TYPE
TARGET_COMPONENT_TYPE
SOURCE_INHERITED_CHANNEL_TAG_IF_RELEVANT
TARGET_INHERITED_CHANNEL_TAG_IF_RELEVANT
DECLARED_MULTI_INPUT_SORTS_IF_RELEVANT
REQUIRED_AUXILIARY_LINEAGE_SET
SUPPLIED_AUXILIARY_LINEAGE_RECORDS
RELATION_SOURCE
RELATION_PROVENANCE
LINEAGE_SUCCESSOR_STATUS
```

An established component successor must preserve all required declared type and inherited-channel compatibility conditions from the supplied source interface.

For multi-input property or geometric data, all auxiliary lineage obligations explicitly required by the frozen claim must be evaluable.

```text
REQUIRED_AUXILIARY_LINEAGE_UNAVAILABLE
  -> LINEAGE_SUCCESSOR_BLOCKED
```

The protocol assumes no universal linear difference between related components.

## 10. Lineage-family coherence

When coherence is required, emit exactly one family status:

```text
LINEAGE_FAMILY_COHERENT
LINEAGE_FAMILY_INCOHERENT
LINEAGE_FAMILY_BLOCKED
LINEAGE_FAMILY_CONFLICTING
LINEAGE_FAMILY_OUT_OF_SCOPE
LINEAGE_FAMILY_UNDERDETERMINED
```

### 10.1 Self-time identity

For every relevant time t in the frozen family:

```text
relation(t,t)
  =
identity relation on the declared channel/component set at t
```

Any evaluable violation yields:

```text
LINEAGE_FAMILY_INCOHERENT
```

### 10.2 Composition inclusion

For every required ordered triple r <= s <= t:

```text
relation(s,t) composed with relation(r,s)
  subset
relation(r,t)
```

Any evaluable violation yields:

```text
LINEAGE_FAMILY_INCOHERENT
```

### 10.3 Direct-long-interval separation

The protocol does not replace a supplied direct long-interval relation by equality with composed intermediate lineage.

```text
COMPOSED_INTERMEDIATE_RELATION
  !=
DIRECT_LONG_INTERVAL_RELATION_BY_DEFAULT
```

Direct long-interval lineage may contain additional admissible information.

### 10.4 Component-family additions

For component lineage, coherence additionally requires claim-relevant:

```text
component-type preservation
inherited channel-lineage compatibility
required input-sort lineage compatibility
```

when supplied by the source interface.

## 11. Identity-bearing component family

State- and interval-level claims require a frozen, nonempty identity-bearing family at every relevant time.

Record:

```text
IDENTITY_BEARING_FAMILY_ID
IDENTITY_BEARING_FAMILY_VERSION
IDENTITY_BEARING_FAMILY_PROVENANCE
IDENTITY_BEARING_FAMILY_SELECTION_RULE_OR_JUSTIFICATION
IDENTITY_BEARING_COMPONENT_SET_BY_TIME
```

The family must be selected before claim evaluation.

```text
POST_HOC_IDENTITY_BEARING_SELECTION
  -> LINEAGE_PROTOCOL_NONCONFORMANCE
```

Protocol v0.1 does not define a universal identity-bearing family for all models.

## 12. State-succession coverage

For source time s and target time t with frozen identity-bearing families I(s) and I(t), evaluate separately:

```text
PREDECESSOR_TO_SUCCESSOR_COVERAGE:
  every component in I(s)
  has at least one component in I(t)
  related by the supplied coherent component-lineage relation

SUCCESSOR_TO_PREDECESSOR_COVERAGE:
  every component in I(t)
  has at least one component in I(s)
  related by the supplied coherent component-lineage relation
```

State succession is established only when both coverage directions pass and every other required state-level obligation is satisfied.

An evaluable failure of either direction yields:

```text
STATE_SUCCESSION:
  NOT_ESTABLISHED
```

This is not a bijection requirement.

```text
STATE_SUCCESSION != LITERAL_STATE_EQUALITY
STATE_SUCCESSION != BIJECTION_BY_DEFAULT
STATE_SUCCESSION != CARDINALITY_EQUALITY_BY_DEFAULT
```

## 13. Interval identity preservation

For `INTERVAL_IDENTITY_PRESERVATION`, the frozen task must define the interval/time set on which the claim is evaluated.

The protocol establishes interval identity preservation only when, for every required ordered pair of times in the frozen interval, the target state is a lineage-connected successor of the source state relative to the frozen identity-bearing family and coherent lineage family.

One successful pair is insufficient for an interval claim.

```text
PAIRWISE_STATE_SUCCESSION_AT_ONE_PAIR
  !=
INTERVAL_IDENTITY_PRESERVATION
```

Rank equality, small entropy rate, or another secondary stability diagnostic does not substitute for this criterion.

## 14. Branching, merging, and stronger optional constraints

Base Lineage permits supported relation-valued branching and merging.

Record:

```text
BRANCH_MERGE_TOPOLOGY
BASE_LINEAGE_RELATION_STATUS
```

If the task separately declares any stronger condition, evaluate it in a separate ledger:

```text
UNIQUE_SUCCESSOR_REQUIREMENT
BIJECTIVE_COMPONENT_TRANSPORT_REQUIREMENT
CARDINALITY_CONSERVATION_REQUIREMENT
OTHER_DECLARED_LINEAGE_CONSTRAINT
```

Allowed optional-constraint statuses:

```text
OPTIONAL_CONSTRAINT_SATISFIED
OPTIONAL_CONSTRAINT_UNSATISFIED
OPTIONAL_CONSTRAINT_BLOCKED
OPTIONAL_CONSTRAINT_OUT_OF_SCOPE
OPTIONAL_CONSTRAINT_UNDERDETERMINED
```

The underlying base lineage relation remains independently recorded.

```text
OPTIONAL_CONSTRAINT_UNSATISFIED
  !=
AUTOMATIC_ERASURE_OF_BASE_LINEAGE
```

## 15. Lineage-successor status family

Every required lineage query receives one status:

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

### 15.1 ESTABLISHED

Use only when the source-defined canonical gate or an admissible supplied lineage relation supports the directed successor claim and all claim-relevant required conditions are satisfied.

### 15.2 EXPLICITLY_NEGATED

Use only when applicable supplied evidence or a frozen domain rule explicitly excludes the requested successor relation.

Mere absence is insufficient.

### 15.3 NOT_ESTABLISHED

Use when the required interface is available and evaluable but the requested in-scope relation is unsupported or a required evaluable condition fails.

Examples include:

```text
no admissible pair in an evaluable complete supplied relation
type incompatibility
failed required state-coverage direction
evaluably incoherent family when coherent-family status is required
```

### 15.4 AMBIGUOUS

Use when claim-relevant object identity, type, family member, or target is not uniquely identified under the frozen task.

### 15.5 CONFLICTING

Use when applicable supplied records make mutually incompatible lineage claims under the same frozen semantics and no precedence resolves them.

### 15.6 BLOCKED

Use when a required interface is unavailable.

Examples include:

```text
missing required lineage relation
missing identity-bearing-family record
missing required auxiliary-lineage relation
missing formation/transition classification
missing required schema/decoder/handoff
```

### 15.7 INAPPLICABLE

Use when the requested lineage relation does not apply to the declared object types or claim level.

### 15.8 OUT_OF_SCOPE

Use when the requested relation or identity question lies outside the frozen task.

### 15.9 UNDERDETERMINED

Use when multiple admissible mappings or relation semantics yield different claim-relevant outcomes and the frozen task provides no resolver.

Required guards:

```text
NOT_ESTABLISHED != EXPLICITLY_NEGATED
NOT_ESTABLISHED != BLOCKED
AMBIGUOUS != CONFLICTING
CONFLICTING != UNDERDETERMINED
INAPPLICABLE != OUT_OF_SCOPE
```

## 16. Task-level terminal

Every executable run emits exactly one:

```text
LINEAGE_TASK_ESTABLISHED
LINEAGE_TASK_PARTIAL
LINEAGE_TASK_NOT_ESTABLISHED
LINEAGE_TASK_BLOCKED
LINEAGE_TASK_CONFLICTING
LINEAGE_TASK_OUT_OF_SCOPE
LINEAGE_TASK_UNDERDETERMINED
```

Terminal precedence:

```text
LINEAGE_TASK_OUT_OF_SCOPE
-> LINEAGE_TASK_CONFLICTING
-> LINEAGE_TASK_UNDERDETERMINED
-> LINEAGE_TASK_BLOCKED
-> LINEAGE_TASK_ESTABLISHED /
   LINEAGE_TASK_PARTIAL /
   LINEAGE_TASK_NOT_ESTABLISHED
```

### ESTABLISHED

Every required in-scope lineage obligation for the frozen claim is established and every required coherence/coverage condition passes.

### PARTIAL

The run contains multiple required lineage obligations, at least one is established, and at least one other evaluable obligation is not established, with no higher-priority terminal.

PARTIAL may not be used to rescue a single state-succession proposition whose required bidirectional coverage fails.

### NOT_ESTABLISHED

The requested in-scope proposition is evaluable but not established.

### BLOCKED

At least one required in-scope obligation cannot be evaluated because a required interface is unavailable.

### CONFLICTING

Required applicable records make mutually incompatible claims under the same frozen semantics.

### OUT_OF_SCOPE

The requested operation is not a Lineage task or lies outside the frozen lineage scope.

### UNDERDETERMINED

Multiple admissible claim-relevant lineage mappings or semantics yield different terminal outcomes with no frozen resolver.

The terminal does not erase lower-level statuses.

## 17. Secondary-diagnostic sidecar

If rank, entropy rate, stability functional, similarity score, distance, aggregate equality, or another diagnostic is supplied, record it separately as:

```text
SECONDARY_DIAGNOSTIC_ID
DIAGNOSTIC_SOURCE
DIAGNOSTIC_SCOPE
DIAGNOSTIC_VALUE_OR_STATUS
DIAGNOSTIC_PROVENANCE
NOT_USED_AS_PRIMARY_LINEAGE_CRITERION
```

A secondary diagnostic may accompany a Lineage result.

It may not create, negate, or replace the primary lineage relation unless an explicit separate domain rule is supplied and the resulting stronger claim is kept distinct.

## 18. Neighboring-method handoff ledger

For every claim-relevant handoff, record:

```text
HANDOFF_ID
SOURCE_METHOD_OR_DOMAIN
HANDOFF_ARTIFACT_ID
HANDOFF_ROLE
HANDOFF_SCOPE
HANDOFF_PROVENANCE
LINEAGE_USE
NON_SUBSTITUTION_GUARD
```

Required method boundaries include:

```text
Tracking:
  trace recording != successor identity

Dynamics:
  source lineage primitives / transition records
  != constitutive evolution-law derivation by Lineage

Reconstruction:
  candidate hidden/past relation != established lineage

Transformation:
  source-target mapping != successor identity

Comparison:
  similarity/difference != successor identity

Classification:
  class membership != individual successor identity

Aggregation / Compression:
  reduced equality/inequality != primary lineage criterion

Audit:
  lineage result != general audit verdict
```

## 19. Binding operation T1-T16

Every conformant run executes:

```text
T1
  freeze task identity/version, claim level, times, direction,
  scope, required obligations, and scope version

T2
  freeze predecessor/successor identity/type/formation/status records

T3
  for state/interval claims, freeze identity-bearing-family
  identity/version/provenance/selection rule before evaluation

T4
  classify fixed-background regular-epoch versus transition context

T5
  apply the canonical fixed-background channel-lineage gate only
  when all source preconditions are established

T6
  otherwise evaluate only supplied admissible lineage relations
  or explicitly authorized lineage handoffs

T7
  evaluate relation direction, type compatibility,
  inherited channel compatibility, and required auxiliary lineage

T8
  assign successor statuses without collapsing
  NOT_ESTABLISHED / BLOCKED / EXPLICITLY_NEGATED / ambiguity /
  conflict / underdetermination / scope distinctions

T9
  when coherence is required, evaluate self-time identity

T10
  when coherence is required, evaluate composition inclusion
  while preserving direct long-interval lineage separately

T11
  evaluate component-lineage obligations and required
  multi-input auxiliary-lineage records

T12
  for state claims, evaluate both directions of
  identity-bearing component coverage

T13
  for interval claims, evaluate every required ordered time pair

T14
  preserve branching/merging and evaluate any stronger
  optional uniqueness/bijection/cardinality constraints separately

T15
  record neighboring-method handoffs and secondary diagnostics
  without substitution or overclaim

T16
  emit task terminal, conformance, method-gain status,
  and maximum-supported-claim record
```

## 20. Validity gates G1-G16

A run is `LINEAGE_PROTOCOL_CONFORMANT` only if all applicable gates pass.

```text
G1  TASK_AND_CLAIM_LOCK

G2  PREDECESSOR_SUCCESSOR_IDENTITY_LOCK

G3  IDENTITY_BEARING_FAMILY_PRECOMMIT
    applicable to state/interval claims

G4  EPOCH_TRANSITION_CLASSIFICATION

G5  CANONICAL_LINEAGE_GATE_DISCIPLINE

G6  RELATION_SOURCE_AND_PROVENANCE_DISCIPLINE

G7  TYPE_AND_INHERITED_CHANNEL_COMPATIBILITY

G8  AUXILIARY_LINEAGE_DISCIPLINE

G9  SELF_TIME_IDENTITY_COHERENCE

G10 COMPOSITION_INCLUSION_COHERENCE

G11 DIRECT_LONG_INTERVAL_SEPARATION

G12 STATE_COVERAGE_DISCIPLINE
    applicable to state/interval claims

G13 BRANCH_MERGE_AND_OPTIONAL_CONSTRAINT_SEPARATION

G14 SUCCESSOR_STATUS_AND_TERMINAL_DISCIPLINE

G15 NEIGHBORING_METHOD_AND_DIAGNOSTIC_NON_SUBSTITUTION

G16 MAXIMUM_SUPPORTED_CLAIM_DISCIPLINE
```

An inapplicable gate is recorded as `NOT_APPLICABLE_BY_FROZEN_TASK`, not silently omitted.

## 21. Protocol conformance status

Allowed conformance statuses:

```text
LINEAGE_PROTOCOL_CONFORMANT
LINEAGE_PROTOCOL_NONCONFORMANT
LINEAGE_PROTOCOL_INDETERMINATE
```

`LINEAGE_PROTOCOL_NONCONFORMANT` is used for failures of this protocol's binding procedure, not merely because the requested lineage proposition is not established.

Examples of protocol nonconformance:

```text
post-hoc identity-bearing-family selection
identity-by-label substitution
canonical fixed-background rule used across an invalid transition
type-incompatible relation accepted as established
required auxiliary lineage silently ignored
coherent-family claim despite failed self-time/composition check
direct long-interval relation replaced by unjustified equality with composition
one-sided state coverage declared sufficient
branching rejected merely for non-uniqueness
optional stronger constraints treated as universal
secondary diagnostic substituted for lineage
neighboring-method result silently promoted to lineage identity
terminal/status semantics changed after result inspection
```

A conformant run may validly return:

```text
NOT_ESTABLISHED
BLOCKED
CONFLICTING
OUT_OF_SCOPE
UNDERDETERMINED
PARTIAL
```

without becoming protocol failure.

## 22. Method-gain status

When a fair comparator is supplied, record one of:

```text
LINEAGE_METHOD_GAIN_ESTABLISHED
LINEAGE_METHOD_GAIN_PARTIAL
LINEAGE_METHOD_GAIN_NO_GAIN
LINEAGE_METHOD_GAIN_NOT_ASSESSED
LINEAGE_METHOD_GAIN_UNDERDETERMINED
```

A baseline must receive the same claim-relevant identities, lineage relations, formation/transition data, identity-bearing family, types, constraints, provenance, and scope.

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
```

## 23. Maximum-supported-claim record

Every run emits an explicit bounded claim.

A conformant established Lineage result may assert only the frozen lineage proposition supported by the applicable source interface.

It may not silently assert:

```text
literal equality
truth/authenticity
causality
legal ownership/responsibility
Transformation correctness
Tracking completeness
Reconstruction truth
empirical validity
Audit success
external-domain adequacy
unique successor
bijection
cardinality conservation
```

unless separately established.

## 24. Output schema

Every executable run emits at least:

```text
LOCKED_LINEAGE_TASK_AND_SCOPE

PREDECESSOR_SUCCESSOR_REGISTER
FORMATION_AND_EPOCH_LEDGER

CHANNEL_LINEAGE_RELATION_LEDGER
COMPONENT_LINEAGE_RELATION_LEDGER
LINEAGE_RELATION_PROVENANCE_LEDGER
LINEAGE_SUCCESSOR_STATUS_LEDGER

LINEAGE_FAMILY_COHERENCE_STATUS
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

Outputs not applicable to the frozen claim are explicitly marked `NOT_APPLICABLE_BY_FROZEN_TASK`.

## 25. Core guards

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

ENTROPY_OR_STABILITY_DIAGNOSTIC
  !=
PRIMARY_IDENTITY_CRITERION

FORMATION_TRANSITION != AUTOMATIC_SUCCESSION
CHANNEL_CHANGE != AUTOMATIC_SUCCESSION

BRANCHING != PROTOCOL_FAILURE
MERGING != PROTOCOL_FAILURE
LINEAGE_RELATION != UNIQUE_SUCCESSOR_BY_DEFAULT
LINEAGE_RELATION != BIJECTION_BY_DEFAULT
LINEAGE_RELATION != CARDINALITY_CONSERVATION_BY_DEFAULT

COMPOSED_INTERMEDIATE_RELATION
  !=
DIRECT_LONG_INTERVAL_RELATION_BY_DEFAULT

TRACKING_LINK != LINEAGE_SUCCESSOR_DECISION
RECONSTRUCTED_LINEAGE_CANDIDATE != ESTABLISHED_LINEAGE
TRANSFORMATION_MAPPING != SUCCESSOR_IDENTITY
COMPARISON_SIMILARITY != SUCCESSOR_IDENTITY
CLASS_MEMBERSHIP != INDIVIDUAL_SUCCESSOR_IDENTITY

NOT_ESTABLISHED != EXPLICITLY_NEGATED
NOT_ESTABLISHED != BLOCKED
```

## 26. Frozen protocol state

```text
DEDICATED_LINEAGE_PROTOCOL: established v0.1

TASK_INTERFACE_DRAFT:
  v0.1 historical draft preserved

PRE_PROTOCOL_BOUNDARY_ATTACKS: 18
PRESERVED_NO_REFINEMENT: 13
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5

BOUNDARY_AMENDMENT_001: established
REFINEMENT_GROUPS_ADOPTED: 8/8

VALIDITY_GATES: G1-G16
BINDING_OPERATION: T1-T16

DIRECT_LINEAGE_PILOTS_ATTEMPTED: 0
SUCCESSFUL_DIRECT_LINEAGE_PILOTS: 0

BASELINE_LINEAGE_CASES: 0
NO_GAIN_LINEAGE_CASES: 0
REPRODUCIBILITY_CASES: 0

EXTERNAL_LINEAGE_APPLICATIONS: 0
INDEPENDENT_LINEAGE_VALIDATION: not established
INDEPENDENT_REPLICATION: not established

LINEAGE_INTERNAL_STANDARDIZATION_STATUS: developing
CURRENT_LINEAGE_EVIDENCE_STATUS: protocol_frozen

PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

Next: prospectively precommit and execute the first positive constructed Lineage challenge.
