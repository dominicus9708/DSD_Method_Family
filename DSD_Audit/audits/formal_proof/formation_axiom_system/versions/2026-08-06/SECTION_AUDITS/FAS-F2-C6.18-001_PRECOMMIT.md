# FAS-F2-C6.18-001 — Prospective Formal Proof Audit precommit

- Date: 2026-10-19 KST.
- Parent: DSD Audit / FPA v0.1, no new method slot.
- Fixed source: Kwon Dominicus, `DSD_Formation_Axiom_System_EN(5).pdf`, 33-page supplied attachment, SHA-256 `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`.
- Exact source location: §6.4 **Corollary 6.18 (Closure-stage exclusion)** on source printed p.22 (PDF page around 23); dependency Definition 6.15 (stage-comparison sets and first branching index), Theorem 6.16, Theorem 6.17(ii).
- Precommit initial status: **NOT_REVIEWED**; prior T6.17 result already reviewed, general `I_3(L,M)=I_4(L,M)` was proved relative to declared background.
- **Frozen exact corollary claim:** Whenever first branching index `b(L,M)` is defined, `b(L,M)≠4`. A failure at Stage 4 is already a failure at Stage 3; configuration describability cannot be the first independent branching source after all Stage 3 data are preserved/reflected.

## Prospective proof obligations

1. Read and type-check exact definition `b=min{k∈{0,...,7}:I_k=∅}` **only when** `I_7=∅`. Distinguish undefined `b` (strict isomorphic) from a numerical branching result.
2. Deduce `b≠4` by contradiction: `b=4` forces `I_4=∅` and `I_3≠∅` through first-minimum definition; `I_3=I_4` makes this impossible. Alternatively, exact emptiness profiles suffice.
3. Audit dependence on **same ambient full comparison tuple collection**, fixed pair (B,F), full formation descriptors and all Stage3 primitive preservation/reflection obligations. Do not infer the result merely from stage-wise inclusion; strict nestedness alone allows b=4.
4. Adversarial: choose a general nested chain with `I_3≠∅`, `I_4=∅` to demonstrate why Theorem 6.17's stronger equality is indispensable; this abstract chain is not a valid full-Formation-stage model satisfying source hypotheses.
5. Boundary: check `I_0=∅` (b=0), `I_3=I_4=∅` (first ≤3), `I_3=I_4≠∅` with later failure (b=5,6,7), all nonempty (b undefined). A finitary powerset/exhaustive profile check cannot substitute the general argument.
6. Reuse the previously audited T6.16/T6.17 dependencies and finite witnesses only with provenance; write a new deterministic finite profile and hostile nested-only countercase script under existing F2 scripts folder, plus JSON. No edits to frozen English PDF or Zenodo.
7. Independent external evaluator and full-paper F2 statuses stay separate. Preserve historical T4.7 wording-clarification recommendation.

## Verdict categories locked in advance
`MATHEMATICAL_VERDICT = PROVED_IN_DECLARED_BACKGROUND | DISPROVED_BY_VALID_COUNTERMODEL | PROOF_GAP | INDETERMINATE`
`DSD_AUDIT_VERDICT = PASS | PASS_WITH_BOUNDARY | PASS_WITH_REFINEMENT | FAIL | INDETERMINATE`
`REVISION_NEED = NONE | CLARIFICATION | ASSUMPTION | PROOF | THEOREM | DEPENDENCY_REAUDIT | UNDETERMINED`

Next case after bounded closure: **Theorem 6.19 (symmetry and strict-isomorphism invariance of first branching)** `FAS-F2-T6.19-001` / NOT_STARTED.
