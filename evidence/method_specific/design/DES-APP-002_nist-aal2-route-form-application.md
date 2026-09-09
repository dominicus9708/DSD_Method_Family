# DES-APP-002 — NIST SP 800-63B-4 AAL2 Route-Form Design Application

Status: **PASS — second external Design application**  
Date: **2026-09-09**  
Evidence scope: `method_specific`  
Method directly tested: **DSD Design / DSD 설계론**  
Method protocol: **DSD Design Protocol v0.1**  
Case class: **external_application**  
Precommit: `DES-APP-002_precommit.md`, commit `cadc9ae`

## 1. External source / 외부 출처

Frozen source:

```text
NIST SP 800-63B-4
Digital Identity Guidelines: Authentication and Authenticator Management
July 2025
Authentication Assurance Level 2
```

The authoritative NIST AAL2 text states, at the form level used by this case:

```text
AAL2 requires two distinct authentication factors.

AAL2 authentication uses either:
  one multi-factor authenticator,
  or a combination of two single-factor authenticators.

Permitted multi-factor forms:
  MF out-of-band
  MF OTP
  MF cryptographic authentication

Permitted two-single-factor grammar:
  one listed physical authenticator
    look-up secret
    out-of-band device
    SF OTP
    SF cryptographic authentication
  plus either
    password
    biometric comparison

A biometric characteristic is not recognized as an authenticator by itself.
```

The same AAL2 section separately requires at least one replay-resistant authenticator in actual use and requires verifiers to offer at least one phishing-resistant option.
Those requirements are preserved at their operational / verifier-portfolio scopes and are not rewritten into the route-form grammar.

---

## 2. Frozen task re-statement / 동결 과업 재진술

```text
CASE_ID: DES-APP-002
DESIGN_TASK_ID: DES-TASK-APP-002
PROTOCOL_VERSION: v0.1
CLAIMED_OUTPUT_LEVEL: DESIGN_SPACE
TARGET_DSD_LAYER_SCOPE:
  Formation
  General Property
TARGET_RESOLUTION:
  authenticator route topology and source-recognized factor/form categories
CANDIDATE_COVERAGE:
  exhaustive only relative to the frozen 15-form fixture
DOMAIN_BRIDGE:
  NIST_AAL2_ROUTE_FORM_BRIDGE_001
```

Hard checks:

```text
H1 NIST_AAL2_PERMITTED_FORM
H2 TWO_DISTINCT_FACTOR_STRUCTURE
```

No baseline comparison is active.
No Optimization objective is active.

---

## 3. Candidate execution / 후보 실행

### Source-permitted forms

| Candidate | Frozen route form | H1 | H2 | Result |
|---|---|---:|---:|---|
| N1 | MF out-of-band | pass | pass | admissible |
| N2 | MF OTP | pass | pass | admissible |
| N3 | MF cryptographic authentication | pass | pass | admissible |
| N4 | password + look-up secret | pass | pass | admissible |
| N5 | password + out-of-band device | pass | pass | admissible |
| N6 | password + SF OTP | pass | pass | admissible |
| N7 | password + SF cryptographic authentication | pass | pass | admissible |
| N8 | biometric comparison + look-up secret | pass | pass | admissible |
| N9 | biometric comparison + out-of-band device | pass | pass | admissible |
| N10 | biometric comparison + SF OTP | pass | pass | admissible |
| N11 | biometric comparison + SF cryptographic authentication | pass | pass | admissible |

### Source-grounded controls

| Candidate | Frozen route form | H1 | H2 | Result | Basis |
|---|---|---:|---:|---|---|
| N12 | password only | fail | fail | rejected | single-factor route; not in AAL2 permitted-form grammar |
| N13 | SF cryptographic authentication only | fail | fail | rejected | possession-only single-factor route; not in AAL2 permitted-form grammar |
| N14 | biometric comparison alone | fail | fail | rejected | one factor and biometric is not a standalone authenticator |
| N15 | password + biometric comparison | fail | pass | rejected | two factor categories are present, but the NIST two-single-factor grammar requires a listed physical authenticator paired with password or biometric |

The N15 result is an important boundary check:

```text
TWO_DISTINCT_FACTOR_STRUCTURE
!=
NIST_AAL2_PERMITTED_FORM
```

Two different factor categories alone do not establish that a route matches the source-permitted AAL2 authenticator grammar.

---

## 4. Admissible Design space / 허용 설계공간

The exact admissible family within the frozen fixture is:

```text
{N1,N2,N3,N4,N5,N6,N7,N8,N9,N10,N11}
```

All four controls are rejected for the precommitted bases.

No ranking, cost function, preference, or best-route selection was applied.

---

## 5. Source-scope discipline / 출처 범위 규율

### Phishing-resistant option requirement

NIST requires verifiers to **offer at least one phishing-resistant authentication option at AAL2**.
That is a verifier-offering / portfolio-level requirement.

This case evaluates individual route forms and therefore does **not** apply the following invalid transformation:

```text
verifier SHALL offer >=1 phishing-resistant option
-> every individual permitted AAL2 route must itself be phishing-resistant
```

No candidate was rejected by such a transformation.

### Replay resistance and implementation requirements

NIST also requires at least one authenticator used at AAL2 to be replay-resistant and imposes approved-cryptography, protected-channel, and context-dependent FIPS requirements.

The current target resolution contains route forms, not fully specified deployed implementations.
Therefore the execution does not fabricate:

```text
implementation-level replay-resistance evidence
approved-cryptography implementation evidence
protected-channel realization
FIPS validation state
full verifier-portfolio conformance
```

The output is a route-form Design space only.

---

## 6. DSD interface handling / DSD 인터페이스 처리

### Formation

Formation records the route topology and admitted authenticator-component roles at the declared form resolution.
It does not invent implementation instances, cryptographic modules, verifier channels, or deployment facts.

### General Property

General Property carries claim-relevant typed form/factor classifications supplied by the external bridge.
It does not rewrite Formation identity or upgrade unknown implementation properties into defined compliant values.

### Bridge

```text
NIST_AAL2_ROUTE_FORM_BRIDGE_001
```

maps the NIST form grammar into the frozen Design candidate records while preserving external normative authority.
DSD does not become the authority for which authenticator forms NIST permits.

---

## 7. Three Design ledgers / 설계 3중 장부

### Terminal status

At least eleven candidates satisfy H1 and H2 within the frozen fixture.
The task asks for `DESIGN_SPACE`.

```text
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
```

### Protocol conformance

The execution preserved the precommitted task, source, candidate basis, candidate coverage, bridge, candidate order, hard checks, output level, and source-scope guards.
No post-hoc exception, hidden Optimization, candidate-basis revision, or source-scope rewrite was introduced.

```text
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
```

### Method gain

No baseline comparison was precommitted.

```text
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

---

## 8. Precommitted scoring / 사전 고정 채점

```text
SOURCE_AND_PROVENANCE_CHECKS:      6 / 6 PASS
CANDIDATE_VERDICT_CHECKS:         15 / 15 PASS
REJECTION_AND_FAMILY_CHECKS:       5 / 5 PASS
SCOPE_AND_BRIDGE_CHECKS:            6 / 6 PASS
LEDGER_AND_PROTOCOL_CHECKS:         6 / 6 PASS

PRECOMMITTED_REQUIRED_CHECKS: 38
PASSED: 38
FAILED: 0
CHALLENGE_VERDICT: PASS
```

No precommitted criterion was altered after execution began.

---

## 9. Evidence verdict / 증거 판정

```text
CASE_ID: DES-APP-002
CASE_CLASS: external_application
EXTERNAL_DOMAIN: digital_identity_authentication_security
EXTERNAL_STANDARD: NIST SP 800-63B-4, July 2025
PROTOCOL: v0.1
ADMISSIBLE_FAMILY: {N1,N2,N3,N4,N5,N6,N7,N8,N9,N10,N11}
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
PRECOMMITTED_REQUIRED_CHECKS: 38
PASSED: 38
FAILED: 0
DIRECT_EVIDENCE_RESULT: PASS
EXTERNAL_APPLICATION_INCREMENT: +1
EXTERNAL_DOMAIN_INCREMENT: +1
DIRECT_CONSTRUCTED_PILOT_INCREMENT: +0
```

---

## 10. What this directly supports / 직접 지지 범위

The case directly supports that, for this frozen NIST AAL2 form-level task, DSD Design can:

```text
consume an externally supplied candidate/construction grammar
preserve source-permitted versus non-permitted route forms
separate generic two-factor structure from source-specific permitted-form grammar
preserve the biometric-not-standalone-authenticator boundary
keep verifier-portfolio requirements separate from individual route-form filtering
avoid inventing implementation-level conformance from form-level data
return the complete fixture-relative admissible family without Optimization
```

It increases external breadth from one application/domain to two applications/two domains.

---

## 11. Limits / 한계

This result does **not** establish:

```text
full NIST SP 800-63B-4 implementation conformance
operational replay resistance of any concrete implementation
phishing resistance of every admitted route
FIPS validation of any concrete authenticator or verifier
protected-channel realization
security superiority of DSD
method gain
independent evaluator validation
cross-team reproducibility
established maturity
```

The eleven positive forms are externally enumerated by NIST, which is stronger external candidate-basis evidence than a wholly project-authored candidate family.
However, the 15-record evaluation fixture and the four negative controls are still project-frozen.
This remains a same-project evaluation of an external source.

The next maturity-relevant pressure should therefore either:

1. use a non-software/physical domain or a real external artifact with irregular candidate options, or
2. prepare a genuinely independent evaluator packet once external breadth is judged sufficient for that stage.

No automatic maturity promotion is performed from this PASS.
