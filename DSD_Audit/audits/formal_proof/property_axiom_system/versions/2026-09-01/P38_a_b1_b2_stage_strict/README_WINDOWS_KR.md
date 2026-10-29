# P38 Windows 11 PowerShell 재현
기존 저장소 dominicus9708/DSD_Method_Family의 루트에서 실행:

```powershell
$base = 'DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\P38_a_b1_b2_stage_strict'
New-Item -ItemType Directory -Force "$base\replay" | Out-Null
py -3.10 "$base\verify_p38_three_semantics.py" --out "$base\replay\P38_EXPECTED_EVIDENCE.json"
if ((Get-Content "$base\P38_EXPECTED_EVIDENCE.json" -Raw) -cne (Get-Content "$base\replay\P38_EXPECTED_EVIDENCE.json" -Raw)) { throw 'P38 result mismatch' }
Get-FileHash "$base\replay\P38_EXPECTED_EVIDENCE.json" -Algorithm SHA256
```

Python 3.10이 없으면 `python`으로 실행할 수 있다. 이 프로그램은 제한된 유한 예시 검사이며 일반 집합론 증명의 자동 형식화가 아니다.
