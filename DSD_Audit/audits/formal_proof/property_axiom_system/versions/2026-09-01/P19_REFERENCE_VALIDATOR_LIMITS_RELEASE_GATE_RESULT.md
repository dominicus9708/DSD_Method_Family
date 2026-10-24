# PA-P19-20260901-REFERENCE-VALIDATOR-LIMITS-AND-RELEASE-GATE-001 — actual source-locked audit

**Executed:** 2026-10-24 KST. **Original author:** Kwon Dominicus.
**Exact source:** `DSD_Property_Axiom_System_EN(4).pdf`, 23 pp, printed 2026.09.01, 157854 bytes, SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.
**Precommit:** [P19 prospectively frozen](P19_REFERENCE_VALIDATOR_LIMITS_RELEASE_GATE_PRECOMMIT.md) before running the new negative checks.
**Direct manuscript review:** pages 6–11 checked from the uploaded original PDF: Definition 2.1 finite nonempty typed profile, Definition 2.3 unavailable vs supplied-empty, Definition 2.5 well-typed premodel, Definition 2.6 primitive core, Definition 3.3 statuses, C1, Theorem 3.7 inverse laws, original Countermodels 4.1 and 4.2.

## 1. Existing evidence and new audit question

- [P17](P17_INDEPENDENT_TYPED_REFERENCE_VALIDATOR_RESULT.md): independent reference validator passed **30** positive/expected-negative checks and dynamically classified **13** live original models (2 premodels, 11 admitted cores).
- [P18](P18_DIFFERENTIAL_VALIDATOR_METAMORPHIC_RESULT.md): **47** metamorphic controls passed.
- These data **do not** establish that the P17 **validator itself** handles every invalid Python container robustly, represents every legitimate ZFC set element, or implements original C1's exact `CompProp/RedProp` inverse property.
- Therefore P19 was preregistered to challenge the independent checker rather than simply reuse its green status.

## 2. P19 finite independent tests and concrete negative findings

Added [P19 independent negative-control Python](scripts/verify_p19_reference_limits.py) **without modifying P17** or the historical `Property_Axiom_System/src/`. The script imports the unchanged P17 source by ordinary same-directory import and reports **20 independently named expected positive/negative observations**.

| Observation | Actual result | Correct scope |
| --- | --- | --- |
| P17 accepts a correctly typed baseline core | PASS | Positive control |
| Unhashable member of a Python carrier tuple | **uncaught `TypeError`**, not an `invalid_presentation` return | **Reference implementation robustness gap**, not ZFC source contradiction |
| `declared=None` | **uncaught `TypeError`** | Robustness gap |
| `ap=None`, `sat=None`, `xi=None` | Three distinct **uncaught `TypeError`** results | Robustness gap |
| Collision between inherited and auxiliary sort label universes | Correctly returns `invalid_presentation: sort_overlap` | Positive error-detection control |
| Inherited carrier encoded as tuple rather than set | Correctly rejects `inherited_not_set` | Canonical coding convention |
| Malformed three-element assignment graph row | Correctly rejects `invalid_assignment_graph` | Positive negative-input detection |
| Two admitted cores with different **nonzero** values `1` and `2` | Their exact primitives differ but P17 `completion()` outputs are **identical** | **Concrete noninjective derived-summary witness**, not a counterexample to original mathematical C1 |
| P17 `completion()` has no exact assignment or full defined-record content | Confirmed; returns only kind status, domain count, prerequisite-satisfied count, and status-by-repr dictionary | **Not the source's full `CompProp` implementation** |
| Two distinct hashable inherited-carrier elements with **identical `repr`** | P17 admits a mathematically typed 2-element model, but two different input-status entries collapse to **one** dictionary key | **Concrete loss from serialization key choice** |
| Finite ordered 5-coordinate mixed inherited/auxiliary input product | Correctly validates 32 typed inputs and produces 32 status entries for distinct string representations | Positive larger-arity bound |
| Undeclared surplus applicability coordinate | `ignore` admits; `reject` rejects; the modes are distinct | Preserve *both* policy options, source only says extra coordinates not required |
| Primitive input preserved by a successful P17 summary `completion` call | PASS | Nonmutation, not full reduction-inverse proof |

**Crucial mathematical separation:**

The original **Theorem 3.7**, `RedProp(CompProp(P))=P`, explicitly operates on the **full mathematical completion**, which retains exact defined property records `(varpi,x,z)` and the complete primitive coordinate data. The Python P17 `completion()` is deliberately a **summary**, and these P19 witnesses show why that summary is not injective and cannot on its own certify/reconstruct the source's full core. **No counterexample to the mathematical Theorem 3.7 was obtained.**

The two objects used for `repr` collision are deliberately distinct identity-hashable Python instances whose printable representations are the same. Because `repr(x)` is not a mathematical element identifier, it is not injective in general. The bug is in *record serialization*, not in typed ZFC set construction or PI/PII.

The five malformed-container cases illustrate that the current reference `validate()` has **partial defensive type checking**, not a promise to always return a structured failure on arbitrary Python garbage. This was not covered by P17/P18.

## 3. Real GitHub execution and independent archive check

- **Initial actual [GitHub Actions #40098897034](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40098897034):** Python **3.10 and 3.12 both completed success**, each reported `P19 EXPECTED LIMITATION CHECKS PASS 20` and `P19 INDEPENDENT EVIDENCE CHECK PASS`. The exact P17 source Git blob was locked unchanged: `d5e796022133bf066b6d485950044f93b5d656ca`.
- The new generated JSON objects were extracted from both job logs, JSON parsed and confirmed **identical across Python versions**, then committed unchanged to [P19 observed result JSON](results/p19_reference_limits.json).
- **Subsequent actual [GitHub Actions #40098977466](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40098977466):** Python 3.10 and 3.12 both **completed/success**; each reran P19 against unchanged P17 and logged `P19 ARCHIVED JSON MATCH`. The archive is thereby reproducible on both versions.
- All **20/20** are *correctly reproduced expected observations*, including **real negative failures in the P17 reference code**; “20 PASS” does **not** mean P17 accepts/validates 20 malformed data structures correctly.

## 4. Current release / proof closure matrix

| Gate | Evidentiary status | Next obligation |
| --- | --- | --- |
| Original 2026-09-01 PDF source custody | LOCKED SHA256 | Preserve printed statements and version control |
| Original PI/PII typed-background independence | SOURCE-SUPPORTED | C1-relative published scope separate |
| General mathematical C1 completion inverse, Th3.7 | SUPPORTED ON ADMITTED FULL CORES; **not tested by summary-only P17** | Build genuinely primitive-preserving **full** reference `CompProp/RedProp` and independent inverse controls, or retain explicit nonimplementation scope |
| P17 30 reference tests / original 13 models | FINITE PASS | Validates tested input/codomains only |
| P18 47 metamorphic tests | FINITE PASS | Does not establish arbitrary-object/input serializations |
| P19 20 adversarial source-vs-code observations | FINITE PASS with **real code limitation witnesses** | Add a **separate** defensive typed-input wrapper or new independent full-core representation, do not alter P17's historical evidence |
| Input malformed-type exceptions | ROBUSTNESS GAP CONFIRMED | Normalize/reject malformed containers with structured validation errors in future implementation, while preserving old P17 for audit history |
| Noninjective `completion()` summary | SOURCE-IMPLEMENTATION SCOPE GAP CONFIRMED | Do not advertise summary output as full `CompProp` or verify Th3.7 with it |
| Noninjective `repr(x)` status dictionary keys | SERIALIZATION LOSS CONFIRMED | Use actual typed record indices with bijective serialization or preserve underlying objects in a full mathematical completion |
| Historical generator/validator `Property_Axiom_System` | Old 7/7, P14R/P16 negative cases recorded | Change only in separate code-patch proposal after preserving source semantics |
| Original §6 forward maps, Def6.1 | **PRINTED SOURCE CONDITION MISSING: OPEN** | Clarify source-declared & available profile guard |
| Original Th6.8 “exactly bijective embedding” | **PRINTED SOURCE CONDITION MISSING: OPEN** | Require S2/S3 and full strict S1–S4 scope |
| Original Th4.3 independence “relative to C1” | **PRINTED PROOF SCOPE OPEN** | Choose and prove explicit typed-premodel conservative defining extension or narrow relative claim |
| Full ZFC proof-assistant certification, external review | NOT ESTABLISHED | Independent separate workstream |
| EN/KR author TeX parity / manuscript revisions / Zenodo | NOT EXECUTED | Separate author authorized manuscript gate |

## 5. Current result and non-edit successor

```text
CASE: PA-P19-20260901-REFERENCE-VALIDATOR-LIMITS-AND-RELEASE-GATE-001
SOURCE_LOCKED_EN_20260901_PDF_SHA256: 03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c
P19_ADVERSARIAL_OBSERVATIONS: 20/20 REPRODUCED
PYTHON_3_10: EXECUTED / ARCHIVED_JSON_EQUAL
PYTHON_3_12: EXECUTED / ARCHIVED_JSON_EQUAL
REFERENCE_UNCAUGHT_PYTHON_TYPE_ERRORS: FIVE DISTINCT INPUT_CASES
P17_SUMMARY_INJECTIVE_ON_PRIMITIVE_CORES: FALSE
P17_STATUS_KEY_REPR_INJECTIVE: FALSE
MATHEMATICAL_Th3_7_DISPROVED: NO
ORIGINAL_P17_CODE_EDITED: NO
HISTORICAL_GENERATOR_TESTS_RESULTS_EDITED: NO
AUTHOR_PDF_TEX_ZENODO_EDITED: NO
SECTION6_PRINTED_SOURCE_GAPS: 2 OPEN
THEOREM4_3_RELATIVE_C1_SCOPE: OPEN
WHOLE_PROPERTY_FPA: OPEN
NEXT: PA-P20-20260901-FULL-C1-REFERENCE-COMPLETION-AND-REDUCTION-001 / NOT_EXECUTED
```

### Execution instructions (Windows 11)

From the existing `DSD_Method_Family` checkout root:
```powershell
python DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\scripts\verify_p19_reference_limits.py DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\results\p19_reference_limits.json
```
Inputs: P17 reference Python in the *same existing `scripts/` folder*; no separate data file required. Output: P19 JSON in the established versioned `results/` folder. Running overwrites the local P19 result file; CI uses runner temporary path to preserve the recorded archive.
