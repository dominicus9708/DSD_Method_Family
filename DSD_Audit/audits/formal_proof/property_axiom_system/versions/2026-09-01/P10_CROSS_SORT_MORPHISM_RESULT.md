# PA-P10-20260901-CROSS-SORT-MORPHISM-REGRESSION-001 — executed multi-sort map stress audit

**Executed 2026-10-23 KST.** Manuscript author **Kwon Dominicus**. Original locked `DSD_Property_Axiom_System_EN(4).pdf`, 23 pages, date printed 2026.09.01, SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.

**Prospective source-audit obligations:** [P10_CROSS_SORT_MORPHISM_PRECOMMIT.md](P10_CROSS_SORT_MORPHISM_PRECOMMIT.md), Git blob `851fec00d4b86d3d1ae81f9042f81640a4827b36`; created in the previous audit turn before construction and execution of the new checker.

## 1. Defined finite stress universe — not every admissible model

A fixed common Formation Stage-VI background and shared Property signature with TWO optional auxiliary input sorts `u,v`; THREE distinct retained labels:
- `p: (u,v)`, a mixed binary ordered product;
- `q: (v,u)`, the *reversed ordered* mixed binary product;
- `r: (u,u)`, a repeated-sort binary typed product.

Each auxiliary carrier is (0) **unavailable**, (1) supplied singleton, or (2) supplied two-element set `{0,1}`. No available-but-empty carrier is included. Candidate declaration sets are the SIX explicitly selected families `∅,{p},{q},{r},{p,q},{p,q,r}`. Each declared **profile-available** kind has an independently valid PI/PII-compatible supplied primitive `Ap,Sat_d,Ξ` from FOUR deterministic tested templates:
1. Full applicability, full dependency-satisfaction, undefined assignment;
2. Full applicability/satisfaction, assigned value 0 at the first typed input;
3. Restricted applicability with full dependency satisfaction and undefined assignment;
4. Full applicability with restricted dependency satisfaction and undefined assignment.

`Ap,Sat` are defined only for declared and *actually available* profiles; a declared but profile-unavailable kind remains a distinct permitted kind-level state, **not an empty typed product**. The templates do not enumerate all possible assignment graphs, assigned nonzero values, multiple prerequisite sets, empty supplied carriers or arbitrary inherited sorts. There are `9 × 6 × 4 = 216` template expressions, many duplicate identical primitive cores because unavailable or undeclared kinds make template choice immaterial. Deduplication gives **108 distinct full primitive cores** over the fixed background.

## 2. Executed numerical evidence

| Test | Actual count |
| --- | ---: |
| distinct legal full cores | **108** |
| ordered source/target core pairs | **11,664** |
| candidate componentwise carrier maps tested | **30,318** |
| valid source-profile-guarded forward maps | **9,253** |
| valid source-profile-guarded embeddings | **3,054** |
| valid S1–S4 strict isomorphism maps | **168** |
| composable forward-map PAIRS whose composite satisfies F1–F5 | **629,926** |
| composable embedding-map PAIRS whose composite satisfies reflection/injectivity | **34,589** |
| composable strict-isomorphism PAIRS whose composite is strict | **336** |
| source/target ordered pairs first branched at Stage 1 | 10,064 |
| first branch Stage 2 | 1,294 |
| first branch Stage 3 | 150 |
| first branch Stage 4 | 48 |

The two-sort checker enumerates *all componentwise set maps* for each ordered pair of its 108 template cores, including **nonidentity permutations of supplied two-element carriers** and nonbijective maps. It enumerates the full family of carrier bijections for Stage-1 through Stage-4 comparison *within the finite universe* (not just a chosen candidate bijection).

## 3. Tests actually enforced

The independent checker asserts:
- Full typed ordered-input tuple mapping according to each kind's exact profile. It does not swap property-kind labels `p,q,r`.
- Every original primitive core satisfies PI and PII; includes legal declared-but-unavailable property kinds.
- For all source-guarded F1–F5 map families, identity and **all composable map-pair** closures (629,926 actual map pairs).
- For all source-typed injective and reflective embeddings, all 34,589 composable map pairs preserve the embedding conditions.
- S1–S4 full strict maps preserve/reflect the primitive data, invert under set-carrier bijections and compose in all 336 actually available composable map pairs. There are 168 strict maps (more than one per isomorphism class due to nontrivial carrier automorphisms).
- All 11,664 core pairs satisfy nested stage-comparison cardinalities, `I4=I5`, and `I4>0 iff at least one full S1–S4 strict comparison`. Pairwise symmetry of full stage comparison cardinalities was independently enforced.
- There is a valid legal core where a declared kind has an unavailable profile, confirming literal Definition6.1 unguarded F3 is ill typed.
- There exist source-to-target componentwise carrier-bijective embeddings with unequal declaration sets, so the source Theorem6.8 shorthand is insufficient.
- A core with a defined property record exists. Under the source's *optional representation-package* definition, identical one-record selected domains can independently be encoded as 0 vs 1, giving an **elementary separate conceptual witness** for core-isomorphic but representation-nonisomorphic models. The automated multi-sort checker does **not enumerate a complete space of representation packages**, so this latter fact is a source-level deduction, not an additional claimed numeric exhaustive test.

**No third mathematical inconsistency was discovered in the tested finite family.** The previous **two §6 scope/claim issues** survive. Their proposed repairs (source profile availability guard; strict S2/S3 declaration/availability equalities alongside component bijections) are supported in this *bounded* setting only, not mathematically established for every possible ZFC source model by finite enumeration.

## 4. Actual code/execution chain (not inferred)

- New GitHub source: [verify_p10_cross_sort.py](scripts/verify_p10_cross_sort.py), **CI-reported SHA256** `ecc37d19ed2c2a6b2849fb07f08fec9d0a0192e0c5cb3e9bc4386384368b39b4`.
- Machine-generated and GitHub-committed [p10_cross_sort_ci.json](results/p10_cross_sort_ci.json), **CI output SHA256** `18b3c39576c8f0b9eb90b3aa37e70d7254c4d4176d1425fb13e86780a028f0e3`.
- Dedicated workflow [`.github/workflows/property_fpa_p10.yml`](https://github.com/dominicus9708/DSD_Method_Family/blob/main/.github/workflows/property_fpa_p10.yml), commit `2e5815bfbdba0a83f2fc9c4ed68d60096aa2c4f7`.
- **New actual GitHub Actions [run #39923494959](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/39923494959)** has `status=completed / conclusion=success`, original commit SHA `2e5815bfbdba0a83f2fc9c4ed68d60096aa2c4f7`.
- Python **3.12**, job `120314117255`: compiled and executed the GitHub script, compared fresh runner JSON with committed JSON, **all SUCCESS**.
- Python **3.10**, job `120314117737`: same, **all SUCCESS**.
- Both job logs independently report `P10 CI PASS 108`, candidate/forward/embedding/strict counts above, `P10 archived JSON equals fresh GitHub CI calculation`, matching source/output SHA256.
- Existing original `dominicus9708/Property_Axiom_System` software `src/`, `tests/` and numerical fixtures were NOT modified. Original PDF, LaTeX and Zenodo were NOT edited or published.

## 5. Scope limitations and subsequent non-edit obligations

- Full generalized property source has **56/56 numbered items manually scope-audited** by the earlier P9B1–P9B5 work. This is **not** 56/56 independently proven ZFC theorems.
- Exhaustive enumeration is only over the 108 **explicitly selected** finite templates. No available-but-empty auxiliary carriers, 3+ sorts, arbitrary ordered profile lengths, property assignments taking nonzero values, multiple prerequisite kinds, inherited-sort/cross-typed maps, or arbitrary representation packages were part of P10's full numerical search.
- Future source-level universal proof work should derive identities and composition of F1–F5/embedding/S1–S4 by induction on finite ordered profile length and stable substitution/transport of `Ap,Sat_d,DomΞ`, including declared-but-unavailable profile scope. It should separately check target extra declarations and inclusion submodel preorder, negative/empty carrier edge cases, and representation functoriality with actual selected tuple-domain data.
- There is **no requirement to modify original numerical experiment Python** because this independent stress checker was added under `DSD_Method_Family` version-specific FPA; any future author manuscript section edits are an independent P9 (source-edit) gate, not this test.
- Next non-edit gate recommended: `PA-P11-20260901-UNIVERSAL-MORPHISM-PROOF-001` beginning with explicit statement of corrected minimal map domain guards and separate hypothesis closure. **FPA whole paper remains OPEN**.

```text
CASE: PA-P10-20260901-CROSS-SORT-MORPHISM-REGRESSION-001
LOCKED_SOURCE_PDF: 2026.09.01 English / SHA verified
BOUNDED_MODELS: 108
BOUNDED_ORDERED_PAIRS: 11664
BOUNDED_CANDIDATE_CARRIER_MAPS: 30318
FORWARD_MAPS: 9253
EMBEDDINGS: 3054
STRICT_ISOMORPHISMS: 168
ALL_COMPOSABLE_FORWARD_MAP_PAIRS: 629926 PASS
ALL_COMPOSABLE_EMBEDDING_PAIRS: 34589 PASS
ALL_COMPOSABLE_STRICT_PAIRS: 336 PASS
MULTI_SORT_TYPED_ORDER_AND_PERMUTATIONS: PASS_WITH_BOUNDARY
PYTHON_3_10_GITHUB_CI: PASS / SOURCE_AND_JSON_EQUALITY
PYTHON_3_12_GITHUB_CI: PASS / SOURCE_AND_JSON_EQUALITY
FPA_TWO_EXISTING_SECTION6_GAPS: OPEN
NEW_THIRD_FATAL_CONTRADICTION: none_found_in_family
GENERAL_ZFC_THEOREM_FROM_FINITE_ENUMERATION: not_established
FULL_PROPERTY_FPA: OPEN
AUTHOR_MANUSCRIPT_AND_ORIGINAL_EXPERIMENT_SOFTWARE_EDITED: no
NEXT: PA-P11-20260901-UNIVERSAL-MORPHISM-PROOF-001 / NOT_STARTED
```
