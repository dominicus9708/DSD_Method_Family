# DSD Design Direct Evidence / DSD 설계론 직접 증거

Status: **Protocol v0.1 established / maturity: established / independent validation open**

This lane records evidence that directly tests **DSD Design / DSD 설계론**. Evidence from other DSD methods or shared-core validation does not automatically count as direct Design validation.

A Design maturity audit is an **Audit meta-record** and does not increase the Design direct-pilot count.
Independent-evaluator packet preparation is also infrastructure rather than direct evidence; only an eligible frozen external submission can change the independent-validation ledger.

## Current protocol

- `methods/04_design/PROTOCOL_v0.1.md` — executable protocol.

## Case-ID convention

```text
DES-CH-###   constructed Design challenges
DES-APP-###  external or independently generated Design applications
DES-AUD-###  Design-specific audit / maturity records
DES-IEP-###  independent evaluator packet infrastructure
```

## Direct evidence registry

### `DES-CH-001` — positive status-sensitive Design space

```text
ADMISSIBLE_FAMILY: {T1,T2}
PRECOMMITTED_REQUIRED_CHECKS: 11/11 PASS
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

Preserved `DEFINED_ZERO != APPLICABLE_BUT_UNDEFINED != CHANNEL_ABSENCE` and returned the full admissible family without hidden Optimization.

### `DES-CH-002` — negative terminal-status separation

```text
Case I -> DESIGN_INFEASIBLE
Case U -> DESIGN_UNDERDETERMINED
Case B -> DESIGN_BLOCKED
PRECOMMITTED_REQUIRED_CHECKS: 20/20 PASS
```

Directly prevents non-exhaustive failure-to-find from becoming global infeasibility and confirms `DESIGN_BLOCKED + CONFORMANT` when a required predecessor is missing.

### `DES-CH-003` — first Design/Optimization boundary attempt

```text
PRECOMMITTED_REQUIRED_CHECKS: 20/21
DIRECT_EVIDENCE_RESULT: FAIL_AS_PRECOMMITTED_CHALLENGE
FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
PROTOCOL_FAILURE_INFERRED: no
```

Candidate differences existed only outside the frozen Design target resolution. The failed challenge was preserved without post-hoc repair.

### `DES-CH-004` — corrected Design/Optimization boundary

```text
Case S -> {C1,C2,C3} / DESIGN_ADMISSIBLE
Case U -> DESIGN_UNDERDETERMINED
PRECOMMITTED_REQUIRED_CHECKS: 23/23 PASS
```

The correction placed `reserve_mode = MODE_A / MODE_B / MODE_C` inside `TARGET_RESOLUTION`; downstream `resource_cost` remained Optimization-only.

### `DES-CH-005` — NO_GAIN baseline equivalence

Baseline: `B0_EXPLICIT_CONSTRAINT_MATRIX`.

```text
B0 == DSD on frozen claim-relevant result
G1-G4: NOT_ESTABLISHED
DESIGN_ADMISSIBLE / CONFORMANT / NO_GAIN
PRECOMMITTED_REQUIRED_CHECKS: 25/25 PASS
```

Extra DSD bookkeeping is not method gain by itself.

### `DES-CH-006` — broader strongest-reasonable-baseline comparison

Baseline: `B1_TYPED_ADMISSIBILITY_TABLE`.

```text
Formation + General Property
15 candidates
multi-constraint failure sets
DESIGN_SPACE + UNIQUE_TARGET

Case S:
  B1  -> {A1,A2}
  DSD -> {A1,A2} / DESIGN_ADMISSIBLE

Case U:
  B1  -> NOT_UNIQUE_AT_DECLARED_RESOLUTION
  DSD -> DESIGN_UNDERDETERMINED

G1-G5: NOT_ESTABLISHED
DESIGN_METHOD_GAIN_STATUS: NO_GAIN
PRECOMMITTED_REQUIRED_CHECKS: 54/54 PASS
```

This fills the competent-baseline category without establishing DSD superiority.

### `DES-APP-001` — WCAG 2.2 external-standard application

Files:
- `DES-APP-001_precommit.md` — precommit `4847dbd`.
- `DES-APP-001_wcag22-submit-control-application.md` — result `32a7842`.

```text
EXTERNAL_DOMAIN: web accessibility
ADMISSIBLE_FAMILY: {W1,W2,W3}
DESIGN_ADMISSIBLE / CONFORMANT / NOT_ASSESSED
PRECOMMITTED_REQUIRED_CHECKS: 36/36 PASS
```

External authority remains W3C WCAG 2.2; full WCAG conformance is not claimed.

### `DES-CH-007` — deterministic retrace of DES-APP-001

Files:
- `DES-CH-007_precommit.md` — precommit `d6d9103`.
- `DES-CH-007_retrace-des-app-001.md` — result `d666a41`.

```text
RETRACE_RESULT: PASS
PRECOMMITTED_REQUIRED_CHECKS: 44/44 PASS
REPRODUCIBILITY_LEVEL: deterministic_same_project
```

This supports same-project procedural retraceability, not independent replication.

### `DES-APP-002` — NIST SP 800-63B-4 AAL2 route-form application

Files:
- `DES-APP-002_precommit.md` — precommit `cadc9ae`.
- `DES-APP-002_nist-aal2-route-form-application.md` — result `329f2b8`.

```text
EXTERNAL_DOMAIN: digital identity / authentication security
SOURCE_SUPPLIED_POSITIVE_CONSTRUCTION_GRAMMAR: yes
ADMISSIBLE_FAMILY: {N1,N2,N3,N4,N5,N6,N7,N8,N9,N10,N11}
DESIGN_ADMISSIBLE / CONFORMANT / NOT_ASSESSED
PRECOMMITTED_REQUIRED_CHECKS: 38/38 PASS
```

Preserved:

```text
TWO_DISTINCT_FACTOR_STRUCTURE
!= NIST_AAL2_PERMITTED_FORM
```

No route-form result is expanded into full deployed-system AAL2 conformance.

### `DES-APP-003` — 2010 ADA ramp-run physical application

Files:
- `DES-APP-003_precommit.md` — precommit `b78ca3a`.
- `DES-APP-003_ada-ramp-run-physical-application.md` — result `091b969`.

External authority: U.S. Access Board, 2010 ADA Standards for Accessible Design, selected §405 ramp-run subset.

```text
EXTERNAL_DOMAIN: built environment / physical accessibility

R1 -> admissible
R2 -> admissible
R3 -> rejected H1
R4 -> rejected H2
R5 -> rejected H3
R6 -> rejected H4
R7 -> rejected H5
R8 -> rejected H1,H2,H3,H4,H5
R9 -> admissible
R10 -> rejected H0; geometry remains INAPPLICABLE

ADMISSIBLE_FAMILY: {R1,R2,R9}
DESIGN_ADMISSIBLE / CONFORMANT / NOT_ASSESSED
PRECOMMITTED_REQUIRED_CHECKS: 38/38 PASS
```

The case does not promote advisory guidance into hard constraints, does not inject inactive alteration/employee-work-area exceptions, and does not overclaim full ADA ramp or engineering certification.

## Independent evaluator infrastructure

### `DES-IEP-001` — blinded evaluator packet prepared

Public frozen files:

```text
DES-IEP-001_reviewer-packet.md
  commit 78b1fb45d0b2e40838517828d089942e7b55e7d8

DES-IEP-001_submission-template.md
  commit fe1eedca019b4283a21047d21fcac12dd672e328

DES-IEP-001_reference-commitment.md
  commit 8fe4ff64b3fc964746d7e8c11bd03d712c40fedd
```

Reference-key SHA-256 commitment:

```text
3f2cf7c7787578063096c98ada872f29fffb6fdef27f7893d039e04604a2b0cf
```

Current effect:

```text
INDEPENDENT_EVALUATOR_PACKET: prepared
REFERENCE_KEY_COMMITMENT: frozen
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
DESIGN_DIRECT_PILOT_INCREMENT_FROM_PACKET_PREPARATION: 0
```

This remains infrastructure only.

## Audit meta-record registry

### `DES-AUD-001` — historical first maturity audit

Files:
- `DES-AUD-001_precommit.md` — precommit `bf4c55c`.
- `DES-AUD-001_maturity-review.md` — result `b2316d4`.

```text
AUDIT_ID: DSD-AUDIT-20260908-DESIGN-001
PRECOMMITTED_REQUIRED_CHECKS: 24/24 PASS
METHOD_MATURITY_CLASSIFICATION: developing
PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
M9_EXTERNAL_BREADTH: INSUFFICIENT
```

This historical decision remains unchanged.

### `DES-AUD-002` — revision maturity audit

Files:
- `DES-AUD-002_precommit.md` — precommit `0468c87`.
- `DES-AUD-002_revision-maturity-review.md` — result `36d8c75`.

The audit reuses the `DES-AUD-001` maturity axes and promotion logic, with the expanded post-audit corpus frozen before scoring.

```text
AUDIT_ID: DSD-AUDIT-20260909-DESIGN-002
PRECOMMITTED_REQUIRED_CHECKS: 26/26 PASS
AUDIT_EXECUTION_VERDICT: PASS
M9_EXTERNAL_BREADTH: PASS
M5_REPRODUCIBILITY: CONDITIONAL_PASS
M10_INDEPENDENT_PRACTICAL: UNRESOLVED_BUT_BOUNDED
M11_PROTOCOL_PRESSURE: PRESENT_NONFATAL
FINAL_MATURITY_DECISION: PROMOTE_ESTABLISHED
METHOD_MATURITY_CLASSIFICATION: established
PROMOTION_TO_ESTABLISHED: SUPPORTED
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
DESIGN_DIRECT_PILOT_INCREMENT_FROM_AUDIT: 0
```

The established label is limited to method/protocol evidence maturity under the current DSD method-family framework.
It does not establish independent evaluator validation, independent replication, broad inter-rater agreement, measured practical superiority, efficiency advantage, or defect-reduction advantage.

## External-breadth state after DES-AUD-002

```text
EXTERNAL_APPLICATIONS: 3
EXTERNAL_DOMAINS: 3
EXTERNAL_APPLICATION_PASSES: 3

1. web accessibility
2. digital identity / authentication security
3. built environment / physical accessibility
```

This is the material evidence change that clears the historical M9 blocker.

## Current status

```text
DEDICATED_PROTOCOL: v0.1 established
DIRECT_CONSTRUCTED_PILOTS: 7
POSITIVE_CASES: 1
NEGATIVE_OR_FAILURE_CASES: 1
BOUNDARY_CASES_UNDER_PROTOCOL: 2 attempted
BOUNDARY_VALIDATION_PASSES: 1
BOUNDARY_TEST_DESIGN_FAILURES: 1
NO_GAIN_CASES: 1
BASELINE_COMPARISON_CASES: 1
BASELINE_COMPARISON_RESULT: NO_GAIN
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
EXTERNAL_APPLICATIONS: 3
EXTERNAL_DOMAINS: 3
EXTERNAL_APPLICATION_PASSES: 3
INDEPENDENT_EVALUATOR_PACKET: prepared
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
METHOD_MATURITY_CLASSIFICATION: established
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

## Immediate next evidence task

The former M9 external-breadth blocker is closed under the revision-audit criterion.
The dominant unresolved axis is now independent/practical evidence, with reproducibility still limited to same-project retrace.

Next:

1. select a genuinely separate evaluator;
2. distribute only the frozen clean `DES-IEP-001` packet/template/source material;
3. freeze the completed evaluator submission before answer-key reveal;
4. reveal the escrow reference, verify the SHA-256 commitment;
5. score the frozen submission under the precommitted 24-check rule;
6. preserve agreement or disagreement as a new Audit/evidence record.

Do not rewrite either historical audit.
