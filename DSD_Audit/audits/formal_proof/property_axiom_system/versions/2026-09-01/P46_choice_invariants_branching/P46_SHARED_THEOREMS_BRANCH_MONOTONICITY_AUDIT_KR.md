# PA-P46 — 속성공리계 A/B1/B2 공통 정리·의미론 분기 정리·최초 분기 순서 감사

**실행 기준일:** 2026-11-04 KST. **저자:** Kwon Dominicus.
**잠금:** 속성공리계 P27 EN SHA256 \`51c194ec33f802a2061b68b3521fdb831f0f754a0386fa72f8e89a39efff7bdb\`; KR SHA256 \`a643ea619f9594142bfc09b9f486c948cf0a85679a3b2a8a43bc731a1e108fbb\`. 영·국문 LaTeX·PDF·Zenodo 원고 수정하지 않음. 의미론 선택·병합·폐기 없음.
**근거:** [P38 raw/active 단계비교](../P38_a_b1_b2_stage_strict/P38_A_B1_B2_STAGE_STRICT_C1_GENERAL_AUDIT_KR.md), [P42 20+13 의존성](../P42_consolidated_premises_countermodels_revision_spec/P42_CLAIMS_PREMISES_COUNTERMODELS_REVISION_SPEC_KR.md), [P44 선택 전 충분성](../P44_predecision_readiness/P44_PREDECISION_READINESS_AND_EVIDENCE_AUDIT_KR.md), [P45 정규화·인수분해](../P45_semantics_predecision_comparison/P45_SEMANTIC_COMPARISON_MATH_AUDIT_KR.md).

## 1. 적용 범위와 형식적 비교 지반

적법한 Stage-VI 형성 기록과 하나의 공유 속성 시그니처를 고정한다. 모형들의 기저 운반체·후보 집합·원시 가족은 집합 크기로 둔다. \`A\`는 정확히 활성 인덱스에 정의된 적법 원시자료, \`B\`는 원시자료의 **타입이 합당한 추가 raw 인덱스**를 보존하는 가상 확장 명세다. \`B\`가 이미 P27에 확정 채택되었다는 뜻은 아니다. 양쪽 모두 동일한 활성 코어를 얻는 제한 \(N:B\to A\)과 canonical no-surplus 포함 \(i:A\to B\)를 허용한다고 가정한다.

- \`I_k^act(P,Q)\`: 선언/이용가능한 활성 좌표의 제6·7절 보존 조건을 단계별로 적용한다. B1은 이 관계를 사용하고 A에서는 raw와 활성 자료가 동일하다.
- \`I_k^raw(P,Q)\`: 동일한 후보 운반체 전단사 집합으로 시작하여, 3단계에서 **추가 raw Ap/Sat 가족의 인덱스 존재와 원소**까지, 4단계에서 **raw Xi의 존재와 부분함수 그래프**까지 보존한다. B2는 이 관계와 강화 raw strict 동형을 사용해야 한다.
- C1은 활성 자료의 함수로 파생되며, \`Comp_raw(P)=(P,Derived(N(P)))\`로 raw 전체를 원시좌표에 유지한다. \`Comp_bad(P)=(N(P),Derived(N(P)))\`라는 무통지 정규화는 다른 연산이다.
- 각 \`I_k\`는 **하나의 고정 후보 전단사 가족 집합에서 조건을 추가해 얻는 부분집합**이므로 동일 대상을 비교해야 아래 정리가 성립한다. 서로 다른 시그니처나 후보군을 임의로 혼용하면 적용 불가.

## 2. 선택 이전에도 보존되는 7개 결과

| ID | 성립 가능한 결과 | 명시적 전제·제약 |
|---|---|---|
| C01 | PI·PII 활성 포함 공리 | 타입이 적법하고 선언·프로필이 제공된 종류에 대해 적용. B의 비활성 raw 좌표에 새 공리를 **몰래** 확대하지 않음 |
| C02 | C1 파생좌표의 결정성 | C1에 사용되는 모든 활성 원시좌표가 보존된 경우 |
| C03 | \`Red(Comp(P))=P\`, \`Comp(Red(F))=F\` | A는 전체 활성 원시자료를, B는 전체 raw 원시자료를 손실 없이 보존 |
| C04 | typed finite presentation의 유일한 C1 완성 | \`T\`(타입 적법) + \`F\`(유한) + \`I\`(활성 PI/PII 포함 조건); B의 잉여 raw가 허용 타입 조건을 충족 |
| C05 | \(I_4=I_5\) | raw와 active 중 어느 의미론이든 단계4에서 **C1이 사용하는 좌표 전체**를 검사하고 단계5에는 C1 파생값만 추가 |
| C06 | 기존 typed 존재 증인의 유효성 | B가 no-surplus canonical 제시 \`i(A)\`를 허용할 때; 임의 고정 시그니처의 증인 존재는 주장하지 않음 |
| C07 | 고정 형성 기반 인터페이스 | 동일한 Stage VI 및 시그니처에 상대적이며 단계 번호는 물리적 시간 좌표가 아님 |

이 목록은 “세 대안이 논문 원문에서 이미 확정·완전 증명되었다”는 뜻이 아니다. **선택별 필요한 명세가 충족될 경우 동일한 핵심 결론을 보존할 수 있다는 조건부 비교**이다.

## 3. 선택에 따라 달라지는 여섯 가지

| 항목 | A | B1 | B2 |
|---|---|---|---|
| V01 적법 원시 가족 | 활성 인덱스만 | 타입에 맞는 raw 잉여 허용 | 타입에 맞는 raw 잉여 허용 |
| V02 완전 기술자 | 활성 원시자료 | raw 보존/활성 동형과 구별 | raw 보존/raw 강화 동형 비교 |
| V03 strict | 기존 활성 strict | 기존 활성 strict (N을 통한 비교) | 별도 raw strict 필요 |
| V04 \`I_k\` | 활성 단계별 조건 | \`I_k^{act}(N(P),N(Q))\` | raw 전체 단계별 조건 |
| V05 최초 분기 불변량 | 활성 strict에 상대 | 활성 strict에 상대 | raw strict에 상대 |
| V06 §11(5–9) | 기존 활성 문구로 정합 가능 | raw 기술자와 활성 동형의 차이를 별도 명시 | 관련 사상·strict·단계/분기 정리 재정식화 필요 |

**A의 적은 수정량은 B의 정보보존적 가치를 부정하는 근거가 아니며, B2의 더 자세한 판별은 이를 반드시 원시모형에 포함해야 한다는 증명이 아니다.**

## 4. P46 신규 일반 집합론 정리 — 비교의 정교화와 분기 순서

**T1. 단계 비교 후보의 포함.** 같은 후보 운반체 전단사 \(\operatorname{Bij}_T(P,Q)\)에서 시작하고 raw 비교가 활성 조건을 빠뜨리지 않고 추가 raw 조건만 강화한다면
\[
I_k^{raw}(P,Q)\subseteq I_k^{act}(P,Q),\qquad k=1,2,3,4,5.
\]
1·2단계는 같고 3·4단계는 추가 조건으로 강화한다. 5단계는 동일한 C1 파생 좌표만 요구하여 각 비교에 대해 4단계와 같다. 모든 운반체가 무한이어도 이 포함은 집합의 조건 강화로 성립한다.

**T2. 분기 순서 정리.** 원문 \`b_prop\`는 엄격 비동형에서만 정의되어 있으므로, 다음 감사용 확장 지수를 별도로 둔다.
\[
\beta_q(P,Q)=
\begin{cases}
\min\{k\in\{1,2,3,4\}:I_k^q(P,Q)=\varnothing\},&I_4^q(P,Q)=\varnothing,\\
\infty,&I_4^q(P,Q)\ne\varnothing.
\end{cases}
\]
(값의 순서는 \(1<2<3<4<\infty\).)
T1과 단계집합의 중첩으로
\[
\boxed{\beta_{raw}(P,Q)\le\beta_{act}(P,Q)}.
\]
**증명:** \(I_k^{act}=\varnothing\)이면 포함에 따라 \(I_k^{raw}=\varnothing\). 따라서 활성 비교에서 공집합이 처음 나타나는 지점보다 늦게 raw 비교의 공집합이 처음 나타날 수 없다. 활성 비교에서 공집합이 전혀 없을 때는 \(\beta_{act}=\infty\)로 정의해 부등식을 유지한다.

이는 raw 분기가 **더 일찍 나타날 수도 있다는 의미**일 뿐, B2가 본질적으로 옳다는 가치 판단이 아니다. \(\beta\)는 감사용 확장이지 기존 P27의 \`b_prop\`에 아직 추가하지 않는다.

**T3. 동형류의 정련(refinement).** \(\cong_{raw}\)가 \(\cong_{act}\)의 모든 보존조건을 포함하면 \(\cong_{raw}\Rightarrow\cong_{act}\)이며 역은 일반적으로 거짓이다. 집합 크기의 클래스 가족에서 \(\mathcal B/{\cong_{raw}}\to\mathcal A/{\cong_{act}}\)를 \([P]_{raw}\mapsto[N(P)]_{act}\)로 정의하면 이 사상은 canonical no-surplus 포함 덕분에 전사다. 하지만 미선언 종류의 typed raw Ap 인덱스 차이가 있는 한 활성동형류 하나에 서로 다른 raw동형류가 들어갈 수 있어 일반적으로 단사가 아니다. 여기서 **동형류**는 P45의 raw 문자 동일성 몫과 구분된다.

**T4. 기존 strict에 대해 raw 첫 분기는 불변량이 아님.** 활성 동일 코어인데 미선언 raw Ap 또는 raw Xi만 다른 두 제시의 \(\beta_{act}=\infty\)인 반면 \(\beta_{raw}\in\{3,4\}\). 기존 strict로 양끝 모형을 재표시해도 raw 비교에서는 분기가 바뀔 수 있다. raw 최초 분기 불변성은 강화 raw strict에 상대적이다.

**T5. S-02/S-04는 선택을 보류해도 분리 가능.** T+F+I 완성 정리와 모든 고정 시그니처의 강한 존재 주장에 대한 반례는 활성 구조에 관한 것이고 canonical no-surplus 제시는 세 대안에서 허용된다고 가정한다. 그러나 *A의 고정 시그니처 자원조건을 B2의 추가 raw 분기에 대한 필요충분조건으로 무단 전파하면 안 된다.* B2는 잉여 raw만으로도 3·4단계에서 분기할 수 있기 때문이다.

## 5. 독립 유한 재현 (일반 정리와 구분)

고정 상속 운반체의 원소가 하나이고 사상은 항등인 예제로, 활성 코어 4가지와 미선언 후보 q의 원시 Ap 인덱스 3상태(없음/공집합/1원소), 원시 Xi 인덱스 3상태(없음/공함수/값 0 정의)를 결합한다. 그 결과 원시 제시 36개, 순서쌍 \(36^2=1,296\)개.

| \(\beta_{act}\) | \(\beta_{raw}\) | 모형 순서쌍 |
|---|---|---:|
| 2 | 2 | 486 |
| 3 | 3 | 324 |
| 4 | 4 | 54 |
| 4 | 3 | 108 |
| ∞ | ∞ | 36 |
| ∞ | 3 | 216 |
| ∞ | 4 | 72 |
| **전체** | | **1,296** |

이 검사에서는 \(\beta_{raw}<\beta_{act}\)인 순서쌍이 **396개**이며, \(\beta_{raw}>\beta_{act}\)인 것은 **0개**다. 활성동형이지만 raw동형이 아닌 쌍 288개, raw동형류 36개와 활성동형류 4개가 나타난다. 숫자는 **한 개의 유한 타입 모형 예제**에 해당하며 대안들에 대한 통계적 승률이나 미래 DSD 방법군의 일반 성질이 아니다.

또한 raw 차이만으로 \(\beta_{raw}=3\)이면서 활성값 할당 차이로 \(\beta_{act}=4\)인 순서쌍 108개가 있다. 이는 raw 비교가 활성 비교의 분기를 **더 일찍 발생**시킨다는 T2의 엄격 부등 사례이다.

## 6. 현재 FPA 조사 종료 관문

| 종결 의무 | P46 판정 |
|---|---|
| P29–P45의 명시된 S01..04 추적 | 조건부 증명·반례·영/국문 원고 경계 연결 |
| 공통 정리·분기 정리 분리 | **본 P46에서 수행** |
| A/B1/B2의 실제 채택 목적·정의 | **아직 결정하지 않음** |
| S01→S03의 원고·동형·비교집합 일치 | **미수정·OPEN** |
| S02의 typed finite 명시와 S04 양화 문구 | **미수정·OPEN** |
| 최종 EN/KR 원고 개정·전체 자연어 동치 재검증 | **미수행** |
| 공리계 전체의 외부 독립 수학 검증·FPA CLOSED | **미확립·OPEN** |

**판정:** \`PREDECISION_TRACKED_MATHEMATICAL_OBLIGATIONS=SCOPED\`. 이는 기록된 S-01~S-04 및 주된 양화·타입 의무의 **의미론 선택 전 공통 감사가 정리되었다는 제한적 판정**이지 논문 전체가 완전 검증되었다는 선언이 아니다.

후속 P47에서는 **누락 가능성·최종 선택 전 감사의 종료 가능성**을 비순환적인 문서 증거로 다시 점검하고, 사용자에게 A/B/B1/B2의 조기 채택을 요구하지 않는다. 이후 선택을 하더라도 원고를 새 버전으로 절 단위로 수정하고 사후 재감사해야 한다. 원고 저자 \`Kwon Dominicus\` 및 LaTeX 절 경계 \`% -----\` 규칙 준수.

\`\`\`text
AUDIT_ID: PA-P46-20261104-CHOICE-INVARIANT-BRANCHING-AUDIT
COMMON_RESULTS: 7
INTERPRETATION_DEPENDENT: 6
CONDITIONAL_GENERAL_THEOREMS: 5
RAW_BETA_LE_ACTIVE_BETA: PROVED_UNDER_MATCHING_CANDIDATE_CONTRACT
FINITE_PAIRS: 1296
FINITE_RAW_EARLIER: 396
SOURCE_P27_EN_KR_PDF_ZENODO_EDITED: NO
A_B1_B2_SELECTED: NONE
FULL_PROPERTY_FPA: OPEN
EXTERNAL_INDEPENDENT_VALIDATION: NOT_ESTABLISHED
\`\`\`
