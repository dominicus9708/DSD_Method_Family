# FAS-F2-C7.4-001 — Prospective audit precommit: Arbitrarily large finite formation types

Date: 2026-10-20 KST. Existing DSD Audit/FPA v0.1. Previous T7.3 marked source-bound PROVED; C7.4 NOT_STARTED before this precommit.

## Source-locked original statement

Primary source: Kwon Dominicus, supplied `DSD_Formation_Axiom_System_EN(5).pdf`, 33 pages, SHA256 `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`. Exact locus §7.2, printed p.25, immediately after Theorem 7.3.

> Corollary 7.4 (Arbitrarily large finite formation types). For every integer n ≥ 1, there is a formation-finite full model with |M_B^L| = n. Hence the axiom system has arbitrarily large pairwise non-isomorphic formation-finite models. The construction also permits arbitrary finite partial-assignment and role data subject only to the stated typing condition.

Prerequisites: source Theorem 7.3 full finite-data realization; Definition 2.3 formation-finite; Definition 6.10 strict base-fixed isomorphism requires material bijection. Review §2.1 background (base support, fixed B/F) and distinctions among non-isomorphic structures and strict base-fixed formation-isomorphism.

## Locked proof/test obligations

1. For each n≥1 choose **a single common** set-sized B with nonempty support {s} and field F (e.g. F₂) and finite M_n of cardinality exactly n, empty relational material-record signature and constant anchor α_n(a)=s. Invoke/source-construct Theorem 7.3 over these fixed B,F. No assumption α injective or support of B has ≥n elements.
2. Prove n-indexed full models have all primitive I/II/III/V and derived IV/VI/VII: for every A⊆M_n distinct e_A,p_A and restrictions/realizations by inclusion, A*=M_n, finite Λ and R. Option A: λ,ρ singleton, pointed Vλ={0λ}, Dλ=M_n, qλ(a)=0λ, and R0={(M_n,a,λ,ρ):a∈M_n}; then C contains exactly n operational channels, W=F^(C), term basis vectors, |E|=|P|=2^n, |Dcomp|=2^n. Definitional empty seeds/partial domains also legal.
3. Nonisomorphism: if m≠n, material carriers have distinct finite cardinalities and hence **no bijection** required by Def6.10. Thus pairwise no **strict base-fixed formation isomorphism** for source-defined classification; distinguish stronger/other unqualified category notions unless grounded. Use the same B and F across all n.
4. Distinguish `∀n∃ finite L_n` from `∃ one infinite formation-finite L`; no claim of infinite material cardinality, boundless individual models, or single universal model. n may be arbitrarily large while each 2^n expression/config carrier is finite.
5. Validate source final sentence: **arbitrary but valid finite** Qλ=Dλ and role seed R0 with `a∈A∩Dλ` permitted by T7.3, not independent unrestricted role tuples. Pointed Vλ may be infinite, despite finite number of kinds/domains.
6. Hostile cases: n=0 is not necessary (Theorem7.3 handles M=∅); empty-support base invalid for positive n constant anchor; empty C and finite zero term model permitted; multiple materials anchored to same s permitted and any attempted requirement of injective anchor would break the source construction, so confirm no such source condition. Equal cardinality does not guarantee isomorphism.
7. Source-aligned reproducible Python finite selections n=1..6, two role/assignment patterns (all defined with n role channels; partial with valid empty/nonempty roles), test primitive/closure gates, |M|, |E|=|P|=2^n, singleton active witnesses, each seed's exact channel, finite family composites and pairwise no typed material bijections across distinct n. For n=6, 2^n families modest. Avoid exploding powersets of powersets or exhaustive all maps.
8. General cardinality argument independent of finite computational data; F₂ and selected n for testing are not restrictions of theorem.
9. Supply identical locally executed Python to GitHub in canonical `scripts` and deterministic JSON in `results`; verify exact Git blobs and document if byte identity cannot be confirmed. Do not claim GitHub execution if not performed.
10. Verdict independent mathematical / FPA / revision / independent external evaluation. Original PDF/Zenodo unchanged; 22/22 method-family internal standardization unchanged, full F2 audit OPEN; T4.7 optional wording note preserved.

FPA verdict candidates: MATHEMATICAL_VERDICT PROVED_IN_DECLARED_BACKGROUND/DISPROVED_BY_VALID_COUNTERMODEL/PROOF_GAP/INDETERMINATE; DSD_AUDIT_VERDICT PASS/PASS_WITH_BOUNDARY/PASS_WITH_REFINEMENT/FAIL/INDETERMINATE; REVISION_NEED NONE/CLARIFICATION/ASSUMPTION/PROOF/THEOREM/DEPENDENCY_REAUDIT/UNDETERMINED.

Next bounded unit after C7.4 must be selected from **the actual original PDF after §7.2**, likely Section 7.3 fully specified formation-finite D2 early-branch model; do not invent a theorem number. Mark **NOT_STARTED** until separate source lock.
