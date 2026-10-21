# FAS-F2-G4-CLAIM-INVENTORY-001 — prospective original-source claim inventory and audit-coverage reconciliation

Date: 2026-10-21 KST. **Precommit status: NOT_EXECUTED.** This is a meta-audit of inventory/traceability, not a new proof of the source claims; no full-F2 judgment is assigned in advance.

## Immutable source
- Kwon Dominicus, `DSD_Formation_Axiom_System_EN(5).pdf`; 33 pages; SHA256 `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`.
- Scan numbered, heading-anchored source labels in the body of the PDF only: `Definition`, `Theorem`, `Proposition`, `Corollary`, `Lemma`, `Countermodel`, `Remark`, each with `section.number`. Do not count citations to a label or bibliography as a new source item, or treat unnumbered appendix headings as numbered theorem labels.
- Crosswalk with verified GitHub FPA standalone `THEOREM_AUDITS/*_RESULT.md` and grouped `SECTION_AUDITS/*_RESULT.md`. Record precommits and executable evidence separately; appendix/section audits may audit scope but do not implicitly prove every nearby source statement.

## Frozen audit obligations
1. I01: exact source SHA, reproducible text extraction (PDF text vs layout), source-title/number/kind/order uniqueness and span boundaries; report source statements from PDF rather than inventing.
2. I02: census **by claim kind and section**, including definitions, remarks, countermodels, and lemmas, not just 14 numbered theorems.
3. I03: actual executed result-file inventory in both directories. Do not equate 42 files with 42 independent claims; `PRECOMMIT` and `RESULT` are one case, and group cases contain multiple labels.
4. I04: build one row per original source label with exact `label/kind/heading/source page` plus explicit evidence path(s), role `standalone` / `grouped-explicit` / `dependent-context` / `unverified`. Source references alone do not count as explicit audit.
5. I05: ensure genuine original result reports explicitly discuss the mapped label; merely guessing from filenames or previous ChatGPT count is insufficient. Where partial evidence is found, mark review level with restraint.
6. I06: reconcile duplicated files/reviews and identify labels with no explicit review, especially all five Remarks and structural Definitions; distinguish `claim source-covered` from `all dependencies closed`.
7. I07: no retroactive mathematical PASS, no completion percentage unless denominator and numerator are defined. Do not erase existing findings T4.7, §7.3 D2, §8 fixed-J, P5.13.
8. I08: check exact coverage of named theorems, propositions, corollaries, countermodels, lemmas vs definitions and remarks. Identify non-numbered source prose and cross-paper dependencies as separate future phase.
9. I09: deterministic Python source/PDF + evidence-manifest inputs, JSON and Markdown outputs in existing `DSD_Audit/audits/formal_proof/formation_axiom_system/scripts` and `results` paths; complete script on GitHub and Windows reproducible command using *existing repo-relative paths*. Avoid arbitrary project input or outputs.
10. I10: independently compute/verify JSON counts against source, preserve all 69 source rows and per-label evidence/status; Git SHA blob roundtrip; Notion/GitHub reciprocal links.
11. I11: report precise distinction between `explicit evidence for a numbered source label` and `proof independently validated`. Do not declare original Formation source, Zenodo or other manuscript modified.
12. I12: document next prospectively lockable audit unit based on uncovered labels or full dependency/statement reconciliation; whole F2 stays OPEN and method-family 22/22 remains unchanged.

## Initial unverified census hypothesis (must be checked independently)

An initial anchored-heading scan of `pdftotext -layout` yielded 69 labels: 14 Theorem, 16 Proposition, 14 Corollary, 2 Lemma, 6 Countermodel, 12 Definition, 5 Remark across original Sections 2–7. These figures are **prospective expected checks**, NOT audit execution results. Counted at source-heading level, not previous case level.

```text
MATHEMATICAL_VERDICT: NOT_APPLICABLE_TO_META_INVENTORY
DSD_AUDIT_VERDICT: NOT_EXECUTED
ORIGINAL_PDF_ZENODO: unchanged
FULL_F2_FPA: OPEN
INDEPENDENT_EXTERNAL_VALIDATION: not_established
```
