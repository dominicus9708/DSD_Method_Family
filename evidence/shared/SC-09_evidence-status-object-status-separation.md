# SC-09 — Evidence-Status / DSD-Object-Status Separation / 증거상태·DSD 객체상태 분리 검증

Status: **promoted_with_conditions**  
Date: 2026-09-06  
Evidence scope: `shared_method_family`  
Case origin: `constructed_benchmark`

## 1. Result / 결과

`Evidence-Status / DSD-Object-Status Separation` is promoted as a **conditional shared-core rule**.

A representative method from each of the eight higher-level fields was tested against three status-axis perturbations:

- `EO`: evidence-to-object coercion — an evidential state such as insufficient evidence or out of audit scope is rewritten as a DSD object status such as applicable-but-undefined, inapplicable, absent, or zero;
- `OE`: object-to-evidence coercion — a DSD object status such as applicable-but-undefined, inapplicable, or defined-zero is treated as if it directly determined whether the claim is sufficiently supported, insufficiently supported, or outside audit scope;
- `CU`: coupled-update contamination — changing only the evidence package changes the DSD object status, or changing only the DSD object data automatically changes evidence status, without an explicit new source/model revision or evidence reassessment.

```text
EVIDENCE_TO_OBJECT_COERCION_CHECKS: 8/8 detected
OBJECT_TO_EVIDENCE_COERCION_CHECKS: 8/8 detected
COUPLED_UPDATE_CONTAMINATION_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
SHARED_CORE_PROMOTION_RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
```

Invariant meaning:

> Keep the status of the DSD object/model record separate from the status of the evidence supporting a claim about that object or its application. `undefined`, `inapplicable`, `defined_zero`, `channel_absent`, or a dynamic transition class are object-side states; `confirmed within scope`, `undetermined/insufficient`, and `out of scope` are evidence/audit-side states. One axis may constrain claims about the other, but the two axes are not identical and neither may be substituted for the other without an explicit rule.

## 2. Source basis / 소스 근거

### Property Axiom System

The current Property Axiom System explicitly distinguishes the following property-side statuses:

```text
undeclared
profile unavailable
inapplicable
prerequisite unsatisfied
applicable but undefined
defined
  -> defined zero / defined nonzero for zero-bearing kinds
```

These are derived from declaration, profile availability, applicability, dependency satisfaction, and assignment-domain membership. They are **object/model statuses**, not statements about how strong the auditor's evidence is.

### Formation / Static / Dynamics interfaces

Formation separately preserves undefined assignment, defined value/zero, channel absence, and admitted zero-bearing terms. Static Aggregation does not zero-pad undefined states into defined data. Dynamics preserves predecessor status distinctions required by a claim and treats status/domain transition as a structural event class rather than an evidence verdict.

### DSD General Audit

The current audit methodology separately records audit-evidence states:

```text
기술 가능 / 범위 내 확인
미정·불충분
범위 밖
```

The audit page explicitly states that these are **states of audit evidence**, not states of the DSD object itself, and instructs the object status to be kept in a separate ledger.

For this SC-09 pilot only, the three audit labels are normalized as:

```text
confirmed_within_scope
undetermined_or_insufficient
out_of_scope
```

This normalization is a record convenience, not a replacement of the canonical Korean audit wording.

## 3. Locked two-axis witnesses / 고정 2축 witness

Use one zero-bearing Property kind `q` over a fixed valid Formation background.

### Witness A — object undefined, evidence confirmed

```text
xU in Ap_q
xU in DepSat_q
xU not in Dom(Xi_q)

DSD_OBJECT_STATUS: applicable_but_undefined
EVIDENCE_STATUS: confirmed_within_scope
EVIDENCE_TARGET: the formal claim that xU has the above object status in the supplied model
```

There is no contradiction. The evidence may be sufficient to confirm that the **object status is undefined**.

### Witness B — object defined zero, application evidence insufficient

```text
x0 in Ap_q
x0 in DepSat_q
Xi_q(x0) = 0

DSD_OBJECT_STATUS: defined_zero
EVIDENCE_STATUS: undetermined_or_insufficient
EVIDENCE_TARGET: whether the supplied formal model instance is adequately supported as a claim about an external target
```

Again there is no contradiction. A formal model may contain a defined-zero object status while external evidence for applying that model to a real target remains insufficient.

### Witness C — same object status, different evidence status

Keep the same formal object record as Witness B while changing only the independent evidence package:

```text
C1: DSD_OBJECT_STATUS = defined_zero
    EVIDENCE_STATUS   = undetermined_or_insufficient

C2: DSD_OBJECT_STATUS = defined_zero
    EVIDENCE_STATUS   = confirmed_within_scope
```

A one-field generic `STATUS` cannot represent this difference without losing one axis.

## 4. Perturbations / 교란 연산

### EO — Evidence-to-object coercion

Invalid examples:

```text
undetermined_or_insufficient -> applicable_but_undefined
out_of_scope                 -> inapplicable
no observational support     -> channel_absent
insufficient evidence         -> defined_zero/false
```

The left side describes the auditor's epistemic/evidence position. The right side describes the model/object.

### OE — Object-to-evidence coercion

Invalid examples:

```text
applicable_but_undefined -> insufficient evidence
inapplicable             -> out of audit scope
defined_zero             -> sufficiently supported
channel_absent           -> claim contradicted
```

A model-internal status does not by itself establish the quality, authority, or completeness of the evidence for a claim about that model or its external application.

### CU — Coupled-update contamination

Hold object data fixed and improve only the evidence package:

```text
EVIDENCE_STATUS:
  undetermined_or_insufficient
  -> confirmed_within_scope
```

The object status must remain unchanged unless the object/model record itself is revised.

Conversely, hold the evidence package fixed and change the formal object data from a defined-zero record to an applicable-but-undefined record. Evidence status must be reassessed under the evidence rules; it does not automatically become `insufficient` merely because the object is now undefined.

## 5. Eight-field transfer test / 8개 상위 분야 교차 시험

| Field | Representative method | EO: evidence -> object | OE: object -> evidence | CU: coupled update | Result |
|---|---|---|---|---|---|
| I. Structural Description & Understanding | Analysis | lack of support is misdescribed as object undefinedness/absence | object undefinedness is mistaken for weak evidence | improved citations silently change the structural description without model revision | PASS: 3/3 detected |
| II. Criteria & Validation | Audit | `미정·불충분` is converted into `applicable_but_undefined` or absence | `defined_zero` is treated as audit confirmation | evidence update changes the audited object status instead of only the evidence ledger | PASS: 3/3 detected |
| III. Construction & Transformation | Synthesis | insufficient support for an input is treated as an undefined synthesized property | an undefined synthesized property is taken as evidence insufficiency | evidence package change mutates the synthesized object without a new construction record | PASS: 3/3 detected |
| IV. Evidence & Lineage | Measurement | low/insufficient evidence is rewritten as zero or absent measured object state | zero/undefined measurement object state is used as the confidence/evidence grade | calibration/evidence improvement changes the object state rather than the support assessment | PASS: 3/3 detected |
| V. Reduction & Representation | Compression | evidence status is encoded into object-status slot | object status is encoded into evidence-status slot | one generic status field loses pairs such as `defined_zero + insufficient` versus `defined_zero + confirmed` | PASS: 3/3 detected |
| VI. Inverse Inference & Reconstruction | Diagnosis | insufficient diagnostic evidence is converted into `undefined` hidden state | hidden-state undefinedness is treated as proof of evidence insufficiency | new evidence changes the hidden-state record without an explicit diagnostic/model update | PASS: 3/3 detected |
| VII. Computation & Selection | Computation | evidence grade is used as the branch condition for DSD object semantics | object status is used as if it were validation/confidence score | cache/state logic changes object output when only evidence metadata changes | PASS: 3/3 detected |
| VIII. Dynamics & Action | Simulation | weak empirical support is rewritten as a dynamic status/domain transition | simulated transition class is treated as evidence that the model is empirically supported | validation evidence changes simulated state history without a new model/input revision | PASS: 3/3 detected |

This tests transfer of the separation rule only. It does not directly validate the eight representative methods as complete methodologies.

## 6. Negative controls / 음성 대조군

SC-09 permits legitimate relations between the two axes.

1. `DSD_OBJECT_STATUS: applicable_but_undefined` together with `EVIDENCE_STATUS: confirmed_within_scope` is valid when the evidence fully establishes that the supplied object/model is applicable, prerequisite-satisfied, and outside the assignment domain.
2. `DSD_OBJECT_STATUS: defined_zero` together with `EVIDENCE_STATUS: undetermined_or_insufficient` is valid when the formal model contains a zero assignment but the evidence connecting the model to an external target is incomplete.
3. Evidence can support, contradict, or leave unresolved a **proposition about** object status. The evidential predicate is applied to the proposition; it is not identical to the object status named inside the proposition.
4. Purely formal single-model work that makes no evidence/audit claim may record only object status; the full evidence ledger is then not applicable.
5. Pure evidence/provenance work about a target that has no DSD object model may use evidence status without inventing a DSD object status.

Therefore SC-09 is not “the two axes never interact.” It is:

> **Interaction requires an explicit claim/evidence relation; category substitution is forbidden.**

## 7. Standard two-axis status record / 표준 2축 상태 기록

```text
STATUS_RECORD_ID:
TARGET_CLAIM:

DSD_OBJECT_LAYER: Formation / Property / Dynamics / none
DSD_OBJECT_ID:
DSD_OBJECT_STATUS:
DSD_OBJECT_STATUS_BASIS:

EVIDENCE_STATUS:
EVIDENCE_STATUS_VOCABULARY:
EVIDENCE_BASIS:
EVIDENCE_SCOPE:
EVIDENCE_SOURCE_RECORDS:

CLAIM_ABOUT_OBJECT_STATUS:
CLAIM_STATUS_RELATION:
  evidence_assesses_claim_about_object / none
OBJECT_STATUS_CHANGED_THIS_REVISION: yes / no
EVIDENCE_STATUS_CHANGED_THIS_REVISION: yes / no
CHANGE_BASIS:
CROSS_AXIS_AUTOMATIC_COERCION: prohibited
```

## 8. Promotion test / 승격 시험

```text
SOURCE_SUPPORT: pass
SAME_SEMANTIC_MEANING_ACROSS_METHODS: pass
EVIDENCE_TO_OBJECT_COERCION_COUNTEREXAMPLE: pass
OBJECT_TO_EVIDENCE_COERCION_COUNTEREXAMPLE: pass
COUPLED_UPDATE_CONTAMINATION_COUNTEREXAMPLE: pass
NON_TRANSFER_CASE_IDENTIFIED: pass
METHOD_TASK_REDEFINITION: none
DIRECT_VALIDATION_SEPARATION: pass
SHARED_CORE_PROMOTION_RESULT: promoted_with_conditions
```

## 9. Transfer conditions / 적용 조건

Apply SC-09 when a record contains both:

- a DSD object/model status or transition class; and
- an audit, evidence, confidence, verification, support, or source-sufficiency judgment about a claim involving that object or its external application.

The rule is especially important when `undefined`, `inapplicable`, `absent`, or `zero` could be confused with `unknown`, `unsupported`, `unverified`, or `outside scope`.

## 10. Non-transfer / minimal-record cases / 적용하지 않거나 단순화하는 경우

- A purely formal object record with no evidential claim need not invent an evidence status.
- A pure source-verification record without a DSD object model need not invent a DSD object status.
- A domain may use a richer evidence vocabulary than the three current audit states; SC-09 requires axis separation, not one universal evidence ontology.
- An explicit model-update rule may let new evidence trigger a new object/model revision, but the transition must be recorded as a revision/update rather than an automatic reinterpretation of the old object status.

## 11. Evidence limits / 한계

- This is a constructed cross-field status-separation pilot.
- Property-side status semantics are source-supported by the current Property Axiom System; Formation/Static/Dynamics provide compatible status-preservation examples.
- Evidence-side status semantics are supported by the current DSD General Audit methodology and automation roadmap.
- One representative method per higher-level field was tested.
- The English evidence-status labels used here are normalized pilot labels for the existing Korean audit vocabulary, not a new foundational DSD axiom.
- This does not directly validate the overall correctness, performance, or usefulness of all 22 methods.

## 12. Relation to SC-01–SC-08 / SC-01~08과의 관계

```text
SC-01 = distinguish statuses inside the selected DSD object/interface
SC-02 = lock the source/interface/version defining those statuses
SC-03 = make cross-structure mappings explicit
SC-04 = use only claim-relevant DSD layers as dependencies
SC-05 = respect information-loss/reconstruction limits
SC-06 = separate regular evolution, transition, and lineage
SC-07 = separate evidence applicability from case origin
SC-08 = preserve evaluation integrity
SC-09 = separate evidence status from DSD object status
```

SC-09 is not redundant with SC-01. SC-01 protects distinctions **within the DSD object/status space**; SC-09 protects the boundary **between that object/status space and the evidence/audit status space**.

## 13. Next step / 다음 단계

Run the **specialization-restraint separation/duplication audit**. The purpose is to decide whether specialization restraint has enough independent semantic content to become a separate shared-core record, or whether it is already fully covered by SC-01 and SC-04. Do not create `SC-10` unless that independence test passes.
