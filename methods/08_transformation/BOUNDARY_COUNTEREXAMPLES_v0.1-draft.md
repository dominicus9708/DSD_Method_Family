# DSD Transformation Boundary Counterexamples v0.1 — pre-protocol attack record

Status: **18 pre-protocol boundary attacks completed**  
Date: **2026-09-16**

Purpose: pressure the Transformation Task Interface before protocol freeze. These are constructed internal counterexamples, not external validation cases.

## Results summary

```text
BOUNDARY_ATTACKS_RUN: 18
PRESERVED_NO_REFINEMENT: 10
PRESERVED_WITH_NONBREAKING_REFINEMENT: 8
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
```

## Attack ledger

### B1 — equal scalar output, different component structure

Two source states produce the same final scalar target but differ in claim-relevant component structure.

Required result: target equality does not establish faithful structural transformation.

```text
SAME_TARGET_OUTPUT != FAITHFUL_TRANSFORMATION
```

Outcome: preserved; supports explicit information-loss ledger.

### B2 — undefined collapsed to numeric zero

A source carrier is applicable but undefined; the target format has a numeric zero field.

Required result: do not silently encode undefined as zero unless an explicit encoding bridge says so, and even then preserve provenance.

Outcome: **refinement R2**.

### B3 — missing source field filled by target default

Target schema requires a field absent from the source and supplies default `0`.

Required result:

```text
TARGET_DEFAULT != SOURCE_DERIVED_VALUE
```

Outcome: **refinement R3**.

### B4 — many-to-one normalization

Distinct source tokens `{A,a}` both normalize to `a`.

Required result: record merge/collision; normalized endpoint equality does not establish source identity.

Outcome: preserved; supports R2/R4.

### B5 — one-to-many expansion

One source carrier expands into two target carriers through a declared decomposition rule.

Required result: distinguish split mapping from duplicated evidence.

Outcome: **refinement R2**.

### B6 — partial map outside domain

Transformation rule is defined only for source subset `D`; supplied source `x` lies outside `D`.

Required result: do not fabricate a target value or silently totalize the map.

```text
PARTIAL_MAP != TOTAL_MAP
```

Outcome: **refinement R1**.

### B7 — inverse exists only on a subset

Forward map is many-to-one globally but injective on a declared subset.

Required result: reversibility claim must carry scope.

Outcome: **refinement R5**.

### B8 — target schema cannot represent source status

Source distinguishes missing, undefined, zero, and nonzero; target schema has only a nullable numeric field.

Required result: loss must be explicit even when every source record can be serialized.

Outcome: preserved; supports R2/R4.

### B9 — unit conversion without conversion bridge

Source is in unit U1, target expects U2, but no conversion relation is supplied.

Required result: transformation is blocked rather than numerically copied.

Outcome: preserved.

### B10 — version-sensitive schema migration

Map valid for source schema v1 is applied to v2, where one field changed semantics.

Required result: source/target/map versions must be frozen.

Outcome: **refinement R8**.

### B11 — aggregation masquerading as transformation

A component vector is replaced by its sum.

Required result: the operation may be consumed as an Aggregation handoff, but Transformation must not relabel aggregate equality as carrier preservation.

Outcome: preserved.

### B12 — compression masquerading as transformation

A source representation is encoded into fewer bits with a reconstruction tolerance objective.

Required result: Compression's reconstruction/error objective remains separate; Transformation may record the encoding only through an explicit handoff.

Outcome: preserved.

### B13 — design/synthesis confusion

A target field is newly invented to satisfy a design requirement rather than derived by a source-to-target rule.

Required result: target creation by Design/Synthesis is not source preservation.

Outcome: preserved; supports R3.

### B14 — two-stage chain hides intermediate loss

`A -> B -> C` ends at a numerically matching C even though A distinctions were collapsed at B and later reintroduced from a default table.

Required result:

```text
CHAIN_ENDPOINT_MATCH != LOSSLESS_INTERMEDIATE_CHAIN
```

Outcome: **refinement R6**.

### B15 — sample round-trip succeeds but global inverse fails

A few test inputs satisfy `G(F(x))=x`, but other inputs collide under F.

Required result: sample success cannot support a global invertibility claim.

Outcome: preserved; supports R5.

### B16 — stochastic transformation

Transformation emits one of several target states under an explicit random policy.

Required result: output cannot be treated as deterministic unless random mechanism/seed or distributional semantics are frozen.

Outcome: **refinement R7**.

### B17 — time/version-dependent transformation chain

Identical source token at `t0` and `t1` maps differently because the active target schema changes.

Required result: temporal/version scope must be explicit; same source token does not imply same target meaning across regimes.

Outcome: **refinement R8**.

### B18 — external enrichment inserted during conversion

A target record contains a field obtained from an auxiliary lookup rather than the source.

Required result: enrichment must be `TARGET_ADDED_NOT_SOURCE_DERIVED` with provenance rather than treated as preservation.

Outcome: **refinement R3**.

## Refinement groups forced

```text
R1 transformation/map identity, version, domain, codomain, applicability
R2 carrier correspondence plus split/merge/status-preservation taxonomy
R3 target addition/default/enrichment provenance
R4 information-loss, collision, injectivity, reconstruction limits
R5 inverse/reversibility scope and sample-vs-global discipline
R6 composed-chain/intermediate-stage provenance and loss retention
R7 stochastic/nondeterministic policy and replay semantics
R8 temporal/schema-version scope and migration semantics
```

No attack requires collapsing Transformation into Design, Synthesis, Aggregation, Compression, Comparison, Interpretation, or Computation.

The historical Task Interface remains unchanged. Refinements are added prospectively through Boundary Amendment 001.
