# PA-P29 — 속성공리계 P27 동결본의 표준 유한 실현 정리 전제 및 일반 증명 의무 감사

- 감사일: 2026-10-28 KST
- 저자: Kwon Dominicus
- 감사 기준: P27 영문·국문 LaTeX. **원고 편집·출판·Zenodo 갱신 금지** (사용자 지시: FPA 전체 종결 후 일괄 편집)
- 영문 P27 SHA256: `51c194ec33f802a2061b68b3521fdb831f0f754a0386fa72f8e89a39efff7bdb`
- 국문 P27 SHA256: `a643ea619f9594142bfc09b9f486c948cf0a85679a3b2a8a43bc731a1e108fbb`

## 1. 새로 확인한 증명 의무: §8.2 정리 8.5 표준 유한 실현

영문 원문은 “Let finite auxiliary carriers, a finite declared property family, finite applicability and prerequisite-satisfaction sets, and finite partial assignment maps be given over a fixed Stage-VI formation record and shared signature. If ... Dom(Ξ)⊆Ap∩DepSat ... then ... unique property-finite full model”이라고 명시한다. 국문판의 같은 정리도 유사한 문장을 사용한다. 반면 증명 첫 두 문장은 포함관계가 PI·PII라는 점에서 곧바로 **supplied data form a primitive property core**라고 추론한다.

**정확한 논리 경계:** `Dom(Ξ)⊆Ap∩DepSat`은 입력의 적법한 타입·공역·필수 좌표 조건을 *함의하지 않는다*. 유한성과 포함관계만을 전제로 하는 문자 그대로의 해석에서는 유일한 완전모형을 보장할 수 없다.

기본 예시: 공유 속성시그니처의 단항 종류 `p`에 대해 `X_A(u)={a}`이고 `X_{A,p}={(a)}`인데, `Ap_{A,p}={(ghost)}`, `Sat_{A,p,d}={(ghost)}`, `DomΞ=∅`로 둔다. 모든 제공 자료가 유한하고 표시된 포함관계 `∅⊆Ap∩DepSat`은 참이다. 그러나 `Ap⊄X_{A,p}` 및 `Sat_d⊄X_{A,p}`이므로 정의 2.5의 **타입 전모형 자체가 아니다**. 이는 *의도한 정리의 적법 타입 입력을 반증하는 모형*이 아니라, **타입 조건이 생략된 문장으로부터 결론을 얻을 수 없음을 보이는 반례**이다. 잘못된 값공역과 arity에서도 별도의 음성 예시를 얻는다.

정리의 증명은 다음의 **조건부 형태에서 일반 ZFC 논증으로 유효**하다: (T) 제공 자료가 정의 2.5에 따른 적법한 타입 전모형이고, 모든 필수 원시좌표가 선언·프로필 이용가능성의 규약에 맞게 제공된다. (I) 모든 선언·프로필 이용가능한 종류에 대해 `DomΞ⊆Ap∩DepSat`. (F) 속성 유한성의 정의를 만족한다. 그러면 (T)+(I)로 PI·PII를 만족한 원시코어이고, C1은 그 코어에 대한 결정론적 함수적 확장이다. 유도 정의역·레코드는 유한이다. 이 일반 논증에는 운반체 전체가 유한하거나 적분·물리 의미가 필요하지 않다.

**판정:** `PROOF_GAP` if premise (T) is not inherited, `PASS_WITH_BOUNDARY` under the manuscript-wide reading that all supplied “primitive property data” are by definition typed. `REVISION_NEED: CLARIFICATION` (논문 편집은 현재 수행하지 않음). 이는 제11절 결론 (10)의 “finite compatible primitive presentation”에 이미 나타난 **compatible** 조건을 제8절 정리의 형식 전제로 정확히 복원하면 정리의 의도와 정합적이다.

## 2. §2–3: 원시자료와 C1

- `Def2.5`: 선언·프로필 이용가능성의 양화를 전체 항목 (2)–(4)에 동일하게 적용해야 한다는 **범위 명료화 의무**가 남는다. 특히 `required`와 `forbidden`을 혼동하면 안 되므로, 잉여 원시좌표를 금지할지/무시할지 자동 결정하지 않는다.
- 적법한 전모형 + PI·PII → 원시코어. `CompProp(P)=(P,D(P))`, `RedProp(P,D(P))=P`; 완전모형의 파생 좌표가 동일 정의에서 산출되는 한 반대 합성도 항등이다. 이는 순수 집합론적 정의 기반으로 일반 크기에 대해 조건부 성립한다. **원시자료를 요약·직렬화하며 버리는 구현과 동일시하지 않는다.**

## 3. §6: 사상·매장·엄격 동형의 일반 단계

- 두 전방 사상 `f:A→B`, `g:B→C`에 대해 출발의 선언된 이용가능 프로필은 `(F1),(F2)`에 의해 중간/종점 모두 이용가능. 유한 순서 프로필의 곱 사상은 성분별 정의되어 `(g∘f)_ϖ=g_ϖ∘f_ϖ`가 성립. 원시집합의 상 포함과 값 보존은 관계 합성/등식의 추이로 보존. 각 `id_A`와 사상 합성으로 범주를 이룬다. 분기·무한 운반체와 독립된 **일반 조건부 논증**이다.
- 매장: 보조 운반체 사상의 단사성은 합성에서 보존. E1/E2/E3는 각 `R_A(x)↔R_B(fx)↔R_C(gfx)`로 합성 시 보존된다. 선행조건이 비었을 때 E2만 공허하고 E1/E3는 유지되어야 한다.
- 엄격 동형: E1–E3를 만족하는 매장에 S1(전단사), S2(이용 가능 보조 타입 집합 동일), S3(선언 종류 동일)를 추가하면 이용 가능한 곱사상은 전단사가 되고 역성분 함수는 반영 조건과 F5 값을 역방향 보존하여 S4를 도출한다. 기존 S2/S3 반례는 여전히 유효하다.
- 잔여 의무: Def2.5의 **잉여 자료 좌표**를 원시코어의 데이터 동일성으로 볼지, strict 비교에서 무시하는 구별된 부가정보로 볼지 확정해야 한다. 이를 자동으로 정리 위반으로 판정하지 않는다.

## 4. §7: 단계별 비교 집합의 도출 범위

`I_k(A,B)`는 해당 단계까지 비교조건을 만족하는 **모든 운반체 전단사족**이다. 조건을 표준적으로 명시한 상태라면 포함관계 `I_5⊆I_4⊆⋯⊆I_1`와 결정론 C1에 의한 `I_4=I_5`, 그리고 `I_4≠∅` ↔ strict 동형은 정의와 §6으로부터 따름. 역사상으로 대칭, 동형의 전·후합성으로 불변성을 얻는다. 

**잔여 형식화 의무:** 원문 `Def7.1`의 “strict-comparison conditions visible through property stage”를 실제 성분·관계·값 보존 공식으로 전개하여, `I_4`의 원소와 S1–S4 엄격 동형의 일대일 일치를 명시적으로 확인해야 무조건적인 FPA 종료가 가능하다. 현재 일반 증명은 자연스러운 단계해석을 고정했을 때의 조건부 증명이다.

## 5. 한정된 새로운 계산 증거

본 감사의 별도 Python은 상기 ‘표시된 포함관계만으로 타입 적법성을 얻을 수 없는’ 경우를 4가지로 분리하였고, 정상 사례 3가지 및 운반체 크기 0/1/2의 적법한 코어 1+6+36개에서 C1/축약 입력보존을 확인했다. **일반 증명은 수학적 논증에만 근거하며, 유한 코드가 무한 경우를 증명한다는 주장 없음.**

## 6. 결론과 다음 순서

- `P29_FROZEN_SOURCE`: YES (영문/국문 TeX 및 원래 Zenodo 미변경)
- `P29_TH8_FINITE_REALIZATION`: PROOF_GAP_IF_UNTYPED / PROVED_CONDITIONALLY_IF_WELL_TYPED
- `P29_MAP_EMBEDDING_ISO`: GENERAL_CONDITIONAL_PROOF_SUPPORTED
- `P29_I4_I5`: GENERAL_CONDITIONAL_PROOF_SUPPORTED / I_k_EXPLICIT_SCHEMA_OPEN
- `P29_NEW_PRIMITIVE_AXIOM_CONTRADICTION`: NOT_FOUND
- `P29_MANUSCRIPT_REVISION`: DEFERRED_UNTIL_FPA_CLOSED
- `WHOLE_PROPERTY_FPA`: OPEN

**다음 감사:** (1) Def2.5 ‘not required’ 잉여좌표의 존재/동일성 의미를 법적 모형과 함께 결정 (2) Def7.1의 단계비교집합을 완전한 집합론 공식으로 전개해 §6 strict 증명과 일대일 비교 (3) 제11절 13개 결론의 전제장부에 P29 결과 전파. 문제 발견은 보존하되, 수리 없이 논문을 수정하거나 새로 출판하지 않는다.