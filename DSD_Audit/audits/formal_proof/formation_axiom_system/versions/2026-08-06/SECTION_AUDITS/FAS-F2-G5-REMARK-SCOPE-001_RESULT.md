# FAS-F2-G5-REMARK-SCOPE-001 — Five original explanatory Remarks, exact source-bound audit

**2026-10-21 KST · Author Kwon Dominicus · Formal Proof Audit v0.1 · No new theorem claimed.**

## 1. Source lock and prospective evidence

- Original manuscript: \`DSD_Formation_Axiom_System_EN(5).pdf\`, 33 pages, directly inspected via \`pdftotext -layout\` and PyMuPDF exact page headings. SHA256: \`8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a\`.
- Original numbered Remarks: **3.1 p7, 3.2 p7, 3.4 p9, 6.9 p18, 6.13 p20**. These five were previously either context-cited (3.4) or lacked a distinct labelled-item audit (3.1, 3.2, 6.9, 6.13).
- Precommitted obligation file: [FAS-F2-G5-REMARK-SCOPE-001_PRECOMMIT.md](FAS-F2-G5-REMARK-SCOPE-001_PRECOMMIT.md), commit \`51fcc997ffed73cac9b212518c8691f01e52137\`, before current selected finite execution.
- Standard-library [actually executed Python](../scripts/verify_g5_remark_scope.py), commit \`5a7b109ab6ad1a90d71baf7cd47bfa4c6a6bff49\`, **SHA256 \`7530f501388002021341662095adf1970a321f1bba7c9b280c6bbaf16b90568e\`**, Git blob \`5ba98739b6260d307e4c7596158bf186839cefa8\`, **6,607 bytes**. Actual local/GitHub code blob identity rechecked.
- [Exactly generated local JSON uploaded to GitHub](../results/g5_remark_scope.json), commit \`fdadf2e39de524ffdedbfecb3cfe0ab784e8bd00\`, **SHA256 \`8ad93dbe58e8eb040187a1b10a8691de1d4695d24ba3290512c3210180e5cb37\`**, Git blob \`51c2fa9918a52224c1d83d3826817f50247a2dc7\`, **1,453 bytes**. Git blob is byte-identical to locally emitted JSON.
- Command executed: \`python -W error -m py_compile .../verify_g5_remark_scope.py\` and \`python -W error .../verify_g5_remark_scope.py\`, both successful.
- All source propositions, lemmas and axioms remain independently classified. A Remark review is a **source explanation/scope audit**, not a new mathematical theorem certification.

## 2. Source statements and independent reasoning

### Remark 3.1 — Distinct scopes of Axioms I and II (source p7)

**Original assertion:** I governs expression describability on the entire candidate expression carrier; II separately requires sound targets for the \`Res\` relation and identity restrictions for admitted expressions. Neither primitive axiom replaces the other.

- I: \`Des_expr(x) => Adm_expr(x)\`, for every candidate expression.
- II: for \`Res(H,h)\`, typing/sound inheritance and \`Adm_expr(h)\`; for each admitted H, \`Res(H,H)\`; it does not require that every Des expression be admitted merely from the *Des* predicate.
- Relative independence examples: take one candidate x, Des empty and Adm={x}, but no Res identity. I holds while II fails. Conversely Des={x}, Adm empty and Res empty: II's identity/target requirements hold vacuously and I fails.
- **Critical scope boundary:** neither example is a full original Formation model satisfying *both* I and II. They are appropriately typed interpretations showing the candidate axiom's non-implication. The full system simultaneously imposes both.
- **Verdict:** SOURCE_EXPLANATION_ALIGNED. No amendment needed.

### Remark 3.2 — Identity restriction (source p7)

**Original assertion:** the witness \`H=h\` is permitted in Clause IV, because II requires identity \`Res(h,h)\` for admitted expressions; the core does not require proper strict restriction.

- Given a candidate \`p\` and \`Des_expr(h)\`, I implies \`Adm_expr(h)\`; II then gives \`Res(h,h)\`. Thus whenever \`Realize(h,p)\` and **all three configuration flags** (\`Adm_cfg\`, LC, BC) hold, the \`(h,h)\` pair satisfies the restriction/realization witness part and \`Psi(p)\` is true.
- Without \`Realize(h,p)\`, or with any flag false, an identity restriction alone does **not** make \`p\` describable. This is an independent direct Clause-IV observation.
- **Verdict:** SOURCE_EXPLANATION_ALIGNED_WITH_WITNESS_SCOPE. No manuscript correction; do not export the strengthened false reading.

### Remark 3.4 — Model-class status of primitive-reduct characterization (source p9)

**Original assertion:** original Theorem 3.3 identifies primitive reducts of full Formation models exactly with typed primitive Formation cores.

- For typed primitive data satisfying I–III,V, Clause IV deterministically defines \`Des_cfg,Psi,K_des,A*=A\`; Stage V globally supplied q determines local graphs; Clause VI determines C; Clause VII determines the **finite set** domain and Comp **relative to separately supplied term vector space W and map T:C→W**. The original says "relative to these supplied post-Stage-VI data", so no global uniqueness of W or T from the primitive core is claimed.
- The converse is definitional: a full model's primitive reduct satisfies I–III,V, hence is a primitive Formation core. This is a model-class characterization **in the present typed set-theoretic setting**, not a metatheorem of logical completeness or independence from all external mathematical background.
- Direct fixture: keep primitive data identical, fix term T(c)=1 twice and receive the same derived closure twice; choose instead T(c)=2 and the finite component sum changes while the primitive reduct / determined C are unchanged. Thus an overstrong interpretation "primitive data uniquely determine all term values" fails, but it is **not** the original Remark.
- **Verdict:** SOURCE_EXPLANATION_ALIGNED_WITH_RELATIVE_UNIQUENESS. No correction.

### Remark 6.9 — Induced subsets need not be submodels (source p18)

**Original assertion:** arbitrary induced subsets are not automatically Formation submodels. Dropping every witness of a retained configuration may alter Psi; retaining assigned items not in the new A* may violate V. Definition 6.4's full-model and witness-reflection requirements protect these properties.

- Original full single-expression/single-configuration witness with material item a, admitted/describable h, \`Res(h,h)\`, \`Realize(h,p)\`, all three gates true, \`act(p)={a}\`, and regime-global q(a)=0 has \`Psi(p)=true\`, \`A*={a}\`, and a valid assignment Q={a}. All anchors constant to one external support and internal material record empty.
- Choose a retained configuration p but remove all witness expressions. If Q is also removed, the induced primitive data can still be a full Formation model with \`Psi(p)=false\`, but its inclusion into the original model **fails witness reflection**: target \`Psi(p)=true\` while the retained model has false. Other embedding reflection requirements such as assignments may also fail; the counterexample does not claim witness reflection is the only obstruction.
- Alternatively retain the old q(a)=0 while removing witnesses. Then new \`A*=empty\` yet Q={a}; Primitive V requires \`Q⊆A*\` and fails. That induced record is **not** a legal full Formation model and hence cannot be a Formation submodel.
- These are **existential counterexamples to automatic submodel status**, not claims that no properly closed induced submodels exist. Definition 6.4 also specifies R1–R5 and independent witness reflection; satisfying only material subset relationships is insufficient.
- **Verdict:** SOURCE_EXPLANATION_ALIGNED. No correction.

### Remark 6.13 — Base fixing (source p20)

**Original assertion:** strict base-fixed comparison preserves material-record structure and the support of retained material items. Internal coordinate names may change provided the anchored base structure is preserved.

- Interpret relative to the original **strict base-fixed Definition 6.10, condition E1**: \`Phi_M\` is an isomorphism of material-record structures with the external support \`Supp(B)\` fixed. Thus material labels themselves may differ; the induced incidence and anchors must commute with the material bijection and **external support is not relabelled**.
- Example: source a,b carry external anchor labels N,S respectively and a→b incidence; target x,y carry N,S respectively and x→y incidence. The material bijection a→x,b→y preserves anchored structure despite distinct internal names. Swapping the images a→y,b→x while keeping target external anchors N,S fixed fails, and the reversed oriented incidence also fails.
- This Remark does **not** authorize arbitrary renaming of anchor targets or a change in external base B, nor a guarantee that every coordinate permutation preserves the full structure. It is correctly confined to source strict comparisons, not all forward maps.
- **Verdict:** SOURCE_EXPLANATION_ALIGNED_WITH_E1_SCOPE. No correction.

## 3. Computation, what it establishes, and what it does not

Five selected finite scenario suites, **19 recorded assertion/result flags**, passed:

\`\`\`json
{"assertions": 19, "outcome": "ALL_SELECTED_FIXTURES_PASS", "remarks_tested": 5}
\`\`\`

The 19 flags are **not 19 distinct theorems or an exhaustive search over all Formation models**. Primitive-axiom independence tests are intentionally *single-axiom* typed interpretations, not models of the full conjunction; the submodel test separately distinguishes a valid but nonembedding reduced Formation model from a reduction that violates Axiom V. The proof of relative uniqueness is based on the source's deterministic definitions, not finite enumeration; the computer examples demonstrate boundary behavior.

**Windows 11 command** (from existing cloned \`DSD_Method_Family\` repository root):

\`\`\`powershell
python .\\DSD_Audit\\audits\\formal_proof\\formation_axiom_system\\scripts\\verify_g5_remark_scope.py
\`\`\`

Default generated JSON (existing repo-relative path): \`DSD_Audit/audits/formal_proof/formation_axiom_system/results/g5_remark_scope.json\`. Optional first positional argument selects another JSON path. Standard-library only. No new location convention created.

## 4. Final per-item and full-paper gate

\`\`\`text
AUDIT_CASE: FAS-F2-G5-REMARK-SCOPE-001
REMARK_3_1: SOURCE_EXPLANATION_ALIGNED
REMARK_3_2: SOURCE_EXPLANATION_ALIGNED_WITH_WITNESS_SCOPE
REMARK_3_4: SOURCE_EXPLANATION_ALIGNED_WITH_RELATIVE_UNIQUENESS
REMARK_6_9: SOURCE_EXPLANATION_ALIGNED
REMARK_6_13: SOURCE_EXPLANATION_ALIGNED_WITH_E1_SCOPE
MATHEMATICAL_VERDICT: SOURCE_REMARK_SCOPES_ALIGNED_WITH_DECLARED_BACKGROUND (source-prose review, not new theorem proof)
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE (these five Remarks as written)
ORIGINAL_NUMBERED_SOURCE_ITEMS: 69
MATH_CLAIM_OR_COUNTERMODEL_SOURCE_AUDITS: 52 / 52
DEFINITION_TYPED_REVIEWS: 12 / 12
REMARK_PROSE_AUDITS: 5 / 5
FULL_F2_MANUSCRIPT_FPA: OPEN
INDEPENDENT_EXTERNAL_VALIDATION: not_established
ORIGINAL_PDF_ZENODO: unchanged
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22 / 22 unchanged
NEXT: FAS-F2-G6-REVISION-SCOPE-001 / NOT_STARTED
\`\`\`

**Outstanding independent manuscript-source issues NOT changed:** Theorem 4.7 six residual constraints' comparison against "other primitive axioms" needs a clarified relative residual framework; original §7.3 D2 exposure/boundary conditions need clarification; §8 Discussion's unqualified "strictly weaker" relation under fixed J was found overstrong in prior source audit; Proposition 5.13's blanket channel-membership loss reading requires conditional scope. These should be reconciled in a dedicated G6 revision-scope audit before any full-F2 closure. The 69 original numbered headings now have attached source-bound audit evidence, but this does not automatically close the manuscript-wide dependency graph or constitute formal machine proof / external independent verification.


**Reciprocal Notion case:** https://app.notion.com/p/40081f51e7fa81b3adeedb76f41eaf3c
