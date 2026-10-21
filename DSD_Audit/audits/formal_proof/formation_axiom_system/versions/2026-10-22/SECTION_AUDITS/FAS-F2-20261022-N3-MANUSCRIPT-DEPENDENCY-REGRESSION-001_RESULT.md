# FAS-F2-20261022-N3-MANUSCRIPT-DEPENDENCY-REGRESSION-001 — Whole-text and proof-dependency regression

**Audit performed: 2026-10-22 KST. Source author: Kwon Dominicus.**
Manuscript-version source: `DSD_Formation_Axiom_System_EN(7).pdf` (34 pages, dated 2026.10.22), SHA256 `af721c4188a853880fcc896b80da494e4caa6000ab0af3131ee64cd0770fddfe`. Historical comparison source: `DSD_Formation_Axiom_System_EN(5).pdf` (33 pages, dated 2026.08.06), SHA256 `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`.

## 1. Prospective lock and independent new-version execution
- [N3 precommit](FAS-F2-20261022-N3-MANUSCRIPT-DEPENDENCY-REGRESSION-001_PRECOMMIT.md), Git commit `5f41cf83a1a725333455fcc17a5976b172281dd0`, before the current source comparison and Python execution.
- [Actual source-locked Python](../scripts/verify_n3_source_diff.py) SHA256 `7c17b94a81f7b4663b9efd4a82d03cba83377837e1d44224416134b56bd95926`, Git blob `dae20663d65d3a3e92a40a85078b3f66173556e1`, Git commit `1b16ce385b5cccec45e074eacf788646773b2d8b`. Executed locally under `python -W error -m py_compile` and `python -W error` with exact old and new PDFs.
- [Exact executed JSON](../results/n3_source_diff.json), SHA256 `97765ebd13d29fa7b3d57721b678c31364f90ef5903ddb6c53241230642488a8`, Git blob `f82f2b57f2573f231cd4595ca172f6ad899b66f7`, commit `2a5d549b30e97138490439152e64df9da1758325`. Local/remote executable and output Git blob hashes verified byte-identical.
- Full independent extended Python source-scan/audit was also executed locally at `scripts/verify_n3_dependency_regression.py` (not uploaded as source) and detailed JSON generated locally. GitHub **shorter** executable with exact tested outputs is the published reproducible checker; no false claim that the two script variants are byte-identical.

## 2. Full source diff and numbering audit
- Both editions: **69** numbered original source headings: Theorem 14, Proposition 16, Corollary 14, Lemma 2, Countermodel 6, Definition 12, Remark 5. Exact numbering, kinds and order unchanged.
- All **67 headings excluding Theorem 4.7 and Proposition 5.13** have unchanged corresponding titles/numbering; in fact Theorem 4.7's *title* is also unchanged while its premise/proof wording changed. **Proposition 5.13 alone changes its heading title.**
- PyMuPDF text extraction, omitting only blank lines and pure printed page-number lines, yields **1,820 exactly unchanged content lines** outside source edit spans.
- Exactly **six text-diff hunks**, not six substantive claims: (i) cover date 2026.08.06→2026.10.22, (ii–iii) T4.7 preamble and proof, (iv) P5.13, (v) §7.3 D2, (vi) §8 Discussion. Thus the **four** specified manuscript correction loci account for **five** substantive diff hunks.
- All other content passages including unedited numbered mathematical statements and their source proof prose, original §6 definitions and results, §7.4, §9 Conclusion, Appendices A–E, bibliographic content and cited case identifiers remain unchanged in extracted text. A text match is NOT a second machine proof of any theorem.

## 3. Dependency impact analysis
1. **T4.7:** the revised six-clause relative-independence background removes the logical ambiguity of an intact parent axiom containing the falsified residual. Proposition 4.6's typing-induced dependencies and Theorem 4.5's separate independence argument are textually unchanged.
2. **P5.13:** the zero-extension result explicitly requires absent candidate and admitted zero-term channel coexisting. The rest of §5 (q partial, channel membership/role and undefined T outside admitted channel C) remains textually unchanged. The original false universal strengthening is no longer asserted.
3. **D2 §7.3:** new explicit 57-item material carrier / 9 retained selected items / six inherited blocked slots and supplied primitive BC rules underlie the same b=3 claim. §7.4, original Definition 6.15 and Theorem 6.16 stages remain unchanged; N2 checked a typed consistent 57-item witness.
4. **§8 fixed-J:** revised Discussion now explicitly states strict equivalence does NOT unconditionally imply coincidence for a separately fixed arbitrary J. Definition 6.21, Proposition 6.22's one-way nonimplication and Corollary 6.12's proper isomorphism-J finite-family transport remain unchanged, as does §9 Conclusion.
5. These are **source-dependency and proof-text-preservation results** combined with [N2 four-locus mathematical re-audit](FAS-F2-20261022-N2-FOUR-SECTION-REAUDIT-001_RESULT.md). They do not import historical original-paper PASS conclusions as fresh source-specific proofs of every unaffected theorem.

## 4. Publication Release Candidate RC1 preflight
- New **English LaTeX RC1** source SHA256 `4da4441242d1ade8161ec91e3fca1cb9c8a12270dc8c690af3c73a856c10a1b1`, XeLaTeX 34-page PDF SHA256 `67269d0ba332cdc4750a521c591b656a954c3bc76376d92165784fb0a2ab8a3d`.
- New **Korean LaTeX RC1** SHA256 `e0c06cd74286e03bd38b14e0f300fa73a1627bc0732ae75c452b8cb4cba051b3`, XeLaTeX 30-page PDF SHA256 `f16bc6cea7a6dec7c9002f7831eda091e5499124695596db51232302e5d32dc3`.
- For BOTH languages, compared to locally edited G7 TeX, **only** the single cover-date text `2026.08.06`→`2026.10.22` changed. All \label, \cite key sequences and authored theorem-environment counts identical. Source author remains Kwon Dominicus.
- **English RC1 PDF** and supplied new EN(7).pdf: all extracted PDF text **exactly equal after removing whitespace** (71,220 nonwhitespace characters; normalized text SHA256 `c27c616005249130d531b82cac6f03d5a4efb2c2afdc94febaf670ad983554de`). This is text identity, NOT binary PDF identity.
- **Korean RC1 PDF** text normalized equals corresponding earlier G7 Korean preview after replacing the cover date. Korean inherited UnBatang italic fallback warning persists; no newly introduced compilation errors, missing labels/citations or overfull boxes.
- Visual review performed on title and four amended English regions, and corresponding Korean title/edited pages. Zip integrity and every included file hash validated.
- Release-candidate package (download from ChatGPT conversation, **NOT uploaded to GitHub or Zenodo**) SHA256 `226a302edb5c9aa8dfda971bdbc6ac05a75f61442f6f0d4064b91f0c8249db0f`, 622970 bytes, with EN/KR PDF and LaTeX, version notes, bilingual change history, proof-scope summary, scripts, JSON and SHA manifest.
- Zenodo final action: create linked **New version** from the owner's existing Formation Axiom System record, retain correct creator/license/metadata, upload EN PDF (optional Korean/source artifacts according to publishing preference), inspect preview and select Publish. This was **NOT** done, as no connected Zenodo publishing action/authenticated account is available. Do not claim DOI minted.

## 5. Final case and whole-paper boundaries

```text
AUDIT: FAS-F2-20261022-N3-MANUSCRIPT-DEPENDENCY-REGRESSION-001
SOURCE_DIFF_REGRESSION: PASS (69 headings, 67 unchanged other titles, 5 substantive change spans)
DEPENDENCY_REGRESSION: NO_NEW_UNADDRESSED_SOURCE_TEXT_CONFLICT_FOUND
MATHEMATICAL_VERDICT: PREVIOUSLY_AMENDED_FOUR_LOCI_N2_SUPPORTED; N3_VERIFIES_TEXT_AND_DEPENDENCY_COHERENCE_ONLY
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY
BILINGUAL_RC1_LATEX_AND_XELATEX_PREFLIGHT: PASS_WITH_KR_INHERITED_FONT_WARNING
RELEASE_PACKAGE_RC1: CREATED_AND_SHA_VERIFIED
ORIGINAL_2026_08_06_AUDIT_ARCHIVE: unchanged
F2_FULL_PAPER_INDEPENDENT_FORMAL_PROOF_AUDIT: OPEN
EXTERNAL_INDEPENDENT_VALIDATION: not_established
PUBLIC_ZENODO_NEW_VERSION: NOT_PUBLISHED
NEXT: OWNER_ZENODO_NEW_VERSION_DRAFT_AND_PUBLISH (requires linked Zenodo owner access and final publish action)
```

## 6. Windows 11 replay

From checked-out `DSD_Method_Family` root:

```powershell
python -m pip install pymupdf
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\versions\2026-10-22\scripts\verify_n3_source_diff.py "ABSOLUTE_PATH_TO_2026-08-06_EN5.pdf" "ABSOLUTE_PATH_TO_2026-10-22_EN7.pdf"
```

The generated JSON resides in `DSD_Audit/audits/formal_proof/formation_axiom_system/versions/2026-10-22/results/n3_source_diff.json` unless an explicit third path is passed. Input names shown above are **placeholders**, not claims about user-local Windows folders.
