# DSD Tracking Protocol v0.1

Status: **FROZEN EXECUTABLE INTERNAL PROTOCOL**  
Date: **2026-09-20**  
Method: **Tracking / DSD 추적론**  
Legacy subcase: **Provenance / 출처·유래 추적**

Protocol lineage:

```text
TASK_INTERFACE_v0.1-draft.md
  blob: 9382cd0e6e03040a37d6f0b8474f09885edc252d

BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md
  blob: 10c21555f127577c7f84c78f2816e271a4f9148b

TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
  commit: 086c537b1312838500f6d188f32e7c643bde990b
  blob:   846a195f1e18c1fd1b9824638d98e10fc837f10e
```

This protocol freezes the internal operational semantics of DSD Tracking.

It does not establish truth, authenticity, causality, legal ownership/responsibility, successor identity, correctness of a transformation, correctness of an interpretation, empirical validity, Audit success, or independent validation.

## 1. Method form

A Tracking task has the form:

```text
(
  tracking task identity/version,
  trace target,
  bounded trace scope,
  trace dimensions,
  required trace queries/obligations,
  completion/query criterion,
  typed node records,
  typed candidate link records,
  evidence/support records,
  relation-schema/version records,
  optional temporal/process/location/actor/status/handoff records
)
->
(
  locked task/scope record,
  node/status ledger,
  typed relation register,
  trace-link status ledger,
  trace graph/path record,
  evidence/provenance ledger,
  gap/ambiguity/conflict ledger,
  neighboring-method handoff ledger,
  trace terminal,
  conformance,
  method-gain status,
  maximum-supported-claim record
)
```

Tracking records evidence-bounded trace relations.

It does not silently create a missing relation.

## 2. Source-layer discipline

Protocol v0.1 may consume, when supplied and claim-relevant:

```text
Formation:
  formation/channel identity records and declared formation transitions.

Property:
  typed status, applicability, prerequisite, definedness, and value-status records.

Static Aggregation:
  aggregate/reduction handoffs, support-retaining sidecars,
  collision/injectivity/reconstruction-limit records.

Dynamics:
  time-indexed state records, transition records,
  temporal order, explicit lineage handoffs,
  dynamic-support or regime records.

Other DSD methods:
  Transformation ledgers
  Measurement outputs
  Reconstruction sidecars
  Lineage decisions
  Audit records
  Interpretation records
  Comparison/Analysis records
  other typed handoffs.
```

No optional predecessor layer is mandatory when the declared Tracking task does not require it.

The source layers remain logically distinct.

```text
FORMATION_CHANGE != LOCATION_CHANGE
PROPERTY_STATUS != TRACE_TRUTH
AGGREGATE_VALUE != SUPPORT_IDENTITY
DYNAMIC_SUCCESSION_RECORD != TRACKING-INFERRED_LINEAGE
```

## 3. Required task record

Every executable run freezes:

```text
TRACKING_TASK_ID
TASK_VERSION
TRACE_TARGET_OR_TARGET_SET
DECLARED_TRACE_SCOPE
DECLARED_TRACE_DIMENSION_SET
REQUIRED_TRACE_QUERY_OR_OBLIGATION_SET
TRACE_COMPLETION_OR_QUERY_CRITERION
TASK_SCOPE_VERSION

TRACE_NODE_REGISTER
CANDIDATE_TRACE_LINK_SET
TRACE_LINK_RELATION_TYPE_AND_DIRECTION
TRACE_LINK_EVIDENCE_OR_SUPPORT_RECORD
TRACE_LINK_EVIDENCE_PROVENANCE
```

Conditionally required when claim-relevant:

```text
TEMPORAL_OR_PROCESS_ORDER
RELATION_SCHEMA_OR_VERSION
STATUS_RECORDS
ORIGIN_SOURCE_RECORDS
TRANSFORMATION_HANDOFFS
AGGREGATION_OR_COMPRESSION_SIDECARS
DYNAMIC_TRANSITION_RECORDS
LOCATION_OR_CONTAINER_RECORDS
ACTOR_CUSTODY_OWNERSHIP_RESPONSIBILITY_RECORDS
REFERENCE_OR_DEPENDENCY_RECORDS
LINEAGE_HANDOFFS
RECONSTRUCTION_HANDOFFS
INTERPRETATION_HANDOFFS
AUDIT_HANDOFFS
MEASUREMENT_HANDOFFS
CONFLICT_OR_PRECEDENCE_POLICY
OTHER_TYPED_HANDOFFS
```

Required claim-relevant records may be explicitly absent.

Absence remains part of the task state and may yield `MISSING`, `BLOCKED`, `PARTIAL`, or another frozen status according to the rules below.

## 4. Trace-node descriptor

For every claim-relevant node `v`, record:

```text
TRACE_NODE_ID
NODE_VERSION_IF_RELEVANT
NODE_TYPE
DECLARED_DOMAIN
REPRESENTATION_OR_SCHEMA_ID_IF_RELEVANT
SUPPLIED_STATUS
NODE_IDENTITY_PROVENANCE
OPTIONAL_HUMAN_READABLE_LABEL
```

The protocol never uses a reused label as sufficient identity when version/identity distinctions are claim-relevant.

```text
SAME_LABEL != SAME_ENTITY
SAME_FILENAME != SAME_ARTIFACT
SAME_DISPLAY_NAME != SAME_VERSION
```

When predecessor status semantics are supplied, they are preserved in their original typed form.

No new universal status ontology is imposed by Tracking.

## 5. Candidate trace-link descriptor

Every candidate relation `e` is registered as:

```text
TRACE_LINK_ID
SOURCE_NODE_ID
RELATION_TYPE
RELATION_DIRECTION
TARGET_NODE_ID
RELATION_SCHEMA_ID_AND_VERSION_IF_RELEVANT
RELATION_SCOPE
RELATION_QUERY_OR_OBLIGATION_ID
EVIDENCE_RECORD_IDS
RELATION_STATUS
```

A direct edge is distinct from a path.

```text
PATH_REACHABILITY != DIRECT_TRACE_LINK
EDGE_SEQUENCE != DIRECT_RELATION
TEMPORAL_ADJACENCY != TRACE_LINK
```

Relation composition is applied only when a supplied relation schema licenses it.

```text
EDGE_COMPOSITION != RELATION_COMPOSITION_WITHOUT_RULE
```

## 6. Evidence-support ledger

For every claim-relevant link query, record where supplied:

```text
EVIDENCE_RECORD_ID
EVIDENCE_TYPE_OR_ROLE
EVIDENCE_SOURCE
EVIDENCE_VERSION
EVIDENCE_SCOPE
EVIDENCE_PROVENANCE
DIRECT_OR_HANDOFF_ROLE
SUPPORTS_RELATION
NEGATES_RELATION
CONFLICTS_WITH_RECORD
EVIDENCE_APPLICABILITY_STATUS
OPTIONAL_DOMAIN_CONFIDENCE_OR_WEIGHT_METADATA
```

Tracking does not create a universal numerical support score.

A supplied confidence, weight, authenticity, calibration, evidentiary class, or trust label remains typed metadata from its source domain/handoff.

```text
EVIDENCE_FOR_LINK != LINK_ITSELF
TRACEABLE_SOURCE != AUTHENTIC_SOURCE
TRACKED_RECORD != TRUE_RECORD
SUPPLIED_CONFIDENCE != TRACKING_VALIDATION
```

## 7. Trace-link status family

Each in-scope candidate/query relation receives one of:

```text
TRACKING_LINK_ESTABLISHED
TRACKING_LINK_EXPLICITLY_NEGATED
TRACKING_LINK_MISSING
TRACKING_LINK_AMBIGUOUS
TRACKING_LINK_CONFLICTING
TRACKING_LINK_BLOCKED
TRACKING_LINK_INAPPLICABLE
TRACKING_LINK_OUT_OF_SCOPE
TRACKING_LINK_UNDERDETERMINED
```

Semantics:

```text
TRACKING_LINK_ESTABLISHED
  applicable supplied evidence supports the declared typed relation.

TRACKING_LINK_EXPLICITLY_NEGATED
  applicable supplied evidence explicitly supports non-occurrence/non-relation.
  Mere absence does not qualify.

TRACKING_LINK_MISSING
  the required in-scope relation query has no supplied support and no explicit negation.

TRACKING_LINK_AMBIGUOUS
  a supplied record does not uniquely identify the relevant node/relation target
  under frozen identity/schema rules.

TRACKING_LINK_CONFLICTING
  two or more applicable supplied records assert mutually incompatible relation
  states under the same frozen relation schema/scope and no precedence resolves them.

TRACKING_LINK_BLOCKED
  a required prerequisite, decoder, access record, bridge, schema mapping,
  or handoff needed to evaluate the relation is absent/unavailable.

TRACKING_LINK_INAPPLICABLE
  the relation type does not apply to the supplied node/domain combination.

TRACKING_LINK_OUT_OF_SCOPE
  the relation or trace dimension lies outside the frozen task scope/dimensions.

TRACKING_LINK_UNDERDETERMINED
  multiple admissible claim-relevant schemas/mappings/rules yield different
  link judgments with no frozen precedence.
```

Required distinctions:

```text
MISSING_LINK != NEGATIVE_LINK
AMBIGUOUS_LINK != CONFLICTING_LINK
CONFLICTING_LINK != UNDERDETERMINED_LINK
BLOCKED_LINK != MISSING_LINK
INAPPLICABLE_LINK != NEGATED_LINK
OUT_OF_SCOPE_LINK != FALSE_LINK
AMBIGUOUS_LINK != LICENSE_TO_CHOOSE_POST_HOC
CONFLICTING_LINKS != LICENSE_TO_DISCARD_ONE
```

## 8. Graph and path semantics

Let the frozen node set be `V` and typed candidate/established relation records be `E`.

The trace representation is a typed directed multigraph unless a narrower representation is supplied by the task.

Protocol v0.1 permits:

```text
one-to-one links
one-to-many branching
many-to-one merging
multiple independent sources
multiple destinations
disconnected components
cycles
self-reference where relation semantics permits
ordered paths
partially ordered process records
parallel relation types between the same node pair
```

Topology does not automatically determine semantic identity.

```text
BRANCHING_TRACE != LINEAGE_BRANCHING_WITHOUT_HANDOFF
MERGING_TRACE != LINEAGE_MERGER_WITHOUT_HANDOFF
REFERENCE_CYCLE != TEMPORAL_CYCLE
GRAPH_CONNECTIVITY != IDENTITY
PATH_EXISTENCE != DIRECT_EDGE
```

A linear path may be emitted only when the frozen task and evidence actually support that simplification.

## 9. Trace dimensions and relation separation

When declared, Tracking keeps the following relation families separately typed:

```text
ORIGIN_OR_SOURCE_RELATION
VERSION_OR_EDIT_RELATION
TRANSLATION_RELATION
TRANSFORMATION_HANDOFF_RELATION
PROCESS_OR_STAGE_RELATION
METHOD_HANDOFF_RELATION
LOCATION_OR_CONTAINER_RELATION
CUSTODY_RELATION
OWNERSHIP_RELATION
RESPONSIBILITY_RELATION
AUTHORSHIP_OR_OPERATOR_RELATION
STATUS_CHANGE_RELATION
REFERENCE_RELATION
DEPENDENCY_RELATION
EVIDENCE_SUPPORT_RELATION
CAUSAL_RELATION_HANDOFF
LINEAGE_RELATION_HANDOFF
OTHER_DECLARED_TYPED_RELATION
```

Core guards:

```text
TEMPORAL_ADJACENCY != CAUSAL_LINK
PROCESS_ORDER != CAUSAL_LINK

SOURCE_RELATION != OWNERSHIP_RELATION
CUSTODY_RELATION != OWNERSHIP_RELATION
OWNERSHIP_RELATION != RESPONSIBILITY_RELATION

LOCATION_CHANGE != FORMATION_CHANGE
VERSION_CHANGE != LINEAGE_CHANGE
```

A causal or lineage relation may be tracked only when supplied through an explicit handoff or direct domain record.

Tracking does not derive it from order or continuity alone.

## 10. Neighboring-method handoffs

Tracking may consume typed outputs from neighboring methods.

The handoff ledger records:

```text
HANDOFF_ID
SOURCE_METHOD_OR_INTERFACE
SOURCE_ARTIFACT_ID_AND_VERSION
HANDOFF_RELATION_TYPE
HANDOFF_SCOPE
HANDOFF_STATUS
CLAIM_STRENGTH
```

Required method-boundary guards:

```text
TRACE_CONTINUITY != LINEAGE_IDENTITY
TEMPORAL_ADJACENCY != SUCCESSOR_RELATION
VERSION_CHANGE != LINEAGE_CHANGE

MISSING_TRACE_LINK != LICENSE_TO_RECONSTRUCT
RECONSTRUCTED_LINK != ESTABLISHED_TRACE_LINK

TRACE_OF_TRANSFORMATION != TRANSFORMATION_CORRECTNESS
TRACE_OF_AGGREGATE != RECONSTRUCTION_OF_SUPPORT
TRACE_OF_MEASUREMENT != DISCRIMINATION_SUFFICIENCY

TRACE_RECORD != AUDIT_VERDICT
TRACE_CONTEXT != INTERPRETATION_RESULT

SHARED_ARTIFACT != SAME_METHOD
HANDOFF_COMPATIBILITY != METHOD_COLLAPSE
```

A Reconstruction handoff is recorded in:

```text
RECONSTRUCTED_OR_INFERRED_LINK_SIDECAR
```

and remains non-established unless separate evidence establishes the historical/trace relation.

## 11. Trace-level terminal family

Every run emits exactly one:

```text
TRACKING_TRACE_COMPLETE
TRACKING_TRACE_PARTIAL
TRACKING_TRACE_BLOCKED
TRACKING_TRACE_CONFLICTING
TRACKING_TRACE_OUT_OF_SCOPE
TRACKING_TRACE_UNDERDETERMINED
```

Rules:

```text
TRACKING_TRACE_COMPLETE
  every required in-scope trace query/obligation is resolved under the frozen
  completion criterion by an established or explicitly negated relation status,
  and no required unresolved segment remains.

TRACKING_TRACE_PARTIAL
  at least one required in-scope query is resolved but one or more required
  segments remain missing or otherwise unresolved, while the result remains
  meaningful and no higher-priority terminal dominates.

TRACKING_TRACE_BLOCKED
  a required in-scope query cannot be evaluated because a required prerequisite,
  bridge, schema mapping, access record, or handoff is unavailable.

TRACKING_TRACE_CONFLICTING
  applicable supplied evidence contains unresolved mutually incompatible required
  relation claims under the same frozen scope/schema.

TRACKING_TRACE_OUT_OF_SCOPE
  the requested operation is not a Tracking task, or the required trace request
  lies outside the frozen task scope/dimensions.

TRACKING_TRACE_UNDERDETERMINED
  multiple admissible claim-relevant schemas/mappings/rules produce incompatible
  terminal judgments and no frozen precedence selects one.
```

Terminal summary precedence:

```text
OUT_OF_SCOPE
-> CONFLICTING
-> UNDERDETERMINED
-> BLOCKED
-> COMPLETE / PARTIAL
```

This precedence chooses only the run-level terminal.

It does not overwrite lower-level link statuses.

## 12. Completion criterion discipline

A task may define completion by:

```text
all required relation queries resolved
all declared endpoints reached
all nodes in a declared bounded set processed
all declared relation dimensions evaluated
a supplied stop condition satisfied
another explicit finite/bounded criterion
```

Tracking does not equate "no more records currently visible" with trace completeness unless that is part of a supplied bounded completion rule.

```text
NO_MORE_VISIBLE_RECORDS != COMPLETE_TRACE_BY_DEFAULT
SEARCH_EXHAUSTION_CLAIM_REQUIRES_DECLARED_BOUND
```

## 13. Validity gates

A conformant run must satisfy all applicable gates:

```text
G1  task identity/version, target, scope, dimensions, required queries,
    and completion criterion frozen

G2  claim-relevant node identities/types/domains/versions/statuses frozen

G3  candidate link relation type/direction/schema-version frozen

G4  relation and supporting evidence/provenance kept distinct

G5  established/negated link claims use supplied applicable evidence only

G6  missing/ambiguous/conflicting/blocked/inapplicable/out-of-scope/
    underdetermined distinctions preserved

G7  graph topology retained without forced linearization

G8  direct edge vs path/reachability distinction preserved

G9  temporal/process/location/custody/ownership/responsibility/
    causality relation families remain typed and separate

G10 aggregate/compression loss and reconstruction limitations preserved
    when those handoffs are claim-relevant

G11 neighboring-method handoffs remain typed; no silent Lineage,
    Reconstruction, Transformation, Interpretation, Measurement, or Audit execution

G12 reconstructed/inferred links remain distinct from established trace links

G13 terminal status follows frozen completion criterion and terminal precedence

G14 conformance, method-gain status, and maximum supported claim emitted
```

An inapplicable gate is recorded as `NOT_APPLICABLE_WITH_REASON`, not silently omitted.

## 14. Binding operation

The executable Tracking operation is:

```text
T1  freeze task identity/version, target, scope, dimensions,
    required queries, and completion criterion

T2  register typed node identities, versions, domains, and statuses

T3  register candidate typed relation links, direction, schema/version, and scope

T4  register evidence/support records and provenance separately from relation claims

T5  evaluate evidence applicability to each frozen relation query

T6  assign link-level status:
    established / explicitly negated / missing / ambiguous / conflicting /
    blocked / inapplicable / out-of-scope / underdetermined

T7  construct the typed trace graph while preserving branch/merge/cycle structure

T8  record origin/version/transformation/process/location/actor/status/
    reference/dependency relation ledgers for declared dimensions

T9  preserve aggregation/compression information-loss sidecars where relevant

T10 register neighboring-method handoffs without silent method substitution

T11 separate reconstructed/inferred links from established trace links

T12 evaluate the frozen completion criterion over required query obligations

T13 assign exactly one trace-level terminal using frozen precedence

T14 emit conformance, method-gain status, and maximum-supported-claim record
```

No later operation may retroactively alter T1-T4 without opening a new task version.

## 15. Output contract

Every run emits:

```text
LOCKED_TRACKING_TASK_AND_SCOPE
TRACE_NODE_REGISTER
TRACE_NODE_STATUS_LEDGER
TRACE_RELATION_TYPE_REGISTER
TRACE_LINK_LEDGER
TRACE_GRAPH_OR_ORDERED_PATH_RECORD
TRACE_EVIDENCE_SUPPORT_LEDGER
TRACE_GAP_AMBIGUITY_CONFLICT_LEDGER
ORIGIN_SOURCE_LEDGER
VERSION_TRANSFORMATION_STAGE_LEDGER
LOCATION_CONTAINER_LEDGER
ACTOR_CUSTODY_OWNERSHIP_RESPONSIBILITY_LEDGER
REFERENCE_DEPENDENCY_LEDGER
NEIGHBORING_METHOD_HANDOFF_LEDGER
RECONSTRUCTED_OR_INFERRED_LINK_SIDECAR
TRACKING_TRACE_TERMINAL_STATUS
TRACKING_PROTOCOL_CONFORMANCE
TRACKING_METHOD_GAIN_STATUS
MAXIMUM_SUPPORTED_CLAIM
```

Only ledgers relevant to the frozen trace dimensions must contain substantive entries.

Other ledgers may be marked `NOT_APPLICABLE_WITH_REASON`.

## 16. Protocol conformance

Allowed conformance:

```text
CONFORMANT
NONCONFORMANT
UNRESOLVED_CONFORMANCE
```

Examples of nonconformance:

```text
changing scope/dimensions/completion criterion after seeing a preferred path
merging distinct nodes by reused label
silently changing relation type/direction/schema version
creating a trace link from temporal adjacency alone
treating absence as explicit negation
discarding one conflicting source without frozen precedence
treating ambiguous identity as resolved without evidence
forcing a branching/merging/cyclic graph into one linear chain
treating custody as ownership or responsibility
promoting process order to causality
promoting version continuity to Lineage identity
treating tracked transformation as proof of correctness
reconstructing lost aggregate support from trace alone
promoting a Reconstruction candidate link to established history
treating trace record as Audit verdict
claiming complete trace without satisfying the frozen completion criterion
```

A conformant result may be partial, blocked, conflicting, out-of-scope, or underdetermined.

## 17. Method-gain evaluation

Allowed:

```text
GAIN_ESTABLISHED
NO_GAIN
NOT_ASSESSED
```

A fair non-DSD baseline receives the same:

```text
task target/scope/dimensions/completion rule
node identities/types/domains/versions/statuses
candidate relation records
relation schemas/versions
evidence/support records and provenance
temporal/process/location/actor/status records
graph topology information
aggregation/compression sidecars
neighboring-method handoffs
conflict/precedence policies
```

`GAIN_ESTABLISHED` requires a precommitted claim-relevant difference under equal information access.

`NO_GAIN` is valid comparative evidence.

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
```

## 18. Reproducibility and evidence scope

A same-project deterministic retrace must use immutable protocol/precommit artifacts and a separately frozen comparison target.

A successful same-project retrace may establish:

```text
SAME_PROJECT_DETERMINISTIC_RETRACE: established_once_or_more
```

but not:

```text
INDEPENDENT_REPLICATION
INDEPENDENT_VALIDATION
EXTERNAL_APPLICABILITY
PRACTICAL_SUPERIORITY
```

## 19. Shared-core obligations

Protocol v0.1 inherits the project shared core:

```text
SC01 preserve claim-relevant DSD status/type distinctions
SC02 lock source/interface/version semantics
SC03 explicit claim-relevant mappings
SC04 sufficient dependencies without optional-interface overconstraint
SC05 preserve information-loss/reconstruction limits
SC06 separate regular evolution / transition / lineage where relevant
SC07 separate evidence applicability from case origin
SC08 preserve failure / NO_GAIN / precommit integrity
SC09 separate evidence/audit status from DSD object/model status
SC10 keep external-domain standards distinct from internal DSD success
```

No new shared-core clause is asserted by this protocol.

## 20. Maximum supported claim

A successful Tracking run may establish only that, under the frozen task scope and supplied evidence/handoffs, the recorded typed trace relations and unresolved statuses are supported at the stated level.

It does not by itself establish:

```text
truth of tracked content
authenticity of an artifact/source
causality
legal ownership
legal responsibility
Lineage successor identity
correctness of a Transformation
correctness of an Interpretation
measurement discrimination sufficiency
full reconstruction of lost support/history
Audit conformance
external-domain adequacy
independent validation
method superiority
permanent method-registry survival
```

## 21. Historical compatibility

The canonical method name is:

```text
Tracking / DSD 추적론
```

The legacy subcase remains:

```text
Provenance / 출처·유래 추적
```

The repository path:

```text
methods/09_provenance_lineage/provenance/
```

is retained for compatibility only.

The broadened method name does not retroactively rewrite historical provenance records.

## 22. Protocol freeze status

```text
DEDICATED_TRACKING_PROTOCOL: established v0.1
BOUNDARY_AMENDMENT_001: established

VALIDITY_GATES: G1-G14
BINDING_OPERATION: T1-T14

DIRECT_TRACKING_PILOTS_ATTEMPTED: 0
SUCCESSFUL_DIRECT_TRACKING_PILOTS: 0
BASELINE_TRACKING_CASES: 0
NO_GAIN_TRACKING_CASES: 0
REPRODUCIBILITY_CASES: 0

EXTERNAL_TRACKING_APPLICATIONS: 0
INDEPENDENT_TRACKING_VALIDATION: not established
INDEPENDENT_REPLICATION: not established

TRACKING_INTERNAL_STANDARDIZATION_STATUS: developing
CURRENT_TRACKING_EVIDENCE_STATUS: protocol_frozen_pre_validation

PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

Next: prospectively precommit and execute the first positive constructed Tracking challenge.

External validation remains deferred.
