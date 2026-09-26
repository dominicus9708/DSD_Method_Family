# 개선 알고리즘 논의 — DSD 분석론

Status: **TEMPORARY / NON-CANONICAL / DISCUSSION-ONLY**  
Branch: `tmp/analysis-audit-improvement-algorithm-discussion-20260926`  
Created: 2026-09-26 KST

## 0. 운영 원칙

이 폴더는 기존 DSD Analysis 정본을 수정하지 않고, 난제 실전에서 반복적으로 나타난 **추가 후보 알고리즘(delta)** 만 임시로 분리해 검토하기 위한 작업 공간이다.

- 기존 `methods/01_analysis/`의 역할·경계와 역사적 Analysis corpus는 정본으로 유지한다.
- 여기의 후보는 **채택된 DSD Analysis 규칙이 아니다**.
- 원 계산·대규모 결과·증명 트리를 복제하지 않는다.
- 각 후보는 GitHub commit / Notion page / 기존 정본 규칙을 가리키는 **근거 포인터**만 보존한다.
- 사용자와의 논의 및 비교 검증 전에는 main 또는 정본 프로토콜로 병합하지 않는다.
- 최종 상태는 `ADOPT / ADOPT_WITH_LIMITS / KEEP_EXPERIMENTAL / REJECT / DELETE_AFTER_DISCUSSION` 중 하나로 결정한다.

## 1. 보존되는 원본 Analysis 코어

현재 정본의 핵심은 한 선언된 대상을 필요한 DSD 층위만 사용해 구조적으로 분해·재표현하는 것이다.

보존할 기본 점검:
- candidate vs admitted / realized
- undefined vs zero vs absence
- applicability / prerequisite 상태
- 명시적 correspondence / bridge
- aggregate equality vs structural equality
- first branching / boundary
- 외부 분야의 증명·검증 기준과 DSD 분석 결과의 분리

아래 후보들은 이 코어를 대체하지 않고, **실전에서 반복된 추가 절차가 일반화 가능한지** 시험한다.

## 2. 실전에서 추출된 후보 delta

### ANA-Δ01 — Minimum Sufficient Resolution / 최소 충분 해상도
최종 목표가 요구하는 수준보다 강한 중간명제를 자동으로 본선 목표로 승격하지 않는다.

검사:
1. 최종 claim 또는 theorem hinge를 고정한다.
2. 각 중간 목표가 최종 목표에 요구되는 최소 해상도보다 강한지 표시한다.
3. 더 약한 sufficient target이 존재하면 원래 강한 목표는 optional/dormant route로 재분류한다.

실전 근거:
- Riemann j=2에서 pointwise/uniform/sharp variance 목표를 global bridge보다 강한 충분조건으로 재분류.
- 최소 fixed-radial bridge를 기존 (K^8)보다 약한 (K^9) 수준으로 재정의.

### ANA-Δ02 — Dependency Frontier Compression / 의존성 전선 압축
열려 있는 세부 문제 수를 그대로 “남은 독립 장벽 수”로 세지 않는다.

검사:
1. 최종 목표까지의 dependency DAG를 만든다.
2. 동일 부모를 닫는 여러 충분경로는 독립 gate와 공격법을 구분한다.
3. 실제로 닫혀야 하는 최소 gate 집합만 active frontier로 남긴다.
4. 나머지는 삭제하지 않고 dormant/frozen으로 보존한다.

실전 근거:
- Navier–Stokes pre-M23 전선을 두 master gate로 압축.
- Riemann j=2에서 OPEN-93과 최소 bridge 중심으로 다수의 stronger route를 dormant 처리.

### ANA-Δ03 — Resolution Escalation Detector / 해상도 상승 탐지
다음 변환이 실제 부모 목표에 필요한지 별도 검사한다.

후보 escalation:
- weighted average -> uniform supremum
- global -> pointwise
- signed sum -> absolute mass
- first moment -> second moment / (L^2)
- finite/support-sensitive object -> reduced aggregate
- exact parent quadratic form -> 여러 강한 보조 norm

불필요한 escalation은 “오류”가 아니라 **과잉 충분조건**으로 표시한다.

### ANA-Δ04 — Common Latent Object / Duplicate-Branch Audit
서로 다른 표기·물리/쌍대 표현·분기명이 동일한 underlying object의 변환 또는 contraction인지 먼저 검사한다.

출력 분류:
- EXACT_EQUIVALENT
- PARSEVAL_OR_ISOMETRIC_DUAL
- FIXED_WEIGHT_EQUIVALENT
- ONE_WAY_SUFFICIENT
- SIBLING_CONTRACTIONS
- INDEPENDENT

실전 근거:
- Riemann distinct-ray physical fiber와 projective C-character signed aggregate의 exact quadratic identity.
- translate variance와 spectral variance가 master spectral Gram의 서로 다른 contraction이라는 재구성.

### ANA-Δ05 — Signed-Structure Preservation / 부호 구조 보존
최종 목표가 signed cancellation을 허용하면 가능한 가장 높은 층위까지 signed aggregation을 보존한다.
절댓값·양의 envelope는 필요성이 증명될 때만 도입한다.

### ANA-Δ06 — Freeze / Dormancy / Reopen State
실패한 공격법을 삭제하거나 “거짓”으로 판정하지 않고 다음 상태를 구분한다.

```text
ACTIVE
DORMANT_STRONG
FROZEN_UNDER_CURRENT_INPUTS
BLOCKED_AT_EXPLICIT_MISSING_IDENTITY
REOPEN_IF_<condition>
SUPERSEDED_AS_FRONTIER_NOT_AS_LEMMA
```

실전 근거:
- Navier–Stokes BP spectral branch를 intertwining identity 부재 지점에서 freeze.
- stochastic route는 새 Lyapunov/capture theorem 등이 생길 경우에만 reopen.

### ANA-Δ07 — Exact Reuse / Descriptor Cache Candidate
반복 계산에서 동일 complete descriptor·prefix·state expansion을 재사용할 수 있는지 분석한다.

조건:
- 재사용 전후 mapping이 exact임을 인증할 것.
- 계산량 감소와 새로운 수학적 정리를 구분할 것.
- cache/reuse가 omitted branch의 soundness를 손상하지 않을 것.

실전 근거:
- Collatz complete-descriptor cyclic-window 계산에서 exact count 보존과 반복 expansion 감소를 분리 기록.

### ANA-Δ08 — Gain-Type Separation
결과의 이득을 최소한 다음으로 분리한다.

```text
THEOREM_GAIN
STRUCTURAL_GAIN
COMPUTATIONAL_GAIN
AUDIT_GAIN
NO_GAIN
```

계산 가속을 새 정리로, 전선 압축을 증명으로, 오류 차단을 수학적 closure로 승격하지 않는다.

## 3. 후보 결합 순서

현재 잠정 순서:

```text
TARGET / MAXIMUM CLAIM LOCK
-> MINIMUM SUFFICIENT RESOLUTION
-> DEPENDENCY DAG
-> DUPLICATE / COMMON-LATENT-OBJECT CHECK
-> ESCALATION CHECK
-> SIGN / INFORMATION-LOSS CHECK
-> ACTIVE / DORMANT / FROZEN FRONTIER
-> REUSE / COMPUTATION OPPORTUNITY
-> GAIN-TYPE LABEL
```

이는 **실험 후보 파이프라인**이며 정본 Analysis 알고리즘이 아니다.

## 4. 평가 기준

채택 검토 시 최소한 다음을 확인한다.

1. 기존 Analysis 코어로 이미 충분한 규칙을 중복 명명하는가.
2. Riemann / Collatz / Navier–Stokes 외의 사례에도 재현되는가.
3. 잘못된 branch pruning을 유발하지 않는가.
4. 강한 충분조건을 약한 필수조건으로 잘못 바꾸지 않는가.
5. domain-specific proof standard를 DSD 구조 판정으로 대체하지 않는가.
6. 기존 Computation / Optimization / Comparison / Audit 방법의 고유 영역을 침범하지 않는가.
7. baseline 대비 실제 오류 감소·분기 감소·계산 감소가 측정되는가.

## 5. 근거 포인터 — 원 데이터 복제 금지

Riemann:
- `571f53d40de4eb9d47994b64fea3d9eef5722971` — minimal-bridge dependency audit
- `6ed94b50fbb4d23d6e6fca46cfadd962814ecef4` — physical/dual and variance unification audit
- `c5ddc742726cfce72d06fc931ffd7e04ce943fb0` — spectral Gram HS audit

Collatz / Math-verification:
- `03f4c5bc86bbea3a27dbdf509da79d15dd70492d` — complete-descriptor cyclic-window acceleration
- `476d3acac3ad0b1da5917d24506a8d4f70da54c2` — DSD-guided calculation-method transition
- `9bd54609129c1ad4683b30cc175ba1e540b0801c` — unified depth 1..41 DSD re-audit certificate

Navier–Stokes:
- `ac1758781a94166560cd0cff10c8b8ef93e7c23f` — stochastic-route freeze / two-gate frontier
- `f07d7807251b63b830705c5d89792e59805e7bdf` — DSD pruning rebase through ROOT-198
- `bda0d568412c0655880aeec1ef353e0469e7f99b` — final direct BP profile-PDE audit / branch freeze

## 6. 결정 장부

```text
CANDIDATE:
EVIDENCE_SET:
BASELINE:
FAILURE_MODE:
CROSS_DOMAIN_TRANSFER:
MEASURED_GAIN:
BOUNDARY_COLLISION:
DECISION:
MERGE_TARGET:
DELETE_AFTER_DISCUSSION:
NOTES:
```

현재 모든 ANA-Δ 항목의 DECISION은 **PENDING_DISCUSSION**이다.


## 7. 2026-09-27 1차 알고리즘 정제

세 난제 실전에서 얻은 후보를 일반 Analysis 절차로 옮기면서 다음 정제를 적용했다.

- “최소 해상도”를 단일 스칼라가 아니라 **claim-relevant multi-axis resolution profile**로 변경했다.
- 단순 dependency DAG 대신 **typed AND/OR dependency hypergraph**를 사용한다.
- 하나의 frontier rank를 강제하지 않고 **minimal active frontier families**를 보존한다.
- “강한 조건으로 상승”과 “정보를 잃는 축약”을 서로 다른 ledger로 분리한다.
- common latent object가 있어도 projection/contraction/coarsening이면 자동 병합하지 않는다.
- non-frontier route는 삭제하지 않고 supporting/exploratory/dormant/frozen 상태로 보존한다.
- exact reuse/cache의 실제 구현은 Analysis가 아니라 **DSD Computation**으로 이관하는 방향을 택했다.
- gain은 하나의 배타적 등급이 아니라 theorem/structural/computational/reproducibility/audit/negative-narrowing의 **multi-label set**으로 기록한다.

세부 실행안: [GENERAL_ANALYSIS_CONTROLLER_V0_2.md](GENERAL_ANALYSIS_CONTROLLER_V0_2.md)

### 잠정 후보 상태

```text
ANA-Δ01  PROMOTE_TO_AB_TEST
ANA-Δ02  PROMOTE_TO_AB_TEST
ANA-Δ03  PROMOTE_TO_AB_TEST
ANA-Δ04  PROMOTE_TO_AB_TEST
ANA-Δ05  ABSORB_INTO_INFORMATION_LOSS_CHECK
ANA-Δ06  KEEP_AS_SHARED_OPERATIONAL_STATE_LAYER
ANA-Δ07  REFER_TO_COMPUTATION
ANA-Δ08  KEEP_AS_SHARED_RECORDING_RULE
```

이 상태는 정본 채택 결정이 아니라 **다음 A/B 검증을 위한 임시 정제 상태**다.
