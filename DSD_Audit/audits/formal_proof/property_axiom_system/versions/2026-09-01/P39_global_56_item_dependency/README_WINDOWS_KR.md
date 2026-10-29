# PA-P39 Windows 11 재현 — Kwon Dominicus

동결된 원고 경로·입력은 기존 `DSD_Method_Family` GitHub 저장소의 동일 프로젝트 루트를 사용한다. 별도 임의 경로에 소스를 복사하지 않는다.

PowerShell에서 해당 저장소 루트에서:

```powershell
$base = 'DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01'
python "$base\P39_global_56_item_dependency\verify_p39_56_item_ledger.py" `
  --out "$base\P39_global_56_item_dependency\replay\P39_VERIFY_RESULT.json"
```

입력은 `P27_independent_math_revision/DSD_Property_Axiom_System_{EN,KR}_P27_REVISED.tex`과 P39 기대 JSON이고, 출력은 P39 replay 아래 결과 JSON이다. 결과가 19/19가 아니면 비정상 종료한다. 검사 내용은 **해시·56개 항목 및 참조 구조·한 유한 증인**이며, 수학적 일반 증명이나 외부 독립 심사가 아니다. `--out` 생략 시 stdout만 사용한다.

A/B/B1/B2 의미론 최종 선택 보류; P27 원고·PDF·Zenodo 편집 금지; FPA OPEN.
