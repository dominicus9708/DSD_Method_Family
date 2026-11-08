# PA-P49 — 속성공리계 최소 선택 계약·선택 독립 절별 개정 준비 감사

**감사 기준일:** 2026-11-09 KST  
**저자:** Kwon Dominicus  
**대상:** P27 EN/KR 동결 논문, P42–P48 선행 감사 및 형성공리계 Stage-VI 인터페이스  
**범위:** 판단을 위한 명세·논리 의존성 감사만 수행; 논문/Zenodo/선행 기록 수정 없음.

## 0. 선행 출처와 동일성

- P27 EN frozen SHA256: 51c194ec33f802a2061b68b3521fdb831f0f754a0386fa72f8e89a39efff7bdb
- P27 KR frozen SHA256: a643ea619f9594142bfc09b9f486c948cf0a85679a3b2a8a43bc731a1e108fbb
- P27 EN 원본: ../P27_independent_math_revision/DSD_Property_Axiom_System_EN_P27_REVISED.tex
- P42: 20증명+제11절 13항의 조건부 수정 대장.
- P43: 16절/30소절/56번호/78개 표시수식의 영·국문 형식적 대응 감사.
- P45: A/B1/B2 및 N∘i=id 하의 관찰 인수분해 결과.
- P46: I_k_raw ⊆ I_k_active 조건부 및 확장 최초분기 beta_raw ≤ beta_active.
- P47: typed raw 키 부재 vs 명시적 공값을 구분할 필요성.
- P48: DSD 방법군 역할과 PAS raw 저장을 자동 동일시할 수 없다는 조건부 결과.

본 단계는 이전 CI 성공을 새 실행으로 표기하지 않으며 외부 평가와 모든 집합론적 모형에 대한 기계 검증을 주장하지 않는다. 사용자가 제공한 구판 PDF(2026-09-01)와 저장소 P27 개정 원고는 동일 버전으로 간주하지 않으며 P49의 주 논증은 P27 동결 TeX를 기준으로 한다.

## 1. 최소 선택 계약 — 7개 독립 명세 필드

K1. **허용 primitive family 영역:** 미선언 property와 profile unavailable property에 대한 추가 raw key의 존재가 적법한가. 활성좌표만 허용하는 A와 typed raw 잉여를 허용하는 B1/B2를 나눌 핵심 선행 결정이다.

K2. **raw typing와 인덱스 존재:** raw kind는 공유 후보 시그니처에 속해야 하는가, profile unavailable raw 값은 허용하는가, raw Ap/Sat/Xi의 키가 부재한 상태와 키가 존재하나 명시적으로 공집합/공함수인 상태를 구분하는가. 임의의 값을 적법한 typed carrier 없이 raw에 넣어선 안 된다.

K3. **활성화 사상 N과 no-surplus 포함 i:** B1/B2를 채택할 때 N:B→A의 정확한 삭제/정규화 규칙과 i:A→B, N∘i=id_A를 명시한다. B를 보존하지 않기로 하면 이 사상은 외부 감사 비교의 가정일 뿐 PAS 원시구조가 아니다.

K4. **완전 기술자와 C1 환원 범위:** 완성 후 primitive reduction이 잊지 않고 되돌려야 할 저장 좌표를 명시한다. B의 원시 raw를 기술자에 넣기로 하면서 환원에서 잊으면 Red(Comp(P))=P가 깨진다. A처럼 원래 raw가 없다면 문제가 발생하지 않는다.

K5. **동형의 비교 대상:** A는 활성 strict, B1은 raw 저장과 활성 strict를 구분, B2는 raw 키와 값을 비교하는 강화 strict. B2의 raw 비교를 기존 P27 정의 6.3과 동일하다고 부르지 않는다. 이 선택은 도출된 결과가 아닌 정의 변경이다.

K6. **단계비교와 최초분기:** I1–I5를 K5의 동형과 동일한 primitive coordinate family 위에서 구성한다. raw Stage-3/4 조건을 추가한다면 비교집합과 b_prop의 정의 및 불변성 증명을 동시 갱신해야 한다. I4=I5는 C1 완성이 해당 선택의 primitive data 전체에서 정의적으로 결정된다는 전제 아래 유지할 수 있다.

K7. **외부 과업관찰·출처·전이:** 원천자료 provenance, 외부 기준, 방법군 별 observation T 및 시간에 따른 raw→active 전이는 PAS primitive인지 별도 ledger/bridge인지 구분한다. 보존 필요성과 PAS primitive 소속은 같은 질문이 아니다.

**독립성 경계:** K1을 정하지 않고도 PI/PII의 활성 soundness는 검토 가능하다. K5가 결정되지 않으면 §6 strict와 §7 최초분기의 최종 진위를 한 의미론으로 확정할 수 없다. K7은 실제 과업 요구에 의존하며 K1/K5만으로 자동 결정되지 않는다.

## 2. 선택지 판정 — 결론 아닌 수정 조건

| 후보 | K1 raw 적법영역 | K4 C1 환원 | K5 strict | 조건 |
|---|---|---|---|---|
| A | 활성 인덱스에 정확히 제한 | 활성 primitive 전체를 그대로 되돌림 | P27 활성 strict 유지 | 외부 provenance 저장/전이가 필요하면 별도 인터페이스 |
| B1 | 적법 typed raw 잉여를 보존 | raw primitive도 정확히 되돌림 | strict는 활성 N(A)만 비교 | 완전 기술자 동일성과 strict 동형은 의도적으로 다른 판별 |
| B2 | 적법 typed raw 잉여를 보존 | raw primitive도 정확히 되돌림 | 키 존재 및 값까지 포함한 강화 raw strict | §6–7 증명과 Stage-3/4 비교 재구성 필요 |

세 후보를 채택·혼합·폐기하지 않는다. 각 후보는 그 정의에 필요한 가정을 모두 적으면 서로 다른 정합적인 형식 과제가 된다. 대안의 장단점을 독립 검증 결과와 혼동하지 않는다.

## 3. 선택 무관하게 확보 가능한 수정 준비

- **§1/Abstract:** general typed property core, PI/PII, Stage-VI fixed, 기하 선택 특수화 원칙은 유지할 수 있다. 다만 'complete/strict'를 원시 raw 전체까지 보존한다는 뜻으로 확장하는 표현은 K4/K5 종결 전 보류.
- **§2.1–2.3:** Stage-VI 상속, 공유 시그니처, typed profile의 기본 전제는 유지. raw 허용 범위의 결정을 소급하지 않는다.
- **§2.4–2.5:** P27의 'not required'를 'forbidden' 또는 'permitted'로 몰래 읽지 않는다. raw 인덱스/부재와 명시적 공값 규칙을 K1/K2 이후 정의. 현재는 수정 전 표식만 유지.
- **§3:** 선언·profile 가용 활성 종류에 대한 PI/PII와 정의역/상태구분은 공통 증명층. C1의 primitive 환원 대상은 K4 조건부.
- **§4:** 한 입력 반모형과 no-converse 국소 증명은 고정된 증인 시그니처 범위. 임의의 빈 후보 시그니처에서 비공허 증인을 자동 도출하지 않는다.
- **§5:** 완전 기술자에 raw가 들어가는지 K1/K4에 종속. optional representation 패키지의 독립성은 유지.
- **§6:** 현행 forward/embedding/strict가 활성 좌표를 비교하는지 원문대로 기록. B2 raw strict을 택하면 적법 raw 좌표에 대한 사상/반사/가역성 조건 추가 필요. 반대로 A/B1은 원문 활성 strict와 구분 규정 유지.
- **§7:** I1–I5는 §6과 한 계약을 공유해야 한다. 활성/강화 raw 비교집합을 혼합해 최초분기 정리를 증명하지 않는다. 적법한 공통 비교족에서 raw 조건 추가는 I_k_raw⊆I_k_active를 줄 수 있으나 무조건적인 동등성은 아니다.
- **§8:** finite realization은 typing T, finiteness F, soundness inclusion I가 모두 확인된 primitive presentation의 조건부 정리. 비공허 증인은 시그니처/입력/값/필요조건의 이용 가능성 명시.
- **§9:** summary domain은 zero-bearing 및 profile-available 등 명시 조건에서만 정의. summary collision은 strict 비교 정의 변경 시 대응 재검증.
- **§10:** realized-axis, static aggregation, dynamics는 독립 선택 후속층으로 유지. raw 보존으로 시간 전이를 자동 도출 금지.
- **§11:** (1)(2)(4)(13)의 개념적 범위, (3) 독립성의 증인 조건, (5) C1의 원시 환원, (6)–(9) strict/branch의 K5/K6 의존, (10) typing T, (11)(12) 존재 증인 범위를 서로 분리. 고정 임의 시그니처에 대한 보편적인 비공허 증인 주장은 쓰지 않는다.
- **§12–13 및 부록 A–C:** 명세 선택 후 공통 정의/용어/영문-국문 대응 확인. 원고 주석 경계는 저자 관례인 '% -----' 절별로 유지.

**개정 실행 순서:** (a) K1/K2 (b) K3/K4 (c) K5/K6 (d) §2/§3/§5/§6/§7 문장과 정리 (e) §8·§11 양화·타입 범위 (f) §1/abstract, §9–13, 부록 (g) EN/KR 수식·용어 정합성 재감사 (h) 개정 원고 별도 버전 잠금. 현재는 어느 단계의 원고 편집도 실행하지 않는다.

## 4. 신규 논리 점검 및 반례 경계

**M49-1 (원시환원 보존 필요조건):** 원시 모형 P,Q에 대해 Comp(P)=Comp(Q)이면서 P≠Q라면, 동일한 deterministic Red에 대해 Red(Comp(P))=P 및 Red(Comp(Q))=Q는 동시에 성립할 수 없다. 증명은 같은 Comp 출력에 Red를 적용하면 같은 결과가 나와야 한다는 함수의 단일값 성질. 따라서 원시 raw 차이를 버리는 완성을 채택하면서 모든 raw에 대한 정확한 C1 역법칙을 주장할 수 없다.

**M49-2 (동형-분기 계약 정합의 충분조건):** 동일한 정해진 typed primitive coordinate family에 대해 각 Stage-k 비교집합을 누적된 strict 비교조건으로 정의하고 C1 completion이 Stage-4까지 좌표의 정의적 함수라면 I5=I4가 성립한다. 이는 K5/K6이 일치하는 한 A, B1, B2 각각에 대해 적용할 수 있지만 어느 후보가 원문에 이미 채택됐다는 증거는 아니다.

**M49-3 (raw와 provenance 독립성):** 동일 raw P에 다른 외부 레저 e1≠e2를 결합한 (P,e1), (P,e2)는 PAS raw projection으로 구별되지 않는다. 따라서 외부 감사 근거 보존이라는 목표만으로 K1= B2가 필요하다는 주장은 성립하지 않는다. 별도의 Enc/bridge를 공급하는 모델은 가능하다.

**M49-4 (선택 무관한 일관성 한계):** 현재 PI/PII는 활성 property의 정의된 값이 Ap∩DepSat에 들어간다는 soundness만 준다. raw coordinate의 원시 저장 범위, 외부 출처, strict 동형의 비교 강도, 시간 전이는 PI/PII의 논리적 귀결이 아니다.

위 주장은 입력된 전제에서의 일반 집합론적 논증이다. 절별 분류를 해놓았다는 사실이나 유한 테스트 성공으로 다른 논증까지 완료되었다고 해석하지 않는다.

## 5. 증명 의무 및 종료 관문

- S-01: 허용 primitive raw 인덱스의 원문 의미론 확정 — OPEN.
- S-03: S-01에서 이어지는 완전 기술자/strict/I_k/C1의 동일한 비교 대상 확정 — OPEN.
- S-02: §8 finite realization의 typing T 확인 및 적법성 전제 원문 반영 — OPEN.
- S-04: 비공허 국소 증인과 임의 고정 시그니처 전칭의 구분, §11 주장별 양화 범위 반영 — OPEN.
- EN/KR 전체 자연어 증명 동치·독립 외부 형식화 — NOT CERTIFIED.
- 원고/Zenodo 수정 — NO.
- 새 Python 실행 / GitHub Actions — NOT RUN (본 단계는 정의 계약 및 절별 수정 의존성 감사).
- 전체 FPA — OPEN.

**P49 판정:** PRE-REVISION-CONTRACT-READY / SEMANTICS-UNDECIDED / SOURCE-FROZEN / FPA-OPEN.  
**후속:** P50에서는 K1–K7에 대한 독립적인 선택 강제 가능성/불가능성 점검과 절별 증명 의무를 재정렬할 수 있으나 저자의 의미론적 결정을 대체하거나 원고를 편집하지 않는다.
