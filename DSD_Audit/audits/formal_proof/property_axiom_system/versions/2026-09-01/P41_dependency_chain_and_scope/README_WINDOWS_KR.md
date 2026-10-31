# PA-P41 Windows 11 재현 (Kwon Dominicus)

기존 DSD_Method_Family 저장소의 루트에서 실행합니다. P27 원고를 다른 경로에 복사하지 않습니다.

~~~powershell
$base = 'DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01'
python "$base\P41_dependency_chain_and_scope\verify_p41_dependency_dag.py" --out "$base\P41_dependency_chain_and_scope\replay\P41_VERIFY_RESULT.json"
~~~

입력: P27 EN/KR TeX, P39 JSON, P40 JSON, P41 graph JSON. 출력: replay/P41_VERIFY_RESULT.json.
검사 성공은 전체 ZFC 증명 완료가 아니라 지정한 의존 그래프의 재현성 확인입니다.
A/B 의미론 선택 보류, P27 원고/PDF/Zenodo 동결, FPA OPEN.
