# PA-P47 — Windows 11 재현 명령 (Kwon Dominicus)

기존 dominicus9708/DSD_Method_Family GitHub 저장소의 루트에서 실행합니다. CMD가 기본입니다.

```cmd
python "DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\P47_predecision_exit_and_negative_controls\verify_p47_predecision_exit.py" --out "DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\P47_predecision_exit_and_negative_controls\replay\P47_RESULT.json"
```

입력: P27 EN/KR 동결 TeX, P29–P46 각 감사보고서 18개, P39–P46의 증거 JSON, P47 판정 JSON.
출력: P47_predecision_exit_and_negative_controls/replay/P47_RESULT.json. --out 생략 시 stdout JSON.

검사는 원고 해시·18개 보고서 실재·56/20/13/97 연결 및 가상 typed-B 정의 아래의 15개 정상/음성 입력 구분을 확인합니다. CI 통과는 무한모형 일반 증명이나 번역 의미 동치 인증이 아닙니다.

A/B1/B2 최종 의미론을 선택·흡수·폐기하지 않습니다. P27 LaTeX/PDF/Zenodo는 미수정, 전체 FPA OPEN.
