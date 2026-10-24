# PA-P16-20260901-TYPED-PREMODEL-VALIDATION-AND-C1-INTERFACE-001 — original source vs software contract audit

**Executed:** 2026-10-24 KST. **Original author:** Kwon Dominicus.
**Exact frozen source:** `DSD_Property_Axiom_System_EN(4).pdf` (printed 2026.09.01, 23 pages, 157854 bytes), SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.
**Prerecorded non-edit obligations:** [P16 prospectively frozen protocol](P16_TYPED_PREMODEL_VALIDATION_PRECOMMIT.md), commit `1a6701c7381639c02de6e397d3b83725492bc440`.

## 1. First source/implementation distinction — a typed premodel is not just two axioms

**Source manuscript** (PDF printed pp6–9):
- Def2.1 provides distinct inherited and auxiliary input sorts, shared candidate-kind universe, **finite nonempty ordered profiles** `m≥1`, value carrier `Z_L,varpi`, prerequisite-kind universe and finite `delta_L(varpi)`, optional designated zero.
- Def2.3 interprets inherited sorts via the Stage-VI formation record, while auxiliary sort carriers are **partial set-valued data**. An unavailable carrier is *undefined*, not a supplied empty set.
- Def2.4 forms `X_A,varpi` **only when every factor is supplied**; supplied empty factors yield a defined **empty** input product.
- Def2.5 requires `Pi_A⊆hatPi_L`; for every **declared profile-available kind**, typed primitive coordinates `Ap_A,varpi⊆X_A,varpi`, `Sat_A,varpi,d⊆X_A,varpi` for all `d∈delta_L(varpi)`, and a partial function `Xi_A,varpi:X_A,varpi⇀Z_L,varpi`.
- Def2.6: primitive core = a **well-typed premodel additionally satisfying** PI/PII. C1 uniquely completes such a core, not any untyped arbitrary Python record.

**Existing unchanged software:** `Property_Axiom_System/src/property_axiom_reproduction.py`:
- `PropertySpec` has `profile, prerequisites, zero, zero_bearing` but no inherited sort declarations, candidate-kind carrier signature, `Z_L,varpi` value carrier or ambient prerequisite-kind universe.
- `PropertyModel.carrier()` only looks up `auxiliary_carriers`.
- `is_core_model()` returns exactly `primitive_axiom_i() and primitive_axiom_ii()`; those methods assume typed coordinates, and do **not** verify source typed-premodel constraints first.
- `input_product()` returns `set()` when a required sort is unavailable, conflating the return value with the defined `set()` for a supplied-empty carrier (although `profile_available()` and `status()` separately distinguish the availability states).
- `completion()` is callable even on a PI/PII-violating premodel and produces derived Python dict data; this is not automatically the manuscript's admitted `CompProp` construction.

**Verdict:** The original companion is a *source-example finite witness generator*, not a full implementation of the universal typed-premodel mathematical class. The original 7 unit tests and P9A–P12 prior independent audits remained valid in their stated **finite** domains.

## 2. Executed non-destructive negative and positive controls (22/22 observed)

New test artifact stored in **the existing original experiment repository's pre-existing audit folder**:
- [P16 independent Python](https://github.com/dominicus9708/Property_Axiom_System/blob/main/audits/2026-09-01/PA-P16_TYPED_PREMODEL_VALIDATION_AUDIT.py)
- [Actual logged output JSON](https://github.com/dominicus9708/Property_Axiom_System/blob/main/audits/2026-09-01/PA-P16_TYPED_PREMODEL_VALIDATION_AUDIT.json)
- [Dedicated P16 workflow](https://github.com/dominicus9708/Property_Axiom_System/blob/main/.github/workflows/property_p16_typed_validation_audit.yml)

Three positive controls confirmed the expected original example behavior: admissible one-input core accepted, designated defined-zero correctly statused, and defined-zero retained in completion records.

The remaining source-vs-implementation observations included all of these concrete **expected negative controls**:
1. An applicability relation containing `('ghost',)` outside the actual input product can still pass `is_core_model`.
2. A prerequisite satisfaction relation containing an out-of-product ghost can also pass.
3. A wrongly arity-two applicability tuple can be accepted for a unary kind.
4. Missing applicability coordinate for a declared profile-available kind is silently treated as an empty set.
5. Missing prerequisite satisfaction coordinate for a declared profile-available kind is silently treated as empty.
6. The code can recognize unavailable vs supplied-empty through `profile_available` and `status`, **but `input_product` returns the same empty set** for both and is therefore not a literal implementation of Def2.4's partial typed product.
7. Surplus assignment coordinates on a declared **unavailable** kind are not rejected; the source says no coordinates are *required*, not explicitly that surplus must be forbidden. **Interpretation/identity policy OPEN; don't overclassify as a core theorem failure.**
8. Extra relation and assignments on an **undeclared** kind are not rejected; the code ignores them in its core tests. Mathematical extra-metadata identity policy needs specification.
9. An auxiliary carrier label outside the intended shared sort universe is accepted because the source's allowed auxiliary-sort signature is absent from the code.
10. **There is no value-carrier `Z_L,varpi` in `PropertySpec`;** any Python object is accepted as an assigned value provided PI/PII domain inclusions hold. This prevents full source codomain validation.
11. The software accepts **empty property profiles**, although source Def2.1 requires `m≥1`; the generated no-coordinate tuple product `{()}` is not a legal paper signature.
12. Inherited input sort interpretation from the fixed Stage-VI record is not represented: an apparently inherited-only profile is treated as unavailable without an auxiliary carrier.
13. A duplicate-containing Python tuple `('x','x')` is accepted as a carrier presentation, yet the comparison enumerator compares tuple lengths, so it can reject an isomorphism with the singleton presentation even though both denote the same underlying set. **This is a concrete representation/finite-comparison fidelity issue on malformed carrier inputs, not a counterexample in the properly set-coded mathematical class.**
14. Repeating the same property declaration label in a Python tuple can cause `simple_summary` to count it twice, though `Pi_A` is a **set** in the paper. Requires normalization/validator to be faithful to set semantics.
15. A declaration label absent from `signature` raises `KeyError`, not a typed-model validation status.
16. `completion()` returns records on both original typed counterpremodels failing PI/PII; the status method applies priority labels that conceal overlapping raw status predicates, as independently established by [P15](P15_C1_COUNTERMODEL_SEMANTICS_RESULT.md). Its presence as a **Python function** must not be confused with a paper-level completion on admitted cores.

**Important counting note:** the machine output contains **22 explicit booleans**, including three positive baseline checks and multiple facets of some findings above. “22/22 PASS” means *all expected observations were reproduced*, **not that every malformed model was rejected**, and not 22 newly proved general mathematical propositions.

## 3. Verified execution and archived reproducibility

- Initial actual [GitHub Actions P16 run #40076519249](https://github.com/dominicus9708/Property_Axiom_System/actions/runs/40076519249): original code/test Git blob locked; Python 3.10 and 3.12 successfully compiled/ran the independent P16 script, each logging `EXPECTED-DETECTION PASS 22 CASES` and original **7/7 unit tests**.
- The actual generated JSON was extracted from both CI logs, parsed and compared; Python 3.10/3.12 results exactly matched, and the JSON was archived unchanged under the original repository's `audits/2026-09-01/`.
- **Archive replay** [GitHub Actions #40076576837](https://github.com/dominicus9708/Property_Axiom_System/actions/runs/40076576837), commit `bb8a59a337ddd561ed6c1549536e51a8d5b20160`: **completed/success in Python 3.10 and 3.12**, each prints `P16 ARCHIVED JSON MATCH`; original source 3 blob checks and original **7/7** unit tests pass.
- **No** original `src/`, `tests/`, original `results/` files, author source PDF/LaTeX, or Zenodo were changed.

## 4. Mathematical consequences carefully separated from code coverage

| Area | Evidence / verdict |
| --- | --- |
| Def2.5 general typed-premodel constraints | SOURCE-MATH-SUPPORTED; code does not enforce them for arbitrary untrusted input |
| Def2.6 core criterion | SOURCE-MATH-SUPPORTED: well-typed + PI + PII; `is_core_model()` checks **only PI+PII** |
| C1 completion/Th3.7 | SOURCE-MATH-SUPPORTED on actual admitted primitive cores; original code `completion()` is not an admission guard and has no general `RedProp` round-trip formal model API |
| P15 typed counterpremodel independence | SUPPORTED over typing; raw states may overlap on axiom violations; independent of the above code validator |
| P9A–P12 and original 7 finite witnesses | REPRODUCED, with finite scope, from P14R |
| Def6.1 F3–F5 missing declared-available guard | PRINTED MATHEMATICAL CONDITION MISSING, still OPEN; separate from original Python conflating missing/empty product |
| Th6.8 strict isomorphism shorthand missing S2/S3 | PRINTED MATHEMATICAL CONDITION MISSING, still OPEN; separate from duplicate tuple representation issue |
| Surplus coordinates or duplicate set-coded labels | NORMALIZATION / REPRESENTATION-IDENTITY POLICY, not automatic core axiom contradiction |
| Original verifier trusts stored success flag | CODE-RESULT-VERIFIER-COVERAGE GAP from P14R, not retested directly by this P16 code |
| Arbitrary-domain source math proof assistant certification | NOT ESTABLISHED |

## 5. Suggested next *non-edit* audit gate

Prepare a separate typed-premodel **reference validator** in the established audit area, with explicit shared signature, inherited and auxiliary sorts, candidate declaration kinds, prerequisite sets and value carriers. Test malformed input rejection without modifying the author's original Python, then perform differential checks against the P16 failures while preserving all original passing finite witness outputs.

This will make a clean **typed reference specification** available for the eventual decision whether to strengthen the original reproduction program. Such new validator results must not silently alter the source's admitted full-model class or prior experiment data. Proposed case:
`PA-P17-20260901-INDEPENDENT-TYPED-REFERENCE-VALIDATOR-001`.

## 6. Current gate

```text
CASE: PA-P16-20260901-TYPED-PREMODEL-VALIDATION-AND-C1-INTERFACE-001
EXACT_SOURCE_PDF_SHA256: 03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c
SOURCE_DEF2_5_DEF2_6_TYPING: VERIFIED
ORIGINAL_PYTHON_TYPE_VALIDATOR_COMPLETENESS: INSUFFICIENT_FOR_ARBITRARY_INPUT
P16_INDEPENDENT_TESTS_EXPECTED_OUTCOMES: 22/22
GITHUB_PYTHON_3_10: PASS / ORIGINAL_7_7_PASS / ARCHIVE_EQUAL
GITHUB_PYTHON_3_12: PASS / ORIGINAL_7_7_PASS / ARCHIVE_EQUAL
MATHEMATICAL_AXIOMS_PI_PII_C1_REFUTED: NO
PRINTED_SECTION6_TWO_GAPS: STILL_OPEN
PRINTED_THEOREM4_3_C1_RELATIVE_SCOPE: STILL_OPEN
ORIGINAL_CODE_RESULTS_MANUSCRIPT_ZENODO_MODIFIED: NO
WHOLE_PROPERTY_FPA: OPEN
NEXT: PA-P17-20260901-INDEPENDENT-TYPED-REFERENCE-VALIDATOR-001 / NOT_STARTED
```
