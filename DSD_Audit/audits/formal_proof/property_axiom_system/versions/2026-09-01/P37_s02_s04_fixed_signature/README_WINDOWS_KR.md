# P37 속성공리계 FPA — Windows 11 재현

저장소: dominicus9708/DSD_Method_Family. **저장소의 루트**에서 PowerShell 실행.

```powershell
$base = 'DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\P37_s02_s04_fixed_signature'
New-Item -ItemType Directory -Force "$base\replay" | Out-Null
python "$base\verify_p37_fixed_signature.py" --out "$base\replay\P37_FIXED_SIGNATURE_EVIDENCE.json"

# 영문·국문 동결 소스 SHA256 확인
$f = 'DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\P27_independent_math_revision'
Get-FileHash "$f\DSD_Property_Axiom_System_EN_P27_REVISED.tex" -Algorithm SHA256
Get-FileHash "$f\DSD_Property_Axiom_System_KR_P27_REVISED.tex" -Algorithm SHA256
```

기대 EN SHA256: 51c194ec33f802a2061b68b3521fdb831f0f754a0386fa72f8e89a39efff7bdb
기대 KR SHA256: a643ea619f9594142bfc09b9f486c948cf0a85679a3b2a8a43bc731a1e108fbb

저장된 기대 파일 `P37_FIXED_SIGNATURE_EVIDENCE.json`과 replay 결과의 JSON 내용 일치를 확인한다. 별도 Python 패키지는 없다. 이 검사는 선택된 유한 모형과 380개 판정에 한정되며 일반 집합론적 증명은 `P37_S02_S04_GENERAL_THEOREM_SCOPE_AUDIT_KR.md`에 별도 기록한다.

**원고·PDF·Zenodo 미수정. A/B 의미론 미선택. 전체 FPA OPEN.**
