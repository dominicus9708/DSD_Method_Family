# DES-APP-002 — NIST SP 800-63B-4 AAL2 Route-Form Design Precommit

Status: **PRECOMMITTED BEFORE DESIGN SCORING**  
Date: **2026-09-09**  
Evidence scope: `method_specific`  
Method directly tested: **DSD Design / DSD 설계론**  
Method protocol: **DSD Design Protocol v0.1**  
Case class: **external_application**  
External domain: **digital identity / authentication security**

## 1. Purpose / 목적

Run the second external Design application in a domain materially different from the prior WCAG user-interface accessibility case.

This case tests whether DSD Design can consume an **externally supplied authenticator-type and combination grammar** from NIST SP 800-63B-4 without:

- inventing a universal candidate generator;
- turning verifier-level requirements into per-route requirements;
- treating every two-factor combination as NIST-permitted AAL2;
- treating a biometric characteristic as a standalone authenticator;
- overclaiming deployed-system AAL2 conformance from a form-level design-space result.

The goal is not to show DSD superiority.
No baseline comparison is active in this case.

---

## 2. Frozen external source / 외부 출처 동결

```text
EXTERNAL_STANDARD:
  NIST SP 800-63B-4
  Digital Identity Guidelines: Authentication and Authenticator Management
  July 2025

AUTHORITATIVE_SOURCE:
  NIST / official 800-63-4 publication and HTML rendering

PRIMARY_SECTION:
  Authentication Assurance Level 2
  Permitted Authenticator Types
  Authenticator and Verifier Requirements
```

Claim-relevant source rules frozen for this case:

```text
S1  AAL2 requires proof of possession/control of two distinct authentication factors.

S2  AAL2 authentication SHALL use either:
      a) a multi-factor authenticator, or
      b) a combination of two single-factor authenticators.

S3  Permitted multi-factor authenticator forms:
      MF out-of-band
      MF OTP
      MF cryptographic authentication

S4  A permitted two-single-factor form SHALL include one physical authenticator from:
      look-up secret
      out-of-band device
      SF OTP
      SF cryptographic authentication
    in conjunction with either:
      password
      biometric comparison

S5  A biometric characteristic is not recognized as an authenticator by itself.

S6  At AAL2, at least one authenticator used in the actual authentication process SHALL be replay-resistant.

S7  Verifiers SHALL offer at least one phishing-resistant authentication option at AAL2.
```

Important scope lock:

```text
S6 is an operational authentication-process requirement.
S7 is a verifier-offering / portfolio-level requirement.

This Design task resolves route FORM only.
It does not certify implementation-level replay resistance,
approved-cryptography implementation details,
protected-channel realization,
FIPS validation,
or full verifier-portfolio compliance.
```

The case therefore must not reject a source-permitted route form merely because that individual form is not established here as phishing-resistant.

---

## 3. Design task lock / 설계 과업 동결

```text
CASE_ID: DES-APP-002
DESIGN_TASK_ID: DES-TASK-APP-002
PROTOCOL_VERSION: v0.1
TASK_SCOPE:
  construct/filter the source-permitted AAL2 authenticator route-form design space
  at authenticator-topology resolution

CLAIMED_OUTPUT_LEVEL:
  DESIGN_SPACE

GOALS:
  return every candidate in the frozen fixture whose route form matches
  the NIST SP 800-63B-4 AAL2 permitted-form grammar

HARD_CONSTRAINTS:
  H1 NIST_AAL2_PERMITTED_FORM
  H2 TWO_DISTINCT_FACTOR_STRUCTURE

CONSTRAINT_SOURCE_OR_SPECIFICATION:
  NIST SP 800-63B-4 AAL2 normative text for H1/H2

BASE_STRUCTURE_OR_PREDECESSOR:
  none

TARGET_DSD_LAYER_SCOPE:
  Formation
  General Property

TARGET_RESOLUTION:
  route topology
  authenticator class or classes
  password / biometric-comparison partner where applicable
  source-grounded standalone-authenticator status where claim relevant

CANDIDATE_COVERAGE:
  exhaustive relative only to the frozen DES-APP-002 15-form fixture
  not exhaustive over all conceivable products, protocols, implementations, or deployments

DSD_INTERFACE_PROFILE:
  current project Design v0.1 interface discipline

DOMAIN_BRIDGE:
  NIST_AAL2_ROUTE_FORM_BRIDGE_001

EXTERNAL_STANDARD:
  NIST SP 800-63B-4, July 2025

VALIDATION_OR_ACCEPTANCE_RULE:
  A candidate is Design-admissible only if its form satisfies both H1 and H2.
  Operational implementation requirements outside TARGET_RESOLUTION remain unclaimed.

SOFT_PREFERENCES:
  none

AUXILIARY_METHODS_OR_HANDOFFS:
  none

NONOPTIMIZATION_SELECTION_RULE_IF_NEEDED:
  not used
```

---

## 4. External candidate/construction basis / 외부 후보·구성 기반

The positive grammar is supplied directly by the NIST AAL2 permitted-authenticator rules rather than invented as a DSD-specific generator.

The fixture freezes the eleven source-permitted forms plus four source-grounded controls constructed only from authenticator/factor forms explicitly recognized by the same NIST corpus.

### Permitted-form candidates

```text
N1   MF out-of-band
N2   MF OTP
N3   MF cryptographic authentication

N4   password + look-up secret
N5   password + out-of-band device
N6   password + SF OTP
N7   password + SF cryptographic authentication

N8   biometric comparison + look-up secret
N9   biometric comparison + out-of-band device
N10  biometric comparison + SF OTP
N11  biometric comparison + SF cryptographic authentication
```

### Source-grounded controls

```text
N12  password only
N13  SF cryptographic authentication only
N14  biometric comparison alone
N15  password + biometric comparison
```

The fixture itself is project-frozen, but the primitive types and the eleven positive route forms are source-supplied.
The four controls are included to test exact source-boundary behavior, not to claim an exhaustive universe of invalid forms.

---

## 5. Frozen candidate expectations / 후보별 기대 판정

```text
N1   H1 pass / H2 pass -> admissible
N2   H1 pass / H2 pass -> admissible
N3   H1 pass / H2 pass -> admissible
N4   H1 pass / H2 pass -> admissible
N5   H1 pass / H2 pass -> admissible
N6   H1 pass / H2 pass -> admissible
N7   H1 pass / H2 pass -> admissible
N8   H1 pass / H2 pass -> admissible
N9   H1 pass / H2 pass -> admissible
N10  H1 pass / H2 pass -> admissible
N11  H1 pass / H2 pass -> admissible

N12  H1 fail / H2 fail -> rejected
N13  H1 fail / H2 fail -> rejected
N14  H1 fail / H2 fail -> rejected
N15  H1 fail / H2 pass -> rejected
```

Rationale lock for controls:

```text
N12 password only:
  single factor; not an AAL2 permitted route form

N13 SF cryptographic only:
  possession only; not an AAL2 permitted route form

N14 biometric comparison alone:
  NIST explicitly does not recognize biometric characteristic as an authenticator by itself

N15 password + biometric comparison:
  two distinct factor categories may be present,
  but the NIST two-single-factor AAL2 grammar requires the password/biometric partner
  to be combined with one listed physical authenticator;
  therefore H2 alone is insufficient and H1 fails
```

Expected Design family:

```text
{N1,N2,N3,N4,N5,N6,N7,N8,N9,N10,N11}
```

Expected three ledgers:

```text
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

---

## 6. Scope and bridge guards / 범위·브리지 가드

The execution must preserve all of the following:

```text
G1  NIST authority remains external authority; DSD does not replace it.
G2  The eleven positive forms come from the source-permitted AAL2 grammar.
G3  N15 is not admitted merely because it contains two distinct factor categories.
G4  Biometric comparison alone is not promoted into a standalone authenticator.
G5  Verifier-level phishing-resistant-option requirement is not applied as a per-route rejection rule.
G6  Operational replay-resistance/cryptography/channel/FIPS requirements are not silently marked satisfied from route form alone.
G7  DESIGN_ADMISSIBLE means admissible at the frozen route-form resolution only.
G8  No full deployed-system AAL2-conformance claim is made.
G9  No candidate outside the frozen fixture is inferred absent or invalid.
G10 No Optimization/ranking operation is introduced.
```

---

## 7. Precommitted scoring / 사전 고정 점수

### Source and provenance checks — 6

1. official NIST SP 800-63B-4 source/version preserved;
2. AAL2 two-factor rule preserved;
3. three multi-factor forms preserved;
4. physical-authenticator-plus-password/biometric grammar preserved;
5. biometric-alone limitation preserved;
6. verifier-level phishing-resistant-option requirement preserved at its own scope.

### Candidate verdict checks — 15

7-17. N1-N11 are each admitted.
18-21. N12-N15 are each rejected.

### Rejection-basis and family checks — 5

22. N12 fails H1 and H2.
23. N13 fails H1 and H2.
24. N14 fails H1 and H2 and retains the biometric-not-standalone-authenticator note.
25. N15 fails H1 while H2 passes.
26. admissible family is exactly N1-N11 within the frozen fixture.

### Scope/bridge discipline checks — 6

27. external authority remains separate from Design verdict.
28. S7 is not converted into a per-route hard rejection rule.
29. implementation-level replay resistance is not fabricated from route form alone.
30. approved-cryptography/protected-channel/FIPS implementation conformance is not fabricated.
31. candidate coverage remains fixture-relative.
32. no full-system AAL2 conformance is claimed.

### Ledger and protocol checks — 6

33. terminal status is DESIGN_ADMISSIBLE.
34. protocol conformance is CONFORMANT.
35. method gain is NOT_ASSESSED.
36. no hidden Optimization occurs.
37. Formation and General Property remain within their declared roles.
38. no post-hoc task, candidate-basis, source-scope, or acceptance-rule revision is introduced after precommit.

```text
PRECOMMITTED_REQUIRED_CHECKS: 38
```

A failed source interpretation, bridge violation, candidate verdict, scope guard, or ledger check remains a failure and will not be repaired after scoring begins under this case ID.

---

## 8. Evidence-count rule / 증거 수 규칙

If executed successfully:

```text
EXTERNAL_APPLICATION_INCREMENT: +1
EXTERNAL_DOMAIN_INCREMENT: +1
DIRECT_CONSTRUCTED_PILOT_INCREMENT: +0
```

This is an external application, not a constructed Design challenge.
It does not automatically change the `developing` maturity classification or establish independent evaluator validation.
A later maturity re-audit must be a separate record.
