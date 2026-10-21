# FAS-F2-T3.3-001 — audit result for Theorem 3.3
**2026-10-19 · First substantive FPA v0.1 audit; theorem-local, NOT a paper-wide F2 certificate.**

```text
SOURCE: DSD_Formation_Axiom_System_EN(5).pdf, 33 pages
SOURCE_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
ORIGINAL_LOCUS: printed PDF pp. 8-9, Section 3.2
AUDIT_ID: FAS-F2-T3.3-001
PRECOMMIT_COMMIT: 033fb2159d05635f27059bed6e04c3ad4593f55c
PRECOMMIT_BLOB: 98a2194d8d11d53e5c10bdc1bf6dbbc7323f9e33
MATH_VERDICT: PROVED_IN_DECLARED_BACKGROUND
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE
OPTIONAL_NONBINDING_EXPOSITION: show explicit zero-vector-space witness for every primitive core
CHECKS: T1-T10 inspected and supported, 10/10
SCOPE: relative closure, supplied (W_L,T_L), ZFC-relative set constructions
FINITE_WITNESS_CODE_EXECUTED_IN_THIS_AUDIT: no
EXTERNAL_INDEPENDENT_VALIDATION: not_established
ZENODO_OR_MANUSCRIPT_CHANGED: no
NEXT_CASE: FAS-F2-T4.5-001 (not started)
```

## A. Source-derived formal statement (scope exact)
Theorem 3.3 states that any **well-typed primitive input** uniquely determines derived Formation data via Clauses IV and VI through the channel set `C_L`. After **an F-vector space W_L and an actual function T_L:C_L→W_L are supplied**, Clause VII uniquely completes the finite composition layer. For a primitive input satisfying Axioms I, II, III, V, the result is a full Formation model. Conversely, the primitive reduct of every full Formation model is such a core. This is **not** absolute uniqueness when the supplied `W_L` or `T_L` changes.

Evidence sections in the frozen PDF:
- printed pp. 3–5: set-sized convention, primitive carrier/typed data, Definitions 2.1 and 2.2;
- printed p. 7: Axioms I–III; Clause IV; assignment Axiom V;
- printed p. 8: graph/local restrictions, Clause VI, supplied `W_L,T_L`, Clause VII, Theorem 3.3 statement;
- printed p. 9: printed proof and Remark 3.4.

## B. Independent mathematical reconstruction of the proof (ZFC-relative)
Let `D` be fixed **well-typed primitive data**, including each source relation, `Role_L`, and assignment partial map `q_(L,λ):Q_(L,λ)→V_(L,λ)`. All sorts are sets by Section 2.1.

S1. For each candidate configuration `p∈P_B^L`, construct the explicitly given witness predicate
`Ψ_L(p) = ∃H,h[Res_L(H,h) ∧ Desexpr_L(h) ∧ Realize_L(h,p) ∧ Admcfg_L(p) ∧ LC_L(p) ∧ BC_L(p)]`.
The quantifiers range over the **already supplied set-sized typed expression carriers**. No choices of witnessing pairs are made in the output predicate.

S2. Define `Descfg_L(p) := Ψ_L(p)`, `Kdes_L := {p∈P_B^L : Ψ_L(p)}`, and `Ades_L := ⋃_{p∈Kdes_L}act_L(p)`; Section 2.1 set formation and extensionality make all three unique. Definition 2.1 gives `A*_L = Ades_L`.

S3. For fixed primitive maps `q_(L,λ)`, define the graphs `Γ_(L,λ) = {(a,q_(L,λ)(a)):a∈Q_(L,λ)}`, and restrictions `Γ_(L,λ)(p)`. They are uniquely determined; their existence does **not** establish Axiom V for an input which fails it.

S4. The typed disjoint union `U_L = ⨆_{λ∈Λ_L}(P_B^L×M_B^L×{λ}×V_(L,λ)×R_L)` is determined from the primitive sorts and value spaces.

S5. Define `Chan_L(p,a,λ,v,ρ)` by the biconditional of Clause VI, namely `Descfg_L(p) ∧ (a,v)∈Γ_(L,λ)(p) ∧ Role_L(p,a,λ,ρ)`. Then `C_L={c∈U_L:Chan_L(c)}` is uniquely determined; an individual witness history is not a component of channel identity.

S6. Supply `W_L` as an F-vector space and a genuine total term map `T_L:C_L→W_L`. Do not treat these as outputs uniquely forced by the core.

S7. Form the set `Dcomp_L=P_fin(C_L)` and define `Comp_L(F)=Σ_{c∈F}T_L(c)`. Existence uses ordinary finite set formation and vector addition. The finite-set sum is order independent because vector addition is associative/commutative, and its empty value is `0_(W_L)`. It is extensional in `F`.

S8. Uniqueness: if `E,E'` extend **the exact same** `D,W_L,T_L` and each satisfies IV, VI, VII, their `Descfg,Kdes,Ades,Γ,U,Chan,C,Dcomp,Comp` are pairwise equal by S1–S7. Thus the relative expansion is unique, not just unique up to unspecified isomorphism.

S9. Any core `D` satisfying Primitive Axioms I–III and V has **at least one** admissible supplied post-VI pair: let `W_L={0}` be the zero F-vector space and `T_L:C_L→{0}` be the unique constant-zero function (including for `C_L=∅`). Then S1–S7 produce a full model according to Definition 2.2. This elementary existence witness is *implicit* in the supplied-data setup and is offered as nonmandatory expository clarification.

S10. The primitive reduct of any full model already satisfies I–III and V by **Definition 2.2**. Together with S9, the set/class of primitive reducts of all full models equals the class of primitive formation cores. This is not a claim that IV–VII alone imply the independent primitive axioms.

Mathematical conclusion: within the stated **typed set-theoretic, set-sized, F-vector-space** setting, the printed statement is derivable. The proof does not grant uniqueness across different externally supplied `W,T`.

## C. Precommitted test-by-test assessment
| Test | Outcome | Evidence / status |
|---|---|---|
| T1 | PASS | Set-sized typed input and supplied F-vector space/total `T` distinguished explicitly in §§2–3. |
| T2 | PASS | `Ψ,Des_cfg,Kdes,Ades` are fixed by formulas without witness selection, including empty case. |
| T3 | PASS_WITH_SCOPE | `A*=Ades`; `Q⊆A*` is Axiom V and **not** derived for axiom-violating raw input. |
| T4 | PASS | Typed disjoint union and `Chan,C` uniquely fixed by Clause VI. |
| T5 | PASS | `P_fin(C)` and finite unordered sums determined by supplied `W,T`, including `Comp(∅)=0_W`. |
| T6 | PASS | Different supplied `T` can produce different full expansions, and therefore does not contradict the explicitly *relative* uniqueness. Multiple histories do not change `C`. |
| T7 | PASS_WITH_EXPOSITORY_NOTE | Every core extends using the zero F-vector space and `T(c)=0`; this witness is not expressly spelled out in the printed proof but follows without strengthening assumptions. |
| T8 | PASS | Converse primitive-reduct statement is definitional under Definition 2.2. |
| T9 | PASS | Empty channels, zero term and nonunique trace cases are lawful; a violation of Axiom V does not yield a full model. No countermodel to the locked theorem premises was found in the reviewed boundary classes. |
| T10 | PASS | Mathematical result does not prove primitive-axiom independence, physics, absolute uniqueness, new empirical laws or independent validation. |

## D. Adversarial boundary cases and limitations
1. **Empty channel set:** with no admitted operational channels (e.g., empty role relation) take `C_L=∅`. Then `T:∅→W` is unique for each supplied W, `P_fin(∅)={∅}`, and `Comp(∅)=0_W`. Relative closure still works.
2. **Multiple histories:** two different `(H,h)` pairs may witness the same `Ψ(p)`, but both produce the same boolean `Descfg(p)`; no arbitrary witness selection enters the closure. This does not assert there is always one witness.
3. **Defined zero vs absent channel:** a present `c∈C_L` may have `T(c)=0_W`; an absent channel `c∉C_L` is outside the term-map domain. This does not break existence/uniqueness.
4. **Different post-VI data:** with a legal nonempty admitted-channel model and e.g. `W=F`, compare term maps `T_0(c)=0` and `T_1(c)=1` on the same channel. Resulting composite values differ; *absolute* closure uniqueness would be false, but that is not what Theorem 3.3 asserts. With C empty, choosing different W likewise changes the supplied data, not relative uniqueness.
5. **Raw input violating V:** if `Q_λ⊄A*`, derived predicates may still be mechanically defined, but no full formation model under Definition 2.2 is obtained. The theorem is conditional precisely on being a primitive core.
6. **Background-dependence:** construction assumes ordinary ZFC-style sets and standard properties of F-vector spaces. Neither self-consistency of ZFC nor categoricity or independent external checking is established.

Adversarial outcome: **no counterexample satisfying all locked theorem premises identified** in these inspected classes. The finding is supported primarily by the general set-theoretic derivation S1–S10, not by a finite counterexample search.

## E. Cross-paper and claim boundaries
- This audit checks only the logical claim of Theorem 3.3 and its direct definitions/clauses. It does not automatically certify Theorem 3.6, Axiom Independence Theorem 4.5, branching invariance including 6.17/6.20, or Theorem 7.3.
- Downstream Formation→Property→Static Aggregation→Dynamics compatibility is **not** audited here.
- If future work changes primitive data, stage definitions, vector-space contract or supplied map typing, Theorem 3.3 must be reopened under a new source version.
- The zero-vector-space argument shows model-class *existence*, not a nontrivial channel or a physically meaningful term realization.

## F. Decisions and next checkpoint
```text
THEOREM_3_3_MATH: PROVED_IN_DECLARED_BACKGROUND
FORMAL_AUDIT_EXECUTION: PASS_WITH_BOUNDARY
FOUND_CRITICAL_GAP: no
REQUIRED_THEOREM_REVISION: no
OPTIONAL_EDITORIAL_NOTE: explicit zero-space witness for all-core expansion
IMPACT_ON_F2_FULL_PAPER: one theorem reviewed, others open
NEXT: FAS-F2-T4.5-001 — independently test all four primitive-axiom countermodels (4.1–4.4)
```
This is an **author-project internal, model-assisted proof audit**; independent verification is not claimed.
