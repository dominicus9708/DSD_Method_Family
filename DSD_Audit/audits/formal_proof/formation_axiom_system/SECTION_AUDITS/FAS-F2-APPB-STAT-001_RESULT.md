# FAS-F2-APPB-STAT-001 — Appendix B: Formation-Stage Status and Result Map

**2026-10-20 KST · DSD Audit / FPA v0.1 · Original unnumbered appendix-source audit, not a new theorem.**

## 1. Frozen original and verdict

```text
AUDIT_CASE: FAS-F2-APPB-STAT-001
AUTHOR: Kwon Dominicus
PDF_SOURCE: DSD_Formation_Axiom_System_EN(5).pdf (33 attached pages)
SOURCE_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
SOURCE_LOCATION: Appendix B, printed p31, sixteen source rows
PRECOMMIT_COMMIT: df98dc7b9c5b908874ef52491bcc5d3c48afae8b
EXECUTED_PYTHON_COMMIT: 1cd1898f842677119f34e1bcc5ba326d053888c6
PYTHON_BYTES: 5243
PYTHON_SHA256: 4efd29b2fb2ff27ad9f8fb7755ab4ede7e2d05180f366a5d32c90d94704d13d2
PYTHON_GIT_BLOB: e4b9a2862a28ba6c1461850c1bd01d32f1dd1070
EXECUTED_JSON_COMMIT: 26ed2705157a1c17921b77843961b01dbd817109
JSON_BYTES: 3690
JSON_SHA256: 24244befd22bc97c33526ec763f54c704330604aa7e5f752aa98d05d799e9479
JSON_GIT_BLOB: d27f9f50ee523a6e8b34362083e08f94ebbf0416
MATHEMATICAL_VERDICT: SOURCE_RESULT_MAP_ALIGNED_WITH_DECLARED_THEOREM_SCOPES
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE
ORIGINAL_TABLE_ROWS_MATCHED: 16/16
SOURCE_MAP_CONTRADICTIONS_FOUND: 0
NEXT: FAS-F2-APPC-CONSTRUCT-001 / NOT_STARTED
FULL_F2_MANUSCRIPT_FPA: OPEN
INDEPENDENT_EXTERNAL_VALIDATION: not_established
SOURCE_PDF_ZENODO: unchanged
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged
```

Exact source is titled **“Formation-Stage Status and Result Map”** and is a two-column stage/result **summary map** on printed p31, visually checked against the rendering as well as PDF extracted text. Its sixteen items are not independent extra axioms or new theorems. Source's stage range **I–VII** denotes seven formation stages with **four primitive I/II/III/V** and **three defining closure IV/VI/VII**, while Stage0 in comparison sets is ambient carrier/background comparison, NOT an eighth formation axiom.

## 2. All sixteen original table rows, in source order

| Row | Stages used in original Appendix B | Original result in brief | Body result and audit boundary |
|---|---|---|---|
| B01 | **I, II, III, V** | Independent non-vacuous primitives; minimal residual clauses | **Theorem4.5**, **Prop4.6**, **Theorem4.7**: packages independent relative typed/closure background, **six residual constraints only after factoring out typing-induced consequences**. MATCH. |
| B02 | **IV, VI, VII** | Unique closure, primitive reduct characterization | **Theorem3.3**: **relative to supplied post-Stage-VI W,T**. Do not claim unique independent choice of term data. MATCH. |
| B03 | **I–VII** | A full model exists, finite typed data realizable | **Theorem7.1/Cor7.2/Thm7.3/Cor7.4**: valid typed finite material/anchor/quantity/role seed including `a∈A∩Dλ`, not arbitrary invalid data; for each finite n there is a model, not one infinite formation-finite model. MATCH with boundary. |
| B04 | **I** | Expression non-admission blocks describing it | Primitive I, `Des_expr(x)⇒Adm_expr(x)`, by contrapositive `¬Adm⇒¬Des`. Mere admission does **not** guarantee description. MATCH. |
| B05 | **II** | Material and anchors inherited under restrictions | Axiom II and source induced material record convention. No transitivity of Res is assumed in the core (see optional Appendix D). MATCH. |
| B06 | **II–III** | Support inherited through realization | III requires `act(p)⊆mat(h)` and `anch_p=anch_h|act(p)`; prior II supports restriction chain. MATCH. |
| B07 | **I–IV** | Describable p has described restricted-expression witness | Definition2.1 `Ψ(p)`, Closure IV: real pair `Res(H,h),Des_expr(h),Realize(h,p)` plus **Adm_cfg/LC/BC** gates. `H=h` identity witness valid; proper restriction not mandatory. MATCH with qualification. |
| B08 | **IV–V** | Describability not the same as assignment | IV fixes describability; Primitive V independently supplies one regime-global **partial q** on `Q⊆A*`. Describable configurations need not carry assigned values. MATCH. |
| B09 | **IV–VI** | Operational channel needs described p and assigned value | Clause VI **also needs `Role(p,a,λ,ρ)`**, with `(a,v)∈Γλ(p)`, not merely existence of q somewhere in regime. MATCH as necessary, not sufficient conditions. |
| B10 | **V–VII** | Undefined assignment, channel absence and zero contribution distinct | `q` undefined outside Q; C absent when VI fails; admitted channel T may be 0; `Comp(∅)=0_W`. MATCH. |
| B11 | **I–VII + Defs2.4,3.5** | Coherent reductions, admitted iff nonempty trace | **Proposition2.5/Theorem3.6**: for **candidate c∈U**; trace history is NOT inserted in channel operational identity. MATCH. |
| B12 | **I–VII + Def6.2** | Forward witness, admitted channel and (conditionally) finite composites | **Proposition6.3**, **Theorem6.5/Corollary6.6**: basic witness/channel preservation requires no channel-map injectivity, but equality of **finite SET-family sums** does require `hatΦ|C_L` injective. MATCH with boundary. |
| B13 | **I–VII + Def6.4** | Embeddings reflect and preserve, wide subcategory, inclusion preorder | **Theorem6.8, Corollary6.7, Proposition6.11**, with source reflection/embedding conditions, not arbitrary forward maps. MATCH. |
| B14 | **I–VII + Defs6.10,6.15** | Strict isomorphism is bijective embedding; earliest failure by nested comparisons | **Theorem6.14/Theorem6.16**: comparisons over same fixed (B,F), every candidate comparison tuple tested at first empty level. Earliest failure may be `I0`; stage4 cannot first independently fail. MATCH. |
| B15 | **IV, VI, VII + Thm6.17** | Determined closure, no independent Stage4 branch, channel/composite preservation from inputs | **Theorem6.17(i–iv)**: Stage4 fixed by Stage3; Stage6 fixed by Stage5 **and Role**; Stage7 by Stage6 **and supplied W,T**, with Stage7 strict comparison term-isomorphism requirements. No claim all output maps preserve arbitrary sums. MATCH with qualification. |
| B16 | **I–VII + Thms6.19,6.20** | First branching symmetric and strict-iso invariant; declared static theory collected | **Theorem6.19/Theorem6.20**, **only fixed (B,F) and the declared static typed framework**. “Completes the declared static typed formation theory” means collects these stated formal results, NOT Gödel-completeness, physical explanatory completeness, source-wide external peer review or resolution of other problems. MATCH with boundary. |

**Overall: 16 of 16 original source-stage/result pairings substantively match the prior audited source, with their hypotheses retained. No false stage source or necessary theorem repair identified.**

## 3. Hostile controls: necessary versus sufficient and omitted assumptions

1. **Expression admission:** Primitive I only states the forward implication from describability to admission. Its contrapositive in B04 holds; its converse does **not** automatically hold.
2. **Full configuration witness:** A Res(historical expression, restricted expression) and Realize relation alone are not enough if any one of Adm_cfg, LC, BC fails. B07 is correct as a necessary witness statement; the complete Ψ formula must be consulted for sufficiency.
3. **Admitted channel:** B09 states necessary conditions only. A valid q on a material item and a described configuration still do not admit a channel when the source Role tuple is missing.
4. **Defined zero:** q(a)=0 where a∈Q can create an admitted channel, and T(c) may be zero. For a∉Q there is no q(a) or admitted channel on that assignment. An empty family's composite equals 0 without asserting any channel.
5. **Forward-map collision:** two distinct source admitted role-channels each with T=1 may both map to a single target admitted role-channel with T=1. Individual term preservation holds, yet the source finite SET-family sum is 2 versus image family's 1. This is an explicit boundary illustration for Proposition6.3's injectivity caveat, not a flaw in Appendix B.
6. **Closure stages and branching:** I3=I4 means no first independent Stage4 obstruction (Theorem6.17). Stage6 closure depends on the Role data that are included at that stage; Stage7 requires supplied term data and the strict comparison's terminal term preservation. Neither is fixed by Stage3 alone.
7. **Global reach:** Appendix B is an overview of the manuscript's fixed-base static results; none of its sixteen rows establishes empirical mechanisms, infinite-family accumulation or other higher-level DSD method validations. The §8 D10 independently erroneous unqualified fixed-J “strictly weaker” comparison is **not reproduced in Appendix B**.

## 4. Actual executed code, reproducibility and limits

- [Prospective §B FPA obligations](FAS-F2-APPB-STAT-001_PRECOMMIT.md)
- [Actually executed Python](../scripts/verify_appb_stage_result_map.py)
- [Executed JSON ledger](../results/appb_stage_result_map.json)

The exact **5243-byte Python** was compiled with `python -m py_compile` and executed with `python -W error`. It uses a manually transcribed sixteen-row, source-inspected ledger (not machine-parsed PDF), and selected small Boolean/channel fixtures for nonadmission, Ψ with all three config gates, global defined-zero/undefined, Role, finite set-channel-map collisions, Stage4 derived determinacy and the previously audited 768/1536 partition. The JSON records all 16 row references and those selected checks; **the script does not prove Theorems3.3–7.4 or independently review their original proof lines**.

Local Python SHA256: `4efd29b2fb2ff27ad9f8fb7755ab4ede7e2d05180f366a5d32c90d94704d13d2`, Git blob `e4b9a2862a28ba6c1461850c1bd01d32f1dd1070`. Local JSON SHA256: `24244befd22bc97c33526ec763f54c704330604aa7e5f752aa98d05d799e9479`, Git blob `d27f9f50ee523a6e8b34362083e08f94ebbf0416`. **Both saved GitHub files were fetched and their blob SHAs match exact executed local bytes.** No GitHub Actions CI run or external independent evaluator certification is claimed.

Windows 11, at cloned GitHub repository root:

```powershell
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_appb_stage_result_map.py
```

Default output: `DSD_Audit/audits/formal_proof/formation_axiom_system/results/appb_stage_result_map.json`; optional first argument is output file.

## 5. Formal audit gates and next unit

- G01 PASS attached immutable PDF SHA, actual Appendix B printed p31 rendered and text extracted; exact 16 rows.
- G02 PASS all 16 source-map entries traced to the original referenced theorem and applicable hypotheses.
- G03 PASS primitive independent packages vs typed residual six qualifications preserved.
- G04 PASS uniqueness **relative** to supplied W,T and finite anchored role seed typing retained.
- G05 PASS expression admission contrapositive, primitive config gates and global partial q accounted for.
- G06 PASS trace iff admitted, defined zero/channel absence and empty-family zero distinguished.
- G07 PASS finite forward composites conditional on **injective induced channel map**.
- G08 PASS embeddings reflect witnesses, strict iso as bijective embedding at fixed B,F.
- G09 PASS Stage4 no independent first obstruction, Role and post-Stage6 W/T conditions.
- G10 PASS_WITH_BOUNDARY closing phrase interpreted as **declared static formal results only**; no unqualified physical/metalogical completeness inference.
- G11 PASS selected local fixture executed and exact Python/JSON remote blob matched, not a universal theorem-prover.
- G12 PASS prior §8 D10, §7.3 D2 and optional T4.7 clarity notes stay separate, no source PDF/Zenodo changes.

**MATHEMATICAL_VERDICT: SOURCE_RESULT_MAP_ALIGNED_WITH_DECLARED_THEOREM_SCOPES**
**DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY**
**REVISION_NEED: NONE**

Numbered source theorem-level FPA **14**, propositions **2**, corollaries **9**, all unchanged. Now **six** separately audited original unnumbered source sections §§7.3,7.4,8,9, Appendix A and Appendix B. Whole F2 FPA OPEN, independent external evaluation not established, source PDF and Zenodo unchanged, method-family 22/22 internal standardization unchanged.

**NEXT:** original Appendix C “Finite-Construction and Witness Reconstruction Protocol,” `FAS-F2-APPC-CONSTRUCT-001 / NOT_STARTED` (original printed pp31–32), a separate source and separately precommitted FPA unit.

[Notion synchronized Appendix B 16-row source-stage FPA](https://app.notion.com/p/3ff81f51e7fa812fb441dca8ed6fd05a)
