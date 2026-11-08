# PA-P48 — 속성공리계 A/B1/B2와 DSD 방법군의 역할 적합성·관찰 기준 감사

**감사 기준일:** 2026-11-09 KST. **원고 저자:** Kwon Dominicus.
**동결 원고:** P27 EN SHA256 \`51c194ec33f802a2061b68b3521fdb831f0f754a0386fa72f8e89a39efff7bdb\` / KR SHA256 \`a643ea619f9594142bfc09b9f486c948cf0a85679a3b2a8a43bc731a1e108fbb\`.
**작업 범위:** P48은 모형 의미론을 *결정하지 않는* 감사/비교 문서다. P27 영문·국문 LaTeX, PDF 및 Zenodo 미수정. A, B1, B2 중 어떠한 대안도 채택·흡수·폐기하지 않는다. 전체 FPA는 OPEN.

## 1. 이 비교가 필요한 이유

P47까지의 수학 감사에서 동일한 활성 속성 구조를 가지면서 raw 제시가 다른 두 모형은 조건부 B2에서 서로 다른 동형류가 될 수 있다는 점을 확인했다. 그러나 **더 많은 원시좌표를 보존하거나 더 잘게 분류한다는 사실** 자체는 DSD 방법군의 어떤 과업에서도 반드시 그렇게 해야 한다는 실무·수학적 명세를 도출하지 않는다.

따라서 P48은 다음 층위를 나누어 비교한다.

1. **속성공리계의 정적 형식 의미론:** 원시 PI·PII, C1, 타입, 속성 단계, 비교, 완성.
2. **DSD 방법군에서 선택적으로 사용하는 층위:** Formation / General Property / Static Aggregation / Dynamics / domain bridge.
3. **방법별 실제 증거·이력·원천자료 저장:** 외부 증거, 판례, 표준, 명세 버전, 근거 출처 등의 정보는 반드시 보존해야 할 수 있으나 **그것이 곧 속성공리계 primitive coordinate라는 증명은 없다**.
4. **활성화·변화의 동역학:** raw 자료의 보존만으로 다음 시점의 속성 선언/타입 검사를 통과시키거나 전이 규칙을 제공하지 않는다.

### 원천 근거 구분

- [P27 EN 동결 원고](../P27_independent_math_revision/DSD_Property_Axiom_System_EN_P27_REVISED.tex): 제2절 정적 typed property premodel; 미선언/프로필 미제공 종류의 raw 원시좌표는 \`not required\`이며 요구·금지 중 어느 한쪽이 자동으로 정해지지 않는다. PI/PII는 선언 및 프로필 가용 종류에 적용된다.
- [P45 일반 정규화·인수분해](../P45_semantics_predecision_comparison/P45_SEMANTIC_COMPARISON_MATH_AUDIT_KR.md), [P46 공통·분기 결과](../P46_choice_invariants_branching/P46_SHARED_THEOREMS_BRANCH_MONOTONICITY_AUDIT_KR.md), [P47 raw typed 음성대조](../P47_predecision_exit_and_negative_controls/P47_PREDECISION_EXIT_AND_TYPED_RAW_AUDIT_KR.md): 조건부 A/B1/B2의 정보·동형 의미론.
- [Notion DSD 방법군](https://app.notion.com/p/3d281f51e7fa80a890b0ec3ee2397c16): 분석·감사·명세·설계 등 수단의 역할·증거 분리, 필요한 층위만 선택, 외부 분야의 독립 표준과 bridge 유지.
- [Notion DSD 프로젝트 상위](https://app.notion.com/p/3b281f51e7fa812f976eee2ab0eef969): 일반 속성코어는 축/법선 등 특수 기하에 한정되지 않고 typed property core이며 선택적 특수화를 별개로 둔다.
- [Notion 분석론](https://app.notion.com/p/3bb81f51e7fa81258d0ac502f01b2803), [Notion 감사](https://app.notion.com/p/3d181f51e7fa81158053ef995f6fb3d4), [Notion 명세론](https://app.notion.com/p/3d281f51e7fa818e9e41f9f4d10bc4c3), [Notion 설계론](https://app.notion.com/p/3d281f51e7fa8187a406dfe96228b952): 방법별 실제 역할과 분리된 평가기준.
- [Notion 명세론 정지결정](https://app.notion.com/p/3d581f51e7fa8135aa58c4b85b062c3b): 현재의 내부 constructed benchmark 누적 중단. 이번 P48 예시는 **속성공리계 감사용 사고실험**으로, 명세론의 새로운 외부 검증 실적으로 계산하지 않는다.

## 2. A/B1/B2의 구조적 의미와 필요한 외부 층

| 대안 | PAS의 원시자료 | PAS의 strict 비교 | method/evidence 외부 저장의 위치 |
|---|---|---|---|
| A | 활성 인덱스로 제한한 typed 원시코어 | 기존 활성 strict | 출처·이력 등은 PAS와 별도 연계 레저/bridge로 보존 *가능하지만* 연결 규약이 아직 설계되지 않음 |
| B1 | 타입이 맞는 raw 잉여 좌표까지 내부 보존 | \`N(P)\`로 제한한 활성 strict | raw 제시 자체는 내부 보존되지만, 출처·법적 평가·실제 검증자료가 모두 raw family에 포함된다는 근거 없음 |
| B2 | 타입이 맞는 raw 잉여 좌표까지 내부 보존 | raw 인덱스 존재·값을 포함하는 **강화 raw strict** | 출처와 domain standard는 필요하면 별도로 유지; raw strict의 세분화가 실무 우수성이라는 결론 아님 |

**‘완전 기술자에 raw를 기록한다’와 ‘raw까지 동형의 비교조건에 넣는다’는 별개 명세 결정이다.** A가 모든 자료를 삭제해야 한다는 뜻도 아니며, B2가 모든 외부 근거를 이미 담는다는 뜻도 아니다.

## 3. 방법별 역할에 대한 출처 기반 감사

| 방법 / 후속층 | 노션에 선언된 주 역할 | P48에서 확인된 PAS raw 의무 |
|---|---|---|
| **분석론** | 대상 구조의 분해, 상태·관계·적용 구분, 필요 층위 선택 | 활성 구조 분석에 raw 잉여가 언제나 요구된다는 기록 **없음**; 출처/관점 차이는 필요 시 다른 층에서 보존 |
| **감사** | 실제 claim과 근거, 독립 증거, 기준 위반을 별도 판정 | 원천 기록의 보존은 중요하나 그 저장소가 PAS primitive여야 한다는 증명 **없음** |
| **명세론** | typed 요구사항·상태, 부재/미정의/0/적용불가, bridge·lineage 의무 | 상태 구분은 PAS와 접점이 있지만 version/lineage/전이는 별도 method output. PAS 정적 원시좌표로 자동 환원 금지 |
| **설계론** | 목표·제약에서 후보 구조를 구성, 필요한 경우 Property를 활성화 | 설계된 후보의 출처·제약은 기록할 수 있으나 PAS raw 내부 저장 **필수 아님**; 성능 판정은 외부 domain bridge |
| **정적집계/동역학** | 필요할 때 선택적으로 연결되는 층 | 시계열 전이/활성화는 정적 P27의 PI·PII·C1에서 자동 제공되지 않음 |

이는 **현재 Notion 페이지와 동결 P27에서 직접 지지되는 범위**다. 새로 도입한 ‘최소 대표성’ 기준은 P48의 분석적 제안이지 기존 노션의 공식 의사결정 기준을 소급 변경하지 않는다.

## 4. 새 선택-상대적 수학 명제: 과업 관찰족의 정보충분성

고정 적법 Stage-VI/공유 속성 시그니처에서 정규화 \(N:\mathcal B\to\mathcal A\)가 정의되고, 정규 no-surplus 포함 \(i:\mathcal A\to\mathcal B\)가 \(N\circ i=\operatorname{id}_{\mathcal A}\)를 만족한다고 가정한다. 이때 관찰 과업의 집합 \(\mathcal O=\{T_j:\mathcal B\to Y_j\}_{j\in J}\)를 *사전에 명시*한다.

**정리 M48-1(과업별 활성정보 충분성):**
\[
\forall j\in J,\ \exists \overline T_j:\mathcal A\to Y_j,\ T_j=\overline T_j\circ N
\]
가 성립할 필요충분조건은
\[
\forall j\in J,\ \forall P,Q\in\mathcal B,\
N(P)=N(Q)\Longrightarrow T_j(P)=T_j(Q)
\]
이다.

**증명:** ‘⇒’은 합성함수의 성질. ‘⇐’은 각 \(j\)에 대해 \(\overline T_j(a):=T_j(i(a))\)로 정의하면 충분하다. \(N\circ i=\operatorname{id}\)이므로 \(P\)와 \(i(N(P))\)의 \(N\) 상이 같아 각 \(T_j\) 값도 같다. 이는 P45의 개별 관찰 함수 인수분해를 과업별 가족으로 확장한 직접 귀결이다.

**해석:** 어떤 후속 사용이 실제로 활성 status만 읽는다면, 그 과업의 관찰값을 산출하는 데 raw 부가자료가 *수학적으로 필요하지 않다*. 반대로 과업이 raw 좌표의 존재 여부를 읽어야 한다면 그런 관찰은 정규화로 인수분해되지 않는다. 다만 이것이 raw 보관 위치를 **PAS 내부**로 정하는 논증은 아니다. 방법 레저가 외부에 있어도 필요한 관찰을 구현할 수 있으므로 추가 제약이 필요하다.

**M48-2(외부 근거의 자동 포괄을 부정하는 독립 예제):** 같은 raw 모형 \(P\)에 대하여 출처 레저 항목만 \(e_1,e_2\)로 다르게 둔 \((P,e_1),(P,e_2)\)를 생각한다. 수학적으로 PAS의 raw \(P\)가 두 경우 동일하므로 \(\pi_\mathcal B(P,e_i)=P\)만으로는 출처 \(e_i\)를 복원할 수 없다. 따라서 B1/B2의 raw 확장이 실제 외부 서지·판례·표준·시험 provenance 전체를 자동 담는다고 할 수 없다. 단, 새로운 인코딩 \(\mathrm{Enc}:E\to\text{PAS raw}\)을 별도로 정의하는 미래 설계는 논리적으로 금지되지 않는다.

**M48-3(관찰 동치와 raw strict의 차이):** 동일한 활성 정규화에 대해 raw 존재 키만 다른 두 typed 제시는 \(\mathcal O\)가 활성 검사를 포함할 때 관찰 동치지만, 키 존재를 비교하는 B2의 강화 raw strict 아래서는 비동형이다. finer classification 자체가 과업상 오류인 것은 아니고, 과업이 사용하지 않는 구분을 추가로 보존한 것이다.

**M48-4(전이 부재):** raw Xi만 존재하는 미선언 속성 \(q\)를 아무 정식화 없이 선언으로 승격하면 활성에 필수인 Ap/Sat·타입/PI·PII 등의 조건을 충족하지 못할 수 있다. 정적 P27에는 raw 승격 동역학 자체가 없으므로 raw 보존은 미래 활성화의 자동 적법성을 보장하지 않는다.

**M48-5(A와 B1의 과업 관찰 동치):** \(\mathcal O\)가 위 \(N\)을 통해 모두 인수분해하는 범위라면 A의 활성 제시와 B1의 raw 제시는 동일한 \(\mathcal O\) 관찰값을 생성한다. 그렇더라도 raw 보존력·출처·다른 과업에서의 동일성을 주장할 수 없다.

각 명제의 전제는 GitHub \`P48_ROLE_FIT_EVIDENCE_LEDGER.json\`에 별도로 고정하였다.

## 5. 작은 유한 음성대조 및 판별 사례

적법하게 선언된 속성 \(p\)는 한 상속 입력 \(a\)와 필요조건 \(d\), \(\mathrm{Ap}_p=\mathrm{Sat}_{p,d}=\{a\}\), \(\Xi_p=\varnothing\)로 둔다. 같은 활성코어를 가진 raw 제시 \(P,Q\)에서 미선언·프로필 이용가능 \(q\)의 raw \(\mathrm{Ap}_q\) 키가 **P에는 없고 Q에는 명시적으로 공집합**으로 있다고 둔다.

- 활성 정규화 \(N(P)=N(Q)\): PI/PII 및 C1의 활성 상태가 같다.
- **키 존재를 구분하는** typed B2라면 raw 3단계에서 다름; B1의 기존 활성 strict에선 동형.
- **없는 키와 명시적 공집합을 동치로 취급하는 다른 계약**을 선택한다면 그 B2 결과는 달라짐(P47의 조건).
- 원천 자료 \(e_1,e_2\)가 PAS 내 어느 primitive 좌표에도 기록되지 않으면 A/B1/B2 중 어느 선택만으로도 외부 출처를 자동 복원할 수 없음.
- \(q\)를 동역학 없이 선언하면 정상 상태로의 승격이 자동 성립하지 않음.

**검증 지위:** 한 입력의 독립된 constructed/negative model. 실제 명세론 벤치마크·외부 domain test·독립 evaluator 성과로 기록하거나 실무상 우월성을 추정하지 않는다.

## 6. 원고 선택 전에 남긴 6개의 필수 결정 문제

| ID | 선택을 좌우하는 구체적 질문 | 현재 지위 |
|---|---|---|
| Q1 | ‘필수 아님’ 원시 자료를 PAS 적법 premodel 내부에 포함할 것인가 | **미결정** |
| Q2 | raw 저장과 raw strict 동형의 판별을 동시에 요구하는가 | **별개 선택** |
| Q3 | 출처·이력·감사 증거를 PAS primitive로 둘 의무가 있는가, 외부 레저 + bridge로 충분한가 | **과업별 추가 근거 필요** |
| Q4 | raw 인덱스 부재와 명시적 공값을 서로 다른 자료로 볼 것인가 | **미결정** |
| Q5 | 잠재 raw 속성의 활성화·전이 규칙을 정적 P27의 의무라고 볼 수 있는가 | **현행 원고에서 도출되지 않음** |
| Q6 | raw 차이를 감지하는 것이 실제 downstream 목적 관찰인가 | **실제 검증 미확립** |

**잘못된 판정 방지:** A가 ‘데이터를 버리는 이론’이라고 단정하거나 B2를 ‘무조건 더 정밀해서 정답’으로 선언하거나, 명세론의 기존 일시정지 규칙을 새 내부 constructed challenge 때문에 자동으로 해제하지 않는다.

## 7. 최종 판정과 다음 단계

- \`P48_ROLE_FIT=A/B1/B2_CONDITIONAL_BY_TASK\`. DSD 방법군의 여러 역할은 PAS 원시좌표의 필요성을 스스로 결정하지 않는다.
- \`DECISION=DEFERRED\`. 본래 독립 연구자의 의미론적 목적과 명시적 과업 요구를 추가 대조하지 않은 채 임의 채택·흡수·폐기 금지.
- \`S-01/S-03\` 정의·동형·비교범위 미결. \`S-02/S-04\` 수학적 범위는 기존 조건부 논증을 유지하며 **동결 원고는 여전히 개정되지 않음**.
- \`PROPERTY_FPA=OPEN\`. P48의 유한 회귀검사가 전체 무한 집합에 대한 형식 증명이나 외부 평가자 검증을 대신하지 않는다.
- 후속 P49는 **결정 최소 계약과 선택 무관한 절별 개정 준비 명세**를 작성할 수 있다. 결정 자체와 개정 실행을 자동 진행하지 않는다.
- 원고 개정 시 저자 \`Kwon Dominicus\`, 절별 \`% -----\` 주석 경계, 영문·국문 대응 및 새로운 버전 별도 잠금 원칙을 유지하되 **이번 단계는 원고 편집하지 않았다**.

\`\`\`text
AUDIT_ID: PA-P48-20261109-METHOD-ROLE-SEMANTIC-ADEQUACY
SOURCE_INTEGRITY: P27_EN_KR_FROZEN
METHOD_LAYER_SOURCE_COMPARISON: 5
CONDITIONAL_MATH_CLAIMS: 5
DECISION_QUESTIONS: 6
NEW_PRIMITIVE_AXIOM_CONTRADICTION: NOT_ESTABLISHED
DOMAIN_EXPERIMENTS_AND_PRACTICAL_SUPERIORITY: NOT_ESTABLISHED
A_B1_B2_SELECTION: DEFERRED
P27_TEX_PDF_ZENODO_EDITED: NO
PROPERTY_FPA: OPEN
\`\`\`
