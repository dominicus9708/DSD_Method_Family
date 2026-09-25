# DSD Method Family — Current Sync State

Synchronized: **2026-09-25 KST**  
Repository: `dominicus9708/DSD_Method_Family`  
Method-state source commit before this synchronization record: `bdd617895576f4ccf1151a9dff6787a81ee76ca6`  
Canonical Notion root: https://app.notion.com/p/3d281f51e7fa80a890b0ec3ee2397c16
Canonical Notion synchronization page: https://app.notion.com/p/3e281f51e7fa811fa626e62c57d5cf07

This file is the current cross-surface restoration/synchronization checkpoint for the DSD Method Family.
It does not replace method-specific READMEs, immutable precommits, protocols, evidence records, audits, or historical worklogs.

## 1. Canonical architecture

```text
DSD foundational layers
-> 8 higher-level method fields
-> 22 independent methods
-> SC-01~SC-10 shared core
-> explicit cross-method and external-domain applications
```

The 8 higher-level fields are organizational categories only.
They do not merge their member methods.

1. Structural Description & Understanding — Analysis, Comparison, Classification, Interpretation
2. Criteria & Validation — Specification, Audit
3. Construction & Transformation — Design, Synthesis, Transformation
4. Evidence & Lineage — Measurement, Tracking, Lineage
5. Reduction & Representation — Aggregation, Compression
6. Inverse Inference & Reconstruction — Diagnosis, Reconstruction
7. Computation & Selection — Computation, Optimization
8. Dynamics & Action — Simulation, Prediction, Control, Operation

The total remains **22 independent methods**.

Legacy combined paths `09_provenance_lineage`, `10_aggregation_compression`, `12_computation_optimization`, and `15_diagnosis_reconstruction` are compatibility wrappers only and are not independent methods.

## 2. Current method status snapshot

These labels reproduce the current method-specific repository status at synchronization time.
They are not a cross-method ranking and do not imply independent external validation unless explicitly stated.

| Method | Current repository status |
|---|---|
| Analysis | established |
| Audit | established |
| Specification | internally standardized at Protocol v1.0; evidence maturity developing |
| Design | Protocol v0.1; maturity established; independent validation open |
| Synthesis | Protocol v0.1 established; method-protocol evidence maturity established; validation in progress |
| Comparison | Protocol v0.1 established; maturity established after CMP-AUD-001; validation in progress |
| Classification | Protocol v0.1 frozen; maturity established; independent-evaluator infrastructure next |
| Transformation | Protocol v0.1 internally standardized; external validation queued, not yet opened |
| Tracking | Protocol v0.1 internally standardized; TRK-AUD-001 28/28 PASS; external validation deferred |
| Lineage | Protocol v0.1 internally standardized; LIN-CH-006 56/56 PASS deterministic same-project retrace; LIN-AUD-001 28/28 PASS / PROMOTE_INTERNAL_STANDARD; external validation deferred |
| Aggregation | developing |
| Compression | proposed/developing |
| Measurement | Protocol v0.1 internally standardized; MSR-AUD-001 28/28 PASS; external validation deferred |
| Computation | proposed |
| Optimization | proposed |
| Simulation | proposed |
| Prediction | proposed |
| Control | proposed |
| Diagnosis | proposed |
| Reconstruction | proposed |
| Interpretation | Protocol v0.1 internally standardized; frozen-axis internal audit passed; external validation queued |
| Operation | proposed |

## 3. Shared core

Shared-core extraction is **closed for the current registry with conditions**.
The current reusable rule set remains:

```text
SC-01  preserve claim-relevant DSD status/type distinctions
SC-02  lock claim-relevant source/interface/version semantics
SC-03  make claim-relevant cross-structure mappings explicit
SC-04  use sufficient dependencies without optional-interface overconstraint
SC-05  respect information-loss and reconstruction limits
SC-06  separate regular evolution, transition, and lineage
SC-07  separate evidence applicability from case origin
SC-08  preserve evaluation integrity, failures, NO_GAIN, and precommit boundaries
SC-09  separate evidence/audit status from DSD object/model status
SC-10  keep external-domain validation standards distinct from DSD-internal success
```

Shared-core evidence does not automatically become direct validation evidence for every independent method.

## 4. Evidence applicability

The canonical evidence split is:

```text
evidence/shared/
evidence/method_specific/
evidence/real_world_cases/
evidence/CURRENT_EVIDENCE_APPLICABILITY_MATRIX.md
```

`EVIDENCE_SCOPE_CLASS` and `CASE_ORIGIN` remain separate.
Historical Analysis and Audit evidence is preserved in its original scope; reusable lessons may support shared rules without retroactively validating another method.

## 5. Recently closed internal-standardization front — Tracking / DSD 추적론

Canonical current name: **Tracking / DSD 추적론**.  
Legacy path retained: `methods/09_provenance_lineage/provenance/`.  
`Provenance / 출처·유래 추적` remains an origin/derivation subrange and historical compatibility label.

Current frozen/development record:

```text
DEDICATED_TRACKING_PROTOCOL: established v0.1
PRE_PROTOCOL_BOUNDARY_ATTACKS: 18
BOUNDARY_AMENDMENT_001: established

TRK-CH-001: 56/56 PASS
TRK-CH-002: 64/64 PASS
TRK-CH-003: 72/72 PASS / fixture-bounded separation
TRK-CH-004: 64/64 PASS / NO_GAIN
TRK-CH-005: preserved fixture failure 68/72
TRK-CH-005B: 72/72 PASS / NO_GAIN
TRK-CH-006: 56/56 PASS / deterministic same-project retrace

CLAIM_RELEVANT_MISMATCHES: 0
POST_COMPARISON_CORRECTIONS: 0
SAME_PROJECT_DETERMINISTIC_RETRACE: established_once

EXTERNAL_TRACKING_APPLICATIONS: 0
INDEPENDENT_TRACKING_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
TRACKING_INTERNAL_STANDARDIZATION_STATUS: established
CURRENT_TRACKING_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

TRK-AUD-001 was prospectively precommitted and executed:

```text
AUDIT_PRECOMMIT_COMMIT: 22a0fea4a321bbf47189aaf7737839c1b03e6eb9
AUDIT_PRECOMMIT_BLOB: 3a6041fd6a168170ebd2d8d4ba090edc6a4cfa2a
AUDIT_RESULT_COMMIT: 66c2f2cbabb3fcba6f17dce688ee03041cfe6e20
AUDIT_CHECKS: 28/28 PASS
FINAL_INTERNAL_STANDARDIZATION_DECISION: PROMOTE_INTERNAL_STANDARD
```

Tracking external validation remains deferred as a separate evidence phase.

### Active method — Lineage / DSD 계보론

Current state:

```text
TASK_INTERFACE_DRAFT: v0.1 historical draft preserved

TASK_INTERFACE_COMMIT:
  e233916530e8824427411d070ba0881160648618

PRE_PROTOCOL_BOUNDARY_ATTACKS: 18

BOUNDARY_ATTACK_COMMIT:
  3a8e860b7ea04eb321bb10c99922b224a58ff3dd

PRESERVED_NO_REFINEMENT: 13
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5

BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0

BOUNDARY_AMENDMENT_001: established
REFINEMENT_GROUPS_ADOPTED: 8/8

AMENDMENT_COMMIT: a448ac1ab49faddb97968ff5987d3c75ac77b6e0
AMENDMENT_BLOB: 35568d0a27a8537347600efff87064b6b4ad177f

DEDICATED_LINEAGE_PROTOCOL: established v0.1
PROTOCOL_COMMIT: f69f364985d604d2c883b14b2efa18535a6bbf6e
PROTOCOL_BLOB: 0ef686f3987b590e67e07b9ee5e4861c31e6e1ef
VALIDITY_GATES: G1-G16
BINDING_OPERATION: T1-T16

LINEAGE_INTERNAL_STANDARDIZATION_STATUS: established
CURRENT_LINEAGE_EVIDENCE_STATUS: validation_in_progress

SHARED_CORE_REOPEN_REQUIRED: no
```

The five prospective refinements concern:

```text
identity-bearing-family identity/version/provenance and selection lock
explicit lineage-family coherence status
NOT_ESTABLISHED versus BLOCKED semantics
required auxiliary-lineage absence
self-time/composition-coherence consequences and task-terminal precedence
```

LIN-CH-001 was prospectively precommitted and executed:

```text
PRECOMMIT_COMMIT: 0d797ac8321d2ed9b79e98d0890cc5bf721b25a4
PRECOMMIT_BLOB: f9f31a9c7cdb5692ba06e1d01750a02dc9984c3c
RESULT_COMMIT: 0b455a95c46225182c4fa2627766334fd507480f
RESULT_BLOB: a53dedb60cee339d75d792ecccd72a5ff7e30d64
CHECKS: 64/64 PASS
TASK_TERMINAL: LINEAGE_TASK_ESTABLISHED
PROTOCOL_CONFORMANCE: LINEAGE_PROTOCOL_CONFORMANT
```

Current direct counters:

```text
DIRECT_LINEAGE_PILOTS_ATTEMPTED: 5
SUCCESSFUL_DIRECT_LINEAGE_PILOTS: 5
POSITIVE_LINEAGE_CASES: 1
NEGATIVE_OR_UNRESOLVED_LINEAGE_CASES: 1
METHOD_BOUNDARY_LINEAGE_CASES: 1
METHOD_FAMILY_BOUNDARY_PAIRS_TESTED: 8
EXACT_COLLAPSE_PAIRS: 0
UNRESOLVED_BOUNDARY_PAIRS: 0
PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS: 8
DYNAMICS_SOURCE_LAYER_BOUNDARY_TESTS: 1
SOURCE_HANDOFF_SEPARATION: established_at_fixture_level
ALL_NINE_LINEAGE_SUCCESSOR_STATUSES_DIRECTLY_EXERCISED: yes
ALL_SEVEN_LINEAGE_TASK_TERMINALS_DIRECTLY_EXERCISED: yes
BASELINE_LINEAGE_CASES: 2
NO_GAIN_LINEAGE_CASES: 2
STRONGEST_REASONABLE_BASELINE_LINEAGE: established_at_constructed_evidence_level
REPRODUCIBILITY_CASES: 1
SAME_PROJECT_DETERMINISTIC_RETRACE: established_once
CLAIM_RELEVANT_MISMATCHES: 0
POST_COMPARISON_CORRECTIONS: 0
```

LIN-CH-002 was prospectively precommitted and executed:

```text
PRECOMMIT_COMMIT: 169021711ea5069f1e63246efdd2ddfafbb3067a
PRECOMMIT_BLOB: d5537721f9dc55291f61569ad57eaa7e6b844a5b
RESULT_COMMIT: bce8356317ca8b1411eee7b518f1c993864b6fa6
RESULT_BLOB: 3a40361b1c589e6a206bcbd4a6baa38054e6f075
CHECKS: 80/80 PASS
ALL_NINE_LINEAGE_SUCCESSOR_STATUSES_DIRECTLY_EXERCISED: yes
ALL_SEVEN_LINEAGE_TASK_TERMINALS_DIRECTLY_EXERCISED: yes
```

LIN-CH-003 was prospectively precommitted and executed:

```text
PRECOMMIT_COMMIT: 7c68b63a0643b50fab49443c126955f0035d97a7
PRECOMMIT_BLOB: 7488e670a50ee08ca739b6e37ce78781c8b04b83
RESULT_COMMIT: cc86daab1c8e0643e878159c913836bfe1e5aa38
RESULT_BLOB: ea3a94a1e6c572ea51efa719fd9450bd5c83c433
CHECKS: 72/72 PASS
METHOD_FAMILY_BOUNDARY_PAIRS_TESTED: 8
EXACT_COLLAPSE_PAIRS: 0
PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS: 8
SOURCE_HANDOFF_SEPARATION: established_at_fixture_level
```

LIN-CH-004 competent baseline:

```text
PRECOMMIT_COMMIT: 20d6dacf04f6a87b276af23bc7d4468b937a4850
PRECOMMIT_BLOB: 0ac9e959500192f28177112de68361ccd8a29270
RESULT_COMMIT: 0c2f048ddfce4191be38826d33f5ee2b1f342750
RESULT_BLOB: 39dca881b4f8b726226779f13e44d7f44846daf4
CHECKS: 64/64 PASS
GAIN_STATUS: NO_GAIN
```

LIN-CH-005 strongest-reasonable baseline:

```text
PRECOMMIT_COMMIT: d0c5b6c6d060c30a85856f93cbd53d4dc341515a
PRECOMMIT_BLOB: 91dc9f6aeab1a1b101354b0ebbb2c4ae0eb123e1
RESULT_COMMIT: 628d1f31de6060d943666f76cd05990423f35add
RESULT_BLOB: b2d0bca6e270d61dc378a2950876da935df8db48
CHECKS: 72/72 PASS
GAIN_STATUS: NO_GAIN
STRONGEST_REASONABLE_BASELINE_LINEAGE: established_at_constructed_evidence_level
```

LIN-CH-006 deterministic same-project retrace:

```text
PRECOMMIT_COMMIT: eaae98831363f9c4cdf4ad90fb6219e7362dbd85
PRECOMMIT_BLOB: ae4a04ecf9273141cccbb7055cbcad416ae9d4cd
RECONSTRUCTION_LEDGER_COMMIT: f60f70c1b970ce8c10eaecf7b4430ed57c0f3d8e
RECONSTRUCTION_LEDGER_BLOB: d2cd0f3f86ead187a45e8e3a8ac724322ea9467d
RESULT_COMMIT: cfdf96d2db01631f19ea8f83f8ce815e7e06857b
RESULT_BLOB: 51464ada941925e2adef5bd98ee2f511fda8f10c
CHECKS: 56/56 PASS
CLAIM_RELEVANT_MISMATCHES: 0
POST_COMPARISON_CORRECTIONS: 0
SAME_PROJECT_DETERMINISTIC_RETRACE: established_once
```

LIN-AUD-001 frozen-axis internal standardization audit:

```text
AUDIT_PRECOMMIT_COMMIT: 041f0f3129cd6925fbde683738028be431847cb7
AUDIT_PRECOMMIT_BLOB: a341a35a683d8d3d8276c0109862aec4d6293936
AUDIT_RESULT_COMMIT: 4fbc33e79dbac603a4cddbc356e105d2c6189eba
AUDIT_RESULT_BLOB: ed186ab0ff00e79e30972f40a4c1365cedfa8cd1
AUDIT_CHECKS: 28/28 PASS
FINAL_INTERNAL_STANDARDIZATION_DECISION: PROMOTE_INTERNAL_STANDARD
LINEAGE_INTERNAL_STANDARDIZATION_STATUS: established
```

**Next canonical phase:** external applications and/or independent validation infrastructure, kept separate from the closed internal-standardization lane.

## 6. Historical-preservation and verdict discipline

Do not retroactively rewrite historical evidence for cosmetic consistency.

Preserve independently:

```text
PASS
VALID_IN_DOMAIN
NOT_SUFFICIENT_FOR_EXTENSION
NON_IDENTICAL
RECONSTRUCTION_LOSS
REJECTED
FAIL
NO_GAIN
INDETERMINATE
SUPERSEDED
OPEN
CONDITIONAL
NO-GO
```

A preserved failure or NO_GAIN result is evidence about a bounded test, not a reason to erase, absorb, or delete a method.

## 7. Cross-surface source-of-truth policy

- **GitHub** — executable protocols, immutable/precommitted artifacts, evidence, audits, reproducibility/retrace records, repository-level canonical file state.
- **Notion** — readable canonical planning/status/roadmaps, method pages, research-note organization, cross-links, and current human-facing summaries.
- **Project chat** — working reasoning, interpretation, sequencing decisions, and temporary discussion context.
- **Published DSD papers** — foundational Formation / Property / Static Aggregation / Dynamics interfaces used by the method family.

When surfaces differ, preserve history and reconcile by explicit version/commit/time provenance rather than silently overwriting the older record.

## 8. Current project sequencing

The current family-wide priority is **method-specific protocol/evidence maturation**, not adding more shared-core labels.

At this synchronization point, Tracking's internal-standardization lane remains closed at Protocol v0.1. DSD Lineage Boundary Amendment 001 is established and executable Lineage Protocol v0.1 is frozen. The positive, negative/unresolved, boundary, competent-baseline, and strongest-reasonable-baseline challenges remain complete. LIN-CH-006 deterministically retraced the strongest-baseline Lineage-side outputs at 56/56 PASS with zero claim-relevant mismatches and zero post-comparison corrections. LIN-AUD-001 then passed 28/28 and promoted Lineage Protocol v0.1 to project-internal standard status. The Lineage internal-standardization lane is closed; external applications and independent validation remain separate later evidence phases. External-domain and independent validation remain separate evidence stages.
