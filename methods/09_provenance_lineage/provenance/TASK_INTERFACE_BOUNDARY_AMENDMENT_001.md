# DSD Tracking Task Interface Boundary Amendment 001

Status: **PROSPECTIVE AMENDMENT ESTABLISHED**  
Date: **2026-09-20**  
Method: **Tracking / DSD 추적론**

Historical inputs preserved:
- `TASK_INTERFACE_v0.1-draft.md`
- `BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`

This amendment does not rewrite the historical Task Interface.

It prospectively binds the refinements forced by the 18 pre-protocol boundary attacks.

## 1. Amendment purpose

The historical interface correctly broadened Provenance into Tracking and separated trace recording from truth, authenticity, causality, Lineage identity, Reconstruction, Transformation, Interpretation, Measurement, and Audit.

The boundary attacks show that an executable Tracking protocol additionally requires stronger locks around:

```text
task / target / scope / trace dimensions / completion criterion
node identity / version / type / domain / status
link relation type / direction / schema version
evidence support and provenance
graph topology
gap / negative / ambiguity / conflict / blockage / scope semantics
time / process / location / custody / ownership / responsibility / causality
neighboring-method handoffs and reconstructed-link status
```

The following eight refinement groups are therefore binding for Tracking Protocol v0.1.

## 2. R1 — tracking task, target, scope, dimensions, completion criterion

Every executable Tracking task freezes before trace evaluation:

```text
TRACKING_TASK_ID
TASK_VERSION
TRACE_TARGET_OR_TARGET_SET
DECLARED_TRACE_SCOPE
DECLARED_TRACE_DIMENSION_SET
REQUIRED_TRACE_QUERY_OR_OBLIGATION_SET
TRACE_COMPLETION_OR_QUERY_CRITERION
TASK_SCOPE_VERSION
```

`DECLARED_TRACE_DIMENSION_SET` may include, when actually requested:

```text
origin/source
version/edit/translation
transformation
process/stage/method-handoff
location/container
custody
ownership
responsibility
authorship/operator
status
reference/dependency
evidence/support
other explicitly typed trace dimension
```

A relation outside the frozen dimension set is `TRACKING_LINK_OUT_OF_SCOPE`; it is not false, missing, or conflicting merely because it is excluded.

An unbounded request such as "trace everything" may not receive `TRACKING_TRACE_COMPLETE` until a bounded scope and completion/query criterion are supplied.

```text
UNBOUNDED_TRACE_REQUEST != COMPLETE_TRACE
OUT_OF_SCOPE_RELATION != MISSING_RELATION
```

Changing scope, dimensions, required query set, or completion criterion after a preferred path is seen requires a new task version.

## 3. R2 — trace-node identity, version, type, domain, status

Every claim-relevant node must have an identity descriptor:

```text
TRACE_NODE_ID
NODE_VERSION_IF_RELEVANT
NODE_TYPE
DECLARED_DOMAIN
REPRESENTATION_OR_SCHEMA_ID_IF_RELEVANT
SUPPLIED_STATUS
NODE_IDENTITY_PROVENANCE
```

Human-readable labels are not sufficient identifiers when multiple nodes may reuse the same label.

```text
SAME_LABEL != SAME_ENTITY
SAME_FILENAME != SAME_ARTIFACT
SAME_DISPLAY_NAME != SAME_VERSION
```

When supplied predecessor-layer status semantics are claim-relevant, Tracking preserves those distinctions instead of collapsing them to one generic "missing" state.

The amendment does not create a new universal status ontology.

It requires only preservation of the typed status information actually supplied by predecessor interfaces.

## 4. R3 — typed link relation, direction, and relation-schema version

Each candidate link is represented prospectively as:

```text
TRACE_LINK_ID
SOURCE_NODE_ID
RELATION_TYPE
RELATION_DIRECTION
TARGET_NODE_ID
RELATION_SCHEMA_ID_AND_VERSION_IF_RELEVANT
RELATION_SCOPE
RELATION_STATUS
```

A direct edge is distinct from reachability through a path.

```text
PATH_REACHABILITY != DIRECT_TRACE_LINK
EDGE_SEQUENCE != DIRECT_RELATION
TEMPORAL_ADJACENCY != TRACE_LINK
```

Relation composition is allowed only when the supplied relation schema explicitly licenses it.

```text
EDGE_COMPOSITION != RELATION_COMPOSITION_WITHOUT_RULE
```

A later relation-schema version may not be applied retroactively to an earlier trace record unless an explicit migration/translation rule is supplied.

## 5. R4 — evidence support, provenance, and relation/support separation

Every claim-relevant candidate relation must keep the relation record separate from the evidence supporting, negating, or failing to resolve it.

The support ledger records, where supplied:

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
```

Tracking v0.1 does not invent a universal numerical evidence-strength score.

If a domain supplies confidence, weight, trust, authenticity, calibration, or legal evidentiary status, Tracking may retain it as typed metadata but does not reinterpret it.

```text
EVIDENCE_FOR_LINK != LINK_ITSELF
TRACEABLE_SOURCE != AUTHENTIC_SOURCE
TRACKED_RECORD != TRUE_RECORD
SUPPLIED_CONFIDENCE != TRACKING_VALIDATION
```

## 6. R5 — graph/path semantics: branching, merging, cycles, multiple sources

Tracking v0.1 uses an explicitly typed graph model rather than assuming one linear chain.

The trace graph may contain:

```text
one-to-one links
one-to-many branching
many-to-one merging
multiple independent sources
multiple destinations
disconnected components
cycles
self-reference when relation semantics permits
ordered paths
partially ordered process records
```

Topology alone does not determine semantic relation type.

A cycle in a reference/dependency graph is not automatically a temporal cycle, causal loop, or protocol defect.

```text
BRANCHING_TRACE != LINEAGE_BRANCHING_WITHOUT_HANDOFF
MERGING_TRACE != LINEAGE_MERGER_WITHOUT_HANDOFF
REFERENCE_CYCLE != TEMPORAL_CYCLE
GRAPH_CONNECTIVITY != IDENTITY
```

Tracking preserves all supported branches rather than choosing one preferred path unless the frozen task includes a supplied precedence/selection rule.

## 7. R6 — missing, negated, ambiguous, conflicting, blocked, inapplicable, out-of-scope, underdetermined

Protocol v0.1 expands the historical link-status family prospectively to:

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
ESTABLISHED
  supplied applicable evidence supports the declared typed relation.

EXPLICITLY_NEGATED
  supplied applicable evidence explicitly supports non-occurrence/non-relation.
  Mere absence is insufficient.

MISSING
  the required in-scope relation query has no supplied support or explicit negation record.

AMBIGUOUS
  a supplied record does not uniquely identify the relevant node/relation target
  under the frozen identity/schema rules.

CONFLICTING
  two or more applicable supplied records assert mutually incompatible
  relation states under the same frozen scope/schema with no precedence.

BLOCKED
  evaluation of the required in-scope relation cannot proceed because a required
  prerequisite, decoder, bridge, access record, schema mapping, or handoff is absent/unavailable.

INAPPLICABLE
  the relation type does not apply to the supplied node/domain combination.

OUT_OF_SCOPE
  the relation or trace dimension lies outside the frozen task scope.

UNDERDETERMINED
  multiple admissible claim-relevant schemas/mappings/interpretive relation rules
  yield different link statuses and no frozen precedence selects one.
```

Required guards:

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

## 8. R7 — temporal, process, location, custody, ownership, responsibility, causality separation

When claim-relevant, Tracking separately types:

```text
TEMPORAL_ORDER
PROCESS_STAGE_ORDER
LOCATION_OR_CONTAINER_RELATION
CUSTODY_RELATION
OWNERSHIP_RELATION
RESPONSIBILITY_RELATION
AUTHORSHIP_OR_OPERATOR_RELATION
SOURCE_OR_DERIVATION_RELATION
CAUSAL_RELATION_HANDOFF
```

No relation is silently converted into another.

```text
TEMPORAL_ADJACENCY != CAUSAL_LINK
PROCESS_ORDER != CAUSAL_LINK
CUSTODY_RELATION != OWNERSHIP_RELATION
OWNERSHIP_RELATION != RESPONSIBILITY_RELATION
SOURCE_RELATION != OWNERSHIP_RELATION
LOCATION_CHANGE != FORMATION_CHANGE
```

A causal relation may be tracked when a separate domain/Dynamics/Analysis handoff explicitly supplies it.

Tracking itself does not infer causality from order.

## 9. R8 — neighboring-method handoffs and reconstructed-vs-established trace

Tracking may consume typed artifacts from:

```text
Formation / Property
Static Aggregation
Dynamics
Analysis / Comparison / Classification
Specification / Audit
Design / Synthesis / Transformation
Measurement
Lineage
Reconstruction
Interpretation
Aggregation / Compression
Simulation / Prediction
other declared domain methods
```

But consuming a handoff does not authorize Tracking to perform the neighboring method silently.

Required guards:

```text
TRACE_CONTINUITY != LINEAGE_IDENTITY
VERSION_CHANGE != LINEAGE_CHANGE

MISSING_TRACE_LINK != LICENSE_TO_RECONSTRUCT
RECONSTRUCTED_LINK != ESTABLISHED_TRACE_LINK

TRACE_OF_TRANSFORMATION != TRANSFORMATION_CORRECTNESS
TRACE_OF_AGGREGATE != RECONSTRUCTION_OF_SUPPORT

TRACE_RECORD != AUDIT_VERDICT
TRACE_CONTEXT != INTERPRETATION_RESULT
TRACE_OF_MEASUREMENT != DISCRIMINATION_SUFFICIENCY

SHARED_ARTIFACT != SAME_METHOD
HANDOFF_COMPATIBILITY != METHOD_COLLAPSE
```

When Reconstruction supplies a candidate link, Tracking records it in a separate sidecar such as:

```text
RECONSTRUCTED_OR_INFERRED_LINK
RECONSTRUCTION_SOURCE
RECONSTRUCTION_STATUS
NOT_ESTABLISHED_AS_HISTORICAL_TRACE_LINK
```

unless separate direct evidence later establishes the relation.

When Lineage supplies successor identity, Tracking may record that lineage relation as a typed handoff, but the identity decision remains a Lineage result.

## 10. Trace-level terminal obligations

Protocol v0.1 must define exactly one trace-level terminal:

```text
TRACKING_TRACE_COMPLETE
TRACKING_TRACE_PARTIAL
TRACKING_TRACE_BLOCKED
TRACKING_TRACE_CONFLICTING
TRACKING_TRACE_OUT_OF_SCOPE
TRACKING_TRACE_UNDERDETERMINED
```

Prospective semantics:

```text
COMPLETE
  every required in-scope trace query/obligation is resolved under the frozen
  completion criterion with an established or explicitly negated relation status,
  and no required unresolved segment remains.

PARTIAL
  at least one required in-scope query is resolved but one or more required
  segments remain missing or otherwise unresolved, while the trace still yields
  a meaningful bounded partial result and no higher-priority terminal below dominates.

BLOCKED
  a required in-scope query cannot be evaluated because a required prerequisite,
  bridge, schema mapping, access record, or handoff is unavailable.

CONFLICTING
  applicable supplied evidence contains unresolved mutually incompatible
  required relation claims under the same frozen scope/schema.

OUT_OF_SCOPE
  the requested operation is not a Tracking task or the required trace request
  lies outside the frozen scope/dimensions.

UNDERDETERMINED
  multiple admissible claim-relevant schemas/mappings/rules yield incompatible
  terminal judgments with no frozen precedence.
```

Terminal precedence for a single frozen run is:

```text
OUT_OF_SCOPE
-> CONFLICTING
-> UNDERDETERMINED
-> BLOCKED
-> COMPLETE / PARTIAL
```

This precedence resolves only which terminal label summarizes the run.

It does not erase lower-level link statuses.

## 11. Prospective protocol obligations

Tracking Protocol v0.1 must contain:

```text
task / target / scope / dimension / completion locks
typed node register
typed relation and direction register
relation-schema/version lock
evidence/support/provenance ledger
graph/path semantics
link-status family including BLOCKED
gap / ambiguity / conflict ledger
temporal/process/location/custody/ownership/responsibility separation
neighboring-method handoff ledger
reconstructed/inferred link sidecar
trace-level terminal semantics and precedence
conformance
method-gain record
maximum-supported-claim record
```

## 12. Amendment result

```text
BOUNDARY_AMENDMENT_001: established
REFINEMENT_GROUPS_ADOPTED: 8/8

HISTORICAL_TASK_INTERFACE_REWRITTEN: no

HISTORICAL_LINK_STATUS_FAMILY_EXTENDED_PROSPECTIVELY:
  yes, TRACKING_LINK_BLOCKED added

BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0

PROTOCOL_FREEZE_AUTHORIZED: yes
EXTERNAL_APPLICATION: no
```

Next: freeze executable Tracking Protocol v0.1 from the historical Task Interface plus this amendment.
