# PA-P17-20260901-INDEPENDENT-TYPED-REFERENCE-VALIDATOR-001 — audited result

**Executed:** 2026-10-24 KST. **Manuscript author:** Kwon Dominicus.
**Exact source locked:** `DSD_Property_Axiom_System_EN(4).pdf`, 23 pages, printed 2026.09.01, SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.
**Prerecorded constraints:** [P17 precommit](P17_INDEPENDENT_TYPED_REFERENCE_VALIDATOR_PRECOMMIT.md). User asked for autonomous continuation; original author paper, Zenodo, `Property_Axiom_System/src`, `tests`, and `results` remain untouched.

## 1. Source-faithful domain / code separation

Directly reviewed original PDF printed pages **6–10**:
- Definition 2.1 fixes inherited and auxiliary sort labels, inherited Stage-VI carriers, candidate property kinds and finite **nonempty** ordered profiles `m>=1`, explicit value carriers `Z_L,varpi`, optional distinguished zero inside the value carrier, and finite sets of contextual prerequisite kinds.
- Definition 2.3 supplies auxiliary carrier sets as a **partial** function, so an unavailable sort is **not** a supplied empty set.
- Definition 2.4 forms `X_A,varpi` only when each factor exists; an available empty factor gives a defined empty product, with ordered/repeated coordinates retained.
- Definition 2.5 defines well-typed **property premodels** with declared kinds subset of candidate kinds and `Ap,Sat_d,Xi` coordinates on declared available profiles; exact typed relation subsets, partial-function graph with values in `Z`. An axiom-violating but well-typed premodel is legitimate.
- Definition 2.6: admissible **primitive property core** means *well-typed premodel plus PI plus PII*. C1 (p9) completes only such a core, with unique derived coordinates; it does **not** claim that any arbitrary malformed Python dict is completable.

### New reference code

- [Independent validator and differential checker](scripts/verify_p17_typed_reference_validator.py), residing only in the versioned **DSD_Method_Family P17 audit** directory; the original experiment repo remains unchanged.
- [Actually executed frozen JSON](results/p17_typed_reference_validator.json), from **real Python 3.10/3.12 CI jobs**.
- [New dual-Python workflow](https://github.com/dominicus9708/DSD_Method_Family/blob/main/.github/workflows/property_fpa_p17.yml) checks out a second, unchanged `dominicus9708/Property_Axiom_System` repository and refuses to continue if its original `src/property_axiom_reproduction.py` Git blob differs from `04844beca113c24267660fcbb09bc8f833403a28`.

The independent implementation has its own `Kind`, `Signature`, `Premodel` data contracts, not `PropertySpec`. It checks available typed products, explicit finite value carriers, partial assignment function graphs, declaration and prerequisite signatures, missing mandatory coordinates, nonempty profiles, duplicates in set-coded presentations, and **separates**:
```text
INVALID_PRESENTATION    [typing/signature/required-coordinates violation]
TYPED_PREMODEL          [well typed but PI or PII fails]
ADMITTED_CORE           [well typed AND PI AND PII]
```
Only `ADMITTED_CORE` is permitted to enter the reference `completion` function.

## 2. All 30 independent positive and expected-negative controls passed

Actual source-independent controls include:
- valid designated-zero original-like core and completion;
- out-of-product application and prerequisite-satisfied set elements;
- wrongly ordered/input-length tuple;
- out-of-product assignment input and a value **outside its specified value carrier**;
- deliberately **nonfunctional** assignment graph (same input, two different values);
- missing applicable, prerequisite and assignment primitive coordinates;
- unknown candidate kind and unknown auxiliary sort;
- duplicated sort-carrier and duplicated property declarations as malformed **presentations**;
- illegal **zero-length** input profile, unknown profile sort, unknown prerequisite kind, distinguished zero outside its carrier;
- both **typed but axiom-failing premodels**, with C1 refusal before admission;
- a **supplied-empty** carrier and an **unsupplied** carrier retained as distinct (defined empty product vs no typed product);
- inherited-sort mixed profile and repeated-sort profile;
- **two explicitly separate surplus metadata policies**: `ignore` or `reject`. The original English text says no coordinates are *required* for unavailable or undeclared kinds; it does not on its own force a universal policy for surplus incidental source metadata.

**Interpretation:** 30/30 means the **expected checks were reproduced**, including many intentional negatives. It does *not* mean 30 arbitrary user-submitted Python presentations were all valid or that infinite ZFC source models are mechanically certified.

### Source/scope caveats about this reference validator

- Each selected finite input/value carrier in the Python tests is a hashable Python set coding; **this is a finite audit implementation**, not an implementation for all possible set-theoretic values/Stage-VI physical records.
- Source Section 4's example value carrier is `R`; for the *differential finite witness test only*, the actual original Python's observed assigned values all lie in a deliberately chosen **finite subcarrier `{0,1,2}`** used by the reference comparator. It establishes membership in a compatible finite codomain, **not equivalence of every mathematical signature or all real-valued cases**.
- To test set semantics robustly, duplicated source-carrier tuples and repeated declarations are rejected as **noncanonical Python presentations**; this is a validation/normalization convention for the reference tool, not an asserted new theorem that the original ZFC theory forbids duplicate entries in every serialization.
- A dictionary represents a single-valued partial function by construction; a separate iterable graph case detects conflicting repeated input/value pairs.

## 3. Differential audit of all *actual* original constructors

The P17 preregistration said “all original seven witness constructors”; direct code inspection found **EIGHT original `construct_*` functions**, returning **THIRTEEN actual models**: four single models, three 2-model comparison witnesses, and a 3-model forward-map chain.

The original functions were dynamically imported and invoked from the **separate freshly checked-out historical repository**, not hand-retyped expected outputs. The complete actual observed classifications were:

| Source original fixture | Independent verdict |
| --- | --- |
| `construct_pi_countermodel()` | TYPED_PREMODEL, PI false / PII true |
| `construct_pii_countermodel()` | TYPED_PREMODEL, PI true / PII false |
| `construct_one_input_model()` | ADMITTED_CORE |
| `construct_status_witness()` | ADMITTED_CORE |
| `construct_stage2_branch()` (two models) | ADMITTED_CORE / ADMITTED_CORE |
| `construct_stage3_branch()` (two models) | ADMITTED_CORE / ADMITTED_CORE |
| `construct_stage4_branch()` (two models) | ADMITTED_CORE / ADMITTED_CORE |
| `construct_forward_map_chain()` (three models) | ADMITTED_CORE / ADMITTED_CORE / ADMITTED_CORE |

**Result: 13/13 source model classifications match their intended mathematical roles**, of which **11/11 were well-typed, sound admitted cores**, and **2/2 were well-typed, intentionally PI/PII-violating premodels**. C1 was actually invoked and passed for each of the 11 valid reference cores only. The two counterpremodels were **not** reclassified as full models.

This gives a stronger validation of the original **particular** examples without fixing or discarding past witnesses. It does NOT restore the original `PropertyModel.is_core_model()` as a comprehensive arbitrary-input validator; P16 found valid negative controls against that general claim.

## 4. Actual GitHub Actions custody and replay

- [Initial run **#40085322170**](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40085322170): completed **success** in Python **3.10 and 3.12**, each logged `P17 REFERENCE VALIDATOR 30 self tests; 13 actual original models` and `P17 INDEPENDENT ACTUAL-ORIGINAL DIFFERENTIAL PASS`. Both complete machine-generated output JSON objects were extracted from actual job logs, parsed and checked equal, then archived with no mathematical-content changes.
- [Archive replay **#40085361331**](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40085361331): completed **success** in Python **3.10 and 3.12**, each checked original code Git blob, ran all independent and original-constructor differential tests, then printed `P17 ARCHIVED JSON MATCH` against the GitHub-committed JSON.
- Original experiment Git blob pinned to `04844beca113c24267660fcbb09bc8f833403a28`.
- This P17 source and JSON live exclusively in `DSD_Method_Family/DSD_Audit/audits/formal_proof/property_axiom_system/versions/2026-09-01`; original P9A–P16 results, author PDF/TeX and original experiment code were not overwritten.

## 5. Remaining mathematical and code obligations

| Aspect | Evidentiary status |
| --- | --- |
| Exact original general premodel/core typing rules | REVIEWED; P17 independent finite reference validator conforms to the tested contractual cases |
| 30 reference positive/negative observations | EXECUTED_AND_PASS |
| Eight actual historical constructor functions / 13 models | EXECUTED; **2 typed premodels** and **11 admitted cores** |
| Differential compatibility with original examples | PASS within chosen finite-value embedding, not entire signature |
| Malformed input rejection in the **original** PropertyModel | STILL INCOMPLETE; no original code modification |
| Original `verify_property_axiom_results.py` result-tamper detection | STILL INCOMPLETE per P14R; not part of P17's code changes |
| Surplus metadata semantics | TWO POLICY VARIANTS EXPLICITLY DISTINGUISHED |
| Core-relative C1 completion/reduction in general ZFC | P15 mathematical interpretation remains distinct; not globally proof-assistant-verified |
| Published Definition6.1 F3–F5 guard | **SOURCE CONDITION MISSING — OPEN** |
| Published Theorem6.8 bijective-embedding shorthand S2/S3 | **SOURCE CONDITION MISSING — OPEN** |
| Theorem4.3 “relative to C1” interpretation | **PROOF SCOPE OPEN** |
| EN/KR source parity, author manuscript revisions, Zenodo, peer review | NOT EXECUTED / OPEN |

**Conclusion:** New reference validator and actual original fixture differential are **PASS WITH FINITE SCOPE**. No new source-core contradiction was found. Do not infer complete proof of the full General Property Axiom System, automatic acceptance of arbitrary serialized source data or external independent refereeing.

## 6. Existing location / Windows 11 execution

From the **`DSD_Method_Family` repository root** and with the original repository checked out separately:
```powershell
python DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\scripts\verify_p17_typed_reference_validator.py DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\results\p17_typed_reference_validator.json --original-src ..\Property_Axiom_System\src
```
This example assumes sibling working copies named `DSD_Method_Family` and `Property_Axiom_System`; specify the actual `--original-src` location on the user's Windows PC if different. Execution overwrites the named P17 audit-result JSON; CI instead uses temporary runner output and checks equality to the archived file.

```text
CASE: PA-P17-20260901-INDEPENDENT-TYPED-REFERENCE-VALIDATOR-001
EXACT_ORIGINAL_PDF_SHA256: 03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c
P17_SELF_POSITIVE_NEGATIVE_CONTROLS: 30/30 PASS
ORIGINAL_CONSTRUCTOR_FUNCTIONS: 8
ORIGINAL_CONCRETE_MODELS: 13
TYPED_AXIOM_FAILING_COUNTERPREMODELS: 2/2 CORRECTLY_CLASSIFIED
WELL_TYPED_ADMITTED_CORES: 11/11 CORRECTLY_CLASSIFIED
PYTHON_3_10_GITHUB_CI: PASS / FRESH_ARCHIVED_JSON_EQUAL
PYTHON_3_12_GITHUB_CI: PASS / FRESH_ARCHIVED_JSON_EQUAL
GENERAL_ARBITRARY_SET_THEORETIC_MODELS_FORMAL_PROOF: NOT_DONE
PUBLISHED_SECTION6_CONDITION_GAPS: TWO OPEN
PUBLISHED_THEOREM4_3_C1_RELATIVE_SCOPE: OPEN
ORIGINAL_AUTHOR_MANUSCRIPT_EXPERIMENT_SOURCE_FILES_CHANGED: NO
WHOLE_PROPERTY_FPA: OPEN
NEXT: PA-P18-20260901-DIFFERENTIAL-VALIDATOR-METAMORPHIC-AUDIT-001 / NOT_STARTED
```
