# FAS-F2-APPA-TYP-001 — Prospective Appendix A Typing and Notation source audit

Date: 2026-10-20 KST. FPA v0.1, previous completed FAS-F2-SEC9-CONC-001. **Frozen before crosswalk audit and executable selected sanity tests.** This is a SOURCE APPENDIX audit (not a numbered theorem).

## Immutable source lock

Kwon Dominicus, attached 33-page `DSD_Formation_Axiom_System_EN(5).pdf`, PDF SHA256 **8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a**. Appendix **A, “Typing and Notation,” printed p.30**, immediately after conclusion's final sentence and before Appendix B, containing **nineteen symbol/meaning table rows and a map-domain convention**. Checked PDF text extraction **and page rendering** to preserve script symbols, not raw OCR.

## Prospective scope and exact crosswalk obligations

1. B, Supp(B): fixed set-sized common candidate base and typed support carrier, §2.1–2.2, do not treat support as arbitrary singleton or infinite by definition.
2. Material-record structure `M_L` and its material carrier `M_B^L`, §2.2: structure≠carrier; material signature only material-internal **relations** and externally valued annotation functions, not material-output functions; induced subsets are possible.
3. Candidate expression/configuration `E_B^L,P_B^L`; both include unsuccessful candidates, §§2.2,6.1.
4. `Adm_expr^L,Des_expr^L` expression domain only, Primitive I.
5. `Adm_cfg^L,LC_L,BC_L` configuration domain only, Primitive III and closure IV's witness; **Des_cfg** derived, not primitive.
6. `Res_L,Realize_L` typed `E×E` and `E×P`, Primitive II/III, no required restriction transitivity unless optional Appendix D.
7. `Psi_L,A_L^*` derived formula in **primitive vocabulary**, not itself primitive field; `A_L^*:=union{act_L(p):Psi_L(p)}`; §2.2 Definition2.1.
8. `K_des^L,A_L` derived from closure IV; equality `A_L=A_L^*` in full model, §3.1.
9. `(V_{L,λ},0_{L,λ})` is **pointed set**, not necessarily a vector space and not W; §2.2.
10. `Q_{L,λ},q_{L,λ},Gamma_{L,λ}`: one regime-global partial map q defined on Q; Γ is graph; config locals are RESTRICTIONS, §3.2 V.
11. `U_L,C_L,T_L`: U candidate 5-tuples (potentially infinite), C admitted by derived Chan, T:C→W supplied POST Stage VI, **not T:U→W**, §§2.2,3.2.
12. `D_L^comp,Comp_L`: ALL FINITE **sets** of admitted channels, includes empty and no duplicates, `Comp(∅)=0_W`; §3.2 VII.
13. `F_{L≤k},F_k(B,F),π_{j,i}`: stage truncations from full model vs metatheoretic **class** of all well-typed Stage-k records, and coordinate-erasure functions between appropriate stages (π_{k,k} identity), §2.3 Def2.4/Prop2.5. Neither truncations nor record classes are full models.
14. `Tr_L(c)` candidate-channel c∈U, set of full witness histories, empty exactly when no admitted channel, Def3.5/Thm3.6; histories not channel keys.
15. `Σ_L` full descriptor, includes unsuccessful candidate classes plus supplied term data, Def6.1.
16. `FormDesc_{B,F}` is a METATHEORETIC possibly proper class of set-coded full descriptors over fixed B,F, not a set carrier, §2.1,6.1.
17. `Φ,hatΦ` forward map and INDUCED CANDIDATE-CHANNEL map; verify `hatΦ:U_L→U_M` on full candidate 5-tuples, admitted C maps into C by preservation; composite preservation requires `hatΦ|C_L` **injective** for arbitrary forward map, Def6.2/Prop6.3. J:W_L→W_M is separate F-linear component, source Appendix A omits it from shorthand table.
18. `≅_B^fix` strict base-fixed isomorphism, typed bijections plus J F-linear iso, Def6.10/Thm6.14; **not arbitrary heterogeneous (B,F)** and not J-independent composite-level coincidence.
19. `I_k(L,M),b(L,M)` Stage0..7 comparison sets, first empty index for **strictly nonisomorphic pairs**; possible b=0; Stage4 cannot first branch, Def6.15, Thm6.16/6.17/6.19/6.20.
20. Domain footnote: check that `q(a)` only Q, channel formulas use Γ rather than totalizing q, and `T(c)` only C. In general the term T(c) for unadmitted candidate c∈U\C is UNDEFINED, not zero.

## Hostile boundary tests before verdict

- Undefined q outside Q vs defined q(a)=0 on Q; detect local independent assignment attempts as invalid under V.
- A single admitted channel with T(c)=0 versus no channel; verify both give Comp(∅)=0 yet distinct C and Dcomp.
- Candidate Tr(c)=∅ while c∈U\C, and Tr(c) nonempty exactly for c∈C, including zero-term cases.
- `π_{j,i}` on nested records for all i≤j≤k≤7, `π_{k,k}=id`; Stage0 is background record NOT eighth formation stage; `F_k(B,F)` metatheoretic class, not data set materialized in Python.
- Forward channel map collision: if hatΦ maps two DISTINCT admitted channels to one target, forward map preserves each term but sum need NOT commute because family is a SET. Cite Prop6.3 injectivity caveat; potential selected counterexample without claiming source says all forward maps preserve composite.
- Appendix A's 19-row table is a summary, not an exhaustive primitive signature. Audit nonlisted `Role_L,Chan_L,W_L,J,Λδ,size,δ,Des_cfg_L,ConfAdm_L,Form_{B,F},EmbForm_{B,F}` versus main text. Flag any table misdescription, but do NOT label summarization omissions as inconsistency without misleading assertion.
- Compare types of externally anchored base B, material structure and carrier; `A_L=A_L^*` only after closure, no arbitrary ZFC class used as model carrier.
- Check prior §8 D10 fixed-J logical-weakness issue: NOT reproduced as Appendix A “≅”; no new implication claimed by table. Prior §7.3 D2 inherited-record clarity and §9 adjective remain separate.
- Source PDF/Zenodo not modified, independent external evaluation not established, total F2 audit OPEN, method family internal 22/22 unchanged. Numbered theorem14/proposition2/corollary9 and separate unnumbered §7.3/7.4/8/9 four completed; this audit will be the fifth unnumbered source section if finished.

## Outcome and next boundaries

Freeze standard statuses: SOURCE_CROSSWALK_MATCH/MISMATCH; Mathematical verdict `SOURCE_NOTATION_CONSISTENT_WITH_DECLARED_TYPING` or `SOURCE_NOTATION_TYPE_MISMATCH`; FPA `PASS_WITH_BOUNDARY`, `PASS_WITH_REFINEMENT`, `FAIL`, `INDETERMINATE`; revision `NONE`, `CLARIFICATION`, `PROOF`, `UNDETERMINED`. Optional recommendation for explicit glossary W, Role, Γ local etc, but not necessarily required revision.

Next original source **Appendix B Formation-Stage Status and Result Map**, tentative `FAS-F2-APPB-STAT-001`, NOT_STARTED until separately source-locked. After B, C, D, E and Declarations/source bibliography; whole F2 FPA remains OPEN.
