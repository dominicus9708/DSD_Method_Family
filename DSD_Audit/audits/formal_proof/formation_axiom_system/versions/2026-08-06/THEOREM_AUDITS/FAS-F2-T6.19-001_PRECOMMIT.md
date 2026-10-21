# FAS-F2-T6.19-001 — prospective FPA theorem audit / 사전고정

Date: 2026-10-19 KST.
Method: existing DSD Audit / Formal Proof Audit (FPA) v0.1.
Immutable source: Kwon Dominicus, attached `DSD_Formation_Axiom_System_EN(5).pdf` (33 pages), SHA-256 `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`.
Exact source locus: §6.4, **Theorem 6.19 (Symmetry and strict-isomorphism invariance of first branching)**, printed page 22, Definition 6.15 stages S1–S8 and strict Definition 6.10 E1–E9.
Prior case: FAS-F2-C6.18-001 / PROVED_IN_DECLARED_BACKGROUND / PASS_WITH_BOUNDARY / REVISION_NEED NONE. T6.19 NOT_STARTED before precommit.
Source version frozen. No Zenodo byte-identity inference.

## Prospectively locked exact claim
1. For **each k=0,...,7**, `I_k(L,M)≠∅ iff I_k(M,L)≠∅`.
2. `b(L,M)` and `b(M,L)` have identical definedness and are equal when defined.
3. If `L' ≅_B^fix L` and `M ≅_B^fix M'`, then for **each k=0,...,7** `I_k(L,M)≠∅ iff I_k(L',M')≠∅`.
4. Hence defined `b(L,M)=b(L',M')`; first-branching index depends only on ordered strict-isomorphism classes and is symmetric in the two arguments.

## Frozen attack plan
- General proof k≤6: invert *only* carrier/kind/role/pointed-value bijections, indexed by target kind. Reverse J: choose the **zero function** W_M→W_L, NOT inverse of arbitrary possibly nonbijective J. Ensure J is part of a full comparison tuple but its stage-k effect is unrestricted.
- General proof k=7: J is F-linear isomorphism by S8; use genuine inverse J^{-1}; check E9 reverse using bijection of admitted channels and E1–E8.
- At every k verify preservation/reflection of E1 anchored isomorphism, E2/E3/E4 predicates and relations, derived I4, E5 graph domain/undefined vs defined zero, E6 graph biconditional, E7 *only qualified negligible* sizes/threshold, E8 role, then E9 at 7. Check that inverse of zero-preserving pointed bijections preserves zero and right indexed value spaces.
- For strict representative replacement choose orientations `A:L'→L` and `B:M→M'` and conjugate full comparison tuple `B∘Theta∘A`. Components are bijections; before7 `J_B∘J_Theta∘J_A` remains **an arbitrary map**, not assumed linear or invertible; at7 it is an F-linear isomorphism. Prove each stage condition remains iff; compose with strict A^{-1}, B^{-1} for the converse. No claim of unique or canonical representative.
- Derive b symmetry and invariance from **each** nonempty/empty stage indicator, not merely from I7; avoid claiming set equality of oppositely typed tuple sets. No b numeral if I7 nonempty.
- Counterexamples to weakened claims: blindly invert an arbitrary pre7 J that is not bijective; replace same-base *strict* requirement by forward embedding or numerical-composite match; mis-index inverse I. These do **not** falsify source theorem but reveal why hypotheses matter.
- Finite selected source-typed model examples: reverse k=0,...,7 profile and strict renamed representatives; include b=0,1,2,3,5,6,7 and b undefined, defined-zero graph and a Stage7 term-space dimension mismatch. Derive expected counts and test bi-implications. Execute tests where feasible, save Python and JSON under existing repo folder; finite checks are NOT proof of general theorem.
- Separate MATHEMATICAL_VERDICT, DSD_AUDIT_VERDICT, REVISION_NEED, author-led vs external validation, and source PDF/Zenodo status. Preserve historical T4.7 optional wording recommendation; no paper-wide certification.

Verdict options: PROVED_IN_DECLARED_BACKGROUND / DISPROVED_BY_VALID_COUNTERMODEL / PROOF_GAP / INDETERMINATE; PASS / PASS_WITH_BOUNDARY / PASS_WITH_REFINEMENT / FAIL / INDETERMINATE; NONE / CLARIFICATION / ASSUMPTION / PROOF / THEOREM / DEPENDENCY_REAUDIT / UNDETERMINED.

Next after this one bounded theorem case: FAS-F2-T6.20-001 (Theorem 6.20, Static formation closure), NOT_STARTED.
