# PA-P40 재현 (Windows 11)

논문 LaTeX/PDF/Zenodo 수정 없이, 기존 DSD_Method_Family 저장소 루트에서 실행:

```powershell
$root = 'DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01'
python "$root\P40_20_statement_proof_audit\verify_p40_20_proof_claims.py" `
  --out "$root\P40_20_statement_proof_audit\replay\P40_VERIFY_RESULT.json"
```

입력: P27 동결 EN/KR TeX, P39 JSON, P40 20항 장부.
출력: P40/replay/P40_VERIFY_RESULT.json (옵션 생략 시 stdout만 출력).
검사: 원본 해시, 번호·타입·증명 환경, 4개 잔여 의무, 한 원소 반모형/정당한 미정의 상태, 두 속성 요약 충돌.
A/B 선택은 아직 보류이며 기계 검사 성공은 무한 집합 전반에 대한 형식증명 완료가 아니다.
