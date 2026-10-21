# FAS-F2-C6.26-001 — Prospective source-bound proof audit: Channel-cardinality obstruction

Date: 2026-10-20 KST. Owner: established DSD Audit / Formal Proof Audit v0.1.
Previous checkpoint: C6.25 reviewed, C6.26 **NOT_REVIEWED before this precommit**.

## Source lock and exact claim

- Primary source: Kwon Dominicus, uploaded 33-page `DSD_Formation_Axiom_System_EN(5).pdf`.
- SHA-256: `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`.
- Exact original location: §6.5, printed page **24**, `Corollary 6.26 (Channel-cardinality obstruction)`.
- Original statement: **If `|C_L| ≠ |C_M|`, then no strict base-fixed formation isomorphism exists.**
- Dependencies: Definition 6.10 E1–E9 and induced admitted-channel map; **Corollary 6.12** establishes a bijection of admitted channels under every strict base-fixed formation isomorphism. Definitional Closure Clause VI identifies the actual `C`; Clause VII defines `T`, `Dcomp=P_fin(C)`, `Comp`.

## Frozen prospective audit plan

1. Prove general implication by contradiction: strict isomorphism induces a bijection `hatPhi_C:C_L→C_M` (source Corollary 6.12), contradicting unequal **set cardinalities**, with no finiteness assumption in the theorem.
2. Distinguish the necessary implication from its converse. Equal channel cardinality **does not** suffice for strict equivalence (e.g. different roles/assignment graph or T). Unequal channel cardinality does **not** identify the first branching index `b`, nor a unique failed primitive preservation clause; do not assert automatically `b=6`.
3. Construct two explicit **full** source Formation models over the same fixed base and same scalar field, with all primitive I/II/III/V and definitional IV/VI/VII: one material a, expression h, configuration p, quantity kind lambda, role carrier `{r,s}` in both. Defined zero q_lambda(a)=0, a true restriction/realization witness, both anchors equal. Set `Role_L={(p,a,lambda,r)}` and `Role_M={(p,a,lambda,r),(p,a,lambda,s)}`. Full derived C sizes 1 vs 2 although primitive CANDIDATE CARRIER sizes and role labels match, so candidate bijections are **nonempty**.
4. Choose separately supplied `W_L=W_M=F2` and total `T(c)=0` for admitted c, to show equal all-family aggregate `0` is compatible with channel-cardinality mismatch. Check trace equivalence on 4 total candidate-channel tuples, with nonadmitted candidates having no assigned T.
5. Enumerate all two role-label bijections; they satisfy E1–E7, fail E8, and **cannot induce admitted-channel bijections**. Clarify the corollary's proof uses *derived cardinality*, not need to diagnose a particular E8 clause (although this witness happens to fail E8).
6. Test empty C vs singleton C with identical ambient carrier sizes and valid primitive model data (role relation empty), preserving the empty-family composition `0`; empty `C` is allowed by Clause VI.
7. Positive control: identical source and target `L`, channel count 1 vs 1 and an actual strict identity isomorphism. Distinct equal-count countercontrol: same all carriers, one active role and channel each, but a different fixed `T` value `0` vs `1`; because `J=id_F2` is the unique F2-linear iso of one-dimensional W, E9 fails on each E8-compatible tuple. Thus equal |C| alone cannot establish strict equivalence.
8. Mathematical term-space caveat: source Corollary 6.26 applies to arbitrary set-sized (possibly infinite) `C`; finite Python enumerates only small legal examples. No assumption of ZFC cardinal comparability beyond bijection equals-cardinality.
9. Precommit before tests; write and execute **identical** standard-library Python source in current container, push same source into canonical repo script folder and compare Git blob SHA, save exact JSON under existing sibling results. Separate mathematical proof from finite checks and externally independent validation.
10. Track existing method-family 22/22 status unchanged, earlier T4.7 optional wording issue, full F2 whole-manuscript FPA OPEN and unchanged original PDF/Zenodo. Do not promote Section 7, next `FAS-F2-T7.1-001` remains NOT_STARTED until separately precommitted.

Veridct taxonomy frozen: MATHEMATICAL_VERDICT = PROVED_IN_DECLARED_BACKGROUND|DISPROVED_BY_VALID_COUNTERMODEL|PROOF_GAP|INDETERMINATE; FPA_VERDICT = PASS|PASS_WITH_BOUNDARY|PASS_WITH_REFINEMENT|FAIL|INDETERMINATE; REVISION_NEED = NONE|CLARIFICATION|ASSUMPTION|PROOF|THEOREM|DEPENDENCY_REAUDIT|UNDETERMINED.

Next bounded case after C6.26: **`FAS-F2-T7.1-001` — Theorem 7.1 (Existence of a full formation model)**, NOT_STARTED.
