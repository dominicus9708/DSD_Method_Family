# PA-P31 — 속성공리계 P27 동결본 §11 최종 13항 역방향 의존성 감사

- 감사 기준: Kwon Dominicus, P27 영문·국문 LaTeX 후보. EN SHA256 `51c194ec33f802a2061b68b3521fdb831f0f754a0386fa72f8e89a39efff7bdb`; KR SHA256 `a643ea619f9594142bfc09b9f486c948cf0a85679a3b2a8a43bc731a1e108fbb`.
- 감사 단계: P29 유한 실현 전제 감사 → P30 잉여 원시좌표 의미론/제7절 비교집합 정식화 → **P31 제11절 의존성 역감사**.
- **원고 동결:** 원고 LaTeX·PDF, 출판물, Zenodo, 기존 코드와 결과를 수정하지 않음. 발견사항은 분리된 감사 파일·검증 프로그램에만 기록.
- 적용 프로토콜: FPA-01~07; 수학적 정당성/DSD 감사판정/원고수정의무/외부평가 분리.

## 1. 원문 고정과 새 핵심 쟁점: §11 최종 정리의 양화 범위

원문 Theorem 11.1은 **“Fix a Stage-VI DSD formation record FVI and a shared property signature Sprop. Then … [1–13]”**로 시작한다. 반면 제4절의 공리 독립 반모형은 **특정** 공유 시그니처(`u`, 속성 하나, 값공역 실수, prerequisite `d`)를 별도로 선택한다. 제8절의 최초 분기 2·3·4 구성도 필요한 속성 후보·정렬·값 구조가 있는 각각의 명시적 시그니처에 상대적이다. 제9절의 요약 충돌도 두 zero-bearing 속성과 2원소 입력을 요구한다.

**반사례/범위 판별:** Def2.1은 후보 종류 우주 `Pihat`, 보조 정렬 `Saux`가 비공집합이어야 한다고 규정하지 않는다. 유효한 임의 Stage-VI 고정 기반 위에 `Pihat=∅`, `Saux=∅`, `PiZero=∅`인 공유 속성 시그니처를 택한다. P30의 '정규 제한 좌표 가족' 해석에서는 보조 운반체 공급, 선언, Ap, Sat, Xi 모두 공집합인 완전모형 하나가 존재한다(제8절 자명 확장의 바로 그 모형). 이 고정 시그니처에서:

1. **원시공리 PI, PII가 모든 타입 전모형에 대해 공허하게 참**이다. 그러므로 (3)을 '임의로 고정한 개별 공유 시그니처마다 두 공리가 서로 비도출'이라는 전칭명제로 해석하면 거짓이다. 독립성의 원문 §4.2 증명 자체는 *증인 시그니처에서의* 일반 언어론적 비도출로서는 유효하다.
2. **선언·적용가능성·할당 최초 분기 2·3·4가 하나도 존재하지 않는다.** (11)의 존재 주장이 임의 고정 시그니처에서 성립하는 것으로 읽히면 거짓이다. §8.3 개별 시그니처를 선택한 세 유한 구성은 여전히 유효하다.
3. **요약 충돌/비동형 두 모형이 존재하지 않는다.** 하나뿐인 정규 완전모형은 자신과 엄격 동형이다. 그러므로 (12)을 *해당 고정 시그니처의 모델 범주에서 항상 비분류*로 읽으면 거짓이다. §9.1은 **허용된 시그니처 중 어떤 적절한 시그니처에서 비동형-동일요약 쌍이 존재한다**는 결과로는 여전히 유효하다.

한 단계 덜 특수한 배경에서도 문제는 보인다: 후보 속성이 하나 있어도 `δ(ω)=∅`이면 PII가 모든 타입 전모형에서 성립하며, **해당 개별 시그니처에서** PII 독립성을 증명할 수 없다.

**정확한 판정:** 수학적 공리계의 자기모순이라고 주장하지 않는다. 그러나 §11의 선행하는 “Fix … Sprop”를 단일 임의 시그니처 전칭으로 읽을 때 결론 (3), (11), (12)는 **유효한 반모형에 의해 그 문자적 강한 판본이 부정**된다. 제4·8·9절의 존재 정리를 §11로 전달하려면 “모든 고정 기반에서 성립하는 보편 구조 정리”와 “**허용된 적절한 시그니처가 존재하는 계열 수준**의 비도출·증인 정리”를 구분해야 한다. **수정 후보는 감사대장에만 기록하고 현재 원고에는 적용하지 않는다.**

## 2. §11 13개 항목의 역방향 증명 의무 대장

| 최종 번호 | 직접 근거 | P29/P30/P31 이후 판정 | 종결 전제/영향 |
|---:|---|---|---|
| 1 | Def2.1 finite ordered profiles | `SUPPORTED_AS_DEFINITION` | 후보종류가 존재하면 m≥1, 축 필수 없음. 후보∅에서도 정의 자체 성립 |
| 2 | §3 PI·PII | `SUPPORTED_AS_AXIOM_CONTENT` | 선언되면서 프로필 이용 가능한 종류에 한정 |
| 3 | Th4.3 + CM4.1/4.2 | `FIXED_SIGNATURE_QUANTIFIER_SCOPE_GAP` | 공통 **증인** 시그니처의 비도출은 지지. 임의 고정 시그니처 독립성은 거짓 |
| 4 | Def3.4 status + §4 no converse | `SUPPORTED_AS_STATUS_TAXONOMY` | 상태 분류의 정의적 배타성. 모든 고정 시그니처에 각 상태 실현이 있다는 주장으로 확대 금지; zero-bearing 별도 조건 |
| 5 | Th3.7 completion/reduction | `CONDITIONAL_P30_SURPLUS_CONVENTION` | 정규 제한 원시좌표로 정하거나 잉여 좌표가 보존되는 완전 기술자 범위를 명시해야 원시자료 정확한 역법칙 판정 |
| 6 | §6 forward maps, embedding, preorder | `GENERAL_ARGUMENT_SUPPORTED_WITH_P30_SCOPE` | 선언·프로필 이용가능성 반영 및 F1-F5, E1-E3. 전체 잉여좌표 동일성 자동 보존 아님 |
| 7 | Th6.8 + S1–S4 | `GENERAL_ARGUMENT_SUPPORTED_WITH_P30_SCOPE` | S2/S3 반드시 포함. 전체 surplus descriptor 동형과 혼동 금지 |
| 8 | §6 representation isomorphism | `SUPPORTED_CONDITIONALLY` | 고정 표현 시그니처, 동일 활성 표지, 선택된 정의역 전단사·값 보존 필요 |
| 9 | Th7.5 and Def7.1 | `CONDITIONAL_P30_EXPLICIT_IK_SCHEMA` | 모든 전단사 가족 집합의 명시적 I_k 성분식 선택 필요. P30 정식화에서는 일반 도출 성립 |
| 10 | Th8.1, Th8.4 | `CONDITIONAL_P29_WELL_TYPED_PREMISE` | 적법한 finite typed primitive presentation을 전제로. 포함관계만으로 타입 적법성 불가 |
| 11 | §8.3 three finite constructions | `FIXED_SIGNATURE_EXISTENCE_SCOPE_GAP` | stage 2/3/4 각 증인에 필요한 종류·정렬·값을 포함한 적절한 시그니처 선택 가능해야 함 |
| 12 | Th9.2 + Construction8.7 | `FIXED_SIGNATURE_EXISTENCE_SCOPE_GAP` | 최소 두 zero-bearing 종류와 2원소 배치를 허용한 시그니처에 대한 **존재적 비분류**, 모든 시그니처의 비분류 아님 |
| 13 | §2 inherited FVI convention | `SUPPORTED_RELATIVE_FIXED_BASE` | 구조적 고정 기반으로서의 Stage VI; 임의 Formation v4.5 전체 무조건 증명 아님 |

증거 등급은 `PROVED_IN_DECLARED_BACKGROUND`와 `PROOF_GAP`를 혼용하지 않는다: 미해결 문장 자체는 `PROOF_GAP`/`NEEDS_SCOPE_CLARIFICATION`이며 위 조건부 일반 논증은 별개로 지지된다.

## 3. 실제 독립 Python 검사와 수학적 의미

`verify_p31_main_theorem_scope.py`는 13개 정해진 기대 관찰을 실행하고 `P31_EXPECTED_EVIDENCE.json`으로 재현한다.

- 제2절 규정상 배제되지 않는 공집합 후보 시그니처: 정규 모형 하나, 네 비교단계 자기 항등, 공리 모두 공허하게 참, 단계 2·3·4 및 같은 요약·비동형 충돌쌍 없음.
- 선행조건이 없는 단일 속성 시그니처에서 PII가 PI 위반 전모형에 대해서도 공허하게 참.
- 같은 **비어 있지 않은 선행조건 시그니처**에서 PI 위반/PII 만족, PII 위반/PI 만족 전모형 두 개.
- 각각 충분한 속성 종류·값 구조를 공급한 (서로 다른) 고정 시그니처에서 stage2/stage3/stage4 분기 유한 증인 재현.

**경계:** 이 코드는 공집합 시그니처의 확장제시를 일률적으로 거부하는 일반 validator가 아니라, P30에서 이미 분리한 **정규 제한 가족 해석에 대한 판별 증거**이다. 정리의 논리적 범위를 확정하는 것은 수학적 문장 해석 및 전칭/존재 양화 감사이고, 유한 코드 자체가 이를 보편 증명하는 것은 아니다.

## 4. 종결 전 수정사항 관리 및 원고 동결 규칙

- **필수 명세결정 S-01:** P30 잉여 원시좌표를 `canonical restricted data`로 제한할지, `extended presentation`과 `core-equivalence`를 분리할지 선택.
- **필수 정리전제 S-02:** P29 Th8.4의 `typed compatible primitive presentation` 전제를 명확히 하여 PI·PII와 별도 검증.
- **필수 명세결정 S-03:** P30 Def7.1의 `I1..I5` 비교집합을 원문 범위대로 성분식으로 명료화하고 strict iso와 대응성 재검증.
- **신규 필수 정리범위 S-04:** §11 (3), (11), (12)의 **임의 고정 시그니처 보편 진술 vs 적절한 시그니처의 존재적 독립/증인** 구분. 문장/증명 의존범위 갱신은 FPA 종결을 위한 보류된 개정 작업으로 따로 기록.
- **검사 S-05:** §11의 다른 항목도 같은 방식으로 전칭/존재 해석을 혼동하지 않는지 최종 언어 판독.

논문 LaTeX·PDF는 사용자의 지시에 따라 **내부 FPA 감사 작업이 끝날 때까지 편집하지 않는다**. 단, 발견한 `PROOF_GAP`을 사라진 것으로 간주하여 FPA를 `CLOSED`로 표시하지 않는다. 실질적인 감사가 종결 준비 상태에 이르면 보류 수정사항을 일괄 반영한 뒤 **수정판과 증명 의무의 대응검증**을 마쳐야 정식 `CLOSED`를 판정할 수 있다. 형성공리계 전역 FPA, 외부 심사는 별개.

## 5. 판정

```
AUDIT_ID: PA-P31-20261028-SECTION11-REVERSE-DEPENDENCY-001
P27_EN_KR_SOURCE_EDITED: NO
P31_13_ITEMS_REVIEWED: 13/13
P31_EXPECTED_FINITE_OBSERVATIONS: 13/13
P31_NEW_SCOPE_GAP: MAIN_THEOREM_ITEM_3_11_12_UNDER_FIXED_SIGNATURE_UNIVERSAL_READING
P31_OLD_OPEN: P29_WELL_TYPED / P30_SURPLUS / P30_IK_COMPONENT_FORMULA
MATHEMATICAL_VERDICT: PROOF_GAP_IN_FIXED_SIGNATURE_UNIVERSAL_READING
DSD_AUDIT_VERDICT: PASS_WITH_REFINEMENT
REVISION_NEED: CLARIFICATION_AND_DEPENDENCY_REAUDIT_DEFERRED
INDEPENDENT_EXTERNAL_VALIDATION: not_established
WHOLE_PROPERTY_FPA: OPEN
```

후속 권장순서: 새 발견사항을 원고에 즉시 편집하지 않고 (a) §11(3·11·12) 범위 교차검토, (b) 제2절 정규 데이터 의미론과 제7절 I_k 결합법 재검산, (c) 충분한 일반 증명 단계별 완료 대장 만들기. 원시공리 PI/PII 자체의 불일치가 검출된 것은 아님.