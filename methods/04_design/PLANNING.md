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
13. **Next:** prepare a genuinely independent evaluator packet with hidden expected results before reviewer submission.
14. Optional additional breadth: non-software/physical external application with real irregular candidate artifact.
15. Re-audit maturity only after materially new evidence is frozen.

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

The frozen fixture adds four source-grounded controls.

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

The execution also preserves verifier-level phishing-resistant-option requirements at portfolio scope and does not invent route-level replay-resistance, cryptography, protected-channel, FIPS, or full-deployment conformance.

This moves external evidence from:

```text
1 application / 1 domain
```

to:

```text
2 applications / 2 domains
```

with the second case using a source-supplied positive route-form grammar.

### Dedicated retrace

`DES-CH-007` froze immutable refs for the protocol, `DES-APP-001` precommit, and historical result.

The claim-relevant re-execution reconstructed exactly:

```text
H0-H3
W1-W10 candidate records
candidate verdicts and rejection sets
admissible family {W1,W2,W3}
external source/version
WCAG_APPLICATION_BRIDGE_001
DESIGN_ADMISSIBLE
CONFORMANT
NOT_ASSESSED
```

and matched the historical result.

```text
RETRACE_RESULT: PASS
PRECOMMITTED_REQUIRED_CHECKS: 44/44 PASS
REPRODUCIBILITY_LEVEL: deterministic_same_project
```

This is not independent replication.

## First maturity audit / 첫 성숙도 감사

`DES-AUD-001` precommitted 14 maturity axes and 24 audit-discipline checks before scoring.

Audit ID:

```text
DSD-AUDIT-20260908-DESIGN-001
```

Result at audit time:

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

`DES-APP-002` is later evidence and therefore does not retroactively change this result.
A new maturity decision requires a new audit record.

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
METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

## Recording rule / 기록 규칙

Historical runs remain preserved under the protocol version used at execution time. Prospective corrections do not rewrite earlier evidence. Maturity re-audits must be new audit records rather than edits to `DES-AUD-001`.

## Next step / 다음 단계

The first audit's primary breadth blocker has been materially pressured by `DES-APP-002`, but independent evaluator validation remains absent.

The next preferred step is to prepare a frozen **independent evaluator packet** that:

```text
contains task material and scoring instructions without revealing expected results
commits expected results separately before reviewer submission
keeps reviewer identity/independence distinct from the project evaluator
prevents post-submission criterion changes
scores candidate verdicts, rejection bases, terminal status, conformance, and source-scope discipline
```

A non-software/physical external application remains useful as an additional breadth track, particularly if the candidate set is taken directly from a real artifact rather than project-frozen controls.
