# DSD Method Family — Current Sync State

Synchronized: **2026-09-22 KST**  
Repository: `dominicus9708/DSD_Method_Family`  
Method-state source commit before this synchronization record: `5d9475708718780a3038451290b25e1f9c0b0fe1`  
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
| Lineage | developing |
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

### Active next method — Lineage / DSD 계보론

Current status before development: **developing**.

The next canonical sequence is:

```text
Task Interface
-> pre-protocol boundary attack
-> Boundary Amendment if required
-> executable Protocol
-> positive / negative / boundary / NO_GAIN
-> strongest-reasonable baseline
-> deterministic same-project retrace
-> frozen-axis internal standardization audit
-> external validation later
```

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

At this synchronization point, Tracking's internal-standardization lane is closed at Protocol v0.1. The active next work item is DSD Lineage internal construction, beginning with its Task Interface and pre-protocol boundary attack. External-domain and independent validation remain separate evidence stages.
