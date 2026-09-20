# TRK-CH-004 — Competent Non-DSD Tracking Baseline Comparison Result

Status: **EXECUTED — 64/64 PASS / NO_GAIN**  
Date: **2026-09-21**  
Case ID: `TRK-CH-004`  
Case class: `competent_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen identities

```text
TRACKING_PROTOCOL_COMMIT:
  a0d979325c11919fecaa4d8eab129477a365af87

TRACKING_PROTOCOL_BLOB:
  72e9cc8576ae87e088bdf2f8ebb3d7016c2894c1

PRECOMMIT_COMMIT:
  def62998c5f52c1e8d00c51dd8dfad4630c93e04

PRECOMMIT_BLOB:
  fd321cb2c883c7e28383eedc89f631c31ef4b894

BASELINE_ID:
  B0_GENERIC_TYPED_TRACE_LEDGER
```

No protocol, baseline operation, fixture, mapping, gain axis, or scoring rule was changed after precommit.

## 2. Equal-information check

Tracking and B0 received the same claim-relevant records for every frozen fixture:

```text
task target
scope
trace dimensions
query set
completion rule
node IDs / versions / types / domains
relation types / directions
relation-schema records
evidence records and provenance
support / explicit-negation / absence flags
prerequisite / decoder / access availability
graph topology
location / custody records
method-handoff records
loss / reconstruction-warning sidecars
precedence or explicit absence of precedence
```

Result:

```text
EQUAL_INFORMATION_ACCESS: yes
TRACKING_HIDDEN_ADVANTAGE_INPUTS: 0
BASELINE_WITHHELD_CLAIM_RELEVANT_INPUTS: 0
```

## 3. Q1 — positive multidimensional trace

### Tracking

All required direct relations from the frozen TRK-CH-001 semantics remained:

```text
TRACKING_LINK_ESTABLISHED
```

for the required query set.

Tracking retained:

```text
PDF_EXPORT -> COPY_A
PDF_EXPORT -> COPY_B

COPY_A -> PKG_FINAL
REF_TABLE -> PKG_FINAL

PKG_FINAL DEPENDS_ON COPY_A
PKG_FINAL DEPENDS_ON REF_TABLE

PKG_FINAL REFERENCES DOC_DRAFT_V2
DOC_DRAFT_V2 REFERENCES REF_TABLE
```

and did not fabricate a direct:

```text
PKG_FINAL REFERENCES REF_TABLE
```

Tracking also preserved:

```text
custody != ownership/responsibility
Transformation handoff != Transformation correctness
```

Result:

```text
TRACKING_TRACE_TERMINAL_STATUS:
  TRACKING_TRACE_COMPLETE
```

### B0

B0 registered the same node IDs, directed relation types, evidence references, and graph topology.

All required direct relations were:

```text
B0_PRESENT
```

B0 also retained the one-to-many branch, many-source inclusion, dependency/inclusion distinction, and two-edge reference path.

B0 did not synthesize a direct reference edge from path reachability.

B0 did not upgrade custody to ownership/responsibility or the Transformation handoff to a correctness claim.

Result:

```text
B0_TRACE_COMPLETE
```

Comparison:

```text
Q1_CLAIM_RELEVANT_MATCH: yes
```

## 4. Q2 — explicit negative, missing, ambiguity

Frozen statuses:

```text
Q1 supported source relation
Q2 explicit applicable non-reference record
Q3 no support / no explicit negation / prerequisites available
Q4 duplicate display label with two distinct node IDs
```

Tracking:

```text
Q1 -> TRACKING_LINK_ESTABLISHED
Q2 -> TRACKING_LINK_EXPLICITLY_NEGATED
Q3 -> TRACKING_LINK_MISSING
Q4 -> TRACKING_LINK_AMBIGUOUS

terminal:
  TRACKING_TRACE_PARTIAL
```

B0:

```text
Q1 -> B0_PRESENT
Q2 -> B0_EXPLICIT_NEGATIVE
Q3 -> B0_ABSENT_REQUIRED_LINK
Q4 -> B0_AMBIGUOUS

terminal:
  B0_TRACE_PARTIAL
```

Both preserved:

```text
explicit negative != absence
absence != blockage
duplicate-label ambiguity != permission to choose a target
```

Comparison:

```text
Q2_CLAIM_RELEVANT_MATCH: yes
```

## 5. Q3 — blocked + inapplicable

Frozen state:

```text
Transformation envelope:
  supplied

required decoder:
  unavailable

custody query target:
  non-actor storage container

custody schema:
  actor/custodian required
```

Tracking:

```text
decoder-dependent relation:
  TRACKING_LINK_BLOCKED

custody relation:
  TRACKING_LINK_INAPPLICABLE

terminal:
  TRACKING_TRACE_BLOCKED
```

B0:

```text
decoder-dependent relation:
  B0_BLOCKED

custody relation:
  B0_NOT_APPLICABLE

terminal:
  B0_TRACE_BLOCKED
```

Neither side converted blockage into missing or inapplicability into explicit negation.

Comparison:

```text
Q3_CLAIM_RELEVANT_MATCH: yes
```

## 6. Q4 — conflicting applicable evidence

Frozen records:

```text
ARTIFACT_C STORED_IN LOCATION_X at T0
ARTIFACT_C STORED_IN LOCATION_Y at T0

schema:
  exactly one storage location at T0

precedence:
  absent
```

Tracking:

```text
relation:
  TRACKING_LINK_CONFLICTING

terminal:
  TRACKING_TRACE_CONFLICTING
```

B0:

```text
relation:
  B0_CONFLICT

terminal:
  B0_TRACE_CONFLICT
```

Both applicable records remain visible.

Neither side discards one record post hoc.

Comparison:

```text
Q4_CLAIM_RELEVANT_MATCH: yes
```

## 7. Q5A — outside scope

Frozen dimensions:

```text
source
version
```

Requested query:

```text
ownership
```

No scope extension is supplied.

Tracking:

```text
TRACKING_LINK_OUT_OF_SCOPE
TRACKING_TRACE_OUT_OF_SCOPE
```

B0:

```text
B0_OUTSIDE_SCOPE
B0_TRACE_OUTSIDE_SCOPE
```

Neither side converts excluded scope into falsehood or missing evidence.

```text
Q5A_CLAIM_RELEVANT_MATCH: yes
```

## 8. Q5B — underdetermined relation semantics

Frozen candidate record:

```text
DQ-1
```

Two admissible schemas:

```text
DEP-v1:
  DQ-1 -> dependency relation established

DEP-v2:
  DQ-1 -> metadata-reference only;
  dependency query explicitly negative

precedence:
  absent
```

Tracking:

```text
TRACKING_LINK_UNDERDETERMINED
TRACKING_TRACE_UNDERDETERMINED
```

B0:

```text
B0_UNRESOLVED_SCHEMA
B0_TRACE_UNRESOLVED
```

Neither side chooses one schema post hoc.

```text
Q5B_CLAIM_RELEVANT_MATCH: yes
```

## 9. Gain-axis result

The six precommitted gain axes were scored only from frozen claim-relevant outputs.

```text
G1 typed trace-link classification advantage:
  BASELINE_MATCH

G2 graph topology / direct-edge discipline advantage:
  BASELINE_MATCH

G3 evidence-versus-relation provenance advantage:
  BASELINE_MATCH

G4 gap / ambiguity / conflict / blockage semantic advantage:
  BASELINE_MATCH

G5 scope / schema / terminal discipline advantage:
  BASELINE_MATCH

G6 overclaim-boundary advantage:
  BASELINE_MATCH
```

Therefore:

```text
TRACKING_METHOD_GAIN_STATUS:
  NO_GAIN
```

The competent generic trace ledger reproduced the claim-relevant outputs because it received the same typed identities, relations, evidence/provenance, scope, schema, prerequisite, topology, and sidecar records.

No DSD-specific performance advantage is established by this fixture.

## 10. What NO_GAIN means here

```text
NO_GAIN
  means:
    no claim-relevant advantage over B0 was established
    for the frozen constructed tasks under equal information access
```

It does not mean:

```text
Tracking protocol failed
Tracking should be deleted
Tracking should merge into Lineage or Reconstruction
Tracking is identical to every trace system
Tracking has no organizational value
Tracking cannot show gain on another precommitted task
```

Preserved:

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
```

## 11. Frozen scoring

### A. Fairness and immutability

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

A: 10/10
```

### B. Q1 positive multidimensional trace

```text
B1 PASS
B2 PASS
B3 PASS
B4 PASS
B5 PASS
B6 PASS
B7 PASS
B8 PASS
B9 PASS
B10 PASS
B11 PASS
B12 PASS
B13 PASS
B14 PASS
B15 PASS
B16 PASS

B: 16/16
```

### C. Q2 negative/missing/ambiguous

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
C11 PASS
C12 PASS

C: 12/12
```

### D. Q3 blocked/inapplicable

```text
D1 PASS
D2 PASS
D3 PASS
D4 PASS
D5 PASS
D6 PASS
D7 PASS
D8 PASS
D9 PASS
D10 PASS

D: 10/10
```

### E. Q4 conflict

```text
E1 PASS
E2 PASS
E3 PASS
E4 PASS
E5 PASS
E6 PASS
E7 PASS
E8 PASS

E: 8/8
```

### F. Q5 scope + underdetermination

```text
F1 PASS
F2 PASS
F3 PASS
F4 PASS
F5 PASS
F6 PASS

F: 6/6
```

### G. Gain conclusion

```text
G1 PASS
G2 PASS

G: 2/2
```

Final:

```text
TOTAL_REQUIRED_CHECKS: 64
PASSED: 64
FAILED: 0
TOTAL: 64/64 PASS
```

## 12. Conformance and protocol pressure

```text
TRK-CH-004_CONFORMANCE:
  CONFORMANT

TRACKING_METHOD_GAIN_STATUS:
  NO_GAIN

PROTOCOL_DEFECT_EXPOSED:
  no

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
```

The result does not expose a contradiction in Tracking Protocol v0.1.

It shows that the current frozen tasks are also solvable by a competent generic typed trace ledger when equal structured information is supplied.

## 13. Counter update authorized by precommit

```text
DIRECT_TRACKING_PILOTS_ATTEMPTED:
  3 -> 4

SUCCESSFUL_DIRECT_TRACKING_PILOTS:
  3 -> 4

BASELINE_TRACKING_CASES:
  0 -> 1

NO_GAIN_TRACKING_CASES:
  0 -> 1

TRACKING_METHOD_GAIN_STATUS:
  NO_GAIN
```

Unchanged:

```text
POSITIVE_TRACKING_CASES: 1
NEGATIVE_OR_FAILURE_TRACKING_CASES: 1
METHOD_BOUNDARY_TRACKING_CASES: 1

ALL_NINE_LINK_STATUSES_DIRECTLY_EXERCISED: yes
ALL_SIX_TRACE_TERMINALS_DIRECTLY_EXERCISED: yes

STRONGEST_REASONABLE_BASELINE_TRACKING:
  not established

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

## 14. Maximum supported claim

TRK-CH-004 establishes only:

```text
Under Q1-Q5B and equal information access,
the competent B0 generic typed trace ledger reproduced
the claim-relevant Tracking outputs.

No DSD-specific gain was established in this comparison.
```

It does not establish external adequacy, independent validation, general inferiority/superiority, permanent redundancy, method merger, or registry deletion.

## 15. Next

Proceed to a separately precommitted strongest-reasonable non-DSD Tracking baseline challenge.

The stronger comparator should be allowed to integrate version-aware relation schemas, branch/merge/cycle handling, direct-edge versus reachability checks, sidecar-aware handoffs, competing semantics, typed unresolved states, and bounded maximum-claim reporting in one generic trace engine.

Only after that comparison should same-project deterministic retrace be attempted.
