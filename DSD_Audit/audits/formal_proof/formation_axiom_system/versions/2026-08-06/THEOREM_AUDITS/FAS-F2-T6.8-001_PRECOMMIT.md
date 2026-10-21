# FAS-F2-T6.8-001 — Prospective proof-audit precommit

Date: 2026-10-19 KST
Protocol: DSD Audit / FPA v0.1
Pre-audit state: Theorem 6.8 NOT_REVIEWED; previous C6.6/C6.7 complete.
Frozen source: Kwon Dominicus, DSD_Formation_Axiom_System_EN(5).pdf, 33 pages, SHA-256 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a.
Printed page: 17; Theorem 6.8, with Definitions 6.1/6.2/6.4, Proposition 6.3, Closure IV/VI/VII and Theorem 6.5.

## Exact frozen theorem (source transcription)
"A formation embedding preserves and reflects configuration describability and admitted-channel membership on its image. It also preserves every finite composite under the induced channel injection."

Source proof outline: forward preservation comes from Proposition 6.3; witness reflection plus Closure IV gives configuration describability reflection; R4 and R5 reflect other channel conjuncts of Clause VI; injectivity of f_P, f_M, tau_Lambda, tau_R and I_lambda gives injected channel mapping, so finite composition result is Proposition 6.3.

## Locked obligations, before empirical witness tests
T1: Precisely typed channel candidates c in U_L, image candidate Φ-hat(c) in U_M, including q definedness/zero and role.
T2: For each source candidate configuration p, prove Psi_L(p) iff Psi_M(f_P(p)); distinguish forward implication from independently assumed witness reflection.
T3: For every source candidate channel c (not only c in C_L), prove c in C_L iff Phi-hat(c) in C_M using Clause VI plus R4/R5, zero-preserving I and witness reflection. Distinguish "on its image" from "every target channel".
T4: Prove induced channel map injective using the full typed tuple and injectivity of f_P, f_M, tau_Lambda, I_lambda, tau_R (and source lambda index alignment). Do not wrongly use f_E or J alone to establish channel injectivity.
T5: For all finite F subset C_L, prove J(Comp_L(F))=Comp_M(Phi-hat[F]) from linearity, F6 and injectivity. Check empty F and defined-zero channels, cancellation, terms T independent of assigned v.
T6: Construct legal nondegenerate full Formation source/target models with correct primitive axioms, restriction identity, realization anchor, A-star/q domain, admission, term maps; test admitted, non-admitted, absent q, missing role, and target-only channels.
T7: An adversarial *forward* map (not embedding) whose target-only witness changes Psi at image should fail reflection; an isomorphic embedding with witness-reflection satisfies it. Search for a genuine theorem countermodel under all embedding premises.
T8: Independent runtime verification of checked finite cases; finite checks NEVER imply universal proof.
T9: Preserve earlier FPA and Theorem 4.7 clarification status; audit only T6.8, not paper-wide approval.

## Predeclared result classification
MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND | DISPROVED_BY_VALID_COUNTERMODEL | PROOF_GAP | INDETERMINATE.
DSD_AUDIT_VERDICT: PASS | PASS_WITH_BOUNDARY | PASS_WITH_REFINEMENT | FAIL | INDETERMINATE.
REVISION_NEED: NONE | CLARIFICATION | ASSUMPTION | PROOF | THEOREM | DEPENDENCY_REAUDIT | UNDETERMINED.
If countermodel or proof gap is found, record it without post-hoc replacement. No edits to the frozen paper/Zenodo before a separately scoped revision.
