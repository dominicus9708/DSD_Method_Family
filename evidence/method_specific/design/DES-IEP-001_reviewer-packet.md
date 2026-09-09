# DES-IEP-001 — Blinded Independent Evaluator Packet / 독립 평가자 블라인드 패킷

Status: **PREPARED — NOT YET EXECUTED**  
Date prepared: **2026-09-09**  
Method under evaluation: **DSD Design / DSD 설계론**  
Protocol: **DSD Design Protocol v0.1**  
Packet class: `independent_evaluator_packet`  
Evidence effect at preparation: **none**

## 1. Purpose / 목적

This packet is prepared for a genuinely separate evaluator to apply DSD Design Protocol v0.1 without access to the hidden reference answer key.

The packet itself is **not** independent-evaluator evidence.
Independent validation begins only after an eligible external evaluator receives the frozen packet, completes the scoring without prohibited answer exposure, and freezes a submission before the reference key is revealed.

```text
PACKET_PREPARED
!=
INDEPENDENT_EVALUATOR_VALIDATION
```

The packet contains two held-out tasks based on already-frozen external authorities used in the Design evidence program:

```text
Task W — W3C WCAG 2.2 submit-control subset
Task N — NIST SP 800-63B-4 AAL2 route-form subset
```

The candidate records below are new packet records `E1-E6` and `D1-D6` and are not the historical case IDs from `DES-APP-001` or `DES-APP-002`.

---

## 2. Evaluator eligibility / 평가자 적격성

The evaluator must declare all of the following before scoring:

```text
E1  I did not receive the DES-IEP-001 reference answer key or escrow nonce.
E2  I did not inspect Design evidence files that reveal materially equivalent candidate answers after accepting this packet.
E3  I used only this packet, the supplied external source text/links, and the supplied Protocol v0.1 material unless a procedural clarification is logged.
E4  I did not receive answer-leading feedback after scoring began.
E5  I will freeze my submission before any reference-key reveal.
E6  I disclose prior DSD exposure and any accidental contamination.
```

If `E1`, `E4`, or `E5` is false, the submission is not eligible as independent evidence.
If `E2` or `E3` is false, the submission must be marked `CONTAMINATED_OR_NONBLIND` unless the later Audit determines the exposure was non-answer-bearing.

The evaluator may be:

- a human external reviewer;
- a separately initialized model/session with no access to the hidden key or project conversation history;
- an external team using a declared internal procedure.

The current project assistant/session is not eligible as the independent evaluator for this packet.

---

## 3. Required Design rules supplied to the evaluator / 제공 규칙

For this packet, use the following Protocol v0.1 rules.

```text
R1  Hard constraints determine Design admissibility.
R2  External authority remains separate from the DSD Design verdict.
R3  Candidate coverage is only what the packet declares.
R4  DESIGN_SPACE returns the complete admissible family within declared coverage.
R5  No hidden Optimization may select a preferred admissible candidate.
R6  DESIGN_INFEASIBLE requires exhaustive coverage or an impossibility proof.
R7  Claim-relevant absent / undefined / inapplicable states must not be silently collapsed.
R8  TERMINAL_DESIGN_STATUS is separate from DESIGN_PROTOCOL_CONFORMANCE.
R9  DESIGN_METHOD_GAIN_STATUS is NOT_ASSESSED when no baseline comparison is performed.
R10 A subset Design verdict must not be expanded into full external-standard conformance.
```

Allowed terminal Design statuses:

```text
DESIGN_ADMISSIBLE
DESIGN_INFEASIBLE
DESIGN_UNDERDETERMINED
DESIGN_BLOCKED
```

Protocol conformance:

```text
CONFORMANT
NONCONFORMANT
UNDETERMINED
```

Method gain:

```text
GAIN_ESTABLISHED
NO_GAIN
NOT_ASSESSED
```

---

# TASK W — WCAG 2.2 submit-control subset

## 4. Task W source and scope lock / W 과업 출처·범위

External authority:

```text
W3C Web Content Accessibility Guidelines (WCAG) 2.2
W3C Recommendation dated 12 December 2024
```

Only the following frozen checks are active.

```text
H0  submit_control is ADMITTED

H1  target size:
    width >= 24 CSS px
    AND height >= 24 CSS px
    with no SC 2.5.8 exception active in this packet

H2  label in name:
    accessible name is defined
    AND contains visible label text "Submit"

H3  ordinary-text contrast ratio >= 4.5:1
```

Packet assumptions:

```text
ordinary active non-logo text
visible label = "Submit"
authored pointer target
no target-size exception applies
```

The note that putting the visible label text at the **start** of the accessible name is not a hard requirement for this packet.

Claimed output level:

```text
DESIGN_SPACE
```

Candidate coverage:

```text
exhaustive relative only to E1-E6
```

No baseline comparison is active.

## 5. Task W candidate records / W 후보

```text
E1
  submit_control = ADMITTED
  width = 25
  height = 25
  visible_label = "Submit"
  accessible_name = DEFINED("Submit payment")
  contrast_ratio = 4.6

E2
  submit_control = ADMITTED
  width = 24
  height = 30
  visible_label = "Submit"
  accessible_name = DEFINED("Order — Submit")
  contrast_ratio = 4.5

E3
  submit_control = ADMITTED
  width = 28
  height = 28
  visible_label = "Submit"
  accessible_name = APPLICABLE_BUT_UNDEFINED
  contrast_ratio = 7.0

E4
  submit_control = ADMITTED
  width = 24
  height = 23
  visible_label = "Submit"
  accessible_name = DEFINED("Submit")
  contrast_ratio = 4.4

E5
  submit_control = ADMITTED
  width = 30
  height = 30
  visible_label = "Submit"
  accessible_name = DEFINED("Send")
  contrast_ratio = 4.5

E6
  submit_control = CHANNEL_ABSENCE
  width = INAPPLICABLE
  height = INAPPLICABLE
  visible_label = INAPPLICABLE
  accessible_name = INAPPLICABLE
  contrast_ratio = INAPPLICABLE
```

## 6. Task W required evaluator output / W 제출 항목

For each `E1-E6`, report:

```text
ADMISSIBILITY_RESULT:
  admissible / rejected / unresolved / blocked

FAILURE_SET:
  subset of {H0,H1,H2,H3}, or NONE
```

Then report:

```text
ADMISSIBLE_FAMILY_W:
TERMINAL_DESIGN_STATUS_W:
DESIGN_PROTOCOL_CONFORMANCE_W:
DESIGN_METHOD_GAIN_STATUS_W:
```

Answer two scope questions:

```text
W-S1  Does this packet justify a claim of full WCAG 2.2 conformance? yes/no + one sentence.
W-S2  Is "visible label must occur at the start of accessible name" a hard requirement in this packet? yes/no + one sentence.
```

---

# TASK N — NIST AAL2 route-form subset

## 7. Task N source and scope lock / N 과업 출처·범위

External authority:

```text
NIST SP 800-63B-4
Digital Identity Guidelines: Authentication and Authenticator Management
July 2025
Authentication Assurance Level 2
```

Frozen route-form rules:

```text
S1  AAL2 requires two distinct authentication factors.

S2  AAL2 authentication uses either:
      a multi-factor authenticator,
      or a permitted combination of two single-factor authenticators.

S3  Permitted multi-factor forms include:
      MF out-of-band
      MF OTP
      MF cryptographic authentication

S4  A permitted two-single-factor form includes one listed physical authenticator:
      look-up secret
      out-of-band device
      SF OTP
      SF cryptographic authentication
    together with either:
      password
      biometric comparison

S5  Biometric characteristic/comparison is not a standalone authenticator by itself.

S6  At least one authenticator in the actual AAL2 authentication process must be replay-resistant.

S7  The verifier must offer at least one phishing-resistant authentication option at AAL2.
```

This packet evaluates **route form only**.
It does not establish replay-resistance implementation, approved cryptography, protected-channel realization, FIPS validation, verifier portfolio completion, or full deployed-system AAL2 conformance.

Hard constraints:

```text
H1  NIST_AAL2_PERMITTED_FORM
H2  TWO_DISTINCT_FACTOR_STRUCTURE
```

Claimed output level:

```text
DESIGN_SPACE
```

Candidate coverage:

```text
exhaustive relative only to D1-D6
```

No baseline comparison is active.

## 8. Task N candidate records / N 후보

```text
D1
  MF cryptographic authentication

D2
  password + SF OTP

D3
  biometric comparison + SF cryptographic authentication

D4
  password only

D5
  password + biometric comparison

D6
  biometric comparison alone
```

## 9. Task N required evaluator output / N 제출 항목

For each `D1-D6`, report:

```text
ADMISSIBILITY_RESULT:
  admissible / rejected / unresolved / blocked

FAILURE_SET:
  subset of {H1,H2}, or NONE
```

Then report:

```text
ADMISSIBLE_FAMILY_N:
TERMINAL_DESIGN_STATUS_N:
DESIGN_PROTOCOL_CONFORMANCE_N:
DESIGN_METHOD_GAIN_STATUS_N:
```

Answer two scope questions:

```text
N-S1  Does a route-form Design verdict establish full deployed-system AAL2 conformance? yes/no + one sentence.
N-S2  Should every individual route be rejected unless that route itself is established as phishing-resistant? yes/no + one sentence.
```

---

## 10. Submission integrity / 제출 무결성

The evaluator should use `DES-IEP-001_submission-template.md` and freeze the completed submission before the reference commitment is opened.

Acceptable freezing methods include:

- Git commit with immutable SHA;
- timestamped signed file;
- email to the project owner with the final attachment before key reveal;
- another immutable/time-ordered record documented in the later Audit.

After submission freeze, the project may reveal the escrow nonce and canonical reference key and verify the published SHA-256 commitment.

Do not edit the evaluator submission after reveal.
Corrections after reveal must be a separately labeled post-reveal note and do not replace the original independent score.

---

## 11. Precommitted agreement categories / 사전 합의 판정 범주

Semantic scoring contains **24 checks**:

```text
12 candidate result + failure-set checks
 6  admissible-family / three-ledger checks across the two tasks
 4  scope-boundary checks
 2  source/task identity checks
```

Critical subset:

```text
10 critical checks:
  exact admissible family W
  exact admissible family N
  terminal status W
  terminal status N
  gain status W
  gain status N
  W-S1
  W-S2
  N-S1
  N-S2
```

Agreement classes after key reveal:

```text
INDEPENDENT_AGREEMENT_FULL
  eligibility gates satisfied
  24/24 semantic checks

INDEPENDENT_AGREEMENT_PARTIAL
  eligibility gates satisfied
  at least 21/24 semantic checks
  all 10 critical checks pass

INDEPENDENT_DISAGREEMENT
  eligibility gates satisfied
  fewer than 21/24 semantic checks
  OR any critical check fails

CONTAMINATED_OR_INELIGIBLE
  independence eligibility not satisfied
```

A single eligible submission may establish **single-evaluator independent agreement at the recorded level**.
It does not establish broad inter-rater agreement, population-level reproducibility, or method maturity by itself.

---

## 12. Evidence-count rule / 증거 계수 규칙

Preparation of this packet changes no Design evidence count.

```text
INDEPENDENT_EVALUATOR_PACKET: prepared
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
DESIGN_DIRECT_PILOT_INCREMENT_FROM_PACKET_PREPARATION: 0
```

Only an eligible frozen external submission scored after commitment reveal can change the independent-evaluator evidence ledger.
