# DES-CH-007 — DES-APP-001 Deterministic Retrace Precommit

Status: **PRECOMMITTED BEFORE RETRACE SCORING**  
Date: **2026-09-08**  
Evidence scope: `method_specific`  
Method directly tested: **DSD Design / DSD 설계론**  
Method protocol: **DSD Design Protocol v0.1**  
Case class: **reproducibility**

## 1. Purpose / 목적

Run the first dedicated reproducibility/retrace test for DSD Design.

The target of the retrace is the completed external-standard application `DES-APP-001`.
The retrace asks whether a clean deterministic re-execution from the preserved protocol and frozen application precommit reproduces the claim-relevant candidate verdicts, admissible family, terminal status, protocol-conformance status, method-gain status, external-source identity, and active bridge without editing the historical application.

This is **not** an independent replication and is not blinded: the same project/evaluator has access to the historical result. The evidence claim is therefore limited to deterministic record sufficiency and retraceability.

---

## 2. Frozen artifact manifest / 동결 산출물 목록

The retrace is anchored to immutable Git commit references.

```text
A. DESIGN_PROTOCOL
path:
  methods/04_design/PROTOCOL_v0.1.md
ref:
  b3d658c839dfe60b65efbc44abf874e257d4a0e2

B. SOURCE_APPLICATION_PRECOMMIT
path:
  evidence/method_specific/design/DES-APP-001_precommit.md
ref:
  4847dbd1f5a38adb5d5c285b19ac41ebcfe86b96
blob_sha_observed_before_retrace:
  9ca8f854e137397074253f167b247ee9aa2797cc

C. HISTORICAL_RESULT_FOR_POST_REEXECUTION_COMPARISON
path:
  evidence/method_specific/design/DES-APP-001_wcag22-submit-control-application.md
ref:
  32a7842758be0cc179f996fdd8035d9683d31da9
blob_sha_observed_before_retrace:
  e13fe6a20812c748487086ee3e09194b8b56c376
```

No historical artifact may be edited as part of DES-CH-007.

---

## 3. Retrace input discipline / 재추적 입력 규율

The reconstruction basis is:

```text
PROTOCOL_v0.1 at frozen ref
+
DES-APP-001_precommit at frozen ref
```

The historical `DES-APP-001` result is used only as the comparison target after reconstruction.

No Notion summary, current-method README, chat summary, or later project note is an authoritative reconstruction input for this case.
If such material differs from the frozen Git artifacts, the frozen Git artifacts control the retrace.

The same evaluator already knows the historical result, so this procedure cannot establish evaluator independence or blind replication.

---

## 4. Frozen fields that must be reconstructed / 재구성 필드

From the source application precommit, reconstruct exactly:

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

Reconstruct the task-local/external checks exactly:

```text
H0 submit_control is ADMITTED
H1 width >= 24 AND height >= 24 CSS px under frozen no-exception assumptions
H2 accessible name is defined AND contains visible label "Submit"
H3 contrast ratio >= 4.5:1 under frozen ordinary active non-logo text assumptions
```

---

## 5. Frozen reconstructed candidate verdict target / 동결 재구성 목표

The clean re-execution must independently apply H0-H3 to the frozen candidate records and produce:

```text
W1  -> admissible
W2  -> admissible
W3  -> admissible
W4  -> rejected {H1}
W5  -> rejected {H1}
W6  -> rejected {H2}
W7  -> rejected {H2}
W8  -> rejected {H3}
W9  -> rejected {H1,H2,H3}
W10 -> rejected {H0}; control properties remain INAPPLICABLE
```

Expected reconstructed family:

```text
{W1,W2,W3}
```

Expected Design ledgers:

```text
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

These are frozen as the required match target before scoring the retrace.

---

## 6. Retrace-specific evidence ledger / 재추적 증거 장부

The following fields are **DES-CH-007 evidence-scoring fields**, not new Protocol v0.1 terminal statuses:

```text
RETRACE_ARTIFACT_INTEGRITY:
  PASS / FAIL

RETRACE_TASK_FIELD_MATCH:
  PASS / FAIL

RETRACE_EXTERNAL_SOURCE_MATCH:
  PASS / FAIL

RETRACE_BRIDGE_MATCH:
  PASS / FAIL

RETRACE_CANDIDATE_RECORD_MATCH:
  PASS / FAIL

RETRACE_CANDIDATE_VERDICT_MATCH:
  PASS / FAIL

RETRACE_REJECTION_BASIS_MATCH:
  PASS / FAIL

RETRACE_ADMISSIBLE_FAMILY_MATCH:
  PASS / FAIL

RETRACE_TERMINAL_STATUS_MATCH:
  PASS / FAIL

RETRACE_CONFORMANCE_MATCH:
  PASS / FAIL

RETRACE_GAIN_LEDGER_MATCH:
  PASS / FAIL

RETRACE_RESULT:
  PASS / FAIL
```

`RETRACE_RESULT=PASS` requires every preceding retrace field to be `PASS`.

---

## 7. Precommitted required checks / 사전 고정 검사

### Artifact and provenance checks

1. Protocol path and frozen protocol ref are recorded exactly.
2. Source application precommit path/ref are recorded exactly.
3. Historical result path/ref are recorded exactly.
4. Source precommit blob SHA matches `9ca8f854e137397074253f167b247ee9aa2797cc`.
5. Historical result blob SHA matches `e13fe6a20812c748487086ee3e09194b8b56c376`.
6. No historical source/result artifact is edited by DES-CH-007.
7. Reconstruction authority is limited to frozen Protocol + frozen source precommit.
8. Historical result is treated as post-reconstruction comparison target rather than a replacement for candidate re-evaluation.

### Task/source/bridge reconstruction checks

9. `DESIGN_TASK_ID = DES-TASK-APP-001` is reconstructed.
10. `CLAIMED_OUTPUT_LEVEL = DESIGN_SPACE` is reconstructed.
11. DSD layers Formation + General Property are reconstructed.
12. candidate coverage is reconstructed as exhaustive relative only to the frozen fixture.
13. external authority/version is reconstructed as W3C WCAG 2.2 Recommendation 2024-12-12.
14. selected criteria are exactly SC 1.4.3, 2.5.3, and 2.5.8.
15. bridge ID `WCAG_APPLICATION_BRIDGE_001` is reconstructed.
16. H0-H3 are reconstructed without adding or deleting a condition.
17. frozen no-exception target-size assumption is preserved.
18. the SC 2.5.3 best-practice note is not promoted into H2.
19. no full-WCAG-conformance claim is introduced.

### Candidate-record and verdict checks

20. Candidate order is exactly W1-W10.
21. All W1-W10 source candidate records are recoverable from the frozen precommit.
22. W1 reconstructs as admissible.
23. W2 reconstructs as admissible.
24. W3 reconstructs as admissible.
25. W4 reconstructs with failure set exactly {H1}.
26. W5 reconstructs with failure set exactly {H1}.
27. W6 reconstructs with failure set exactly {H2}.
28. W7 reconstructs with failure set exactly {H2} and preserves `APPLICABLE_BUT_UNDEFINED`.
29. W8 reconstructs with failure set exactly {H3}.
30. W9 reconstructs with failure set exactly {H1,H2,H3}.
31. W10 reconstructs with failure set exactly {H0}, `CHANNEL_ABSENCE`, and INAPPLICABLE control properties.
32. reconstructed admissible family is exactly {W1,W2,W3}.

### Ledger and comparison checks

33. reconstructed terminal Design status is `DESIGN_ADMISSIBLE`.
34. reconstructed protocol conformance is `CONFORMANT`.
35. reconstructed method-gain status is `NOT_ASSESSED`.
36. reconstructed candidate verdicts match the historical result exactly.
37. reconstructed rejection bases match the historical result exactly.
38. reconstructed admissible family matches the historical result exactly.
39. reconstructed three Design ledgers match the historical result exactly.
40. external source/version and bridge match the historical result exactly.
41. all retrace-specific evidence fields are scored separately from Protocol v0.1 terminal Design statuses.
42. common-evaluator/same-project dependence is explicitly preserved as a limitation.
43. no independent-replication claim is made.
44. no method-maturity claim is made from this retrace alone.

```text
PRECOMMITTED_REQUIRED_CHECKS: 44
```

Any mismatch remains a failure in the executed record.
No historical record may be repaired to make the retrace pass.

---

## 8. Evidence-count rule / 증거 수 규칙

Once executed after this precommit, `DES-CH-007` counts as one direct constructed Design challenge in the `reproducibility` class regardless of outcome.

A successful result may fill the dedicated Design reproducibility/retrace evidence category at the deterministic same-project level.
It does not establish independent evaluator validation or external replication.

---

## 9. Frozen limitations / 동결 한계

Even a perfect retrace remains:

```text
same project
same evaluator family
non-blinded
record-based
deterministic rather than independently replicated
```

The strongest claim available from a PASS is that the frozen Design record contains enough declared information for deterministic claim-relevant re-execution and exact comparison at the recorded resolution.
