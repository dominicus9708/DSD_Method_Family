# P28 — Historical Zenodo-linked Property GitHub vs current P27 research

Date: 2026-10-27 KST. Kwon Dominicus.

The historical [Property_Axiom_System](https://github.com/dominicus9708/Property_Axiom_System) repo, release [1.1 (2026-09-01)](https://github.com/dominicus9708/Property_Axiom_System/releases/tag/1.1), was checked against P27 revised bilingual manuscript and the broader DSD_Method_Family audit. **Do not interpret current main as the historically tagged 1.1 snapshot**; original tag, original src/tests/results, past CI evidence, `.zenodo.json`, `CITATION.cff`, and published manuscript/Zenodo were not altered.

Current companion repo has been **non-destructively supplemented** with:
- `audits/2026-10-27/p27_independent_math.py`: verified P27 672 finite cores and 396,898 bounded pairs.
- `audits/2026-10-27/p27_expected_result.json`: full expected finite audit JSON.
- `audits/2026-10-27/P27_LEGACY_RELEASE_AND_CURRENT_PAPER_COMPATIBILITY.md`: historical/new manuscript mapping and code limits.
- `.github/workflows/property_p27_current_audit.yml`: both Python 3.10 and 3.12 reverify old source Git blob identity, seven old tests, three original results semantic regression and current P27 exact JSON.
- README and PROOF_MAP reflect the preserved version divide and scope.

**Actual completed CI** [#40348615249](https://github.com/dominicus9708/Property_Axiom_System/actions/runs/40348615249): SUCCESS both Python versions, and both logs contain the original source-custody hash check, 3 historical fixture semantic comparisons, and exact P27 JSON replay. This is bounded finite verification, not whole-property FPA proof.

**Source compatibility finding:** Original `simple_summary` is already keyed by property labels, agreeing with corrected P27 Def9.1 on the **restricted** profile-available/zero-bearing/property-finite domain; the code does NOT enforce all P27 input well-typedness. Original forward maps and comparisons are bounded computational companions, not complete implementations of Def6.1–6.8 for arbitrary multi-sort signatures. The historical release's bare “bijective embeddings” wording is superseded by P27 S1+S2+S3 (+derived S4).

**Publication boundary:** This audit did not establish the exact original *general* Property paper Zenodo DOI. The separately realized-axis Property DOI must not be substituted. No new manuscript or software release, DOI, Zenodo deposit, or moving of release tags was performed. `CITATION.cff` software 0.1.0 and release 1.1 may denote separate version axes.

**Next research gate:** if requested, verify original Zenodo general-paper record and related GitHub link, separately prepare public revised edition/release metadata; otherwise advance arbitrary multi-sort and independent proof-review obligations in P27. Both Property and Formation whole FPA remain OPEN.

Notion: [P28](https://app.notion.com/p/40581f51e7fa81019206cfa2bc56bc7d).
