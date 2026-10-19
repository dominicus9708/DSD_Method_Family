# Formation F2 — execution plan and checkpoints
Status: IN_PROGRESS — three named theorem audits plus seven source items of Section 4.3 internally audited; whole Formation F2 remains not complete. Date: 2026-10-19.

## Initial work unit FAS-F2-T3.3-001
1. Lock Theorem 3.3 exact statement and its proof in the supplied 33-page source (Section 3, PDF page 8; page number must be verified against the source artifact).
2. Extract Definition 2.2, primitive signature, Clause IV, Clause VI, Clause VII and all standing conventions that it uses.
3. Build an explicit dependency DAG: primitive typed input → Ψ and configuration status → assignment graph and channel universe → admitted channel set → supplied W,T → finite composite.
4. Verify two directions separately: (a) existence and uniqueness of relative closure after W,T supply; (b) primitive reduct of any full model satisfies each primitive axiom.
5. Attack with allowed boundary cases, including empty channel set, multiple witness histories, arbitrary component terms and alternative supplied W,T. Do not treat changing W,T as nonuniqueness *under the same supplied data*.
6. Register exact proof-step evidence and output mathematical verdict, audit verdict, revision need separately.
7. Trace dependents: Theorem 3.6, Theorem 4.5, Theorem 6.17, Theorem 6.20, and later use in Property/Static/Dynamics; actual dependency claims must be verified while executing.
8. STOP and report checkpoint before starting 4.5. If unresolved, preserve open obligation and source text unchanged.

## Next blocks after T3.3
- FAS-F2-T4.5-001: primitive-axiom independence and validity of Countermodels 4.1–4.4.
- FAS-F2-T4.7-001: residual clausewise independence (the six sub-claims separately).
- FAS-F2-T6.17-001: I3=I4 and comparison-equivariant closure, scrutinizing 6.16/6.19/6.20 dependencies.
- FAS-F2-T7.3-001: arbitrary finite anchored-data realization, source-supplied scope.
- Remaining items per PROOF_OBLIGATIONS.md, including complete coverage and dependency closure before any paper-level F2 verdict.

## Evidence separation
Manuscript proven claims: author statements not FPA-verified yet.
Old Notion 2026-09-10 internal status: PASS-CONDITIONAL, historical.
Formation companion code: finite witness/regression only; general manuscript theorems not automatically formally certified.
Historical preparation status before FPA began: NOT_STARTED; current 2026-10-19 checkpoint: three theorem audits completed, no paper-wide PASS.
Publication policy: record incremental audits only in method-family GitHub/Notion, link the manuscript repo; Zenodo version only upon justified material correction or substantive release, with prompt public correction for material errors.

## Checkpoint reached — 2026-10-19 (do not skip)
- Completed `FAS-F2-T3.3-001` with prospective precommit commit `033fb2159d05635f27059bed6e04c3ad4593f55c` and [theorem audit result](THEOREM_AUDITS/FAS-F2-T3.3-001_RESULT.md) commit `4c6ff68061b530db1ff75e62f543dc29f100d429`.
- MATHEMATICAL_VERDICT: `PROVED_IN_DECLARED_BACKGROUND` (**only** Theorem 3.3); FPA process `PASS_WITH_BOUNDARY`.
- Relative uniqueness is restricted to **same** supplied `W_L,T_L`; primitive-core expansion has a zero-F-vector-space witness; no mandatory manuscript correction.
- Notion audit: https://app.notion.com/p/3fe81f51e7fa815698c1df6ab625ad8c
- That next work unit `FAS-F2-T4.5-001` has now been executed and checkpointed on 2026-10-19; its precommit and result are linked below. No historical verdict was overwritten.
- All other F2 propositions and the paper-wide claim remain OPEN/NOT_REVIEWED. No Zenodo changes.

## Checkpoint reached — FAS-F2-T4.5-001 (2026-10-19)
- Prospective precommit: `4d7ed1e6a16c01f0bc2a4d17fc5d3bc1a0472f45` / blob `89993ec145be104eace74049098a94c9b5e0abe1`.
- [Theorem 4.5 audit result](THEOREM_AUDITS/FAS-F2-T4.5-001_RESULT.md) commit `5ef5ec99cec050e6b432bb5b6aec41722382a316`: mathematical `PROVED_IN_DECLARED_BACKGROUND`; FPA `PASS_WITH_BOUNDARY`; no required revision.
- [Python finite verifier](scripts/verify_t45_countermodels.py) and [deterministic JSON](results/t45_axiom_independence.json): 4/4 source-listed nonvacuous counterinterpretations reproduce the four distinct axiom-failure cases; project-internal not external replication.
- [Notion Theorem 4.5 audit](https://app.notion.com/p/3fe81f51e7fa811eb18ff1e5428d7fb2).
- Theorem 4.7 was executed and recorded in the next checkpoint; retain this older step as historical instruction. No paper-wide F2 verdict or Zenodo change.

## Checkpoint — FAS-F2-T4.7-001 (2026-10-19)
- Prospectively locked [Theorem 4.7 challenge protocol](THEOREM_AUDITS/FAS-F2-T4.7-001_PRECOMMIT.md), commit `ce1c6e303ebdd9148c80dc08127ed946100bd3e4` / blob `dea17056afe9bd40db6aced2ec14ec5d57a76119`.
- [Formal mathematical audit](THEOREM_AUDITS/FAS-F2-T4.7-001_RESULT.md), commit `fa032fa64b42ec13ae70cc57a72257ba99f24b09`: six residual clause non-entailments established via six explicit finite typed interpretations; `MATHEMATICAL_VERDICT=PROVED_IN_DECLARED_BACKGROUND` for **residualized six-clause theory**. `DSD_AUDIT_VERDICT=PASS_WITH_REFINEMENT`, `REVISION_NEED=CLARIFICATION`.
- Exact wording concern: Theorem 4.7's “other primitive axioms” cannot retain its **whole containing parent axiom** while falsifying one clause. Source should say “other five residual constraints” and separately note unaffected whole axioms; do not silently alter source.
- [Finite reproduction Python](scripts/verify_t47_residual_clauses.py) / [deterministic JSON](results/t47_residual_clauses.json); non-independent bounded evidence. Local same-fixture implementation executed 6/6.
- [Notion theorem record](https://app.notion.com/p/3fe81f51e7fa8182ac05f470ddc5c0d9).
- **HISTORICAL STOP before §4.3:** `FAS-F2-SEC4.3-001` was then NOT_STARTED; it has now been executed, see newest checkpoint below.
- No paper/Zenodo modification; no manuscript-wide F2 verdict; 22/22 method-family internal-standardization unchanged.


## Checkpoint — FAS-F2-SEC4.3-001 (2026-10-19)
- [Prospective precommit](SECTION_AUDITS/FAS-F2-SEC4.3-001_PRECOMMIT.md) commit `dae15972d8cb3d800bdef4a9f3bcc7d4acfe97b8`.
- [Seven-item §4.3 mathematical audit](SECTION_AUDITS/FAS-F2-SEC4.3-001_RESULT.md) commit `2a03260813f27829762ba5375e93aa5a7b2494df`: Cor.4.8, Countermodel4.9, Lemma4.10, Cor.4.11, Prop.4.12, Lemma4.13, Cor.4.14. `MATHEMATICAL_VERDICT=PROVED_IN_DECLARED_BACKGROUND` for these scoped claims; FPA `PASS_WITH_BOUNDARY`, optional 4.9 explanatory clarification.
- [Executed same-project finite checker](scripts/verify_sec43.py), commit `23aac767ca055965c89f50cb781e46ad6e540c38`, and [JSON](results/sec43_witnesses.json). Two explicit finite witness constructions (4.9 admissible but not describable; 4.12 nontransitive relation with nonempty admitted-channel kernel).
- [Notion §4.3 result](https://app.notion.com/p/3fe81f51e7fa81c88b4dfc5f7e936d7d).
- No actual original manuscript or Zenodo changes; Theorem 4.7's previous `PASS_WITH_REFINEMENT` remains a separate advisory.
- **STOP.** Next proposed bounded audit `FAS-F2-G0-001`: Section 2 typed signatures, set/class status, primitive/derived boundaries and Proposition 2.5. Prospectively precommit before any verdict. Alternatively execute outstanding Theorem 3.6 after dependency audit. Neither has started. No overall F2 PASS.
