# DSD Tracking Task Interface v0.1 — historical draft

Status: **historical draft / preserved**  
Date: **2026-09-20**  
Method: **Tracking / DSD 추적론**  
Compatibility note: **Provenance / 출처·유래 추적** remains an origin/derivation subcase.

## 1. Task identity

DSD Tracking receives a declared trace target, a bounded trace scope, supplied trace nodes and candidate relations, and evidence/support records for those relations.

It returns an explicit trace ledger and trace graph/path showing which links are established, explicitly negated, missing, ambiguous, conflicting, inapplicable, out of scope, or underdetermined within the declared scope.

Tracking follows supplied/evidence-supported relations.

It does not silently infer hidden links, decide successor identity, prove authenticity or truth, infer causality, assign legal responsibility, validate a transformation, reconstruct missing history, or issue an Audit verdict.

## 2. Inputs

Required inputs:

```text
TRACKING_TASK_ID
TRACE_TARGET_OR_TARGET_SET
DECLARED_TRACE_SCOPE
DECLARED_TRACE_DIMENSION_SET
TRACE_COMPLETION_OR_QUERY_CRITERION
TRACE_NODE_REGISTER
TRACE_NODE_IDENTITY_TYPE_DOMAIN_VERSION
CANDIDATE_TRACE_LINK_SET
TRACE_LINK_RELATION_TYPE_AND_DIRECTION
TRACE_LINK_EVIDENCE_OR_SUPPORT_RECORD
TRACE_LINK_EVIDENCE_PROVENANCE
```

Conditionally required:

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
```

If a claim-relevant link, relation type, direction, schema/version, or evidence record is absent, Tracking must preserve that limitation rather than fill the link by intuition.

## 3. Binding operation

Tracking must:

```text
1 lock the tracking question, target, scope, trace dimensions, and completion criterion;

2 lock every claim-relevant trace-node identity, type, domain, version,
  and supplied status before connecting nodes;

3 type every candidate link by relation kind, direction, and relation schema/version
  where relevant;

4 preserve supplied status distinctions rather than coercing missing, undefined,
  inapplicable, or explicitly negated relations into one generic absence class;

5 admit an established trace link only from supplied/evidence-supported relation records;

6 record evidence/support provenance separately from the relation itself;

7 permit graph structure rather than forcing every trace into one linear chain;

8 preserve branching, merging, cycles, multiple sources, and multiple destinations
  when the supplied trace records require them;

9 preserve missing, ambiguous, conflicting, blocked, inapplicable,
  out-of-scope, and underdetermined segments without post-hoc repair;

10 keep temporal adjacency and process order separate from causality;

11 keep location/container, custody, ownership, responsibility,
   authorship, and source relations separately typed;

12 record Transformation, Aggregation, Compression, Measurement,
   Interpretation, Audit, Reconstruction, and Lineage handoffs without
   silently performing those neighboring methods;

13 keep reconstructed or inferred links distinct from established trace links;

14 emit trace-node, trace-link, support, gap/conflict, handoff,
   terminal, conformance, and method-gain records.
```

## 4. Trace-link status family

```text
TRACKING_LINK_ESTABLISHED
TRACKING_LINK_EXPLICITLY_NEGATED
TRACKING_LINK_MISSING
TRACKING_LINK_AMBIGUOUS
TRACKING_LINK_CONFLICTING
TRACKING_LINK_INAPPLICABLE
TRACKING_LINK_OUT_OF_SCOPE
TRACKING_LINK_UNDERDETERMINED
```

These statuses describe the declared trace relation, not truth of the tracked content.

A missing link is not an explicitly negative relation.

A conflicting link record is not permission to choose the preferred branch.

## 5. Trace-level terminal status family

```text
TRACKING_TRACE_COMPLETE
TRACKING_TRACE_PARTIAL
TRACKING_TRACE_BLOCKED
TRACKING_TRACE_CONFLICTING
TRACKING_TRACE_OUT_OF_SCOPE
TRACKING_TRACE_UNDERDETERMINED
```

A trace terminal is distinct from protocol conformance, authenticity, causality, Lineage identity, and Audit success.

## 6. Trace graph record

Let the supplied trace-node set be `V` and candidate relation records be typed directed edges `E`.

This graph notation is an interface record, not a new DSD axiom.

For an edge `e=(u, r, v)`:

```text
u:
  source node identity

r:
  declared relation type + direction + schema/version when relevant

v:
  target node identity
```

An edge may be marked `TRACKING_LINK_ESTABLISHED` only when the frozen evidence/support record actually supports the declared relation under the locked scope.

Tracking does not infer:

```text
u -> v successor identity
u causes v
u owns v
u is responsible for v
u is authentic because it is traceable
```

unless the corresponding neighboring-method or domain-specific bridge is separately supplied.

## 7. Outputs

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
```

Only outputs relevant to the declared trace dimensions need be populated.

## 8. Core guards

```text
TRACKED != TRUE
TRACKED != AUTHENTIC
TRACKED != VALIDATED

TRACE_LINK != CAUSAL_LINK
TRACE_CONTINUITY != LINEAGE_IDENTITY
TEMPORAL_ADJACENCY != SUCCESSOR_RELATION
SAME_LABEL != SAME_ENTITY

SOURCE_RELATION != OWNERSHIP_RELATION
OWNERSHIP_RELATION != RESPONSIBILITY_RELATION
CUSTODY_RELATION != OWNERSHIP_RELATION

LOCATION_CHANGE != FORMATION_CHANGE
VERSION_CHANGE != LINEAGE_CHANGE

MISSING_LINK != NEGATIVE_LINK
AMBIGUOUS_LINK != LICENSE_TO_CHOOSE_POST_HOC
CONFLICTING_LINKS != LICENSE_TO_DISCARD_ONE

RECONSTRUCTED_LINK != ESTABLISHED_TRACE_LINK

TRACE_OF_TRANSFORMATION != TRANSFORMATION_CORRECTNESS
TRACE_OF_AGGREGATE != RECONSTRUCTION_OF_SUPPORT
TRACE_RECORD != AUDIT_VERDICT
TRACE_CONTEXT != INTERPRETATION_RESULT
```

## 9. Failure / no-gain criteria

Protocol nonconformance includes:

```text
changing trace scope after seeing a preferred path;
identifying nodes only by a reused label when identity/version matters;
silently changing relation schema or direction;
inventing a missing link from temporal adjacency;
choosing one ambiguous/conflicting source without frozen precedence;
turning missing into explicit negative;
treating custody as ownership or responsibility;
treating process order as causality;
treating a tracked transformation as proof that the transformation was correct;
reconstructing an aggregate's lost support from the trace alone;
treating a reconstructed link as an established historical link;
treating trace continuity as Lineage identity;
treating a trace record as an Audit verdict;
forcing a branching/merging/cyclic trace into one linear chain.
```

`NO_GAIN` is allowed when a fair non-DSD trace/graph evaluator receiving the same node identities, relation types, evidence records, versions, statuses, and scope produces the same claim-relevant trace result.

```text
NO_GAIN != METHOD_FAILURE
CASE_FAIL != METHOD_DELETION_PROOF
```

## 10. Method boundaries

```text
Lineage:
  decides predecessor/successor identity, inheritance, split/merge/replacement.
  Tracking may record supplied lineage handoffs but does not decide identity by continuity.

Reconstruction:
  infers compatible missing/hidden/past structure from incomplete evidence.
  Tracking marks missing segments unless a reconstruction handoff is explicitly supplied.

Transformation:
  performs or characterizes source-to-target mapping and preservation/loss.
  Tracking records where a declared transformation sits in the trace chain.

Audit:
  evaluates conformance to criteria.
  Tracking constructs and reports the trace record.

Interpretation:
  evaluates meaning under context/source/bridge constraints.
  Tracking records context/source/reference relations without deciding the meaning.

Measurement:
  evaluates whether supplied readouts discriminate alternatives.
  Tracking can follow measurement artifacts/results but does not establish discrimination sufficiency.

Aggregation / Compression:
  produce or characterize reduced representations.
  Tracking records their handoffs and loss sidecars but does not reconstruct discarded support.

Comparison:
  compares declared targets.
  Tracking may provide histories for comparison but does not replace comparison criteria.
```

## 11. Historical compatibility

The repository directory name `provenance/` is retained only for path compatibility.

New records use:

```text
METHOD_NAME: Tracking / DSD 추적론
LEGACY_SUBCASE: Provenance / 출처·유래 추적
```

The broadened name does not retroactively rewrite historical provenance records.
