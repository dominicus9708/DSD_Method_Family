# FAS-F2-APPD-RESTRICT-001 — Prospective Appendix D audit obligations

**Source lock date:** 2026-10-21 KST. **Audit protocol:** FPA v0.1. **Status at this precommit:** NOT_EXECUTED, no verdict preassigned.

- Author/source: Kwon Dominicus, `DSD_Formation_Axiom_System_EN(5).pdf`, 33 pp., original Appendix D, printed page 32.
- Exact PDF SHA-256: `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`.
- Original Appendix D adds global `Res(H,h) and Res(h,g) => Res(H,g)`, defines `E_adm={x:Adm_expr(x)}`, states `Res|E_adm×E_adm` is a preorder with identity restrictions, and **optionally** proposes `(H|Y)|Z=H|Z` for uniquely induced subexpressions, `Z subset Y`.
- Source dependencies: Primitive Axiom II (material inclusion, exact anchor restriction, target admission, admitted-source identity; no base transitivity), Section 4.3 Lemma 4.10, Corollary 4.11, Proposition 4.12, and post-Stage-VI definitional closures.

## Prespecified independent obligations
1. D01: Transcribe exact quantifier scope. Is added transitivity global on all candidate expressions, rather than only the admitted–admitted subrelation? Check this distinction on unadmitted sources.
2. D02: Prove the restricted relation is reflexive on every admitted expression using Axiom II identity, and transitive using the *new* global clause. No antisymmetry or totality assumed.
3. D03: Independently construct a legal full primitive model where admissible identity restrictions and sound inheritance hold but `Res` fails transitivity; preserve the existing Proposition 4.12 non-implication.
4. D04: Verify `Res(H,h)`, `Res(h,g)` entail material inclusion, anchor equality and inherited relational data (Lemma 4.10), **without** deriving a primitive `Res(H,g)` in the unextended system.
5. D05: Examine the optional two-stage induced restriction identity with well-typed nested `Z⊆Y⊆mat(H)`; explicitly distinguish abstract primitive `Res` from an additional functional selection `H|Y`. Check uniqueness and existence hypotheses.
6. D06: Construct legal symmetric/mutual-restriction models demonstrating preorder need not be partial order; keep candidate identity and extensional material sameness separate.
7. D07: As an exploratory **derived observation not stated as a theorem of original Appendix D**, evaluate whether transitive closure of a typed sound restriction relation remains Axiom-II-sound, and what post-closure primitive/deduced record must be rebuilt. Keep optional work strictly subordinate.
8. D08: Execute independently specified finite fixtures (small material/anchor model, all reflexive relations on three/four admitted expression tags, nonadmitted-source scope witness, finite induced-subset two-step checks); document exhaustive fixture universe and limits precisely.
9. D09: Retain the unrelated F2 historical §7.3 D2 scope, §8 fixed-J comparison error, T4.7 wording clarification, previous Appendix C result. Do not overwrite or silently fix original PDF/Zenodo.
10. D10: Record mathematical, audit-process, revision and independent-validation verdicts independently; save actually executed code and JSON with SHA256/Git blob verification; Notion and GitHub sync only after actual results. F2 full-paper remains OPEN and 22/22 method-family internal standardization unchanged.

## Pre-results status

```text
CASE: FAS-F2-APPD-RESTRICT-001
SOURCE_PDF_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
EXECUTION_STATUS: NOT_STARTED
MATHEMATICAL_VERDICT: NOT_REVIEWED
DSD_AUDIT_VERDICT: NOT_EXECUTED
REVISION_NEED: UNDETERMINED
F2_FULL_PAPER_FPA: OPEN
INDEPENDENT_EXTERNAL_VALIDATION: not_established
METHOD_FAMILY_STANDARDIZATION: 22/22 unchanged
```
