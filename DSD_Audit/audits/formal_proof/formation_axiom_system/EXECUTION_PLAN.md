# Formation F2 — execution plan and checkpoints
Status: IN_PROGRESS — Theorems 3.3 and 4.5 internally audited; full Formation F2 not complete. Date: 2026-10-19.

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
Current FPA execution status: NOT_STARTED; no false PASS count.
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
- **STOP.** Next bounded unit: `FAS-F2-T4.7-001`, the six residual clauses after Proposition 4.6, NOT_STARTED. Create a new prospective precommit before review. Keep Theorem 4.7 separate from Theorem 4.5; no paper-wide F2 verdict or Zenodo change.
