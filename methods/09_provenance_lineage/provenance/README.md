# DSD Tracking / DSD 추적론

Status: **Tracking Protocol v0.1 internally standardized / TRK-AUD-001 28/28 PASS / PROMOTE_INTERNAL_STANDARD / external validation deferred**  
Legacy path ID: `09A`  
Legacy path: `methods/09_provenance_lineage/provenance/`  
Former Korean label: **DSD 출처·유래 추적론**  
Former English compatibility label: **Provenance**  
Higher field: **IV. Evidence & Lineage / 증거·계보**


## Internal-standardization files

- [`PLANNING.md`](PLANNING.md)
- [`TASK_INTERFACE_v0.1-draft.md`](TASK_INTERFACE_v0.1-draft.md)
- [`BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`](BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md)
- [`WORKLOG.md`](WORKLOG.md)
- [`TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`](TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md)
- [`PROTOCOL_v0.1.md`](PROTOCOL_v0.1.md)
- [`TRK-AUD-001 precommit`](../../../evidence/method_specific/tracking/TRK-AUD-001_precommit.md)
- [`TRK-AUD-001 result`](../../../evidence/method_specific/tracking/TRK-AUD-001_internal-standardization-review.md)

## Internal-standardization sequence

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

## Current internal state

```text
DEDICATED_TRACKING_PROTOCOL: established v0.1
TASK_INTERFACE_DRAFT: v0.1 historical draft preserved

PRE_PROTOCOL_BOUNDARY_ATTACKS: 18
PRESERVED_NO_REFINEMENT: 8
PRESERVED_WITH_NONBREAKING_REFINEMENT: 10
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0

BOUNDARY_AMENDMENT_001: established

DIRECT_TRACKING_PILOTS_ATTEMPTED: 5
SUCCESSFUL_DIRECT_TRACKING_PILOTS: 5
POSITIVE_TRACKING_CASES: 1
NEGATIVE_OR_FAILURE_TRACKING_CASES: 1
ALL_NINE_LINK_STATUSES_DIRECTLY_EXERCISED: yes
ALL_SIX_TRACE_TERMINALS_DIRECTLY_EXERCISED: yes
METHOD_BOUNDARY_TRACKING_CASES: 1
BASELINE_TRACKING_CASES: 2
NO_GAIN_TRACKING_CASES: 2
STRONGEST_REASONABLE_BASELINE_TRACKING: established_at_constructed_evidence_level
REPRODUCIBILITY_CASES: 1
SAME_PROJECT_DETERMINISTIC_RETRACE: established_once

EXTERNAL_TRACKING_APPLICATIONS: 0
INDEPENDENT_TRACKING_VALIDATION: not established
INDEPENDENT_REPLICATION: not established

TRACKING_INTERNAL_STANDARDIZATION_STATUS: established
CURRENT_TRACKING_EVIDENCE_STATUS: validation_in_progress
```

## Pre-protocol refinement groups

```text
R1 task / target / scope / dimension / completion lock
R2 node identity / version / type / domain / status discipline
R3 link relation / direction / schema-version discipline
R4 evidence support / provenance ledger
R5 graph structure / branching / merging / cycles / multi-source
R6 missing / negative / ambiguous / conflicting / blocked / out-of-scope
R7 temporal / process / location / custody / ownership / responsibility / causality
R8 neighboring-method handoffs / reconstructed-vs-established trace
```

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

## Frozen protocol identity

```text
AMENDMENT_COMMIT: 086c537b1312838500f6d188f32e7c643bde990b
AMENDMENT_BLOB:   846a195f1e18c1fd1b9824638d98e10fc837f10e

PROTOCOL_COMMIT:  a0d979325c11919fecaa4d8eab129477a365af87
PROTOCOL_BLOB:    72e9cc8576ae87e088bdf2f8ebb3d7016c2894c1

VALIDITY_GATES: G1-G14
BINDING_OPERATION: T1-T14
```

Boundary Amendment 001 prospectively extends the historical link-status family with:

```text
TRACKING_LINK_BLOCKED
```

without rewriting the historical Task Interface.

## TRK-CH-001 — positive constructed Tracking challenge

- [Precommit](../../../evidence/method_specific/tracking/TRK-CH-001_precommit.md)
- [Result](../../../evidence/method_specific/tracking/TRK-CH-001_positive-constructed.md)

```text
PRECOMMIT_COMMIT: 296ed60f2962a4fc7d93dd7cd36dfe75af3c662c
PRECOMMIT_BLOB:   abddc44d571b99434990ee5d6f52b91ac59a5664
RESULT_COMMIT:    1054ae30fcfba557088bb28cbe825c837762478e
RESULT_BLOB:      eb86349f7a3d525a8aab7174a1612116276a32ee

TOTAL: 56/56 PASS
TRACKING_TRACE_TERMINAL_STATUS: TRACKING_TRACE_COMPLETE
TRACKING_PROTOCOL_CONFORMANCE: CONFORMANT
TRACKING_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The positive fixture simultaneously exercised origin/source, version/edit, Transformation handoff, branching, many-source package inclusion, dependency fan-in, location/container, custody, reference path, and evidence provenance without promoting trace continuity to Lineage identity or process order to causality.

## TRK-CH-002 — negative / unresolved terminal coverage

- [Precommit](../../../evidence/method_specific/tracking/TRK-CH-002_precommit.md)
- [Result](../../../evidence/method_specific/tracking/TRK-CH-002_negative-terminal-coverage.md)

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

Directly exercised negative/unresolved link semantics include explicit negation, missing, ambiguity, conflict, blockage, inapplicability, out-of-scope status, and underdetermination.

```text
EXPLICITLY_NEGATED != MISSING
MISSING != BLOCKED
AMBIGUOUS != CONFLICTING
AMBIGUOUS != UNDERDETERMINED
CONFLICTING != UNDERDETERMINED
INAPPLICABLE != OUT_OF_SCOPE
OUT_OF_SCOPE != FALSE
```

## TRK-CH-003 — direct method-boundary challenge

- [Precommit](../../../evidence/method_specific/tracking/TRK-CH-003_precommit.md)
- [Result](../../../evidence/method_specific/tracking/TRK-CH-003_method-boundary.md)

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

Tested neighbors:

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
Analysis
```

This result is fixture-bounded only.

```text
FIXTURE_BOUNDED_SEPARATION != PERMANENT_METHOD_INDEPENDENCE
FIXTURE_NONCOLLAPSE != PERMANENT_IRREDUCIBILITY
```

## TRK-CH-004 — competent non-DSD baseline

- [Precommit](../../../evidence/method_specific/tracking/TRK-CH-004_precommit.md)
- [Result](../../../evidence/method_specific/tracking/TRK-CH-004_competent-baseline.md)

```text
PRECOMMIT_COMMIT: def62998c5f52c1e8d00c51dd8dfad4630c93e04
PRECOMMIT_BLOB:   fd321cb2c883c7e28383eedc89f631c31ef4b894
RESULT_COMMIT:    86f55716146a6e52d9cbc2d1b3895de3376f34f4
RESULT_BLOB:      6377255145183e3b2212b1d824a282bc7d22255e

TOTAL: 64/64 PASS
TRACKING_METHOD_GAIN_STATUS: NO_GAIN
TRK-CH-004_CONFORMANCE: CONFORMANT
```

All six precommitted gain axes were `BASELINE_MATCH`.

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
```

## TRK-CH-005 — preserved fixture-expectation failure

- [Precommit](../../../evidence/method_specific/tracking/TRK-CH-005_precommit.md)
- [Result](../../../evidence/method_specific/tracking/TRK-CH-005_strongest-reasonable-baseline.md)

```text
PRECOMMIT_COMMIT: b410f63882fd311c24033e4527899023474ce7bc
PRECOMMIT_BLOB:   fc408e2ee33a422964ed1c966d4a2e7edfce421b
RESULT_COMMIT:    89b7f183c1bb567c1c133221f91feddf9d7e85c9
RESULT_BLOB:      b98f1ae00e9817d4379793abefe9b2d107d10d19

TOTAL: 68/72
CHALLENGE_RESULT: FAIL_PRECOMMIT_FIXTURE_EXPECTATION
PROTOCOL_REVISION_REQUIRED: no
```

The failed expectation incorrectly treated `does not establish DEPENDS_ON` as an explicit negative dependency record.

```text
NOT_ESTABLISHED != EXPLICITLY_NEGATED
MISSING_LINK != NEGATIVE_LINK
```

The historical failure is preserved and was not used to advance canonical counters.

## TRK-CH-005B — corrected strongest-reasonable baseline

- [Corrective precommit](../../../evidence/method_specific/tracking/TRK-CH-005B_precommit.md)
- [Result](../../../evidence/method_specific/tracking/TRK-CH-005B_strongest-reasonable-baseline.md)

```text
PRECOMMIT_COMMIT: d69b2e68d835854c1483fdcb6c87a61a81953ebe
PRECOMMIT_BLOB:   21c233dc9914e8327f587fe38973df13624f287a
RESULT_COMMIT:    82d01f10595a30bdce17fd9d5defc60f35bba730
RESULT_BLOB:      c447e772b5aafbdf0a712b8a370e077990e6c7d8

TOTAL: 72/72 PASS
TRACKING_METHOD_GAIN_STATUS: NO_GAIN
STRONGEST_REASONABLE_BASELINE_TRACKING:
  established_at_constructed_evidence_level
```

All seven frozen gain axes were `BASELINE_MATCH`.

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
```

## TRK-CH-006 — deterministic same-project retrace

- [Precommit](../../../evidence/method_specific/tracking/TRK-CH-006_precommit.md)
- [Reconstruction ledger](../../../evidence/method_specific/tracking/TRK-CH-006_reconstruction-ledger.md)
- [Result](../../../evidence/method_specific/tracking/TRK-CH-006_deterministic-retrace.md)

```text
PRECOMMIT_COMMIT: 5afb654a259869ecf0caf1c2458d57648bdad391
PRECOMMIT_BLOB:   abe172c341954795c3e2394399a0bbaa3d7ca783

LEDGER_COMMIT:    397d7edef430fc788ed7a94f76891edf97d5ef3b
LEDGER_BLOB:      7b77f98f7a0536f50aebee056112752f750abdbb

RESULT_COMMIT:    4a27d27ff61fb5ba6df9d3e99f71d6b82a906f37
RESULT_BLOB:      ef20412a8edcf23d5602ce6a323752af760ee461

TOTAL: 56/56 PASS
CLAIM_RELEVANT_MISMATCHES: 0
POST_COMPARISON_CORRECTIONS: 0
SAME_PROJECT_DETERMINISTIC_RETRACE: established_once
```

The reconstruction ledger was frozen before the formal comparison step against the TRK-CH-005B result target.

This is same-project artifact consistency evidence, not blind or independent replication.

```text
SAME_PROJECT_RETRACE != INDEPENDENT_REPLICATION
DETERMINISTIC_MATCH != INDEPENDENT_VALIDATION
RETRACE_PASS != EXTERNAL_APPLICABILITY
```

## TRK-AUD-001 — frozen-axis internal standardization audit

- [Precommit](../../../evidence/method_specific/tracking/TRK-AUD-001_precommit.md)
- [Result](../../../evidence/method_specific/tracking/TRK-AUD-001_internal-standardization-review.md)

```text
AUDIT_PRECOMMIT_COMMIT: 22a0fea4a321bbf47189aaf7737839c1b03e6eb9
AUDIT_PRECOMMIT_BLOB:   3a6041fd6a168170ebd2d8d4ba090edc6a4cfa2a

AUDIT_RESULT_COMMIT:    66c2f2cbabb3fcba6f17dce688ee03041cfe6e20

PRECOMMITTED_REQUIRED_CHECKS: 28
PASSED: 28
FAILED: 0

FINAL_INTERNAL_STANDARDIZATION_DECISION:
  PROMOTE_INTERNAL_STANDARD

TRACKING_INTERNAL_STANDARDIZATION_STATUS:
  established
```

Frozen method-axis results:

```text
M1 PASS
M2 PASS
M3 PASS
M4 PASS
M5 CONDITIONAL_PASS
M6 PASS
M7 PASS
M8 PASS
M9 PASS
M10 PASS
M11 PASS
M12 PASS
M13 PASS
M14 DEFERRED_BY_SEQUENCE
M15 PASS
```

The audit preserved the original TRK-CH-005 68/72 fixture expectation failure and both NO_GAIN results. Internal promotion does not establish external applicability, independent validation, independent replication, or DSD-specific comparative gain.

## Next

Tracking internal construction is closed at Protocol v0.1 unless a later contradiction reopens it.

Proceed to **DSD Lineage / DSD 계보론** as the next not-yet-internally-standardized method.

Tracking external validation remains queued as a separate later evidence phase.
