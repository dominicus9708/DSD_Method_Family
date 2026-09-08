# DES-CH-007 — DES-APP-001 Deterministic Retrace

Status: **PASS — first dedicated deterministic Design retrace under Protocol v0.1**  
Date: **2026-09-08**  
Evidence scope: `method_specific`  
Method directly tested: **DSD Design / DSD 설계론**  
Method protocol: **DSD Design Protocol v0.1**  
Case class: **reproducibility**  
Precommit: `DES-CH-007_precommit.md`, commit `d6d9103`

## 1. Evidence claim / 증거 주장

This case re-executes the claim-relevant logic of `DES-APP-001` from the frozen Design Protocol v0.1 and frozen `DES-APP-001_precommit.md`, then compares the reconstructed result with the preserved historical `DES-APP-001` result.

The result supports **deterministic record sufficiency and retraceability only**.
It is not blinded and not an independent replication.

---

## 2. Frozen artifact integrity / 동결 산출물 무결성

Artifact manifest used by the precommit:

```text
PROTOCOL
  methods/04_design/PROTOCOL_v0.1.md
  ref b3d658c839dfe60b65efbc44abf874e257d4a0e2

SOURCE PRECOMMIT
  evidence/method_specific/design/DES-APP-001_precommit.md
  ref 4847dbd1f5a38adb5d5c285b19ac41ebcfe86b96
  blob 9ca8f854e137397074253f167b247ee9aa2797cc

HISTORICAL RESULT
  evidence/method_specific/design/DES-APP-001_wcag22-submit-control-application.md
  ref 32a7842758be0cc179f996fdd8035d9683d31da9
  blob e13fe6a20812c748487086ee3e09194b8b56c376
```

The immutable refs and observed blob SHAs match the frozen manifest.
No historical artifact was edited during DES-CH-007.

### Non-blind procedural note

The historical result was already available to the same project/evaluator and was fetched before the retrace precommit in order to freeze its commit/blob identity.
Therefore this test does not claim cognitive blinding.

For the **reconstruction operation**, candidate facts and rules were taken from the frozen Protocol + source application precommit; the historical result served as the match target rather than as a substitute candidate rule table.
This is the operational meaning of the precommitted comparison discipline in a deliberately non-blinded same-project retrace.

---

## 3. Reconstructed task / 재구성 과업

Recovered from the frozen source precommit:

```text
CASE_ID: DES-APP-001
DESIGN_TASK_ID: DES-TASK-APP-001
PROTOCOL_VERSION: v0.1
CLAIMED_OUTPUT_LEVEL: DESIGN_SPACE
TARGET_DSD_LAYER_SCOPE:
  Formation
  General Property
CANDIDATE_COVERAGE:
  exhaustive relative only to DES-TASK-APP-001 fixture
DOMAIN_BRIDGE:
  WCAG_APPLICATION_BRIDGE_001
EXTERNAL_STANDARD:
  W3C WCAG 2.2 Recommendation 2024-12-12
SELECTED_SUCCESS_CRITERIA:
  SC 1.4.3
  SC 2.5.3
  SC 2.5.8
CANDIDATE_ORDER:
  W1-W10
```

Reconstructed checks:

```text
H0 submit_control is ADMITTED
H1 width >= 24 AND height >= 24 CSS px under frozen no-exception assumptions
H2 accessible name is defined AND contains visible label "Submit"
H3 contrast ratio >= 4.5:1 under frozen ordinary active non-logo text assumptions
```

No condition was added, deleted, weakened, or strengthened.
The SC 2.5.3 best-practice note about label position was not promoted into H2.
No full-WCAG-conformance claim was introduced.

---

## 4. Clean candidate re-execution / 후보 재실행

The following table is re-derived from the frozen candidate records and H0-H3.

| Candidate | Reconstructed rule application | Failure set | Retraced result |
|---|---|---|---|
| W1 | admitted; 24x24; name `Submit`; contrast 4.5 | none | admissible |
| W2 | admitted; 32x28; name `Submit order` contains `Submit`; contrast 7.0 | none | admissible |
| W3 | admitted; 24x24; name `Checkout Submit` contains `Submit`; contrast 4.5 | none | admissible |
| W4 | admitted; 23x24; valid name; contrast 7.0 | H1 | rejected |
| W5 | admitted; 24x23; valid name; contrast 7.0 | H1 | rejected |
| W6 | admitted; 24x24; `Send order` does not contain `Submit`; contrast 7.0 | H2 | rejected |
| W7 | admitted; 24x24; accessible name `APPLICABLE_BUT_UNDEFINED`; contrast 7.0 | H2 | rejected |
| W8 | admitted; 24x24; valid name; contrast 4.4 | H3 | rejected |
| W9 | admitted; 20x20; `Send order`; contrast 4.0 | H1,H2,H3 | rejected |
| W10 | `CHANNEL_ABSENCE`; control properties `INAPPLICABLE` | H0 | rejected |

Status-sensitive handling was preserved:

```text
W7:
  APPLICABLE_BUT_UNDEFINED
  != defined accessible name
  != CHANNEL_ABSENCE

W10:
  CHANNEL_ABSENCE
  -> H0 fail
  control properties remain INAPPLICABLE
  -> no zero-padding or fabricated defined values
```

Reconstructed family:

```text
{W1,W2,W3}
```

---

## 5. Reconstructed Design ledgers / 재구성 Design 장부

### Terminal Design status

The frozen candidate coverage is exhaustive only relative to the fixture, and at least W1-W3 satisfy all active checks.
For `DESIGN_SPACE`, the reconstructed result is therefore:

```text
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
```

### Protocol conformance

The frozen task record contains the task/claim, constraint sources, candidate basis and coverage, active DSD layers, external standard, explicit bridge, candidate records, external checks, output level, limits, and reproducibility information required for the claim-relevant re-execution.
No candidate-basis change, source substitution, status collapse, hidden Optimization, or unrecorded task revision is introduced by this retrace.

```text
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
```

### Method gain

DES-APP-001 contains no baseline comparison.
Under Protocol v0.1 this requires:

```text
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

---

## 6. Historical-result comparison / 과거 결과 비교

Comparison against the immutable historical result at commit `32a7842`:

```text
candidate verdicts:
  reconstructed == historical

rejection bases:
  reconstructed == historical

admissible family:
  reconstructed {W1,W2,W3}
  historical    {W1,W2,W3}

terminal status:
  reconstructed DESIGN_ADMISSIBLE
  historical    DESIGN_ADMISSIBLE

protocol conformance:
  reconstructed CONFORMANT
  historical    CONFORMANT

method gain:
  reconstructed NOT_ASSESSED
  historical    NOT_ASSESSED

external source/version:
  reconstructed W3C WCAG 2.2 Recommendation 2024-12-12
  historical    W3C WCAG 2.2 Recommendation 2024-12-12

bridge:
  reconstructed WCAG_APPLICATION_BRIDGE_001
  historical    WCAG_APPLICATION_BRIDGE_001
```

No claim-relevant mismatch was found.

---

## 7. Retrace-specific evidence ledger / 재추적 증거 장부

These are DES-CH-007 evidence-scoring fields, not additions to the Protocol v0.1 terminal-status vocabulary.

```text
RETRACE_ARTIFACT_INTEGRITY:          PASS
RETRACE_TASK_FIELD_MATCH:            PASS
RETRACE_EXTERNAL_SOURCE_MATCH:       PASS
RETRACE_BRIDGE_MATCH:                PASS
RETRACE_CANDIDATE_RECORD_MATCH:      PASS
RETRACE_CANDIDATE_VERDICT_MATCH:     PASS
RETRACE_REJECTION_BASIS_MATCH:       PASS
RETRACE_ADMISSIBLE_FAMILY_MATCH:     PASS
RETRACE_TERMINAL_STATUS_MATCH:       PASS
RETRACE_CONFORMANCE_MATCH:           PASS
RETRACE_GAIN_LEDGER_MATCH:           PASS
RETRACE_RESULT:                      PASS
```

---

## 8. Precommitted scoring / 사전 고정 점수

```text
ARTIFACT_AND_PROVENANCE_CHECKS:       8 / 8 PASS
TASK_SOURCE_BRIDGE_CHECKS:           11 / 11 PASS
CANDIDATE_RECORD_AND_VERDICT_CHECKS: 13 / 13 PASS
LEDGER_AND_COMPARISON_CHECKS:        12 / 12 PASS

PRECOMMITTED_REQUIRED_CHECKS: 44
PASSED: 44
FAILED: 0
CHALLENGE_VERDICT: PASS
```

No historical file was repaired or reclassified to obtain the pass.

---

## 9. Evidence verdict / 증거 판정

```text
CASE_ID: DES-CH-007
CASE_CLASS: reproducibility
CASE_ORIGIN: deterministic_retrace_of_preserved_DES-APP-001
PROTOCOL: v0.1
RETRACE_TARGET: DES-APP-001
RETRACE_RESULT: PASS
PRECOMMITTED_REQUIRED_CHECKS: 44
PASSED: 44
FAILED: 0
DIRECT_EVIDENCE_RESULT: PASS
DIRECT_CONSTRUCTED_PILOT_INCREMENT: +1
DEDICATED_RETRACE_PASS_INCREMENT: +1
```

This fills the dedicated Design `reproducibility/retrace` evidence category at the deterministic same-project level.

---

## 10. What this directly supports / 직접 지지 범위

At the declared record resolution, the preserved `DES-APP-001` precommit plus Protocol v0.1 contain enough information to reconstruct:

```text
active external source/version
selected success criteria
active bridge
candidate order and candidate facts
candidate-level verdicts and rejection bases
admissible family
terminal Design status
protocol conformance
method-gain status
```

and to match the preserved historical result exactly.

---

## 11. Limits / 한계

This PASS does **not** establish independent reproducibility.

The retrace remains:

```text
same project
same evaluator family
non-blinded
record-based
deterministic
```

The historical result was known to the evaluator and was fetched for immutable identity before the retrace precommit.
Accordingly, the result supports record sufficiency/retraceability, not independent reviewer agreement or blind replication.

It also does not establish:

```text
external evaluator agreement
cross-team replication
method superiority
method maturity
```

The next development step is a DSD Audit maturity review of the accumulated Design evidence, explicitly discounting common-evaluator dependence and preserving the absence of independent validation.
