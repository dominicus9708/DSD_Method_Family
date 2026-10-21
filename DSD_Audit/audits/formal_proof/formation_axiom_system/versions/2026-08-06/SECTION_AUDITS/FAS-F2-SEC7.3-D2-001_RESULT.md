# FAS-F2-SEC7.3-D2-001 — Section 7.3 fully specified formation-finite D2 early-branch model

**2026-10-20 KST · Existing DSD Audit/FPA v0.1 · One unnumbered SOURCE SECTION (do not invent a theorem number)**

\`\`\`text
AUDIT_CASE: FAS-F2-SEC7.3-D2-001
AUTHOR: Kwon Dominicus
SOURCE: DSD_Formation_Axiom_System_EN(5).pdf (33 pages, supplied attachment)
SOURCE_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
SOURCE_LOCATION: original Section 7.3, printed pp.25–26
SOURCE_TITLE: Fully specified formation-finite D2 early-branch model
PRECOMMIT_COMMIT: 7e4d88b145e598a4ed5cdd7d100bc46997996a28
PYTHON_COMMIT: ed2cf28e1d153b01dba4784fd7f9aa57aed16da2
PYTHON_SHA256: 5c0782961bf41992f6247e7032fcbf3b6f103755a0b2e19dacb3691e9a070516
PYTHON_GIT_BLOB: 5949d6c21cab61c2194bbcd9dfcf0eaf058fc9b6
JSON_COMMIT: 9e5e6bcc87e2166dd3ca62d130d3889fc4202372
JSON_SHA256: f5da7b3a5e19ad93f669a9ec9ecc0045671080d79bc3d7cf664756e1966c837a
JSON_GIT_BLOB: b1fa5dcca82bf8f377f6027ef5c7dbd425a723a5
MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND
DSD_AUDIT_VERDICT: PASS_WITH_REFINEMENT
REVISION_NEED: CLARIFICATION
BRANCH_CLAIM: b(L+,L−)=3 verified
GEOMETRIC_BOUNDARY_COMPLETENESS: consistent completion exhibited; specific inherited annotation coding not exhaustively printed in source
SOURCE_PDF_ZENODO: unchanged
F2_WHOLE_MANUSCRIPT_FPA: OPEN
INDEPENDENT_EXTERNAL_VALIDATION: not established
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged
NEXT: FAS-F2-SEC7.4-3X3-001 / NOT_STARTED
\`\`\`

## 1. Frozen manuscript claims, and what is or is not claimed

Source §7.3 describes two **full formation-finite** regimes L+ and L− on a common 3×3 nearest-neighbor D2 grid with common typed material universe, material records and anchoring. Their expression/configuration and restriction/realization inputs are identical; the first independent distinction is **primitive boundary compatibility** of the same blocked-boundary candidate configuration p*. The asserted consequences are:
- \`K_des^+={p*}\`, \`K_des^−=∅\`.
- Positive regime q at exactly one internal edge item r* with value 1, one role and one admitted channel; negative regime empty q/Role/C.
- Both full models are strictly non-equivalent, with \`I2(L+,L−)≠∅\`, \`I3(L+,L−)=∅\`, and by source Definition6.15/Theorem6.16 **\`b(L+,L−)=3\`**.

The material geometry is a **finite witness**, not a theorem that geometry itself independently forces the boundary predicate. As explicitly established by the source Primitive Interface Convention (§2.2), **BC is supplied primitive regime input**, not a calculated dynamical function of geometry; the different BC outcomes are **chosen** according to the blocking policy. The example demonstrates the stage at which this primitive policy difference becomes a strict-isomorphism obstruction, not a derivation of a physical transmissivity law.

## 2. Concrete source-consistent finite completion, material counts and inherited data

The source states \`X_D2={0,1,2}×{0,1,2}\` with nearest-neighbor adjacency, **one vertex item per site**, **one undirected edge item per nearest-neighbor pair**, and **one potential boundary slot item for each site and cardinal direction**. A concrete typed implementation therefore uses:

\`\`\`text
|vertex items|=9; |undirected edge items|=12;
|potential (site,direction) boundary-slot items|=9×4=36;
|M_B|=57.
S*={(0,0),(1,0)}. The two sites are nearest neighbors.
h* retained items = 2 vertex items + 1 joining edge r*
                    + 6 exposed site-direction slots = 9 items.
H* full retained material = all 57 items.
p* active material = same 9 items as h*.
\`\`\`

Here the six slots are the directional incidences whose neighbor is **not in S***; boundary items remain **candidate slots** of the original 3×3 universe, including directions leaving the whole grid. The source does not explicitly enumerate the 57 items or the six subset-boundary slots, but they follow from its stipulated “one for each” conventions under the natural typed graph interpretation.

A concrete relational material-record signature can use a binary **incidence relation** connecting each edge item to its two endpoint vertex items and each slot item to its associated site vertex. Restrict it to retained tuples. Anchor each item to the correspondingly typed support (vertex, edge, boundary slot). The source permits precisely such induced relational substructures and external annotations (§2.2).

**Refinement boundary: inherited blocked boundary annotation.** The source says p* marks all six exposed boundary items **blocked**, and Primitive Axiom III requires the exposed boundary data of p* to be inherited from h*. Primitive Axiom II requires h* to inherit its records/annotations from H*. Yet source §7.3 does not separately print the full external boundary-annotation map on H* and h* or a rule specifying whether the “blocked” marker is inherited record or configuration-only metadata. The test therefore deliberately uses ONE *explicit consistent completion* of the source's general finite data: take a common external “blocked” annotation for the potential slot items in H*, then restrict that map to h* and p*; set \`BC^+(p*)=true\`, \`BC^−(p*)=false\` according to the supplied regime policies. This obeys II and III and does **not** alter the announced material/anchor geometry or the BC difference. Such annotations could be fixed with fewer values, but a completion choice should **not be silently mistaken for an exhaustively listed literal source record**.

**Coordinate naming boundary:** The source calls the internal edge joining (0,0) to (1,0) “horizontal.” In the customary **(row,column)** convention—made explicit by the later §7.4 label \`(r,c)\`—the same edge is **vertical** (first coordinate changes, second fixed). If §7.3 instead uses first coordinate horizontal, the name works. This does not change nearest-neighbor adjacency, the 57/9/6 counts, the inherited restricted structure or the proof of b=3. Recommended future clarification: call r* the **joining nearest-neighbor edge**, or stipulate the axis convention; do not silently transpose S* in the locked manuscript.

These are **source-specification clarifications**, not demonstrated inconsistencies or countermodels. A common, fully typed, axiom-compliant completion exists and preserves the main branching claim.

## 3. Primitive axioms and Closure IV, VI and VII

**Common source primitive data:** \`E={H*,h*}\`, \`P={p*}\`. Both admitted; h* describable; H* not explicitly declared describable, thus false under the source Section7 default (“undeclared primitive predicates false/empty”). Exactly
\`\`\`text
Res={(H*,h*),(H*,H*),(h*,h*)};
Realize={(h*,p*)}.
Adm_cfg(p*)=LC(p*)=true in both.
BC_+(p*)=true; BC_−(p*)=false.
\`\`\`

**Axiom I:** h* descriptive admission implies expression admission; H* admitted but not required describable.

**Axiom II:** All three Res pairs respect \`mat(h*)⊆mat(H*)\`, anchor restriction and induced material-incidence/boundary records. Both admitted expressions have their identity restrictions, H*→H* and h*→h*.

**Axiom III:** h*→p* has \`act(p*)=mat(h*)\`, equal inherited anchors, incidence and exposed blocked boundary metadata in the selected consistent completion.

**Closure IV:** In both regimes there are two valid expression-history pairs \`(H*,h*)\` and \`(h*,h*)\` linked to p* by the realization of h*. The only distinguishing conjunct in \`Ψ(p*)\` is BC:
\`\`\`text
Ψ_+(p*)=true, K_des^+={p*}, A*+=act(p*) (9 typed material items)
Ψ_−(p*)=false, K_des^−=∅, A*−=∅.
\`\`\`

**Primitive Axiom V:** Use common \`Λ={lambda_E}\`, pointed value space **R with zero 0**, \`Λδ=∅\`, common \`RoleCarrier={rho_H}\`. In L+, global partial assignment \`Q_+={r*}\`, \`q_+(r*)=1∈R\`. Since r* is an active item, \`Q_+⊆A*+\`. In L−, \`Q_−=∅\`, q− empty, so \`Q_−⊆A*−=∅\`. If one illegally copied L+'s nonempty q to original L−, Axiom V would FAIL; this is an invalid alternative, not a counterexample to the valid source model.

**Closure VI:** In L+ \`Role(p*,r*,lambda_E,rho_H)\` is true, q is defined at r*, and p* describable; hence exactly one admitted operational channel
\`\`\`text
c+=(p*,r*,lambda_E,1,rho_H), C+={c+}.
\`\`\`
L− has no describable config, no assignment or Role; \`C−=∅\`. **Channel absence is not a channel assigned term zero.** The source assigns Vλ=R, so its candidate universe U need not be finite; this does **not** violate Definition2.3's **formation-finite** criterion, which requires only finite material/expression/configuration/kind/role/admitted channel carriers and finite assignment domains. The finite code enumerates Γ-supported candidates for source exact channel inclusion, not all continuum many U tuples.

**Post-VI W and Closure VII:** Source chooses **W+=W−=R**, term \`T+(c+)=1\`, and T− the unique empty map. The source's finite-composition rule yields:
\`\`\`text
Dcomp+={∅,{c+}}; Comp+(∅)=0, Comp+({c+})=1.
Dcomp−={∅}; Comp−(∅)=0.
\`\`\`
Thus both are full **formation-finite** models under source Definition2.2/2.3. Neither the real W nor the real pointed value space is required finite; the model has only one or zero admitted channels.

## 4. Formal first-branch index: existential witness and universal failure

Definition6.15 stages are nested candidate comparison sets of typed carrier/kind/role/pointed zero-preserving bijections, with **J an arbitrary map W+→W− before Stage7** (a requirement of linear isomorphism appears only at Stage7). For these two descriptors the material-record structure, anchoring, expression/configuration/quantity/role/value-space carriers and maps are identical. Choose **identity bijections** on these sorts and identity J:R→R.

- **I0 nonempty:** identity tuple preserves anchored material data and the fixed base B, field F.
- **I1 nonempty:** expression Adm and Des predicates are identical.
- **I2 nonempty:** all three Res relations are identical and preserved/reflected.
- **I3 empty:** Stage3 requires Realize AND each of \`Adm_cfg\`, \`LC\`, \`BC\` preservation *and reflection*. The singleton p* in L+ must map to singleton p* in L− under **any** candidate configuration bijection. Yet \`BC_+(p*)=true\` and \`BC_−(p*)=false\`. Thus every possible typed tuple fails, irrespective of its material/expression maps or J; I3=∅.

Nestedness gives \`I4=I5=I6=I7=∅\`. By source Theorem6.16,
\`\`\`text
b(L+,L−)=min{k∈{0,...,7}:Ik=∅}=3.
\`\`\`
Both are **strictly non-isomorphic**. Since Stage4 is definitional from Stage3, this case does not contradict previously audited Theorem6.17 and Corollary6.18's exclusion of a first obstruction solely at Stage4. **The first failure precedes assignment q (Stage5), Role (Stage6) and term/composite preservation (Stage7)**, even though those inputs also differ.

**Counterfactual/hostile controls:** If one sets BC− true while keeping q−/Role− empty, the original same base and shared structure now permit identity comparisons through **I4**, but Stage5 fails due to \`|Q_+|=1≠0=|Q_−|\`: first branching would be b=5 for that modified otherwise legal model. If one instead gives the original BC-false L− a nonempty q, Axiom V is violated because A*−=∅. Swapping L+ and L− leaves BC disparity, so the branch is symmetric (consistent with source Theorem6.19).

## 5. Finite execution, exact GitHub byte identity, and limits

[Prospective precommit](FAS-F2-SEC7.3-D2-001_PRECOMMIT.md) · [exact locally executed Python](../scripts/verify_sec73_d2_early_branch.py) · [exact saved JSON](../results/sec73_d2_early_branch.json).

The script constructs all 57 typed material items and their anchor/induced incidence records, retains the nine-item h*/p* subset with six boundary slots and a blocked-annotation consistent completion, checks the three restriction pairs and one realization pair, explicitly computes \`Ψ\`, \`A*\`, q definedness, Role, C, finite composites and the identity-comparison stage checks with BC disagreement. It records the source's **axis-naming uncertainty and explicit boundary-record completion** rather than claiming the latter were all fully enumerated in the original PDF.

\`\`\`text
EXECUTED_PYTHON_BYTES: 9473
EXECUTED_PYTHON_SHA256: 5c0782961bf41992f6247e7032fcbf3b6f103755a0b2e19dacb3691e9a070516
EXECUTED_PYTHON_GIT_BLOB: 5949d6c21cab61c2194bbcd9dfcf0eaf058fc9b6
EXECUTED_JSON_BYTES: 1534
EXECUTED_JSON_SHA256: f5da7b3a5e19ad93f669a9ec9ecc0045671080d79bc3d7cf664756e1966c837a
EXECUTED_JSON_GIT_BLOB: b1fa5dcca82bf8f377f6027ef5c7dbd425a723a5
\`\`\`

The standard-library Python was executed locally with \`python -W error\`, and both exact script and result Git blob hashes **matched the file bytes uploaded to and fetched back from GitHub**. This demonstrates a valid finite **explicitly completed** source-typed witness and the stage-index calculation, **not** independent external certification or proof that every possible completion of unspecified boundary records is valid.

Windows at cloned repository root:

\`\`\`powershell
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_sec73_d2_early_branch.py
\`\`\`

Default output: \`DSD_Audit/audits/formal_proof/formation_axiom_system/results/sec73_d2_early_branch.json\`. Optional first argument is a JSON output path.

## 6. FPA v0.1 gate matrix

- **G01 PASS:** immutable author/PDF/source §7.3 pp.25–26 and exact unnumbered case.
- **G02 PASS:** nine vertices, twelve undirected edges, 36 potential directional slots; h* material subset 2+1+6=9, common B and material record across regimes.
- **G03 PASS_WITH_REFINEMENT:** source “horizontal” r* clashes with normal row-column reading; naming clarification recommended, not incidence/branch failure.
- **G04 PASS_WITH_REFINEMENT:** inherited *blocked* boundary annotation on H*/h*/p* not exhaustively written; one consistent source-compatible completion exhibits II/III soundness. For literal “fully specified” status, clarify the annotation as part of explicit primitive data.
- **G05 PASS:** Primitive I/II/III/V and definitional IV/VI/VII under the completed well-typed model, including empty A*− and q−.
- **G06 PASS:** positive exactly one channel term +1, negative no channels, finite composites with zero on empty families.
- **G07 PASS:** source Vλ=W=real spaces may be infinite; formation-finite Definition2.3 only requires the listed formation carriers/domains finite.
- **G08 PASS:** explicit I2 witness via identity and universal failure I3 under singleton p* and mismatched primitive BC; b=3 by definition.
- **G09 PASS:** b=5 if BC− repaired but q− still empty; otherwise illegally assigning nonempty q− at empty A*− violates V; Stage4 not independent.
- **G10 PASS_WITH_BOUNDARY:** source BC is a regime-supplied primitive predicate; no derivation that grid physics necessitates the truth values.
- **G11 PASS:** exact locally executed Python/JSON Git blob verified; finite witness is not a full characterization of all completions or a proof of source's separate §7.4 indexed witness.
- **G12 PASS:** source PDF/Zenodo unchanged, existing 22/22 method-family standardization unaffected, no external mathematical review established.

**FINAL BOUNDED VERDICT:** \`MATHEMATICAL_VERDICT=PROVED_IN_DECLARED_BACKGROUND\` (branch result for an explicit valid completion); \`DSD_AUDIT_VERDICT=PASS_WITH_REFINEMENT\`; \`REVISION_NEED=CLARIFICATION\`.

The mathematically decisive result **\`b(L+,L−)=3\` survives**. The remaining issue is **source specification completeness / coordinate terminology**, not a valid countermodel or new axiom need. In any future manuscript revision (not in this audit), make the inherited blocked annotation explicit and either call r* the joining nearest-neighbor edge or fix a coordinate convention. Existing optional T4.7 wording clarification is a separate historical action. F2 whole-manuscript FPA remains **OPEN**, independent external validation not established.

**NEXT source-bounded case NOT_STARTED:** \`FAS-F2-SEC7.4-3X3-001\`, unnumbered §7.4 “Fully specified synthetic formation-finite 3×3 indexed witness.” A separate precommit is required.

[Notion synchronized §7.3 D2 boundary and branch FPA case](https://app.notion.com/p/3ff81f51e7fa81b2842affbdae09d613)
