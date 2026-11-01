# PA-P42 — P27 동결본 20개 증명대상·제11절 13결론의 전제/반례/일괄개정 보류 명세

**감사일:** 2026-11-02 (Asia/Seoul). **원고 저자:** Kwon Dominicus.
**감사 정본:** P27 EN SHA256 `51c194ec33f802a2061b68b3521fdb831f0f754a0386fa72f8e89a39efff7bdb`; KR SHA256 `a643ea619f9594142bfc09b9f486c948cf0a85679a3b2a8a43bc731a1e108fbb`. P27 EN/KR LaTeX·PDF·Zenodo **동결**. 원시공리 PI/PII·C1·정의 원고는 전혀 편집하지 않음.
**선행:** [P40 20항](../P40_20_statement_proof_audit/P40_20_PROOF_CLAIMS_REVERSE_AUDIT_KR.md), [P41 97개 의존관계](../P41_dependency_chain_and_scope/P41_PROOF_CHAIN_CYCLE_AND_SCOPE_AUDIT_KR.md), [P37 S02/S04](../P37_s02_s04_fixed_signature/P37_S02_S04_GENERAL_THEOREM_SCOPE_AUDIT_KR.md), [P38 A/B1/B2](../P38_a_b1_b2_stage_strict/P38_A_B1_B2_STAGE_STRICT_C1_GENERAL_AUDIT_KR.md).
**명시:** 보고서는 향후 영·국문 절별 일괄 개정을 위한 `명세 초안`이며, 채택된 새 공리·증명 완료 또는 완료된 논문 개정이 아님. A/B1/B2 선택 없음.

## 1. P40 20개 증명 대상: 원문 주장, 적용범위, 수정 보류 항목

아래 `audit_status`는 정의적 지지, 특정 시그니처 증인, 조건부 일반 증명, 강한 전칭판 반증을 구분한다. 정리10·명제7·따름정리3이다. 따름정리4.6/7.3/8.8에 별도 proof 환경이 없는 것만으로 결함이라는 판정을 내리지 않는다.

| 항목 | 유형 | P40의 논증 판정 | 연계 또는 신설 전파 | **후속 원고 수정이 필요할 경우의 검토 사항(미적용)** |
|---|---|---|---|---|
| 3.7 | theorem | CONDITIONAL_GENERAL_PROOF | S-01 | 정규화 N과 완성 Comp 구별 |
| 4.3 | theorem | WITNESS_PROVED_SCOPE_OPEN | S-04 | 고정 시그니처 vs 전체 계열의 양화 구분 |
| 4.4 | proposition | WITNESS_PROVED_SCOPE_OPEN | S-04 | 정리4.3 증인 범위 승계 |
| 4.5 | proposition | GENERAL_WITNESS_SUPPORTED | S-04_LOCAL_EXISTENCE_SCOPE | §4.1에서 고정한 비공집합 입력·속성 증인 시그니처에 상대적인 존재/비함의로 명확화. 모든 고정 시그니처에서 개별 증인 존재를 주장하지 말 것. |
| 4.6 | corollary | DIRECT_COROLLARY_SUPPORTED | S-04_LOCAL_EXISTENCE_SCOPE | §4.1에서 고정한 비공집합 입력·속성 증인 시그니처에 상대적인 존재/비함의로 명확화. 모든 고정 시그니처에서 개별 증인 존재를 주장하지 말 것. |
| 5.5 | proposition | GENERAL_ARGUMENT_SUPPORTED | — | 표현표지·부가 패키지의 독립성 |
| 6.2 | proposition | GENERAL_CONDITIONAL_S01 | S-01 | B raw 제시에서 사상 범위 |
| 6.4 | proposition | GENERAL_CONDITIONAL_S01 | S-01 | 활성 프로필 적용 |
| 6.6 | theorem | GENERAL_CONDITIONAL_S01 | S-01 | 부분모형 의미론 제한 |
| 6.8 | theorem | GENERAL_CONDITIONAL_S01 | S-01 | B2 raw 강화 동형과 구별 |
| 6.9 | proposition | GENERAL_CONDITIONAL_S01 | S-01 | raw 잉여 좌표 전체로 확대 금지 |
| 6.11 | theorem | GENERAL_ARGUMENT_SUPPORTED | — | 표현 서명 및 표현자료 typing |
| 7.2 | proposition | GENERAL_CONDITIONAL_S01_S03 | S-01, S-03 | A/B1 활성 vs B2 raw 비교 명시 |
| 7.3 | corollary | DIRECT_COROLLARY_CONDITIONAL | S-01, S-03 | B2를 기존 strict로 동일시하면 거짓 |
| 7.5 | theorem | GENERAL_CONDITIONAL_S01_S03 | S-01, S-03 | I_k 정의와 strict 일치 필요 |
| 8.1 | theorem | GENERAL_FIXED_BASE_SUPPORTED | — | 임의 정당한 Stage VI·공유 시그니처 |
| 8.4 | theorem | TYPING_PREMISE_SCOPE_OPEN | S-02, S-01 | 포함식만으로 타입 적법성 추론 불가 |
| 8.8 | corollary | DIRECT_COROLLARY_CONDITIONAL | S-01, S-03 | raw 전체와 active 혼동 금지 |
| 9.2 | theorem | EXISTENTIAL_WITNESS_SUPPORTED | S-04 | 적절 시그니처에서의 존재, 모든 고정 시그니처 아님 |
| 11.1 | theorem | GLOBAL_SCOPE_AND_SEMANTICS_OPEN | S-01, S-02, S-03, S-04 | 통합 정리 문장과 선행정리 범위 분리 |

## 2. 제11절 13개 결론: 20개 항목 및 독립 공리와 일대일 연동

| §11 항목 | 선행 번호/정의 | 감사 판정 | 검증된 범위에 맞춘 안전한 진술 후보 |
|---|---|---|---|
| 1 | 2.1 | DEFINITIONAL_SUPPORTED | 고정된 적법 시그니처에서 유한 순서 타입 프로필; 일차원 축 가정 불필요 |
| 2 | 2.5, PI, PII | AXIOM_CONTENT_SUPPORTED | 활성 종류의 Dom Xi⊆Ap 및 Dom Xi⊆DepSat; typing과 분리 |
| 3 | 4.1, 4.2, 4.3, 4.4 | UNIVERSAL_FIXED_SIGNATURE_DISPROVED | 적절한 공통 typed premodel 시그니처에 존재 반모형. 임의 고정 Σ에서 상호독립이라고 하지 않음. |
| 4 | 3.3, 4.5, 4.6 | DEFINITIONAL_WITH_EXISTENCE_BOUNDARY | 서로 다른 상태 규칙의 구분은 정의적. 모든 Σ에서 각 상태의 증인 존재나 영값 분할 가능성까지 주장하지 않음. |
| 5 | 3.7, C1 | CONDITIONAL_SEMANTICS | 모든 원시좌표 보존 조건에서 완성·축약 쌍방 역법칙. N 정규화와 구별. |
| 6 | 6.2, 6.4, 6.6 | CONDITIONAL_ACTIVE_SCOPE | A·B1의 활성 구조에 대한 사상/매장/부분모형 범위. raw 보존 자동 수반 없음. |
| 7 | 6.7, 6.8 | CONDITIONAL_ACTIVE_SCOPE | S1-S3 ⇒ S4, 기존 strict는 활성구조; B2 강화 raw동형과 별도. |
| 8 | 5.3, 5.4, 6.10, 6.11 | CONDITIONAL_FIXED_REPRESENTATION | 공통 표현시그니처와 적법 Y, Enc 조건 및 기반 strict의 동일 정의 유지. |
| 9 | 7.1, 7.2, 7.3, 7.5, 8.8 | CONDITIONAL_COMPARISON_ALIGNMENT | A/B1 활성 비교에서는 P33 일반 증명 지지; B2 raw 강화 동형 필요. |
| 10 | 8.1, 8.3, 8.4 | TYPED_PREMISE_REQUIRED | 전자는 모든 고정 기반에서 가능. 후자는 T(well-typed)+F(property-finite)+I(inclusions) 필요. |
| 11 | 8.5, 8.6, 8.7 | UNIVERSAL_FIXED_SIGNATURE_DISPROVED | 적절한 후보·입력·값공역이 있는 시그니처에서 존재. P37의 단계별 조건과 연동. |
| 12 | 9.1, 9.2 | UNIVERSAL_FIXED_SIGNATURE_DISPROVED | 정의역 조건이 갖춰진 적절한 시그니처에서의 존재 비분류. 임의 고정Σ 전칭 불가. |
| 13 | 2.1, 3.5, 11.1 | FIXED_STAGE_VI_RELATIVE | 정의와 인터페이스 수준에서 형성 기록을 변경하지 않음. 물리적 보존법칙 주장 아님. |

종합정리 §11(3),(11),(12)를 공집합 후보 종류 시그니처에서도 각각 성립하는 보편적 명제로 해석하면 **기존 P31·P34의 반모형으로 반증**된다. 소형 모형 검산과 해당 범위의 일반 수학 논증을 구별한다.
§11(4)의 지위 구분은 **가능한 상태의 정의상 분리**이지, 값공역·프로필이 없는 모든 시그니처에서 모든 상태의 실제 증인이 있다는 주장이 아니다. §11(5–9)는 원시좌표 의미론 및 단계 비교에 조건부. §11(10)은 타입 전제가 명확해야 한다. §11(13)은 고정 Stage-VI 인터페이스에 관한 상대적 진술이다.

## 3. P42 추가 감사: §4.5 및 §4.6의 존재 정리 범위

**원문 사실:** §4.1은 `σ(p)=(u)`, `X(u)={x}`, `Z_p=R`, `δ(p)={d}`인 **공통 특정 시그니처를 고정**한다. §4.5에서 `Ap_p={x}`, `Sat_{p,d}={x}`, `Dom Xi_p=∅`를 두어 두 가지 converse를 동시에 반증한다. §4.6은 그 모델에 C1을 적용하여 applicable and prerequisite-satisfied but undefined 상태의 존재를 얻는다. 이 특정 배경에서의 증명은 유효하다.

**추가 확인할 논리 간극:** 4.5의 `core system does not imply either converse`는 **적법한 시그니처 계열 전체에 대한 도출 불가능성**으로 읽으면 위 반모형으로 지지된다. 그러나 후보 속성 종류가 전혀 없는 특정 시그니처에서는 모든 선언된 속성에 대한 converse 포함식이 공허하게 참이므로, 같은 시그니처 안에서 converse 위반 증인 존재가 불가능하다. 마찬가지로 4.6 `There are full property models containing an input...`는 §4.1처럼 적절한 후보·비공집합 입력곱의 배경에서 참이지만, 임의의 고정 시그니처 전부에 대한 존재 명제로 승격할 수 없다.

이것은 원문 §4.1의 명시된 배경을 잘못되었다고 판단하는 것이 아니라, **§11의 서두에서 고정한 Σ로의 부적절한 전파를 금지**하는 S-04의 세부 하위 증명 의무이다. P40이 4.5·4.6의 `risk`를 공란으로 보존한 점은 그 기록을 소급 위조하지 않고, P42에서 `S-04_LOCAL_EXISTENCE_SCOPE` **추가 태그**로 반영한다.

한 원소 `p:(u),X(u)={a},δ(p)={d}` typed core에서 `Ap=Sat={a}`, `Dom Xi=∅`이면 PI/PII 참, converse 두 개 거짓, C1 status는 applicable-but-undefined. 빈 종류 시그니처에서 위반/미정의 존재 증인은 없음. 두 경우를 서로 비교해야 원래 국소 증명과 과대 일반화를 구별할 수 있다.

## 4. 원고 일괄 개정 시의 절별 검사 순서 — **아직 적용 금지**

- **§2 (Def2.5·2.7):** A 정규 제한 가족, B1 원시 raw 보존/활성 비교, B2 raw 비교/강한 동형의 인덱스·타입 규칙을 **최종 비교 후** 문구 확정. `not required`를 임의로 `forbidden`이라 자동 해석하지 않음.
- **§3 (C1·Th3.7):** 실제 원시자료 전체의 정확한 보존과 정규화 N 연산을 분리. 완료 모형 양방향 역법칙을 유지하되 raw 잉여의 취급 명시.
- **§4 (4.3–4.6):** PI/PII 독립성·typing 비함의 및 converse 비함의·undefined 상태 증인의 **§4.1 특정 배경 vs 임의 고정 시그니처** 범위 문구 검토. 원래 적법 증인을 폐기하지 않음.
- **§5 (Def5.1):** 완전 원시 기술자에 활성 자료 및 raw 여분자료가 무엇으로 표현되는지 확정. 표현 패키지 동형과 혼동 금지.
- **§6 (6.2–6.11):** 기존 strict가 활성 코어용인지 B2 raw용인지 명시. B2 선택 시 별도 강한 raw strict를 정의해야 함.
- **§7 (7.1–7.5):** `I1...I5`를 인덱스·전단사 후보를 포함한 명시적 집합 정의로 적고 제6절 strict와 동형 대응을 증명. B2 raw stage4/5는 별도 관계 유지.
- **§8 (8.4–8.8):** well-typed compatible primitive presentation T + finite F + inclusion I, 존재 증인의 시그니처 자원조건을 명시.
- **§9 (9.2):** 정의9.1 도메인(영 지정/프로필 가용성) 및 두 속성 증인/추가 단일 속성 증인의 비교 조건을 구별.
- **§11 (11.1):** 고정 기반에 대한 전칭 구조 정리와 특정 적절 시그니처에 대한 **존재** 결과를 별도 문장·정리로 분리. 위 13항 대장을 각각 검사.
- **KR/EN:** 모든 수정은 절 단위로 정렬, LaTeX 주석 `% -----` 경계 및 저자 Kwon Dominicus 유지. 고친 판본을 새로 잠근 후 수학·참조·PDF 재검산. 기존 동결 원고를 조용히 덮어쓰지 않음.

## 5. 현재 종료 관문

S-01→S-03, S-02, S-04 미결 4항 유지. P42는 이 중 S-04의 4.5·4.6 파급을 추가로 탐지했지만, 새로운 상위 공리나 독립적 원시공리 모순을 선언하지 않는다.
**감사 조사와 논문 개정/최종 FPA 종료는 별도 단계**이다. A/B1/B2의 채택 여부는 사용자의 지시에 따라 전체 조사 완료 후 판단.

```text
AUDIT_ID: PA-P42-20261102-CONSOLIDATED-CLAIMS-AND-REVISION-SPEC
SOURCE_FROZEN: YES
PROOF_CLAIM_LEDGER: 20/20
MAIN_THEOREM_ITEMS: 13/13
NEW_SCOPE_DETAIL: S04_LOCAL_EXISTENCE_4_5_4_6
S01_SEMANTICS: DEFERRED
S02_S03_S04: OPEN
MANUSCRIPT_TEX_PDF_ZENODO_EDITED: NO
AUDIT_REVIEW_COMPLETE: NOT_YET_DECLARED
PROPERTY_FPA: OPEN
INDEPENDENT_EXTERNAL_VALIDATION: NOT_ESTABLISHED
```
