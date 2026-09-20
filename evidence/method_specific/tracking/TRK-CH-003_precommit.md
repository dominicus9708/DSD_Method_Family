# TRK-CH-003 Precommit — Direct Method-Boundary Challenge

Status: **PROSPECTIVELY FROZEN / NOT YET EXECUTED**  
Date: **2026-09-21**  
Case ID: `TRK-CH-003`  
Case class: `direct_method_boundary_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen comparators

```text
TRACKING_PROTOCOL_COMMIT:
  a0d979325c11919fecaa4d8eab129477a365af87

TRACKING_PROTOCOL_BLOB:
  72e9cc8576ae87e088bdf2f8ebb3d7016c2894c1

METHOD_FAMILY_REGISTRY_COMMIT_AT_PRECOMMIT:
  6fe215e3f393f00e227a087b72a7803ee12f2399

METHOD_FAMILY_REGISTRY_BLOB:
  00cfc102fa3d838b7b05c122871112b7bab32dd6

METHOD_BOUNDARY_MATRIX_COMMIT_AT_PRECOMMIT:
  ced69912a2501761dbf733e99789d1ddadbe0587

METHOD_BOUNDARY_MATRIX_BLOB:
  bf2e9771db16abcf0323d4ed8eebcb771a7634f9
```

Tracking Protocol v0.1 is immutable for this challenge.

Neighboring-method descriptions are used only as current registry/task definitions.

This case does not validate, mature, or independently verify any neighboring method.

## 2. Purpose

Test whether Tracking's binding operation remains distinct under fair shared-artifact access from:

```text
B1  Lineage
B2  Reconstruction
B3  Transformation
B4  Audit
B5  Interpretation
B6  Measurement
B7  Aggregation
B8  Compression
B9  Comparison
B10 Analysis
```

Allowed boundary outcomes:

```text
DISTINCT_BINDING_OPERATION_WITH_SHARED_ARTIFACTS
PARTIAL_OVERLAP_NOT_COLLAPSE
EXACT_COLLAPSE_CANDIDATE
UNRESOLVED_BOUNDARY
```

No boundary result may be promoted to permanent method-registry survival, permanent irreducibility, or a merger/deletion decision.

## 3. Fair shared-artifact packet TRK-SP-003

Every boundary comparison receives the same claim-relevant packet.

### 3.1 Node identities

```text
SRC0       source artifact / version s1
DOC1       document artifact / version v1
DOC2       document artifact / version v2
PDF1       transformed artifact / version pdf1
LEGACY1    legacy artifact / version l1
OBS1       measurement record / version m1
AGG1       aggregate record / version a1
CMP1       compressed record / version c1
CTX1       context/source record / version x1
REP1       comparison report / version r1
ANA1       analysis report / version n1
INT1       interpretation report / version i1
AUD1       audit report / version u1
```

### 3.2 Direct trace evidence

```text
E01:
  SRC0 SOURCE_OF DOC1

E02:
  DOC1 EDITED_TO DOC2

E03:
  DOC2 TRANSFORMATION_HANDOFF_TO PDF1

E04:
  PDF1 METHOD_HANDOFF_TO OBS1
  source method: Measurement

E05:
  OBS1 METHOD_HANDOFF_TO AGG1
  source method: Aggregation

E06:
  AGG1 METHOD_HANDOFF_TO CMP1
  source method: Compression

E07:
  CTX1 SOURCE_OF INT1

E08:
  DOC2 METHOD_HANDOFF_TO REP1
  source method: Comparison

E09:
  DOC2 METHOD_HANDOFF_TO ANA1
  source method: Analysis

E10:
  DOC2 METHOD_HANDOFF_TO INT1
  source method: Interpretation

E11:
  DOC2 METHOD_HANDOFF_TO AUD1
  source method: Audit
```

All E01-E11 are supplied applicable evidence records with independent evidence IDs and provenance.

### 3.3 Frozen missing-history query

Required Tracking query:

```text
QGAP:
  DOC2 COPIED_TO LEGACY1
```

Direct support:

```text
absent
```

Explicit negation:

```text
absent
```

Required relation schema/access:

```text
available
```

Therefore Tracking's own expected relation status is:

```text
TRACKING_LINK_MISSING
```

### 3.4 Reconstruction candidate packet

A separate Reconstruction input packet is supplied:

```text
R-A:
  compatible history candidate:
  DOC2 COPIED_TO LEGACY1

R-B:
  compatible history candidate:
  SRC0 COPIED_TO LEGACY1

available evidence:
  does not eliminate either candidate
```

No Reconstruction result is preloaded as a historical fact.

If a Reconstruction task is executed, its binding operation is to infer/retain the admissible reconstruction set.

Tracking may later record such a result only as a Reconstruction handoff sidecar.

### 3.5 Lineage packet

Frozen continuity evidence:

```text
DOC1 EDITED_TO DOC2
DOC2 TRANSFORMATION_HANDOFF_TO PDF1
```

Explicit Lineage successor-identity handoff:

```text
absent
```

The Lineage task, if invoked, asks whether predecessor/successor identity across change is justified.

Tracking's task is only to record the supported typed trace links.

### 3.6 Transformation packet

Supplied map descriptor:

```text
MAP M:
  DOC2 -> PDF1

declared preservation target:
  text body preserved

declared loss question:
  editability metadata may be omitted

Transformation evaluation result:
  not preloaded
```

Transformation, if invoked, evaluates preservation/loss under its task.

Tracking records only the existence and provenance of E03 until a Transformation result is handed off.

### 3.7 Audit packet

Checklist:

```text
A-REQ-1 scope/version locked
A-REQ-2 evidence provenance retained
A-REQ-3 no unsupported direct link created
A-REQ-4 reconstructed candidate not promoted to historical fact
```

Audit, if invoked, evaluates a performed record/process against those criteria.

Tracking itself constructs the trace ledger and emits Tracking conformance, not an Audit verdict.

### 3.8 Interpretation packet

```text
CTX1:
  source/context record

two admissible readings of DOC2 phrase P:
  I-A
  I-B

precedence:
  none
```

Interpretation, if invoked, evaluates readings under source/context/bridge constraints.

Tracking records source/context/report links and does not choose I-A/I-B as the meaning of DOC2.

### 3.9 Measurement packet

```text
alternatives:
  H0, H1

candidate readout m:
  H0 -> LOW
  H1 -> HIGH

decision rule:
  LOW/HIGH fixed

observed result:
  absent
```

Measurement, if invoked, evaluates discrimination sufficiency.

Tracking may record provenance and handoff of OBS1 but does not turn traceability into a discrimination verdict.

### 3.10 Aggregation packet

```text
components:
  +1, -1

aggregation rule:
  SUM

AGG1:
  0

collision sidecar:
  another support {0} may also map to 0
```

Aggregation, if invoked, constructs/evaluates the declared aggregate and its collision/injectivity limits.

Tracking records OBS1 -> AGG1 and the supplied sidecar without reconstructing support from AGG1 alone.

### 3.11 Compression packet

```text
input representation:
  AGG1 + status sidecar

compression map:
  C1

output:
  CMP1

retained distinction objective:
  retain aggregate value + collision-warning bit
```

Compression, if invoked, evaluates the representation reduction against the declared purpose.

Tracking records AGG1 -> CMP1 as a handoff and does not judge compression quality.

### 3.12 Comparison packet

```text
subjects:
  DOC1, DOC2

supplied correspondence map:
  field A <-> field A
  field B <-> field B

comparison criteria:
  field equality + declared edit markers

comparison report:
  not preloaded
```

Comparison, if invoked, emits correspondence/divergence/equivalence outputs.

Tracking records the existence/provenance of REP1 when supplied as a handoff but does not derive structural equivalence from E02.

### 3.13 Analysis packet

```text
target:
  DOC2

declared decomposition:
  header
  body
  references

analysis result:
  not preloaded
```

Analysis, if invoked, structurally decomposes and re-expresses DOC2.

Tracking records the Analysis handoff relation to ANA1 but does not perform that decomposition.

## 4. Tracking binding operation on TRK-SP-003

Tracking must, using its own frozen protocol:

```text
1 lock target/scope/dimensions/query set;
2 retain all node identities/versions/types;
3 type E01-E11 by relation and direction;
4 retain evidence provenance separately;
5 construct the typed graph;
6 mark QGAP as TRACKING_LINK_MISSING;
7 keep Reconstruction candidates out of established history;
8 keep Lineage identity absent unless handed off;
9 preserve Aggregation/Compression loss sidecars;
10 preserve method-handoff identities;
11 emit Tracking terminal/conformance/max-claim records.
```

For the frozen Tracking query set:

```text
required direct links:
  E01-E11
required gap query:
  QGAP
```

Expected run-level terminal:

```text
TRACKING_TRACE_PARTIAL
```

because supported trace content exists while QGAP remains missing.

## 5. Boundary expectations

### B1 — Lineage

Shared:

```text
DOC1, DOC2, PDF1
edit/transformation continuity
version records
```

Lineage binding operation:

```text
determine predecessor/successor identity, inheritance,
split/merge/replacement across change
```

Tracking binding operation:

```text
record supported typed trace links and gaps
without deciding identity from continuity
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
TRACE_CONTINUITY != LINEAGE_IDENTITY
```

### B2 — Reconstruction

Shared:

```text
QGAP
R-A / R-B candidate histories
available evidence
```

Reconstruction binding operation:

```text
infer/retain compatible prior or missing histories
under incomplete evidence
```

Tracking binding operation:

```text
mark direct trace gap MISSING and keep any Reconstruction result
in a non-established sidecar unless direct evidence later establishes it
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
RECONSTRUCTED_LINK != ESTABLISHED_TRACE_LINK
```

### B3 — Transformation

Shared:

```text
DOC2
PDF1
map M
preservation/loss question
```

Transformation binding operation:

```text
evaluate source-to-target mapping,
preservation, omission, addition, loss, reconstructibility
```

Tracking binding operation:

```text
record the typed Transformation handoff and provenance
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
TRACE_OF_TRANSFORMATION != TRANSFORMATION_CORRECTNESS
```

### B4 — Audit

Shared:

```text
trace records
evidence provenance
A-REQ-1..A-REQ-4
```

Audit binding operation:

```text
retrace/evaluate performed work against declared criteria
and emit an Audit verdict
```

Tracking binding operation:

```text
construct the trace record and Tracking terminal/conformance
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
TRACE_RECORD != AUDIT_VERDICT
```

### B5 — Interpretation

Shared:

```text
DOC2
CTX1
source/context links
I-A / I-B
```

Interpretation binding operation:

```text
evaluate supported readings under source/context/bridge constraints
```

Tracking binding operation:

```text
record source/context/report links without choosing meaning
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
TRACE_CONTEXT != INTERPRETATION_RESULT
```

### B6 — Measurement

Shared:

```text
H0/H1
candidate readout m
decision rule
OBS1 provenance
```

Measurement binding operation:

```text
evaluate whether supplied/proposed readouts discriminate declared alternatives
at the declared resolution
```

Tracking binding operation:

```text
record OBS1 source/handoff/provenance links
without emitting Measurement sufficiency
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
TRACE_OF_MEASUREMENT != DISCRIMINATION_SUFFICIENCY
```

### B7 — Aggregation

Shared:

```text
component values
SUM operation
AGG1
collision sidecar
```

Aggregation binding operation:

```text
construct/evaluate the declared aggregate readout
and preserve collision/injectivity limits
```

Tracking binding operation:

```text
record OBS1 -> AGG1 and supplied sidecars
without reconstructing support
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
TRACE_OF_AGGREGATE != AGGREGATION_OPERATION
```

### B8 — Compression

Shared:

```text
AGG1
C1
CMP1
retention objective
```

Compression binding operation:

```text
reduce representation under the declared downstream purpose
and evaluate retained/destructive distinctions
```

Tracking binding operation:

```text
record AGG1 -> CMP1 and the compression handoff/provenance
without judging compression adequacy
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
TRACE_OF_COMPRESSION != COMPRESSION_SUCCESS
```

### B9 — Comparison

Shared:

```text
DOC1
DOC2
correspondence map
comparison criteria
```

Comparison binding operation:

```text
determine justified correspondence/divergence/equivalence
within declared comparison coverage
```

Tracking binding operation:

```text
record DOC1 -> DOC2 edit trace and Comparison report handoff
without converting trace continuity into structural equivalence
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
TRACE_RELATION != COMPARISON_VERDICT
```

### B10 — Analysis

Shared:

```text
DOC2
declared decomposition targets
ANA1 handoff identity
```

Analysis binding operation:

```text
decompose and structurally re-express one declared target
```

Tracking binding operation:

```text
record source/version/method-handoff relations
without performing internal decomposition
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
TRACE_OF_ANALYSIS != STRUCTURAL_DECOMPOSITION
```

## 6. Exact-collapse criterion

A neighbor is an `EXACT_COLLAPSE_CANDIDATE` only if executing that neighboring method's own current declared task under equal access to TRK-SP-003 materially reproduces Tracking's:

```text
task/scope/dimension/query locks
typed node/version register
typed directed relation register
relation-vs-evidence/provenance separation
link-status ledger including unresolved statuses
graph/path topology
gap/ambiguity/conflict/blockage semantics
neighboring-method handoff ledger
reconstructed-vs-established separation
trace-level terminal
Tracking-specific conformance/gain/max-claim outputs
```

Sharing artifacts, traversing relations, citing provenance, or producing one overlapping ledger is insufficient for exact collapse.

## 7. Frozen scoring — 72 checks

### A. Common fairness / immutability — 12

```text
A1 Tracking protocol identity fixed
A2 registry commit/blob fixed
A3 boundary-matrix commit/blob fixed
A4 all ten neighboring methods named before execution
A5 same TRK-SP-003 packet available to all boundary comparisons
A6 no neighbor denied a claim-relevant artifact available to Tracking
A7 no Tracking link-status or terminal preloaded as a neighbor output
A8 QGAP remains unsupported by direct evidence
A9 Reconstruction candidates remain candidates, not historical facts
A10 no protocol/registry/boundary wording changed after precommit
A11 no external application
A12 method gain remains NOT_ASSESSED
```

### B. Ten method-boundary groups — 50

For each B1-B10:

```text
1 shared artifacts identified
2 neighboring binding operation stated without replacing it by Tracking
3 Tracking binding operation stated
4 output-contract difference preserved
5 exact collapse not asserted unless exact-collapse criterion is met
```

```text
B1-B10 subtotal: 50
```

### C. Global boundary discipline — 10

```text
C1 trace continuity != Lineage identity
C2 missing trace link != Reconstruction result
C3 transformation trace != Transformation correctness
C4 trace record != Audit verdict
C5 trace context/source link != Interpretation result
C6 measurement trace != discrimination sufficiency
C7 aggregate trace != Aggregation operation
C8 compression trace != Compression success
C9 trace relation != Comparison verdict
C10 trace of Analysis != structural decomposition
```

```text
TOTAL_REQUIRED_CHECKS: 72
PASS_THRESHOLD: 72/72
PARTIAL_PASS_ALLOWED: no
```

Any unexpected exact collapse or unresolved boundary must remain visible.

## 8. Allowed result summary

If all ten pairs satisfy the frozen non-collapse criterion:

```text
BOUNDARY_PAIRS_TESTED: 10
EXACT_COLLAPSE_PAIRS: 0
UNRESOLVED_BOUNDARY_PAIRS: 0
PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS: 10

BOUNDARY_STATUS:
  FIXTURE_BOUNDED_SEPARATION_ESTABLISHED
```

This establishes only fixture-bounded separation in the constructed packet.

It does not establish permanent method survival, permanent irreducibility, or future non-overlap.

## 9. Allowed counter changes on 72/72 PASS

```text
DIRECT_TRACKING_PILOTS_ATTEMPTED:
  2 -> 3

SUCCESSFUL_DIRECT_TRACKING_PILOTS:
  2 -> 3

METHOD_BOUNDARY_TRACKING_CASES:
  0 -> 1
```

Unchanged:

```text
POSITIVE_TRACKING_CASES: 1
NEGATIVE_OR_FAILURE_TRACKING_CASES: 1

ALL_NINE_LINK_STATUSES_DIRECTLY_EXERCISED: yes
ALL_SIX_TRACE_TERMINALS_DIRECTLY_EXERCISED: yes

BASELINE_TRACKING_CASES: 0
NO_GAIN_TRACKING_CASES: 0
STRONGEST_REASONABLE_BASELINE_TRACKING: not established
REPRODUCIBILITY_CASES: 0

EXTERNAL_TRACKING_APPLICATIONS: 0
INDEPENDENT_TRACKING_VALIDATION: not established
INDEPENDENT_REPLICATION: not established

TRACKING_INTERNAL_STANDARDIZATION_STATUS: developing
CURRENT_TRACKING_EVIDENCE_STATUS: validation_in_progress

PROTOCOL_REVISION_REQUIRED: no unless contradiction found
SHARED_CORE_REOPEN_REQUIRED: no unless contradiction found
```
