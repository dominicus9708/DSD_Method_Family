# FAS-F2-T4.7-001 — Residual clausewise independence audit / 잔여 제약 독립성 감사
Date: 2026-10-19 · Protocol: FPA v0.1 · A theorem-level **internal** audit, not an external certification or paper-wide F2 PASS.

```text
AUDIT_ID: FAS-F2-T4.7-001
SOURCE: DSD_Formation_Axiom_System_EN(5).pdf, 33 pages, §4.2 printed pp.10-11
SOURCE_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
PRECOMMIT_COMMIT: ce1c6e303ebdd9148c80dc08127ed946100bd3e4
PRECOMMIT_BLOB: dea17056afe9bd40db6aced2ec14ec5d57a76119
MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND
MATHEMATICAL_VERDICT_SCOPE: six residual constraints relative to background typing and OTHER FIVE RESIDUAL CONSTRAINTS
DSD_AUDIT_VERDICT: PASS_WITH_REFINEMENT
REVISION_NEED: CLARIFICATION
CHECKS: 12/12 reviewed, 6/6 finite source-described counterinterpretations internally verified
INDEPENDENT_EXTERNAL_VALIDATION: not_established
FULL_PAPER_F2_VERDICT: not_issued
MANUSCRIPT_ZENODO_CHANGE: none
NEXT_CASE: FAS-F2-SEC4.3-001 / not_started
```

## 1. Exact original source and logical concern

Theorem 4.7 states: "After the dependencies in Proposition 4.6 are factored out, the following residual primitive constraints are independently necessary relative to the typed background and the other primitive axioms" (six constraints (i)–(vi)). Its printed proof closes by saying that other residual constraints and "the other primitive axioms" remain true.

**Scope ambiguity:** For (ii), (iii), (iv) — three *conjuncts of Primitive Axiom II* — no finite counterinterpretation can falsify one of them **and satisfy Primitive Axiom II in full**. Likewise omitting residual (i), (v), or (vi) falsifies its own parent Axiom I, III, or V. Thus reading "other primitive axioms" to include the containing parent axiom would make the exact literal requirement impossible. The scientifically coherent interpretation follows the primary list and source's exhibited proof: independence of each individual residual in the **residualized six-clause axiom presentation**, with its parent primitive axiom **replaced** by its residual clauses, not retained as a separate complete premise.

**Recommended next manuscript clarification, no immediate source edit:** Replace "relative to the typed background and the other primitive axioms" with "relative to the typed background and all other five residual constraints, with the original primitive axioms decomposed into those constraints." Replace the proof's "other residual constraints and the other primitive axioms remain true" with "other five residual constraints remain true; equivalently, every primitive axiom not containing the omitted constraint remains true, while all the other clauses of the affected primitive axiom are preserved." This is a precise domain/premise correction, not a counterexample to the residual independence result.

Do not silently edit the frozen manuscript or erase the source wording; this refinement is preserved as a **specific future section-level edit candidate**, not a mandatory immediate Zenodo release.

## 2. Proposition 4.6 audited first — logical reductions

(a) The Section 2.1 definition of restricted function `f|A` gives `dom(anch_H|mat(h))=dom(anch_H)∩mat(h)=mat(H)∩mat(h)`. If this equals `anch_h` with domain `mat(h)`, equality of function domains forces `mat(h)⊆mat(H)`. Likewise `anch_p=anch_h|act(p)` forces `act(p)⊆mat(h)`. The displayed inclusions should be kept visible as typing side conditions but cannot be counted as *independently new* primitive clauses under those equalities.

(b) The stipulated material signature is relational, with possible annotations into fixed external codomains; a retained subset gets the induced relational structure/restricted annotations by definition. Inheritance is not a separate independent axiom under the declared convention.

(c) A regime-global `q_λ:Q_λ→V_λ` is declared as one partial function and thus is single-valued. Configuration-local graphs are restrictions; single-valuedness is not a second Axiom V conjunct. Remaining V residual is `Q_λ⊆A*`.

Mathematical verdict on Proposition 4.6 as used here: consistent with the written typed convention; no new primitive assumption found.

## 3. Explicit six-constraint residual theory

Let `B` denote the manuscript's fixed well-typed set-theoretic background, with IV, VI, VII *definitional* and `A*` computed from primitive data. Define:
- R1: `∀x(Desexpr(x) ⇒ Admexpr(x))`;
- R2: `∀H,h(Res(H,h) ⇒ anch_h=anch_H|mat(h))`;
- R3: `∀H,h(Res(H,h) ⇒ Admexpr(h))`;
- R4: `∀H(Admexpr(H) ⇒ Res(H,H))`;
- R5: `∀h,p(Realize(h,p) ⇒ anch_p=anch_h|act(p))`;
- R6: `∀λ(Q_λ⊆A*)`.

Typed inference, induced relational data, global partial-function single-valuedness are background, *not seventh/eighth residuals*. The precise mathematical independence claim is, for each i in {1,...,6}, there exists a typed `M_i` with `M_i ⊨ B∪{R_j:j≠i}` and `M_i ⊭ R_i`. Equivalently, `B∪{R_j:j≠i} ⊭ R_i`. This formulation is relative to ZFC-based set-constructed counterinterpretations and ordinary soundness; it is not a claim of formal independence from all possible logics.

## 4. Nondegenerate common kernel and six counterinterpretations

All six begin from paper §4.1: `Supp(B)={s0,s1}`, `M_B={a,b}`, empty material-relational signature; `g` admitted/describable with `mat(g)={a}`, `anch_g(a)=s0`; `p` has `act(p)={a}`, `anch_p(a)=s0`; `Res(g,g)`, `Realize(g,p)`, configuration predicates at p true; `Λ={λ}`, `V=R`, `Q={a}`, `q(a)=1`, `Role(p,a,λ,ρ)`, supplied `W=R,T(c_g)=1`, and all other primitive predicates false unless specifically extended.

| Case | Violation | Other five residuals | Why only this one fails |
|---|---|---|---|
| R1 / (i) | R1 FALSE | TRUE | Add describable, unadmitted x on inert b, with no Res/Realize links |
| R2 / (ii) | R2 FALSE | TRUE | Admitted non-describable H,h on b with different anchors, sound identities, and Res(H,h) |
| R3 / (iii) | R3 FALSE | TRUE | Admitted non-describable source H and unadmitted non-describable target h on b, **matching anchors**, Res(H,H) and Res(H,h) |
| R4 / (iv) | R4 FALSE | TRUE | Admitted non-describable h on b with **no** Res(h,h) |
| R5 / (v) | R5 FALSE | TRUE | Admitted non-describable h with sound identity, Realize(h,p'), anchors of b disagree, all three configuration-admission predicates false at p' |
| R6 / (vi) | R6 FALSE | TRUE | Set Q={a,b}, q(a)=q(b)=1 while A*={a}; single-valued function remains well typed |

All six preserve `K_des={p}`, `A*={a}`, `C={c_g}`, `Comp(∅)=0` and `Comp({c_g})=1`. R3 vs R4 shows that restriction-target admission and identity restrictions are logically distinct; R2 additionally separates sound anchoring. In no case was an independent seventh constraint smuggled into the background. Different *whole* primitive axioms need not all be true: the containing parent axiom is deliberately broken.

## 5. Bounded reproducibility and evidential scope

- A pure Python standard-library verifier was constructed for six explicit source-described finite counterinterpretations, including all quantifiers over the supplied finite carriers, anchor-domain equality, configuration describability `Ψ`, source material status, admitted channel and composite.
- An in-session finite implementation ran and returned: `6/6 source-described finite residual-clause counterinterpretations VERIFIED`.
- [Repository Python verifier](../scripts/verify_t47_residual_clauses.py), commit `a337926a84b867099b74ac343d9d6a1ab9c6d93a`.
- [Repository deterministic JSON fixture](../results/t47_residual_clauses.json), commit `2aa196b30dd4b307050183ab322635e91d06cfb6`.
- GitHub source and JSON are stored to reproduce; the locally executed original implementation and committed script implement the same six source-defined fixtures but are not identical byte-for-byte. Re-running the committed script in a checked-out repository remains a reproducibility check; do not call that an externally audited CI run.
- For a checked-out repository root on Windows 11:
```powershell
py -3.11 DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_t47_residual_clauses.py --output DSD_Audit\audits\formal_proof\formation_axiom_system\results\t47_residual_clauses.json
```
- Neither a finite script nor the use of DSD Audit itself establishes the whole manuscript. For the limited independence theorem, the mathematical non-entailment is supported by **the existence of one legal counterinterpretation per residual**, not by finite enumeration over all models.

## 6. Precommit gates and final disposition

| Frozen gate | Outcome |
|---|---|
| 1. Original "other primitive axioms" scope ambiguity | REFINEMENT NEEDED — explicit clarification recorded |
| 2. Proposition 4.6 anchor-domain, induced data, partial-function reductions | PASS |
| 3–5. Six finite examples, truth tables and common active channel | PASS |
| 6–9. Cases R3/R4/R5/R6 all others preserved | PASS |
| 10–11. Parent-axiom vs residualized framework and definitional closure | PASS_WITH_SCOPE |
| 12. Separate mathematics, method audit, revision, reproducibility | PASS |

**Scoped mathematical result: PROVED_IN_DECLARED_BACKGROUND** for the six-constraint residualized presentation.
**FPA method result: PASS_WITH_REFINEMENT** because the original theorem/proof phrase "other primitive axioms" is ambiguous or literally inconsistent if the intact parent axiom is retained.
**Manuscript revision class: CLARIFICATION** — incorporate suggested precise wording when next section-level revision is warranted; no new counterexample invalidates the intended six independent residuals. This is not yet an F2 paper-wide PASS or independent external verification.

## 7. Stop and resumption
STOP after this theorem. Next begin `FAS-F2-SEC4.3-001` (Corollary 4.8, Countermodel 4.9, Lemma 4.10 and related Section 4.3 local consequences), with a **new precommit** and target-source lock.
