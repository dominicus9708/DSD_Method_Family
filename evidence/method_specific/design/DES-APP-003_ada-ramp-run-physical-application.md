# DES-APP-003 — 2010 ADA Ramp-Run Physical Design Application

Status: **EXTERNAL_APPLICATION_PASS**  
Date: **2026-09-09**  
Evidence scope: `method_specific`  
Method directly tested: **DSD Design / DSD 설계론**  
Method protocol: **DSD Design Protocol v0.1**  
Precommit: [`DES-APP-003_precommit.md`](DES-APP-003_precommit.md)  
Precommit commit: `b78ca3a03df1bc93fa3000f470d5451ffd3aa3f1`  
External domain: **built environment / physical accessibility**

## 1. Purpose / 목적

Execute the frozen third external Design application in a non-software physical domain while preserving the independent-evaluator track as unexecuted until a genuinely separate evaluator submission exists.

The application uses selected 2010 ADA ramp requirements as external authority and a project-frozen finite parameter fixture grounded in those source fields.

No baseline comparison is performed.
No method superiority is claimed.

---

## 2. Frozen source verified / 외부 출처 확인

The frozen source remains:

```text
2010 ADA Standards for Accessible Design
U.S. Access Board
Chapter 4 — Accessible Routes
Section 405 — Ramps
https://www.access-board.gov/files/ada/ADA-Standards.pdf
```

The selected source rules used exactly as precommitted are:

```text
§405.2 running slope     -> 1:12 maximum
§405.3 cross slope       -> 1:48 maximum
§405.5 clear width       -> 36 inches minimum
§405.6 rise              -> 30 inches maximum per ramp run
§405.7 landings          -> top and bottom required
```

The execution does not import:

```text
advisory gentler-slope recommendations
alteration-specific steeper-slope allowances
employee-work-area width exception
surfaces
handrails
landing dimensions beyond presence
edge protection
wet-condition drainage
other accessible-route obligations
```

Those items remain outside the frozen claim.

---

## 3. Bridge execution / 브리지 실행

```text
DOMAIN_BRIDGE: ADA_RAMP_RUN_BRIDGE_001
```

The ratio convention is applied as frozen:

```text
running slope 1:n passes H1 when n >= 12
cross slope   1:n passes H2 when n >= 48
```

For `R10`, structural absence is preserved:

```text
ramp_run = CHANNEL_ABSENCE
geometry/property fields = INAPPLICABLE
```

No absent field is zero-filled.

---

## 4. Candidate execution / 후보 판정

### R1

```text
running_slope = 1:12   -> H1 pass
cross_slope = 1:48     -> H2 pass
clear_width = 36       -> H3 pass
rise = 30              -> H4 pass
top/bottom landings    -> H5 pass

RESULT: admissible
```

### R2

```text
running_slope = 1:16
cross_slope = 1:60
clear_width = 42
rise = 12
both landings present

RESULT: admissible
```

### R3

```text
running_slope = 1:11 -> steeper than 1:12
FAILURE_SET: {H1}
RESULT: rejected
```

### R4

```text
cross_slope = 1:40 -> steeper than 1:48
FAILURE_SET: {H2}
RESULT: rejected
```

### R5

```text
clear_width = 35 in < 36 in
FAILURE_SET: {H3}
RESULT: rejected
```

### R6

```text
rise = 31 in > 30 in
FAILURE_SET: {H4}
RESULT: rejected
```

### R7

```text
bottom_landing = ABSENT
FAILURE_SET: {H5}
RESULT: rejected
```

### R8

```text
running_slope = 1:10   -> H1 fail
cross_slope = 1:40     -> H2 fail
clear_width = 34       -> H3 fail
rise = 31              -> H4 fail
top/bottom landings absent -> H5 fail

FAILURE_SET: {H1,H2,H3,H4,H5}
RESULT: rejected
```

### R9

```text
running_slope = 1:20
cross_slope = 1:60
clear_width = 40
rise = 20
both landings present

RESULT: admissible
```

### R10

```text
ramp_run = CHANNEL_ABSENCE
H0 = fail
H1-H5 = INAPPLICABLE at this candidate state

FAILURE_SET: {H0}
RESULT: rejected
```

---

## 5. Admissible family / 허용 설계공간

```text
ADMISSIBLE_FAMILY:
{R1,R2,R9}
```

All three are retained.
No cost, convenience, shorter length, gentler slope, or other preference is used to rank them.

```text
ADMISSIBLE_FAMILY
!=
OPTIMAL_OR_PREFERRED_RAMP
```

---

## 6. Threshold and status pressure / 경계값·상태 압박

The exact threshold cases behaved as frozen:

```text
1:12 running slope -> pass
1:11 running slope -> fail
1:48 cross slope   -> pass
36 in clear width  -> pass
30 in rise         -> pass
```

The absent-ramp control also preserved:

```text
CHANNEL_ABSENCE
!= admitted ramp with width=0, rise=0, or slope=0
```

This prevents a structural nonexistence state from being interpreted as a geometric value.

---

## 7. Source-scope discipline / 출처 범위 규율

The U.S. Access Board remains the authority for the selected ADA checks.
DSD only structures the candidate evaluation.

The execution specifically did **not**:

- apply advisory preferred gentler slopes as mandatory;
- use alteration-specific slope exceptions to rescue R3 or R8;
- use the employee-work-area width exception to rescue R5 or R8;
- infer compliance with omitted handrail, surface, edge-protection, landing-dimension, drainage, or other requirements;
- claim permit approval, structural adequacy, construction safety, or full ADA compliance.

Therefore the strongest valid external claim is:

```text
{R1,R2,R9}
are admissible relative to the frozen selected-subset ramp-run task
within the R1-R10 fixture.
```

---

## 8. Three Design ledgers / 3중 장부

```text
TERMINAL_DESIGN_STATUS:
DESIGN_ADMISSIBLE

DESIGN_PROTOCOL_CONFORMANCE:
CONFORMANT

DESIGN_METHOD_GAIN_STATUS:
NOT_ASSESSED
```

`NOT_ASSESSED` is required because no baseline comparison was run.

---

## 9. Precommitted scoring / 사전 고정 점수

### Source and scope checks

```text
7/7 PASS
```

### Candidate verdict checks

```text
10/10 PASS
```

### Rejection-basis and family checks

```text
8/8 PASS
```

### Threshold and status checks

```text
6/6 PASS
```

### Protocol and claim-discipline checks

```text
7/7 PASS
```

Final:

```text
PRECOMMITTED_REQUIRED_CHECKS: 38
PASSED: 38
FAILED: 0
CHALLENGE_VERDICT: PASS
```

No post-hoc repair, source substitution, exception insertion, candidate alteration, or target-resolution change was used.

---

## 10. Evidence effect / 증거 효과

```text
EXTERNAL_APPLICATION_INCREMENT: +1
EXTERNAL_DOMAIN_INCREMENT: +1
DIRECT_CONSTRUCTED_PILOT_INCREMENT: +0
```

Updated Design external-evidence state:

```text
EXTERNAL_APPLICATIONS: 3
EXTERNAL_DOMAINS: 3
EXTERNAL_APPLICATION_PASSES: 3

DOMAINS:
  web accessibility
  digital identity / authentication security
  built environment / physical accessibility
```

The independent-evaluator ledger is unchanged:

```text
INDEPENDENT_EVALUATOR_PACKET: prepared
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
```

`DES-AUD-001` remains historical and is not rewritten.
This application is new evidence for a future re-audit.

---

## 11. Limits / 한계

- The source is a real external physical-accessibility standard, but the finite `R1-R10` fixture is project-constructed.
- Only selected §405 requirements are active; full ramp compliance is not evaluated.
- The case does not test structural engineering, materials, loads, site grading, construction tolerance, drainage, handrails, edge protection, or inspection practice.
- No competent external baseline is compared.
- No external evaluator participated.
- No practical cost/time/error advantage is measured.

## 12. Next step / 다음 단계

The external evidence breadth now spans three materially different domains.

The main unresolved maturity blocker remains genuinely independent evaluation.
The next evidence-changing event should therefore be an eligible frozen `DES-IEP-001` evaluator submission before reference-key reveal.

A future revision maturity audit should occur only after such materially new evidence or another comparably strong independent record exists.
