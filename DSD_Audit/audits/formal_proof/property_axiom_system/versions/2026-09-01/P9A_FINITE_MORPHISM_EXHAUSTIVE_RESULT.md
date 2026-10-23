# PA-P9A-20260901-FINITE-MORPHISM-EXHAUSTIVE-001 — verified full finite-map and comparison challenge

**Execution date:** 2026-10-23 KST. **Author of manuscript:** Kwon Dominicus.
**Exact input:** general Property Axiom System EN PDF `DSD_Property_Axiom_System_EN(4).pdf`, 23 pages, printed 2026.09.01, SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.
**Prerecorded obligations:** [P9A prospective checklist](P9A_FINITE_MORPHISM_EXHAUSTIVE_PRECOMMIT.md), Git commit `38e4a4ef5644be947755018e71499bc62ddab8b9`, committed *before execution*.

## 1. Exact finite universe (new independent checker, not the old Python)

Fix any shared Formation Stage-VI background and one auxiliary sort `u`. Fix **two distinct property-kind labels** `p, q`, each of profile `(u)`, each with one prerequisite `d`, value carrier `{0,1}`. The auxiliary carrier is either unavailable (the property can nevertheless be declared; no typed product exists), or available as the singleton `{x}`. For an available profile, each declared kind independently specifies primitive applicability membership of x, prerequisite-satisfaction membership of x, and a partial assignment (undefined or defined 0/1), with both soundness axioms enforced.

There are exactly 4 full cores with u unavailable (`2²` independent declared/undeclared kinds), and 49 with u available (`7²`: one undeclared state + six legal declared combinations for each kind). **Total = 53 legal full primitive cores with unique C1 completion.**

**This is a deliberately small, completely enumerated, source-derived subfamily**, not all full Property models, all functions, or arbitrary typed signatures.

## 2. Observed exhaustive results

| Grounded quantity | Count |
| --- | ---: |
| legal full cores | 53 |
| ordered model pairs | 2,809 |
| source-available-guarded forward property maps | 854 |
| source-available-guarded embeddings | 347 |
| carrierwise-bijective embeddings (every available source component bijective) | 347 |
| strict S1–S4 property isomorphisms | 53 |
| strict-isomorphism classes | 53 |
| first branch Stage 1 ordered pairs | 392 |
| Stage 2 | 1,044 |
| Stage 3 | 1,200 |
| Stage 4 | 120 |

The above counts are for a fixed singleton/unavailable sort and fixed labels, not claimed as manuscript's original finite witness counts.

Programmatically checked **every legal pair** for nested comparison sets, `I4=I5`, strict equivalence iff Stage-4 comparison survives, comparison symmetry, and replacement-by-strict-isomorphic-object invariance. Checked all `53³=148,877` ordered model triples for closure under composition of repaired forward maps, embeddings, and full S1–S4 strict maps. All checks passed, and first branching witnesses occurred at every possible primitive comparison stage 1 through 4.

## 3. Two exact math boundaries confirmed

**P5-A, Definition 6.1 source F3–F5 is not well typed on all literal declared kinds:**
An otherwise admissible full core has `Pi_A={p}` with u unavailable. Definition 2.5 permits that model and explicitly supplies **no** `X_A,p`, `Ap_A,p` or `Xi_A,p`. The source F3 literally says `For every varpi∈Pi_A, product map phi_varpi:X_A,varpi→X_B,varpi` ... That map does not exist for A=B, even on the alleged identity of this full core. The paper does not state the needed source-availability guard in F3–F5.
**Verdict:** an explicit *typing/quantifier guard* is needed to justify the claimed category over **every** currently admitted full model; it is not correct to mark this as falsifying the underlying two soundness axioms. With the condition `varpi∈Pi_A AND available_profile_A(varpi)`, the 53-core category test is PASS.

**P5-B, Theorem 6.8 “strict iff bijective embedding” (without declaration/availability conditions):**
Take A with no declared property kinds and B with q declared, both with no auxiliary carrier available. The (empty) family of auxiliary carrier maps A→B is componentwise bijective by the empty-family convention, the F1/F2 and all source-indexed embedding conditions hold, **but strict S3 requires `Pi_A=Pi_B`, which fails**. This example is mathematically allowed by both core axioms and C1. There are also examples with both auxiliary carriers available as matching singletons and different declaration sets. Thus componentwise bijective embedding cannot be a standalone sufficient definition of strict isomorphism.
**Verdict:** original definition S1–S4 is *not* contradicted; instead the shorthand “bijective embeddings” is missing conditions, and Theorem 6.8/summary must be worded carefully.

**New quantitative witness from the finite family:** there are 347 carrierwise-bijective embeddings but only 53 strict isomorphism comparisons, so **294** carrierwise-bijective embeddings fail strict conditions. This counts a deliberately restricted 53-core family; it is not a count for all property models.

## 4. Real executed provenance

- Locally ran `python -W error -m py_compile` and a full execution with the independent script and generated JSON.
- Uploaded code: [P9A 53-core Python](scripts/verify_p9a_finite_morphisms.py), Git blob `c04eb5ae30a8088ec7baf23aa1926a6d03a0b34a`, **verified CI source SHA256 `05e00fd453dfd916df07119c5c86129e2a0a68f6e31b5dd006ed87f80772586d`**.
- Uploaded result: [P9A JSON](results/p9a_finite_morphisms.json), **new-run SHA256 `0ce85ba6095e8fb8e1a4311547ea1378b249df7a66ae3b12f6ad0a80277bf939`**.
- Exact GitHub-repository script was compiled/executed, and its fresh result JSON was compared structurally to the version-committed JSON in **both Python versions**:
  [GitHub Actions #39897341069](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/39897341069), commit `5eb1643582a0e22269b3443833299dd7da31d66f`, `completed / success`.
  - Python 3.10 job `120230708576`, compile, execution and JSON equality PASS.
  - Python 3.12 job `120230708740`, same three checks PASS.
- The original property experiment repository `dominicus9708/Property_Axiom_System` remains unchanged. Earlier 7/7 tests in both Python versions belong to **a different** software suite; no conflation with this new P9A checker.

## 5. Limits and future source audit

This finite check does **not** establish universal category/equivalence theorems. It supports the source-bound countermodels and shows that the *repaired readings* are **consistent over the entire 53-core family**. Different typed signatures, multiple elements, more auxiliary sorts, and full universal theorem reasoning require separate scrutiny.

A separate, old P9 source-edit task remains blocked on author LaTeX. New non-edit next case is `PA-P9B-20260901-56-CLAIM-ROW-REVIEW-001`: claim-by-claim review of 56 original numbered items with hypothesis typing, hidden all-quantifiers and dependencies, not automatic PASS import from P1–P8. Archive results per small batch, preserving original source PDF.

```text
PA_P9A_FINITE_53_CORES: PASS
PA_P9A_2809_PAIRS: PASS
PA_P9A_148877_TRIPLES: PASS
PYTHON_3_10_REPO_CI: PASS
PYTHON_3_12_REPO_CI: PASS
P5_A_MISSING_SOURCE_PROFILE_GUARD: CONFIRMED
P5_B_BIJECTIVE_EMBEDDING_SHORTHAND: CONFIRMED_WITH_LEGAL_COUNTERMODEL
UNIVERSAL_THEOREM_PROVED: no
OLD_EXPERIMENT_SOURCE_MODIFIED: no
MANUSCRIPT_EDITED_OR_PUBLISHED: no
GENERAL_PROPERTY_FPA: OPEN
NEXT: PA-P9B-20260901-56-CLAIM-ROW-REVIEW-001 / NOT_STARTED
```
