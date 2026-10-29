# PA-P37 — S-02 및 S-04의 독립 일반 증명·고정 시그니처 필요충분조건 감사

감사일: 2026-10-29 KST. 원고 저자: **Kwon Dominicus**. 적용 절: P27 §2·§3·§4·§7·§8·§9·§11.

**원고 동결:** P27 영문 SHA256 51c194ec33f802a2061b68b3521fdb831f0f754a0386fa72f8e89a39efff7bdb, 국문 a643ea619f9594142bfc09b9f486c948cf0a85679a3b2a8a43bc731a1e108fbb. 원고 LaTeX/PDF 및 Zenodo 불변. 원문에 본 결과가 이미 반영되었다고 주장하지 않음.

## 1. 의미론 범위와 선행 자료

사용자의 결정에 따라 **A/B 의미론을 아직 선택하지 않는다**. S-02는 타입 적법성 및 정확한 원시자료 보존이라는 조건 아래 A 또는 B에서 성립한다. S-04의 아래 필요충분조건은 P33에서 정의한 **A(정규 제한 활성 원시좌표) 및 활성 단계 비교**를 임시 작업 해석으로 명시한 정리이다. B1은 활성 구조에 적용하면 유사하지만, B2의 raw 전체 엄격동형까지 자동 적용하지 않는다.

선행 문서: [P29 타입 전제](../P29_finite_realization_premise/P29_FPA_SCOPE_AUDIT_KR.md), [P32 정확한 C1](../P32_surplus_primitive_semantics/P32_SURPLUS_SEMANTICS_AND_EXACT_C1_INVERSE_AUDIT_KR.md), [P33 비교집합](../P33_explicit_stage_comparison_proof/P33_I1_I5_GENERAL_PROOF_AND_RAW_SCOPE_AUDIT_KR.md), [P34 양화 반례](../P34_fixed_signature_quantifier_scope/P34_FIXED_SIGNATURE_QUANTIFIER_AUDIT_KR.md), [P35 종결 대장](../P35_integrated_fpa_closure_ledger/P35_FPA_INTEGRATED_CLOSURE_LEDGER_KR.md), [P36 의미론 비교](../P36_semantics_decision/P36_SEMANTIC_A_B_MINIMAL_AXIOM_AUDIT_KR.md).

## 2. S-02 — 적법한 유한 원시 제시에서의 유일한 완성

기반 Stage-VI 기록과 공유 시그니처를 고정한다. (T) 제공 좌표가 정의 2.5의 **적법한 typed premodel**이고 활성 속성마다 필요한 Ap, Sat_d, Xi가 정확히 타입화되어 제공됨; (F) 정의 8.3의 속성 유한성(선언 종류, 보조 운반체, 제공된 Ap/Sat, 할당 정의역의 유한성); (I) 모든 선언·프로필 이용가능 종류 w에서 Dom Xi_w ⊆ Ap_w ∩ DepSat_w를 가정한다. B raw를 별도로 채택하면 그 타입 규약과 전체 원시제시 보존을 T에 추가한다.

**일반 증명:** T가 적법 전모형을 만들고 I가 PI/PII를 만족시켜 원시코어 P를 만든다. C1은 P로부터 D_w, DepSat_w, 상태와 PropRec를 함수적으로 결정하므로 Comp(P)=(P,Derived(P))가 존재하고 유일하다. F에서 선언종류와 할당 정의역이 유한이므로 원시의 property-finite 성질 및 정의된 레코드의 유한성이 유지된다. 상속된 입력운반체 자체가 무한하면 모든 입력에 대한 상태 함수가 유한 집합이 될 필요는 없다. 이는 정의 8.3의 property-finite 개념과 구별한다.

**역방향 경계:** 포함식 I만으로 타입 적법성을 얻을 수 없다. X_p={(a)}인데 Ap_p={(ghost)}, Sat_p,d={(ghost)}, Xi_p가 공함수이면 I는 공허하게 참이지만 Ap/Sat는 X_p의 부분집합이 아니므로 typed premodel이 아니다. 잘못된 값 공역, 튜플 길이, 필수 원시좌표 누락도 타입 조건 위반이다. **P27 Th8.4의 원문이 T를 암묵적으로 요구한다는 독해와, T 없이 충분하다는 강한 독해를 구별한다.**

**보류한 명료화 후보:** 제8절 정리의 supplied finite primitive data를 ‘정의 2.5를 만족하며 필요한 입력좌표 전체가 주어진 compatible, well-typed primitive presentation’으로 한정하고 제11절 (10)의 compatible과 맞춘다. 논문 본문 변경은 아직 금지.

## 3. S-04 — 임의 고정 시그니처에서의 증인 존재에 관한 일반 분류

하나의 고정 FVI와 공유 시그니처 Σ를 취한다. PiHat은 후보 속성 종류, S_aux는 선택적 보조 종류이다. Real(w)는 보조 운반체 공급을 적법하게 고를 때 w의 타입 입력곱이 **비공집합**이 될 수 있다는 뜻이다. 모든 유한 프로필에서 이는 그 프로필에 들어가는 **상속 운반체들이 모두 비공집합**이라는 것과 동치다. 보조 종류는 각각 단일원소 집합으로 공급할 수 있다.

### S04-I — 공리 PI·PII 상호 비도출의 필요충분조건

**조건:** 어떤 w∈PiHat에 대해 Real(w), Z_w≠∅, δ(w)≠∅가 모두 성립한다.

**충분성:** 입력 x 및 값 z를 택해 Xi_w(x)=z. 첫 전모형은 Ap=∅, 모든 Sat_d={x}: PI 위반/PII 만족. 두 번째 전모형은 Ap={x}, 하나의 d0에 대한 Sat_d0=∅, 나머지 Sat={x}: PI 만족/PII 위반. 모두 동일 고정 서명 안의 적법한 typed **premodel**이다.

**필요성:** PII 위반이면 어떤 할당된 x가 선행조건을 만족하지 못한다. 따라서 x∈X_w, Z_w 비공집합이고 δ(w)도 비어 있지 않다. 위 조건이 없다면 PII가 모든 typed premodel에서 성립하거나 어떤 할당도 존재할 수 없으므로 두 공리의 **상호** 비도출이 불가능하다.

### S04-B — 단계 2·3·4 최초 분기 증인의 필요충분조건 (P33의 I_k)

- **Stage 2:** PiHat≠∅. 필요한 경우 프로필 미제공이어도 같은 보조 공급으로 한쪽에서 w를 선언하고 다른 쪽에서 선언하지 않으면 I1 비공집합, I2 공집합이다. 필요성은 선언집합 차이가 반드시 있어야 함.
- **Stage 3:** ∃w∈PiHat, Real(w). 같은 공급·선언에서 한쪽 Ap=∅, 다른 쪽 Ap={x}; Xi는 양쪽 공함수. I2 비공집합, I3 공집합. 역으로 모든 이용가능 입력곱이 공집합이면 Ap와 Sat의 유일한 값은 공집합이므로 분기 불가능.
- **Stage 4:** ∃w∈PiHat, Real(w) 및 Z_w≠∅. 같은 공급·선언·Ap/Sat에서 한쪽 Xi=∅, 다른 쪽 Xi_w(x)=z로 지정하면 I3 비공집합, I4 공집합. 역으로 모든 가능한 정의역이 공집합이거나 값공역이 비면 모든 부분할당이 공함수.

### S04-C — P27 요약의 고정 서명별 비분류 증인 필요충분조건

**조건:** S_aux≠∅ 또는 ∃w∈PiZero, Real(w). P27 Def9.1의 요약이 정의되는 property-finite full model 쌍을 대상으로 한다.

**충분성:** S_aux에 u가 있으면 선언 종류를 공집합으로 두고 A에는 u를 미공급, B에는 공집합 캐리어로 공급하면 요약 둘 다 (0,∅)지만 strict S2가 실패한다. 또는 zero-bearing w에서 입력 x가 가능한 경우 둘 다 w를 선언하고 Xi는 공함수, 한쪽 Ap=∅ 다른 쪽 Ap={x}로 택한다. 두 요약은 (1,{(w,0,0,0)})로 같지만 strict 동형은 아니다.

**필요성:** S_aux가 비고 zero-bearing 종류 중 비공집합 입력곱을 허용하는 것이 없다면, 모든 요약-적법 모형은 고정 상속 운반체 위에서 입력곱이 빈 zero-bearing 종류만 선언할 수 있다. 해당 종류들의 Ap/Sat/Xi는 모두 공집합으로 강제된다. 요약이 속성 라벨을 보존하므로 동일 요약이면 선언 집합이 일치해 정규 코어가 동일하고 strict 동형이다.

**논리적 경계:** 세 정리의 고정 서명별 필요충분조건은 원문 §§4,8,9의 기존 존재 증인을 부정하지 않는다. 그러나 제11절 첫머리의 Fix FVI, Σ를 모든 시그니처의 무조건 전칭으로 읽은 (3)/(11)/(12)는 공집합 후보 시그니처에서 이미 반증되었다. 본 P37 결과는 그 범위를 더 정밀하게 분리한 **독립 감사 정리**이지 P27 원문에 이미 포함된 결론이라는 뜻이 아니다.

## 4. 제한 유한모형 독립 회귀 (일반 증명과 구별)

- [P37 독립 계산기](verify_p37_fixed_signature.py): Python 표준 라이브러리, 후보 종류 최대 하나, 상속 h 운반체 크기 0/1, 보조 종류 u 미포함 또는 미공급/공집합/1원소, 순서·반복 프로필, prerequisite 0/1, 값공역 공집합/한 점, zero-bearing 선택.
- 실제 **76개 서명 유형**, **608개 typed premodel**, **520개 PI/PII 적법 코어**, 위 5개 분류식의 **380개 관찰/기대 비교 전부 일치**.
- [예상 결과 JSON](P37_FIXED_SIGNATURE_EVIDENCE.json). 모든 후보 시그니처·임의 무한 운반체의 계산적 전수 검증이라고 주장하지 않는다.

## 5. 제11절·동결 관리 판정

| 의무 | 결과 | 원고 상태 |
|---|---|---|
| S-02 / Th8.4, §11(10) | T+F+I ⇒ 유일 C1 완성 일반 논증 지지; T 없는 강한 문장은 부적법 예제로 배제 | 수정 보류 |
| S-04 / §11(3) | 고정 Σ에서 mutual PI/PII 독립의 필요충분조건 도출(A) | 수정 보류 |
| S-04 / §11(11) | 고정 Σ에서 Stage2/3/4 존재의 필요충분조건 도출(A) | 수정 보류 |
| S-04 / §11(12) | 고정 Σ에서 요약 충돌 존재의 필요충분조건 도출(A) | 수정 보류 |
| S-01→S-03 | A/B 최종 선택 보류. B1은 활성 핵심·raw 자료 2층, B2는 별도 강한 동형 필요 | OPEN |

MATHEMATICAL_VERDICT: CONDITIONAL_GENERAL_PROOFS_SUPPORTED / FIXED_SIGNATURE_UNIVERSAL_OVERCLAIMS_DISPROVED; DSD_AUDIT_VERDICT: PASS_WITH_REFINEMENT; PROPERTY_FPA: OPEN; S01_SELECTION: DEFERRED; MANUSCRIPT_PDF_ZENODO_EDITED: NO; EXTERNAL_VALIDATION: NOT_ESTABLISHED.

**후속 P38:** A/B를 계속 보존한 채 S-03 I1–I5와 raw/active 비교, 엄격 동형의 일반 증명 의무를 병렬 감사한다. 공통 S-02/S-04 결과는 소스 개정 직전의 보존된 증명 대장에 남긴다.
