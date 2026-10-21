# FAS-F2-G4-CLAIM-INVENTORY-001 — Exact 69-row source/audit evidence reconciliation

**2026-10-21 KST · Kwon Dominicus source · Formal Proof Audit v0.1 · Inventory process only, not an original new theorem or external proof certificate.**

## Source/provenance and prospective boundary

- Original 33-page `DSD_Formation_Axiom_System_EN(5).pdf`; SHA256 `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`; PDF headings extracted by actual locally executed PyMuPDF script, independently compared with `pdftotext -layout`. PDF printed pages = rendered page numbers minus 2 in this edition.
- [Precommit](FAS-F2-G4-CLAIM-INVENTORY-001_PRECOMMIT.md) commit `ee67a6a51a4632be19314bfdec74fe1184cb6b5e`, created before crosswalk execution.
- [Actual executed Python](../scripts/verify_f2_claim_inventory.py), commit `5249363303bed60b6b0b7325d6134f68ce0974e5`, locally executed source SHA256 `7e7ed3a1cefaa2f78550e0055886fc9626349343d12d91d551d3e5be5efff03d`, Git blob `aa633e0fbb9eb25e25f44333c0657f238d352c6e`, confirmed same GitHub exact bytes.
- Local full PDF-driven 69-row deterministic JSON generated with SHA256 `050dde7e3336065af8b723ba03c417213a16a7b1d60ce1a17ea2297d43919aba` and Git blob `a5e6eb5a687c57264cb2b5cce3f6ea33ffbf301f`. **This full PDF-extracted JSON was generated locally and is reproducible by the uploaded script; unlike the GitHub summary, it has not been committed to this repository.**
- [GitHub summary JSON](../results/f2_claim_inventory_summary.json), commit `9bee550d1e5ab2266431a65053766364c9af8895`. The GitHub summary is a distinct compact file, not a byte-identical substitution for the full locally emitted 69-row JSON.

## 1. Source census and evidence denominator

| Numbered original heading type | Original PDF | Explicit mathematics audit | Definition typing audit | Context citation only | No explicit item audit located |
|---|---:|---:|---:|---:|---:|
| Theorem | 14 | 14 | 0 | 0 | 0 |
| Proposition | 16 | 15 | 0 | 1 (6.3) | 0 |
| Corollary | 14 | 14 | 0 | 0 | 0 |
| Lemma | 2 | 2 | 0 | 0 | 0 |
| Countermodel | 6 | 6 | 0 | 0 | 0 |
| Definition | 12 | 0 | 12 | 0 | 0 |
| Remark | 5 | 0 | 0 | 1 (3.4) | 4 (3.1,3.2,6.9,6.13) |
| **Total** | **69** | **51** | **12** | **2** | **4** |

**Interpretation:** 51 numbered mathematical proof/countermodel labels have source-specific recorded argument/fixture reviews (not 51 externally certified theorems). Twelve definitions have typed/source review, which is NOT an existence/proof claim. Two labels were cited in related cases but lacked **direct item proof/review** and four Remarks lack confirmed explicit separate review. Thus 63/69 source headings have direct assigned evidence, with six labels needing further focused checks. The denominator 69 covers the stated seven numbered **heading kinds in Sections 2–7**, **not** the unnumbered prose in §8/§9 or the five appendices.

### Record-count reconciliation

Existing GitHub audit case records, verified by listing actual result files:
- `THEOREM_AUDITS`: **21 RESULT cases** = 14 separate theorem, 2 separate proposition, 5 separate corollary files. The folder name does NOT mean every file is a theorem.
- `SECTION_AUDITS`: **15 RESULT cases** = six grouped cases directly examining numbered source items, plus nine original unnumbered section/appendix cases.
- **36 independent case-result documents**, separate from their 36 PRECOMMIT files. There are **27 distinct numbered-heading source evidence cases**, but their audit scopes together cover more than 27 labelled headings. Do not sum 21+15 as 36 original theorem proof claims.

## 2. Exhaustive original 69-row heading-to-case crosswalk

Status abbreviations: `Explicit mathematical audit` = original labelled claim discussed directly in recorded FPA; `Definition typed review` = explicit definitional/type scope in a recorded FPA (not proposition proof); `Context` = cited as background without a standalone item adjudication; `NO EXPLICIT AUDIT` = not identified in the reviewed case corpus. Case IDs refer to source report file names included in the Python `EVIDENCE` manifest.

| 원문 항목 | 인쇄쪽 | 증거 수준 | 감사 사례 |
|---|---:|---|---|
| Definition 2.1 | 3 | Definition typed review | G0 |
| Definition 2.2 | 3 | Definition typed review | G0 |
| Definition 2.3 | 3 | Definition typed review | G0 |
| Definition 2.4 | 4 | Definition typed review | G0 |
| Proposition 2.5 | 4 | Explicit mathematical audit | G0 |
| Remark 3.1 | 5 | NO EXPLICIT AUDIT | — |
| Remark 3.2 | 5 | NO EXPLICIT AUDIT | — |
| Theorem 3.3 | 6 | Explicit mathematical audit | T3.3 |
| Remark 3.4 | 7 | Context citation only | T3.3 |
| Definition 3.5 | 7 | Definition typed review | T3.6 |
| Theorem 3.6 | 7 | Explicit mathematical audit | T3.6 |
| Countermodel 4.1 | 8 | Explicit mathematical audit | T4.5 |
| Countermodel 4.2 | 8 | Explicit mathematical audit | T4.5 |
| Countermodel 4.3 | 8 | Explicit mathematical audit | T4.5 |
| Countermodel 4.4 | 8 | Explicit mathematical audit | T4.5 |
| Theorem 4.5 | 8 | Explicit mathematical audit | T4.5 |
| Proposition 4.6 | 8 | Explicit mathematical audit | T4.7 |
| Theorem 4.7 | 9 | Explicit mathematical audit, refinement | T4.7 |
| Corollary 4.8 | 9 | Explicit mathematical audit | S4.3 |
| Countermodel 4.9 | 9 | Explicit mathematical audit | S4.3 |
| Lemma 4.10 | 10 | Explicit mathematical audit | S4.3 |
| Corollary 4.11 | 10 | Explicit mathematical audit | S4.3 |
| Proposition 4.12 | 10 | Explicit mathematical audit | S4.3 |
| Lemma 4.13 | 10 | Explicit mathematical audit | S4.3 |
| Corollary 4.14 | 10 | Explicit mathematical audit | S4.3 |
| Definition 5.1 | 10 | Definition typed review | S5 |
| Proposition 5.2 | 10 | Explicit mathematical audit | S5 |
| Corollary 5.3 | 11 | Explicit mathematical audit | S5 |
| Proposition 5.4 | 11 | Explicit mathematical audit | S5 |
| Proposition 5.5 | 11 | Explicit mathematical audit | S5 |
| Proposition 5.6 | 11 | Explicit mathematical audit | S5 |
| Corollary 5.7 | 11 | Explicit mathematical audit | S5 |
| Proposition 5.8 | 11 | Explicit mathematical audit | S5 |
| Proposition 5.9 | 11 | Explicit mathematical audit | S5 |
| Countermodel 5.10 | 11 | Explicit mathematical audit | S5 |
| Proposition 5.11 | 12 | Explicit mathematical audit | S5 |
| Proposition 5.12 | 12 | Explicit mathematical audit | S5 |
| Proposition 5.13 | 12 | Explicit mathematical audit, refinement | S5 |
| Proposition 5.14 | 12 | Explicit mathematical audit | S5 |
| Definition 6.1 | 13 | Definition typed review | T6.5 |
| Definition 6.2 | 13 | Definition typed review | T6.5 |
| Proposition 6.3 | 14 | CONTEXT ONLY; separate proof missing | T6.5 |
| Definition 6.4 | 14 | Definition typed review | T6.5 |
| Theorem 6.5 | 15 | Explicit mathematical audit | T6.5 |
| Corollary 6.6 | 15 | Explicit mathematical audit | S6.6-6.7 |
| Corollary 6.7 | 15 | Explicit mathematical audit | S6.6-6.7 |
| Theorem 6.8 | 15 | Explicit mathematical audit | T6.8 |
| Remark 6.9 | 16 | NO EXPLICIT AUDIT | — |
| Definition 6.10 | 16 | Definition typed review | P6.11 |
| Proposition 6.11 | 17 | Explicit mathematical audit | P6.11 |
| Corollary 6.12 | 18 | Explicit mathematical audit | C6.12 |
| Remark 6.13 | 18 | NO EXPLICIT AUDIT | — |
| Theorem 6.14 | 18 | Explicit mathematical audit | T6.14 |
| Definition 6.15 | 18 | Definition typed review | T6.16 |
| Theorem 6.16 | 19 | Explicit mathematical audit | T6.16 |
| Theorem 6.17 | 19 | Explicit mathematical audit | T6.17 |
| Corollary 6.18 | 20 | Explicit mathematical audit | C6.18 |
| Theorem 6.19 | 20 | Explicit mathematical audit | T6.19 |
| Theorem 6.20 | 21 | Explicit mathematical audit | T6.20 |
| Definition 6.21 | 21 | Definition typed review | P6.22 |
| Proposition 6.22 | 21 | Explicit mathematical audit | P6.22 |
| Theorem 6.23 | 21 | Explicit mathematical audit | T6.23 |
| Corollary 6.24 | 22 | Explicit mathematical audit | C6.24 |
| Corollary 6.25 | 22 | Explicit mathematical audit | C6.25 |
| Corollary 6.26 | 22 | Explicit mathematical audit | C6.26 |
| Theorem 7.1 | 22 | Explicit mathematical audit | T7.1 |
| Corollary 7.2 | 22 | Explicit mathematical audit | C7.2 |
| Theorem 7.3 | 23 | Explicit mathematical audit | T7.3 |
| Corollary 7.4 | 23 | Explicit mathematical audit | C7.4 |

The original section and appendix source audits are tracked as **separate unnumbered cases** and must not be appended to or subtracted from these 69 source-labelled rows.

## 3. Evidentiary findings and precise remaining work

1. **Proposition 6.3 (Forward preservation; printed p.14)** is repeatedly employed in T6.5 and T6.8 source case records. T6.5 explicitly declares it a dependency and proves morphism composition using its conclusion. That is **not** a separately frozen Proposition 6.3 audit with direct tests of the precise forward preservation implications and finite-composite injectivity qualifier. **Required next proof audit:** `FAS-F2-P6.3-FORWARD-001 / NOT_STARTED`.
2. **Remark 3.4** is included as a source context in the T3.3 audit but has no individual remark adjudication; it must not be elevated from citation to passed source claim without explicit scope checks.
3. **Remark 3.1, 3.2, 6.9, 6.13**: no item-specific direct source audit was located in the inspected corpus. These are explanatory paragraphs, not automatically independent original theorems. Next separate (short) prose-claim audit can check accuracy and dependence on primitive typing/identity, submodels, and base fixing, with no paper-wide PASS assumed.
4. Existing substantive language/boundary findings remain: **Theorem 4.7** wording relative to *other five residual clauses*; **§7.3 D2** edge/boundary inheritance; **§8 fixed-J** “strictly weaker” wording; **Proposition 5.13** overbroad unqualified reading. Full mathematical proof coverage depends on resolving or explicitly scoping those claims; inventory completion does not close them.
5. This 69-label inventory does not independently certify semantic completeness of non-numbered proof prose, dependency edges, absence of unstated axioms, manuscript-wide conclusions, or equivalence of the source PDF to any published Zenodo revision.

## 4. Reproduction, computation scope and case disposition

The locally executed PyMuPDF source checker performs: SHA256 source lock; heading-anchored PDF text extraction across exactly 33 pages; uniqueness and fixed-kind census; one row per original heading with literal original title, printed/rendered page, evidence category and verified report path; a no-unexpected-claim/duplicate-evidence assertion. Results: **69 unique extracted headings**, source-kind breakdown 14/16/14/2/6/12/5, evidence status 51/12/2/4, supported by **27** unique direct source evidence case reports. Source statement mathematical truth was **not** recomputed in this particular meta-inventory run.

Windows 11, after checking out the existing GitHub repo, and referring to the **original PDF at the location where the user actually saved it**:

```powershell
python -m pip install pymupdf
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_f2_claim_inventory.py --pdf "C:\actual\path\DSD_Formation_Axiom_System_EN(5).pdf"
```

Generated output (default, existing repo location): `DSD_Audit/audits/formal_proof/formation_axiom_system/results/f2_claim_inventory.json`. The `C:\actual\path` fragment is an **explicit example placeholder** for the true location of the original PDF, not a claimed user-local path. The report+script are on GitHub, with the GitHub compact summary JSON; a separate full run output can be regenerated locally from the same source hash.

```text
AUDIT_CASE: FAS-F2-G4-CLAIM-INVENTORY-001
MATHEMATICAL_VERDICT: NOT_REVIEWED (meta-level inventory, no new original theorem proved)
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY (original-label extraction and evidence-level reconciliation)
REVISION_NEED: NONE (inventory itself; prior four independent source advisories unchanged)
ORIGINAL_NUMBERED_SOURCE_HEADINGS: 69
EXPLICIT_MATHEMATICAL_AUDIT_LABELS: 51
EXPLICIT_DEFINITION_TYPING_AUDITS: 12
CONTEXT_ONLY_OR_DEPENDENCY_LABELS: 2
NO_EXPLICIT_ITEM_AUDIT_LABELS: 4
TOTAL_AUDIT_RESULT_CASE_FILES: 36 (21 standalones and 15 sections)
PRIOR_ORIGINAL_UNNUMBERED_SOURCE_CASES: 9
F2_FULL_PAPER_FPA: OPEN
EXTERNAL_INDEPENDENT_VALIDATION: not_established
ORIGINAL_PDF_ZENODO: unchanged
DSD_METHOD_FAMILY_STANDARDIZATION: 22/22 unchanged
NEXT: FAS-F2-P6.3-FORWARD-001 / NOT_STARTED
```
