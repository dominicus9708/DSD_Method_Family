# PA-P14R-20261024 — independent non-destructive replay of all existing Property Python

**Execution date:** 2026-10-24 KST.
**Author:** Kwon Dominicus.
**Exact manuscript source:** `DSD_Property_Axiom_System_EN(4).pdf`, original 2026.09.01, 23 pages, SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.

**Scope:** the user's request to rerun and audit the **existing** historical Python, not to begin manuscript revision. Original mathematical claims are not inferred to be globally valid from these bounded scripts.

## 1. Original experiment repository (unchanged)

Companion repo: [Property_Axiom_System](https://github.com/dominicus9708/Property_Axiom_System).

Frozen Git blobs:
- `src/property_axiom_reproduction.py` `04844beca113c24267660fcbb09bc8f833403a28`;
- `src/verify_property_axiom_results.py` `18f48c15e142a8da2b8c283404ab1fd0d0c262d2`;
- `tests/test_property_axiom_reproduction.py` `8ba18051a84c8ea913d5773139674e3aba0749a3`.

**Actual fresh GitHub Actions:**
- Original workflow [#39977127410](https://github.com/dominicus9708/Property_Axiom_System/actions/runs/39977127410) **SUCCESS**, original generator + verifier and **7/7 unit tests**, both Python 3.10/3.12.
- Extra original-code audit [#39977127221](https://github.com/dominicus9708/Property_Axiom_System/actions/runs/39977127221) **SUCCESS**, original code SHA locked, plus **9/9 expected negative tests**, both Python versions.
- Important **initial strict-byte replay** [#39977709753](https://github.com/dominicus9708/Property_Axiom_System/actions/runs/39977709753) deliberately **FAILED** both versions because two saved fixture files are not byte-identical.
- Correctly scoped **semantic replay** [#39977845896](https://github.com/dominicus9708/Property_Axiom_System/actions/runs/39977845896) **SUCCESS** on both versions:
  - `property_witness_summary.json`: same parsed JSON contents, **not** same bytes (current regenerated 2251 vs existing committed 1835 bytes; compact old nested JSON vs expanded current `indent=2`).
  - `proof_obligation_audit.json`: byte-for-byte identical (same parsed data).
  - `witness_catalog.csv`: same 10 parsed CSV rows, **not** same bytes (regenerated 1084 vs committed 1074; CRLF vs LF difference).
  - All **7/7** original unit tests and **9/9** negative-control detections again PASS.

**Code audit findings** in [companion original repo report](https://github.com/dominicus9708/Property_Axiom_System/blob/main/audits/2026-09-01/PA_REPLAY_AUDIT_20261024.md):
1. `PropertyModel.is_core_model()` only combines two primitive-axiom check methods and does not enforce full input typing. Explicit `Ap` and `Sat_d` sets containing out-of-product `('ghost',)` were accepted as core models when assignments were empty.
2. `verify_property_axiom_results.py` can still return success when a **temporary** status witness is corrupted, and when an individual audit check is false but the stored `all_checks_pass=True` is left unchanged. This is verification-coverage incompleteness, **not** a claim that the known original unmodified witnesses failed.
3. `status()` returns priority-ordered single labels on PI/PII-violating **typed premodels**, hiding raw simultaneous `defined` + `inapplicable` or `defined` + `prerequisite-unsatisfied`. This reinforces the **P14** source proof-scope issue `Th4.3 relative to C1`; admitted full cores still require PI/PII and thus avoid this overlap.
4. Declared but unavailable property kind can carry surplus Python assignment coordinates without an error; whether to forbid vs ignore them as extraneous metadata needs explicit core identity modeling, not an asserted manuscript inconsistency.

**Severity classification:**
- `ORIGINAL_FINITE_WITNESS_REPRODUCTION: PASS`.
- `ORIGINAL_TYPED_VALIDATOR_COMPLETENESS: FAIL_FOR_ARBITRARY_INPUT`.
- `ORIGINAL_RESULT_VERIFIER_COMPLETENESS: FAIL_TO_DETECT_SELECTED_TAMPER`.
- `HISTORICAL_BITWISE_FIXTURE_PARITY: FORMAT_ONLY_MISMATCH`.
- `FULL_MANUSCRIPT_FPA: OPEN`.

## 2. P9A–P12 independent scripts reexecuted unchanged

DSD Method Family version folder (no code changes):
- `scripts/verify_p9a_finite_morphisms.py` Git blob `c04eb5ae30a8088ec7baf23aa1926a6d03a0b34a`;
- `scripts/verify_p10_cross_sort.py` `64d1b6027ab97cdfb4be264f2ac2f9e27c6b1500`;
- `scripts/verify_p11_empty_dependency_edges.py` `4c988d4dfc3b78aa3b2c2249e07ea8669f85d102`;
- `scripts/verify_p12_representation_aggregate.py` `146e3e6fe88c3b397b9f26f563ac368b6d9c8178`.

New replay-only workflow [property_legacy_audits_replay_20261024.yml](https://github.com/dominicus9708/DSD_Method_Family/blob/main/.github/workflows/property_legacy_audits_replay_20261024.yml) tests source Git blobs, executes **all four original Python scripts** under Python **3.10 and 3.12**, and checks each freshly produced JSON against its archived version:
- P9A **53 legal cores / 2809 ordered pairs** and 53 strict-comparison pairs, source witness and map closure revalidated.
- P10 **108 legal template cores / 11664 ordered pairs**, 30318 carrier map candidates, 9253 forward maps, 3054 embeddings, **168 strict individual maps**. As the source returns strict *map* multiplicities, it is incorrect to infer 168 strict *model pairs*: the branch counts total 11556 nonisomorphic ordered pairs; **108 isomorphic ordered pairs** are left, with **168 actual strict maps** among them.
- P11 **10/10 original edge cases** passed.
- P12 **14/14 original representation/aggregate negative and positive edge cases** passed.
- All 4 committed JSON documents were **exactly equal to the newly executed contents** on both Python versions.

**Audit-of-audit failure preserved:** initial new workflow [#39977201550](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/39977201550) **FAILED** in the *new independent comparison formula*, which incorrectly added the number of strict **maps** (168) to the number of branched **model pairs** (11556) and compared with 11664. No original P9A–P12 script or JSON failed and all four already matched their archives. The wrong cross-check was corrected without changing original scripts. [Re-execution #39977321537](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/39977321537) **SUCCESS**, both Python versions, prints `P9A-P12 independent cross-suite constraints PASS`.

This is a **real audit methodology finding**: never conflate a morphism count with the number of ordered objects admitting a morphism. Preserve the failed run as evidence of an audit-control bug and corrected methodology, not as an original numerical failure.

## 3. Mathematical connection and remaining obligations

- **Original printed manuscript §6 still has two known condition issues**: F3–F5 source declared but profile-unavailable guard; strict isomorphism vs componentwise-bijective embedding shorthand missing S2/S3. These are manuscript problems and were **not** silently fixed by replay success.
- **Th4.3 relative-to-C1** remains open because the independence witnesses are typed **premodels** where raw status predicates overlap. New Python negative tests make that overlap explicit; the full-core C1 uniqueness theorem remains separately supported in its declared scope.
- All evidence is **finite deterministic code reproduction and scoped negative test results**, not independent proof assistant certification, formal verification over all arbitrary sets, or external refereeing.
- No original author manuscript PDF/LaTeX, Zenodo, original experiment algorithms or old fixture files modified.

## 4. Windows 11 commands for the existing established folders

**In repository root `Property_Axiom_System`:**
```powershell
python src\property_axiom_reproduction.py --output-dir results
python src\verify_property_axiom_results.py --results-dir results
python -m unittest discover -s tests -v
python audits\2026-09-01\PA-REPLAY-20261024_NEGATIVE_CONTROLS.py
```
**In repository root `DSD_Method_Family`**, use the existing input-free scripts and version-scoped output files (placeholders below are the established filenames):
```powershell
python DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\scripts\verify_p9a_finite_morphisms.py DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\results\p9a_finite_morphisms.json
python DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\scripts\verify_p10_cross_sort.py DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\results\p10_cross_sort_ci.json
python DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\scripts\verify_p11_empty_dependency_edges.py DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\results\p11_empty_dependency_edges.json
python DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\scripts\verify_p12_representation_aggregate.py DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\results\p12_representation_aggregate.json
```
**Caution:** these commands overwrite local `results/` files. Run from a clean checkout or separate working tree to preserve historical formatting; the external CI instead regenerates into disposable runner temporary folders and compares.

```text
AUDIT_CASE: PA-P14R-20261024-REPLAY
ORIGINAL_7_7: PASS_BOTH_PYTHON
ORIGINAL_NEGATIVE_9_9: PASS_BOTH_PYTHON
ORIGINAL_FIXTURE_SEMANTIC_3_3: PASS_BOTH_PYTHON
ORIGINAL_FIXTURE_EXACT_BYTES_1_3: FORMAT_ONLY_MISMATCH
P9A_P10_P11_P12_FRESH_JSON_4_4: PASS_BOTH_PYTHON
NEW_CODE_COVERAGE_FINDINGS: TYPED_INPUT_VALIDATION_MISSING; VERIFIER_TAMPER_MISSED; STATUS_ON_COUNTERPREMODELS
NEW_AUDIT_ASSERTION_ERROR: CORRECTED_AND_REPLAYED
ORIGINAL_SOURCE_OR_DATA_REWRITTEN: no
WHOLE_GENERAL_PROPERTY_FPA: OPEN
NEXT: PA-P15-20260901-C1-COUNTERMODEL-SEMANTICS-001 (separate mathematical gate)
```
