# PA-P15-20260901-C1-COUNTERMODEL-SEMANTICS-001 — prospective targeted non-edit metatheory check

**Not executed at precommit**. Scheduled audit record 2026-10-24 KST.
Original author Kwon Dominicus; exact 2026.09.01 general Property PDF `DSD_Property_Axiom_System_EN(4).pdf`, 23 pp, SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.
Triggered by [P14 independent obligation matrix](P14_NONEDIT_PROOF_OBLIGATION_MATRIX_RESULT.md), which confirmed the two printed Section-6 issues and newly sharpened a **proof-scope** question in Theorem 4.3 “relative to C1”. Neither PI/PII independence over typing nor consistency of *full admitted cores* was disproved.

## Frozen obligations for P15

1. Explicitly formalize two interpretations of C1: (i) **functional single-valued, exclusive status** of Def3.3 restricted to admitted cores satisfying both PI and PII; (ii) C1's raw defining equations viewed as **possibly overlapping status predicates on all typed premodels**. Do not conflate these semantics.
2. Re-evaluate both Countermodels 4.1 and 4.2 under each interpretation. E.g. CM4.1 has `x∉Ap` AND `x∈DomXi`, and CM4.2 has `x∈Ap\DepSat` AND `x∈DomXi`. Under a status-partition reading this is overlapping labels; under Boolean-predicate reading it is allowed but not a full admitted status.
3. Determine whether Theorem 4.3's “relative to shared typed background and Definitional Closure Clause C1” can be made formally meaningful as independence of **primitive axioms over a conservative definitional expansion** of premodels without invoking the primitive axioms circularly.
4. Construct a clear derivation or counterinterpretation under each semantics; determine precise printed-paper status: valid typed-background independence, possible C1-relative independence with explicit extension, or actually false under literal full-core-only C1 domain.
5. Inspect impact on Def3.3's unique status assignment, Theorem3.7 completion/reduction, and Main Theorem11.1(3); identify where language should be changed in a later version **without editing now**.
6. Independently determine whether other primitive-core theorems (C1 unique completion, state partition, nonconverse) rely on this premodeled interpretation; do not falsely downgrade full-core results because invalid premodels overlap.
7. Optional tiny Python truth table is only auxiliary to logic, not a universal theorem: if needed, commit script and outputs in the exact established versioned `scripts/`, `results/` paths and require CI execution; no changes to original experiment Python.
8. Record P15 in GitHub and Notion and keep actual author PDF/LaTeX/Zenodo unchanged. Preserve all countermodels and failures, no forced “success means absorb / failure means discard” branch closure.

```text
CASE: PA-P15-20260901-C1-COUNTERMODEL-SEMANTICS-001
STATUS: NOT_EXECUTED / PRECOMMITTED
P14: COMPLETED
§6_PRINTED_CONDITION_GAPS: 2 OPEN
THEOREM_4_3_C1_RELATIVE_SCOPE: OPEN
FULL_PROPERTY_FPA: OPEN
```
