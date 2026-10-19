# FAS-F2-P6.22-001 — Precommitted audit for Definition 6.21 / Proposition 6.22

Date: 2026-10-20 KST. Existing DSD Audit / Formal Proof Audit v0.1. Prior checkpoint T6.20 complete; P6.22 **NOT_STARTED** before this precommit.

**Frozen exact source:** Kwon Dominicus, attached `DSD_Formation_Axiom_System_EN(5).pdf`, 33 pages, SHA-256 `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`, §6.5 p.23 **Definition 6.21 (Composite-level coincidence relative to a fixed map)** and **Proposition 6.22 (Composite-level coincidence does not imply strict formation equivalence)**. Original PDF/Zenodo not to be changed.

## Source-locked exact obligations

1. Definition 6.21: **prescribe** an F-linear *isomorphism* J:W_L→W_M **independently of the families selected**. Two **nonempty** finite admitted-channel families F_L∈Dcomp_L\{∅}, F_M∈Dcomp_M\{∅} are J-composite-level coincident iff J(Comp_L(F_L))=Comp_M(F_M).
2. Definition 6.21's *under strict non-equivalence* is the conjunction of nonexistence of strict base-fixed formation isomorphism and existence of those nonempty composite-coincident families. Do not invert its quantifier order by choosing J after seeing outputs.
3. Proposition 6.22: construct **two full formation models over the same base and scalar field**, not merely vectors or channel-count abstractions. The source example says same single describable p, assigned item a and value, L has one admitted role/channel c0 with T_L(c0)=0, M two admitted roles/channels d+,d− with T_M(d+)=1, T_M(d−)=-1. W_L=W_M=R and prechosen J=id_R. Families are F_L={c0}, F_M={d+,d−}. Assert both nonempty and sums zero.
4. Verify full typing and **all four primitive axioms I/II/III/V**, source-bound same external B, material support/anchor equality, expression admission/describability, identity Res, Realize, Admcfg/LC/BC, regime-global assignment with q(a)=0, V_lambda pointed zero, negligible-status legal, typed roles. Construct IV/VI/VII *definitionally*; no arbitrary Chan/Comp outputs.
5. Verify |R_L|=1 vs |R_M|=2 and |C_L|=1 vs |C_M|=2, making strict isomorphism impossible by Definition 6.10 / Corollary 6.12 (both typed role and channel bijection). Cardinality mismatch, not merely unequal family cardinality, proves non-equivalence.
6. Check trace witness iff for all source candidates, show defined assigned value zero does **not** force T=0; T freely supplied on admitted channels. Include empty composite as auxiliary but do not mistakenly use empty families to satisfy Definition 6.21.
7. Adversarial safeguards: equality of sums alone is insufficient to force any channel matching; the two compared families need **not** correspond under induced channel bijection; J must be a pre-fixed **linear isomorphism**, not arbitrary nonlinear/zero function. Consider whether a weaker example with equal role counts/zero sums would be invalid evidence and distinguish minimal source witness from stronger claims.
8. Finite reproducible Python using exact rational/int terms as a *selected subset* of R; explain computational finite check does NOT certify whole real vector space and the general existence proof is the mathematical full-model construction. Execute source-aligned checks locally, then commit script and results in existing repo aligned paths, not an invented storage convention.
9. Record mathematical verdict, audit verdict, revision needed, proof dependency, failure modes, source edition, external validation, full-paper OPEN and historical T4.7 wording clarification. Do not promote T6.23 or C6.24–6.26 without independent audit.

Locked taxonomy: MATHEMATICAL_VERDICT = PROVED_IN_DECLARED_BACKGROUND | DISPROVED_BY_VALID_COUNTERMODEL | PROOF_GAP | INDETERMINATE; DSD_AUDIT_VERDICT = PASS | PASS_WITH_BOUNDARY | PASS_WITH_REFINEMENT | FAIL | INDETERMINATE; REVISION_NEED = NONE | CLARIFICATION | ASSUMPTION | PROOF | THEOREM | DEPENDENCY_REAUDIT | UNDETERMINED.

**NEXT after this bounded case:** `FAS-F2-T6.23-001` / NOT_STARTED; no claim that 6.21 is a theorem.
