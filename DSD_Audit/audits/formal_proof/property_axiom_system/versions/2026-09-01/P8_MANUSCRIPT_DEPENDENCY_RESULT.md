# PA-P8-20260901-DEPENDENCY-001 — manuscript-wide dependency and revision-readiness audit

Author **Kwon Dominicus**. Executed 2026-10-22 KST. Exact 23-page English PDF SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.
Prospective precommit `72ed52c12e17d3c32970a140a7687fdb4ca02a72`, created before this dependency classification.
**Method:** read English §§2–13 and Appendices A–C, source-specific claims, prior case reports, existing verified full CI log. This is a **dependency and selected-proof audit**, NOT a completed exhaustive new formal proof of all 56 numbered items.

## 1. Dependency map for all thirteen claims of Theorem 11.1 (printed pp19–20)

| Item | Source basis | Status |
| --- | --- | --- |
| (1) finite typed profiles / no universal axis | Definition 2.1–2.5 | SOURCE-SUPPORTED |
| (2) two primitive soundness conditions | §3 PI / PII | SOURCE-SUPPORTED |
| (3) mutual residual independence / not typing tautologies | Countermodels 4.1–4.2, Theorem 4.3, Proposition 4.4 | SUPPORTED |
| (4) separated partial-status cases | Definition 3.3, Proposition 4.5 | SUPPORTED |
| (5) unique C1 completion and inverse laws | C1, Theorem 3.7 | SUPPORTED, relative to fixed primitive core |
| (6) forward map category / embeddings / submodel preorder | Definitions 6.1,6.3,6.5; Props 6.2,6.4; Thm 6.6 | CONDITIONAL — missing guard for declared yet profile-unavailable kinds in source F3–F5 |
| (7) strict isomorphism and equivalence | Definition 6.7, Theorem 6.8 | EQUIVALENCE SUPPORTED under S1–S4; **“exactly bijective embeddings” wording requires S2/S3** |
| (8) representation-inclusive equivalence finer | Def6.10, Th6.11 | SUPPORTED conditional on valid core strict maps |
| (9) branching symmetry/invariance / no Stage-5 branch | Definition 7.1, Proposition 7.2, Theorem 7.5 | SUPPORTED, conditional on typed comparisons |
| (10) trivial and finite realization | Th8.1, Th8.4 | SUPPORTED in stated finite compatible data domain |
| (11) first branching 2/3/4 witnesses | Constructions 8.5–8.7 | SUPPORTED by source argument + recent 7-test finite CI |
| (12) finite simple-summary nonclassification | Definition 9.1, Th9.2 | SUPPORTED by explicit collision witness |
| (13) Stage-VI fixed Formation interface | §2.1, Remark 3.5 | SUPPORTED |

**Dependency propagation:** P5's forward-map definedness issue affects the unconditional category claim (6), strict summary (7), representation category (8) and potentially any theorem defining comparison via those morphisms, including (9) and the manuscript Abstract. The valid *intended* categories can be recovered by adding source-profile availability guards and fully stating strict-isomorphism S1–S4; no change to the two primitive axioms or C1 is needed for these local fixes.

## 2. Other exact-source boundaries

- §9.2 says aggregate equality “is consequently weaker” than strict property equivalence; as an **information-loss/nonreconstruction** statement it is supported by §9's finite summary witness, but there is **no core constraint on arbitrary separately supplied downstream bridge Θ_A** to establish an unconditional converse implication under arbitrary, unrelated bridges. Qualify this sentence as comparison of information retained, not a universal implication without equivariance and support hypotheses.
- §§10,12,13 consistently place the earlier realized-axis property system in a *specialization* and keep current typed property core axis-independent. No universal line/rank/bilinear/normal requirement is imported.
- Appendix C builds typed finite witnesses in the exact source order (supply sorts → declare kinds → type product → applicability & prerequisites → partial assignment → check `DomΞ⊆Ap∩DepSat` → C1 completion → optional representation). It does **not** explicitly attempt to reconstruct the missing F3 profile-availability quantifier, so the §6 gate remains open.
- The paper's §23 data/code paragraph says an executable general-property repo **“is intended to accompany the final public version”**, while `dominicus9708/Property_Axiom_System` actually exists and has fresh CI evidence on 2026-10-22. This is a **publication-status / bibliography update candidate**, not a source mathematical contradiction.
- Repository README subtitle `A General Typed Property Extension` differs from actual PDF `A Typed Applicability-and-Dependency Extension of the Formation Axiom System`; editorial synchronization is advisable at release.
- Exactly 56 numbered headings (Definitions23, Theorems10, Propositions7, Corollaries3, Countermodels2, Remarks7, Constructions4) inventoried at P0. An *exhaustive proof-level* 56/56 re-audit has NOT been done; no numerical success percentage was invented.

## 3. Findings prioritized without forced discard

**Source-edit candidate A / mathematical typing (priority high):** Def6.1 F3–F5 and Def6.3 source-input clause must explicitly restrict to property kinds declared **and whose profiles are available in the source model**. This restores identity and composition for legal cores with declared but unavailable profiles (per Def2.5) without changing primitive axioms.

**Source-edit candidate B / logical equivalence phrasing (priority high):** Th6.8, Abstract and Theorem11.1(7) must not conflate componentwise bijection with full strict-isomorphism S1–S4. At minimum include S2 available-sort equality and S3 property-declaration equality (plus inverse compatibility), as shown by an explicit legal counterinterpretation in [P5–P7](P5_P7_COMPARISON_RESULT.md).

**Source-edit candidate C / editorial scope (priority medium):** §9.2 aggregate/strict equivalence phrasing should say aggregate agreement alone does not reconstruct strict core, and not assert a fixed-bridge unconditional implication.

**Source-edit candidate D / bibliographic (priority low):** repository README subtitle and paper's data/code-availability sentence should be synchronized before archival release.

English section-wise candidate amendment language prepared in [PATCH_PROPOSAL_EN.md](PATCH_PROPOSAL_EN.md). **Not applied** to PDF or LaTeX; Korean precise parity cannot be completed without the corresponding actual source.

## 4. Follow-up and verdict

```text
CASE: PA-P8-20260901-DEPENDENCY-001
MANUSCRIPT_56_HEADING_INDEX: COMPLETE
THEOREM_11_1_ALL_13_DEPENDENCIES: CLASSIFIED
ALL_56_INDIVIDUAL_PROOFS_REAUDITED: no
P1_P4_CORE: SUPPORTED
P5_CATEGORY_AND_BIJECTIVITY: MANUSCRIPT_CLARIFICATION_REQUIRED
P6_STAGE_BRANCHES: SUPPORTED_WITH_TYPING_DEPENDENCY
P7_SIMPLE_SUMMARY: SUPPORTED
EXTERNAL_SPECIFIC_AXIS_SPECIALIZATION: preserved separate
PYTHON_ORIGINAL_EXECUTION: success both Python 3.10/3.12 (7/7 each)
MANUSCRIPT_SOURCE_CHANGES_APPLIED: no
FPA_WHOLE_PROPERTY_PAPER: OPEN
BILINGUAL_PARITY: UNVERIFIED
INDEPENDENT_EXTERNAL_VALIDATION: not_established
NEXT: PA-P9-SECTIONWISE-TEX-INTEGRATION-READINESS-001 / BLOCKED_ON_EDITABLE_SOURCE
```
