# PA-P46 — Windows 11 재현 (Kwon Dominicus)

기존 \`dominicus9708/DSD_Method_Family\` 저장소 루트에서 실행하고, 입력·출력·검증코드는 기존 속성공리계 버전 폴더의 위치를 유지합니다.

```powershell
$root = 'DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01'
python "$root\P46_choice_invariants_branching\verify_p46_branch_monotonicity.py" `
  --out "$root\P46_choice_invariants_branching\replay\P46_VERIFY_RESULT.json"
```

**입력:** P27 동결 EN/KR TeX, P42 20+13 대장, P44 준비성 대장, P45 의미론 비교 대장, P46 조건부 수학정리 및 기대조건 대장.

**출력:** P46/replay/P46_VERIFY_RESULT.json. \`--out\` 없으면 stdout JSON.

검사 내용: 36 raw 제시, 1,296 순서쌍의 활성/전체 raw 단계 분기 표, 타입 적법성, 원고 SHA, S01~04 보류 상태, \(I_k^{raw}\subseteq I_k^{act}\) 및 \(\beta_{raw}\le\beta_{act}\)를 **지정한 유한모형 안에서** 확인.

무한 집합 일반 증명이나 전체 자연어 번역 동치, 후속 DSD 이용가능성을 이 검사로 인증하지 않습니다.
A/B1/B2 미선택. P27 LaTeX/PDF/Zenodo 미수정. FULL FPA OPEN.
