# PA-P43 — 속성공리계 P27 영·국문 절별 수학적 정합성과 FPA 종료 관문 감사

- **원고 저자**: Kwon Dominicus; **감사일**: 2026-11-02 KST.
- **동결 정본**: P27 EN SHA256 `51c194ec33f802a2061b68b3521fdb831f0f754a0386fa72f8e89a39efff7bdb`; KR SHA256 `a643ea619f9594142bfc09b9f486c948cf0a85679a3b2a8a43bc731a1e108fbb`.
- **원고 유지**: EN/KR LaTeX, PDF, Zenodo 변경 없음. 사용자 지시대로 A/B1/B2 선택 보류. 전체 속성공리계 **FPA OPEN**.
- **연속 감사 근거**: [P39 56항](../P39_global_56_item_dependency/P39_GLOBAL_56_ITEM_DEPENDENCY_AUDIT_KR.md), [P40 20항](../P40_20_statement_proof_audit/P40_20_PROOF_CLAIMS_REVERSE_AUDIT_KR.md), [P41 의존 DAG](../P41_dependency_chain_and_scope/P41_PROOF_CHAIN_CYCLE_AND_SCOPE_AUDIT_KR.md), [P42 20+13 대장](../P42_consolidated_premises_countermodels_revision_spec/P42_CLAIMS_PREMISES_COUNTERMODELS_REVISION_SPEC_KR.md).

## 1. 언어별 구조 및 수식 대응 결과

- 본문/부록 `section` **16/16**, `subsection` **30/30**.
- 번호가 부여된 정의·정리·명제·따름정리·구성·반모형·비고 **56/56**: 위치, 환경 종류, 정확한 `label`가 양쪽에서 일치.
- 원고 교차참조 라벨 각각 **36개**, 인용 발생 각각 **31회**, 인용대상 누락 **0**; 17개 `proof` 환경 각 동일.
- PI·PII 2개 및 C1 1개 양쪽 존재. 공통 매크로 17개.
- 각 언어에 표시수식 `\\[...\\]` **78개**. 아래 표의 16개 절에서 수식 순서까지 비교하였다. 정규화는 수식 뒤 문장부호, 공백, 현지화된 `\\text{...}` 설명을 제거하되 (E1)·(E2)·(E3) 표지는 보존한다. **정규화 수식 배열 78/78 일치**. 비본질적 자연어 표기가 제거됐다는 사실은 주의사항이다.

| 절 | EN 제목 | KR 제목 | 표시 수식 EN/KR | 수식 뼈대 |
|---|---|---|---|---|
| 1 | Introduction | 서론 | 1/1 | 일치 |
| 2 | Formation Interface, Signature, and Property Premodels | 형성 인터페이스, 시그니처 및 속성 예비모형 | 13/13 | 일치 |
| 3 | Primitive Axioms and Definitional Completion | 원시 공리와 정의적 완성 | 10/10 | 일치 |
| 4 | Primitive Independence and Residual Minimality | 원시 독립성과 잔여 최소성 | 12/12 | 일치 |
| 5 | Complete Property Descriptors and Optional Representations | 완전 속성 기술자와 선택적 표현 | 3/3 | 일치 |
| 6 | Structure-Preserving Maps, Embeddings, and Strict Equivalence | 구조 보존 사상, 매장 및 엄격한 동치 | 11/11 | 일치 |
| 7 | Staged Comparison and First Branching | 단계별 비교와 첫 분기 | 6/6 | 일치 |
| 8 | Model Existence and Finite Realization | 모형 존재와 유한 실현 | 14/14 | 일치 |
| 9 | Compression and Classification Obstructions | 압축 및 분류 장애 | 5/5 | 일치 |
| 10 | Relation to the Realized-Axis Specialization and Later DSD Layers | 실현축 특수화 및 후속 DSD 층과의 관계 | 1/1 | 일치 |
| 11 | Main Property-Closure Theorem | 주 속성 폐쇄 정리 | 0/0 | 일치 |
| 12 | Discussion and Scope | 논의와 범위 | 0/0 | 일치 |
| 13 | Conclusion | 결론 | 1/1 | 일치 |
| 14 | Typing and Notation | 유형화와 표기 | 0/0 | 일치 |
| 15 | Axiom, Definition, and Dependency Map | 공리, 정의 및 의존성 지도 | 0/0 | 일치 |
| 16 | Finitely Specified Reconstruction Protocol | 유한 명세 재구성 절차 | 1/1 | 일치 |

**범위 제한:** 수식 뼈대·라벨·배열의 일치만으로 자연어 텍스트의 모든 양화·전제의 수학적 의미가 완전 동치라고 형식 증명하는 것은 불가능하다. 국문·영문의 언어적 동치에 대한 목표별 대조를 병행했고, 미검증 영역을 `G4`로 유지한다. `\\text{...}`를 버린 수식 대조로 그 내부의 한국어 설명을 검증했다고 주장하지 않는다.

## 2. 고위험 진술의 병렬 대조와 공통 미해결 의무

| 원문 위치 | 비교 항목 | P43 판정 |
|---|---|---|
| 2.5 | not required / 요구하지 않는다 | SAME_UNRESOLVED_AMBIGUITY |
| 3.7 | completion/reduction and raw preservation | SAME_CONDITIONAL_PREMISE |
| 4.3-4.6 | fixed witness and generic non-derivability/undefined existence scope | SAME_EXISTENTIAL_SCOPE_RESTRICTION |
| 6.7-6.9 | active strict versus B2 raw strict | SAME_SEMANTIC_CHOICE_OPEN |
| 7.1-7.5 | I1...I5 strict-comparison conditions visible by stage | SAME_EXPLICIT_COMPARATOR_REQUIRED |
| 8.4 | typed compatible finite primitive presentation | SAME_TYPED_PREMISE_REQUIRED |
| 9.2 | summary collision witness versus fixed-signature universal | SAME_EXISTENTIAL_SCOPE_RESTRICTION |
| 11.1 | Fix FVI and shared signature preceding 13 claims | SAME_UNIVERSAL_EXISTENTIAL_SCOPE_GAP |

제11절 13개 결론은 EN/KR에서 **같은 순서**, 같은 고정 Stage VI·공유 시그니처 전제, 같은 선행 결과의 인용에 대응함을 본문 문구와 대조했다. 동일한 강한 전칭 해석의 문제는 한 언어의 오역이 아니라 양쪽 원고에 공통으로 발생한다.

### S-04 하위 의무 보존
- §4.3/§4.4의 공리 독립성 증거는 §4.1의 특정 적절한 시그니처에서 성립한다. 임의 고정 시그니처에서 무조건적 상호독립을 주장하는 강한 판본은 반례가 있다.
- §4.5/§4.6의 역포함 비함의·applicable-but-undefined 존재는 적절한 국소 증인 시그니처에 의존하며 모든 고정 시그니처에 대해 그 상태의 증인 존재를 요구할 수는 없다.
- §11(3),(11),(12) 및 적절한 시그니처에서의 존재증인 관계를 P42와 연결한 채 그대로 OPEN.

### S-02 및 S-01→S-03 보존
- §8.4의 PI/PII 포함조건만으로는 타입 적법성을 도출할 수 없고, 적법한 typed finite presentation 전제 T가 필요하다.
- Def2.5 미선언/프로필 미제공 원시자료의 `not required`는 EN/KR 모두 `요구하지 않는다`와 대응하나 A와 B의 어느 쪽을 원고가 결정했다고 선언할 수 없음.
- 제6절 strict는 활성 원시좌표 기준이며 B2 raw 동형은 별도로 강화해야 한다. 제7절 I_k 비교 정의를 raw/active에 상대화하기 전에는 최종 진술을 닫지 않는다.

## 3. 감사 종료 관문

| 관문 | 목적 | 상태 |
|---|---|---|
| G1 | EN/KR 56 numbered statements, 36 labels, 16 sections and 30 subsections | CHECKED_STRUCTURE_ONLY |
| G2 | 78 EN/KR display math expressions after punctuation/prose-label normalization | PASS_EQUIVALENT_FORMULA_SKELETONS |
| G3 | 13 final claims same ordered structural and quantifier-sensitive wording | TARGETED_BILINGUAL_REVIEW_SUPPORTED_NOT_PROOF |
| G4 | all bilingual natural-language proof semantics formal equivalence | NOT_FULLY_CERTIFIED |
| G5 | A/B1/B2 semantics comparison and final convention | DEFERRED_UNTIL_WHOLE_AUDIT_REVIEW |
| G6 | S02 typed finite and S04 quantifier scopes revised into new manuscript | FROZEN_SOURCE_NOT_REVISED |
| G7 | post-revision global mathematical proof and external independent validation | NOT_ESTABLISHED |

**이번 판정:** EN/KR 수식 구조와 핵심 수학 명제의 목표별 비교에서 **새로운 언어별 독립 모순은 발견되지 않음**. 이는 자연어 전체의 번역 오류 부재에 대한 절대적 인증이 아니다. 반례를 발견하지 못한 진술에 대해서도 수학적 완전성까지 주장하지 않는다.
`G1`–`G3`의 대장 작성은 완료되었으나, `G4`는 제한적이며 `G5`–`G7`이 남아 **FULL_FPA_OPEN**이다.
이 문서는 **감사 조사 결과를 최종 선택 전 묶기 위한 근거**이며, A/B의 채택·흡수·폐기는 논문 전체 결과의 비교 없이 진행하지 않는다.

## 4. 후속 작업 (원고 편집 금지)

P44에서는 새로운 증인 개수나 단순 검산을 확대하기보다, P29–P43의 남은 개방 의무를 일괄 폐쇄 가능한지 점검하는 `PRE_DECISION_READINESS` 감사로 진행한다. G4의 사람에 의한 언어적 검토와 G5의 A/B1/B2 병렬 수학·정보보존 평가를 분리한다. 이후 의미론이 선택되면 원고를 **절 단위**로 개정하고 `% -----` 주석 구분, 저자 Kwon Dominicus, EN/KR 1:1 대응을 유지하며 새로운 버전을 별도로 재검산한다.

```text
AUDIT_ID: PA-P43-20261102-EN-KR-SEMANTIC-PARITY-AND-GATES
BILINGUAL_SECTIONS: 16/16
SUBSECTIONS: 30/30
NUMBERED_ITEMS: 56/56
REFERENCE_LABELS: 36/36
DISPLAY_MATH_SKELETONS: 78/78
MAIN_CLAIMS: 13/13
S01_S03: OPEN
S02: OPEN
S04: OPEN
A_B_B1_B2_SELECTION: DEFERRED
SOURCE_TEX_PDF_ZENODO_EDITED: NO
PROPERTY_FPA: OPEN
EXTERNAL_FORMAL_VALIDATION: NOT_ESTABLISHED
```
