# FAS-F2-C7.4-001 — Arbitrarily large finite formation types / 임의로 큰 유한 형성 유형

**2026-10-20 KST · Source-bound DSD Audit / Formal Proof Audit v0.1 · A single original corollary, not a whole-paper certificate**

\`\`\`text
AUDIT_CASE: FAS-F2-C7.4-001
SOURCE: Kwon Dominicus, DSD_Formation_Axiom_System_EN(5).pdf, 33 pages
SOURCE_PDF_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
SOURCE_LOCUS: §7.2, Corollary 7.4, printed p.25
PRECOMMIT_COMMIT: ba241da61811d6455d442cf7d12188a302c15ab1
EXECUTED_PYTHON_COMMIT: 72784a9285972a50e6c4a87dd278f34022455510
EXECUTED_PYTHON_SHA256: 882c27ed0815477103befd208eba65461abe67eb78632b46cbc38bd09f53013a
EXECUTED_PYTHON_GIT_BLOB_SHA: eea7e91d616c2c4d85f600160b4da737a9561562
EXECUTED_JSON_COMMIT: 29e999990ef537bcc6c4d1a7ab0975fd5a468e2d
EXECUTED_JSON_SHA256: 4a94a05bf7ac8ce5fbd7ba7a3ed634deaa38896b6d38f0f0c3dd8852c150a8fe
EXECUTED_JSON_GIT_BLOB_SHA: 02354094d8db36af7a9609520e2b31781fd69e6e
MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE
F2_FULL_MANUSCRIPT_FPA: OPEN
EXTERNAL_INDEPENDENT_VALIDATION: not_established
SOURCE_PDF_ZENODO: unchanged
DSD_METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged
NEXT: FAS-F2-SEC7.3-D2-001 / NOT_STARTED
\`\`\`

## 1. Frozen exact claim, source and dependencies

The attached English source at §7.2 p.25 reads:

> **Corollary 7.4 (Arbitrarily large finite formation types).** For every integer n ≥ 1, there is a formation-finite full model with |M_B^L| = n. Hence the axiom system has arbitrarily large pairwise non-isomorphic formation-finite models. The construction also permits arbitrary finite partial-assignment and role data subject only to the stated typing condition.

The immediately preceding **Theorem 7.3**, independently audited in case FAS-F2-T7.3-001, is the explicit source construction from finite relational material data, anchored materials, finite kinds/roles, per-kind pointed sets and global partial assignments, and a finite role seed \`R0\` with \`a∈A∩Dλ\`. Definition 2.3 specifies **formation-finite**; Definition 6.10 makes bijectivity of the material map a necessary condition for strict base-fixed formation isomorphism.

The corollary asserts an **unbounded FAMILY of individual finite models**, not an infinite single formation-finite model, not all models having independent term vectors, and not a claim that an arbitrary invalid role seed is realizable.

## 2. Universal mathematical existence construction (ALL integers n≥1)

Fix a field F and a single base B whose support contains at least one point s; for example, take \`F=F₂\` and a singleton-support set-coded B. Importantly, **the same B and F work for every n**. For arbitrary integer n≥1, let \`M_n={a_0,...,a_(n-1)}\`, use an empty material-relational signature (or any finite relational structure), and anchor **every** a_i to s via \`α_n(a_i)=s\`. This is allowed: source Axioms II/III require correct codomain and restricted anchors, **not injectivity**.

Choose one quantity-kind λ, one role ρ, the pointed singleton \`Vλ={0λ}\`, the full global assignment domain \`Dλ=M_n\`, \`qλ(a)=0λ\` for every a, and the finite valid seed

\`\`\`text
R0_n = {(M_n,a,λ,ρ): a∈M_n}.
\`\`\`

Every seed satisfies the source requirement \`a∈M_n∩Dλ\`. Apply Theorem 7.3 with **every subset \`A⊆M_n\`**, creating \`e_A\` and \`p_A\`, both retaining exactly A with anchor \`α_n|A\`, all required admission/coherence/boundary primitive inputs true, and subset inclusion Res/Realize. Then:

\`\`\`text
|M_B| = n
|E_B| = |P_B| = 2^n
K_des = {p_A : A⊆M_n}
A* = M_n
Qλ = Dλ = M_n
C = {(p_(M_n),a,λ,0λ,ρ):a∈M_n}; |C|=n
W = F^(C), T(c)=e_c, Dcomp=P(C), |Dcomp|=2^n.
\`\`\`

**Primitive I:** all expressions e_A describable/admitted. **Primitive II:** restrictions Res(e_A,e_Z) by inclusion Z⊆A inherit anchors and induced relational records, and every e_A has identity Res(e_A,e_A). **Primitive III:** realizations Realize(e_A,p_Z) have active Z⊆A and inherited anchors. **Closure IV:** every p_A has genuine witness \`(e_A,e_A)\`, giving K_des all configurations and A*=M_n. **Primitive V:** qλ is a single well-typed regime-global partial assignment on Qλ=M_n⊆A* and its zero values are **defined**. **Closure VI:** by exact role seed and well-typed assignment, C matches the above set, and each channel has a formation trace. **Clause VII:** after VI supply the free F-vector space \`F^(C)\` and its standard basis component map, then every finite family is composable and has a finite vector sum. This makes a FULL model under Definition 2.2.

**Formation-finite:** material, expression, configuration, quantity-kind, role, admitted-channel carriers and each assignment domain are finite for every individually fixed n. For example, although \`2^n\` grows without bound as n varies, it is finite for every finite n. The source Definition 2.3 does not impose finite cardinality on every pointed \`Vλ\` or the F-vector term space W. No extra cardinal bound on \`Supp(B)\` follows from a large n: a single support point suffices.

## 3. Pairwise nonisomorphism and exact strength

For distinct positive integers n≠m the material carriers \`M_n\` and \`M_m\` have different **finite** cardinalities. By Definition 6.10, a strict formation isomorphism would include a material bijection \`f_M:M_n→M_m\`; none exists. Consequently the source-indexed family is **pairwise non-strict-base-fixed-formation-isomorphic**, even though all descriptors have the **same B,F, kind and role cardinalities**. Any stronger, unqualified notion of isomorphism preserving the typed material sort likewise cannot identify carriers of unequal size; the proof does not purport to classify entirely unrelated comparison notions.

The logical form is:

\`\`\`text
∀n∈N (n≥1 ⇒ ∃L_n [Full(L_n)∧FormationFinite(L_n)∧|M(L_n)|=n])
and for these chosen L_n, n≠m ⇒ no typed strict isomorphism L_n≅L_m.
\`\`\`

This does **not** imply \`∃L [FormationFinite(L)∧|M(L)|=∞]\`, nor a single unbounded finite carrier, nor that equal-size full models must be isomorphic. The source's third sentence follows directly from the full Theorem 7.3: **arbitrary finite PARTIAL assignment domains/values** and finite role seeds are permitted **provided every seeded \`(A,a,λ,ρ)\` satisfies \`a∈A∩Dλ\`**, with the other stated typing conditions. The full-domain singleton-zero example above is only an existence witness, not a forced restriction on allowed finite data.

## 4. Hostile controls / limits of what was shown

- **Zero n:** Original Corollary7.4 starts at n≥1. Theorem7.3 also permits an empty M, but its existence is neither necessary nor a counterexample here.
- **Empty support:** Our fixed base has s∈Supp(B). Demanding a positive-sized material carrier anchored to an empty support cannot use this witness and violates its prerequisite, not the original existential claim.
- **Noninjective anchor:** Our family intentionally maps n different materials to one and the same s; the paper's primitive axiom typing permits this. Assuming injectivity would be an unauthorized added axiom.
- **Partial assignment:** Take any proper Dλ⊆M_n and qλ:Dλ→Vλ. The source construction remains valid when roles are seeded only on a∈A∩Dλ. Undefined q at some a is **not** an assignment qλ(a)=0λ.
- **Empty channels:** For R0=∅, the same full model construction admits zero channels and supplies zero-dimensional W, empty T, and one empty channel-family with composite 0.
- **Same-size countercontrol:** Two n=1 models with different assignment-domain cardinalities (Dλ=M versus Dλ=∅) need not be strict-isomorphic because Definition6.10 E5 fails; equal |M| alone is not a sufficiency theorem.
- **Free basis:** Free F-vector terms \`T(c)=e_c\` and composite family injectivity hold in this **standard** model, not every DSD Formation model.
- **Finite test scope:** selected n≤6 and finite pointed Vλ do NOT establish all n, arbitrary finite role patterns, arbitrary fields, or all possibly infinite pointed Vλ. Those follow mathematically from the source construction, not exhaustive software execution.

## 5. Executed selected finite test and exact files

Artifacts:
- [Prospectively frozen FPA plan](FAS-F2-C7.4-001_PRECOMMIT.md)
- [Locally executed and GitHub-matched Python](../scripts/verify_c74_arbitrarily_large_finite.py)
- [Locally executed and GitHub-matched deterministic JSON](../results/c74_arbitrarily_large_finite.json)

The actual standard-library Python was executed via \`python -W error\`, using **each n=1..6**, **two sample fields F₂ and Q**, two assignment/role patterns (full and valid partial), and an extra empty-domain/role case for n=1 in each field. The **26** selected source-typed full-model instances all passed. They derive all subset expressions/configurations, restriction/realization pairs, K_des/A*, exact global partial q, the role seed C=R0 correspondence, and the standard free-basis Clause VII composites.

| Quantity checked | Selected result |
|---|---:|
| Distinct n sampled | 6 (n=1..6) |
| Field samples | F₂ and Q |
| Source-typed full-model cases | **26** |
| Total admitted-channel occurrences | **66** |
| Total finite-channel families/composites | **310** |
| Material-cardinality unequal pairs per field, n∈{1..6} | **15** |
| Same-size domain-definedness non-equivalence guard | PASS |
| Original primitive/derived clauses and basis family injection | PASS for each fixture |

Exact local–GitHub **byte identity**, checked by Git blob SHA after upload/read-back:
\`\`\`text
PYTHON_BYTES=5745
PYTHON_SHA256=882c27ed0815477103befd208eba65461abe67eb78632b46cbc38bd09f53013a
PYTHON_GIT_BLOB_SHA=eea7e91d616c2c4d85f600160b4da737a9561562
JSON_BYTES=14665
JSON_SHA256=4a94a05bf7ac8ce5fbd7ba7a3ed634deaa38896b6d38f0f0c3dd8852c150a8fe
JSON_GIT_BLOB_SHA=02354094d8db36af7a9609520e2b31781fd69e6e
\`\`\`
This confirms the **exact committed code and JSON correspond to actually run local bytes**, but is not external independent replication. Finite checked cases are supplementary, **not** the general proof of arbitrarily large finite models.

**Windows 11 run command from cloned \`dominicus9708/DSD_Method_Family\` repo root:**
\`\`\`powershell
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_c74_arbitrarily_large_finite.py
\`\`\`
Output by default: \`DSD_Audit/audits/formal_proof/formation_axiom_system/results/c74_arbitrarily_large_finite.json\`. Optional first argument overrides.

## 6. FPA v0.1 gate verdicts

- G01 **PASS:** supplied source 33-page locked SHA, original §7.2 Corollary7.4 p25.
- G02 **PASS:** exact quantifier: each n≥1 admits its own formation-finite FULL model, not an infinite single formation-finite model.
- G03 **PASS:** anchored finite M_n over a fixed common B,F with noninjective α permitted, source Theorem7.3 prerequisites satisfied.
- G04 **PASS:** primitive I/II/III/V and derived IV/VI/VII follow from source's every-subset standard construction.
- G05 **PASS:** one-channel-per-valid-role seed in positive witness, |C_n|=n and 2^n composable finite families, with genuine witnesses.
- G06 **PASS:** pairwise no strict typed material bijection for n≠m; no assumption of equal cardinality sufficiency.
- G07 **PASS_WITH_BOUNDARY:** arbitrary legal finite partial q and role seed allowed only under original \`a∈A∩Dλ\` condition.
- G08 **PASS:** invalid empty support, n=0 outside statement, same-size different-domain comparison and C=∅ boundaries distinguished.
- G09 **PASS_WITH_BOUNDARY:** selected finite Python n≤6/F₂,Q is not universal n/field model proof.
- G10 **PASS:** finite E/P=2^n, no finite W or external Vλ restriction added; no universal free-basis requirement imposed.
- G11 **PASS_WITH_BOUNDARY:** following §7.3 fully specified formation-finite D2 early-branch model is unnumbered in source and remains a separate NOT_STARTED audit, as do other later sections. Historical optional T4.7 wording recommendation unchanged.
- G12 **PASS:** exact script and JSON Git blob matched local actually executed files; no external independent formal review established.

**MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND**
**DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY**
**REVISION_NEED: NONE**

The boundary is the original input typing, distinction between unbounded **finite model sizes** and an **infinite model**, and separation between general proof and selected tests; it is **not** a gap in source Corollary 7.4. Original PDF/Zenodo unchanged, 22/22 DSD Method Family internal standardization unchanged. Whole Formation F2 manuscript FPA still OPEN.

**Next bounded original source audit, NOT_STARTED:** \`FAS-F2-SEC7.3-D2-001\` — §7.3, “Fully specified formation-finite D2 early-branch model” (a source section, **not** an invented theorem label). Start with its own precommit.
