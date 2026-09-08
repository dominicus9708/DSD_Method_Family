# DES-APP-001 — WCAG 2.2 Submit-Control Design Application Precommit

Status: **PRECOMMITTED BEFORE EVALUATION**  
Date: **2026-09-08**  
Evidence scope: `method_specific`  
Method directly tested: **DSD Design / DSD 설계론**  
Method protocol: **DSD Design Protocol v0.1**  
Case class: **external_application**

## 1. Purpose / 목적

Apply DSD Design Protocol v0.1 to a real external standard rather than a DSD-internal synthetic rule set.

The external authority is **W3C Web Content Accessibility Guidelines (WCAG) 2.2**, W3C Recommendation dated 12 December 2024.

This application deliberately tests only a frozen subset of WCAG 2.2 requirements relevant to one authored submit control. It does **not** claim full WCAG 2.2 conformance for a page, site, product, or process.

The external requirements, fixture assumptions, candidate family, expected result, and scoring criteria are frozen before evaluation.

---

## 2. External source lock / 외부 출처 동결

Authoritative source:

```text
W3C
Web Content Accessibility Guidelines (WCAG) 2.2
W3C Recommendation 12 December 2024
Dated version:
https://www.w3.org/TR/2024/REC-WCAG22-20241212/
Latest published version consulted:
https://www.w3.org/TR/WCAG22/
```

Frozen source clauses used in this application:

### WCAG 2.2 SC 1.4.3 — Contrast (Minimum), Level AA

For ordinary text in this fixture, the frozen relevant threshold is:

```text
contrast ratio >= 4.5:1
```

The fixture explicitly excludes the large-text, incidental, and logotype exceptions.

### WCAG 2.2 SC 2.5.3 — Label in Name, Level A

For a user-interface component with a visible text label:

```text
the accessible name contains the text presented visually
```

The WCAG note that having the label text at the start of the name is a best practice is not treated as a hard requirement.

### WCAG 2.2 SC 2.5.8 — Target Size (Minimum), Level AA

For the authored pointer target in this fixture:

```text
target size >= 24 by 24 CSS pixels
```

The fixture explicitly locks that none of the SC 2.5.8 exceptions apply:

```text
Spacing exception: not applicable to the frozen fixture
Equivalent-control exception: not applicable
Inline exception: not applicable
User-agent-control exception: not applicable
Essential/legal-presentation exception: not applicable
```

No unlisted WCAG requirement is imported into this case after the precommit.

---

## 3. Frozen Design task / 동결 설계 과업

```text
CASE_ID: DES-APP-001
DESIGN_TASK_ID: DES-TASK-APP-001
PROTOCOL_VERSION: v0.1
CASE_CLASS: external_application
CASE_ORIGIN: external_W3C_standard_plus_frozen_candidate_fixture
TASK_SCOPE:
  identify the complete admissible family of submit-control designs
  relative only to the frozen task-local existence requirement and
  WCAG 2.2 SC 1.4.3, 2.5.3, and 2.5.8 under the frozen applicability assumptions
CLAIMED_OUTPUT_LEVEL: DESIGN_SPACE
GOALS:
  G1 provide one authored submit user-interface control
  G2 satisfy the three frozen WCAG success-criterion checks at the declared resolution
CONSTRAINT_SOURCE_OR_SPECIFICATION:
  task-local control-existence requirement + W3C WCAG 2.2 dated Recommendation
BASE_STRUCTURE_OR_PREDECESSOR:
  none; explicit candidate control records
TARGET_DSD_LAYER_SCOPE:
  Formation
  General Property
TARGET_RESOLUTION:
  submit-control admission state
  target width in CSS px
  target height in CSS px
  visible label text
  accessible-name status/value
  normal-text contrast ratio
CANDIDATE_OR_CONSTRUCTION_BASIS:
  explicit frozen finite family {W1-W10}
CANDIDATE_GENERATION_RULE:
  none; enumerate W1-W10 exactly once in listed order
CANDIDATE_COVERAGE:
  exhaustive relative only to DES-TASK-APP-001 fixture
DSD_INTERFACE_PROFILE:
  current Formation + General Property interface used by Design Protocol v0.1
DOMAIN_BRIDGE:
  WCAG_APPLICATION_BRIDGE_001 frozen in this precommit
EXTERNAL_STANDARD:
  W3C WCAG 2.2 Recommendation 2024-12-12; SC 1.4.3, 2.5.3, 2.5.8 only
AUXILIARY_METHODS_OR_HANDOFFS:
  none
SOFT_PREFERENCES:
  none
NONOPTIMIZATION_SELECTION_RULE_IF_NEEDED:
  none; return complete admissible family
```

---

## 4. Frozen bridge / 동결 도메인 브리지

```text
WCAG_APPLICATION_BRIDGE_001
```

Task-local requirement:

```text
H0 submit_control is ADMITTED
```

External-standard checks:

```text
H1 SC 2.5.8 target-size check:
   width >= 24 CSS px AND height >= 24 CSS px
   because the frozen fixture states that no SC 2.5.8 exception applies

H2 SC 2.5.3 label-in-name check:
   accessible name is defined
   AND contains the visible label text "Submit"

H3 SC 1.4.3 contrast-minimum check:
   contrast ratio >= 4.5:1
   because the frozen text is ordinary active non-logo text
```

DSD status handling under the bridge:

```text
CHANNEL_ABSENCE for submit_control -> H0 fail
APPLICABLE_BUT_UNDEFINED accessible name -> H2 fail, not coerced to empty-string success or to structural absence
INAPPLICABLE property on absent control -> preserved as inapplicable; not treated as a numeric or text value
DEFINED_ZERO / DEFINED_NONZERO distinction is preserved where applicable, but this fixture uses explicit numeric contrast ratios rather than a zero/nonzero threshold
```

The bridge does not claim that WCAG itself uses DSD status terminology.
It only maps frozen candidate facts into the three selected external checks.

---

## 5. Frozen applicability assumptions / 동결 적용 가정

Every admitted-control candidate W1-W9 has:

```text
component type: authored user-interface button/control
visible label text: "Submit"
pointer target: author-defined
text scale: ordinary / not large-scale
component state: active
text role: not decorative
text role: not logo or brand name
SC 2.5.8 exceptions: none apply
```

W10 contains no admitted submit control and therefore its control properties are marked `INAPPLICABLE` rather than fabricated.

These assumptions are fixture facts, not claims that the WCAG source independently supplies this specific interface context.

---

## 6. Frozen candidate family / 동결 후보군

```text
W1:
  submit_control = ADMITTED
  width = 24
  height = 24
  visible_label = "Submit"
  accessible_name = DEFINED("Submit")
  contrast_ratio = 4.5

W2:
  submit_control = ADMITTED
  width = 32
  height = 28
  visible_label = "Submit"
  accessible_name = DEFINED("Submit order")
  contrast_ratio = 7.0

W3:
  submit_control = ADMITTED
  width = 24
  height = 24
  visible_label = "Submit"
  accessible_name = DEFINED("Checkout Submit")
  contrast_ratio = 4.5

W4:
  submit_control = ADMITTED
  width = 23
  height = 24
  visible_label = "Submit"
  accessible_name = DEFINED("Submit")
  contrast_ratio = 7.0

W5:
  submit_control = ADMITTED
  width = 24
  height = 23
  visible_label = "Submit"
  accessible_name = DEFINED("Submit")
  contrast_ratio = 7.0

W6:
  submit_control = ADMITTED
  width = 24
  height = 24
  visible_label = "Submit"
  accessible_name = DEFINED("Send order")
  contrast_ratio = 7.0

W7:
  submit_control = ADMITTED
  width = 24
  height = 24
  visible_label = "Submit"
  accessible_name = APPLICABLE_BUT_UNDEFINED
  contrast_ratio = 7.0

W8:
  submit_control = ADMITTED
  width = 24
  height = 24
  visible_label = "Submit"
  accessible_name = DEFINED("Submit")
  contrast_ratio = 4.4

W9:
  submit_control = ADMITTED
  width = 20
  height = 20
  visible_label = "Submit"
  accessible_name = DEFINED("Send order")
  contrast_ratio = 4.0

W10:
  submit_control = CHANNEL_ABSENCE
  width = INAPPLICABLE
  height = INAPPLICABLE
  visible_label = INAPPLICABLE
  accessible_name = INAPPLICABLE
  contrast_ratio = INAPPLICABLE
```

No candidate may be added, removed, edited, or reinterpreted after this precommit.

---

## 7. Frozen expected candidate results / 동결 예상 후보 결과

```text
W1  -> admissible
W2  -> admissible
W3  -> admissible
W4  -> rejected on {H1}
W5  -> rejected on {H1}
W6  -> rejected on {H2}
W7  -> rejected on {H2}
W8  -> rejected on {H3}
W9  -> rejected on {H1,H2,H3}
W10 -> rejected on {H0}; H1-H3 not evaluated as defined control properties
```

Expected admissible family:

```text
{W1,W2,W3}
```

Important boundary locks:

```text
24 by 24 passes H1 exactly at the threshold.
4.5:1 passes H3 exactly at the threshold.
W3 passes H2 even though "Submit" is not at the start of the accessible name,
because the source makes start-position a best practice note rather than the criterion itself.
No SC 2.5.8 exception is invented to rescue W4, W5, or W9.
No full-WCAG-conformance claim is permitted.
```

---

## 8. Frozen expected DSD result / 동결 DSD 예상 결과

```text
ADMISSIBLE_TARGETS_OR_ADMISSIBLE_FAMILY: {W1,W2,W3}
REJECTED_CANDIDATES: {W4,W5,W6,W7,W8,W9,W10}
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

No baseline comparison is part of DES-APP-001.
Therefore neither `GAIN_ESTABLISHED` nor `NO_GAIN` may be inferred.

---

## 9. Precommitted required checks / 사전 고정 검사

### External-source and scope checks

1. The external authority is W3C WCAG 2.2 Recommendation dated 2024-12-12.
2. Only SC 1.4.3, SC 2.5.3, and SC 2.5.8 are imported as external hard checks.
3. The application does not claim full WCAG 2.2 conformance.
4. SC 1.4.3 is applied at 4.5:1 because the fixture locks ordinary active non-logo text.
5. SC 2.5.3 is applied as visible-label text being contained in the accessible name.
6. The best-practice note about placing visible label text at the start of the name is not promoted into a hard requirement.
7. SC 2.5.8 is applied as at least 24 by 24 CSS px under the frozen no-exception fixture.
8. No SC 2.5.8 exception is invented after candidate inspection.

### Candidate checks

9. DSD evaluates exactly W1-W10.
10. W1 is admissible.
11. W2 is admissible.
12. W3 is admissible.
13. W4 fails exactly {H1}.
14. W5 fails exactly {H1}.
15. W6 fails exactly {H2}.
16. W7 fails exactly {H2} without coercing undefined name into another status.
17. W8 fails exactly {H3}.
18. W9 fails exactly {H1,H2,H3}.
19. W10 fails H0 as CHANNEL_ABSENCE and its control properties remain INAPPLICABLE.
20. The complete admissible family is exactly {W1,W2,W3}.

### Threshold and status checks

21. Width 24 passes the frozen target-size threshold.
22. Height 24 passes the frozen target-size threshold.
23. Width 23 fails H1 when no exception applies.
24. Height 23 fails H1 when no exception applies.
25. Contrast 4.5 passes H3.
26. Contrast 4.4 fails H3.
27. `APPLICABLE_BUT_UNDEFINED` accessible name is not treated as a defined name.
28. `CHANNEL_ABSENCE` is not treated as an admitted control with zero-valued properties.
29. `INAPPLICABLE` on W10 is not coerced into a defined width, height, name, or contrast value.

### Protocol and evidence checks

30. TERMINAL_DESIGN_STATUS = DESIGN_ADMISSIBLE.
31. DESIGN_PROTOCOL_CONFORMANCE = CONFORMANT.
32. DESIGN_METHOD_GAIN_STATUS = NOT_ASSESSED because no baseline comparison is run.
33. No hidden Optimization selects one of W1-W3 as best.
34. No candidate or constraint is revised after precommit.
35. The external standard remains separately identified from the DSD method verdict.
36. The result record includes the dated external source, task-local assumptions, candidate records, rejection bases, and reproducibility record.

```text
PRECOMMITTED_REQUIRED_CHECKS: 36
```

Any failed check remains failed in the executed result.
No post-hoc source reinterpretation, exception insertion, or candidate repair is permitted.

---

## 10. Evidence-count rule / 증거 수 규칙

Once executed after this precommit, `DES-APP-001` counts as one external-application Design evidence record regardless of outcome.

A successful run may fill the Design `external_application` evidence category at the single-application level.
It does not establish independent evaluator agreement, broad external generality, or method maturity.

---

## 11. Frozen limitations / 동결 한계

This application uses a real external standard but a constructed finite candidate fixture.

It directly tests whether DSD Design can consume externally authoritative constraints without:

```text
rewriting the source criterion
promoting best practice into a hard requirement
inventing an exception
collapsing undefined/inapplicable/absent states
claiming more external conformance than the frozen subset supports
```

It does not establish:

```text
full WCAG 2.2 conformance
website-wide accessibility
human usability advantage
runtime advantage
independent evaluator agreement
external candidate-generation quality
method maturity
```
