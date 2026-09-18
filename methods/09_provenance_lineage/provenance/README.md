# DSD Tracking / DSD 추적론

Status: **developing**  
Legacy path ID: `09A`  
Legacy path: `methods/09_provenance_lineage/provenance/`  
Former Korean label: **DSD 출처·유래 추적론**  
Former English compatibility label: **Provenance**  
Higher field: **IV. Evidence & Lineage / 증거·계보**

## Task

Track a declared target, artifact, datum, document, model, interpretation, component, responsibility, state record, or result across an explicit trace space and record **where it came from, where it went, what happened to it, through which handoffs or transformations it passed, and which evidence supports each trace link**.

The broadened method retains provenance/origin tracking as one important subcase, but is no longer limited to origin/derivation alone.

## Scope families

DSD Tracking may trace, when declared and supported:

- **origin/source tracking** — source, copy, edition, extraction, import, citation, derivation;
- **transformation/version tracking** — edit, translation, conversion, aggregation, compression, schema/model version, representation change;
- **process/stage tracking** — processing stage, workflow step, method handoff, acceptance/rejection state, transition record;
- **location/container tracking** — where an artifact or record resides when a location/container identity is explicitly supplied;
- **actor/responsibility/ownership tracking** — author, operator, custodian, reviewer, responsible unit, ownership/custody handoff when relevant;
- **evidence/support tracking** — which evidence, witness, record, bridge, or source supports each link;
- **status tracking** — claim-relevant declared status changes without silently converting unknown, missing, inapplicable, or undefined states;
- **reference/dependency tracking** — explicit references, dependencies, upstream/downstream handoffs, and broken or ambiguous links;
- **trace-gap tracking** — missing links, conflicting links, ambiguous paths, unverifiable segments, and scope-limited traces.

## Primary DSD sources

Typical DSD inputs may include:

```text
formation traces
typed status records
support-retaining records
source/version locks
explicit bridges
Transformation ledgers
Aggregation/Compression sidecars
Dynamics transition records
Lineage handoffs when successor identity is separately established
```

No optional source is mandatory when the declared tracking task does not require it.

## Typical outputs

- trace target and trace scope;
- trace-node and trace-link ledger;
- source/origin record where applicable;
- version/edit/translation/transformation history;
- process/stage and method-handoff history;
- location/container and custody/responsibility history where supplied;
- reference/dependency graph or ordered trace;
- evidence/support record for each claim-relevant link;
- missing-link, ambiguous-link, conflicting-link, and out-of-scope records;
- status-change ledger;
- explicit handoff to Lineage when successor identity must be decided rather than merely traced.

## Boundary with neighboring methods

### Tracking vs Lineage

```text
Tracking:
  follows and records traceable links, states, locations, versions, handoffs, actors,
  and evidence across the declared trace scope.

Lineage:
  determines predecessor/successor identity, inheritance, split/merge/replacement,
  and identity preservation across change.
```

A tracked temporal or transformation chain does not automatically establish successor identity.

```text
TRACE_CONTINUITY != LINEAGE_IDENTITY
TEMPORAL_ADJACENCY != SUCCESSOR_RELATION
SAME_LABEL_ACROSS_TRACE != SAME_ENTITY
```

### Tracking vs Reconstruction

Tracking records supported or explicitly unresolved links. Reconstruction infers compatible hidden, missing, damaged, compressed, or past structure from incomplete evidence.

```text
MISSING_TRACE_LINK != LICENSE_TO_RECONSTRUCT
RECONSTRUCTED_LINK != ESTABLISHED_TRACE_LINK
```

### Tracking vs Audit

Tracking constructs/reports the trace. Audit evaluates whether work, evidence, procedure, or claims conform to declared rules and standards.

```text
TRACE_RECORD != AUDIT_VERDICT
```

### Tracking vs Transformation

Transformation performs or characterizes source-to-target mapping and preservation/loss. Tracking may record that such a transformation occurred and connect its source/result artifacts, but does not replace the Transformation operation.

### Tracking vs Interpretation

Tracking records source/context/reference chains when supplied. Interpretation evaluates a meaning-bearing reading through source/context/bridge constraints.

## Core guards

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
LOCATION_CHANGE != FORMATION_CHANGE
VERSION_CHANGE != LINEAGE_CHANGE
MISSING_LINK != NEGATIVE_LINK
AMBIGUOUS_LINK != LICENSE_TO_CHOOSE_POST_HOC
RECONSTRUCTED_LINK != ESTABLISHED_TRACE_LINK
TRACE_RECORD != AUDIT_VERDICT
```

## Scope limit

Tracking establishes only the trace relations supported by the declared records and bridges.

It does **not** automatically establish:

- truth or authenticity;
- causality;
- legal responsibility or ownership merely from possession/custody;
- predecessor/successor identity;
- hidden missing links;
- correctness of a transformation;
- correctness of an interpretation;
- empirical validity of a model;
- conformance/audit success.

The legacy directory name `provenance/` is retained only for path compatibility. New method-family records should use **Tracking / DSD 추적론** as the method name and treat **Provenance** as a narrower historical/origin-tracking subcase.
