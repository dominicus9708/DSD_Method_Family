# DSD Method Family Framework / DSD 방법군 공통 프레임

Status: working framework
Framework date: 2026-09-06

This document organizes the DSD Method Family derived from the Formation Axiom System, General Property Axiom System, Channel-Indexed Static Aggregation, Structural Reorganization Dynamics, and explicit optional specializations.

이 문서는 형성공리계, 속성공리계, 채널별 정적 집계, 구조 재구성 동역학 및 명시적 선택 특수화에서 파생되는 DSD 사용 방식을 공통 방법군으로 정리합니다.

## 1. Preservation rule / 기존 구조 보존 원칙

- Existing DSD Analysis and DSD Audit records remain valid historical and operational records.
- Existing `DSD_Audit/`, `audits/`, `challenges/`, `methodology/`, `protocols/`, and `templates/` paths are preserved.
- New classification material is additive under `methods/fields/`.
- Historical paths are not silently rewritten when a method is refined or reclassified.
- Earlier compound 09/10/12/15 paths are retained only for compatibility and are not counted as current methods.

## 2. Shared DSD source layers / 공통 DSD 기반 층위

A method uses only the layers required by its task.

1. **Formation** — admission, restriction, realization, partial assignment, operational-channel formation, finite composition interface.
2. **General Property** — typed profiles, applicability, contextual prerequisites, partial property assignments, status distinctions.
3. **Static Aggregation** — channel-indexed analytic realization, finite aggregation, optional typed-property aggregation, information-loss and reconstruction conditions.
4. **Dynamics** — component-resolved trajectories, regular epochs, transition classes, lineage, dynamic bridges.
5. **Optional specializations** — realized-axis geometry or any additional domain-specific structure supplied explicitly.

The current paper-facing interface lock remains in `DSD_INTERFACE_PROFILE.md`.

## 3. Current method architecture / 현재 방법 구조

The current conceptual architecture is:

```text
DSD foundational layers
-> 8 higher-level method fields
-> 22 independent methods
-> explicit cross-method application cases
```

The higher-level fields are organizational categories only. They do not merge member methods, inherit results across methods, or create a new method merely by grouping names together.

현재 개념적 정본은 **8개 상위 분야 / 22개 독립 방법**입니다. 상위 분야는 분류·탐색·연구관리용이며, 소속 방법의 입력·연산·산출물·실패 조건·검증기준을 합치지 않습니다.

## 4. Eight higher-level fields / 8개 상위 분야

### I. Structural Description & Understanding / 구조 기술·이해
- Analysis / DSD 분석론
- Comparison / DSD 비교론
- Classification / DSD 분류론
- Interpretation / DSD 해석론

### II. Criteria & Validation / 기준·검증
- Specification / DSD 명세론
- Audit / DSD 감사

### III. Construction & Transformation / 구성·변환
- Design / DSD 설계론
- Synthesis / DSD 합성론
- Transformation / DSD 변환론

### IV. Evidence & Lineage / 증거·계보
- Measurement / DSD 측정론
- Provenance / DSD 출처·유래 추적론
- Lineage / DSD 계보론

### V. Reduction & Representation / 축약·표현
- Aggregation / DSD 집계론
- Compression / DSD 압축론

### VI. Inverse Inference & Reconstruction / 역추론·복원
- Diagnosis / DSD 진단론
- Reconstruction / DSD 복원론

### VII. Computation & Selection / 계산·선택
- Computation / DSD 계산론
- Optimization / DSD 최적화론

### VIII. Dynamics & Action / 동역학·행동
- Simulation / DSD 시뮬레이션론
- Prediction / DSD 예측론
- Control / DSD 제어론
- Operation / DSD 운영론

Total: **22 independent methods**.

## 5. Independence rule / 방법 독립성 규칙

Two methods remain distinct when their task interfaces differ materially in any of the following:

```text
INPUTS
OPERATION
OUTPUTS
FAILURE_OR_NO_GAIN_CRITERIA
VALIDATION_STANDARD
```

The current full boundary audit is maintained at [`../methods/METHOD_BOUNDARY_MATRIX.md`](../methods/METHOD_BOUNDARY_MATRIX.md).

Current result:

```text
EXACT_DUPLICATE_METHODS_FOUND: 0
METHOD_COUNT: 22
```

Important distinctions include:

- **Analysis ≠ Comparison ≠ Classification ≠ Interpretation**: Analysis decomposes and structurally re-expresses one declared target; Comparison judges cross-target preserved/differing structure; Classification assigns classes under explicit criteria; Interpretation separates source, context, interpretive assumptions, and bridge-supported readings.
- **Provenance ≠ Lineage**: provenance records origin/derivation; lineage records predecessor-successor identity across change.
- **Aggregation ≠ Compression**: aggregation constructs a readout or representative value; compression intentionally removes representation subject to retained-distinction requirements.
- **Computation ≠ Optimization**: computation determines required evaluation; optimization selects among admissible alternatives under explicit objectives and constraints.
- **Diagnosis ≠ Reconstruction**: diagnosis infers present hidden states or causes; reconstruction infers prior, omitted, damaged, or compressed structures or histories.
- **Simulation ≠ Prediction**: simulation evolves model-consistent states; prediction makes a claim about a future target and requires appropriate empirical/domain validation.
- **Control ≠ Operation**: control chooses interventions; operation manages repeated lifecycle, resources, monitoring, execution, and handoff.
- **Specification ≠ Audit**: specification declares requirements or criteria; audit evaluates compliance, evidence, procedure, and structural consistency against relevant standards.

A field classification or a shared operator never licenses inference from one method result to another without an explicit bridge.

Historical DSD Analysis records may contain comparison, classification, or interpretation operations together with analysis. Those records are preserved; new method-family records identify method-specific outputs separately.

## 6. Common method record / 공통 방법 기록 형식

Every method definition should state at least:

```text
METHOD_NAME:
HIGHER_FIELD:
STATUS: established / developing / proposed / experimental
TASK:
INPUTS:
DSD_LAYERS_USED:
DOMAIN_BRIDGE:
EXTERNAL_STANDARD:
OPERATION:
OUTPUTS:
FAILURE_OR_NO_GAIN_CRITERIA:
INFORMATION_LOSS_CHECK:
LINEAGE_OR_TRANSITION_CHECK:
LIMITS:
REPRODUCIBILITY_RECORD:
```

Numeric or A/B labels may be retained in paths for historical compatibility, but the method name and field are the conceptual identifiers.

## 7. Domain-bridge rule / 분야별 브리지 원칙

DSD does not replace a field's own proof, validation, interpretation, professional, empirical, ethical, or safety standards.

A domain application therefore has the form:

```text
DSD structural layer
+ selected independent method(s)
+ explicit domain bridge
+ domain-specific standard
-> method-specific result(s)
```

A mathematical proof remains mathematical proof; a medical judgment remains subject to medical evidence and clinical standards; a historical interpretation remains subject to source criticism; an artistic interpretation is not reduced to a scalar aggregate merely because selected features can be encoded.

This boundary is now separately cross-field tested as **SC-10 External-Standard / Domain-Validation Separation**. An explicit domain bridge and a DSD-internal PASS are not by themselves substitutes for the receiving domain's competent validation standard.

## 8. Status and bridge discipline / 상태·브리지 규율

Across the method family:

- preserve absence, undefinedness, inapplicability, prerequisite failure, and defined zero when the selected interface distinguishes them;
- do not infer cross-layer mappings from terminology alone;
- do not infer structural identity from aggregate equality without reconstruction conditions;
- preserve failed mappings, alternative mappings, and `NO_GAIN` results;
- when dynamics is used, distinguish value evolution from status/domain and formation-level transitions;
- use explicit lineage when successor identity is not inherited automatically;
- do not treat membership in the same higher-level field or reuse of the same DSD operator as evidence of method equivalence;
- do not replace a receiving domain's validation standard with DSD-internal structural success.

## 9. Method composition / 방법 조합

The methods are composable but not a mandatory pipeline. Typical combinations include:

```text
Specification -> Design -> Synthesis -> Audit
Analysis -> Comparison -> Classification
Measurement -> Provenance -> Lineage
Aggregation -> Compression
Diagnosis -> Reconstruction
Computation -> Optimization
Simulation -> Prediction -> Control -> Operation
Interpretation -> Comparison -> Audit
```

A case may combine methods from several fields, but each intermediate and final result should remain attributable to the method that produced it.

## 10. Legacy compatibility / 기존 복합 경로 호환성

The following directories remain as historical navigation wrappers only:

- `09_provenance_lineage/` → Provenance + Lineage
- `10_aggregation_compression/` → Aggregation + Compression
- `12_computation_optimization/` → Computation + Optimization
- `15_diagnosis_reconstruction/` → Diagnosis + Reconstruction

These wrapper names are not current method names and are not included in the count of 22 methods.

## 11. Development policy / 개발 정책

- Analysis and Audit are the two most mature current methods and retain their established corpora.
- Comparison, Provenance, Lineage, and Aggregation have comparatively direct support in current DSD formal structures but still require dedicated method-level protocols.
- Proposed methods should be promoted only after concrete protocols, counterexamples, boundary cases, `NO_GAIN` cases, reproducibility records, and cross-domain tests accumulate.
- Similarity to an existing external methodology is not novelty by itself.
- The intended contribution is a shared DSD structural layer plus explicitly separable method roles and cross-method interoperability, not a claim to replace all disciplinary methods.

## 12. Evidence applicability and case-origin separation / 증거 적용성·사례 출처 분리

Evidence scope and case origin are separate dimensions.

### 12.1 Shared method-family evidence

Shared evidence supports reusable operating disciplines. The current promoted registry is **SC-01 through SC-10**.

It does **not** directly validate all 22 methods.

```text
EVIDENCE_SCOPE_CLASS: shared_method_family
SHARED_RULES_SUPPORTED:
SOURCE_RECORDS:
METHODS_DIRECTLY_TESTED:
METHODS_NOT_DIRECTLY_VALIDATED:
TRANSFER_LIMIT:
```

The specialization-restraint pattern is retained as a derived profile over SC-01/03/04 rather than a separate shared-core ID.

### 12.2 Method-specific evidence

A method-specific record directly tests one independent method under that method's own task, inputs, operation, outputs, failure conditions, and validation criteria.

```text
EVIDENCE_SCOPE_CLASS: method_specific
METHOD_DIRECTLY_TESTED:
METHOD_VERSION_OR_PROTOCOL:
RESULT:
REPRODUCIBILITY_RECORD:
```

`ANL-CH-*` records remain direct evidence for DSD Analysis. `DSD_Audit/` and new audit records remain direct evidence for DSD Audit. Other methods may reuse shared disciplines but are not directly validated by those corpora.

### 12.3 Real-world application evidence

Actual events, judicial cases, historical incidents, personal cases, empirical datasets, and documented organizational/technical incidents are recorded separately from synthetic toy cases and constructed benchmarks.

```text
CASE_ORIGIN:
  real_event
  judicial_case
  historical_case
  personal_case
  empirical_dataset
  organizational_or_technical_incident

SOURCE_STATUS:
PRIMARY_OR_AUTHORITATIVE_SOURCE:
FACT_INTERPRETATION_BOUNDARY:
METHODS_APPLIED:
METHODS_DIRECTLY_TESTED:
DOMAIN_BRIDGE:
EXTERNAL_STANDARD:
PRIVACY_OR_SENSITIVITY_HANDLING:
```

A real-world case is application evidence first. It contributes to method validation only when the method protocol, failure/scoring criteria, external standard, and baseline are sufficiently locked to make it a genuine test rather than an illustration.

### 12.4 Two-axis rule

`EVIDENCE_SCOPE_CLASS` and `CASE_ORIGIN` must not be collapsed into one field. For example, one judicial case may be `method_specific` evidence for Audit while also supporting shared evidence-status or bridge disciplines.

The current registry and migration matrix are maintained under [`../evidence/`](../evidence/).

## 13. Shared-core extraction and closure / 공통 구조 추출·종료

The controlling rule is [`SHARED_CORE_EXTRACTION_RULE.md`](SHARED_CORE_EXTRACTION_RULE.md).

Each shared element preserves the following separation:

```text
SHARED_CORE:
METHOD_SPECIFIC_INPUT:
METHOD_SPECIFIC_OPERATION:
METHOD_SPECIFIC_OUTPUT:
METHOD_SPECIFIC_FAILURE_CRITERIA:
METHOD_SPECIFIC_VALIDATION:
```

The current shared-core registry is:

```text
SC-01  Status / Typed-Domain Discipline
SC-02  Source / Interface / Version Lock
SC-03  Explicit Bridge Discipline
SC-04  Minimum-Layer / Optional-Interface Restraint
SC-05  Aggregate / Information-Loss / Reconstruction Restraint
SC-06  Transition / Lineage Discipline
SC-07  Evidence Scope / Case-Origin Separation
SC-08  Baseline / Failure-NO_GAIN / Anti-Post-Hoc Discipline
SC-09  Evidence-Status / DSD-Object-Status Separation
SC-10  External-Standard / Domain-Validation Separation
```

The shared-core closure audit reviewed all 45 unordered rule pairs and found no exact duplicate shared rules. Every SC has representative transfer coverage across all eight higher-level fields and explicit activation/non-transfer conditions.

```text
SHARED_CORE_CLOSURE:
  closed_for_current_registry_with_conditions

DIRECT_METHOD_VALIDATION_FROM_SHARED_CORE:
  not claimed
```

`REPRODUCIBILITY_RECORD` remains part of method/evidence maturity architecture rather than a separate universal semantic SC because concrete rerun/retrace obligations differ materially by method.

Shared-core extraction should be reopened only when source semantics, method boundaries, new independent methods, or a genuinely new stable cross-method obligation changes the current closure basis. Until then, development priority moves to method-specific protocols, evidence accumulation, reproducibility/retraceability, and real-world application cases.
