# PA-P24-20260901-SOURCE-PAPER-REVISION-NECESSITY-001 — direct manuscript audit result

**Audit date:** 2026-10-25 KST.
**Author:** Kwon Dominicus.
**Audit status:** P24 EXECUTED; manuscript correction required; **original paper NOT EDITED**.
**Original Property PDF:** 23 pp, dated 2026.09.01, SHA256 \`03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c\` (actually hashed from supplied exact PDF).
**Formation v4.5 PDF:** 34 pp, dated 2026.10.22, SHA256 \`af721c4188a853880fcc896b80da494e4caa6000ab0af3131ee64cd0770fddfe\` (actually hashed from supplied exact PDF).
**Prior evidence:** [P23 finite interface audit](P23_TYPED_STAGEVI_ADAPTER_20261022_RESULT.md) and [P24 preregistered proof obligations](P24_PROPERTY_SECTION6_CONDITIONS_PROOF_PRECOMMIT.md).

## 1. Revision-first verdict

**YES: the locked September Property manuscript needs targeted correction.** The audit identifies **three substantive source-locus problems**; two consequential repeated claims and a dependent embedding definition must be repaired, while the central PI/PII axioms, the literal Stage-VI interface, and C1 completion inverse laws do **not** require redesign on this evidence.

| Status | Source | Printed page | Problem | Necessary action |
| --- | --- | ---: | --- | --- |
| REQUIRED / definition-domain repair | Definition 6.1 (F3–F5) | 13 | Quantifies over all \(\varpi\in\Pi_A\) even when source profile unavailable; \(X_{A,\varpi}\), its product map and primitive coordinates need not exist by Defs2.4–2.5 | Explicit \(\varpi\in\Pi_A\) **and** available source profile guard for F3–F5; F1 supplies target availability |
| REQUIRED / dependent coherence | Definition 6.3 | 13 | “for every source input” tacitly uses absent \(X_{A,\varpi}\) for source-declared/unavailable kinds | Same guard before all membership reflections |
| REQUIRED / incorrect equivalence shorthand | Theorem 6.8 statement+proof | 14 | A bijective *embedding* need not match **availability sets S2** or **declaration sets S3**; as written theorem asserts too large a strict-isomorphism class | Correct equivalence to bijective embeddings with S2,S3; explicitly prove S4 from them |
| REQUIRED / proof qualification | Theorem 4.3 statement and one proof sentence | 11 | “relative to Definitional Closure C1” despite countermodels violating PI or PII; original C1 starts from an admitted primitive property core | Restrict independence claim to **shared typed premodels**; C1 is applied only on admitted cores |
| REQUIRED / downstream repeats | Abstract and Theorem 11.1 item (7) | 1,19 | Repeat bijective-embedding equivalence without S2,S3 | Correct phrase in both |
| RECOMMENDED / proof and scope clarification | Proposition6.2, Definition2.5 | 13,7–8 | Identity/composition proof needs source-profile guard explicitly; Def2.5's numbered subitems could be clearer about scope | 1–2 clarifying sentences; no new axiom |

**Already preserved by minimum repair:** PI and PII core axioms, admissible model and completion inverse laws, formation Stage-VI five-coordinate channel identity, values and conditional undefinedness, first-branching theorem after strict comparison corrected, and the equivalence relation conclusion (with corrected proof). Preservation of downstream conclusions is subject to the correct underlying definitions; no global independent proof of the entire paper is claimed.

## 2. Proof defect A: source profile unavailable

Property Def2.3 supplies a **partial** auxiliary carrier map. Def2.4 declares \(X_{A,\varpi}=\prod_r X_A(s_r)\) only if each profile sort is available. Def2.5 allows a declared kind with unavailable profile and says no applicability/prerequisite/assignment coordinates are required.

Choose shared signature with sort \(u\) and candidate kind \(k\), profile \((u)\). Choose an admissible \(A\) with \(k\in\Pi_A\), \(u\notin\mathrm{Dom}(X^{aux}_A)\), and no primitive k-coordinates. PI/PII hold vacuously. Original Definition6.1 asks to interpret \(\phi_k:X_{A,k}\to X_{B,k}\) for every \(k\in\Pi_A\), but \(X_{A,k}\) is undefined. In particular, the printed identity-map argument of Proposition6.2 cannot be applied to this valid \(A\) without a source-availability guard. This is a **well-formedness/domain defect**, not a counterexample to an adequately guarded category theorem. Replacing undefined by empty product is invalid: available empty carrier is itself a separately permitted case.

Let \(G_A(k):=k\in\Pi_A\land \operatorname{Available}_A(k)\). Interpret F3–F5 and embedding reflections *only* on kinds with \(G_A(k)\). F1 gives availability in \(B\), because inherited sorts are fixed and each auxiliary sort supplied in \(A\) is supplied in \(B\). Therefore all \(\phi_k\) and reflected primitive data used in these clauses are well defined. Identity maps and composable maps preserve F1,F2 and the source guard. For \(A\xrightarrow{\Phi}B\xrightarrow{\Psi}C\), if \(G_A(k)\), then \(G_B(k)\) by F1+F2 and \(G_C(k)\) similarly. The induced product map satisfies \((\psi\circ\phi)_k=\psi_k\circ\phi_k\). Image inclusions and assignment-value equalities compose pointwise. Thus identity and composition laws, and the embedding subcategory laws using reflected predicates, follow under the repaired quantification. No need to alter PI,PII, or formation source.

## 3. Proof defect B: S2 and S3 are not forced by a bijective embedding

The source strict Definition6.7 requires S1 carrier bijections, S2 **equal sets of available auxiliary sorts**, S3 **equal declared property kinds**, and S4 inverse-direction embedding. Original Theorem6.8 says instead simply “exactly the bijective property embeddings”. Two independent typed full-model counterexamples disprove that implication as printed.

**S2 finite countermodel:** Let both property declaration sets be empty. \(A\) supplies no auxiliary sort, \(B\) supplies \(u=\{b\}\). The empty family of available source carrier maps is vacuously a bijection family; F1,F2 and all embedding source-kind clauses hold. Yet \(\mathrm{Dom}(X^{aux}_A)=\varnothing\ne\{u\}=\mathrm{Dom}(X^{aux}_B)\). Not strict by S2.

**S3 finite countermodel:** Supply one singleton \(u\) in both A,B and its bijection \(a\mapsto b\). \(\Pi_A=\varnothing\) but \(\Pi_B=\{k\}\) with valid empty applicability, prerequisite and assignment coordinates over \(u\). Source-empty declarations make F2/F3–F5/reflection vacuous; the carrier bijection makes the forward map a bijective property embedding. S3 fails, so it is not strict.

**Corrected characterization and general set-theoretic argument:** A strict isomorphism is precisely an embedding whose source-available carrier maps are bijections, whose two availability sets agree, and whose declaration sets agree. The conditions S1–S3 make product maps bijections for every common **available** kind (inherited sorts are fixed identities). Embedding's three membership **biconditionals** hold for all source product elements. For any target element choose the unique inverse preimage and substitute into the biconditional, yielding the required inverse reflection. Assignment-value equality likewise reverses on reflected domains. Hence inverse maps satisfy forward map and embedding axioms. There are no product-map conditions for kinds unavailable on either side, given S2. Thus S4 follows *given* S1–S3 **and** a property embedding. Composition, identity and inverse preserve all these properties, establishing the equivalence-relation portion of Th6.8. S4 has not been silently dropped from source Definition6.7; the amended theorem proves it under the more precise hypothesis.

## 4. Proof-scope defect C: Theorem 4.3

Original Theorem4.3 claims mutual non-derivability “relative to the shared typed background and Definitional Closure Clause C1.” Yet source C1 explicitly begins “Given a primitive property core” and Def2.6 defines a core as a typed premodel satisfying both PI and PII. Source Countermodels 4.1/4.2 are typed premodels violating one axiom and therefore **not** primitive cores. They cannot simultaneously be witnesses inside a class which already requires both axioms.

The original countermodels *do* prove PI/PII mutual nonderivability **relative to typed premodel requirements alone**. The statement should be revised to that domain, with one explanatory proof line that C1 remains a separate conditional definitional completion on admitted cores. This preserves original theorem's genuine result while removing misleading C1 relativity. The later original Theorem11.1 item (3) already says relative to typed background and needs no mathematical content change.

## 5. Dependency map and proposed exact EN/KR manuscript edits

[Section-by-section English replacement text with Korean 1:1 semantic check](P24_PROPERTY_PAPER_SECTION_PATCH_EN_KR_DRAFT.md) is supplied as a separate reviewable edit proposal, not silently applied to the manuscript.

- \`§6.1 Def6.1 F3/F4/F5\` — source kind declared + available guard.
- \`§6.1 Prop6.2 proof\` — explicit identity/composition guard.
- \`§6.2 Def6.3\` — same source-available guard in embedding reflection.
- \`§6.3 Th6.8 theorem+proof\` — S1/S2/S3, prove S4.
- \`§4.2 Th4.3 theorem+scope proof sentence\` — typed premodel background, not C1 admissibility.
- \`Abstract\` and \`§11 Th11.1(7)\` — exact strict-isomorphism characterization.
- \`§7 stage comparison, §6.4 representation lift, §11 and discussion\` — wording/dependency review required after editing, but no additional independent contradiction demonstrated in P24.
- \`Formation v4.5 Stage VI, Property C1 Theorem3.7\` — unchanged by this patch.

## 6. Independent finite regression, archive and limitations

The [independent P24 Python script](scripts/verify_p24_paper_change_countermodels.py) uses a shared typed signature and explicitly admitted full property models to exercise unavailable-but-declared kinds, available empty sorts, unguarded-vs-guarded identity and forward maps, the independent S2/S3 countermodels, corrected strict identity/symmetry/composition, source PI/PII typed-premodel countermodels, and value-preservation negative controls.

- **32/32 expected finite observations** pass both Python 3.10 and 3.12.
- First [GitHub Actions #40188230726](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40188230726) success; both detailed JSONs matched.
- After exact JSON was committed, [GitHub Actions #40188274666](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40188274666) success for both versions, reporting \`P24 ARCHIVED FULL JSON REPLAY EXACT\`. [Archived JSON](results/p24_paper_change_countermodels.json).
- PDF SHA256 values were independently recomputed from the supplied binary files. Relevant printed pages 7–8, 11–14, 19–20 were directly rendered/inspected.
- **Finite examples do not replace the general algebraic argument in §§2–4 above**; that argument is conditional on the original fixed Stage-VI, shared signature, and well-typed model assumptions.
- Original manuscript source/bilingual TeX, PDF, Zenodo, all earlier scripts, their CI and their results were **not modified**.

## 7. Final assessment and publication implications

\`\`\`text
P24: EXECUTED / ORIGINAL_PAPER_REVISION_NECESSARY
ESSENTIAL_SOURCE_LOCUS_1: DEF6.1_GUARD_F3_F4_F5
ESSENTIAL_SOURCE_LOCUS_2: THEOREM6.8_STRICT_ISOMORPHISM_S2_S3
ESSENTIAL_SOURCE_LOCUS_3: THEOREM4.3_C1_RELATIVITY
DEPENDENT_FIXES: DEF6.3 + ABSTRACT + TH11.1(7)
RECOMMENDED_CLARIFICATION: PROP6.2 + DEF2.5
32_EXPECTED_FINITE_OBSERVATIONS: PASS_ON_PYTHON_3_10_AND_3_12
FINAL_ARCHIVE_REPLAY: PASS_ACTIONS_40188274666
SOURCE_SECTION6_TWO_GAPS: IDENTIFIED_WITH_PROPOSED_REPAIR / PRINTED_PDF_STILL_OPEN
SOURCE_THEOREM4_3: TARGETED_REPAIR_PROPOSED / PRINTED_PDF_STILL_OPEN
FULL_PROPERTY_FPA: OPEN
FULL_FORMATION_FPA: OPEN
AUTHOR_PDF_TEX_ZENODO: UNCHANGED
NEXT: P25_AUTHOR_SOURCE_REVISION_SCOPE_AND_EN_KR_BUILD_AUDIT / NOT_EXECUTED
\`\`\`
