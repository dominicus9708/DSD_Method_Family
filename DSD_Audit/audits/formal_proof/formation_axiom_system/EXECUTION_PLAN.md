# Formation F2 — execution plan and checkpoints
Status: PREPARED_FOR_EXECUTION (not a completed proof audit). Date: 2026-10-19.

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
