# TRK-CH-001 Precommit — Positive Constructed Tracking Challenge

Status: **PROSPECTIVELY FROZEN / NOT YET EXECUTED**  
Date: **2026-09-20**  
Case ID: `TRK-CH-001`  
Case class: `positive_constructed_tracking_challenge`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen protocol

```text
PROTOCOL_PATH:
  methods/09_provenance_lineage/provenance/PROTOCOL_v0.1.md

PROTOCOL_COMMIT:
  a0d979325c11919fecaa4d8eab129477a365af87

PROTOCOL_BLOB:
  72e9cc8576ae87e088bdf2f8ebb3d7016c2894c1

BOUNDARY_AMENDMENT_COMMIT:
  086c537b1312838500f6d188f32e7c643bde990b

BOUNDARY_AMENDMENT_BLOB:
  846a195f1e18c1fd1b9824638d98e10fc837f10e
```

The protocol and amendment are immutable comparators for this challenge.

They must not be edited in response to the result.

## 2. Challenge purpose

Test whether Tracking Protocol v0.1 can execute one bounded multi-dimensional trace that simultaneously contains:

```text
origin/source
version/edit
transformation handoff
process/stage
branching
many-to-one dependency merge
location/container
custody
reference/dependency
evidence/support provenance
```

while preserving the following boundaries:

```text
trace continuity != Lineage identity
transformation trace != transformation correctness
custody != ownership/responsibility
process order != causality
path reachability != direct link
tracking result != Audit verdict
```

The case is deliberately positive: every required trace query has applicable supplied evidence and should be resolvable without inventing a missing link.

No baseline, external-domain correctness, independent validation, authenticity, truth, causality, legal responsibility, or method superiority is tested here.

## 3. Frozen task identity

```text
TRACKING_TASK_ID: TRK-CH-001
TASK_VERSION: 1

TRACE_TARGET_OR_TARGET_SET:
  {PKG_FINAL}

DECLARED_TRACE_SCOPE:
  bounded constructed artifact workflow W1

TASK_SCOPE_VERSION:
  W1-SCOPE-v1

DECLARED_TRACE_DIMENSION_SET:
  {
    origin/source,
    version/edit,
    transformation,
    process/stage,
    location/container,
    custody,
    reference/dependency,
    evidence/support
  }

TRACE_COMPLETION_OR_QUERY_CRITERION:
  all required trace query obligations Q1-Q12 must receive
  TRACKING_LINK_ESTABLISHED or TRACKING_LINK_EXPLICITLY_NEGATED;
  no unresolved required query may remain.

EXTERNAL_APPLICATION:
  no
```

The task does not request ownership, responsibility, causality, Lineage identity, authenticity, truth, Audit conformance, or reconstruction.

## 4. Frozen node register

```text
N0 = SRC_MASTER
  type: source artifact
  version: S1
  domain: constructed document workflow

N1 = DOC_DRAFT_V1
  type: document artifact
  version: v1

N2 = DOC_DRAFT_V2
  type: document artifact
  version: v2

N3 = PDF_EXPORT
  type: transformed artifact
  version: pdf-v1

N4 = COPY_A
  type: copied artifact
  version: copy-a-v1

N5 = COPY_B
  type: copied artifact
  version: copy-b-v1

N6 = REF_TABLE
  type: reference artifact
  version: ref-v3

N7 = PKG_FINAL
  type: package artifact
  version: pkg-v1

C1 = REPO_MAIN
  type: container/location
  version: repo-state-1

C2 = ARCHIVE_BOX
  type: container/location
  version: archive-state-1

A1 = OPERATOR_A
  type: actor/custodian

A2 = OPERATOR_B
  type: actor/custodian
```

Human-readable labels are not used as identities.

No two nodes are merged merely because they belong to the same workflow.

## 5. Frozen relation schema

```text
RELATION_SCHEMA_ID: TRK-RS-v1

allowed relation types:
  SOURCE_OF
  EDITED_TO
  TRANSFORMATION_HANDOFF_TO
  COPIED_TO
  DEPENDS_ON
  INCLUDED_IN
  STORED_IN
  CUSTODY_HELD_BY
  PRECEDES_STAGE
  REFERENCES

relation composition:
  none unless explicitly stated by a required query

causal inference:
  prohibited

Lineage identity inference:
  prohibited
```

## 6. Frozen evidence records

```text
E01:
  supports SRC_MASTER SOURCE_OF DOC_DRAFT_V1
  provenance: source-register SR-01

E02:
  supports DOC_DRAFT_V1 EDITED_TO DOC_DRAFT_V2
  provenance: version-log VL-12

E03:
  supports DOC_DRAFT_V2 TRANSFORMATION_HANDOFF_TO PDF_EXPORT
  provenance: transformation-ledger TH-07
  handoff claim only:
    transformation occurrence recorded
    transformation correctness not supplied

E04:
  supports PDF_EXPORT COPIED_TO COPY_A
  provenance: copy-log CL-01

E05:
  supports PDF_EXPORT COPIED_TO COPY_B
  provenance: copy-log CL-02

E06:
  supports COPY_A INCLUDED_IN PKG_FINAL
  provenance: package-manifest PM-1

E07:
  supports REF_TABLE INCLUDED_IN PKG_FINAL
  provenance: package-manifest PM-1

E08:
  supports PKG_FINAL DEPENDS_ON COPY_A
  provenance: package-dependency PD-1

E09:
  supports PKG_FINAL DEPENDS_ON REF_TABLE
  provenance: package-dependency PD-1

E10:
  supports PDF_EXPORT STORED_IN REPO_MAIN
  provenance: location-ledger LOC-4

E11:
  supports COPY_B STORED_IN ARCHIVE_BOX
  provenance: location-ledger LOC-5

E12:
  supports PDF_EXPORT CUSTODY_HELD_BY OPERATOR_A
  provenance: custody-ledger CUS-8

E13:
  supports COPY_B CUSTODY_HELD_BY OPERATOR_B
  provenance: custody-ledger CUS-9

E14:
  supports DOC_DRAFT_V1 PRECEDES_STAGE DOC_DRAFT_V2
  provenance: workflow-order WO-2

E15:
  supports DOC_DRAFT_V2 PRECEDES_STAGE PDF_EXPORT
  provenance: workflow-order WO-2

E16:
  supports PKG_FINAL REFERENCES DOC_DRAFT_V2
  provenance: reference-index RI-5

E17:
  supports DOC_DRAFT_V2 REFERENCES REF_TABLE
  provenance: reference-index RI-6
```

All evidence records are applicable within W1-SCOPE-v1.

No evidence record supplies authenticity, ownership, responsibility, causality, or Lineage identity.

## 7. Frozen required trace queries

```text
Q1  SRC_MASTER SOURCE_OF DOC_DRAFT_V1
Q2  DOC_DRAFT_V1 EDITED_TO DOC_DRAFT_V2
Q3  DOC_DRAFT_V2 TRANSFORMATION_HANDOFF_TO PDF_EXPORT
Q4  PDF_EXPORT COPIED_TO COPY_A
Q5  PDF_EXPORT COPIED_TO COPY_B
Q6  COPY_A INCLUDED_IN PKG_FINAL
Q7  REF_TABLE INCLUDED_IN PKG_FINAL
Q8  PKG_FINAL DEPENDS_ON COPY_A
Q9  PKG_FINAL DEPENDS_ON REF_TABLE
Q10 PDF_EXPORT STORED_IN REPO_MAIN
Q11 COPY_B STORED_IN ARCHIVE_BOX
Q12 PDF_EXPORT CUSTODY_HELD_BY OPERATOR_A
```

Expected link status for Q1-Q12:

```text
TRACKING_LINK_ESTABLISHED
```

E13-E17 are supplementary supported relations.

They are not required for terminal completeness but must be retained in the graph/ledgers because they are in-scope supplied trace records.

## 8. Frozen topology obligations

The graph must preserve:

### 8.1 Branching

```text
PDF_EXPORT -> COPY_A
PDF_EXPORT -> COPY_B
```

This is one-to-many trace branching.

It is not automatically a Lineage branching result.

### 8.2 Many-to-one package inclusion

```text
COPY_A -> PKG_FINAL
REF_TABLE -> PKG_FINAL
```

This is a many-source package/inclusion structure.

It is not automatically a Lineage merger result.

### 8.3 Dependency fan-in

```text
PKG_FINAL -> COPY_A
PKG_FINAL -> REF_TABLE
```

This uses `DEPENDS_ON` and is semantically distinct from `INCLUDED_IN`.

### 8.4 Reference path

```text
PKG_FINAL REFERENCES DOC_DRAFT_V2
DOC_DRAFT_V2 REFERENCES REF_TABLE
```

From this path the protocol may report reachability:

```text
PKG_FINAL reaches REF_TABLE by two REFERENCE edges
```

but may not create a direct:

```text
PKG_FINAL REFERENCES REF_TABLE
```

unless the relation schema explicitly licenses transitive composition.

No such composition rule is supplied here.

## 9. Frozen neighboring-method boundaries

### Transformation

```text
E03 establishes only:
  a declared Transformation handoff exists from DOC_DRAFT_V2 to PDF_EXPORT

NOT established:
  preservation correctness
  losslessness
  conformance of the transformation
```

### Lineage

The task may record version/edit/copy continuity but must not infer:

```text
DOC_DRAFT_V1 and DOC_DRAFT_V2 are the same Lineage entity
PDF_EXPORT is the Lineage successor of DOC_DRAFT_V2
COPY_A and COPY_B are Lineage branches
```

No Lineage handoff is supplied.

### Custody / ownership / responsibility

```text
PDF_EXPORT CUSTODY_HELD_BY OPERATOR_A
COPY_B CUSTODY_HELD_BY OPERATOR_B
```

must not become:

```text
OPERATOR_A owns PDF_EXPORT
OPERATOR_A is responsible for PDF_EXPORT
OPERATOR_B owns COPY_B
OPERATOR_B is responsible for COPY_B
```

### Process / causality

The supplied `PRECEDES_STAGE` records establish order only.

```text
PROCESS_ORDER != CAUSAL_LINK
```

### Audit

No Audit criterion/result is supplied.

```text
TRACE_RECORD != AUDIT_VERDICT
```

## 10. Frozen expected trace terminal

All Q1-Q12 are in scope, applicable, and directly supported by frozen evidence.

No required query is:

```text
missing
ambiguous
conflicting
blocked
inapplicable
out-of-scope
underdetermined
```

Therefore the expected terminal is:

```text
TRACKING_TRACE_COMPLETE
```

This terminal says the frozen required query set is complete.

It does not say all possible history about PKG_FINAL has been discovered.

## 11. Validity-gate acceptance

The run passes protocol conformance only if:

```text
G1  PASS
G2  PASS
G3  PASS
G4  PASS
G5  PASS
G6  PASS
G7  PASS
G8  PASS
G9  PASS
G10 NOT_APPLICABLE_WITH_REASON(
      no aggregation/compression reduction claim is used
    )
G11 PASS
G12 PASS
G13 PASS
G14 PASS
```

For G11, the neighboring-method handoff requirement is exercised by the Transformation handoff and explicit non-substitution guards.

## 12. Frozen scoring — 56 checks

### A. Immutability and task lock — 8

```text
A1 protocol commit/blob fixed
A2 amendment commit/blob fixed
A3 task ID/version fixed
A4 target and bounded scope fixed
A5 trace dimensions fixed
A6 Q1-Q12 fixed before execution
A7 completion criterion fixed
A8 external application explicitly no
```

### B. Node, link, and evidence typing — 12

```text
B1 all node identities remain distinct
B2 node versions/types/domains retained
B3 relation schema/version retained
B4 relation directions retained
B5 evidence IDs retained
B6 evidence provenance retained separately from relation claim
B7 Q1-Q12 each use an applicable supporting evidence record
B8 no unsupported link fabricated
B9 transformation relation typed as handoff
B10 location relations typed separately
B11 custody relations typed separately
B12 reference/dependency relation types remain distinct
```

### C. Link status and completion — 10

```text
C1-C6 Q1-Q6 = TRACKING_LINK_ESTABLISHED
C7-C10 Q7-Q10 = TRACKING_LINK_ESTABLISHED
```

Q11-Q12 are scored under E below together with relation-boundary checks.

### D. Graph topology and direct-edge discipline — 10

```text
D1 PDF_EXPORT branching to COPY_A/COPY_B retained
D2 branch not promoted to Lineage branching
D3 COPY_A + REF_TABLE package fan-in retained
D4 package fan-in not promoted to Lineage merger
D5 dependency fan-in retained separately from inclusion
D6 supplementary reference path retained
D7 two-edge reference reachability may be reported
D8 no unsupported direct PKG_FINAL REFERENCES REF_TABLE edge created
D9 path reachability kept distinct from direct edge
D10 graph not force-linearized
```

### E. Boundary discipline and terminal — 10

```text
E1 Q11 = TRACKING_LINK_ESTABLISHED
E2 Q12 = TRACKING_LINK_ESTABLISHED
E3 custody not promoted to ownership
E4 custody not promoted to responsibility
E5 process order not promoted to causality
E6 version/edit/copy continuity not promoted to Lineage identity
E7 transformation handoff not promoted to transformation correctness
E8 trace result not promoted to Audit verdict
E9 terminal = TRACKING_TRACE_COMPLETE
E10 COMPLETE bounded to frozen Q1-Q12 criterion
```

### F. Conformance / claim scope — 6

```text
F1 applicable G1-G14 gates match the precommit
F2 TRACKING_PROTOCOL_CONFORMANCE = CONFORMANT
F3 TRACKING_METHOD_GAIN_STATUS = NOT_ASSESSED
F4 no truth/authenticity claim inferred
F5 no ownership/responsibility/causality/Lineage claim inferred
F6 maximum claim limited to constructed evidence-bounded trace
```

```text
TOTAL_REQUIRED_CHECKS: 56
PASS_THRESHOLD: 56/56
PARTIAL_PASS_ALLOWED: no
```

Any mismatch remains visible.

The precommit must not be edited to rescue the result.

## 13. Allowed status changes on PASS

Only on 56/56 PASS:

```text
DIRECT_TRACKING_PILOTS_ATTEMPTED: 0 -> 1
SUCCESSFUL_DIRECT_TRACKING_PILOTS: 0 -> 1
POSITIVE_TRACKING_CASES: 0 -> 1

CURRENT_TRACKING_EVIDENCE_STATUS:
  protocol_frozen_pre_validation -> validation_in_progress
```

Unchanged:

```text
NEGATIVE_OR_FAILURE_TRACKING_CASES: 0
METHOD_BOUNDARY_TRACKING_CASES: 0
BASELINE_TRACKING_CASES: 0
NO_GAIN_TRACKING_CASES: 0
STRONGEST_REASONABLE_BASELINE_TRACKING: not established
REPRODUCIBILITY_CASES: 0
EXTERNAL_TRACKING_APPLICATIONS: 0
INDEPENDENT_TRACKING_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
TRACKING_INTERNAL_STANDARDIZATION_STATUS: developing
PROTOCOL_REVISION_REQUIRED: no unless contradiction is exposed
SHARED_CORE_REOPEN_REQUIRED: no unless contradiction is exposed
```
