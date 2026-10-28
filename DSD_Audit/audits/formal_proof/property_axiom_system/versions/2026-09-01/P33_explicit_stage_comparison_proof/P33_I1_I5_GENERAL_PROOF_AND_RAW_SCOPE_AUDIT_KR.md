# PA-P33 — P27 동결본 제7절 단계 비교집합 I1–I5의 일반 집합론적 정식화 및 역감사

- 날짜: 2026-10-28 KST. 저자: Kwon Dominicus.
- 기준: P27 영문 `51c194ec33f802a2061b68b3521fdb831f0f754a0386fa72f8e89a39efff7bdb`, 국문 `a643ea619f9594142bfc09b9f486c948cf0a85679a3b2a8a43bc731a1e108fbb` (모두 **동결·미수정**).
- 선행: P29 (typed presentation), P30 (raw vs active), P31 (§11 scope), P32 (exact C1 inverse vs normalization).
- 판정 원칙: **원문 Def7.1의 설명을 아래 수식으로 구체화하는 독립 증명**이며, 원문에 이미 동등한 형식문이 존재한다고 단정하지 않음. A 정규 제한 가족을 임시 전제로 삼으며 B는 별도 판별.

## 1. 고정 모형 범주와 수학적 전제

하나의 고정된 `(FVI,Sprop)`에 대한 두 **적법한 완전 속성모형** A,B를 취한다. `T_A=Dom X_A^{aux}`, `T_B=Dom X_B^{aux}`. 공유 시그니처의 모든 속성 프로필은 길이 `m>=1`인 유한 순서열이고, 각 기저 운반체는 집합이며, 상속 운반체 사상은 **항등**이다. A/B 원시 가족의 정의역을 `Act(A)={ω∈Π_A:Av_A(ω)}`, `SatIdx(A)={(ω,d):ω∈Act(A),d∈δ(ω)}`에 정확히 고정한 **작업 규약 A**를 가정한다. 이는 P27에 내재한다고 확정하지 않은 조건부 의미론이다.

`T_A≠T_B`이면 `I_1=...=I_5=∅`. 그렇지 않으면
```text
Bij_T(A,B) = product_{s in T_A} Bij(X_A(s),X_B(s)).
```
이 제품은 set-indexed family로서 집합이다(기저가 집합, 함수집합과 그 유한/집합곱을 사용). 어느 인자도 전단사가 없으면 전체는 공집합이며, `T_A=T_B=∅`일 때 전단사가 하나인 빈 함수족을 포함한다. `f=(f_s)`마다 inherited sort에는 항등을 두고, 이용 가능한 속성 `ω`의 프로필 `σ(ω)=(s_1,...,s_m)`에 대해 `f_ω(x_1,...,x_m)=(f_{s_1}(x_1),...,f_{s_m}(x_m))`. 반복 정렬·혼합 정렬·공집합 운반체에도 정의된다. 전단사 성분과 동일한 정렬의 역성분으로부터 `f_ω`는 전단사다.

## 2. 명시적인 다섯 집합

```text
I1(A,B) = Bij_T(A,B).
I2(A,B) = {f in I1 : Pi_A = Pi_B}.
I3(A,B) = {f in I2 : for all w in Pi_A with Av_A(w),
            f_w[Ap_A,w] = Ap_B,w
            and for all d in delta(w),
            f_w[Sat_A,w,d] = Sat_B,w,d}.
I4(A,B) = {f in I3 : for all w in Pi_A with Av_A(w),
            f_w[D_A,w] = D_B,w
            and for all x in D_A,w,
            Xi_B,w(f_w(x)) = Xi_A,w(x)}.
I5(A,B) = {f in I4 : f transports the C1-derived domains,
            prerequisite intersections, statuses and typed records}.
```
각 `I_k`는 `Bij_T`의 분리로 얻은 집합이며, “어느 후보 하나가 실패”와 “I_k 자체가 공집합”은 구분한다. `T_A=T_B`이면 활성/미제공 프로필 상태가 양쪽에서 동일하다.

## 3. 일반 증명 — 전제 A 아래

**명제 1: 내포.** 각 단계는 앞 단계의 조건을 강화하므로 `I5⊆I4⊆I3⊆I2⊆I1` (직접 정의).

**명제 2: `I4=I5`.** `f∈I4`이면 선언·프로필 이용가능성, Ap, 모든 Sat, Dom Xi 및 실제 할당값을 보존한다. `DepSat`은 Sat들의 유한 교집합이며 빈 전제조건 경우 typed product 전체이므로 `f_w`의 전단사에 의해 운반된다. 상태는 순서 있는 조건 분기(undeclared/unavailable/inapplicable/prerequisite-unsatisfied/undefined/defined zero/nonzero)로 결정된다. `PropRec`의 각 `(w,x,z)`는 `(w,f_w(x),z)`에 일대일 대응한다. 따라서 C1 파생 전 좌표 보존, `f∈I5`. 역포함은 정의. 운반체가 무한이어도 일반 논증 동일.

**명제 3: `I4(A,B)≠∅ iff A≅_{L,prop}B`.** `f∈I4`이면 F1/F2는 제공 종류·선언 집합 일치에서, F3/F4는 상-동일성에서, F5는 할당 정의역 상-동일성과 값 보존에서 따른다. 전단사 프로필 사상은 E1–E3 반영도 보장한다. S1(각 성분 전단사), S2(공급 종류 동일), S3(선언 동일)가 충족되며, P27 Th6.8에 의해 역사상 S4가 성립한다. 역으로 P27 strict iso의 F/E/S 조건은 `I4`의 모든 성분 조건을 만족한다. **비교관계는 원시 활성 자료에 대해서만** 형성함을 명시.

**명제 4: first branching.** `A\not≅B`이면 I4가 공집합이고 I1..I4는 유한한 단계 순서를 가지므로 `min{k∈{1,2,3,4}:I_k=∅}`가 정의된다. 단계 조건은 전단사의 역 및 고정 기반 strict 동형과의 전후합성에 대해 보존되므로 공집합성 및 `b(A,B)`는 대칭·strict 동형 불변이다. I4=I5로 단계 5는 독립 최초 분기가 불가능하다.

**정확한 사용범위:** 위 네 명제는 `A/B`의 고정 Stage-VI와 시그니처, 타입 적법성, 정규 제한 인덱스, C1 정의적 완성을 사용한다. 무한 자료형의 유한 전수열거·적분·물리 가정은 요구하지 않는다. 별도 외부 형식 검증 결과는 아니다.

## 4. 확장된 raw 제시(B)에서의 갈림길

P32의 A/B 실험은 서로 strict identity core iso이지만 `raw Stage3` 가족은 다르다. 따라서 위 `I3`를 **활성 좌표 조건**이 아니라 `raw P^{<=3}` 전체의 문자 그대로의 동일성 조건으로 강화하면 `I4_raw=∅`일 수 있지만 strict core iso는 여전히 성립한다. 이 강화된 집합에 대해 `I4_raw≠∅ iff strict core iso`는 성립하지 않는다. `I3_active`를 사용하면 strict 대응은 유지하나 raw 전체 기술자 동형을 뜻하지 않는다.

B에서도 두 개념을 별도 정의하면 모순은 없으나, 현재 P27 Def7.1의 “strict-comparison conditions visible through ...”에서 **active/raw 비교 중 어느 쪽인지** 정해야 전체 FPA를 종료할 수 있다.

## 5. 이번 판정과 다음 증명 의무

- `MATHEMATICAL_VERDICT=PROVED_IN_DECLARED_BACKGROUND_CONDITIONAL_ON_A` (위 네 명제)
- `DSD_AUDIT_VERDICT=PASS_WITH_BOUNDARY`
- `REVISION_NEED=CLARIFICATION_DEFERRED`
- `ORIGINAL_DEF7_1_EXACT_SCHEMA=NOT_YET_FIXED`
- `THEOREM11_ITEM9=SUPPORTED_IF_A_ADOPTED`
- `P31_SCOPE_3_11_12=OPEN`
- `P29_TYPED_FINITE_REALIZATION_PREMISE=OPEN`
- `PROPERTY_FPA=OPEN`, `EXTERNAL_VALIDATION=not_established`
- `P27_EN_KR_TEX_PDF_ZENODO_EDITED=NO`

관련 판별 Python 17/17 및 frozen source 해시는 [P32 CI #40692911750](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40692911750)에서 두 Python 버전으로 확인되었다. 이번 문서의 집합론 증명은 **기존 P32 유한 테스트와 구분되는 논증**이므로 그 CI 실행이 이 일반 증명을 자동 인증했다고 주장하지 않는다.

**다음 FPA:** P31의 fixed-signature 의무 (3),(11),(12)를 계열 수준의 존재/고정 시그니처 조건으로 분해하고, 논문 변경 없이 정확한 정리 진술 후보를 증명·반례별 대장에 기록한다. 그 다음 P29 타입 전제와 남은 종결 게이트를 합쳐 검토.
