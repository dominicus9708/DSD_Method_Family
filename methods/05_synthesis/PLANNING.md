# DSD Synthesis Planning / DSD 합성론 기획

Status: **Protocol v0.1 established / method-protocol evidence maturity established / SYN-IEP-001 prepared / validation in progress**  
Date opened: **2026-09-10**

## Purpose / 목적

Develop DSD Synthesis as an independent method candidate under **Field III: Construction & Transformation**. Synthesis consumes supplied admitted parts or typed component records plus an explicit composition rule and determines which larger constructions are legitimate while preserving component status, interface prerequisites, relations/support, information-loss conditions, and formation-model boundaries.

Method maturity and final registry survival are separate questions.

## Current source/interface lock / 현재 기준 잠금

```text
Formation Axiom System
Property Axiom System
Channel-Indexed Static Aggregation
Structural Reorganization Dynamics
DSD_INTERFACE_PROFILE.md
METHOD_BOUNDARY_MATRIX.md
```

Key constraints:

```text
Formation Clause VII finite composition != universal domain composability
component property != automatic whole property
aggregate equality/readout != structural synthesis equality
single-case success/failure != method survival/merger/deletion decision
```

## Protocol lineage / 프로토콜 계보

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

Historical artifacts and failed challenges remain preserved rather than rewritten.

## Development sequence / 개발 순서

1. ✅ Synthesis-specific task interface.
2. ✅ 16 pre-protocol boundary attacks — 11 no refinement, 5 non-breaking refinement, 0 collapse.
3. ✅ Boundary Amendment 001.
4. ✅ Executable `Synthesis Protocol v0.1` — commit `8787b24`.
5. ✅ `SYN-CH-001` positive — **28/28 PASS**.
6. ✅ `SYN-CH-002` negative/failure — **36/36 PASS**.
7. ✅ `SYN-CH-003` direct method-boundary — **46/46 PASS**.
8. ✅ `SYN-CH-004` failed baseline design **33/35 FAIL** preserved; corrected `SYN-CH-005` **37/37 PASS / NO_GAIN**.
9. ✅ `SYN-CH-006` broader strongest-reasonable-baseline — **52/52 PASS / NO_GAIN**.
10. ✅ `SYN-APP-001` RFC 3986 generic URI external application — **40/40 PASS**.
11. ✅ `SYN-CH-007` deterministic same-project retrace — **48/48 PASS**.
12. ✅ `SYN-APP-002` BIPM SI unit-composition external application — **46/46 PASS**.
13. ✅ `SYN-APP-003` USB Type-C physical mating external application — **44/44 PASS**.
14. ✅ `SYN-AUD-001` first maturity audit — **28/28 audit-execution PASS**, method/protocol evidence maturity `established`.
15. ✅ `SYN-IEP-001` independent-evaluator infrastructure prepared; reference commitment frozen; submissions remain 0.
16. **Externally blocked next event:** genuinely separate immutable evaluator submission before reference reveal.
17. After such submission: escrow reveal -> SHA-256 verification -> predeclared semantic scoring -> independent-evidence Audit.

## Step 14 — SYN-AUD-001 maturity review

```text
AUDIT_ID: DSD-AUDIT-20260910-SYNTHESIS-001
PRECOMMIT: ba966b5
RESULT: bae4388
AUDIT_EXECUTION_VERDICT: PASS
PRECOMMITTED_REQUIRED_CHECKS: 28/28
FINAL_MATURITY_DECISION: PROMOTE_ESTABLISHED
METHOD_MATURITY_CLASSIFICATION: established
PROMOTION_TO_ESTABLISHED: SUPPORTED
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

Maturity axes:

```text
M1  dedicated executable protocol                       PASS
M2  positive/negative terminal discrimination           PASS
M3  neighboring-method boundary discrimination          PASS
M4  NO_GAIN preservation                                PASS
M5  reproducibility/retraceability                       CONDITIONAL_PASS
M6  external application origin                         PASS
M7  strongest-reasonable-baseline comparison            PASS
M8  external source fidelity and bridge discipline      PASS
M9  established-level evidence breadth                  PASS
M10 independent/practical-performance evidence          UNRESOLVED_BUT_BOUNDED
M11 protocol pressure / unresolved core defect          PRESENT_NONFATAL
M12 maximum-supported-claim discipline                  PASS
M13 composition-basis / coverage / equivalence discipline PASS
M14 historical failure / anti-post-hoc preservation     PASS
M15 method-survival / merger-separation discipline      PASS
```

The label remains bounded:

```text
ESTABLISHED_METHOD_PROTOCOL_EVIDENCE_MATURITY
!= INDEPENDENT_VALIDATION
!= INDEPENDENT_REPLICATION
!= PRACTICAL_SUPERIORITY
!= UNIVERSAL_EXTERNAL_GENERALITY
!= PERMANENT_METHOD_REGISTRY_SURVIVAL
```

## Step 15 — SYN-IEP-001 independent evaluator infrastructure

Prepared public artifacts:

```text
REVIEWER_PACKET
  evidence/method_specific/synthesis/SYN-IEP-001_reviewer-packet.md
  commit: 6be55803db46c1941904501ecfa5fb13ba4ec01f

SUBMISSION_TEMPLATE
  evidence/method_specific/synthesis/SYN-IEP-001_submission-template.md
  commit: 079cdda0957314020001fbffac252a4765dac9a9

REFERENCE_COMMITMENT
  evidence/method_specific/synthesis/SYN-IEP-001_reference-commitment.md
  commit: b785df0e30c7e534693b9bc7f3a2011fb1617778
  SHA-256: db5d1c505c3ab2d614357525489f3b2a0dd2fc595fff1e715c69f48ceeb7073f

CLEAN_DISTRIBUTION_RECORD
  evidence/method_specific/synthesis/SYN-IEP-001_distribution-record.md
  commit: af622b9d3abb35ab603736bb324e24061d178f92
```

Packet tasks:

```text
Task S — BIPM SI unit composition, held-out candidates S1-S6
Task P — USB Type-C physical mating/orientation, held-out candidates P1-P6
```

Independence gates:

```text
E1 no key/nonce access
E2 no answer-bearing evidence inspection after acceptance
E3 only allowed materials
E4 no answer-leading feedback
E5 freeze before reveal
E6 disclose prior exposure/contamination
```

Scoring lock:

```text
TOTAL_SEMANTIC_CHECKS: 24
CRITICAL_CHECKS: 10
FULL: 24/24 + eligible
PARTIAL: >=21/24 + 10/10 critical + eligible
DISAGREEMENT: below threshold or any critical failure, while eligible
CONTAMINATED_OR_INELIGIBLE: eligibility failure
```

The secret nonce and plaintext canonical reference key are held in a private escrow outside the public Synthesis tree. The current project assistant/session cannot become the independent evaluator.

## Evidence state after Step 15 / 15단계 후 증거 상태

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 6
SUCCESSFUL_POSITIVE_SYNTHESIS_CASES: 1
SUCCESSFUL_NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
SUCCESSFUL_BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 1
PRESERVED_FAILED_BASELINE_CHALLENGE_DESIGNS: 1
SUCCESSFUL_NO_GAIN_SYNTHESIS_CASES: 2
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
EXTERNAL_SYNTHESIS_APPLICATIONS: 3
EXTERNAL_SYNTHESIS_DOMAINS: 3
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 3
INDEPENDENT_EVALUATOR_PACKET: prepared
REFERENCE_KEY_COMMITMENT: frozen
CLEAN_DISTRIBUTION_RECORD: prepared
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
MEASURED_PRACTICAL_SUPERIORITY: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: established
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

## Recording rule / 기록 규칙

- Shared-core and neighboring-method evidence does not automatically become direct Synthesis validation.
- Historical planning and failed challenge designs are preserved; corrections are prospective under new Case IDs.
- `NO_GAIN` is a legitimate result and is separate from correctness/conformance.
- Success or failure of any single challenge/application/retrace does not decide method survival, merger, absorption, or deletion.
- Established method/protocol evidence maturity does not freeze the 22-method registry permanently.
- External validity is not upgraded beyond the source's declared version and scope.
- Same-project deterministic retrace is not independent replication.
- Independent-evaluator packet preparation is infrastructure, not validation.
- Hidden reference material is never revealed before an eligible submission freeze.
- Protocol v0.1 is revised only prospectively if direct evidence exposes a genuine protocol defect.

## Immediate next task / 다음

No further same-project Synthesis run can satisfy the dominant independence gap. The next valid evidence event requires a genuinely separate evaluator. Once a completed `SYN-IEP-001` submission is immutably frozen before key reveal, verify the commitment and score the submission under a new independent-evidence Audit record. Until then, keep `INDEPENDENT_EVALUATOR_SUBMISSIONS = 0` and do not claim independent validation or replication.
