# PA-P51 — A-core 상태 좌표·정의된 기록 집합의 타입 오류 재감사
**작성 기준:** 2026-11-10 KST  
**저자:** Kwon Dominicus  
**결정 상태:** A-core ADOPTED; B1/B2 UNSELECTED_EXTENSIONS  
**논문 상태:** P51 EN WORKING; P50/P27 preserved; EN/KR parity OPEN; FPA OPEN

## 1. 감사 목표
P50에서 A 활성 속성 중심의 원시 인덱스 \(\mathcal K_A\)를 선택한 이후, P27에서 승계된 §3/§5의 **파생 좌표가 정말 정의된 타입 위에서만 사용되는지** 독립 점검한다. 오류 발견·시정·재발 방지가 감사의 목적이며, 감사 데이터는 DSD 방법군에 나중에 연결 가능한 별도 증거이다. 수학적 공리의 추가 및 raw 보존 정책 변경과는 분리한다.

## 2. 확인된 두 문제

### F51-01 — 정의되지 않은 정의역을 참조할 위험 (실제 수학적 타입 오류)
P50 §3.3에서 \(D_{A,\varpi}=\operatorname{Dom}\Xi_{A,\varpi}\)는 \(\varpi\in\mathcal K_A\)인 경우에만 정의된다. 그런데 같은 절의 "Defined property records"는 \(\varpi\in\Pi_A\)를 사용했다. \(\varpi\in\Pi_A\setminus\mathcal K_A\)인 *선언되었지만 프로필 이용 불가능*한 종류가 허용되므로 \(D_{A,\varpi}\)와 \(\Xi_{A,\varpi}\)가 미정의인 인덱스를 참조한다.

**유한 반례/증인:** 후보 종류 \(\{\varpi_0,\varpi_1\}\), 선언 종류 \(\Pi_A=\{\varpi_0,\varpi_1\}\), \(\varpi_0\)의 프로필만 이용 가능하게 하자. 그러면 \(\mathcal K_A=\{\varpi_0\}\). A-core 정의에 따라 \(\varpi_1\)의 할당좌표는 없다. 기존 set-builder의 \(\varpi\in\Pi_A\) 범위에서 \(\varpi=\varpi_1\)을 대입한 \(x\in D_{A,\varpi_1}\)은 원문 내 정의되지 않았다. 이는 단순히 결과가 공집합이라는 주장으로 덮을 수 없는 **부분적인 수학 표현의 정의역 문제**이다.

**수정:** §3.3 기록 집합의 인덱스를 \(\varpi\in\mathcal K_A\)로 수정. 전칭 원시 family의 허용 범위나 PI/PII는 변경하지 않음.

### F51-02 — §5에서 사용하는 상태 좌표의 명시적 타입 누락 (정의 명확성 오류)
P50 §3.3은 상태의 경우를 서술하지만 §5 complete descriptor의 \(\{\operatorname{Stat}_{A,\varpi}\}\)가 정확히 어떤 *함수/정의역/공역*을 뜻하는지 선언하지 않았다. 특히 "undeclared"는 입력 \(x\)가 아닌 종류 \(\varpi\)의 상태이고, "inapplicable" 등은 활성 종류의 입력 상태로 층위가 다르다.

**수정:** 두 상태를 구분하여 정의적 자료로 추가하였다.

- 종류 상태 \(\operatorname{Stat}_A^{\rm kind}:\widehat\Pi_L\to\{\mathrm{undeclared},\mathrm{profile\!-\!unavailable},\mathrm{active}\}\).
- 활성 입력 상태 \(\operatorname{Stat}_{A,\varpi}:X_{A,\varpi}\to\mathcal V_{\rm stat}\), \(\varpi\in\mathcal K_A\). 입력 상태는 inapplicable, prerequisite-unsatisfied, applicable-undefined, defined, defined-zero, defined-nonzero 중 해당되는 단 하나를 택한다.
- PI/PII에 의해 정의된 값의 입력은 적용가능·선행조건충족이므로 위 분할은 상호배타·전부포괄. zero-bearing 종류는 정의된 값이 실제 영인지에 따라 두 하위 상태로 분할된다.
- §3.4의 C1 및 primitive reduction, §5 기술자, §6 엄격 동형 보존 증명, Appendix A를 모두 동일한 새 타입 표기로 정합화.
- **새 원시 공리 수는 0**. 상태 자료는 원시 data가 아니라 기존 data의 함수이다.

## 3. 수학적 영향 및 조건부 논증

**M51-A — totality/disjointness of input status:** 
For each active \(\varpi\), the domain \(D\subseteq\operatorname{Ap}\cap\operatorname{DepSat}\).
Given \(x\in X_{A,\varpi}\), either \(x\notin\operatorname{Ap}\), or \(x\in\operatorname{Ap}\setminus\operatorname{DepSat}\), or \(x\in\operatorname{Ap}\cap\operatorname{DepSat}\setminus D\), or \(x\in D\). These are disjoint and exhaustive. Values in \(D\) split into defined/nonzero for zero-bearing kinds. Thus \(\operatorname{Stat}_{A,\varpi}\) is a unique set-valued typed function, fixed by A-core primitive data.

**M51-B — record-set well-definedness:** 
\(\operatorname{PropRec}_A=\{(\varpi,x,\Xi_{A,\varpi}(x)):\varpi\in\mathcal K_A,\ x\in D_{A,\varpi}\}\).
Since \(\mathcal K_A\) is a set and each domain and partial map is typed, the record set exists by set construction in ZFC; no out-of-domain kind appears.

**M51-C — inverse closure and strict invariance are conditional:** The typed status functions are determined uniquely by existing primitive coordinates; therefore the revised C1 can still recompute them from the reduct, and any strict map that preserves and reflects declared/available kinds, applicability, prerequisite satisfaction, assignment-domain membership, and values transports them uniquely. This removes the type gap but is not an external formalization or an unconditional validation of every theorem.

## 4. §11 통합 정리 13항의 추적 판정

| 항 | 출처 및 P51 판정 | 추가 의무 |
| --- | --- | --- |
| (1) | §2.2 유한 타입 프로필 정의 | 외부 해석과 구분 |
| (2) | §3.1–3.2 PI/PII | 비함의 역방향은 추가하지 않음 |
| (3) | §4.1–4.3 한 입력 반례 | 존재는 적절한 시그니처에서, 고정 임의 시그니처에서 보장 아님 |
| (4) | §3.3 상태 분할 | P51 함수 타입 시정, 후속 전체 증명 재검토 |
| (5) | §3.4 C1 역법칙 | P51 파생자료 추가에 맞춰 타입 정합 수정 |
| (6) | §6.1–6.2 사상·embedding·preorder | 전체 사상 증명은 독립 재감사 필요 |
| (7) | §6.3 strict 동형 | A-core 활성 가족만 비교, 전체 증명 독립 재감사 필요 |
| (8) | §6.4 선택적 representation | 공통 representation signature 고정 |
| (9) | §7 I1–I5, I4=I5 | P51 파생 상태 명확화, 유한 검산 별도 |
| (10) | §8.1–8.2 trivial + TFI 유한 실현 | P50 typing 전제를 유지 |
| (11) | §8.3 유한 first-branch 증인 | 적절한 공유 시그니처에서의 존재 |
| (12) | §9.1 요약 충돌 | 정당한 zero-bearing/available 증인 클래스에 한정 |
| (13) | §2 Stage VI 고정, §10 후속층 경계 | 역학·출처 ledger는 외부 |

**판정 주의:** 위 표는 13개 주장과 그 근거 절의 대응 및 확인된 타입 오류의 파급 범위를 재점검한 것이다. 13개 정리의 완전한 형식증명 인증을 뜻하지 않는다.

## 5. 재현 검증

### 소스 구조 점검
GitHub에서 P51 소스를 재조회하여 7개 체크(환경 짝의 균형, 모든 \ref 라벨 정의됨, 라벨 중복 없음, PI/PII 원시 공리 2개 유지, 종류 상태의 함수 타입 존재, 기록집합의 활성 인덱스, 전체 파일 재조회)를 모두 통과. 정의 24쌍, 정리 10쌍, 증명 17쌍, 라벨 37개/참조 32회.

### 유한 범위 정확 판별
원소 2개인 고정 보조 담지자, 원시 속성 1종, 선행조건 1개, 값 공간 \(\{0,1\}\)의 유효 A-core 제시를 직접 열거: **36개**.
- 서로 다른 순서쌍 **1,296개**에서 2개 담지자 전단사(항등/교환)를 모두 조사하여 \(I_4=I_5\), 비동형 첫 분기, 대칭성을 확인.
- 순서삼중항 **46,656개**에서 유한 strict 동형의 추이성 대조.
- 엄격 동형 가능 순서쌍 66개; 3단계에서 처음 분기 1092쌍, 4단계에서 처음 분기 138쌍. 합계 1296.
- 선언되었으나 프로필 이용 불가능한 종류는 원시좌표 인덱스 밖이며, 그 종류의 기록집합 원소를 구성하지 않도록 명세함.
- **한계:** 이 수치는 위의 제한된 유한 정의에 대해서만 전수이며 모든 ZFC 모델의 증명/성공률을 뜻하지 않는다. 이번 단계는 새 Python 파일·GitHub Actions CI·전체 LaTeX 원고 빌드를 실행하지 않았다.

## 6. 원본 보존, 재발 방지 및 다음 관문
- [x] P27 동결 원본/P50 작업본 보존, P51 별도 작업본 생성.
- [x] 상태를 종류 상태와 활성 입력 상태로 구분하여 함수를 명시.
- [x] 기록집합의 조건 \(\varpi\in\mathcal K_A\) 명시.
- [x] C1·기술자·엄격 동형·부록까지 동시 전파.
- [x] 정적 문자열·유한 예제 감사와 실제 정리 증명을 구분.
- [ ] P51 전체 원고의 독립 수학 재감사 및 LaTeX 빌드.
- [ ] P51 국문 대응본 작성 및 EN/KR 의미 동치 감사.
- [ ] S-01–S-04 및 제11절의 모든 일반 집합론적 명제에 대한 외부 독립 검증.
- [ ] 원문 개정 완료 이후에만 최종 공개물 교체 고려.

**상태:** P51_TYPED_DERIVED_COORDINATES_REPAIRED / WORKING_ONLY / FPA_OPEN.
**근거:** [P50 영문 작업본](../P50_A_core_adoption_and_revision/DSD_Property_Axiom_System_EN_P50_A_WORKING.tex) · [P51 개정본](./DSD_Property_Axiom_System_EN_P51_A_WORKING.tex) · [P50 결정 기록](../P50_A_core_adoption_and_revision/P50_A_DECISION_AUDIT_AND_PREVENTION_KR.md).
