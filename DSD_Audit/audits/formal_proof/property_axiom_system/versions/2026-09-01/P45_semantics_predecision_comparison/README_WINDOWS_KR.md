# PA-P45 — Windows 11 재현 (Kwon Dominicus)

기존 \`dominicus9708/DSD_Method_Family\` 저장소의 루트에서 실행합니다. 입력·Python·출력 폴더는 기존 속성공리계 FPA 버전 구조를 따릅니다.

```powershell
$base = 'DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01'
python "$base\P45_semantics_predecision_comparison\verify_p45_semantic_factorization.py" `
  --out "$base\P45_semantics_predecision_comparison\replay\P45_VERIFY_RESULT.json"
```

**입력:** P27 EN/KR 동결 TeX, P44 증거대장, P45 의미론 결정 기준 JSON, P45 유한 검산 예상 JSON.

**출력:** P45/replay/P45_VERIFY_RESULT.json. \`--out\` 생략 시 stdout.

36개 적법 raw 제시(활성 구조 4종×잉여 Ap 세 상태×잉여 Xi 세 상태)와 1,296개 순서쌍의 활성 동형·raw 동형/첫 분기를 비교합니다. 활성 관찰의 불가구별성과 raw 진단의 구별 가능성을 계산합니다. **이 유한 재현은 R1–R7 집합론적 일반 증명의 대체물이 아닙니다.**

A/B1/B2 채택·흡수·폐기 보류. 영·국문 P27 LaTeX/PDF·Zenodo 변경 금지. FPA OPEN.
