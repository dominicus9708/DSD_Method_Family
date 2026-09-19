# DSD Tracking Boundary Counterexamples v0.1 — pre-protocol attack record

Status: **18 pre-protocol boundary attacks completed**  
Date: **2026-09-20**

Purpose: pressure the broadened Tracking Task Interface before protocol freeze.

These are constructed internal counterexamples.

They are not external validation.

## Results summary

```text
BOUNDARY_ATTACKS_RUN: 18
PRESERVED_NO_REFINEMENT: 8
PRESERVED_WITH_NONBREAKING_REFINEMENT: 10
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
```

## Attack ledger

### B1 — same label across two versions

Two artifacts both carry label `report-final`, but their version identities and content hashes differ.

Required:

```text
SAME_LABEL != SAME_ENTITY
```

Tracking must lock node identity/version rather than merge by label.

Outcome: **refinement R2**.

### B2 — temporal adjacency without relation evidence

Artifact B appears immediately after artifact A in a workflow timeline, but no supplied record states that A produced B or that B succeeds A.

Required:

```text
TEMPORAL_ADJACENCY != TRACE_LINK
TEMPORAL_ADJACENCY != SUCCESSOR_RELATION
```

Outcome: **refinement R3 / R7**.

### B3 — missing intermediate link

A source S and later artifact T are known, but the intermediate derivation record is absent.

Required:

```text
MISSING_LINK != LICENSE_TO_RECONSTRUCT
```

Tracking must report a gap rather than invent the missing history.

Outcome: **refinement R6 / R8**.

### B4 — conflicting provenance claims

Record E1 states `S1 -> T`; record E2 states `S2 -> T`. Both are admissible under the supplied scope and no precedence rule exists.

Required:

```text
CONFLICTING_LINKS != LICENSE_TO_DISCARD_ONE
```

Outcome: **refinement R4 / R6**.

### B5 — evidence points to a source whose authenticity is unknown

A document's chain of copies is well recorded, but the original document has not been authenticated.

Required:

```text
TRACKED != AUTHENTIC
TRACKED != TRUE
```

Outcome: preserved.

### B6 — tracked transformation with unknown correctness

A migration record explicitly states that V1 was converted to V2, but no Transformation result establishes whether required information was preserved.

Required:

```text
TRACE_OF_TRANSFORMATION != TRANSFORMATION_CORRECTNESS
```

Outcome: **refinement R8**.

### B7 — aggregate output with lost support

A trace records raw records entering Aggregation and scalar output `0`, while the sidecar states the aggregation is noninjective.

Required:

```text
TRACE_OF_AGGREGATE != RECONSTRUCTION_OF_SUPPORT
EQUAL_AGGREGATE != EQUAL_SUPPORT
```

Outcome: preserved; supports R8.

### B8 — custody mistaken for ownership

Actor A physically holds an artifact, while ownership belongs to actor B.

Required:

```text
CUSTODY_RELATION != OWNERSHIP_RELATION
```

Outcome: **refinement R7**.

### B9 — ownership mistaken for responsibility

Actor A owns a system; actor B performed the logged operation.

Required:

```text
OWNERSHIP_RELATION != RESPONSIBILITY_RELATION
```

Outcome: **refinement R7**.

### B10 — location change mistaken for formation change

The same locked artifact identifier moves from container C1 to C2.

Required:

```text
LOCATION_CHANGE != FORMATION_CHANGE
```

Outcome: preserved; supports R7.

### B11 — version change mistaken for Lineage change

A document version changes from v1 to v2 under one versioning system, but no supplied Lineage relation decides identity preservation.

Required:

```text
VERSION_CHANGE != LINEAGE_CHANGE
TRACE_CONTINUITY != LINEAGE_IDENTITY
```

Outcome: **refinement R8**.

### B12 — one source branches to several outputs

S is explicitly copied to T1 and T2.

A linear-chain representation would discard one valid branch.

Required: Tracking must permit branching graph structure.

Outcome: **refinement R5**.

### B13 — several sources merge into one output

S1 and S2 are both supplied inputs to T.

A single-parent trace would erase one supported source relation.

Required: Tracking must permit multi-source / merge-shaped graphs.

Outcome: **refinement R5**.

### B14 — cyclic reference/dependency graph

A references B, B references C, and C references A.

Required: reference/dependency tracking must not assume every trace is acyclic or temporally ordered.

Outcome: **refinement R5**.

### B15 — process order promoted to causality

Step P1 precedes P2 and P2 precedes P3, but no causal bridge is supplied.

Required:

```text
PROCESS_ORDER != CAUSAL_LINK
```

Outcome: preserved; supports R7.

### B16 — reconstructed link fed back as historical fact

A Reconstruction handoff proposes candidate missing link `X -> Y`, and downstream text silently records it as an established trace link.

Required:

```text
RECONSTRUCTED_LINK != ESTABLISHED_TRACE_LINK
```

Outcome: **refinement R8**.

### B17 — explicit relation outside declared trace scope

The task declares version-history tracking only. A valid custody record is supplied but custody is outside the frozen trace dimensions.

Required: relation is `TRACKING_LINK_OUT_OF_SCOPE`, not missing, conflicting, or false.

Outcome: **refinement R1 / R6**.

### B18 — unbounded “trace everything” request

The request gives a target but no time range, trace dimension, endpoint, completion criterion, or allowed relation family.

Required: Tracking cannot claim completion until the trace scope and completion/query criterion are bounded.

Outcome: **refinement R1**.

## Refinement groups forced

```text
R1 tracking task / target / scope / dimension / completion lock

R2 trace-node identity / version / type / domain / status discipline

R3 typed link relation / direction / schema-version discipline

R4 evidence-support / provenance / support-strength ledger

R5 graph/path semantics for branching / merging / cycles / multi-source traces

R6 missing / negative / ambiguous / conflicting / blocked / out-of-scope distinctions

R7 temporal / process / location / custody / ownership / responsibility / causality separation

R8 neighboring-method handoffs and reconstructed-vs-established trace discipline
```

## Boundary result

No attack requires collapsing Tracking into:

```text
Lineage
Reconstruction
Transformation
Audit
Interpretation
Measurement
Aggregation
Compression
Comparison
```

The historical Task Interface remains unchanged.

R1-R8 must be adopted prospectively through Boundary Amendment 001 before Protocol v0.1 is frozen.
