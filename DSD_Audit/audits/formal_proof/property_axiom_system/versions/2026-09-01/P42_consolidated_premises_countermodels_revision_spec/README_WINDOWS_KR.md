# PA-P42 — Windows 11 검증 (Kwon Dominicus)

GitHub `dominicus9708/DSD_Method_Family` 저장소의 기존 루트에서 진행합니다.
P27 EN/KR LaTeX, PDF, Zenodo는 편집하지 않습니다.

```powershell
$root = 'DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01'
python "$root\P42_consolidated_premises_countermodels_revision_spec\verify_p42_integrated_claims.py" `
  --out "$root\P42_consolidated_premises_countermodels_revision_spec\replay\P42_RESULT.json"
```

입력: 고정 P27 EN/KR TeX, P40 20항 JSON, P41 97간선 JSON, P42 전제·반모형 명세 JSON.
출력: P42/replay/P42_RESULT.json.
이 검증은 원본 해시·20/13 대장·§4.5/4.6의 두 적법 예제를 재현하며 일반 집합론 명제 전체를 기계 증명하지 않습니다.
A/B1/B2 선택 보류, FPA OPEN.
