# PA-P47 — 속성공리계 의미론 결정 이전 감사의 종료 가능성·누락 역점검·raw 타입 음성대조 감사

**날짜:** 2026-11-05 KST. **저자:** Kwon Dominicus.
**동결 정본:** P27 EN SHA256 \`51c194ec33f802a2061b68b3521fdb831f0f754a0386fa72f8e89a39efff7bdb\`, KR SHA256 \`a643ea619f9594142bfc09b9f486c948cf0a85679a3b2a8a43bc731a1e108fbb\`.
**변경 제한:** P27 영/국문 LaTeX·PDF·Zenodo 및 PI·PII·C1 원문은 수정하지 않음. A/B1/B2 의미론은 저자 결정 전 보류하며 실패/성공 때문에 어느 것을 병합·폐기하지 않음. **원문 FPA=OPEN**.
**선행:** [P35 통합 의무](../P35_integrated_fpa_closure_ledger/P35_FPA_INTEGRATED_CLOSURE_LEDGER_KR.md), [P39 56항](../P39_global_56_item_dependency/P39_GLOBAL_56_ITEM_DEPENDENCY_AUDIT_KR.md), [P42 20+13](../P42_consolidated_premises_countermodels_revision_spec/P42_CLAIMS_PREMISES_COUNTERMODELS_REVISION_SPEC_KR.md), [P45 정규화](../P45_semantics_predecision_comparison/P45_SEMANTIC_COMPARISON_MATH_AUDIT_KR.md), [P46 공통 정리·분기 단조성](../P46_choice_invariants_branching/P46_SHARED_THEOREMS_BRANCH_MONOTONICITY_AUDIT_KR.md).

## 1. 정확한 '감사 종료'의 범위와 18개 원본 보고서 역조회

P29부터 P46까지 18개 감사에서 작성한 **각 주요 GitHub Markdown 보고서 18/18의 실재와 내용을 직접 재조회**하였다. 데이터 및 논리적 책임의 기준은 원본 P27, P39 56개 번호 항목, P40 20개 정리·명제·따름정리, P41 97개 의존 간선, P42 제11절 13개 세부결론, P43/P44 언어 수식 대장, P45/P46 의미론별 정리다.

이 검토는 문서 근거 사슬의 **완결성에 대한 제한된 재고조사**이지 모든 임의 집합의 정리가 형식증명되었다는 주장이 아니다.

증거 분류:
1. **직접 원문 확인:** EN/KR 원본 SHA와 용어·정의·표시 수식·번호·참조(원문 잠금).
2. **일반 집합론 논증:** S01에 맞는 typed 인덱스, 동일한 후보 전단사, C1의 결정성, 정확한 raw 보존을 명시한 경우의 P33·P37·P38·P45·P46 조건부 증명.
3. **반모형 및 음성대조:** typing과 양화가 누락된 강한 판본 반례; 성공적인 입력뿐 아니라 잘못된 raw 입력의 거부 여부.
4. **유한 독립 회귀:** 특정 입력족의 기대 관찰; 전체 무한 모형에 대한 일반정리 증명의 대체가 아니다.
5. **연구적 목적/용도:** 모형 내부에서 잉여 raw를 보존할지 및 더 엄격하게 동형을 비교할지는 증명으로 정하는 값이 아니라 사용자/저자 의도에 따라 결정할 **명세 선택**이다.

## 2. P47 신규 경계: 'raw 자료를 허용한다'는 모든 raw 입력을 허용한다는 뜻이 아니다

P27 정의 2.5는 미선언·프로필 미가용 원시 좌표가 '필수 아님'이라고 한다. B1/B2는 아직 선택되지 않은 **조건부 typed raw 확장 해석**이다. P38·P45·P46에서 사용한 한 점 raw 비교는 다음 사실을 추가로 명문화해야 한다.

**가정 계약 \`B-TYPED-CHECK-ONLY\`**:
- 속성 종류는 반드시 공유 \`Pihat\` 후보에 속해야 한다.
- 각 부가 raw \`Ap\`, \`Sat\`, \`Xi\`를 정의하려면 해당 종류의 입력 프로필을 실제로 **타입화할 수 있어야 한다**. 아직 제공하지 않은 보조 운반체를 임의로 만들어 곱집합을 구성하면 안 된다.
- 값이 있는 raw \`Xi\`의 그래프는 실제 입력곱과 값 공역의 부분함수여야 한다.
- 선언되고 프로필 이용가능한 **활성 속성**에는 별도로 PI·PII 및 필수 원시좌표가 적용된다. 비활성 raw 좌표에 자동으로 PI/PII를 확대하지 않는다.
- raw 가족을 **부분 인덱스 함수**로 취급한다면 '인덱스 없음'과 '인덱스 있음·값이 공집합/공함수'는 구분된다. 이 선택은 B2 raw 단계3/4 비교에 직접 영향을 준다.

이 계약은 **반례 검증의 한정된 가정**이며 A/B1/B2의 최종 모델 정의를 이미 선택했다는 주장이 아니다.

### 핵심 음성대조

| 사례 | 기대 검사 | 수학적 의미 |
|---|---|---|
| \`p\` 활성 + \`q\` 미선언, \`q\` 입력 프로필 유효, \`Ap_q=∅\` 부가 | typed B 허용 | 비활성 raw는 활성 C1과 분리 |
| 미선언 \`q\`에 타입 적법한 \`Xi_q\`만 존재 | typed B 허용 | 비활성 raw를 PI/PII에 자동 적용하지 않음 |
| 보조운반체가 제공되지 않은 \`r\`의 raw \`Ap_r\` | **거부** | \`X_r\` 자체가 미가용 |
| 공유 시그니처 밖의 \`z\` raw 좌표 | **거부** | 임의 미지 종류를 공동 시그니처로부터 생성 금지 |
| 선언된 활성 \`p\`에서 \`Dom Xi_p\not\subseteq Ap_p\` | **거부** | PI 위반 |
| 선언된 활성 \`p\`에서 \`Dom Xi_p\not\subseteq Sat_{p,d}\` | **거부** | PII 위반 |
| 활성 \`p\`의 필수 \`Ap_p\` 또는 \`Xi_p\` 누락 | **거부** | 적법 typed core 아님 |
| 미선언 \`q\`의 raw \`Xi\`를 선언만 바꾸어 활성화 | **일반적으로 거부** | 자동 승격·활성화는 현행 정적 공리계가 보장하지 않음 |
| 후보 속성 집합이 비어 있는 적법 고정 시그니처 | 4.6/§11(11) 등의 존재 증인은 불가 | S04 강한 고정 시그니처 전칭 해석의 반례 유지 |

### 추가 규약의 필수성: absent 인덱스와 explicit empty 인덱스

한 입력 \`a\`와 미선언·프로필 이용가능 후보 \`q\`를 둔 두 raw 제시 \`P,Q\`의 활성 코어가 같고
\[
\operatorname{Dom}(\operatorname{Ap}^{raw}_P)\cap\{q\}=\varnothing,
\qquad
q\in\operatorname{Dom}(\operatorname{Ap}^{raw}_Q),
\quad\operatorname{Ap}^{raw}_{Q,q}=\varnothing
\]
라고 하자.

- **인덱스 존재까지 구조적 자료로 취급하면:** \`I_2^{raw}(P,Q)≠∅\`이나 \`I_3^{raw}(P,Q)=∅\`; raw 최초 분기는 3이다.
- **없는 키를 묵시적 공집합과 동치로 정의하면:** \`Ap_q\`에서 차이가 사라져 같은 분기를 도출할 수 없다. 이는 *다른 raw 의미론*을 선택한 것이지 원래 인덱스 민감형 정리의 자동 증명이 아니다.
- raw \`Xi_q\`의 '없음'과 '존재하는 공함수'도 동일하게 raw 4단계에 영향을 준다.

**신규 감사 판정:** B2의 \`I_k^{raw}\`가 어떤 객체의 동형 불변량인지 확정하려면, **raw 가족의 부분함수 인덱스 존재 의미론**을 명시해야 한다. P38/P46이 조건부로 이를 가정한 사실을 폐기하지 않되, *P27에서 이미 명시된 사실*로 승격시키지 않는다.

## 3. 총 56항/20증명/13결론 의무의 결산

| 핵심 관문 | 현재 수학적 판정 | 정확히 남은 것 |
|---|---|---|
| S-01 (Def2.5, C1, Def5.1) | A 활성 제한 / B1·B2 typed raw 보존 모두 조건부 가능 | raw 허용 인덱스·타입, **키 존재=공값 여부**, 기술자 동일성의 저자 의도 |
| S-02 (Th8.4, §11(10)) | 타입 T + property-finite F + 활성 PI/PII 포함 I이면 유일한 완성 | 논문 명시 전제 및 영·국문 양쪽 수정·재증명 |
| S-03 (§6–7, §11(9)) | A/B1 활성 strict, B2 강화 raw strict 아래 \`I4=I5\` 및 최초분기; P46의 \`beta_raw≤beta_act\`은 공통 후보 조건부 | S-01 선택 후 raw/active 인덱스 비교집합·동형 대상을 정확히 정의 |
| S-04 (§4/8/9/11) | 임의 고정 시그니처 강한 전칭판 반례 + 적절 배경의 유효 증인; §4.5/4.6 국소 범위 | 전칭 구조와 적절한 시그니처 존재 명제를 분리하는 문장 개정 |

이것은 **4개 미해결을 0개로 바꾸었다는 판정이 아니다.** S-01→S-03, S-02, S-04의 세 작업 경로를 계속 분리한다. P42 20개 증명 상태와 제11절 13항의 기존 상태를 바꾸지 않는다.

### 동형의 세 층을 혼동하지 않기
- **자료 문자 동일성:** 동일한 인덱스 및 값까지 *같은 제시*인가.
- **활성 strict 동형:** 적법한 운반체 재명명 아래 선언/이용가능 프로필의 원시·파생 상태가 대응하는가.
- **강화 raw strict 동형:** 해당 운반체 전단사로 활성 좌표뿐 아니라 채택된 *전체 raw 인덱스 및 값*도 보존하는가.

B1은 raw 문자 동일성·정확한 보존은 활용할 수 있으나 strict가 raw까지 구별하도록 요구하지 않는다. B2는 별도 강화 strict를 정의해야 한다. 기존 동형이 raw 전체를 이미 동치로 분류했다고 주장하지 않는다.

## 4. '감사 조사를 마침'과 '모든 정리의 FPA를 닫음'의 두 판정

**P47의 제한된 조사 종료 판정:**
- P29–P46 **18/18 보고서 존재**, P39 56항·P40 20증명·P41 97간선·P42 13결론 및 S-01~S-04의 연결은 확인됨.
- A/B1/B2가 서로 충돌하는 조건과 각 대안에 유리한 정보보존 조건을 구분. B2의 부분 인덱스 존재/공집합 동치라는 하위 규약을 **명시적 선택 의무**로 기록함.
- **현재 추적한 의무에 대해서는**, 그 이상 분기를 무한히 추가하는 대신 **저자의 의미론 선택을 위한 근거 검토 단계로 옮길 수 있음**. 단, 모든 알려지지 않은 오류의 부재·전체 자연어 번역 동치·외부 형식증명을 전제로 하지 않음.

**변하지 않는 FPA 판정:**
- A/B1/B2는 **선택하지 않음**, 다른 의미론을 실패 때문에 죽이거나 임의 흡수하지 않음.
- P27 영·국문 LaTeX/PDF/Zenodo 동결.
- S-01~S-04 및 §11의 원문 범위 문제 **OPEN**.
- **\`PROPERTY_FPA=CLOSED\`를 선언할 조건은 충족되지 않음.** 실제 의도된 모형 정의 채택→절별 영·국문 새 판본 개정→개정된 정리 20개/13결론 및 영향을 받는 정의의 일반 수학 재감사→미해결 필수 의무가 없을 때에만 후속 독립 종결 판정 가능.
- 원고 새 버전에는 저자 Kwon Dominicus, 절별 \`% -----\` 주석 경계, 기존 파일·버전 및 반례 보존 원칙 적용.

## 5. 최종 표기

\`\`\`text
AUDIT_ID: PA-P47-20261105-PREDECISION-EXIT-AND-TYPED-RAW-NEGATIVE-CONTROLS
P29_P46_REPORTS: 18/18 FOUND
P27_EN_KR_SHA256: FROZEN
TRACKED_SOURCE_CLAIMS: 56
TRACKED_PROOF_TARGETS: 20
TRACKED_MAIN_CONCLUSIONS: 13
TRACKED_PROOF_DEPENDENCY_EDGES: 97
NEW_GUARD: RAW_KEY_ABSENCE_VS_EXPLICIT_EMPTY_REQUIRES_CONVENTION
NEGATIVE_CONTROL_SCOPE: TYPED_B_HYPOTHESIS_ONLY
PREDECISION_INVENTORY: SCOPED_REVIEW_READY
COMPLETE_ABSENCE_OF_UNKNOWN_MATH_GAPS: NOT_ESTABLISHED
A_B1_B2_SELECTION: DEFERRED
SOURCE_EN_KR_TEX_PDF_ZENODO_MODIFIED: NO
PROPERTY_FPA: OPEN
EXTERNAL_INDEPENDENT_FORMAL_VALIDATION: NOT_ESTABLISHED
\`\`\`

후속 P48은 저자 의도와 증거를 대응시키는 **선택 검토안**이 될 수 있으나, 사용자 의도를 임의로 정하거나 원고에 바로 반영해서는 안 된다. 이번 P47은 A/B1/B2를 채택·흡수·폐기하지 않았다.
