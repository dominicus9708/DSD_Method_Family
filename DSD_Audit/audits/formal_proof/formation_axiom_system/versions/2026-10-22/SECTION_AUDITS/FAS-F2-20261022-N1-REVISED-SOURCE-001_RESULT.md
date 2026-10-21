# FAS-F2-20261022-N1-REVISED-SOURCE-001 — New-edition source intake and baseline equivalence check

**Case date:** 2026-10-21 KST. **Manuscript printed date:** 2026.10.22. **Author:** Kwon Dominicus.
**Stage:** source identity, PDF text correspondence and numbered-item census only; **not** full mathematical re-audit of the revised source.

## 1. Source identities and strict separation

| Artifact | Pages | SHA256 | Purpose |
|---|---:|---|---|
| Historical original `DSD_Formation_Axiom_System_EN(5).pdf` | 33 | `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a` | F2 source audited in 2026-08-06 archive |
| New user-uploaded `DSD_Formation_Axiom_System_EN(7).pdf` | 34 | `af721c4188a853880fcc896b80da494e4caa6000ab0af3131ee64cd0770fddfe` | The **new** separately audited PDF source |
| G7 draft compiled EN PDF preview | 34 | `eb035ba69dee64000c9fa6f015b43f95faa23029bd5f705a333b54e4389d38b5` | Derived from revised TeX with old printed date 2026.08.06 |
| G7 revised EN editable LaTeX | n/a | `a22f9171b900115b95738dc0d9abf8e52113df59f3e0ccab5ab028a31014d2ec` | Draft source; date in it not synchronized with newly uploaded PDF |
| G7 revised KO editable LaTeX | n/a | `e73de5b4d2054ce931e4b05b55c729b03ab3f9338abda47af90bdbf69061894a` | Korean draft pending separate bilingual source-to-new-PDF verification |

The GitHub audited sources are **not** silently replaced, the date-stamped version folders are separate, and neither the new English PDF nor either TeX draft is asserted to have been published on Zenodo.

## 2. Reproducible local intake result

Used local PyMuPDF (`fitz`) on the exact above PDF files. For each page in rendered 1-based order, extracted text using `page.get_text('text',sort=True)` for claim-heading census, matching the anchored original-heading regex for `Definition|Theorem|Proposition|Corollary|Lemma|Countermodel|Remark` followed by numeric label.

- Original PDF: **69** numbered headings; new PDF: **69**.
- Both: 14 Theorems, 16 Propositions, 14 Corollaries, 2 Lemmas, 6 Countermodels, 12 Definitions, 5 Remarks.
- The sequence of **label numbers and kinds** is identical. Exactly **one original heading title changed**:
  - 2026-08-06: `Proposition 5.13 (Zero-extension of the term map is not channel-faithful)`;
  - 2026-10-22: `Proposition 5.13 (Conditional channel-membership loss under zero extension)`.
- Other source modifications are inside statement/proof/Discussion paragraphs or finite witness data; identical headings do NOT imply proof continuity.

**Independent extracted PDF text correspondence:**

In each 34-page PDF (the new uploaded EN(7) and the G7 compiled EN preview), concatenate `page.get_text('text')` over all pages and remove **all whitespace characters** with regex `\s+` to compare PDF-extracted content.
Both yield **71,220 non-whitespace characters**.
- New uploaded PDF normalized text SHA256: `c27c616005249130d531b82cac6f03d5a4efb2c2afdc94febaf670ad983554de`.
- G7 EN preview normalized text SHA256: `f942e2cce9f66d1df04f10a0c707a9e926e056561f263bb674c6ea5a7150c551`.
- The only normalized-text difference is the **printed cover date**, `2026.08.06` in the G7 preview versus `2026.10.22` in the new uploaded PDF. Replacing that one literal date yields **exact equality of the full normalized PDF-extracted text**, not merely a high similarity score.

**Boundary:** text extraction equality after replacing a cover date does not imply byte-identical PDFs or line-for-line identical raw TeX. PDF bytes demonstrably differ; rendering/metadata can differ. Still, the new uploaded PDF is strongly corroborated as the G7 revised English text with a new printed date. The new PDF's date is a manuscript label that is **one day after the audit session date (2026-10-21)**; it is not an independently confirmed Zenodo publication timestamp.

## 3. New-edition audit scope and outstanding proof tasks

This N1 case locks provenance and checks source inventory **without importing previous theorem PASS results**. The four G6-amended mathematical and descriptive loci that now need source-specific re-audit on the **new 34-page PDF**:

1. §4.2 **Theorem 4.7** — residual six-clause independence and the proof's quantifier/background scope.
2. §5 **Proposition 5.13** — zero-extension conditional channel admission ambiguity, distinguishing the candidate-channel set `\mathfrak U_L`.
3. §7.3 **D2 finite witness** — complete 57-item grid / nine selected items and six blocked boundary-slot inheritance, earliest branch b=3.
4. §8 **Discussion fixed-J comparison** — no universal implication hierarchy; Proposition 6.22 remains a separate statement. Verify §6.5 and §9 dependency prose.
5. After those focused checks, a manuscript-wide dependency and unaffected-statement regression is still required. Original archival audit code/JSON may serve as *candidate reusable fixtures* but must be explicitly mapped or rerun under the new source; old 69/69 is historical coverage, not a new-edition proof verdict.
6. **Release metadata action (not automatic correction):** G7 revised TeX has the earlier printed date `2026.08.06` whereas the new uploaded PDF prints `2026.10.22`; update and compile version-aligned TeX source before preparing a final Zenodo release package. Korean draft requires its own source-vs-output parity checks.

## 4. Verdict and next checkpoint

```text
CASE: FAS-F2-20261022-N1-REVISED-SOURCE-001
VERSION_SOURCE_LOCK: PASS (new PDF exact SHA256, 34 pages, printed date)
NUMBERED_LABEL_CENSUS: PASS_WITH_BOUNDARY (69/69 sequence, 1 changed heading title)
G7_EN_PREVIEW_VS_NEW_PDF_EXTRACTED_TEXT: PASS_WITH_DATE_DIFFERENCE_ONLY
MATHEMATICAL_VERDICT: NOT_REVIEWED_ON_NEW_SOURCE
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY (N1 intake only)
REVISION_NEED: NEW_VERSION_TEX_DATE_ALIGNMENT; mathematical G6 amendments need new source-bound re-audit
NEW_PDF_FULL_F2_FPA: OPEN
2026_08_06_OLD_F2_AUDIT: separate historical archive; unchanged
ZENODO_NEW_VERSION_PUBLISHED: not_verified
INDEPENDENT_EXTERNAL_VALIDATION: not_established
NEXT: FAS-F2-20261022-N2-FOUR-SECTION-REAUDIT-001 / NOT_STARTED
```
