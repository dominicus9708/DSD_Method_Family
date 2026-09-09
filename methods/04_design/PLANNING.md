# DSD Design Planning / DSD 설계론 기획

Status: **Protocol v0.1 / maturity: developing / validation in progress**

Date opened: **2026-09-08**

## Purpose / 목적

Develop DSD Design as an independent method that constructs and filters target structures from declared goals and constraints while preserving the 22-method boundary discipline.

Shared-core evidence and neighboring-method results may be referenced, but direct Design validation is accumulated separately.

## Protocol and interface

- Current executable protocol: [`PROTOCOL_v0.1.md`](PROTOCOL_v0.1.md)
- Design assumes no universal candidate generator.
- Candidate coverage remains `exhaustive / non_exhaustive / unknown`.
- `DESIGN_INFEASIBLE` requires exhaustive coverage or an impossibility argument.
- Material distinctness is judged at `TARGET_RESOLUTION`.
- Soft preferences are not silently promoted into hard constraints.
- External authority and neighboring-method verdicts remain separately identifiable.

## Three independent Design ledgers

```text
TERMINAL_DESIGN_STATUS:
  DESIGN_ADMISSIBLE
  DESIGN_INFEASIBLE
  DESIGN_UNDERDETERMINED
  DESIGN_BLOCKED

DESIGN_PROTOCOL_CONFORMANCE:
  CONFORMANT
  NONCONFORMANT
  UNDETERMINED

DESIGN_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

Maturity is evaluated separately by DSD Audit.

## Development sequence / 개발 순서

1. ✅ Design-specific task interface and minimum valid output.
2. ✅ Boundary counterexamples and non-breaking refinements.
3. ✅ `PROTOCOL_v0.1.md`.
4. ✅ Positive pilot `DES-CH-001` — 11/11 PASS.
5. ✅ Negative/failure pilot `DES-CH-002` — 20/20 PASS.
6. ✅ Boundary stage — failed `DES-CH-003` preserved; corrected `DES-CH-004` 23/23 PASS.
7. ✅ NO_GAIN pilot `DES-CH-005` — 25/25 PASS.
8. ✅ Broader strongest-reasonable-baseline comparison `DES-CH-006` — 54/54 PASS / NO_GAIN.
9. ✅ First external-standard application `DES-APP-001` — W3C WCAG 2.2 subset, 36/36 PASS.
10. ✅ Dedicated reproducibility/retrace `DES-CH-007` — 44/44 PASS at deterministic same-project level.
11. ✅ First DSD Audit maturity review `DES-AUD-001` — audit 24/24 PASS; maturity classified `developing`; established promotion withheld.
12. ✅ Second external application `DES-APP-002` — NIST SP 800-63B-4 AAL2 route-form grammar, 38/38 PASS.
13. ✅ First blinded independent-evaluator packet `DES-IEP-001` prepared; public reviewer packet + submission template + hidden reference commitment frozen, but no external submission yet.
14. **Next:** obtain a genuinely separate evaluator submission under DES-IEP-001 and score it only after immutable submission freeze and reference-key reveal.
15. Optional additional breadth: non-software/physical external application with real irregular candidate artifact.
16. Re-audit maturity only after materially new evidence is frozen.

## Evidence milestones / 증거 이정표

### Positive and non-success behavior

`DES-CH-001` preserved status distinctions and returned the complete admissible family.

`DES-CH-002` directly separated:

```text
DESIGN_INFEASIBLE
DESIGN_UNDERDETERMINED
DESIGN_BLOCKED
```

including the valid `DESIGN_BLOCKED + CONFORMANT` combination.

### Boundary behavior

`DES-CH-003` exposed a challenge-design defect and was preserved at 20/21 rather than repaired post hoc.
`DES-CH-004` prospectively corrected the candidate-resolution problem and passed the Design/Optimization boundary test.

### Method-gain behavior

`DES-CH-005` and `DES-CH-006` both produced valid `NO_GAIN` results against competent baselines.
No extra DSD bookkeeping was counted as gain by itself.

### External application 1 — DES-APP-001

`DES-APP-001` froze W3C WCAG 2.2 Recommendation 2024-12-12, limited to:

```text
SC 1.4.3 Contrast (Minimum)
SC 2.5.3 Label in Name
SC 2.5.8 Target Size (Minimum)
```

It returned `{W1,W2,W3}` and passed 36/36 checks while keeping source requirements separate from fixture assumptions, not promoting best-practice language into a hard criterion, not inventing an exception, and not overclaiming full WCAG conformance.

### External application 2 — DES-APP-002

`DES-APP-002` freezes NIST SP 800-63B-4, July 2025, AAL2 authenticator route-form rules.

The source supplies the positive candidate/construction grammar:

```text
MF out-of-band
MF OTP
MF cryptographic authentication

listed physical authenticator:
  look-up secret
  out-of-band device
  SF OTP
  SF cryptographic authentication
plus:
  password or biometric comparison
```

Execution result:

```text
N1-N11 -> admissible
N12 password only -> rejected H1,H2
N13 SF cryptographic only -> rejected H1,H2
N14 biometric alone -> rejected H1,H2
N15 password + biometric -> rejected H1 while H2 passes

ADMISSIBLE_FAMILY:
{N1,N2,N3,N4,N5,N6,N7,N8,N9,N10,N11}

DESIGN_ADMISSIBLE / CONFORMANT / NOT_ASSESSED
PRECOMMITTED_REQUIRED_CHECKS: 38/38 PASS
```

Key boundary:

```text
TWO_DISTINCT_FACTOR_STRUCTURE
!= NIST_AAL2_PERMITTED_FORM
```

This moves external evidence from `1 application / 1 domain` to `2 applications / 2 domains`, with the second case using a source-supplied positive route-form grammar.

### Dedicated retrace

`DES-CH-007` reproduced the frozen `DES-APP-001` claim-relevant result exactly and passed 44/44 checks.

```text
RETRACE_RESULT: PASS
REPRODUCIBILITY_LEVEL: deterministic_same_project
```

This is not independent replication.

## First maturity audit / 첫 성숙도 감사

`DES-AUD-001` precommitted 14 maturity axes and 24 audit-discipline checks before scoring.

```text
MINIMUM_PROMOTION_COMPONENTS_PRESENT: 8/8
PRECOMMITTED_REQUIRED_CHECKS: 24/24 PASS
AUDIT_EXECUTION_VERDICT: PASS
METHOD_MATURITY_CLASSIFICATION: developing
PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
PRIMARY_BLOCKER: insufficient external evidence breadth
SECONDARY_BLOCKER: independent/practical evidence not established
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

`DES-APP-002` and `DES-IEP-001` are later records and do not retroactively change the audit.
A new maturity decision requires a new audit record.

## Independent evaluator packet / 독립 평가자 패킷

`DES-IEP-001` is now prepared and frozen as infrastructure.

Public artifacts:

```text
DES-IEP-001_reviewer-packet.md
  commit 78b1fb45d0b2e40838517828d089942e7b55e7d8

DES-IEP-001_submission-template.md
  commit fe1eedca019b4283a21047d21fcac12dd672e328

DES-IEP-001_reference-commitment.md
  commit 8fe4ff64b3fc964746d7e8c11bd03d712c40fedd
```

Public reference-key commitment:

```text
SHA-256
3f2cf7c7787578063096c98ada872f29fffb6fdef27f7893d039e04604a2b0cf
```

The canonical plaintext reference key and nonce remain outside the reviewer packet until an evaluator freezes the submission.
The packet contains two held-out tasks using the frozen WCAG and NIST rule sets, with 12 packet-specific candidates and 24 semantic checks.

Precommitted agreement levels:

```text
FULL: eligible + 24/24
PARTIAL: eligible + >=21/24 + all 10 critical checks
DISAGREEMENT: eligible + <21/24 or any critical failure
CONTAMINATED_OR_INELIGIBLE: independence gate failure
```

Preparation status:

```text
INDEPENDENT_EVALUATOR_PACKET: prepared
REFERENCE_KEY_COMMITMENT: frozen
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
```

The project assistant/session that created the packet cannot count as the independent evaluator.

## Evidence architecture status / 증거 구조 상태

```text
DEDICATED_PROTOCOL: established
POSITIVE_CASE: established
NEGATIVE_OR_FAILURE_CASE: established
BOUNDARY_CASE: established with one preserved failed predecessor test
NO_GAIN_CASE: established
STRONGEST_REASONABLE_BASELINE_COMPARISON: established at constructed level
EXTERNAL_APPLICATIONS: 2
EXTERNAL_DOMAINS: 2
REPRODUCIBILITY_RETRACE: established at deterministic same-project level
INDEPENDENT_EVALUATOR_PACKET: prepared
INDEPENDENT_EVALUATOR_VALIDATION: not established
MATURITY_AUDIT: completed, developing classification
```

Current evidence counts:

```text
DIRECT_CONSTRUCTED_PILOTS: 7
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
EXTERNAL_APPLICATIONS: 2
EXTERNAL_DOMAINS: 2
EXTERNAL_APPLICATION_PASSES: 2
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

## Recording rule / 기록 규칙

Historical runs remain preserved under the protocol version used at execution time. Prospective corrections do not rewrite earlier evidence. Maturity re-audits must be new audit records rather than edits to `DES-AUD-001`.

The independent evaluator packet is also append-only at the committed version. If a defect is found before distribution, record a revision explicitly rather than silently replacing the frozen packet.

## Next step / 다음 단계

The current same-project development work has reached the point where the next core evidence event requires a genuinely separate evaluator.

Operational sequence:

```text
1. select evaluator
2. distribute frozen reviewer packet + submission template + external source material only
3. collect eligibility/contamination declarations
4. freeze final evaluator submission with immutable/timestamped identifier
5. reveal private escrow nonce and canonical key
6. recompute and verify SHA-256 commitment
7. score the frozen submission under the precommitted 24-check rule
8. record the result as a new evidence/Audit record without editing the original submission
```

A non-software/physical external application remains useful as an additional breadth track, particularly if the candidate set is taken directly from a real artifact rather than project-frozen controls.
