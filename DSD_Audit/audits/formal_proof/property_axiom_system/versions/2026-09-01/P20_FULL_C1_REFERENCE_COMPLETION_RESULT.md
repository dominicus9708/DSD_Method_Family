# PA-P20-20260901-FULL-C1-REFERENCE-COMPLETION-AND-REDUCTION-001 — source-exact non-edit audit

**Executed:** 2026-10-25 KST (GitHub Actions 2026-10-24 UTC). **Original author:** Kwon Dominicus.
**Exact frozen manuscript:** `DSD_Property_Axiom_System_EN(4).pdf`, printed 2026.09.01, 23 pp, SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.
**Prospective P20 protocol:** [P20_FULL_C1_REFERENCE_COMPLETION_PRECOMMIT.md](P20_FULL_C1_REFERENCE_COMPLETION_PRECOMMIT.md), frozen before constructing this code.
**Direct source:** Clause C1 and Definition 3.6, manuscript p9; Theorem 3.7 and its proof, p10; Definition 3.4 records (varpi,x,z), p9; typing of declared/available profiles and primitive assignment, pp7–8. The author PDF, LaTeX, Zenodo and original experiment algorithms/fixtures have **not** been changed.

## 1. Mathematical source and new independent reference implementation

In the original text, `CompProp(P)` for a PI+PII-sound, **well-typed primitive core** keeps every primitive datum intact: fixed Stage-VI inherited formation record, shared property signature, supplied auxiliary carrier maps, declaration set, primitive applicability sets, each prerequisite-satisfaction set, and primitive partial assignment **with actual assigned values**. It adds only:
- `D_varpi=Dom(Xi_varpi)`;
- `DepSat_varpi=intersection of Sat_varpi,d`, with the empty-prerequisite convention equal to the full typed input product;
- status predicates/labels for every typed input and kind-level unavailable/undeclared states;
- `Rprop={(varpi,x,z):x in D_varpi,z=Xi_varpi(x)}`, retaining typed input tuples and **exact values**.

The source's Theorem 3.7 states for admitted primitive cores `P` and full models `A`:
```text
RedProp(CompProp(P)) = P
CompProp(RedProp(A)) = A
```
Its source proof is the ordinary definitional inverse: no information in primitive coordinates is discarded in completion, while every derived coordinate is a deterministic function of those primitives; a *full property model* is required to have those exact derived coordinates.

The P17 `completion()` was deliberately only a summary of status strings, domain and prerequisite counts and is **not** injective on primitive cores; P19 proved nonzero value collisions and `repr` key collisions. **Therefore P20 implemented a distinct full reference object** in [P20 Python](scripts/verify_p20_full_c1_inverse.py), separate from P17 (unchanged).

New reference types `Primitive` / `Completion` hold exact typed `Xi` assignment values, original `Ap/Sat`, declared kinds, auxiliary carrier lists and signature; `D`, `DepSat`, and statuses are stored with **real typed input tuple keys** (not `repr(x)` string keys), and `Rprop` retains each full `(varpi,x,z)` value. `comp_prop()` runs only when frozen P17's **typed-premodel validator** confirms `admitted_core`. `red_prop()` refuses tampered derived coordinates by recomputing and comparing a canonical full completion; it returns a new primitive presentation with all original primitive coordinates preserved.

A *fixed Stage-VI interface identity* is represented by a frozen anchor label in the finite P20 audit, **not** an implementation of the entire `F_L^{<=6}` Formation Axiom System object. This distinction is material and no entire-Formation realization claim is made.

### Source-level general argument (not a proof assistant result)

On the class of well-typed primitive cores, let `J(P)` be the tuple of all C1 functional derived coordinates defined from primitive `P`. Define `CompProp(P)=(P,J(P))` and `RedProp(P,J(P))=P`. Then `RedProp(CompProp(P))=P` by projection. If `A` is by definition an admitted full model with its derived coordinates `J(P)`, `CompProp(RedProp(A))=CompProp(P)=(P,J(P))=A`. This argument **requires** the full model class to mean exactly the C1 completions of admitted cores; it is not a claim that arbitrary presentations carrying inconsistent status tables are full models.

P20's finite tests are independent **empirical examples** of this definitional argument, not a mechanical verification of every ZFC set-based object.

## 2. Finite test results: 49/49 expected controls

- [Actual code](scripts/verify_p20_full_c1_inverse.py).
- [Generated and archived JSON](results/p20_full_c1_inverse.json).

The **49 distinct tests**, all true, include:
1. The two inverse laws in both directions `Red(Comp(P))=P`, `Comp(Red(A))=A` for source-admitted full data.
2. Exact assigned values **1 and 2** are retained as different `Rprop` records; previously P17's nonzero-only summary could not distinguish them.
3. Two mathematically distinct, hashable typed inputs with the **same Python `repr`** retain two separate status keys and two exact defined records, repairing *information fidelity in the independent P20 audit* without rewriting P17.
4. Profile-unavailable kind versus declared kind with **supplied empty carrier** are distinguishable (the latter has a defined empty typed product and zero records).
5. Two contextual prerequisites use their **intersection**; absent prerequisites use the entire available typed input product.
6. Mixed inherited/auxiliary sort profile `(h,u,h)` and repeated-sort profile `(u,u)` retain complete ordered tuples in records.
7. A designated-zero change in original assigned value changes the exact completion object; status and record carry correct distinctions.
8. **Typed but PI-failing** and **typed but PII-failing** premodels are refused as inputs to source-style completion.
9. **Tampering a derived status or defined-record set** leads to rejection as a non-full model by the reduction function.
10. **Surplus metadata policy:** `ignore` mode can preserve incidental supplied source coordinates in the primitive payload while `reject` mode refuses extras. This is a specified presentation policy, not a claim that original Definition 2.5 settles the policy.
11. Primitive application sets, prerequisite sets, assignment values and fixed Stage-VI anchor are unchanged through completion/reduction.

**Interpretation:** `49/49 PASS` is a finite regression result, including expected refusal controls. It is not a complete ZFC formal proof or user-author manuscript correction.

## 3. CI execution, source custody and archive reproduction

- [P20 first actual GitHub Actions #40107536576](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40107536576): **Python 3.10 and 3.12 completed/success**, both emitted `P20 FULL C1 INVERSE BOUNDED AUDIT PASS 49` and `P20 INDEPENDENT INVERSE AND NEGATIVE AUDIT PASS`.
- Both independent job logs' JSON payloads were extracted and compared; they **matched exactly across Python versions**. The resulting JSON was archived under the established `versions/2026-09-01/results/` folder.
- [P20 archived replay #40107610139](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40107610139): Python **3.10 and 3.12 both completed/success** and printed `P20 ARCHIVED JSON MATCH`, validating saved data and actual fresh computation.
- GitHub CI explicitly verifies that P17 reference source remains Git blob `d5e796022133bf066b6d485950044f93b5d656ca` (unmodified).
- New work lives only in established versioned `DSD_Audit/audits/formal_proof/property_axiom_system/versions/2026-09-01/scripts/`, `results/`, and the separate workflow. The original author/source `DSD_Property_Axiom_System_EN(4).pdf`, Zenodo, original `Property_Axiom_System/src`, legacy tests and older results remain unchanged.

## 4. Audit obligations still OPEN

| Obligation | Current status |
| --- | --- |
| Exact source Theorem 3.7 definitional inverse on full admitted property cores | Source's set-theoretic reasoning supported; P20 finite independent reproduction PASS |
| P20 finite full completion/reduction, tamper and value-preservation | 49/49 PASS on Python 3.10/3.12; archived replay PASS |
| P17 `completion()` summary and `repr` input collision | P19 failure evidence retained; **P17 is still unchanged**; P20 is a distinct full-reference implementation |
| Any ZFC arbitrary set / full Stage-VI Formation model mechanical verification | NOT ESTABLISHED |
| Current P17 malformed Python input `TypeError` coverage | P19 found robustness gaps; P20's admission step still uses P17, so this gap is **not fixed globally** |
| Original published Definition 6.1 F3–F5 source availability guard | **MATHEMATICAL CONDITION MISSING / OPEN** |
| Original published Theorem 6.8 “bijective embeddings” abbreviation S2/S3 | **MATHEMATICAL CONDITION MISSING / OPEN** |
| Theorem 4.3 “relative to C1” qualifier | **PROOF-SCOPE OPEN** |
| Original author EN/KR TeX edit, Zenodo revision, formal proof assistant or external review | NOT DONE |

## 5. Windows 11 reproducibility command

From the established `DSD_Method_Family` repository root, with the committed scripts in their historical versioned folders:
```powershell
python DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\scripts\verify_p20_full_c1_inverse.py DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\results\p20_full_c1_inverse.json
```
No external numerical input file is necessary; P20 loads the P17 reference source from the **same scripts folder**. The above overwrites the local P20 JSON; CI instead regenerates into an isolated temporary path and compares it to the committed archive.

```text
CASE: PA-P20-20260901-FULL-C1-REFERENCE-COMPLETION-AND-REDUCTION-001
SOURCE_EN_PDF_SHA256: 03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c
GENERAL_DEFINITIONAL_INVERSE_ARGUMENT: SUPPORTED_IN_SOURCE_DOMAIN
FINITE_INVERSE_AND_NEGATIVE_TESTS: 49/49 PASS
PYTHON_3_10: PASS / ARCHIVED_JSON_EQUAL
PYTHON_3_12: PASS / ARCHIVED_JSON_EQUAL
DIFFERENT_NONZERO_VALUE_EXACT_RECORDS_PRESERVED: YES
DIFFERENT_SAME_REPR_TYPED_INPUTS_PRESERVED: YES
ORIGINAL_P17_REFERENCE_SUMMARY_MODIFIED: NO
FULL_STAGEVI_IMPLEMENTED: NO
ORIGINAL_AUTHOR_PDF_TEX_ZENODO_OR_LEGACY_EXPERIMENT_EDITED: NO
PUBLISHED_§6_MISSING_CONDITIONS: TWO / STILL_OPEN
PUBLISHED_Th4_3_C1_RELATIVE_SCOPE: OPEN
WHOLE_PROPERTY_FPA: OPEN
NEXT: PA-P21-20260901-FULL_COMPLETION_ADVERSARIAL_SERIALIZATION-001 / NOT_EXECUTED
```
