# DSD Method Family Framework / DSD 방법군 공통 프레임

Status: working framework
Framework date: 2026-09-06

This document extends the existing DSD Analysis and DSD Audit repository into a broader **DSD Method Family** without relocating or rewriting established historical paths.

이 문서는 기존 DSD 분석론과 DSD 감사의 경로·기록을 보존하면서, Formation Axiom System, General Property Axiom System, Channel-Indexed Static Aggregation, Structural Reorganization Dynamics 및 선택적 특수화에서 파생되는 여러 사용 방식을 하나의 **DSD 방법군**으로 정리하기 위한 공통 프레임입니다.

## 1. Preservation rule / 기존 구조 보존 원칙

- Existing `DSD_Audit/`, `audits/`, `challenges/`, `methodology/`, `protocols/`, and `templates/` paths are preserved.
- Existing DSD Analysis records remain valid historical and operational records.
- New method-family material is added under `methods/`.
- `methods/01_analysis/` and `methods/02_audit/` are registry wrappers pointing to the established locations rather than migrations of the existing corpora.
- Historical paths are not silently rewritten when a method is later generalized.

## 2. Shared DSD source layers / 공통 DSD 기반 층위

A method may use only the layers actually required by its task.

1. **Formation** — admission, restriction, realization, partial assignment, operational-channel formation, finite composition interface.
2. **General Property** — typed profiles, applicability, contextual prerequisites, partial property assignments, status distinctions.
3. **Static Aggregation** — channel-indexed analytic realization, finite aggregation, optional typed-property aggregation, information-loss and reconstruction conditions.
4. **Dynamics** — component-resolved trajectories, regular epochs, transition classes, lineage, dynamic bridges.
5. **Optional specializations** — realized-axis geometry or any domain-specific structure supplied explicitly.

The current paper-facing interface lock remains in `DSD_INTERFACE_PROFILE.md`.

## 3. Sixteen core methods / 16개 핵심 방법

The first method-family registry contains sixteen methods:

1. DSD Analysis / DSD 분석론
2. DSD Audit / DSD 감사
3. DSD Specification / DSD 명세론
4. DSD Design / DSD 설계론
5. DSD Synthesis / DSD 합성론
6. DSD Comparison / DSD 비교론
7. DSD Classification / DSD 분류론
8. DSD Transformation / DSD 변환론
9. DSD Provenance-Lineage / DSD 추적·계보론
10. DSD Aggregation-Compression / DSD 집계·압축론
11. DSD Measurement / DSD 측정론
12. DSD Computation-Optimization / DSD 계산·최적화론
13. DSD Simulation / DSD 시뮬레이션론
14. DSD Control / DSD 제어론
15. DSD Diagnosis-Reconstruction / DSD 진단·복원론
16. DSD Interpretation / DSD 해석론

`Operations/Governance` is retained as a possible cross-cutting lifecycle practice and is not counted as a separate core method in this initial 16-method registry.

## 4. Common method record / 공통 방법 기록 형식

Every method definition should state at least:

```text
METHOD_ID:
METHOD_NAME:
STATUS: established / developing / proposed / experimental
TASK:
INPUTS:
DSD_LAYERS_USED:
DOMAIN_BRIDGE:
EXTERNAL_STANDARD:
OPERATION:
OUTPUTS:
INFORMATION_LOSS_CHECK:
LINEAGE_OR_TRANSITION_CHECK:
LIMITS:
REPRODUCIBILITY_RECORD:
```

## 5. Domain-bridge rule / 분야별 브리지 원칙

DSD does not replace a field's own proof, validation, interpretation, professional, empirical, ethical, or safety standards.

A domain application therefore has the form

```text
DSD structural layer
+ explicit domain bridge
+ domain-specific standard
-> method result
```

A mathematical proof remains mathematical proof; a medical judgment remains subject to medical evidence and clinical standards; a historical interpretation remains subject to source criticism; an artistic interpretation is not reduced to a scalar aggregate merely because DSD can encode selected features.

## 6. Status and bridge discipline / 상태·브리지 규율

Across the method family:

- preserve absence, undefinedness, inapplicability, prerequisite failure, and defined zero when the selected interface distinguishes them;
- do not infer cross-layer mappings from terminology alone;
- do not infer structural identity from aggregate equality without reconstruction conditions;
- preserve failed mappings, alternative mappings, and `NO_GAIN` results;
- when dynamics is used, distinguish value evolution from status/domain and formation-level transitions;
- use explicit lineage when successor identity is not inherited automatically.

## 7. Relationship among the methods / 방법 간 관계

The methods are not a mandatory pipeline. Typical combinations include:

```text
Specification -> Design -> Synthesis -> Audit
Analysis -> Comparison -> Classification
Provenance-Lineage -> Diagnosis-Reconstruction
Aggregation-Compression -> Computation-Optimization
Measurement -> Analysis -> Audit
Simulation -> Control -> Audit
Interpretation -> Comparison -> Audit
```

A case may use one method alone or compose several methods, but each method result should remain separately identifiable.

## 8. Development policy / 개발 정책

- Analysis and Audit are the two most mature current methods and retain their established locations.
- The remaining methods begin as explicit proposed frameworks and should be promoted only after concrete protocols, counterexamples, no-gain cases, and cross-domain tests are accumulated.
- Similarity to an existing external methodology is not treated as novelty by itself.
- The intended contribution is a shared DSD structural layer and interoperability among method roles, not a claim to replace all existing disciplinary methods.
