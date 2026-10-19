# FAS-F2-T6.16-001 — prospective first-branching obstruction audit

Date: 2026-10-19 KST. Formal Proof Audit v0.1, existing DSD Audit method.
Source: Kwon Dominicus, `DSD_Formation_Axiom_System_EN(5).pdf` (33 pages), SHA-256 `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`.
Source locus: §6.4 Definition 6.15 and Theorem 6.16, PDF printed pages 20–21 (source attachment, not asserted byte-identical to Zenodo).
Previous state: Theorem 6.14 PROVED_IN_DECLARED_BACKGROUND, T6.16 NOT_STARTED.

## Locked exact claims
1. For every 0≤k<7, I_(k+1)(L,M) subset I_k(L,M), each defined using the **same** ambient collection of full comparison tuples with bijective carrier/kind/role/zero-pointed value maps and arbitrary J before Stage 7.
2. I_7(L,M)≠∅ iff Σ_L ≅^fix_B Σ_M, with fixed (B,F) full formation descriptors.
3. When I_7=∅, b(L,M):=min{k∈{0,...,7}:I_k=∅} exists, and its definition implies strict nonequivalence; if b>0, every earlier I_j for j<b is nonempty. This is the **earliest collective failure of all candidate full tuples**, not the earliest failed clause in a single map.
4. Stage 0 is anchored-background comparison / ambient typing, NOT an eighth formation stage.
5. Document the stage assignments exactly: I0 E1; I1 E2; I2 E3 restriction; I3 E3 realization + E4 primitive configuration predicates; I4 describability and K_des; I5 E5-E7; I6 E8; I7 J F-linear isomorphism and E9.

## Predeclared mathematical attacks
- General set-inclusion by conjunction and well-founded minimum on finite {0,...,7}, including I0 empty, I7 nonempty, b=7 cases.
- Inspect whether ambient J arbitrary (not necessarily linear/surjective) before I7 makes nonemptiness of earlier stages ill-defined. Check existence/typing of a set map W_L→W_M even for zero-dimensional spaces.
- Derive iff from exact E1–E9 inventory, including E4 configuration closure and E7 negligible threshold, without adding premise.
- Guard against accidental equality I3=I4 being inferred from *this* theorem (it is separately Theorem 6.17, to remain unaudited here).
- Exhaustive selected finite tuple enumerator: keep ambient fixed per example; filter all tuples through S1–S8 and verify nestedness, failure index at 0,1,2,3,5,6,7 where legal; demonstrate b=4 cannot occur only if Theorem 6.17 separately justified, else leave it outside T6.16's verdict.
- Adversarial fake counterexample: choose a bad map at early stage while another map survives; that does not make I_k empty.
- Source or fixture defects must be recorded as found, not post hoc dropped. Finite computer test does not prove universal theorem.
- Release only scoped verdict; no original PDF/Zenodo modifications without separate request; historical T4.7 wording clarification remains independent.

MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND | DISPROVED_BY_VALID_COUNTERMODEL | PROOF_GAP | INDETERMINATE.
DSD_AUDIT_VERDICT: PASS | PASS_WITH_BOUNDARY | PASS_WITH_REFINEMENT | FAIL | INDETERMINATE.
REVISION_NEED: NONE | CLARIFICATION | ASSUMPTION | PROOF | THEOREM | DEPENDENCY_REAUDIT | UNDETERMINED.
