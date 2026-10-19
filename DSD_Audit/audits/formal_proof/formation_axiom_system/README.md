# Formation Axiom System — F2 / FPA audit case

**CASE_STATUS:** IN_PROGRESS_THEOREMS_3_3_4_5_4_7_COMPLETED  
**DATE:** 2026-10-19  
**SUBJECT_CLASS:** FOUNDATIONAL_THEORY  
**OWNER_METHOD:** DSD Audit  
**PROTOCOL:** [FPA v0.1](../../../protocols/mathematics/FORMAL_PROOF_AUDIT_v0.1.md)  
**MATHEMATICAL_STANDARD:** ordinary mathematics, typed set-theoretic reasoning with declared ZFC-relative scope  
**INDEPENDENT_VALIDATION:** not established  

Files:
- [SOURCE_LOCK.md](SOURCE_LOCK.md) — identified attached PDF edition, 33 pages, SHA-256; Zenodo byte identity explicitly unverified.
- [PROOF_OBLIGATIONS.md](PROOF_OBLIGATIONS.md) — Section 2–7 claim register; three theorem-level audits completed, remaining claims NOT_REVIEWED.
- [EXECUTION_PLAN.md](EXECUTION_PLAN.md) — first action Theorem 3.3; resumable checkpoint and downstream impact.
- [Shared theorem-audit template](../../../templates/FORMAL_PROOF_AUDIT_TEMPLATE.md).

The first theorem-level FPA audit completed: [Theorem 3.3 precommit](THEOREM_AUDITS/FAS-F2-T3.3-001_PRECOMMIT.md) and [Theorem 3.3 result](THEOREM_AUDITS/FAS-F2-T3.3-001_RESULT.md): relative unique closure, mathematical `PROVED_IN_DECLARED_BACKGROUND`, FPA `PASS_WITH_BOUNDARY`, no mandatory revision. This is an internal source-bound review, not independent validation or the full-paper F2 verdict.

Do NOT pre-populate `THEOREM_AUDITS/` with invented pass results. Create a theorem audit file when that theorem's audit actually begins. Preserve old source and audit history; this case does not alter the Formation original or re-open 22/22 internal method-family completion.

NOTION FPA hub: https://app.notion.com/p/3fe81f51e7fa81afb612fa69387cdeee
NOTION Formation case: https://app.notion.com/p/3fe81f51e7fa811a9645d2c684661296

NOTION completed T3.3 audit: https://app.notion.com/p/3fe81f51e7fa815698c1df6ab625ad8c
LATEST: [Theorem 4.5 precommit](THEOREM_AUDITS/FAS-F2-T4.5-001_PRECOMMIT.md), [proof audit result](THEOREM_AUDITS/FAS-F2-T4.5-001_RESULT.md), [finite verifier](scripts/verify_t45_countermodels.py) and [deterministic output](results/t45_axiom_independence.json). MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND; FPA: PASS_WITH_BOUNDARY; no mandatory manuscript change. NOTION: https://app.notion.com/p/3fe81f51e7fa811eb18ff1e5428d7fb2
NEXT: FAS-F2-SEC4.3-001 — Section 4.3 consequences, NOT_STARTED. All other F2 obligations remain open.

LATEST FPA AUDIT: [Theorem 4.7 precommit](THEOREM_AUDITS/FAS-F2-T4.7-001_PRECOMMIT.md) and [Theorem 4.7 result](THEOREM_AUDITS/FAS-F2-T4.7-001_RESULT.md). Six residual clauses each have a counterinterpretation satisfying the other five: `PROVED_IN_DECLARED_BACKGROUND` under **residualized** premises, FPA `PASS_WITH_REFINEMENT`, `REVISION_NEED=CLARIFICATION`. Manuscript "other primitive axioms" needs precise rewording; it cannot include the omitted clause's parent axiom unaltered. [Python](scripts/verify_t47_residual_clauses.py) · [JSON](results/t47_residual_clauses.json). [Notion T4.7 audit](https://app.notion.com/p/3fe81f51e7fa8182ac05f470ddc5c0d9).
