# DSD Tracking Planning / DSD 추적론 기획

Status: **internal standardization in progress / TRK-CH-001 56/56 PASS / negative challenge next / external validation deferred**  
Date opened: **2026-09-20**  
Legacy path ID: `09A`  
Legacy directory: `methods/09_provenance_lineage/provenance/`

## Purpose / 목적

Develop DSD Tracking as the atomic method for following a declared target across an explicit trace space and recording supported origin, version, transformation, process/stage, location/container, actor/custody/responsibility, status, reference/dependency, and evidence-support relations without silently upgrading trace continuity into truth, causality, lineage identity, ownership, responsibility, reconstruction, or audit success.

The earlier Provenance / 출처·유래 추적 scope is retained as the origin/derivation subcase of Tracking.

## Project sequencing rule

```text
Task Interface
-> pre-protocol boundary attack
-> Boundary Amendment
-> executable Protocol
-> constructed positive / negative / boundary / NO_GAIN cases
-> deterministic same-project retrace
-> frozen-axis internal standardization audit
-> external validation later
```

## Current sequence

1. ✅ Tracking scope broadened from Provenance while preserving legacy path compatibility.
2. ✅ Task Interface v0.1 historical draft.
3. ✅ Pre-protocol boundary attack — 18 constructed internal cases.
4. ✅ Boundary Amendment 001 — R1-R8 prospectively adopted.
5. ✅ Executable Tracking Protocol v0.1 — frozen.
6. ✅ Positive constructed challenge — `TRK-CH-001`, 56/56 PASS.
7. 🟨 Negative / gap / conflict / out-of-scope challenge.
8. ⬜ Direct method-boundary challenge.
9. ⬜ Competent non-DSD baseline challenge.
10. ⬜ Strongest-reasonable baseline challenge.
11. ⬜ Deterministic same-project retrace.
12. ⬜ Frozen-axis internal standardization audit.
13. ⏸ External applications deferred.

## Current counters

```text
DEDICATED_TRACKING_PROTOCOL: established v0.1
TASK_INTERFACE_DRAFT: v0.1 historical draft preserved

PRE_PROTOCOL_BOUNDARY_ATTACKS: 18
PRESERVED_NO_REFINEMENT: 8
PRESERVED_WITH_NONBREAKING_REFINEMENT: 10
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0

BOUNDARY_AMENDMENT_001: established

DIRECT_TRACKING_PILOTS_ATTEMPTED: 1
SUCCESSFUL_DIRECT_TRACKING_PILOTS: 1
POSITIVE_TRACKING_CASES: 1
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
CURRENT_TRACKING_EVIDENCE_STATUS: validation_in_progress

PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

## Forced refinement groups from boundary attack

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

## Source-layer discipline

Tracking may consume Formation traces, typed property/status records, support-retaining static records, explicit source/version locks, Transformation ledgers, Aggregation/Compression sidecars, Dynamics transition records, and Lineage handoffs when supplied.

No optional predecessor layer is mandatory for every Tracking task.

In particular:

```text
TRACKING_CONSUMES_LINEAGE_HANDOFF
!= TRACKING_DECIDES_LINEAGE_IDENTITY

TRACKING_RECORDS_TRANSFORMATION
!= TRACKING_EXECUTES_TRANSFORMATION

TRACKING_RECORDS_AGGREGATE_HANDOFF
!= TRACKING_RECONSTRUCTS_LOST_SUPPORT
```

## Frozen protocol identity

```text
AMENDMENT_COMMIT: 086c537b1312838500f6d188f32e7c643bde990b
AMENDMENT_BLOB:   846a195f1e18c1fd1b9824638d98e10fc837f10e
PROTOCOL_COMMIT:  a0d979325c11919fecaa4d8eab129477a365af87
PROTOCOL_BLOB:    72e9cc8576ae87e088bdf2f8ebb3d7016c2894c1

VALIDITY_GATES: G1-G14
BINDING_OPERATION: T1-T14
```

Protocol v0.1 contains typed node/link/evidence registers, graph topology, nine link statuses, six trace terminals, completion semantics, neighboring-method handoffs, conformance, gain, and maximum-claim discipline.

## TRK-CH-001

```text
PRECOMMIT_COMMIT: 296ed60f2962a4fc7d93dd7cd36dfe75af3c662c
PRECOMMIT_BLOB:   abddc44d571b99434990ee5d6f52b91ac59a5664
RESULT_COMMIT:    1054ae30fcfba557088bb28cbe825c837762478e
RESULT_BLOB:      eb86349f7a3d525a8aab7174a1612116276a32ee
TOTAL: 56/56 PASS
TRACKING_TRACE_TERMINAL_STATUS: TRACKING_TRACE_COMPLETE
TRACKING_PROTOCOL_CONFORMANCE: CONFORMANT
```

## Next

Create a prospective negative Tracking challenge precommit that directly exercises missing, explicitly negated, ambiguous, conflicting, blocked, inapplicable, out-of-scope, and underdetermined link semantics plus the non-COMPLETE trace terminals. External validation remains deferred.
