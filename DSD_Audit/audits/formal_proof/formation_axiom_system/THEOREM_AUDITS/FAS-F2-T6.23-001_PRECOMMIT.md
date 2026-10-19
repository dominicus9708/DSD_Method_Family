# FAS-F2-T6.23-001 — Prospective formal proof audit

**Date:** 2026-10-20 KST · **Parent:** existing DSD Audit / FPA v0.1 · **Case status before precommit:** NOT_STARTED.

**Locked primary source:** Kwon Dominicus, supplied 33-page `DSD_Formation_Axiom_System_EN(5).pdf`, SHA256 `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`; §6.5 **Theorem 6.23 (Layerwise obstruction to strict formation equivalence)**, printed pp.23–24. Prerequisite Definition 6.10 E1–E9; optional comparison with Definition 6.15 and Theorem 6.16 for scope only. Do not assume source equality to Zenodo public bytes.

## Frozen exact claim

Let `Cand(L,M)` be the collection of **typed candidate bijections AND F-linear term-space ISOMORPHISMS** required by Definition 6.10, with fixed base `(B,F)` and both **full** formation descriptors. If

```text
forall Phi in Cand(L,M), exists i in {1,...,9}: not E_i(Phi),
```

then `Sigma_L` and `Sigma_M` are **not** strictly base-fixed formation-isomorphic.

## Predeclared independent mathematical checks

1. Write Definition 6.10 without omission:
   `strict(L,M) ⇔ exists Phi in Cand(L,M): forall i∈{1,...,9} E_i(Phi)`.
   Show that the theorem follows by quantifier negation/De Morgan, without treating it as a new independent structural axiom.
2. Recheck precise `Cand` typing: carrier/expression/configuration, kind/role and kind-indexed pointed-value bijections fix zero; J must **already** be an F-linear isomorphism. **Contrast** with Definition 6.15 ambient full comparison tuples, whose J is arbitrary until Stage 7; do NOT silently conflate.
3. Verify logical scope of (E1)–(E9) and guard (E9)'s induced-channel map dependence on (E1)–(E8). A candidate failing an earlier Ei suffices, without requiring a well-defined admitted-channel bijection for a failed candidate.
4. Preserve exact quantifier order. The claim `∀Phi ∃i ¬E_i(Phi)` is **not** `∃i ∀Phi ¬E_i(Phi)`; a pair may have distributed candidate failures, without one uniform failed clause. Do not infer a stage index b or minimal obstruction from the theorem alone.
5. **Empty Cand boundary:** if any typed carrier or term-space cannot have bijection/isomorphism, Cand is empty and the universal antecedent holds vacuously. Such failure is genuine strict nonequivalence but is NOT evidence that some particular Ei failed on a concrete candidate.
6. **Nonempty Cand countermodel to strict existence:** construct complete source-typed formation regimes with identical role carriers but different Role relations, or identical Role relation but different supplied component term T, over a fixed base and field. Enumerate all candidate *linear isomorphism* tuples; all fail E8 or E9 respectively. Ensure primitive I/II/III/V and derived IV/VI/VII fully satisfied, including value=0 defined and T independent of assignment.
7. **Positive control:** a strictly isomorphic pair may have some failing candidate tuples but at least one satisfying all E1–E9, making the theorem antecedent false. Prevent the invalid inference `exists bad candidate ⇒ nonequivalence`.
8. **Quantifier-swap hostile example:** finite abstract candidate truth table with distinct failed Ei in separate tuples; explicitly mark as a logical model of the quantifiers, not a Formation full model unless separately constructed.
9. **Weak map hostile cases:** distinguish an arbitrary function, injective non-surjective embedding, numerical composite equality, and typed candidate strict map. Neither partial structural similarity nor equal finite sums is a substitute for the quantified source claim.
10. Execute a deterministic standard-library Python verifier in existing `DSD_Audit/audits/formal_proof/formation_axiom_system/scripts`; emit JSON in sibling `results`. Verify exact same code locally where possible before GitHub commit; do not describe finite instances as general proof or external peer validation.
11. Check dependency/claim-scope and leave Corollaries 6.24, 6.25, 6.26 individually NOT_REVIEWED, unless each receives separate FPA. Preserve earlier Theorem 4.7 nonurgent wording clarification, do not edit source PDF/Zenodo.

## Locked verdict categories

MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND | DISPROVED_BY_VALID_COUNTERMODEL | PROOF_GAP | INDETERMINATE.

DSD_AUDIT_VERDICT: PASS | PASS_WITH_BOUNDARY | PASS_WITH_REFINEMENT | FAIL | INDETERMINATE.

REVISION_NEED: NONE | CLARIFICATION | ASSUMPTION | PROOF | THEOREM | DEPENDENCY_REAUDIT | UNDETERMINED.

A prospective precommit precedes substantial finite/adversarial tests. One theorem audited per session; next proposed case: `FAS-F2-C6.24-001` / NOT_STARTED.
