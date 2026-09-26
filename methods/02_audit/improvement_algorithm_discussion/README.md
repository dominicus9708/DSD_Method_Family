# 개선 알고리즘 논의 — DSD 감사

Status: **TEMPORARY / NON-CANONICAL / DISCUSSION-ONLY**  
Branch: `tmp/analysis-audit-improvement-algorithm-discussion-20260926`  
Created: 2026-09-26 KST

## 0. 운영 원칙

이 폴더는 기존 `DSD_Audit/` 정본과 `methods/02_audit/` 경계를 수정하지 않고, Riemann·Collatz·Navier–Stokes 실전 감사에서 반복된 **추가 후보 알고리즘(delta)** 을 임시 검토한다.

- 정본: `DSD_Audit/methodology/GENERAL_AUDIT_FRAMEWORK.md`
- 정본 기록표준: `DSD_Audit/methodology/AUDIT_RECORDING_STANDARD.md`
- 기존 자동화 계획: `DSD_Audit/methodology/AUDIT_ALGORITHMIZATION_ROADMAP.md`
- 이 폴더는 위 세 문서를 **대체하거나 선행 개정하지 않는다**.
- 원 계산·대규모 로그·증명파일을 복제하지 않고 commit / Notion pointer만 둔다.
- 사용자와의 논의 및 frozen-baseline 비교 전에는 main/정본으로 병합하지 않는다.
- 최종 상태는 `ADOPT / ADOPT_WITH_LIMITS / KEEP_EXPERIMENTAL / REJECT / DELETE_AFTER_DISCUSSION` 중 하나로 결정한다.

## 1. 보존되는 원본 Audit 코어

기존 Audit의 안정 코어는 그대로 유지한다.

```text
SOURCE LOCK
-> INTERFACE LOCK
-> TYPE/STATUS VALIDATION
-> SELECTION/EXCLUSION
-> BRIDGE
-> TRANSITION/LINEAGE
-> ALTERNATIVE/WITNESS
-> AGGREGATION/RECONSTRUCTION
-> CONTRADICTION
-> MAXIMUM-SUPPORTED-CLAIM
-> DOMAIN VERDICT + DSD STRUCTURAL VERDICT
```

아래 후보는 이 파이프라인에 “덧대어질 가치가 있는가”만 검토한다.

## 2. 실전에서 추출된 후보 delta

### AUD-Δ01 — Claim-to-Resolution Sufficiency Audit
감사 대상이 실제 claim보다 강한 pointwise/uniform/norm/moment 조건을 암묵적으로 필수화했는지 검사한다.

출력:
```text
REQUIRED
SUFFICIENT_BUT_STRONGER
OPTIONAL_REFINEMENT
UNRELATED
```

Riemann 실전에서 global theorem hinge와 pointwise/uniform/sharp-variance route를 분리한 절차를 일반화 후보로 둔다.

### AUD-Δ02 — Dependency-Rank / Gate Audit
OPEN 항목의 개수가 실제 독립 논리 장벽 수와 같은지 검사한다.

검사:
- parent/child implication
- equivalent reformulation
- shared sufficient parent
- attack method vs theorem gate
- duplicate descendant
- reopen condition

Navier–Stokes에서 다수 route를 두 master gate로 압축한 방식이 대표 사례다.

### AUD-Δ03 — Escalation Audit
증명·계산 과정에서 다음 강도 상승이 발생하면 근거를 요구한다.

```text
average -> supremum
global -> pointwise
signed -> absolute
first moment -> second moment
weighted object -> uniform envelope
component-resolved -> aggregate-only
finite exact certificate -> general theorem
```

판정은 “강한 식이 틀림”이 아니라, 부모 claim에 비해 **필요 이상인지**를 따로 기록한다.

### AUD-Δ04 — Representation-Duplication / Common-Object Audit
서로 다른 분기가 같은 object의 dual representation, coordinate transform, contraction, 또는 postprocessing인지 추적한다.

동일성이 확인되면 두 route를 독립 evidence/gate로 이중계수하지 않는다.
동일하지 않으면 어떤 강도 차이(moment/norm/support)를 가지는지 기록한다.

### AUD-Δ05 — Freeze and Reopen Audit
branch 종료를 다음처럼 구조화한다.

```text
FROZEN_REASON:
FAILED_IMPLICATION:
PRESERVED_LEMMAS:
CURRENTLY_MISSING_INPUT:
REOPEN_CONDITION:
FRONTIER_EFFECT:
CLAIM_EFFECT:
```

“현재 입력에서 막힘”과 “수학적으로 불가능함”을 분리한다.

### AUD-Δ06 — Executable Invariant Certificate
가능한 경우 사람이 읽는 감사와 별도로 작은 deterministic certificate가 다음 불변량을 재검사하게 한다.

후보:
- lineage identity
- accounting conservation
- exact mapping preservation
- support/cardinality consistency
- canonical anchor totals
- no-double-application / no-double-lift
- branch state transition legality

Collatz depth 1..41 re-audit처럼 **범위 내 exact consistency**와 난제 전체 증명을 명시적으로 분리한다.

### AUD-Δ07 — Frontier Admissibility Audit
새 계산/분기가 현재 frontier를 실제로 단축하는지 검사한다.

```text
DIRECTLY_CLOSES_GATE
PROVIDES_REQUIRED_BRIDGE
REUSABLE_SUPPORTING_LEMMA
OPTIONAL_STRONGER_ROUTE
NON_FRONTIER_EXPLORATION
DUPLICATE_ROUTE
```

Navier–Stokes의 “두 gate 중 하나를 단축하지 않는 ROOT 작업은 canonical frontier가 아니다”라는 실전 규율을 일반화할 가치가 있는지 시험한다.

### AUD-Δ08 — Computation/Theorem Boundary Audit
러너 결과를 다음처럼 분리한다.

```text
EXACT_FINITE_CERTIFICATE
COMPUTATIONAL_ACCELERATION
EMPIRICAL_PATTERN
STRUCTURAL_NARROWING
THEOREM_LEVEL_CLOSURE
GLOBAL_PROOF
```

실행 성공, 계산 가속, 수치 패턴, 구조 축소를 자동으로 theorem closure로 승격하지 않는다.

### AUD-Δ09 — Negative Result Retention with Positive Reuse
실패한 route에서도 보존 가능한 exact identity, counterexample, bound, no-go 범위, future reopen condition을 따로 추출한다.

이 항목은 기존 SC-08의 failure preservation을 **난제 proof-frontier용 세부 실행 규칙**으로 볼 수 있으므로, 독립 규칙이 아니라 specialization으로 귀속될 가능성이 높다.

## 3. 기존 Audit와 중복 가능성이 높은 후보

초기 판단:
- AUD-Δ05는 기존 alternatives/revision/limits와 중첩 가능.
- AUD-Δ06은 기존 reproducibility + mathematics domain adapter의 세부화 가능.
- AUD-Δ08은 기존 “finite computation must not be upgraded into proof”의 executable specialization 가능.
- AUD-Δ09는 SC-08의 specialization일 가능성이 높음.

따라서 이 후보들을 곧바로 새 Audit core rule로 추가해서는 안 된다.

반대로 아래는 기존 문서에 명시도가 상대적으로 낮아 **실전 기반 보강 후보**로 우선 비교할 가치가 있다.
- claim-to-resolution sufficiency
- dependency-rank / gate compression
- escalation audit
- representation-duplication/common-object audit
- frontier admissibility

## 4. 실험용 확장 파이프라인

```text
[기존 Audit 파이프라인]
-> CLAIM / THEOREM HINGE LOCK
-> DEPENDENCY-RANK MAP
-> MINIMUM SUFFICIENT RESOLUTION CHECK
-> REPRESENTATION-DUPLICATION CHECK
-> NORM/MOMENT/UNIFORMITY ESCALATION CHECK
-> FRONTIER ADMISSIBILITY
-> FREEZE / REOPEN LEDGER
-> EXECUTABLE INVARIANT CHECK (가능한 경우)
-> 기존 MAXIMUM-SUPPORTED-CLAIM / DOMAIN + DSD VERDICT
```

정본 채택 전까지는 **실험용**이다.

## 5. 검증 설계

정본 개선 여부는 frozen original Audit baseline과 동일 fixture에서 비교해야 한다.

최소 평가축:
```text
MISSED_OVERCLAIM
FALSE_PRUNING
DUPLICATE_GATE_COUNT
UNNECESSARY_STRONG_TARGET_COUNT
UNJUSTIFIED_ESCALATION_COUNT
FINITE_TO_GENERAL_OVERCLAIM
REPRODUCIBILITY_MISMATCH
FRONTIER_BRANCH_COUNT
REVIEW_TIME_OR_RUN_COST
CLAIM_RELEVANT_CORRECTIONS
```

필요할 경우 DSD_Method_Family runner는 이 A/B 비교에만 사용하고, 후보가 유리해 보인다는 이유로 정본을 자동 개정하지 않는다.

## 6. 근거 포인터 — 원 데이터 복제 금지

Riemann:
- `571f53d40de4eb9d47994b64fea3d9eef5722971`
- `6ed94b50fbb4d23d6e6fca46cfadd962814ecef4`
- `c5ddc742726cfce72d06fc931ffd7e04ce943fb0`

Collatz / Math-verification:
- `173b62cd3bf37886989e8399fef53a6346c7b30b`
- `56b607728e0e6d0367ea49dfe428103811c75f00`
- `9bd54609129c1ad4683b30cc175ba1e540b0801c`

Navier–Stokes:
- `ac1758781a94166560cd0cff10c8b8ef93e7c23f`
- `f07d7807251b63b830705c5d89792e59805e7bdf`
- `bda0d568412c0655880aeec1ef353e0469e7f99b`

## 7. 결정 장부

```text
CANDIDATE:
EXISTING_RULE_OVERLAP:
EVIDENCE_SET:
FROZEN_BASELINE:
FALSE_POSITIVE_RISK:
FALSE_NEGATIVE_RISK:
MEASURED_GAIN:
CROSS_DOMAIN_TRANSFER:
DECISION:
MERGE_TARGET:
DELETE_AFTER_DISCUSSION:
NOTES:
```

현재 모든 AUD-Δ 항목의 DECISION은 **PENDING_DISCUSSION**이다.
