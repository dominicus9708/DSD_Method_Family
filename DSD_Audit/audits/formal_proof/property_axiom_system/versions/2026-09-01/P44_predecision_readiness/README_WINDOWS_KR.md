# PA-P44 Windows 11 재현 명령 — Kwon Dominicus

기존 `dominicus9708/DSD_Method_Family` 저장소의 **동일 루트**에서 실행합니다. 입력 경로는 기존 프로젝트 FPA 경로를 유지합니다.

```powershell
$base = 'DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01'
python "$base\P44_predecision_readiness\verify_p44_predecision_readiness.py" `
  --out "$base\P44_predecision_readiness\replay\P44_VERIFY_RESULT.json"
```

**입력:** 동결 P27 EN/KR LaTeX, P41 97개 DAG, P42 20+13 대장, P43 수식대장, P44 증거 대장, P29–P43 저장된 15개 보고서.

**출력:** `P44_predecision_readiness/replay/P44_VERIFY_RESULT.json`. `--out` 생략 시 stdout.

**범위:** 원고 해시와 근거 파일 존재, 78개 표시/222개 인라인 수식, 15개 감사보고서, S01–S04/3개 의미론의 보류 상태 검사. 자연어 전체의 번역·무한 집합의 일반 증명 또는 FPA CLOSED 자동 인증이 아닙니다.

**상태:** A/B1/B2 결정 보류. EN/KR LaTeX·PDF·Zenodo 수정 금지. FPA OPEN.
