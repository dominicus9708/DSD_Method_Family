# FAS-F2-T3.6-001 — Formation-trace characterization / source-bound proof audit

**2026-10-19 KST · FPA v0.1 · Post-standardization theorem audit · Author-project internal review, NOT external certification.**

```text
AUDIT_ID: FAS-F2-T3.6-001
OWNER_METHOD: DSD Audit
SUBJECT: Formation Axiom System F2, Definition 3.5 and Theorem 3.6, printed p.9
SOURCE_FILE: DSD_Formation_Axiom_System_EN(5).pdf (33 pages)
SOURCE_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
PRECOMMIT_COMMIT: ababf3bd42bd567b731d43d0129c1f04834822f6
PYTHON_COMMIT_FINAL: 0e66f49200766fe9f924c95a89bb2e4aa1560c7b
JSON_COMMIT_FINAL: 6a6ccd89fd38485bb0554b5c2c40797f8e3e8325
MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE
CRITICAL_PROOF_GAP_FOUND: no
FINITE_WITNESS_FIXTURES: 8/8 PASS
CANDIDATE_CHANNEL_EQUIVALENCES_CHECKED: 21
SINGLETON_COMPOSITES_CHECKED: 3
NEW_PRIMITIVE_AXIOM_NEEDED: no
F2_WHOLE_PAPER_VERDICT: not_issued
INDEPENDENT_EXTERNAL_VALIDATION: not_established
PDF_ZENODO_CHANGED: no
NEXT_CANONICAL_AUDIT: FAS-F2-T6.5-001 / NOT_STARTED
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged
```

## 1. Source/claim lock
The source is a typed static set-theoretic Formation system. A candidate channel is the five-tuple
`c=(p,a,lambda,v,rho)` in `U_L`, with channel identity independent of the expression restriction/realization witness history. For this fixed candidate Definition 3.5 defines
`Tr_L(c)={(H,h,p,a,lambda,v,rho): Res(H,h), Des_expr(h), Realize(h,p), ConfAdm(p), (a,v) in Gamma_lambda(p), Role(p,a,lambda,rho)}`.
Theorem 3.6 asserts `c in C_L iff Tr_L(c) != empty`; if true, `T_L(c)` is defined and `Comp_L({c})=T_L(c)`; if false, core `T_L` assigns no term to this candidate.

The parent quantification over H,h is typed over candidate expressions `E_B^L` as in Section 2. The claim is relative to formation-core data satisfying Axioms I,II,III,V, closure IV,VI,VII, and a supplied post-Stage-VI term map `T_L:C_L->W_L`. This is not an absolute theorem about all arbitrary partial functions or all possible external zero extensions.

## 2. Written mathematical derivation (general, not computational)
For any p, define
`W_p={(H,h) in (E_B^L)^2:Res_L(H,h) and Des_expr_L(h) and Realize_L(h,p) and ConfAdm_L(p)}`.
Define the candidate-dependent remaining condition
`A_c=[(a,v) in Gamma_{L,lambda}(p)] and Role_L(p,a,lambda,rho)`.
By Definition 2.1 and Closure Clause IV:
`W_p != empty <=> Psi_L(p) <=> Des_cfg_L(p)`.
By Definition 3.5:
`Tr_L(c) = {(H,h,p,a,lambda,v,rho): (H,h) in W_p and A_c}`.
As the last five coordinates are fixed for this c, this set is nonempty iff `W_p != empty and A_c`. This is precisely `Des_cfg_L(p) and A_c`, which by Clause VI is precisely `c in C_L`. Both directions follow with no new axiom or circular premise.

The domain of the supplied term map is *exactly* `C_L`, so `c in C_L` implies `T_L(c)` defined, while `c not in C_L` implies `T_L(c)` is not a value assigned by the **core** map. Because `{c}` is finite, Clause VII defines `Comp_L({c})=sum_{d in {c}} T_L(d)=T_L(c)`.

This derives all three assertions without using finite test outcomes. There is no assumption that a trace is unique, that its witness count is a term coefficient, or that an absent channel has a zero term.

## 3. Adversarial typed cases and reproducible finite supplement
Run:
```powershell
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_t36_formation_traces.py
```
From the repository root; output is written to the sibling `results/t36_trace_witnesses.json` directory. An optional first CLI argument overrides the output path. Python standard library only.

| Fixture | Result | Boundary exercised |
|---|---|---|
| A single sound witness | PASS | one candidate admitted, one trace |
| B two sound witnesses | PASS | two traces, same *one* operational channel |
| C no realization witness | PASS | non-admitted despite candidate tuple |
| D applicable configuration, undefined q | PASS | undefined not zero |
| E no Role | PASS | defined q alone insufficient |
| F q(a)=0 with T(c)=7 | PASS | defined zero is admitted, no forced relation between q and T |
| G empty candidate universe | PASS | empty-set boundary and vacuous implication |
| H configuration coherence blocked | PASS | failed ConfAdm blocks trace/channel |

The eight generated finite presentations each satisfy the implemented typed versions of Primitive Axioms I–III and V. Clauses IV and VI are recomputed rather than injected as preassigned outcomes. Checks: **8/8 fixture families PASS; 21 typed candidate-channel equivalences; 3 admitted singleton-composite tests.** These are finite witnesses for boundary coherence and reconstruction, NOT an exhaustive check of arbitrary models or proof-assistant certification.

Permanent artifacts:
- [Prospective precommit](FAS-F2-T3.6-001_PRECOMMIT.md)
- [Portable Python verifier](../scripts/verify_t36_formation_traces.py)
- [Deterministic JSON](../results/t36_trace_witnesses.json)

## 4. Gate/status review
- G01 source identity/version: PASS; SHA-256 matches the named attached PDF; Zenodo byte identity not established.
- G02 definitions and noncircularity: PASS; `Psi`, `Tr`, `Chan` are correctly ordered.
- G03 sorts, quantifiers, function domains: PASS; c typed in U, witness over E, T defined only on C.
- G04 primitive vs definitional clauses: PASS; no new source-level axiom inserted.
- G05 deductive soundness: PASS; witness nonemptiness and channel closure are exact Boolean equivalents.
- G06 existence/uniqueness: PASS_WITH_BOUNDARY; theorem does NOT claim unique witness.
- G07 adversarial cases: PASS within selected finite structures.
- G08 finite vs general proof: PASS; general written proof separated explicitly.
- G09 unrelated map-isomorphism claims: NOT_APPLICABLE to T3.6; no classification/injectivity claim inferred.
- G10 imported background: PASS_WITH_BOUNDARY, typed set-theoretic closure relative to source declarations.
- G11 cross-paper impact: PASS_WITH_BOUNDARY; downstream trace/channel references remain conditional on same interfaces, not separately verified.
- G12 status, no-gain, precommit, external-evaluator discipline: PASS; no result promoted to external validation.

## 5. Verdict and continuation
`PROVED_IN_DECLARED_BACKGROUND / PASS_WITH_BOUNDARY / REVISION_NEED=NONE` for the *exact* source statement. Boundary reflects the model scope, finite verifier's limitations and external independence, **not an unresolved theorem step**. No genuine source defect, additional assumption, axiom correction, mandatory proof rewrite, or new Zenodo edition is justified by this audit.

Preserve Theorem 4.7's earlier separate wording clarification obligation; this T3.6 result neither repairs nor reopens that prior finding.

Stop at this logically bounded theorem group per FPA time-out/restart rule. Next dependency-prioritized case: **Theorem 6.5, identities and composition of forward formation maps/embeddings** (FAS-F2-T6.5-001), not started. The rest of the F2 full manuscript remains NOT_REVIEWED or individually historical-reviewed as already recorded.
