# DES-APP-001 — WCAG 2.2 Submit-Control Design Application

Status: **PASS — first external-standard Design application under Protocol v0.1**  
Date: **2026-09-08**  
Evidence scope: `method_specific`  
Method directly tested: **DSD Design / DSD 설계론**  
Method protocol: **DSD Design Protocol v0.1**  
Case class: **external_application**  
Precommit: `DES-APP-001_precommit.md`, commit `4847dbd`

## 1. External source / 외부 출처

Authoritative source used exactly as frozen:

```text
W3C
Web Content Accessibility Guidelines (WCAG) 2.2
W3C Recommendation 12 December 2024
https://www.w3.org/TR/2024/REC-WCAG22-20241212/
```

Frozen clauses:

```text
SC 1.4.3 Contrast (Minimum), Level AA
SC 2.5.3 Label in Name, Level A
SC 2.5.8 Target Size (Minimum), Level AA
```

The source requirements used in the frozen fixture are:

```text
SC 1.4.3:
  ordinary text contrast ratio >= 4.5:1,
  with the fixture excluding the source-listed exceptions.

SC 2.5.3:
  for a user-interface component with a visible text label,
  the accessible name contains the visually presented text.

SC 2.5.8:
  pointer target size >= 24 by 24 CSS px,
  with the fixture explicitly locking that none of the source-listed exceptions apply.
```

The source note under SC 2.5.3 says that placing the label text at the start of the name is a best practice. It was therefore not promoted into a hard requirement.

No other WCAG criterion was imported after the precommit.
No full-WCAG conformance claim is made.

---

## 2. Frozen bridge execution / 동결 브리지 실행

```text
H0 task-local:
  submit_control is ADMITTED

H1 external SC 2.5.8:
  width >= 24 AND height >= 24 CSS px

H2 external SC 2.5.3:
  accessible name is defined
  AND contains visible label text "Submit"

H3 external SC 1.4.3:
  normal-text contrast ratio >= 4.5:1
```

Status handling remained separate from the external source itself. WCAG does not use DSD status vocabulary; the bridge only maps frozen candidate facts into the selected external checks.

---

## 3. Candidate execution / 후보 실행

| Candidate | H0 | H1 target size | H2 label in name | H3 contrast | Failed set | Result |
|---|---|---|---|---|---|---|
| W1 | pass | pass: 24x24 | pass: `Submit` | pass: 4.5 | none | admissible |
| W2 | pass | pass: 32x28 | pass: `Submit order` | pass: 7.0 | none | admissible |
| W3 | pass | pass: 24x24 | pass: `Checkout Submit` contains `Submit` | pass: 4.5 | none | admissible |
| W4 | pass | fail: 23x24 | pass | pass | H1 | rejected |
| W5 | pass | fail: 24x23 | pass | pass | H1 | rejected |
| W6 | pass | pass | fail: `Send order` does not contain `Submit` | pass | H2 | rejected |
| W7 | pass | pass | fail: `APPLICABLE_BUT_UNDEFINED` | pass | H2 | rejected |
| W8 | pass | pass | pass | fail: 4.4 | H3 | rejected |
| W9 | pass | fail: 20x20 | fail: `Send order` | fail: 4.0 | H1,H2,H3 | rejected |
| W10 | fail: CHANNEL_ABSENCE | not evaluated as defined target size | not evaluated as defined accessible name | not evaluated as defined contrast | H0 | rejected |

The complete admissible family is:

```text
{W1,W2,W3}
```

---

## 4. Threshold checks / 경계값 검사

The frozen external thresholds were applied inclusively exactly as stated.

```text
24x24 CSS px -> H1 pass
23x24 CSS px -> H1 fail
24x23 CSS px -> H1 fail

4.5:1 -> H3 pass
4.4:1 -> H3 fail
```

No target-size exception was added to rescue W4, W5, or W9 after inspection.

W3 remained admissible even though its accessible name begins with `Checkout`, because the hard criterion requires containment of the visible label text and the source's start-position language is only a best-practice note.

---

## 5. Status-sensitive checks / 상태 구분 검사

### W7 — undefined accessible name

```text
accessible_name = APPLICABLE_BUT_UNDEFINED
```

This was not treated as:

```text
a defined empty string that somehow passes
CHANNEL_ABSENCE
a defined name
```

It failed H2 because the required name containment could not be established.

### W10 — absent control

```text
submit_control = CHANNEL_ABSENCE
```

The absent control was not converted into an admitted control with zero width, zero height, empty name, or zero contrast.
Its control-specific properties remained `INAPPLICABLE` and the candidate failed the task-local H0 existence requirement.

---

## 6. DSD Design result / DSD 설계 결과

```text
ADMISSIBLE_TARGETS_OR_ADMISSIBLE_FAMILY:
  {W1,W2,W3}

REJECTED_CANDIDATES:
  W4  -> H1
  W5  -> H1
  W6  -> H2
  W7  -> H2
  W8  -> H3
  W9  -> H1,H2,H3
  W10 -> H0

TERMINAL_DESIGN_STATUS:
  DESIGN_ADMISSIBLE

TERMINAL_STATUS_BASIS:
  the exhaustive frozen fixture W1-W10 was evaluated;
  exactly W1,W2,W3 satisfy H0-H3 under the frozen external-source applicability assumptions

DESIGN_PROTOCOL_CONFORMANCE:
  CONFORMANT

DESIGN_METHOD_GAIN_STATUS:
  NOT_ASSESSED
```

No baseline comparison was run, so the method-gain ledger was not upgraded to `GAIN_ESTABLISHED` or `NO_GAIN`.

No Optimization selected one of W1-W3 as best.

---

## 7. External-scope discipline / 외부 범위 규율

The execution preserved four source-boundary conditions.

1. **No source rewrite** — the selected WCAG criteria were not replaced with DSD-native requirements.
2. **No best-practice promotion** — the SC 2.5.3 note about putting visible text at the start of the name was not converted into a hard criterion.
3. **No exception fabrication** — SC 2.5.8 exceptions were fixed as inapplicable before evaluation and were not invoked post hoc.
4. **No overclaim** — this case establishes only the frozen three-criterion subset for the constructed control fixture, not full WCAG 2.2 conformance.

---

## 8. Precommitted scoring result / 사전 고정 점수

```text
EXTERNAL_SOURCE_AND_SCOPE_CHECKS: 8 / 8 PASS
CANDIDATE_CHECKS:                12 / 12 PASS
THRESHOLD_AND_STATUS_CHECKS:      9 / 9 PASS
PROTOCOL_AND_EVIDENCE_CHECKS:     7 / 7 PASS

PRECOMMITTED_REQUIRED_CHECKS: 36
PASSED: 36
FAILED: 0
CHALLENGE_VERDICT: PASS
```

No failed check was hidden, repaired, or reclassified.

---

## 9. Reproducibility record / 재현성 기록

```text
REPRODUCIBILITY_RECORD:
  protocol: methods/04_design/PROTOCOL_v0.1.md
  precommit: evidence/method_specific/design/DES-APP-001_precommit.md
  precommit_commit: 4847dbd
  external_authority: W3C
  external_standard: WCAG 2.2
  external_version: W3C Recommendation 2024-12-12
  external_dated_url: https://www.w3.org/TR/2024/REC-WCAG22-20241212/
  selected_success_criteria:
    SC 1.4.3
    SC 2.5.3
    SC 2.5.8
  candidate_order: W1-W10
  candidate_coverage: exhaustive relative to frozen fixture only
  bridge: WCAG_APPLICATION_BRIDGE_001
  target_resolution: frozen in precommit
  applicability_assumptions: frozen in precommit
  stochastic_generation: none
  baseline: none
  task_revision_after_lock: none
  candidate_revision_after_lock: none
  source-clause revision_after_lock: none
  exception revision_after_lock: none
```

---

## 10. Evidence verdict / 증거 판정

```text
CASE_ID: DES-APP-001
CASE_CLASS: external_application
CASE_ORIGIN: external_W3C_standard_plus_frozen_candidate_fixture
PROTOCOL: v0.1
EXTERNAL_STANDARD: W3C WCAG 2.2 Recommendation 2024-12-12
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
PRECOMMITTED_REQUIRED_CHECKS: 36
PASSED: 36
FAILED: 0
DIRECT_EVIDENCE_RESULT: PASS
EXTERNAL_APPLICATION_INCREMENT: +1
```

This is the first Design external-standard application under Protocol v0.1.

---

## 11. What this case directly supports / 직접 지지 범위

At single-application level, DES-APP-001 supports that DSD Design can consume a real external normative source while keeping:

```text
external authority separate from DSD verdict
source requirement separate from fixture assumption
hard criterion separate from best-practice note
exception status fixed before candidate evaluation
Formation absence separate from property undefinedness/inapplicability
external subset claim separate from full-standard conformance
```

---

## 12. Limits / 한계

This is an external-standard application but the candidate family remains constructed inside the project.

It does not establish:

```text
full WCAG 2.2 conformance
real deployed website accessibility
external candidate generation
independent evaluator agreement
human usability advantage
runtime/cost advantage
cross-domain generality
method maturity
```

The next major evidence step is a reproducibility/retrace test, preferably using a separately frozen record and a clean re-execution path before the later DSD Audit maturity review.
