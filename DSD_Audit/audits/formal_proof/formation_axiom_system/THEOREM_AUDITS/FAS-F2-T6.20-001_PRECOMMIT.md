# FAS-F2-T6.20-001 — Precommitted audit: Static formation closure

Date KST: 2026-10-20. Existing DSD Audit / FPA v0.1. Previous checkpoint: T6.19 completed, T6.20 **NOT_REVIEWED before this precommit**.

**Frozen source:** Kwon Dominicus, attached `DSD_Formation_Axiom_System_EN(5).pdf`, 33 pages, SHA256 `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`. Exact source: §6.4 **Theorem 6.20 (Static formation closure)**, printed p.23; Section 2.2–2.3, Clauses IV/VI/VII and previously audited dependencies. Zenodo byte identity not asserted.

## Exact 5 claims and locked dependencies

(i) **Relative unique closure:** Every **primitive formation core**, together with **supplied post-Stage-VI term data** `W_L` and total `T_L:C_L→W_L`, has a unique full closure expansion. Source dependency: Theorem 3.3. No canonical W or T inferred from primitive data alone.

(ii) **Reduction coherence and trace iff:** Stage reductions are coherent, `π_{j,i}∘π_{k,j}=π_{k,i}`, and a typed candidate operational channel c is admitted iff its formation-trace set Tr(c) is nonempty. Source dependencies: Proposition 2.5 and Theorem 3.6. Do not turn trace witness multiplicity into channel multiplicity.

(iii) **Definitional layers no independent obstruction:** Each definitionally closed Stage IV/VI/VII depends exactly on its primitive or separately supplied data, no free new branching obstruction from these *as definitional layers*. Source dependency: Theorem 6.17, especially I3=I4; **do NOT falsely infer I5=I6 or I6=I7** or b not 6/7, since Role and W/T are independently supplied.

(iv) **Map identities/composition:** Forward maps and witness-reflecting embeddings form identity-and-composition closed classes. Strict isomorphism equals *bijective* embedding and is an equivalence relation. Source dependencies: Theorem 6.5, Corollary 6.6, Proposition 6.11, Theorem 6.14. Compare map typing, base fixing, kind-indexed I, J F-linearity, independent witness reflection.

(v) **Conditional first branching:** Every **strictly non-isomorphic** pair has defined b; b symmetric under L/M reversal, cannot be 4, invariant under strict isomorphism of either argument. Source dependencies: Theorem 6.16, Corollary 6.18, Theorem 6.19. b=0 is anchored-background bookkeeping, not an eighth formation stage; b undefined for strict isomorphic pairs. Prove existence from I7 iff strict isomorphism, and invariance from stage-wise nonemptiness for full tuple sets.

## Adversarial and reproducibility obligations fixed prospectively

A. Derive all 5 source claims by **exact cross-reference** to named already audited results; check dependency graph acyclic, no unintended broadening and no unaudited premise. A synthesis theorem still needs exact dependency checks rather than blanket PASS.
B. Construct or reuse a **source-typed** nondegenerate primitive core with proper restriction, ≥1 successful and ≥1 failed configuration, global partial assignment including defined value zero and absent assignment, typed role and channel trace. Check primitive I, II, III, V; close IV/VI/VII in correct order, including empty finite composite and cancellation.
C. Countercases: same primitive core + distinct supplied T gives **distinct full expansions**, not contradiction to *relative* uniqueness. Different role input changes Stage VI; term input changes VII. Mere composite equality does not imply strict iso. Trace multiplicity doesn't create distinct channel identity. An arbitrary non-witnessed candidate channel has no term even if candidate exists.
D. Check coordinate-erasure identities for all 0≤i≤j≤k≤7, including identity and arbitrary set-coded truncation boundaries; finite model checks do not establish abstract law.
E. For maps use both full strict identity/relabel/compose **and** an example that first branching can be 6 or 7 despite definitional closure layers, and display early failures at 0,1,2,3,5 from preserved earlier fixture. Existing T6.16/T6.17/T6.19 JSON may be reused with explicit provenance; avoid relabeling reused checks as new independent experiments.
F. Test source-defined trace iff separately from channel definition in finite candidate universe, no "trace set nonempty if c ∈ U" shortcut.
G. Separate *proof claims*, finite executable examples, repository artifact execution, independent external validation and whole-paper status. Preserve T4.7 optional wording clarification. Source PDF and Zenodo remain unchanged.
H. If any genuine dependency defect appears, stop and issue PROOF_GAP/REFINEMENT rather than smoothing over or asserting all 5 automatically.

Prospective taxonomy:
- MATHEMATICAL_VERDICT = PROVED_IN_DECLARED_BACKGROUND / DISPROVED_BY_VALID_COUNTERMODEL / PROOF_GAP / INDETERMINATE.
- FPA_VERDICT = PASS / PASS_WITH_BOUNDARY / PASS_WITH_REFINEMENT / FAIL / INDETERMINATE.
- REVISION_NEED = NONE / CLARIFICATION / ASSUMPTION / PROOF / THEOREM / DEPENDENCY_REAUDIT / UNDETERMINED.

One bounded audit unit; latest next after completed T6.20 should be **P6.22** (Definition 6.21 as dependency), not an invented Theorem 6.21. F2 whole paper FPA remains OPEN unless all other groups separately audited.
