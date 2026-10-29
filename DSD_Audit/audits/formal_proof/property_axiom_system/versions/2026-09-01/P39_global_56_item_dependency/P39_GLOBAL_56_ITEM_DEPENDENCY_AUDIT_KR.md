# PA-P39 — P27 동결본 번호 항목 56개 전역 의존성·파급 감사

**실행일:** 2026-10-29 KST. **원고 저자:** Kwon Dominicus.
**입력 정본:** P27 EN SHA256 `51c194ec33f802a2061b68b3521fdb831f0f754a0386fa72f8e89a39efff7bdb`, KR `a643ea619f9594142bfc09b9f486c948cf0a85679a3b2a8a43bc731a1e108fbb`.
**동결:** 영·국문 LaTeX, PDF, Zenodo, 기존 P29–P38 판정·반례 수정하지 않음. 이 문서는 FPA의 감사 증거이며 개정 논문이나 형식화 증명 완결 선언이 아니다.
**선행:** [P35 통합 대장](../P35_integrated_fpa_closure_ledger/P35_FPA_INTEGRATED_CLOSURE_LEDGER_KR.md), [P36 A/B 비교](../P36_semantics_decision/P36_SEMANTIC_A_B_MINIMAL_AXIOM_AUDIT_KR.md), [P37 전칭/존재](../P37_s02_s04_fixed_signature/P37_S02_S04_GENERAL_THEOREM_SCOPE_AUDIT_KR.md), [P38 A/B1/B2](../P38_a_b1_b2_stage_strict/P38_A_B1_B2_STAGE_STRICT_C1_GENERAL_AUDIT_KR.md).

## 1. 원문 56항 정확한 범주와 잠금 검사

- EN/KR 환경 순서 **56/56 동일**. 유형: definition 23, remark 7, theorem 10, countermodel 2, proposition 7, corollary 3, construction 4.
- 원시공리 PI·PII 2개, C1 1개는 독립적인 번호 체계를 사용하므로 56항에서 제외.
- 두 원문 `label` 각 36개, 누락된 교차참조 각 0/0. 명시 `proof` 환경 각 17개; 모든 번호 항목이 독립 proof 환경을 요구한다는 뜻 아님.
- 재현 검증기는 소스 해시, 순서, 종류, 라벨, 정리 개수, 보고서 장부를 각각 검사. 문자열 정합은 수학적 유효성 인증과 구별한다.

## 2. 56항 감사 의존성 전체 지도

아래 S 태그는 **문제의 영향·재확인 필요**를 나타낸다. 태그 없는 항목을 독립 증명이 완결되었다고 해석하지 않는다.

| 항목 | 종류 | 원문 표제 | 증명 의무 연계 | 판정·경계 |
|---|---|---|---|---|
| 2.1 | definition | Shared property signature | — | 현재 직접 차단 요인 없음; 독립 완료 주장 아님 |
| 2.2 | remark | Property names do not determine mathematics | — | 현재 직접 차단 요인 없음; 독립 완료 주장 아님 |
| 2.3 | definition | Auxiliary carrier supply | — | 현재 직접 차단 요인 없음; 독립 완료 주장 아님 |
| 2.4 | definition | Profile availability | — | 현재 직접 차단 요인 없음; 독립 완료 주장 아님 |
| 2.5 | definition | Property premodel | S-01·S-02 | 모형의 활성 가족 정확한 정의역 미확정; A/B 후보 유지 |
| 2.6 | definition | Primitive property core | S-01·S-02 | 기존 일반 논증의 적용 범위·전제 확인 |
| 2.7 | definition | Property-stage truncations | S-01·S-03 | 기존 일반 논증의 적용 범위·전제 확인 |
| 3.1 | definition | Dependency-satisfied region | — | 현재 직접 차단 요인 없음; 독립 완료 주장 아님 |
| 3.2 | definition | Assignment domain | — | 현재 직접 차단 요인 없음; 독립 완료 주장 아님 |
| 3.3 | definition | Property status | S-01 | 기존 일반 논증의 적용 범위·전제 확인 |
| 3.4 | definition | Defined property records | S-01 | 기존 일반 논증의 적용 범위·전제 확인 |
| 3.5 | remark | Formation assignments are not property assignments | — | 현재 직접 차단 요인 없음; 독립 완료 주장 아님 |
| 3.6 | definition | Primitive reduction | S-01 | 기존 일반 논증의 적용 범위·전제 확인 |
| 3.7 | theorem | Completion-reduction inverse laws | S-01·S-02·S-03 | C1 역법칙은 전체 원시자료 정확 보존 전제에 상대적 |
| 3.8 | remark | No core well-foundedness axiom | — | 현재 직접 차단 요인 없음; 독립 완료 주장 아님 |
| 4.1 | countermodel | Primitive Axiom I fails while Primitive Axiom II holds | S-04 | 기존 일반 논증의 적용 범위·전제 확인 |
| 4.2 | countermodel | Primitive Axiom II fails while Primitive Axiom I holds | S-04 | 기존 일반 논증의 적용 범위·전제 확인 |
| 4.3 | theorem | Mutual non-derivability | S-04 | 고정 시그니처 전칭 독립성 반례; 증인 시그니처 범위로 한정 |
| 4.4 | proposition | The primitive axioms are not typing tautologies | S-04 | 기존 일반 논증의 적용 범위·전제 확인 |
| 4.5 | proposition | No hidden converse | — | 현재 직접 차단 요인 없음; 독립 완료 주장 아님 |
| 4.6 | corollary | Applicable but undefined status is nonvacuous | — | 현재 직접 차단 요인 없음; 독립 완료 주장 아님 |
| 5.1 | definition | Complete core property descriptor | S-01 | 완전 기술자의 raw/active 원시좌표 범위 분리 필요 |
| 5.2 | remark | Undefinedness is structural data | S-01 | 기존 일반 논증의 적용 범위·전제 확인 |
| 5.3 | definition | Shared representation signature | — | 현재 직접 차단 요인 없음; 독립 완료 주장 아님 |
| 5.4 | definition | Representation package | — | 현재 직접 차단 요인 없음; 독립 완료 주장 아님 |
| 5.5 | proposition | Representation forgetting | — | 현재 직접 차단 요인 없음; 독립 완료 주장 아님 |
| 6.1 | definition | Forward property map | S-01 | 기존 일반 논증의 적용 범위·전제 확인 |
| 6.2 | proposition | Category of property models | S-01 | 기존 일반 논증의 적용 범위·전제 확인 |
| 6.3 | definition | Property embedding | S-01 | 기존 일반 논증의 적용 범위·전제 확인 |
| 6.4 | proposition | Wide embedding subcategory | S-01 | 기존 일반 논증의 적용 범위·전제 확인 |
| 6.5 | definition | Inclusion submodel | S-01 | 기존 일반 논증의 적용 범위·전제 확인 |
| 6.6 | theorem | Property-submodel preorder | S-01 | 기존 일반 논증의 적용 범위·전제 확인 |
| 6.7 | definition | Strict core property isomorphism | S-01·S-03 | 기존 strict 동형은 활성 좌표 비교; B2 raw 동형과 별개 |
| 6.8 | theorem | Strict property equivalence is an equivalence relation | S-01·S-03 | S1–S3로 S4 도출은 활성 구조 범위에 상대적 |
| 6.9 | proposition | Strict isomorphism preserves completion | S-01·S-03 | 기존 일반 논증의 적용 범위·전제 확인 |
| 6.10 | definition | Representation-preserving lift | S-01 | 기존 일반 논증의 적용 범위·전제 확인 |
| 6.11 | theorem | Representation-inclusive strict equivalence | S-01 | 기존 일반 논증의 적용 범위·전제 확인 |
| 6.12 | remark | Abstract versus represented comparison | S-01 | 기존 일반 논증의 적용 범위·전제 확인 |
| 7.1 | definition | Stage-comparison sets | S-01·S-03 | I_k 성분식과 raw/active 비교 범위 선택 필요 |
| 7.2 | proposition | Nestedness | S-01·S-03 | I4=I5는 각 의미론의 일관된 Stage4/5 정의에 상대적 |
| 7.3 | corollary | Strict comparison at the final primitive stage | S-01·S-03 | I4 비공집합과 strict 동형은 B2 기존 strict에선 거짓 |
| 7.4 | definition | First branching index | S-01·S-03 | 기존 일반 논증의 적용 범위·전제 확인 |
| 7.5 | theorem | Branching symmetry and invariance | S-01·S-03 | 기존 일반 논증의 적용 범위·전제 확인 |
| 7.6 | remark | One failed map does not prove first branching | S-01·S-03 | 기존 일반 논증의 적용 범위·전제 확인 |
| 8.1 | theorem | Trivial extension over every Stage-VI formation record | — | 현재 직접 차단 요인 없음; 독립 완료 주장 아님 |
| 8.2 | construction | One-input nontrivial property model | S-04 | 기존 일반 논증의 적용 범위·전제 확인 |
| 8.3 | definition | Finite primitive property data | S-02 | 기존 일반 논증의 적용 범위·전제 확인 |
| 8.4 | theorem | Standard finite realization | S-02 | finite inclusion만으로 typed premodel 보장 불가 |
| 8.5 | construction | Stage-2 declaration branch | S-03·S-04 | 기존 일반 논증의 적용 범위·전제 확인 |
| 8.6 | construction | Stage-3 applicability branch | S-03·S-04 | 원문 applicability 증인 유효; dependency-only 증인도 별도 구성 |
| 8.7 | construction | Stage-4 assignment branch | S-03·S-04 | 기존 일반 논증의 적용 범위·전제 확인 |
| 8.8 | corollary | No independent Stage-5 witness | S-03 | 기존 일반 논증의 적용 범위·전제 확인 |
| 9.1 | definition | Simple finite property summary | S-04 | 기존 일반 논증의 적용 범위·전제 확인 |
| 9.2 | theorem | Summary equality does not classify strict property structure | S-03·S-04 | 존재 비분류는 적절한 시그니처 조건 필요 |
| 9.3 | remark | What the summary loses | S-04 | 기존 일반 논증의 적용 범위·전제 확인 |
| 11.1 | theorem | Static typed property-closure theorem | S-01·S-02·S-03·S-04 | (3),(11),(12) fixed-signature 강한 전칭판 반례; 전체 의존 종결 OPEN |

## 3. 원문 직접 참조 및 의존성 전파의 정확한 범위

- `thm:completion-inverse` (3.7) → Def5.1 기술자 및 §7의 C1 단계5, Th8.4, §11(5·9·10)의 수학적 전제를 지지. 원시 raw 전체 보존이 필요할 수 있으므로 S-01을 자동 닫지 않는다.
- `thm:independence` (4.3) → §11(3). 증인 시그니처 내 원시공리 독립은 유효하지만 임의 고정 시그니처 전칭판은 P31/P34의 적법 반례로 부정.
- `thm:strict-equivalence` (6.8) → 6.9 및 §7 비교집합의 strict 동형 대응을 지지. 기존 strict는 선언되고 이용 가능한 속성 자료의 동형이며 B2 raw 강화 동형과 동일하지 않음.
- §7(7.1–7.5) → §8 분기(8.5–8.8), §9 비분류(9.2), §11(9·11·12). A/B1에서 활성 비교, B2에서 raw 강화 비교를 **상호 다른 정리**로 보관.
- `thm:finite-realization` (8.4) → §11(10). well-typed finite primitive presentation을 전제로 일반 완성 증명 가능; 포함식만으로 타입 적법성은 도출되지 않음.
- `thm:compression` (9.2) → §11(12). 특정 적절한 시그니처에서의 존재 정리이며 모든 고정 시그니처 비분류가 아님.
- `thm:main` (11.1) → 13항은 자체가 새 공리나 개별 증명들을 대체하지 않음. S-01→S-03, S-02, S-04를 별도로 종료해야 함.

## 4. 신규 보강 검사 — '선행조건만으로' Stage 3 분기

기존 §8.6은 적용가능성 차이에 의한 Stage3 증인이다. **동일한 적용가능성**을 유지하면서 선행조건만 달라지는 증인을 별도로 구성한다.

고정 시그니처에 단항 후보 `p:(u)`, 선행조건 `δ(p)={d}`를 두고 양 모델 모두 `X(u)={a}`, `Π={p}`, `Ap_p={(a)}`, `Ξ_p=∅`로 동일하게 둔다.
단, `Sat_{A,p,d}={(a)}`, `Sat_{B,p,d}=∅`로 둔다. PI·PII는 할당 정의역이 비었으므로 양쪽에서 만족한다.
유일한 운반체 항등 전단사는 선언·가용성·적용가능성을 보존하지만 선행조건 만족집합의 상-동일성을 만족하지 못한다. 따라서 `I_2(A,B)≠∅`, `I_3(A,B)=∅`, 최초 분기는 3이다.
**조건부 일반화:** 동일한 하나의 이용 가능한 비공집합 입력을 실현할 수 있으며 선행조건 종류 하나를 포함한 고정 시그니처에서, 다른 속성 자료를 공통으로 고정해도 선행조건 단독 Stage3 증인을 만들 수 있다. 값 공역이 비어도 할당을 정의하지 않으므로 가능하다.
이는 원문의 기존 적용가능성 증인을 반증한 것이 아니라, §11(11)의 'applicability/dependency'가 각 원시축에 대해 독립적으로 실현 가능함을 더 명확히 한 새 감사 보강이다. 유한 구현 증거와 일반 증명의 구분을 유지한다.

## 5. 감사 후 잔여 중요 의무 및 판정

| 관문 | 현 상태 | 이 단계에서 성립하는 것 |
|---|---|---|
| S-01 원시좌표 의미론 | **선택 보류** | A/B1 및 B2+raw 강화 관계 각각 조건부 체계 가능 |
| S-02 Th8.4 타입 적법성 | **문구 명료화·최종 원문 일치 보류** | T+F+I 일반 유일완성 논증 확보 |
| S-03 I1–I5와 strict 비교 | **원문 의미 범위 결의 보류** | A/B1에서 활성, B2에서 강화 raw 명제 분리 |
| S-04 §11(3)(11)(12) 양화 | **수정문·영국문 대응 보류** | 적절한 시그니처 증인과 P37 고정시그니처 조건부 분류 |
| 신규 독립적 §8.6 선행조건 분기 | **조건부 증인 도출** | 타입/정렬·선행조건 명시 범위에서 일반 구성 |
| 전체 속성공리계 FPA | **OPEN** | 내부 전역 의존 대장 정합성 확보, 전체 증명 종료 아님 |

미해결 중요 의무 4건은 여전히 있으며, 이 항목의 개수 자체로 FPA의 전체 수학적 완성도를 산술 측정하지 않는다. 후속에는 현재 동결 유지 상태에서 56항 **명제별 전제·반모형 역감사**를 계속하고, 모든 감사 조사 완료 후 A/B 의미론 결정→영·국문 원고 절별 일괄개정→개정본 재감사를 별도 단계로 운영한다.

```text
AUDIT_ID: PA-P39-20261029-GLOBAL-56-ITEM-DEPENDENCY
SOURCE_EN_KR_ITEM_COUNT: 56/56
SOURCE_EN_KR_LABEL_COUNT: 36/36
DERIVED_DEPENDENCY_ONLY_STAGE3_WITNESS: SUPPORTED
SOURCE_FIXED_SIGN_QUANTIFIER_COUNTEREXAMPLES: RETAINED
S01_CHOICE: DEFERRED
MANUSCRIPT_TEX_PDF_ZENODO_EDITED: NO
MATHEMATICAL_VERDICT: MIXED_CONDITIONAL_PROOFS_AND_SCOPE_GAPS
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY_AND_REFINEMENT
PROPERTY_FPA: OPEN
INDEPENDENT_EXTERNAL_VALIDATION: not_established
```
