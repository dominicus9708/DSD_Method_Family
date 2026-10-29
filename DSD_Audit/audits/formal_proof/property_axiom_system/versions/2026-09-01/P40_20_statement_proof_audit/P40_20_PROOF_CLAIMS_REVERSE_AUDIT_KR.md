# PA-P40 — 속성공리계 P27 동결본 20개 증명대상 정리별 역감사

**날짜:** 2026-10-29 KST. **저자:** Kwon Dominicus.
**기준 소스:** EN SHA256 `51c194ec33f802a2061b68b3521fdb831f0f754a0386fa72f8e89a39efff7bdb`, KR SHA256 `a643ea619f9594142bfc09b9f486c948cf0a85679a3b2a8a43bc731a1e108fbb`.
**원고 동결:** P27 영문·국문 LaTeX/PDF와 Zenodo 미변경. A/B 의미론 선택 보류.
**선행 증거:** [P39 전역 56항 대장](../P39_global_56_item_dependency/P39_GLOBAL_56_ITEM_DEPENDENCY_AUDIT_KR.md), [P38 A/B1/B2](../P38_a_b1_b2_stage_strict/P38_A_B1_B2_STAGE_STRICT_C1_GENERAL_AUDIT_KR.md), [P37 S02·S04](../P37_s02_s04_fixed_signature/P37_S02_S04_GENERAL_THEOREM_SCOPE_AUDIT_KR.md).

## 1. 독립 증명 대상과 증명문 존재

- 번호 항목 56개 중 **수학적 증명 대상 20개**: 정리 10·명제 7·따름정리 3.
- **17개**에는 원문상 연속된 명시적인 `proof` 환경이 있고, 나머지 **3개**는 4.6·7.3·8.8의 직접 따름정리다. 이들에 proof 환경이 없다는 사실만으로 결함이라고 판정하지 않는다.
- 아래의 `GENERAL_ARGUMENT_SUPPORTED`는 선언된 배경에 대한 수학적 논증 지지이지 Lean/Coq 등에서 모든 항목을 형식적으로 증명했다는 뜻이 아니다.
- 제11절 11.1의 13개 세부 결론은 **하나의 상위 정리의 다중 주장**이며 번호가 부여된 별도 13개 정리가 아니다. P31/P35/P39의 각 결론 의존성을 유지한다.

## 2. 20개 대상별 증명 상태·의존 증거

| 번호 | 유형 | 증명 형식 | 연계 | 감사 분류 |
|---|---|---|---|---|
| 3.7 | theorem | 본문 증명 | S-01 | CONDITIONAL_GENERAL_PROOF |
| 4.3 | theorem | 본문 증명 | S-04 | WITNESS_PROVED_SCOPE_OPEN |
| 4.4 | proposition | 본문 증명 | S-04 | WITNESS_PROVED_SCOPE_OPEN |
| 4.5 | proposition | 본문 증명 | — | GENERAL_WITNESS_SUPPORTED |
| 4.6 | corollary | 선행 결과 의존 | — | DIRECT_COROLLARY_SUPPORTED |
| 5.5 | proposition | 본문 증명 | — | GENERAL_ARGUMENT_SUPPORTED |
| 6.2 | proposition | 본문 증명 | S-01 | GENERAL_CONDITIONAL_S01 |
| 6.4 | proposition | 본문 증명 | S-01 | GENERAL_CONDITIONAL_S01 |
| 6.6 | theorem | 본문 증명 | S-01 | GENERAL_CONDITIONAL_S01 |
| 6.8 | theorem | 본문 증명 | S-01 | GENERAL_CONDITIONAL_S01 |
| 6.9 | proposition | 본문 증명 | S-01 | GENERAL_CONDITIONAL_S01 |
| 6.11 | theorem | 본문 증명 | — | GENERAL_ARGUMENT_SUPPORTED |
| 7.2 | proposition | 본문 증명 | S-01, S-03 | GENERAL_CONDITIONAL_S01_S03 |
| 7.3 | corollary | 선행 결과 의존 | S-01, S-03 | DIRECT_COROLLARY_CONDITIONAL |
| 7.5 | theorem | 본문 증명 | S-01, S-03 | GENERAL_CONDITIONAL_S01_S03 |
| 8.1 | theorem | 본문 증명 | — | GENERAL_FIXED_BASE_SUPPORTED |
| 8.4 | theorem | 본문 증명 | S-02, S-01 | TYPING_PREMISE_SCOPE_OPEN |
| 8.8 | corollary | 선행 결과 의존 | S-01, S-03 | DIRECT_COROLLARY_CONDITIONAL |
| 9.2 | theorem | 본문 증명 | S-04 | EXISTENTIAL_WITNESS_SUPPORTED |
| 11.1 | theorem | 본문 증명 | S-01, S-02, S-03, S-04 | GLOBAL_SCOPE_AND_SEMANTICS_OPEN |

각 행의 구체적 근거, 원문의 직접 참조 및 남은 의무는 동봉한 `P40_20_CLAIMS_LEDGER.json`의 `assessments` 배열에 기록했다. `SOURCE_SCOPE_OPEN`인 문장을 PASS로 올려 세지 않는다.

## 3. 직접 증명과 추가 독립 검증

### (a) 4.5 → 4.6: 두 역포함 부정과 비어 있지 않은 applicable-undefined

공유 시그니처 `p:(u)`, `X(u)={a}`, `δ(p)={d}`를 두고 `Π={p}`, `Ap={a}`, `Sat_d={a}`, `Xi=∅`로 둔다. 원시공리 PI/PII가 성립하고 `Ap⊄Dom Xi`, `DepSat⊄Dom Xi`. C1 완성에서 입력 a는 **적용 가능·전제 충족·값 미정의** 상태다. 따라서 4.5의 존재 반례는 4.6의 직접 증인이 된다. 단 여기서 보이는 것은 존재 정리이며 모든 고정 시그니처에 해당 상태가 실현된다는 뜻은 아니다.

### (b) 9.2의 증인이 실제 8.7 및 9.1의 적용조건을 만족하는가?

고정 시그니처에 두 zero-bearing 단항 속성 p,q와 공유 입력 운반체 X(u)={a,b}, 값공역 {0,1}, 두 속성 모두 선언·완전 적용가능·전제 없음. A는 p=(0,1), q=(0,1); B는 p=(0,1), q=(1,0) 값을 부여한다. 요약은 둘 다 `(2,{(p,2,1,1),(q,2,1,1)})`로 같다. p 값을 보존하는 유일한 입력 전단사는 항등이므로 q의 값이 일치할 수 없어서 strict 동형은 없다. 모든 할당이 타입 적법하고 PI/PII를 만족한다. 이 **특정 시그니처에서의 존재 증인**은 원문 9.2의 근거를 충족한다. 고정된 모든 시그니처에서 이런 반모형이 존재한다고 확대하지 않는다.

### (c) 7.3·8.8: 명시 proof 생략은 선행정리 의존

7.3은 7.2의 `I4=I5`와 Def6의 엄격 동형-Stage4 대응을 필요로 한다. 8.8은 7.2의 등식만 있으면 직접 성립한다. A/B1에서는 P33·P38의 활성 정식화로 지지되고 B2 raw 전체를 고른다면 **강화 raw 엄격 동형과 비교하는 별도 정리**여야 한다. 따라서 `NO_EXPLICIT_PROOF`를 자동 `PROOF_GAP`으로 변환하면 안 되지만, **선행정리가 미확정이면 따름정리의 최종 판정도 OPEN**이다.

## 4. 원문상 가장 중요한 종결 미해결

1. **4.3·4.4와 11.1(3):** 원문 §4는 공통 **증인 시그니처**에 대한 typed counterpremodel로 비도출을 보이지만, 전체 고정 시그니처 전칭으로 해석하면 `Πhat=∅` 반례. P37 필요충분조건 보존.
2. **8.4와 11.1(10):** 타입 적법성 `T` 없이 `Dom Xi⊆Ap∩DepSat`만 사용하면 원시코어 존재를 추론할 수 없음. P29·P37 구분 유지.
3. **6.8·7.2·7.3·7.5·8.8:** A/B1 활성 동형과 B2 raw 전체 비교의 선택·동치 대응 경계. P36·P38 결과 유지.
4. **9.2와 11.1(12):** 9.2는 **존재 명제**로서는 유효하며 P34의 더 작은 증인도 있음. 그러나 11.1의 임의 고정 시그니처 전칭판으로 끌어올리는 것은 잘못.
5. **11.1 전체:** 개별 항목을 검토한 결과를 통합 상위 정리에 자동 전파하지 않는다. 제11절 13개 결론의 1:1 의존성 최종 재감사 필요.

## 5. 종결 판정

- `P40_20_CLAIMS_SCOPED=20/20` (증명 의무 범주 분류).
- `EXPLICIT_PROOF_ENVIRONMENTS=17/20`, `DIRECT_COROLLARIES=3`.
- `MATHEMATICAL_VERDICT=MIXED_SUPPORTED_GENERAL_ARGUMENTS_AND_SCOPE_GAPS`.
- `DSD_AUDIT_VERDICT=PASS_WITH_REFINEMENT`.
- `S-01=DEFERRED`, `S-02/S-03/S-04=OPEN_FOR_FINAL_SOURCE_ALIGNMENT`.
- `P27_EN_KR_SOURCE_EDITED=NO`, `WHOLE_PROPERTY_FPA=OPEN`, `INDEPENDENT_EXTERNAL_VALIDATION=not_established`.

후속 P41은 각 증명 간 **의존 사슬의 순환성·타입·양화**를 다시 감사하고, 추가 보강 없이 전체 일괄 개정 후보 대장으로 넘어갈 수 있을지 평가한다. 
