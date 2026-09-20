# TRK-CH-003 — Direct Method-Boundary Challenge Result

Status: **EXECUTED — 72/72 PASS**  
Date: **2026-09-21**  
Case ID: `TRK-CH-003`  
Case class: `direct_method_boundary_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen identities

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

PRECOMMIT_COMMIT:
  8e289432301f2d8d9a294c8c5e4e66310b17a376
PRECOMMIT_BLOB:
  62353ce322882706369212b6ad34bd8e04489c0c
```

No protocol, registry task definition, shared packet, boundary criterion, or scoring item was changed after precommit.

## 2. Tracking execution on TRK-SP-003

Tracking retained all frozen node identities and the eleven directly supported typed trace links E01-E11.

The direct trace graph includes:

```text
SRC0 SOURCE_OF DOC1
DOC1 EDITED_TO DOC2
DOC2 TRANSFORMATION_HANDOFF_TO PDF1
PDF1 METHOD_HANDOFF_TO OBS1
OBS1 METHOD_HANDOFF_TO AGG1
AGG1 METHOD_HANDOFF_TO CMP1
CTX1 SOURCE_OF INT1
DOC2 METHOD_HANDOFF_TO REP1
DOC2 METHOD_HANDOFF_TO ANA1
DOC2 METHOD_HANDOFF_TO INT1
DOC2 METHOD_HANDOFF_TO AUD1
```

For the frozen gap query:

```text
QGAP:
  DOC2 COPIED_TO LEGACY1

direct support:
  absent

explicit negation:
  absent

required schema/access:
  available
```

Tracking therefore emits:

```text
QGAP:
  TRACKING_LINK_MISSING
```

The supplied Reconstruction candidates R-A and R-B are not inserted into established trace history.

Run-level result:

```text
TRACKING_TRACE_TERMINAL_STATUS:
  TRACKING_TRACE_PARTIAL

TRACKING_PROTOCOL_CONFORMANCE:
  CONFORMANT

TRACKING_METHOD_GAIN_STATUS:
  NOT_ASSESSED
```

The terminal is partial because supported trace content exists while QGAP remains unresolved.

## 3. B1 — Lineage boundary

Shared artifacts:

```text
DOC1
DOC2
PDF1
version/edit continuity
Transformation handoff
```

Lineage binding operation:

```text
determine predecessor/successor identity,
inheritance, split/merge/replacement across change
```

Tracking binding operation:

```text
record the supplied EDITED_TO and Transformation handoff links,
their direction, evidence, and provenance,
without deriving identity from continuity
```

No explicit Lineage handoff is supplied.

Therefore Tracking does not infer successor identity.

```text
TRACE_CONTINUITY != LINEAGE_IDENTITY
VERSION_CHANGE != LINEAGE_CHANGE
```

Boundary result:

```text
B1:
  PARTIAL_OVERLAP_NOT_COLLAPSE
```

Checks B1.1-B1.5: **5/5 PASS**.

## 4. B2 — Reconstruction boundary

Shared artifacts:

```text
QGAP
R-A
R-B
incomplete direct evidence
```

Reconstruction binding operation:

```text
infer and preserve compatible missing/prior histories
under incomplete evidence
```

Tracking binding operation:

```text
emit TRACKING_LINK_MISSING for the unsupported direct relation,
and keep later Reconstruction outputs in a non-established sidecar
unless separate direct evidence establishes them
```

Tracking does not select R-A or R-B.

```text
MISSING_TRACE_LINK != LICENSE_TO_RECONSTRUCT
RECONSTRUCTED_LINK != ESTABLISHED_TRACE_LINK
```

Boundary result:

```text
B2:
  PARTIAL_OVERLAP_NOT_COLLAPSE
```

Checks B2.1-B2.5: **5/5 PASS**.

## 5. B3 — Transformation boundary

Shared artifacts:

```text
DOC2
PDF1
map M
declared preservation/loss question
```

Transformation binding operation:

```text
evaluate source-to-target mapping,
preservation, omission, addition, loss, and reconstructibility
```

Tracking binding operation:

```text
record the existence, direction, source artifact,
target artifact, and provenance of the Transformation handoff
```

Tracking does not decide whether text-body preservation succeeded or editability metadata was acceptably lost.

```text
TRACE_OF_TRANSFORMATION != TRANSFORMATION_CORRECTNESS
```

Boundary result:

```text
B3:
  PARTIAL_OVERLAP_NOT_COLLAPSE
```

Checks B3.1-B3.5: **5/5 PASS**.

## 6. B4 — Audit boundary

Shared artifacts:

```text
trace records
evidence provenance
A-REQ-1..A-REQ-4
```

Audit binding operation:

```text
retrace/evaluate performed work against declared scope,
evidence, procedure, and criteria, then emit an Audit verdict
```

Tracking binding operation:

```text
construct the trace ledger, unresolved-status ledger,
trace terminal, and Tracking conformance
```

Tracking conformance is internal protocol conformance, not the supplied Audit task's verdict.

```text
TRACE_RECORD != AUDIT_VERDICT
TRACKING_CONFORMANCE != AUDIT_RESULT
```

Boundary result:

```text
B4:
  PARTIAL_OVERLAP_NOT_COLLAPSE
```

Checks B4.1-B4.5: **5/5 PASS**.

## 7. B5 — Interpretation boundary

Shared artifacts:

```text
DOC2
CTX1
source/context relation
I-A
I-B
```

Interpretation binding operation:

```text
evaluate supported readings under source identity,
contextual prerequisites, and interpretive bridges
```

Tracking binding operation:

```text
record the source/context/report trace links and their provenance
without selecting the meaning of DOC2
```

No reading is chosen by Tracking.

```text
TRACE_CONTEXT != INTERPRETATION_RESULT
SOURCE_TRACE != MEANING_VERDICT
```

Boundary result:

```text
B5:
  PARTIAL_OVERLAP_NOT_COLLAPSE
```

Checks B5.1-B5.5: **5/5 PASS**.

## 8. B6 — Measurement boundary

Shared artifacts:

```text
H0
H1
candidate readout m
LOW/HIGH rule
OBS1 provenance
```

Measurement binding operation:

```text
evaluate whether the supplied/proposed readout
distinguishes the declared alternatives at the declared resolution
```

Tracking binding operation:

```text
record the Measurement artifact/handoff provenance
and its position in the trace graph
```

Tracking does not emit a discrimination verdict from provenance alone.

```text
TRACE_OF_MEASUREMENT != DISCRIMINATION_SUFFICIENCY
```

Boundary result:

```text
B6:
  PARTIAL_OVERLAP_NOT_COLLAPSE
```

Checks B6.1-B6.5: **5/5 PASS**.

## 9. B7 — Aggregation boundary

Shared artifacts:

```text
components +1,-1
SUM operation
AGG1=0
collision sidecar
```

Aggregation binding operation:

```text
construct/evaluate the declared aggregate readout
and preserve collision/injectivity limits
```

Tracking binding operation:

```text
record OBS1 -> AGG1 as a typed method handoff
and retain the supplied collision sidecar
```

Tracking does not construct SUM and does not reconstruct original support from the aggregate.

```text
TRACE_OF_AGGREGATE != AGGREGATION_OPERATION
EQUAL_AGGREGATE != EQUAL_SUPPORT
```

Boundary result:

```text
B7:
  PARTIAL_OVERLAP_NOT_COLLAPSE
```

Checks B7.1-B7.5: **5/5 PASS**.

## 10. B8 — Compression boundary

Shared artifacts:

```text
AGG1
compression map C1
CMP1
retained-distinction objective
```

Compression binding operation:

```text
reduce representation under the declared downstream purpose
and evaluate retained versus destructive distinctions
```

Tracking binding operation:

```text
record AGG1 -> CMP1 and the Compression handoff/provenance
without judging compression adequacy
```

```text
TRACE_OF_COMPRESSION != COMPRESSION_SUCCESS
```

Boundary result:

```text
B8:
  PARTIAL_OVERLAP_NOT_COLLAPSE
```

Checks B8.1-B8.5: **5/5 PASS**.

## 11. B9 — Comparison boundary

Shared artifacts:

```text
DOC1
DOC2
field correspondence map
comparison criteria
```

Comparison binding operation:

```text
determine justified correspondence, divergence,
equivalence, or bounded noncorrespondence
```

Tracking binding operation:

```text
record DOC1 EDITED_TO DOC2 and the Comparison-report handoff
without converting trace continuity into structural equivalence
```

```text
TRACE_RELATION != COMPARISON_VERDICT
EDIT_HISTORY != STRUCTURAL_EQUIVALENCE
```

Boundary result:

```text
B9:
  PARTIAL_OVERLAP_NOT_COLLAPSE
```

Checks B9.1-B9.5: **5/5 PASS**.

## 12. B10 — Analysis boundary

Shared artifacts:

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
without decomposing DOC2
```

```text
TRACE_OF_ANALYSIS != STRUCTURAL_DECOMPOSITION
```

Boundary result:

```text
B10:
  PARTIAL_OVERLAP_NOT_COLLAPSE
```

Checks B10.1-B10.5: **5/5 PASS**.

## 13. Exact-collapse review

The frozen exact-collapse criterion required a neighboring method, by executing its own current task, to materially reproduce Tracking's full combination of:

```text
scope/dimension/query locks
typed node/version records
typed directed relation records
relation/evidence provenance separation
link-status ledger
graph/path topology
gap/ambiguity/conflict/blockage semantics
neighboring-method handoff ledger
reconstructed-vs-established separation
trace terminal
Tracking conformance/gain/max-claim outputs
```

No tested neighbor did so under TRK-SP-003.

Result:

```text
BOUNDARY_PAIRS_TESTED: 10
EXACT_COLLAPSE_PAIRS: 0
UNRESOLVED_BOUNDARY_PAIRS: 0
PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS: 10

BOUNDARY_STATUS:
  FIXTURE_BOUNDED_SEPARATION_ESTABLISHED
```

This is not a permanent irreducibility result.

## 14. Global boundary guards

All ten precommitted distinctions were preserved:

```text
C1 TRACE_CONTINUITY != LINEAGE_IDENTITY
C2 MISSING_TRACE_LINK != RECONSTRUCTION_RESULT
C3 TRANSFORMATION_TRACE != TRANSFORMATION_CORRECTNESS
C4 TRACE_RECORD != AUDIT_VERDICT
C5 TRACE_CONTEXT_SOURCE_LINK != INTERPRETATION_RESULT
C6 MEASUREMENT_TRACE != DISCRIMINATION_SUFFICIENCY
C7 AGGREGATE_TRACE != AGGREGATION_OPERATION
C8 COMPRESSION_TRACE != COMPRESSION_SUCCESS
C9 TRACE_RELATION != COMPARISON_VERDICT
C10 TRACE_OF_ANALYSIS != STRUCTURAL_DECOMPOSITION
```

## 15. Frozen scoring

### A. Common fairness / immutability

```text
A1 PASS
A2 PASS
A3 PASS
A4 PASS
A5 PASS
A6 PASS
A7 PASS
A8 PASS
A9 PASS
A10 PASS
A11 PASS
A12 PASS

A: 12/12
```

### B. Ten boundary groups

```text
B1  5/5 PASS
B2  5/5 PASS
B3  5/5 PASS
B4  5/5 PASS
B5  5/5 PASS
B6  5/5 PASS
B7  5/5 PASS
B8  5/5 PASS
B9  5/5 PASS
B10 5/5 PASS

B: 50/50
```

### C. Global boundary discipline

```text
C1 PASS
C2 PASS
C3 PASS
C4 PASS
C5 PASS
C6 PASS
C7 PASS
C8 PASS
C9 PASS
C10 PASS

C: 10/10
```

Final:

```text
TOTAL_REQUIRED_CHECKS: 72
PASSED: 72
FAILED: 0
TOTAL: 72/72 PASS
```

## 16. Conformance and protocol pressure

```text
TRK-CH-003_CONFORMANCE:
  CONFORMANT

TRACKING_METHOD_GAIN_STATUS:
  NOT_ASSESSED

PROTOCOL_DEFECT_EXPOSED:
  no

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
```

No baseline was run.

No neighboring method was validated or matured by this challenge.

## 17. Counter update authorized by precommit

```text
DIRECT_TRACKING_PILOTS_ATTEMPTED:
  2 -> 3

SUCCESSFUL_DIRECT_TRACKING_PILOTS:
  2 -> 3

METHOD_BOUNDARY_TRACKING_CASES:
  0 -> 1

POSITIVE_TRACKING_CASES:
  1

NEGATIVE_OR_FAILURE_TRACKING_CASES:
  1

ALL_NINE_LINK_STATUSES_DIRECTLY_EXERCISED:
  yes

ALL_SIX_TRACE_TERMINALS_DIRECTLY_EXERCISED:
  yes
```

Unchanged:

```text
BASELINE_TRACKING_CASES: 0
NO_GAIN_TRACKING_CASES: 0
STRONGEST_REASONABLE_BASELINE_TRACKING: not established
REPRODUCIBILITY_CASES: 0

EXTERNAL_TRACKING_APPLICATIONS: 0
INDEPENDENT_TRACKING_VALIDATION: not established
INDEPENDENT_REPLICATION: not established

TRACKING_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_TRACKING_EVIDENCE_STATUS:
  validation_in_progress

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
```

## 18. Maximum supported claim

TRK-CH-003 establishes only fixture-bounded separation of Tracking's frozen binding operation from the ten tested neighboring method tasks under equal access to TRK-SP-003.

It does not establish:

```text
permanent method independence
permanent irreducibility
registry survival
neighboring-method weakness
external applicability
independent validation
comparative superiority
```

## 19. Next

Proceed to a separately precommitted competent non-DSD Tracking baseline challenge under equal information access.

The baseline must be allowed to use a competent generic trace/graph ledger and may legitimately produce NO_GAIN.
