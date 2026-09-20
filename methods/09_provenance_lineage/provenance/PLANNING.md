# DSD Tracking Planning / DSD 추적론 기획

Status: **internal standardization in progress / TRK-CH-004 competent baseline 64/64 PASS / NO_GAIN / strongest-reasonable baseline next / external validation deferred**  
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
7. ✅ Negative / gap / conflict / out-of-scope challenge — `TRK-CH-002`, 64/64 PASS.
8. ✅ Direct method-boundary challenge — `TRK-CH-003`, 72/72 PASS / fixture-bounded separation.
9. ✅ Competent non-DSD baseline challenge — `TRK-CH-004`, 64/64 PASS / NO_GAIN.
10. 🟨 Strongest-reasonable baseline challenge.
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

DIRECT_TRACKING_PILOTS_ATTEMPTED: 4
SUCCESSFUL_DIRECT_TRACKING_PILOTS: 4
POSITIVE_TRACKING_CASES: 1
NEGATIVE_OR_FAILURE_TRACKING_CASES: 1
METHOD_BOUNDARY_TRACKING_CASES: 1
BASELINE_TRACKING_CASES: 1
NO_GAIN_TRACKING_CASES: 1

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

## TRK-CH-002

```text
PRECOMMIT_COMMIT: bf5ecb9f0ea21e391301bc4de2a0635c6cacb853
PRECOMMIT_BLOB:   6181f8a53dd89a00164a128a3689f33c2ba7df60
RESULT_COMMIT:    84143bdb315c6859a68fe9e3dcd3296a04dd8614
RESULT_BLOB:      b6a445187a82214751deb3b70da995932ccdc9e1
TOTAL: 64/64 PASS
ALL_NINE_LINK_STATUSES_DIRECTLY_EXERCISED: yes
ALL_SIX_TRACE_TERMINALS_DIRECTLY_EXERCISED: yes
TRK-CH-002_CONFORMANCE: CONFORMANT
```

## TRK-CH-003

```text
PRECOMMIT_COMMIT: 8e289432301f2d8d9a294c8c5e4e66310b17a376
PRECOMMIT_BLOB:   62353ce322882706369212b6ad34bd8e04489c0c
RESULT_COMMIT:    bc59d86171bc8d04092ad218b85e663822046cbe
RESULT_BLOB:      5969689a932a21f9fbe570b0b20cde049aa96eb7
TOTAL: 72/72 PASS
BOUNDARY_PAIRS_TESTED: 10
EXACT_COLLAPSE_PAIRS: 0
UNRESOLVED_BOUNDARY_PAIRS: 0
PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS: 10
BOUNDARY_STATUS: FIXTURE_BOUNDED_SEPARATION_ESTABLISHED
```

## TRK-CH-004

```text
PRECOMMIT_COMMIT: def62998c5f52c1e8d00c51dd8dfad4630c93e04
PRECOMMIT_BLOB:   fd321cb2c883c7e28383eedc89f631c31ef4b894
RESULT_COMMIT:    86f55716146a6e52d9cbc2d1b3895de3376f34f4
RESULT_BLOB:      6377255145183e3b2212b1d824a282bc7d22255e
TOTAL: 64/64 PASS
TRACKING_METHOD_GAIN_STATUS: NO_GAIN
TRK-CH-004_CONFORMANCE: CONFORMANT
```

All six frozen gain axes were `BASELINE_MATCH`.

## Next

Create a prospective strongest-reasonable non-DSD Tracking baseline challenge. The comparator may integrate version-aware schemas, graph topology, sidecars, competing semantics, and bounded maximum-claim reporting. External validation remains deferred.
