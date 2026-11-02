# PA-P43 — Windows 11 원문 대비 감사 재현

저자 Kwon Dominicus. 입력·출력 경로는 기존 `DSD_Method_Family` 저장소의 동일 FPA 버전을 사용합니다.

```powershell
$root = 'DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01'
python "$root\P43_bilingual_math_parity_closure_gates\verify_p43_en_kr_parity.py" `
  --out "$root\P43_bilingual_math_parity_closure_gates\replay\P43_CHECK_RESULT.json"
```

입력: 동결 P27 EN/KR LaTeX, P42 20+13 JSON, P43 정합성 JSON.
출력: `replay/P43_CHECK_RESULT.json`. 인자 미지정 시 표준출력 JSON.

표시 수식의 한국어/영어 `\\text{...}` 설명과 문장부호를 무시하는 비교는 **형식 골격 검사**이며 자연어 의미 동치의 기계 증명이 아닙니다.
기존 P27 LaTeX·PDF·Zenodo 변경 금지. A/B1/B2 최종 선택 보류, 전체 FPA OPEN.
