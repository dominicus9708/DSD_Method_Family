# PA-P32 — P27 동결본 잉여 원시좌표·완성/축약·엄격 동형 분리 감사

- 감사일: 2026-10-28 KST
- 저자: Kwon Dominicus
- 논문 동결: 영문 P27 SHA256 `51c194ec33f802a2061b68b3521fdb831f0f754a0386fa72f8e89a39efff7bdb`, 국문 P27 SHA256 `a643ea619f9594142bfc09b9f486c948cf0a85679a3b2a8a43bc731a1e108fbb`.
- 입력: P27 원문 Def2.5, Def2.6/§2.5, C1/Th3.7, Def5.1, Def6.1/6.3/6.7, Def7.1, P29/P30/P31 기존 감사.
- **원고 편집·PDF 출판·Zenodo 변경 금지.** 이 문서는 조건부 의미론 감사이며 저자 규약을 임의로 확정하지 않는다.

## 1. 정확한 질문과 실제 원문 근거

Def2.5는 미선언 또는 프로필 미제공 `ω`의 Ap/Sat/Ξ를 “not required”라고만 적는다. P27의 원시자료는 set-coded tuple이고 인덱스 가족의 **정확한 정의역**은 이 문구만으로 확정되지 않는다. Def5.1 완전 기술자는 원시 가족 전체를 보존한다. 한편 Def6.1/6.3의 보존·반영 조건은 출발에서 선언되고 프로필이 제공된 종류에 한정된다. Def7.1 단계 비교는 “visible through property stage”라는 설명으로 규정되어, 제2절 원시 가족의 전체 인덱스와 같은 대상을 비교하는지가 명문화되지 않았다.

### 두 가능한 원시자료 의미론

**A — 정규 제한 가족:** `Act(A)={ω∈Π_A:profile available}`에서만 필수 Ap/Ξ를 정의하고, Sat는 `(ω,d), ω∈Act(A),d∈δ(ω)`에서 정의한다. 그 외 좌표는 정규 모형 일부가 아니다. 이때 C1의 `Red(Comp(P))=P`와 strict 비교/단계 비교는 같은 활성 자료에 대해 적용된다.

**B — 원시 제시+여분 좌표:** 위 활성 자료 외에 추가로 타입에 맞는 잉여 Ap/Sat/Ξ 자료가 `raw` 속에 포함될 수 있다고 가정한다. 그러면 `Comp`가 그 자료를 그대로 보존하고 `Red`가 파생좌표만 제거한다면 **원시자료의 정확한 역법칙은 B에서도 성립한다**. 반면 strict iso가 활성 자료만 보존할 때 `raw` 전체의 값·인덱스 보존은 따라오지 않는다. 단순히 “잉여 허용⇒C1 실패”라고 결론 내릴 수 없다.

### 조건부 유한 판별 반례

공유 고정 Stage-VI 기반에서 상속 종류 `h`의 운반체는 `{a}`, 후보 속성 `p`의 프로필은 `(h)`, 선행조건은 없음, `Π_A=Π_B=∅`로 둔다. 보조 종류 공급도 없다. A의 원시 가족은 비어 있고 B는 **미선언 p의 추가 적용가능성** `Ap_{B,p}={(a)}`를 raw 데이터로 포함한다고 가정한다. 이 잉여 자료는 `p`가 비선언이지만 `(h)`가 제공되어 있어 타입 자체를 작성할 수 있다.

- 두 모델 모두 활성 제약과 PI/PII는 공허하게 만족한다 (B가 모형으로 **허용되는지는 의미론 B를 선택한 경우에 한함**).
- 선언·제공 종류가 같고 보존할 활성 속성 좌표가 없어서 두 모델은 strict core identity-isomorphic.
- 하지만 raw 원시 가족과 그 가족을 포함하는 완전 기술자는 서로 다르며, literal Stage-3 family도 서로 다르다.
- 따라서 **“원시자료 전체를 비교하는 Stage-3”**와 **“선언된 활성 좌표만 비교하는 strict core 동형”**이 동일하다는 등치는 B에서 무조건 사용할 수 없다.
- 이는 동일 운반체 `h`의 항등 비교이므로 “이름 재표기로 기술자 튜플이 다른 정상적인 동형” 문제로 축소할 수도 없다.

## 2. 일반 집합론적 결론 (정해진 의미론에 상대적)

`N(P)`를 raw 제시 P의 원시 가족을 활성 종류와 해당 선행조건 인덱스로 **제한**하는 정규화라고 하자. `N(P)`가 적법하게 구성된다는 전제하에:

1. `N(N(P))=N(P)`는 함수 제한의 멱등성으로 성립한다.
2. B에서 허용된 서로 다른 raw 제시 `P,Q`라도 `N(P)=N(Q)`가 가능하다. 따라서 `N`은 일반적으로 단사가 아니다.
3. C1의 파생 좌표가 활성 원시자료에 대해서만 정의된다면 `Derived(P)=Derived(N(P))`. 이것은 `P=N(P)`을 뜻하지 않는다.
4. B의 raw 원시자료를 `Comp_raw(P)=(P,Derived(P))`에 **온전히 남기면** `Red_raw(Comp_raw(P))=P`. full model의 derived가 C1을 만족하면 `Comp_raw(Red_raw(F))=F`도 성립한다. 이는 무한 기저집합에서도 구조적인 함수적 등식이다.
5. `Comp`가 말없이 `N(P)`로 바꿔 `Comp_norm(P)=(N(P),Derived(N(P)))`을 만들면 `Red(Comp_norm(P))=N(P)≠P`인 raw P가 있다. 따라서 **정규화를 원시 축약/완성의 정확한 역법칙에 혼입하면 안 된다**.
6. strict core iso와 `I_k` 비교를 활성 좌표 기준으로 정의하면 B의 여분 자료는 관찰되지 않는다. 전자의 등가류와 **raw complete descriptor 전체 동형**은 구별해야 한다.
7. A를 채택하면 B의 raw 부가 좌표는 정규 모델에서 배제되므로 `I_4≠∅ ⇔ strict core iso`와 Stage-3 정보의 일관성을 깔끔하게 확보할 수 있다. 그러나 A가 **이미 논문의 유일한 뜻이라고 주장하지 않는다**.

## 3. P31 제11절 의존성 재분류

| 결론 | P32 영향 | 판정 |
|---|---|---|
| (5) C1·Red 역법칙 | **원시 가족 전체 보존** 시 A와 B 모두 정확한 역법칙 가능. 무통지 정규화만 금지 | `GENERAL_PROOF_CONDITIONALLY_SUPPORTED` |
| (6) forward/embedding | 활성 종류에 관한 비교로 보존되며 raw 부가자료까지 보존한다고 일반화 불가 | `SUPPORTED_FOR_ACTIVE_CORE` |
| (7) strict iso | 원문 S1–S4는 활성 구조 동형. complete descriptor 전체 동형과 구분 | `SUPPORTED_FOR_ACTIVE_CORE` |
| (9) I4/I5/first branching | literal stage family vs 활성구조 stage 비교를 일치시켜야 함 | `FORMAL_SCOPE_OBLIGATION_OPEN` |
| (13) Stage-VI 고정 | 여분 자료 해석과 관계없이 형성 기반은 불변 | `SUPPORTED_RELATIVE_FIXED_BASE` |

P29 Th8.4의 전모형 적법성, P31 Th11.1 (3)/(11)/(12)의 존재/전칭 범위 문제는 이 판별로 해결되지 않는다.

## 4. 작업 규약 제안 — 아직 원고 반영하지 않음

현재 증명 전체의 최소 변경을 우선한다면 **A: 정규 제한 가족**이 실무적으로 단순하다. 논문에서 “not required”를 해당 활성 가족의 정확한 정의역 문장으로 명확히 쓰고, Def5.1/Def7.1의 원시자료 가족 및 비교집합도 동일 인덱스를 사용하게 할 수 있다.

B를 선택하려면 “활성 코어”와 “원시 제시의 부가자료”를 별도 계층으로 정의하고, `strict iso`, `complete descriptor`, `Stage-3 comparison`가 각각 어느 계층을 보는지 명시해야 한다. B도 수학적으로 가능한 선택이나 추가 명세·증명 의무가 더 많다.

**어느 쪽도 현재 논문의 이미 확정된 뜻으로 독단적으로 선택하지 않는다.** 이후 수학 감사에서는 A를 **조건부 기준모형**으로 사용할 수 있지만 B를 실패·폐기한 것으로 처리하지 않는다.

## 5. 실행 증거 및 판정

독립 유한 판별검사 `verify_p32_surplus_semantics.py`: 17/17 예상 관찰을 실제 계산으로 확인. 이는 단일 상속 타입·후보 종류에 대한 **조건부 비교 증인**이지 일반 증명 또는 독립 외부평가가 아니다. 일반 논증은 위의 명시된 정규화/원시보존 등식에 근거한다.

```text
PA_P32_AUDIT: EXECUTED
P27_TEX_PDF_ZENODO: FROZEN_UNCHANGED
SURPLUS_PRESENTATION_SEMANTICS: UNDECIDED_IN_SOURCE
C1_INVERSE_GENERAL: HOLDS_IF_ALL_PRIMITIVES_RETAINED
NORMALIZE_THEN_EXACT_INVERSE: DISPROVED_ON_RAW_B
ACTIVE_STRICT_ISO_VS_RAW_STAGE3: DISTINCT_UNDER_B
RECOMMENDED_WORKING_CONVENTION: A_CONDITIONAL_ONLY
P29_TYPED_DATA_PREMISE: OPEN
P30_IK_SOURCE_SCOPE: OPEN
P31_FIXED_SIGNATURE_SCOPE: OPEN
PROPERTY_FPA: OPEN
```

다음 FPA: (i) Def7.1의 `I_k`를 raw/active 의미론 양쪽으로 전개하고 strict 동형 대응성을 정리 (ii) §11(3),(11),(12) 양화 전제를 시그니처별 판정식으로 분리 (iii) 전체 증명 의무/보류개정 항목을 통합하여 최종 종결 가능성을 감사. 이 과정을 마치기 전에는 원고를 변경하지 않는다.
