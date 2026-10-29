# PA-P38 — 속성공리계 동결 P27의 A/B1/B2 단계 비교·엄격 동형·C1 병렬 감사

- 2026-10-29 KST. 논문 저자: **Kwon Dominicus**.
- 감사 대상: P27 §2.4–2.5, §3 C1/Th3.7, §5 완전 기술자, §6 F1–F5/E1–E3/S1–S4, §7 I1–I5, §11 (5–7,9).
- 동결 원고 EN SHA256 `51c194ec33f802a2061b68b3521fdb831f0f754a0386fa72f8e89a39efff7bdb`; KR SHA256 `a643ea619f9594142bfc09b9f486c948cf0a85679a3b2a8a43bc731a1e108fbb`. LaTeX/PDF/Zenodo 미수정.
- 사용자 결정: **A/B 최종 선택은 전체 공통 감사 이후까지 보류**. B안을 실패·폐기한 것으로 쓰지 않고 B1/B2를 나누어 검사한다.

## 원문과 조건부 감사 명세 구별

Def2.5는 미선언·프로필 미공급 속성 자료를 "not required"라고 기술한다. 이는 잉여자료 금지 또는 허용의 정당화가 아니다. Def6의 현행 strict property isomorphism은 선언되고 이용 가능한 프로필의 활성 원시좌표만 보존한다. Def7.1은 "strict-comparison conditions visible through property stage"라 하여 raw 대 active의 구분을 성분식으로 명시하지 않았다.

- **A 정규 제한 가족:** `Act(P)={ω∈Π_P:Av_P(ω)}`; Ap, Xi의 정확한 인덱스가 Act(P), Sat의 정확한 인덱스가 `{(ω,d):ω∈Act(P),d∈δ(ω)}`. 모든 활성 자료 적법하게 타입화.
- **B1 원시자료 보존+활성 비교:** 적법한 부가 raw 좌표를 원시 제시 안에 보존. 비교 I_k는 정규화 N(P),N(Q)에서 수행. raw 기술자 전체의 보존은 원문 strict와 동일시하지 않음.
- **B2 원시자료 보존+raw 비교:** raw 가족의 인덱스 존재와 좌표 데이터까지 비교하는 I_k^raw를 별도 정의. 이를 나타내는 새 강화 동형 ≅_raw가 필요. 현행 원문 strict와 같다고 주장하면 반례 존재.

B의 추가 원시자료는 공유 시그니처에 포함되고 실제 타입 제품이 정의되는 종류에 한정한다는 **감사 작업 가정**이다. 미공급 프로필을 임의의 곱집합으로 채우지 않는다. A 또는 B 어느 해석도 원문이 이미 채택했다고 단정하지 않는다.

## 일반 집합론적 논증 (선언된 가정에 상대적)

두 적법 완전모형 P,Q가 같은 고정 Stage-VI와 공유 시그니처 위에 있다. T_P=Dom X_P^aux와 T_Q가 다르면 I1~I5 모두 공집합. 같으면 보조 운반체 성분 전단사의 *전체* 가족 집합 Bij_T(P,Q)에서 출발한다. inherited sort는 항등. 각 속성의 유한 ordered profile에 따라 유도 곱사상은 전단사이며 함수집합/집합곱/분리로 I_k는 임의(무한 포함) 집합 운반체에도 집합으로 정의된다.

1. 활성 비교 I1=Bij_T, I2=I1의 선언 보존 부분, I3^act는 활성 Ap/Sat의 전단사 상-등식, I4^act는 활성 할당 정의역/값 보존, I5^act는 C1 파생좌표 보존이다. 정의상 중첩. PI/PII를 만족한 코어에서 D, DepSat, status, PropRec는 활성 자료의 **결정론적 함수**이므로 I5^act=I4^act. P27 Def6 F/E/S의 명시조건을 각 원소에 대입해 `I4^act(P,Q)≠∅ iff P≅_strict,active Q`; 원문 S4는 S1–S3를 가진 embedding의 역으로 따라온다.
2. A에서는 활성 자료가 원시 전체이므로 바로 위 결과가 적용된다. B1에서는 `I_k^{B1}(P,Q)=I_k^A(N(P),N(Q))`, 정확한 raw C1은 `Comp_B(P)=(P,C1(N(P)))`로 **원시 raw 전체를 보존**. 따라서 C1 정확 역법칙 유지. 다만 N은 일반적으로 비단사여서 raw 제시의 구별은 I_k^B1에서 사라질 수 있다.
3. B2에서는 raw Ap/Sat 가족의 **인덱스 집합 일치와 상-등식**을 I3^raw에, raw Xi 가족의 인덱스/부분함수 그래프 운반을 I4^raw에 더한다. C1 파생좌표는 여전히 active 자료만으로 결정되므로 `I5^raw=I4^raw`. 각 k에 `I_k^raw⊆I_k^act`, k=1,2는 등식. `P≅_raw Q :⇔ I4^raw(P,Q)≠∅`는 항등·역·합성에 닫힌 동치관계이며 raw first branching은 raw 동형에 대해서만 대칭/불변.
4. raw iso ⇒ original core strict iso, 역은 일반적으로 거짓. 따라서 B2의 I4raw와 **현행** strict를 혼용한 `I4raw≠∅ iff original strict`는 반례로 거짓. B2 자체가 모순이라는 주장이 아니며, 새 raw 동형 정의와 관련 정리의 의존 변경이 필요한 상황이다.

## 두 개의 구별 증인

상속 종류 h의 운반체 {h0}, 후보 종류 q의 프로필 (h), 값공역 {0,1}. 두 모델 모두 선언 Π=∅, 보조 운반체 없음, 활성 좌표 없음.

- P raw 가족 공집합, Q raw 가족에 **미선언 q의 Ap_q={(h0)}**만 추가. B 조건부 허용에서 P,Q는 original strict identity-isomorphic이지만 I3raw(P,Q)=∅; raw first branch=3.
- P raw 가족 공집합, R raw 가족에 미선언 q의 **Xi_q((h0))=1**만 추가. I3raw(P,R)≠∅, I4raw(P,R)=∅; raw first branch=4. 이 부가 Xi는 *미선언* 종류의 추가 raw 자료로만 사용하고 활성 PI/PII의 대상이라고 무단 변경하지 않는다.

P≅_active Q인데 b_raw(P,Q)=3; Q≅_active Q인데 b_raw(Q,Q)는 정의되지 않으므로 **raw 최초분기 지수는 original strict 동형에 대한 불변량이 아니다**. raw iso에 대해서만 불변.

## 독립 유한 판별과 경계

별도 Python은 두 후보 p:(u), q:(h), δ(p)=∅, δ(q)={d}; 보조 종류 u의 미공급/공집합/1원소/2원소; 할당값 0/1; 4종 활성 템플릿과 3종 부가 raw 템플릿으로 **서로 다른 59개 raw 제시, 3,481개 순서쌍, 1,392개 후보 전단사**를 구성했다. 계산 내 16개 조건이 통과. raw 단계3 분기가 있는 core-iso/raw-noniso 순서쌍 90개 발견. raw 단계4는 별도 명시적 한 점 반모형으로 확인했다. 59개 템플릿에서 raw 단계4 충돌쌍이 0개라도 일반적 부재를 뜻하지 않는다. 유한 회귀와 임의 집합 증명은 엄격히 분리한다.

**검증 프로그램/결과:** `verify_p38_three_semantics.py`, `P38_EXPECTED_EVIDENCE.json`; 실행 재현 규칙 `README_WINDOWS_KR.md`. GitHub Actions는 Python 3.10/3.12에서 두 P27 소스 SHA256 확인 후 독립 JSON 재현을 검사한다.

## 증명 의무 전파

| 제11절 | A | B1 | B2 |
|---|---|---|---|
| (5) C1 | 정확한 active 원시자료 보존 | raw 전체 원시자료 보존 필수 | raw 전체 보존 필수 |
| (6) maps | original active | original active | raw 사상을 원한다면 별도 정의 필요 |
| (7) strict | original S1–S4 | original active strict, raw descriptor와 구별 | ≅raw를 original strict와 혼동 금지 |
| (9) I4=I5 | original strict와 대응 | N(P) active 구조에서 대응 | ≅raw와 대응; original strict와 불일치 |

**미해결:** S-01 A/B 저자 선택 OPEN, S-03 원문 Def7.1의 정확한 의미론 선택 OPEN. S-02 typed finite realization / S-04 theorem 11 quantifier는 P37 조건부 수학 증명이 있지만 원고 미수정. 전체 `PROPERTY_FPA=OPEN`, 외부 독립 검증 미확립, 영·국문 원고·PDF·Zenodo 동결.

다음 P39는 최종 56개 번호 항목의 전역 종결 의무 및 보류 개정 범위를 독립 재감사하되 A/B를 조기 선택하지 않는다.

```
AUDIT_ID: PA-P38-20261029-A-B1-B2-STAGE-STRICT-GENERAL-SCOPE
MATHEMATICAL_VERDICT: CONDITIONAL_GENERAL_PROOFS_SUPPORTED / B2_ORIGINAL_STRICT_EQUIVALENCE_DISPROVED
DSD_AUDIT_VERDICT: PASS_WITH_REFINEMENT
REVISION_NEED: SEMANTICS_AND_DEPENDENCIES_DEFERRED
INDEPENDENT_EXTERNAL_VALIDATION: not_established
P27_EN_KR_TEX_PDF_ZENODO_EDITED: NO
FULL_PROPERTY_FPA: OPEN
```
