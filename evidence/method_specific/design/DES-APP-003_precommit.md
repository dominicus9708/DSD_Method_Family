# DES-APP-003 — 2010 ADA Ramp-Run Physical Design Precommit

Status: **PRECOMMITTED BEFORE DESIGN SCORING**  
Date: **2026-09-09**  
Evidence scope: `method_specific`  
Method directly tested: **DSD Design / DSD 설계론**  
Method protocol: **DSD Design Protocol v0.1**  
Case class: **external_application**  
External domain: **built environment / physical accessibility**

## 1. Purpose / 목적

Run a third external Design application while the independent-evaluator track remains externally blocked pending a genuinely separate submission.

This case moves from software/UI accessibility and digital-identity security into a materially different **physical built-environment** domain.

It tests whether DSD Design can consume a frozen subset of the U.S. Access Board / 2010 ADA Standards ramp-run requirements without:

- turning advisory recommendations into hard requirements;
- importing alteration exceptions into a general new-ramp task after candidate inspection;
- treating an absent ramp run as an admitted ramp with zero-valued dimensions;
- claiming full ADA ramp compliance from a deliberately limited subset;
- silently optimizing among multiple admissible ramp configurations.

The goal is not to show DSD superiority.
No baseline comparison is active.

---

## 2. Frozen external source / 외부 출처 동결

```text
EXTERNAL_STANDARD:
  2010 ADA Standards for Accessible Design
  Chapter 4 — Accessible Routes
  Section 405 — Ramps

AUTHORITATIVE_SOURCE:
  U.S. Access Board

PRIMARY_OFFICIAL_ARTIFACT:
  https://www.access-board.gov/files/ada/ADA-Standards.pdf

SUPPORTING_TECHNICAL_GUIDE:
  https://www.access-board.gov/files/ada/guides/ramps.pdf
```

Claim-relevant source rules frozen for this case:

```text
S1  §405.2 running slope: 1:12 maximum for the ordinary ramp-run scope used here.

S2  §405.3 cross slope: 1:48 maximum.

S3  §405.5 clear width: 36 inches minimum.

S4  §405.6 rise: 30 inches maximum per ramp run.

S5  §405.7 landings: landings are required at the top and bottom of each ramp run.
```

Important scope lock:

```text
The source also contains other ramp requirements and exceptions.
This case does NOT evaluate full §405 compliance.

Inactive / out-of-scope for this fixture include, among other things:
  surfaces
  handrails
  landing dimensions beyond presence
  edge protection
  wet-condition drainage
  other accessible-route obligations
  alteration-specific steeper-slope allowances
  employee-work-area width exception
```

Advisory recommendations for gentler slopes are not hard constraints in this case.
The alteration allowances for steeper slopes are not available because the frozen task is not an alteration exception case.

---

## 3. Design task lock / 설계 과업 동결

```text
CASE_ID: DES-APP-003
DESIGN_TASK_ID: DES-TASK-APP-003
PROTOCOL_VERSION: v0.1
TASK_SCOPE:
  construct/filter the admissible family of ramp-run configurations
  relative only to the frozen task-local ramp-existence requirement
  and selected ADA §405.2, §405.3, §405.5, §405.6, §405.7 checks

CLAIMED_OUTPUT_LEVEL:
  DESIGN_SPACE

GOALS:
  provide an admitted ramp run satisfying all frozen checks

HARD_CONSTRAINTS:
  H0 RAMP_RUN_ADMITTED
  H1 RUNNING_SLOPE_NOT_STEEPER_THAN_1_TO_12
  H2 CROSS_SLOPE_NOT_STEEPER_THAN_1_TO_48
  H3 CLEAR_WIDTH_AT_LEAST_36_IN
  H4 RISE_AT_MOST_30_IN
  H5 TOP_AND_BOTTOM_LANDINGS_PRESENT

CONSTRAINT_SOURCE_OR_SPECIFICATION:
  H0 task-local design requirement
  H1-H5 selected 2010 ADA Standards §405 requirements

BASE_STRUCTURE_OR_PREDECESSOR:
  none

TARGET_DSD_LAYER_SCOPE:
  Formation
  General Property

TARGET_RESOLUTION:
  ramp-run admission state
  running-slope ratio
  cross-slope ratio
  clear width in inches
  rise in inches
  top-landing presence
  bottom-landing presence

CANDIDATE_OR_CONSTRUCTION_BASIS:
  source-grounded parameter schema from selected ADA §405 fields
  plus explicit frozen finite fixture {R1-R10}

CANDIDATE_GENERATION_RULE:
  enumerate R1-R10 exactly once in listed order

CANDIDATE_COVERAGE:
  exhaustive relative only to the frozen DES-APP-003 R1-R10 fixture
  not exhaustive over all real ramp designs

DSD_INTERFACE_PROFILE:
  current Design Protocol v0.1 Formation + General Property discipline

DOMAIN_BRIDGE:
  ADA_RAMP_RUN_BRIDGE_001

EXTERNAL_STANDARD:
  2010 ADA Standards for Accessible Design, selected §405 subset

VALIDATION_OR_ACCEPTANCE_RULE:
  a candidate is admissible only if H0-H5 all pass at the declared resolution

SOFT_PREFERENCES:
  none

AUXILIARY_METHODS_OR_HANDOFFS:
  none

NONOPTIMIZATION_SELECTION_RULE_IF_NEEDED:
  not used; return the full admissible family
```

---

## 4. Frozen bridge / 동결 도메인 브리지

```text
ADA_RAMP_RUN_BRIDGE_001
```

Ratio convention:

```text
running slope 1:n
  passes H1 when n >= 12
  because a smaller denominator is steeper

cross slope 1:n
  passes H2 when n >= 48
```

Status discipline:

```text
CHANNEL_ABSENCE for ramp_run -> H0 fail
properties of an absent ramp run -> INAPPLICABLE
INAPPLICABLE is not coerced to numeric zero
```

The bridge does not claim that ADA itself uses DSD status terminology.
It only maps the frozen fixture into the selected external checks.

---

## 5. Frozen candidate fixture / 후보군 동결

```text
R1
  ramp_run = ADMITTED
  running_slope = 1:12
  cross_slope = 1:48
  clear_width_in = 36
  rise_in = 30
  top_landing = PRESENT
  bottom_landing = PRESENT

R2
  ramp_run = ADMITTED
  running_slope = 1:16
  cross_slope = 1:60
  clear_width_in = 42
  rise_in = 12
  top_landing = PRESENT
  bottom_landing = PRESENT

R3
  ramp_run = ADMITTED
  running_slope = 1:11
  cross_slope = 1:48
  clear_width_in = 36
  rise_in = 12
  top_landing = PRESENT
  bottom_landing = PRESENT

R4
  ramp_run = ADMITTED
  running_slope = 1:12
  cross_slope = 1:40
  clear_width_in = 36
  rise_in = 12
  top_landing = PRESENT
  bottom_landing = PRESENT

R5
  ramp_run = ADMITTED
  running_slope = 1:12
  cross_slope = 1:48
  clear_width_in = 35
  rise_in = 12
  top_landing = PRESENT
  bottom_landing = PRESENT

R6
  ramp_run = ADMITTED
  running_slope = 1:12
  cross_slope = 1:48
  clear_width_in = 36
  rise_in = 31
  top_landing = PRESENT
  bottom_landing = PRESENT

R7
  ramp_run = ADMITTED
  running_slope = 1:12
  cross_slope = 1:48
  clear_width_in = 36
  rise_in = 12
  top_landing = PRESENT
  bottom_landing = ABSENT

R8
  ramp_run = ADMITTED
  running_slope = 1:10
  cross_slope = 1:40
  clear_width_in = 34
  rise_in = 31
  top_landing = ABSENT
  bottom_landing = ABSENT

R9
  ramp_run = ADMITTED
  running_slope = 1:20
  cross_slope = 1:60
  clear_width_in = 40
  rise_in = 20
  top_landing = PRESENT
  bottom_landing = PRESENT

R10
  ramp_run = CHANNEL_ABSENCE
  running_slope = INAPPLICABLE
  cross_slope = INAPPLICABLE
  clear_width_in = INAPPLICABLE
  rise_in = INAPPLICABLE
  top_landing = INAPPLICABLE
  bottom_landing = INAPPLICABLE
```

No candidate may be added, deleted, repaired, or reinterpreted after this precommit.

---

## 6. Frozen expected candidate results / 후보별 기대 판정

```text
R1  -> admissible
R2  -> admissible
R3  -> rejected on {H1}
R4  -> rejected on {H2}
R5  -> rejected on {H3}
R6  -> rejected on {H4}
R7  -> rejected on {H5}
R8  -> rejected on {H1,H2,H3,H4,H5}
R9  -> admissible
R10 -> rejected on {H0}; H1-H5 remain inapplicable because the ramp run is absent
```

Expected admissible family:

```text
{R1,R2,R9}
```

Expected three ledgers:

```text
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

---

## 7. Scope and anti-overclaim guards / 범위 가드

The execution must preserve all of the following:

```text
G1  U.S. Access Board / ADA remains the external authority.
G2  Advisory gentler-slope recommendations are not promoted to hard constraints.
G3  Alteration-specific steeper-slope allowances are not inserted into this ordinary frozen task.
G4  Employee-work-area width exception is not inserted after candidate inspection.
G5  R10 absence is not treated as zero-valued ramp geometry.
G6  The output is only a selected-subset ramp-run design-space verdict.
G7  No claim of full ADA ramp compliance, permit approval, structural adequacy, construction safety, or usability superiority is made.
G8  No Optimization ranks R1, R2, and R9.
```

---

## 8. Precommitted scoring / 사전 고정 점수

### Source and scope checks — 7

1. official U.S. Access Board / 2010 ADA Standards source preserved;
2. §405.2 running-slope threshold preserved as 1:12 maximum;
3. §405.3 cross-slope threshold preserved as 1:48 maximum;
4. §405.5 clear-width threshold preserved as 36 inches minimum;
5. §405.6 rise threshold preserved as 30 inches maximum;
6. §405.7 top/bottom landing requirement preserved;
7. advisory and alteration/employee-work-area exceptions remain outside this frozen task unless explicitly active, which they are not.

### Candidate verdict checks — 10

8. R1 admissible.
9. R2 admissible.
10. R3 rejected.
11. R4 rejected.
12. R5 rejected.
13. R6 rejected.
14. R7 rejected.
15. R8 rejected.
16. R9 admissible.
17. R10 rejected.

### Rejection-basis and family checks — 8

18. R3 fails exactly H1.
19. R4 fails exactly H2.
20. R5 fails exactly H3.
21. R6 fails exactly H4.
22. R7 fails exactly H5.
23. R8 fails exactly H1,H2,H3,H4,H5.
24. R10 fails H0 and retains H1-H5 as inapplicable rather than numeric failures.
25. admissible family is exactly {R1,R2,R9} within the fixture.

### Threshold and status checks — 6

26. running slope 1:12 passes H1.
27. running slope 1:11 fails H1 in the frozen ordinary-ramp scope.
28. cross slope 1:48 passes H2.
29. clear width 36 inches passes H3.
30. rise 30 inches passes H4.
31. CHANNEL_ABSENCE is not coerced into an admitted ramp with zero-valued properties.

### Protocol and claim-discipline checks — 7

32. TERMINAL_DESIGN_STATUS = DESIGN_ADMISSIBLE.
33. DESIGN_PROTOCOL_CONFORMANCE = CONFORMANT.
34. DESIGN_METHOD_GAIN_STATUS = NOT_ASSESSED.
35. no hidden Optimization occurs among R1,R2,R9.
36. candidate coverage remains fixture-relative.
37. no full ADA ramp-compliance or broader engineering certification claim is made.
38. no post-hoc source, candidate, exception, target-resolution, or acceptance-rule revision is introduced.

```text
PRECOMMITTED_REQUIRED_CHECKS: 38
```

Any failed check remains failed under this case ID.
No post-hoc rescue is permitted.

---

## 9. Evidence-count rule / 증거 수 규칙

If executed successfully:

```text
EXTERNAL_APPLICATION_INCREMENT: +1
EXTERNAL_DOMAIN_INCREMENT: +1
DIRECT_CONSTRUCTED_PILOT_INCREMENT: +0
```

This case does not alter the independent-evaluator ledger.
It does not retroactively change `DES-AUD-001`.
Any maturity reclassification requires a separate later Audit.
