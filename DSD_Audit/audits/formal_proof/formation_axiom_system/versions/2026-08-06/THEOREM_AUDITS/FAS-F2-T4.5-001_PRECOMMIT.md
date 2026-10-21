# FAS-F2-T4.5-001 — prospective FPA precommit

Date: 2026-10-19. Status at freeze: **NOT_VERDICTED**. First substantive check of Formation Theorem 4.5, after completed Theorem 3.3 audit. No source or conclusion edited.

## Locked source and exact subject
- Kwon Dominicus, *Formation Axiom System: Dimensional-Structural Describability*, supplied 33-page English PDF `DSD_Formation_Axiom_System_EN(5).pdf`.
- SOURCE_SHA256: `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`.
- Exact manuscript locus: Section 2.2 primitive sorts/data, pp.4–5; Section 3.1 Axioms I–III and Clause IV, p.7; Section 3.2 Axiom V, Clauses VI–VII, pp.8–9; Section 4.1 introductory witness and Countermodels 4.1–4.4, Theorem 4.5, pp.9–10. The source PDF is authority, not earlier audit paraphrases.
- Target claim: relative to declared typed background and fixed closure Clauses IV, VI, VII, **no** one of Primitive Axioms I, II, III, V follows from the remaining three.
- Explicitly distinguish `counterinterpretation to the omitted-axiom theory` from a valid full Formation model requiring all four axioms (Definition 2.2).

## Frozen construction and expected check obligations (not expected truth values)
K0 common nondegenerate witness over `Supp(B)={s0,s1}`, `M_B={a,b}`, empty relational material signature, `g,p` with material and active material `{a}`, anchors at `s0`, admitted/describable g, `Res(g,g)`, `Realize(g,p)`, configuration predicates true, `Λ={λ}`, `V=R`, `Q={a},q(a)=1`, `R={ρ}`, `Role(p,a,λ,ρ)`, `W=R`, `T(c_g)=1`. All unlisted relations/predicates false.

K1 Countermodel 4.1: add `x`, `mat(x)={b}`, `anch_x(b)=s0`, `Desexpr(x)=true`, `Admexpr(x)=false`, no Res/Realize for x. Check only Axiom I false.
K2 Countermodel 4.2: add admitted non-describable `H,h`, each material `{b}`, `anch_H(b)=s0`, `anch_h(b)=s1`, `Res(H,H),Res(h,h),Res(H,h)`; check II false because cross-restriction anchors disagree and I/III/V retained.
K3 Countermodel 4.3: add admitted non-describable `h` and `p_prime`, each use b, `anch_h(b)=s0`, `anch_pprime(b)=s1`, `Res(h,h)`, `Realize(h,p_prime)`, all configuration predicates false at p_prime. Check III false; in particular `p_prime` does not enlarge A*.
K4 Countermodel 4.4: extend `Q={a,b}`, `q(a)=q(b)=1` without introducing describable configurations containing b. Check V false precisely on `Q subset A*` and distinguish single-valuedness from this residual constraint.

## Prospective gates
1. Verify each listed datum is legal under Section 2.2 typing and all admitted expressions possess identity restrictions except when II is deliberately targeted.
2. For all 4 constructions compute truth-value table for I/II/III/V, including universally quantified cases.
3. Verify the **entire soundness** clause of II/III (anchor, domain inclusion, inherited induced relational material structures); not just a selected witness.
4. Confirm derived Clause IV `Ψ,Des_cfg,A*` is defined without using the omitted axiom as a premise and evaluate all candidate configurations.
5. Confirm Clause VI gives `c_g` and no unintended channels; Clause VII supplies a valid finite-sum map and its empty sum.
6. Verify non-vacuity in *every* counterinterpretation: material, candidate expressions/configurations, Res, Realize, `K_des`, Q, Role and admitted channels nonempty.
7. Check whether the claimed independence requires full-model status (it should not) and whether the supplied well-typed input can be extended relative to W,T via Theorem 3.3.
8. Run adversarial boundary attacks: target identity restriction in 4.2; p_prime active material in 4.3; x described/unadmitted inert in 4.1; b active nowhere in 4.4; nontrivial W/T; all unlisted relations false.
9. Treat independence of the **four primitive axioms** separately from Theorem 4.7 residual clausewise minimality (NOT audited here).
10. Record mathematical verdict, process verdict, code/finite-evidence status, scope, and manuscript revision separately. Distinguish observation of one failure from universal axiom independence only insofar as a single fully specified legal counterinterpretation suffices to refute each entailment.

## Outcome discipline
`MATHEMATICAL_VERDICT`: PROVED_IN_DECLARED_BACKGROUND / DISPROVED_BY_VALID_COUNTERMODEL / PROOF_GAP / INDETERMINATE.
`DSD_AUDIT_VERDICT`: PASS / PASS_WITH_BOUNDARY / PASS_WITH_REFINEMENT / FAIL / INDETERMINATE.
No PASS is precommitted. Any discovered flaw is preserved and assigned to the correct axiom; no tweaking frozen fixtures after observing outcomes.
No Zenodo or original PDF change. Update GitHub and Notion in the same work unit. Stop after this one theorem group; next Theorem 4.7 remains NOT_REVIEWED.
