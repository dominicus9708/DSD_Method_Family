# PA-P26 — User-supplied bilingual manuscript source and integrated revision regression

**Author:** Kwon Dominicus. **Audit:** 2026-10-26 KST.
**Scope:** Source-level correction of original uploaded 2026-09-01 EN(3)/KR(3) TeX candidates, plus revised 2026-10-22 Formation Stage-VI interface regression. **Not** an independent complete ZFC formal proof or published new manuscript version.

## Locked inputs and source equivalence

- Uploaded original EN(3) TeX SHA256 `bbcff0c2f7047ddbffb737040f25d171438f6ac2934344a8bcafb8fbc160b8d3`.
- Uploaded original KR(3) TeX SHA256 `91f42dc00bcc653f18a8329bbcfeeb7daf8f8c3ec2032f48abd4f115ee33b241`.
- The compiled original EN(3) 23-page PDF and audit source EN(4) 23-page PDF (SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`) yielded exactly matching **11,488 PDF text tokens**, providing source-content parity without claiming original TeX file-byte identity.
- EN/KR original source inputs preserved separately under [locked_upload](locked_upload); old PDFs, published TeX and Zenodo not overwritten.

## Bilingual section-level mathematical corrections performed

Exactly matching correction-operation IDs in EN and KR were applied to **Abstract and body §§4,6,9,11**:
1. Th4.3: mutual nonderivability over typed premodels, not assuming conditional C1 on axiom-violating counterpremodels.
2. Def6.1 F3/F4/F5: common declared-and-source-profile-available quantification guard; unavailable != available empty.
3. Prop6.2: identity/composition source-product existence argument stated explicitly.
4. Def6.3: property embedding source input domain guard.
5. Th6.8: strict property isomorphism characterized by embeddings satisfying S1 bijective source carrier maps, S2 matching available auxiliary-sort sets, S3 matching declared kind sets, and proof that these together with reflection of primitives imply S4 inverse embedding.
6. §9.2: aggregation equality alone does not reconstruct strict equivalence for arbitrary supplied external bridges.
7. Abstract and Th11.1(7): propagated the strengthened strict-isomorphism claim.

Existing `% -----` comment-delimited section divisions retained; new P26 modified-section comments placed **inside** the four modified sections.
The numbered source environment distribution is unaltered: 23 definitions, 10 theorems, 7 propositions, 3 corollaries, 2 countermodels, 4 constructions and 7 remarks = **56/56**.
Both 2 primitive axioms and 1 C1 closure clause remain untouched; both papers retain exactly 13 main sections, 3 appendices, 36 labels and preserved label order. **Every unedited main section and appendix is byte-identical at the text level to its uploaded original.**

## Actual independent execution

Locally, four original/revised EN/KR LaTeX candidates compiled using XeLaTeX/latexmk:
- Original EN(3) **23 pages**, amended EN **24 pages**.
- Original KR(3) **20 pages**, amended KR **21 pages**.
- No unresolved reference or citation warnings in the final amended compilation.
- Local revised EN PDF SHA256 `e50adff5ba0048cb39764dac093591d39d2b0da733a23c6b64a6aeefa215503d`.
- Local revised KR PDF SHA256 `e69f12eefd6c217f1249842bc19e31aeec68bf68188b71d60a7a221fdbd91455`.
- Visually inspected the pages containing original repaired Th6.8 (English page 14; Korean page 12); no obvious clipping.
- EN/KR source mathematical display formula counts: 78 each; all 78 formulas have identical normalized LaTeX structure after only translated text and terminal punctuation are normalized. Inline math count 218 each. This is **not** full word-by-word bilingual semantic certification: one legacy presentation asymmetry denotes Stage 5 in inline math in EN and in prose in KR.

**Independent GitHub Actions [#40210203224](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40210203224) passed:**
- Python 3.10 and 3.12 both executed uploaded [deterministic script](build_revised_property_axioms.py) against immutable original `EN(3)`/`KR(3)` inputs and verified both generated revised TeX files **byte-for-byte identical** to the committed revisions.
- Both Python versions re-ran P20/P22/P23/P24 archives as full JSON with exact match.
- Separate CI XeLaTeX rebuilt revised EN/KR to **24/21 pages** respectively; bundled PDFs available as CI workflow artifact.
- Repository Git blob SHA values were independently verified to match the original and revised on-disk files, not merely copied status claims.

## Scope, release and next gate

The changed set-theoretic proof text is source-checked and supported by the earlier P24 finite countermodels, but all arbitrary typed signatures have not been separately formalized in a proof assistant.
Original paper and Zenodo remain unchanged. The newly compiled EN/KR PDFs are **reviewable candidates**, not a published revision.
An author decision regarding publication metadata, whether to retain the original publication date in the updated title page, and actual Zenodo new-version release remains a separate gate.
Entire Property FPA = **OPEN**; Formation v4.5 whole FPA = **OPEN**.

```text
PA_P26: INTEGRATED_BILINGUAL_SOURCE_AND_BUILD_COMPLETED
UPLOADED_EN3_KR3_ORIGINALS_PRESERVED: YES
EN3_ORIGINAL_COMPILED_VS_EN4_AUDIT_PDF_TEXT: 11488/11488 EXACT
BILINGUAL_SECTION_EDITS: ABSTRACT + §4 §6 §9 §11
MATH_NUMBERED_ENVIRONMENTS: 56/56 EACH
XELATEX_LOCAL: EN_24_PAGES / KR_21_PAGES
XELATEX_GITHUB_CI: EN_24_PAGES / KR_21_PAGES
P20_P22_P23_P24_PYTHON_3_10_3_12_FULL_JSON: EXACT
BILINGUAL_NATURAL_LANGUAGE_CERTIFICATION: NOT_CLAIMED
PUBLISHED_MANUSCRIPTS_AND_ZENODO: UNCHANGED
WHOLE_PROPERTY_FPA: OPEN
```
