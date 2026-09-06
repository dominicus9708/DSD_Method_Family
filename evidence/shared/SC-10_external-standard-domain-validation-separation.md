# SC-10 — External-Standard / Domain-Validation Separation / 외부 기준·도메인 검증 분리

Status: **promoted_with_conditions**  
Date: 2026-09-06  
Evidence scope: `shared_method_family`  
Case origin: `constructed_benchmark`

## 1. Result / 결과

`External-Standard / Domain-Validation Separation` is promoted as a **conditional shared-core rule**.

The closure-gap audit found that SC-01 through SC-09 can all be satisfied while a downstream record still overclaims that a DSD-internal structural result has replaced the receiving domain's own proof, empirical, professional, interpretive, legal, ethical, or safety validation standard.

A representative method from each of the eight higher-level fields was therefore tested against three perturbations:

- `SO`: standard omission — retain an external-domain claim but remove the domain-specific validation standard;
- `DS`: DSD-to-domain substitution — treat DSD structural fit, correspondence, audit consistency, or model-internal success as if it were the receiving domain's validation result;
- `WS`: wrong-standard substitution — replace the locked task-relevant external standard with a weaker or unrelated standard while preserving the same downstream claim.

```text
STANDARD_OMISSION_CHECKS: 8/8 detected
DSD_TO_DOMAIN_SUBSTITUTION_CHECKS: 8/8 detected
WRONG_STANDARD_SUBSTITUTION_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
SHARED_CORE_PROMOTION_RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
```

Invariant meaning:

> A DSD method may structure, compare, audit, transform, compress, infer, compute, or simulate information relevant to an external domain, but a DSD-internal result does not by itself replace the receiving domain's own validation or authority standard. When the claimed output is a domain-level conclusion, the applicable external standard and the bridge from DSD output to that standard must remain explicit.

## 2. Source basis / 소스 근거

The current `DSD_METHOD_FAMILY_FRAMEWORK.md` states the domain-bridge rule directly:

```text
DSD structural layer
+ selected independent method(s)
+ explicit domain bridge
+ domain-specific standard
-> method-specific result(s)
```

It also states that DSD does not replace a field's proof, validation, interpretation, professional, empirical, ethical, or safety standards.

The current method boundary audit independently preserves method-specific `VALIDATION_STANDARD` as one of the five axes that keep the 22 methods distinct. In particular, Simulation and Prediction are separated because model-consistent trajectory generation is not yet validation of a future external target; Prediction requires appropriate empirical/domain validation.

This SC-10 rule is therefore supported by a domain-independent operating requirement already present in the method-family framework rather than by a claim that the four DSD source papers themselves define every external discipline's validation standard.

## 3. Locked benchmark / 고정 벤치마크

Use a generic two-stage record:

```text
DSD_RESULT:
  a structurally valid method-specific output under locked DSD interfaces

DOMAIN_CLAIM:
  a stronger conclusion about an external mathematical, empirical,
  historical, legal, organizational, engineering, or predictive target

DOMAIN_BRIDGE:
  explicit and typed

EXTERNAL_STANDARD:
  task-relevant domain standard required for DOMAIN_CLAIM
```

The benchmark intentionally allows the DSD result and bridge to be internally valid. The perturbation occurs only at the **validation-standard boundary**.

This makes SC-10 non-duplicative with SC-03: a bridge can be explicit and well typed while the receiving domain's validation requirement is still omitted or replaced.

## 4. Perturbations / 교란 연산

### SO — Standard omission

Delete `EXTERNAL_STANDARD` while retaining the same external-domain claim.

Expected result: the DSD output may remain valid at its own layer, but the stronger domain claim becomes unsupported or under-validated.

### DS — DSD-to-domain substitution

Replace the external-domain validation step with one of the following:

```text
DSD structural correspondence
DSD audit consistency
DSD aggregate fit
DSD simulation consistency
DSD internal PASS
```

and treat that internal result as the domain verdict itself.

Expected result: reject the substitution unless the receiving domain has independently established equivalence between the two standards for the declared claim.

### WS — Wrong-standard substitution

Keep an external standard field but replace the task-relevant standard with a weaker, unrelated, or merely convenient criterion.

Expected result: detect that the claim is being validated under the wrong authority/criterion.

## 5. Eight-field transfer test / 8개 상위 분야 교차 시험

| Field | Representative method | SO | DS | WS | Result |
|---|---|---|---|---|---|
| I. Structural Description & Understanding | Interpretation | external reading claimed with no source/domain interpretive standard | DSD structural reading treated as authoritative interpretation by itself | unrelated interpretive criterion substituted | PASS: 3/3 detected |
| II. Criteria & Validation | Audit | compliance/domain verdict retained after removing relevant standard | DSD audit consistency substituted for the audited domain's governing standard | weaker/non-governing standard substituted | PASS: 3/3 detected |
| III. Construction & Transformation | Design | external design adequacy claimed without engineering/task acceptance standard | DSD structural coherence treated as sufficient external design validation | non-task acceptance criterion substituted | PASS: 3/3 detected |
| IV. Evidence & Lineage | Provenance | historical/source-origin conclusion strengthened without source-authority standard | DSD provenance chain treated as source authenticity/authority by itself | weaker source criterion substituted | PASS: 3/3 detected |
| V. Reduction & Representation | Compression | downstream adequacy claimed without the receiving task's preservation/error standard | DSD-internal retention claim treated as sufficient domain adequacy | unrelated compression-quality criterion substituted | PASS: 3/3 detected |
| VI. Inverse Inference & Reconstruction | Diagnosis | real-domain diagnosis asserted without domain evidence/diagnostic standard | DSD-compatible hidden state treated as confirmed real diagnosis | weaker diagnostic rule substituted | PASS: 3/3 detected |
| VII. Computation & Selection | Optimization | practical superiority claimed without task-relevant objective/acceptance standard | DSD optimization result treated as external utility proof by itself | convenient but wrong objective/standard substituted | PASS: 3/3 detected |
| VIII. Dynamics & Action | Prediction | future external prediction asserted without empirical/domain scoring standard | simulation/model consistency treated as predictive validation | weaker or unrelated forecast criterion substituted | PASS: 3/3 detected |

This is a shared-rule transfer test. It is not direct validation of the eight selected methods as complete methodologies.

## 6. Negative control / 음성 대조군

SC-10 does **not** require an external standard for every internal DSD statement.

The rule is inactive or minimally satisfied when:

1. the claim is explicitly confined to DSD-internal structure, such as a formation/property status or a model-consistent simulation trajectory, and no external-domain truth/authority claim is made;
2. the receiving domain's relevant standard is already part of the locked task record and is applied separately from the DSD result;
3. a documented theorem, calibration result, institutional rule, or other legitimate basis establishes equivalence between the DSD-side criterion and the external standard over the declared claim class;
4. DSD is used only to organize evidence or expose assumptions while the actual domain verdict remains assigned to the domain standard.

Thus SC-10 is not "DSD can never contribute to a domain conclusion." It is:

> **Do not silently replace the receiving domain's validation standard with DSD-internal structural success.**

## 7. Boundary against neighboring shared rules / 인접 규율과의 경계

```text
SC-03:
  asks whether the mapping/bridge from one carrier or domain to another is explicit and justified.

SC-10:
  asks whether the receiving domain's validation/authority standard is still applied after that bridge exists.

SC-07:
  asks what the evidence record directly validates and what kind of case produced it.

SC-10:
  asks what standard is competent to validate the external-domain claim.

SC-08:
  asks whether comparative/confirmatory evaluation uses a competent baseline,
  preserves unfavorable results, and avoids post-hoc rescue.

SC-10:
  applies even when no comparative baseline is relevant, because a domain claim
  may still require a domain-specific proof, authority, or empirical standard.
```

Counterexample to duplication:

```text
bridge explicit                 -> SC-03 satisfied
case-origin/scope recorded      -> SC-07 satisfied
no comparative claim            -> SC-08 baseline clause inactive
object/evidence status separate -> SC-09 satisfied
external domain standard omitted
strong domain claim retained
```

The record still fails SC-10. Therefore SC-10 has a unique failure criterion.

## 8. Standard record / 표준 기록

```text
DOMAIN_VALIDATION_RECORD_ID:
DSD_METHOD_OUTPUT:
DOMAIN_CLAIM:
DOMAIN_BRIDGE:
EXTERNAL_DOMAIN:
EXTERNAL_STANDARD:
STANDARD_SOURCE_OR_AUTHORITY:
STANDARD_APPLICABILITY:
DSD_INTERNAL_VALIDATION_RESULT:
DOMAIN_VALIDATION_RESULT:
EQUIVALENCE_TO_DSD_CRITERION_IF_CLAIMED:
OVERCLAIM_CHECK:
LIMITS:
```

## 9. Promotion test / 승격 시험

```text
SOURCE_SUPPORT: pass
SAME_SEMANTIC_MEANING_ACROSS_METHODS: pass
STANDARD_OMISSION_COUNTEREXAMPLE: pass
DSD_TO_DOMAIN_SUBSTITUTION_COUNTEREXAMPLE: pass
WRONG_STANDARD_SUBSTITUTION_COUNTEREXAMPLE: pass
NON_TRANSFER_CASE_IDENTIFIED: pass
METHOD_TASK_REDEFINITION: none
DIRECT_VALIDATION_SEPARATION: pass
UNIQUE_FAILURE_CRITERION_VS_SC01_09: pass
SHARED_CORE_PROMOTION_RESULT: promoted_with_conditions
```

## 10. Evidence limits / 한계

- This is a constructed cross-field transfer pilot.
- One representative method per higher-level field was tested.
- The benchmark checks the separation rule, not the correctness of any particular mathematical, medical, legal, historical, engineering, or empirical external standard.
- No claim is made that DSD defines or replaces those external standards.
- Promotion of SC-10 does not directly validate all 22 methods.

## 11. Closure consequence / 종료감사에 미치는 영향

SC-10 closes the only stable semantic/operational gap found by the current shared-core closure sweep.

`REPRODUCIBILITY_RECORD` remains mandatory in the method/evidence maturity architecture, but its concrete validation obligation differs materially by method (for example executable rerun, deterministic/seeded computation, source-and-step retraceability, or interpretive audit trail). It is therefore retained as a **method/evidence maturity requirement**, not promoted as another DSD shared semantic rule in this closure version.
