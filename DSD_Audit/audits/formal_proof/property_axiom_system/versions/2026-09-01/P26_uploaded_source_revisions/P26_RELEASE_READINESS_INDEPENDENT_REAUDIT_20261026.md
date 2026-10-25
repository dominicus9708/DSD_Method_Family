# P26 independent re-audit: is the bilingual revision ready for final release?

Date: 2026-10-26 KST. Author: Kwon Dominicus. Status: targeted mathematical release review, NOT whole-FPA closure.

## Accepted P26 evidence
Original supplied EN(3)/KR(3) sources and new P26 PDFs/TeX were independently read. P26 preserved 56 numbered environments, 36 labels, 13 sections and 3 appendices; 24-page EN and 21-page KR PDFs compiled. EN/KR normalized displayed-math consistency and existing P20/P22/P23/P24 full-JSON Python 3.10/3.12 regression passed according to archived P26 CI [40210203224](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40210203224). Core P24 repairs are present in both revised texts. These are reproducibility/source-coherence tests, NOT whole-manuscript mathematical completeness proofs.

## New issue 1: Definition 9.1 summary formula contradicts its label-retention explanation

Both revised languages print a summary of the form
`(|Pi_A|, { (|D_A,w|, N0_A,w, Nneq0_A,w) : w in Pi_A })`.
This is an unindexed SET of numerical triples; despite neighboring prose, no property-kind label w is an element of the triple. Duplicate triples collapse and swapping the counts across labels leaves this value unchanged. Deterministic finite example: two labels alpha,beta with triples (0,0,0) and (1,0,1); swapping the label assignments preserves the printed summary but changes the prose-intended label-retaining summary.

Minimal bilingual amendment:
`(|Pi_A|, { (w, |D_A,w|, N0_A,w, Nneq0_A,w) : w in Pi_A })`
or an indexed family. Then the prose “labels remain associated” is accurate. Theorem 9.2's existing two-kind witness remains a valid equal-summary/nonisomorphism witness even for this stronger summary, so no known fatal inconsistency of the theorem follows.

Classification: MATH-DEFINITION-NOTATION SOURCE PATCH NECESSARY BEFORE LABEL-RETAINING CLAIM IS RELEASED.

## New issue 2: Definition 6.3 free prerequisite-kind index

Both languages give embedding equivalences for applicability, prerequisite satisfaction `Sat_A,w,d`, and assignment-domain membership under quantification over a declared and available w and every source x, but **do not bind d explicitly** in the embedding definition. Neighboring F4 and proof suggest the intended quantifier `for every d in delta_L(w)`.

Minimal safe amendment: give three separately scoped clauses: (E1) applicability iff for each source input; (E2) for EVERY prerequisite d in delta_L(w) satisfaction iff for each source input; (E3) assignment-domain iff for each source input. Do NOT place all three biconditionals inside a new universal quantifier over d: if delta_L(w) is empty, that would make applicability/domain reflection vacuous. Keep value preservation (F5) on domain.

Classification: FORMAL VARIABLE-BINDING CLARIFICATION NECESSARY TO REMOVE AMBIGUITY. The intended definition and Th6.8 remain plausible; no fresh countermodel to the intended theorem is claimed.

## Other remaining audit boundaries

- Def2.5 clauses (2)-(4) could explicitly repeat the declared+available scope, although the ending sentence already supplies it.
- Appendix C item7's scope “every declared kind” may be clarified by reference to profile-available kinds in step4.
- P26 equal EN/KR math counts (78 display, 218 inline) do not prove full natural-language theorem/proof translation equivalence. Manually inspect the edited mathematical quantifier prose after amending.
- Finite regression is not independent proof for arbitrary ZFC-set typed signatures, and external peer evaluation/Zenodo publication remain separate.

## Final release gate

For review as a draft: sufficiently traceable with stated limitations.
For declaring a final corrected paper: NOT YET; amend Def6.3 and Def9.1 in both languages, verify precise equations/labels/proofs and recompile, run P20–P26 source/build regressions, then perform independent human proof-scope review.
No current published PDF/LaTeX/Zenodo was modified. Whole Property FPA remains OPEN.
