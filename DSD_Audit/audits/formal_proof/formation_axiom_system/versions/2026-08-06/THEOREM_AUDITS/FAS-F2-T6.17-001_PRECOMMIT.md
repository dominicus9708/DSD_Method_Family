# FAS-F2-T6.17-001 — Precommitted audit: staged determinacy and nonbranching of definitional closure

**Date:** 2026-10-19 KST · **Parent method:** existing DSD Audit / FPA v0.1 · **Status at precommit:** NOT_REVIEWED.

**Locked primary source:** Kwon Dominicus, `DSD_Formation_Axiom_System_EN(5).pdf` (33 pages), supplied local attachment, SHA-256 `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`. Printed pp.21–22, Theorem 6.17, with §§2.1/2.3 Definition 2.1/2.4; §3 Closure Clauses IV, VI, VII; §6.4 Definition 6.15. Do not assume Zenodo byte identity.

## Source-frozen four-part claim

(i) Stage 4 truncation is uniquely determined by Stage 3; Stage 6 truncation is uniquely determined by Stage 5 **plus supplied Role_L**; Stage 7 truncation is uniquely determined by Stage 6 **plus supplied W_L and T_L**.
(ii) `I_3(L,M) = I_4(L,M)` for full formation models and stage-comparison maps with *common ambient tuple universe*.
(iii) Every `Theta ∈ I_6(L,M)` induces a bijection `U_L→U_M` that preserves **and reflects** `Chan`, and hence a bijection `C_L→C_M`.
(iv) Every `Theta ∈ I_7(L,M)` induces `P_fin(C_L)→P_fin(C_M)` bijectively and preserves *every* finite composite under its F-linear term-space isomorphism.

## Prospective proof tests / falsification targets

1. Confirm `Psi(p)` has **two expression witnesses** H,h with Res(H,h), Desexpr(h), Realize(h,p), Adm_cfg, LC, BC; no substitution of a weaker realization-only formula.
2. Stage3→4: derived `Psi`, `A*`, `Des_cfg`, `K_des`, `A` uniquely set; *separately* prove exact transport of `A*` under fM and `act` via E1/Theta∈I3.
3. I3→I4: back-and-forth witnesses using **bijective** expression/configuration maps and E2, E3, E4 primitive predicates. Check both implications individually; the `K_des` equality requires surjectivity of configuration map, not just injection.
4. Stage5+Role→6: typing of candidate universe `U` as **disjoint kind-indexed union**, global partial graphs' correct local restriction `Gamma(p)`, `Chan` iff `Des_cfg∧Gamma(p)∧Role`, `C` by extension. Role must be supplied, not inferred from Stage5.
5. Theta∈I6: componentwise candidate bijection uses kind-indexed **zero-preserving** `I_lambda`, with inverse reindexed by `tau_Lambda^{-1}`; reflect local graph via E1 support, E5/E6 and E8 Role. Check source and target channels, not only one-direction preservation.
6. Stage6 + W,T→7: `Dcomp=P_fin(C)`, `Comp(F)=sum T(c)` including empty `F`, defined zero versus absent channels, and no blanket assumption all candidate terms are defined.
7. Theta∈I7: `J` becomes F-linear iso **at stage 7 only**; E9 on admitted C, injective channel map, exact finite-set sum including target family bijection and cancellation.
8. Explicit boundary countercases: remove all witnesses after Stage3 (not a matching Stage3); change Role with fixed Stage5; change supplied term T with fixed Stage6; compare a noninjective forward map rather than I6 tuple; pre-7 arbitrary J not linear; preserve some but not all primitive configuration predicates; defined-zero assigned channel versus undefined assignment.
9. Deterministic finite fixtures: at least one configuration with witness, one without, proper restriction H→h, multiple candidate expressions and configurations, global partial assignment with **0 as valid value**, two quantity kinds and one role; selected exhaustive finite candidate channels and finite families, plus I3/I4 maps.
10. Finite execution remains a *selected check* and does not prove arbitrary full Formation models. Separate mathematical verdict, audit quality verdict, revision need, external validation and whole-paper status. No source mutation; don't promote Corollary 6.18 until its own audit.

## Verdict space locked prospectively

`MATHEMATICAL_VERDICT = PROVED_IN_DECLARED_BACKGROUND | DISPROVED_BY_VALID_COUNTERMODEL | PROOF_GAP | INDETERMINATE`.

`FPA_VERDICT = PASS | PASS_WITH_BOUNDARY | PASS_WITH_REFINEMENT | FAIL | INDETERMINATE`.

`REVISION_NEED = NONE | CLARIFICATION | ASSUMPTION | PROOF | THEOREM | DEPENDENCY_REAUDIT | UNDETERMINED`.

Previously completed T6.16 and historical T4.7 wording clarification remain separate. Next case after scoped closure is C6.18; whole-paper F2 audit OPEN.
