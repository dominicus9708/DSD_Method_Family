# FAS-F2-T4.7-001 — prospective precommit (residual clause independence)

Date: 2026-10-19. STATUS AT PRECOMMIT: NOT_VERDICTED.
Source: Kwon Dominicus, *Formation Axiom System: Dimensional-Structural Describability*, 33-page user-supplied PDF, SHA-256 `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`, printed pp.10–11, §4.2, Proposition 4.6 + Theorem 4.7.
Previous cases 3.3 and 4.5: independently recorded, not automatically inherited as proof of T4.7.

## Audit subject — source-based, not assumed true
Proposition 4.6:
(a) typed anchor function equality implies the subset inclusion on material/active domains;
(b) induced material-record structures make inherited relations and fixed-external-codomain restrictions definitional;
(c) regime-global single-valuedness comes from a partial *function* signature, not an independent residual axiom.

Theorem 4.7 enumerates 6 residual constraints:
R1 `Desexpr(x) -> Admexpr(x)` (Axiom I);
R2 every `Res(H,h)` preserves anchoring `anch_h=anch_H|mat(h)` (Axiom II);
R3 every restriction target `h` is admitted (Axiom II);
R4 every admitted `H` satisfies `Res(H,H)` (Axiom II);
R5 every `Realize(h,p)` preserves anchoring `anch_p=anch_h|act(p)` (Axiom III);
R6 every quantity assignment domain `Q_λ⊆A*` (Axiom V).
The theorem says these are independently necessary and its proof describes six constructions based on §4.1's common active kernel.

## Locked challenge questions
1. **Ambiguity attack (theorem statement):** How can a residual clause of Axiom II be false if one keeps that entire primitive axiom among the "other primitive axioms"? Identify exact coherent basis of independence: background typing + derived closure + the other **five residual clauses**. Explicitly record any needed theorem wording adjustment, not silently repair the source.
2. Check Proposition 4.6's anchor-domain implication for arbitrary partial restriction convention `f|A`, not just examples. Type-induced material relation inheritance and q graph single-valuedness must not re-enter residual list.
3. Construct **six distinct source-specified** well-typed finite counterinterpretations, fixing the common §4.1 `g,p,a,λ,ρ,c_g` kernel; default unlisted relations/predicates false.
4. For each `R_i`, verify `R_i=false` and all other `R_j=true` across the full finite domains.
5. Each interpretation retains source-listed positive `K_des={p}, A*={a}, C={c_g}, Comp(∅)=0, Comp({c_g})=1`.
6. Target iii: non-admitted/non-describable restriction target with *matching* anchors and identity on admitted source; thus R2,R4 preserved.
7. Target iv: admitted, non-describable isolated expression without identity restriction; the other restrictions must satisfy target admission and anchoring.
8. Target v: `p'` intentionally non-describable, so A* remains {a}; the deliberately mismatched realization must violate only R5.
9. Target vi: extra domain b is a legal well-typed element, q remains a single-valued partial function; violation must be R6 not an extra independent axiom.
10. Distinguish the **six residual logical clauses** from four original primitive axioms and original full-Formation models. Do not claim independent full model that violates its own constitutive axiom.
11. Check typed background and definitional closures IV, VI, VII can all still be interpreted, including no unintended channels from new inert material.
12. Separate result classes: MATHEMATICAL_VERDICT, DSD_AUDIT_VERDICT, REVISION_NEED, proof coverage and computational evidence. Find full-scope countermodel before asserting falsity; if ambiguity is material, use PASS_WITH_REFINEMENT or PROOF_GAP, as justified.

## Prospectively defined outputs and limits
- Evaluate independently whether all 6 non-entailments are mathematically sound.
- Explicitly identify literal wording vs coherent rephrasing, using **source quote locations and exact affected phrases**.
- A complete arithmetic script may support finite witness reproducibility but is not an independent third-party assessment or a universal automated proof certificate.
- Preserve historical source PDF and prior audit verdicts; no Zenodo edits without explicit decision.
- After one theorem, stop and checkpoint. Next Section 4.3 Corollary 4.8 + Countermodel 4.9 + Lemma 4.10 group is NOT_STARTED.

No PASS/FAIL or revised theorem statement is asserted in this precommit.
