# General Property Axiom System 2026-09-01 — English source-edit proposals only

**Status: NOT APPLIED to any manuscript or Zenodo file.**
Manuscript author: **Kwon Dominicus**.
This is a source-bound independent audit proposal, not a new theorem. Source `DSD_Property_Axiom_System_EN(4).pdf`, printed 2026.09.01, SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.
The editable English/Korean LaTeX source was not available in the accessible source inventory when this proposal was drafted. When the author supplies source, edit **one section at a time**, prefix each edited section with a LaTeX comment delimiter `% -----`, keep original numbering/labels/citations and match Korean 1:1. Do not insert text by blind PDF-to-TeX replacement.

## Section 6.1 — Definition 6.1, F3–F5 (typed-availability guard)
**Motivation:** Def2.5 admits declared kinds with unavailable profiles. For these kinds `X_A,varpi`, `Ap_A,varpi`, `Xi_A,varpi` need not exist; literal “For every varpi∈Pi_A” in F3 is not well typed.

**Proposed qualification preceding F3 (adapt to exact source style):**
> Conditions (F3)–(F5) are imposed for each property kind `varpi∈Pi_A` **whose input profile is available in A**. By (F1), every such profile is also available in B, so the product map `phi_varpi:X_A,varpi→X_B,varpi` is well defined. A declared but profile-unavailable kind carries no application, prerequisite-satisfaction, or assignment coordinate to which (F3)–(F5) could apply.

Update F3's “For every” quantifier accordingly, F4 “for every prerequisite `d∈delta(varpi)` **for such varpi**”, and F5 to the same source-available scope. Do **not** silently convert declared profile-unavailable kinds to undeclared kinds.

## Section 6.2 — Definition 6.3 (typed embedding reflection)
Qualify “for every source input `x∈X_A,varpi`” as **“for every source-declared property kind varpi whose profile is available in A, and every input x in X_A,varpi”**. Reflect applicability, each required prerequisite and assignment-domain membership on exactly those typed inputs.

## Section 6.3 — Theorem 6.8 (strict equivalence summary)
Keep the proof that strict isomorphism under S1–S4 is an equivalence relation. Replace bare
> “Equivalently, strict property isomorphisms are exactly the bijective property embeddings.”

with e.g.
> “Equivalently, strict core property isomorphisms are the property embeddings for which all available auxiliary carrier maps are bijective, the available auxiliary-sort sets and declared property-kind sets coincide, and the inverse maps satisfy the corresponding bidirectional comparison conditions (S1)–(S4).”

This prevents treating componentwise bijective carrier maps as proof of source/target declaration or availability equality.

## Abstract and Section 11 — dependent claim synopsis
Replace short phrase “strict property isomorphisms are exactly the bijective embeddings” with a form that refers explicitly to **bijection plus identical available-sort and declared-property sets and two-way condition preservation**. Similarly qualify Theorem11.1 item (7) without altering its strict-equivalence relation statement.

## Section 9.2 — information loss prose
Replace unqualified aggregate hierarchy wording with:
> “Equality of selected downstream aggregate values does not generally reconstruct strict property equivalence. An implication in the reverse direction for a particular bridge requires suitable compatibility of that bridge and its output comparison with the underlying strict isomorphism.”

This distinguishes §9's internally defined summary collision from externally supplied bridge values.

## Manuscript metadata only
- The actual PDF title subtitle is `A Typed Applicability-and-Dependency Extension of the Formation Axiom System`; the GitHub README uses `A General Typed Property Extension of the Formation Axiom System`. Synchronize only upon the author's chosen canonical title.
- After new-version proof and code verification, update the manuscript's “reproducibility repository is intended to accompany the final public version” wording to describe the actual accessible repository accurately.
- Preserve all original theorem numbers and evidence references, and archive the earlier PDF/TeX as version-specific historical source; do not overwrite.

**Verdict:** `SOURCE_PATCH_PROPOSED / NOT_APPLIED`; next actual TeX/PDF modification **requires the real editable canonical source** and separate bilingual/compilation re-audit.
