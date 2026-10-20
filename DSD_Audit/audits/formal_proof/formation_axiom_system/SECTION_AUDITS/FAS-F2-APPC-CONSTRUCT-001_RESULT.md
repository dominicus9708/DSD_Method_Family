# FAS-F2-APPC-CONSTRUCT-001 — Appendix C finite-construction / witness reconstruction FPA

**2026-10-20 KST · Source-bound FPA v0.1 · Original Appendix C, printed pp.31–32 (33-page PDF).**

## Frozen source, execution provenance, independent status

- AUTHOR: Kwon Dominicus
- PDF: \`DSD_Formation_Axiom_System_EN(5).pdf\`
- PDF SHA256: \`8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a\`
- ORIGINAL SOURCE: Appendix C *Finite-Construction and Witness Reconstruction Protocol* (printed pp31–32), with Section 7.2 Theorem 7.3 and Section 7.4 synthetic 3×3 witness as source references.
- PROSPECTIVE PRECOMMIT: \`45543bb9c77dad8c00f409d84bd7dbef298e5008\`, [precommit](FAS-F2-APPC-CONSTRUCT-001_PRECOMMIT.md), made before executing new selected fixtures.
- EXECUTED SCRIPT COMMIT: \`277daa1bab10b86c8887f901afbfe042c5ef71a4\`
- EXECUTED SCRIPT SHA256: \`0bef9402c69b27deaee2020d93d2baebd7e80693e2dab253e41877c437d2756c\`, bytes: 4386, git blob \`3959544bedf234a5f3510d86fbd3aecdfc286b1e\`
- DETERMINISTIC JSON COMMIT: \`17bddca50c0e0313eb6a3038f43800fe66701653\`
- JSON SHA256: \`3eb4c9c1db8bdcb4919f15afdbb949b6caf1236881c1d82180d640fa24466445\`, bytes: 2289, git blob \`bf0bf1a27e4cfc965dfc7eee8bc8e660f514cc2f\`
- Script and JSON GitHub blobs checked against exact local executed bytes.
- MATHEMATICAL_VERDICT: \`SOURCE_CONSTRUCTION_PROTOCOL_ALIGNED_WITH_DECLARED_FINITE_MODELS\`
- DSD_AUDIT_VERDICT: \`PASS_WITH_BOUNDARY\`
- REVISION_NEED: \`NONE\` **for Appendix C itself**
- INDEPENDENT_EXTERNAL_VALIDATION: \`not_established\`
- FULL_F2_MANUSCRIPT_FPA: \`OPEN\`
- ORIGINAL_PDF_ZENODO: \`unchanged\`
- METHOD_FAMILY_INTERNAL_STANDARDIZATION: \`22/22 unchanged\`

## 1. General standard realization: independent source-typed reasoning

Theorem 7.3 assumes a finite relational material record M with carrier M, one anchor alpha:M→Supp(B), finite quantity and role kinds Lambda and R, supplied pointed value carriers, assignment domains D_lambda⊆M and one regime-global q_lambda:D_lambda→V_lambda, plus *typed* role seed R0⊆P(M)×M×Lambda×R with a∈A∩D_lambda for every (A,a,lambda,rho)∈R0.

Construct distinct e_A and p_A for each A⊆M with mat(e_A)=act(p_A)=A and anchors alpha|A. Endow each retained subset with its induced relational material record. Declare all expressions admitted and describable. Put Res(e_A,e_B) and Realize(e_A,p_B) **iff B⊆A**. Declare all three configuration gates true. For each p_A, (e_A,e_A,p_A) supplies the complete configuration witness. Thus K_des={p_A:A⊆M} and A*=A_L=M, even when M=empty (there is the empty-subset configuration, while A*=empty).

Under source role typing, q is well-defined for every selected role tuple. Definition/Closure VI yields exactly
\`C_L={(p_A,a,lambda,q_lambda(a),rho):(A,a,lambda,rho)∈R0}\`.
The map from the role-seed tuples to operational channels is one-to-one (coordinates A,a,lambda,rho are retained). W_L is the **free F-vector space on finite C_L** (zero vector space for C_L empty), and T_L(c)=e_c is post-Stage-VI supplied term data; Clause VII then gives finite sets and sums. Primitive I, II, III and V hold because all expressions are admitted, subset restriction and realization preserve anchors/material records and identity restrictions, and D_lambda⊆M=A*. No additional restriction transitivity axiom is needed even though this particular constructed model happens to have a transitive subset restriction.

All carriers, expression and configuration families and C_L are finite; the value carriers and F may remain infinite and formation-finiteness is still satisfied. The result is relative to the **stated typing** of the role seed and relational material records; it is not a statement that *arbitrary untyped* assignment/role inputs admit such a model.

Selected Python fixtures: for n=0,1,2,3,4 with sparse/dense legal global assignment domains, total 10/10 executed without assertions; includes empty material, empty role and no-channel term-space boundary. Invalid role seed a∉A∩D_lambda deliberately rejected. The fixtures test only selected data; the general conclusion rests on the preceding source-level all-A argument.

## 2. Original indexed 3×3 reconstruction, exact scope

Let X be a 3×3 nine-site set; the index i(S)=sum_{(r,c)∈S}2^(3r+c) ranges over all 512 site subsets. For every i, the source introduces three **private typed** carrier items a_i^H,V,D and three primitive role relations common to both regimes. Both regimes have 512 describable p_i, the same primitive Stage-0–4 data, and one regime-global assignment q.

- LG assigns all three carriers for every i, values (1,1,-2), giving 1536 channels and **all 512 full-family composite sums zero**.
- LH locally assigns H,V,D at i=0..124 (125 indices); only V at 125..186 (62); only H at 187..505 (319); H,V at 506..511 (6). These four channel subtotal counts are **375,62,319,12**, sum **768**.
- LH values for i<125 are (1,1,-2); all locally assigned LH values for 125≤i<252 are 0; all locally assigned LH values for 252≤i<512 are 1.
- Full-family LH sum distribution: zero 252 (125 common structure + 127 differing structure), one 254, two 6.
- Exact identical channel-role structure: 125. Different: 387. Vertical without horizontal in LH: 62. Fixed J=id_R full-family scalar coincidences among **different** channel structures: **127** (i=125..251); all-index coincidences 252.
- Global Stage-V assignment domains: |Q_LH|=768, |Q_LG|=1536. Section 7.4's identity comparison survives through Stage 4; an E5-reflecting Stage-5 material bijection would require equal finite assignment-domain sizes, impossible. Thus the declared first-branch b=5 is justified; the Python count by itself is not a generic theorem about any arbitrary model.

The reconstructed exhaustive 512-case table is exhaustive **only for the fixed source i(S) indexing and its stipulated role, domain, and value rules**; it is explicitly NOT an enumeration of all possible 3×3 DSD formation rules. Channel identity is the operational five-tuple, not multiplicity of Res/Realize witness histories. The coincidences use full admitted channel families F_L,i, not chosen partial subfamilies.

## 3. Computational provenance and reproducibility scope

- [Exact locally executed script](../scripts/verify_appc_construction.py)
- [Exact deterministic output JSON](../results/appc_construction.json)
- Executed \`python -W error -m py_compile\` and \`python -W error\` followed by SHA256 and git-blob hash comparisons.
- Script manually reconstructs the source rules; it does not parse the source PDF or implement a general logical proof calculus. There are 10 selected ordinary finite model fixtures, the explicit invalid seed guard, and all 512 *specified* synthetic indices.
- This is project-internal source-bound validation, not an external independent reproduction or formal machine proof.

Windows 11, from the cloned repository root:

\`\`\`powershell
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_appc_construction.py
\`\`\`

Output by default: \`DSD_Audit/audits/formal_proof/formation_axiom_system/results/appc_construction.json\`. Optional first command-line argument is an alternative output path.

## 4. Boundary verdict and outstanding historical issues

C01–C10 precommitted scope obligations reviewed. No Appendix C internal source/procedure contradiction found and no newly necessary manuscript correction in Appendix C. Earlier distinct advisories remain open: T4.7 residual-six scope wording, Section 7.3 D2 boundary inheritance/exposed marker clarification, and Section 8 Discussion's unqualified fixed-J “strictly weaker” comparison (contradicted by a previously constructed strict-isomorphism/J counterexample). Appendix C does **not** resolve or negate those findings.

**MATHEMATICAL_VERDICT: SOURCE_CONSTRUCTION_PROTOCOL_ALIGNED_WITH_DECLARED_FINITE_MODELS. DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY. REVISION_NEED: NONE (Appendix C).**

Prior counts remain **14 named theorem audits / 2 proposition audits / 9 corollary audits**. Separately audited original unnumbered sections/appendices increase from six to **seven**: §7.3, §7.4, §8, §9, Appendix A, Appendix B, **Appendix C**. The whole F2 remains OPEN and independent outside validation unestablished; underlying original PDF/Zenodo unchanged.

**NEXT NOT_STARTED:** \`FAS-F2-APPD-RESTRICT-001\` — original Appendix D *Optional Restriction Coherence Extension*, requiring a new prospective precommit. Do not count its optional transitivity as a primitive core axiom.
