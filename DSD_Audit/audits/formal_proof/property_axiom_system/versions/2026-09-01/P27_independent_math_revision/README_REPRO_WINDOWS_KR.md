# P27 Windows 11 reproducibility

Author: Kwon Dominicus. Repository root: `dominicus9708/DSD_Method_Family`.

Expected file locations preserve established relative paths:
- Input P26 EN/KR edited manuscript: `DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\P26_uploaded_source_revisions\DSD_Property_Axiom_System_{EN,KR}_P26_REVISED.tex`.
- Python builders and archived P27 results: `DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\P27_independent_math_revision\`.
- Output: `DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\P27_independent_math_revision\replay\`.

Run in PowerShell at repository root:

```powershell
$root = 'DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01'
python "$root\P27_independent_math_revision\build_p27_bilingual.py" `
  --source-dir "$root\P26_uploaded_source_revisions" `
  --out "$root\P27_independent_math_revision\replay"

python "$root\P27_independent_math_revision\verify_p27_independent_math.py" `
  "$root\P27_independent_math_revision\replay\P27_INDEPENDENT_FINITE_CHECKS.json"

Push-Location "$root\P27_independent_math_revision\replay"
latexmk -xelatex -interaction=nonstopmode -halt-on-error DSD_Property_Axiom_System_EN_P27_REVISED.tex
latexmk -xelatex -interaction=nonstopmode -halt-on-error DSD_Property_Axiom_System_KR_P27_REVISED.tex
Pop-Location
```

TeX Live/MiKTeX with XeLaTeX and Korean fonts is required to produce the PDFs; Python alone performs the section-preserving source revision and finite regression. Verify the replay source files against the committed P27 candidates and JSON against the archived P27 result. This does not provide a general ZFC formalization.

GitHub Actions: [P27 independent mathematics and bilingual build](https://github.com/dominicus9708/DSD_Method_Family/actions/workflows/property_fpa_p27.yml).
