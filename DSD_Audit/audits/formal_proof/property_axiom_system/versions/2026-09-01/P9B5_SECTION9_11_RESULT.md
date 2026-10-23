# PA-P9B5-20260901-LAST4-ITEMS-001 — Section 9 + 11 itemwise source audit, 56/56 review checkpoint

**Executed:** 2026-10-23 KST. Original English Property Axiom System PDF by **Kwon Dominicus**, 23 pp, printed date 2026.09.01, SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.
**Precommit:** [P9B5_SECTION9_11_PRECOMMIT.md](P9B5_SECTION9_11_PRECOMMIT.md), commit `50365b763b257b6749e52c5113c341cc8009614f`.
Source PDF pp17–23; cumulative prior itemwise reports P9B1 (26), P9B2 (12), P9B3 (6), P9B4 (8), now P9B5 final 4 => **56/56 original numbered headings manually reviewed for typing, explicit proof boundaries and dependencies**. **This is NOT 56 completed independent machine proofs** and global FPA remains OPEN.

## Four original numbered headings

| Item | Specific source inspection | Outcome |
| --- | --- | --- |
| **Definition 9.1 (Simple finite property summary)** | For *finite zero-bearing property models*, `S(A)` retains declared kind count and property-labelled triple `(|D_A,varpi|,N^0_A,varpi,N^neq0_A,varpi)`. No source cross-property co-location/correlation or complete typed input/availability is recorded. Zero/nonzero counts need the declared zero-bearing property kind; do not impose them on a kind lacking designated zero. | **WELL_DEFINED_IN_FINITE_ZERO_BEARING_SCOPE**. |
| **Theorem 9.2 (Equal summaries do not classify strict cores)** | Source uses Construction 8.7, two kind labels on two inputs with full applicability. For both models, each kind has domain 2, one assigned zero, one assigned nonzero. `S(A)=S(B)`. A label-preserving carrier bijection must preserve kind1's pattern (0,1), forcing identity; kind2's pattern differs, so strict core isomorphism fails. Exhausted both available permutations as P9B4. | **FINITE_COUNTEREXAMPLE_PROVES EXISTENTIAL NONCLASSIFICATION**. Does not say any summary always fails. |
| **Remark 9.3 (What the summary loses)** | Source explicitly locates collision in missing joint placement/cross-kind correlations, not merely scalar numeric equality. Claims more elaborate summaries *can* fail without a separate injectivity/reconstruction theorem; no universal “all summaries always fail” statement. | **INTERPRETATION_SUPPORTED_WITH_SCOPE**. |
| **Theorem 11.1 (13-part static property-closure summary)** | Each source-item premise/conclusion and dependencies crosschecked with Section proofs as in [P8 full dependency map](P8_MANUSCRIPT_DEPENDENCY_RESULT.md). Items 1–5 and 10–13 supported within their conditions; item6 forward-map category and embedding preorder inherits the **F3–F5 declared-unavailable profile typing gap**; item7's “exactly bijective property embedding” inherits **failure of componentwise bijection alone to imply S2/S3**; items 8–9 require a coherent S1–S4 strict notion and correctly typed map/comparison interfaces. These source claims cannot be stamped unconditionally PASS without clarifying §6. | **PARTIALLY_SUPPORTED / TWO_EXPLICIT_DEPENDENCY_GATES**. |

### Unnumbered §9.2 downstream aggregation relation

`Theta_A:G_A→U` on selected defined typed records is **application-supplied**, not constrained by the Property core to be injective or equivariant. Thus §9.2's statement that equality of aggregate output is “consequently weaker” is valid as a **non-reconstruction observation**: equal output alone generally does not entail strict underlying core equivalence. It should **not** be promoted to a universal implication `strict iso ⇒ equal aggregate outputs` for arbitrary independent choices of `Theta_A,Theta_B`. **Scope note retained**; no new axioms introduced.

### Unnumbered §§10,12,13 and Appendix A–C interface review

- §10 and concluding §§12–13 preserve the fixed formation Stage-VI dependency and distinguish optional realized-axis geometry and downstream dynamics, consistent with the current general Property core.
- Appendix A nomenclature and B classification maintain primitive vs definitional/representation/dependent distinctions.
- Appendix C's sequence 1–11 supplies auxiliary carriers, declares kinds, makes typed products for profile-available kinds, checks PI/PII, then C1 completion. Item7's “for every declared kind” should be read using the step4 **declared + profile available** guard for typed `Ap,DepSat,Xi`. This mirrors the source's explicit premise in Theorem 8.4, unlike the unguarded F3 source phrase.
- Data/code declaration says the *general property reproducibility repository is intended to accompany final public version*, while repository `dominicus9708/Property_Axiom_System` already exists. Treat it as **release-metadata/editorial stale text**, not proof error.
- No claim that exact DOI record dates or availability were freshly externally verified in this manual manuscript audit.

## Full 56 original headings checkpoint with honest limits

| Section | Numbered item count | This audit cycle |
| --- | ---: | --- |
| §2 | 7 | P9B1 |
| §3 | 8 | P9B1 |
| §4 | 6 | P9B1 |
| §5 | 5 | P9B1 |
| §6 | 12 | P9B2 |
| §7 | 6 | P9B3 |
| §8 | 8 | P9B4 |
| §9 | 3 | P9B5 |
| §11 | 1 | P9B5 |
| **Total** | **56** | **56/56 manually scoped** |

**Not yet discharged:** independent formal re-derivation of every general proof in a machine-checkable formal system, all arbitrary typed signatures, all multi-sort/multi-element morphism edge cases, rigorous source repair or EN/KR LaTeX/PDF parity, external peer review. New mathematical issues were specifically localized in §6 source quantification and Th6.8's shortened bijection characterization. Preserve previously observed counterexamples and all finite CI evidence. No source edit performed.

```text
CASE: PA-P9B5-20260901-LAST4-ITEMS-001
P9B_NUMBERED_MANUSCRIPT_ITEMWISE_SCOPE_AUDIT: 56/56 COMPLETE
P9B_ALL_GENERAL_CLAIMS_MACHINE_PROVED: no
P9B_SECTION6_TWO_LOGIC_TYPOLOGICAL_GATES: OPEN
P9B9_SOURCE_EXAMPLE_AND_TH11_DEPENDENCIES: AUDITED_WITH_BOUNDARIES
NEW_INCONSISTENT_CORE_AXIOM_DETECTED: no
ORIGINAL_PYTHON_MANUSCRIPT_ZENODO_MODIFIED: no
FULL_PROPERTY_FPA: OPEN
NEXT: PA-P10-20260901-CROSS-SORT-MORPHISM-REGRESSION-001 / NOT_STARTED
```
