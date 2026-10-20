# FAS-F2-APPA-TYP-001 — Original Appendix A: Typing and Notation / 원문 부록 A 표기·자료형 감사

2026-10-20 KST · Existing **DSD Audit / FPA v0.1** · original **unnumbered appendix**, not a new theorem and not a whole-paper proof certificate.

## Immutable source, prospective precommit, actual execution

```text
AUDIT_ID: FAS-F2-APPA-TYP-001
AUTHOR: Kwon Dominicus
SOURCE_PDF: DSD_Formation_Axiom_System_EN(5).pdf, 33 attached PDF pages
SOURCE_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
SOURCE_LOCATION: Appendix A, Typing and Notation, printed p.30
SOURCE_ROWS: 19 grouped Symbol–Meaning table entries and map-domain footnote
PRECOMMIT_COMMIT: 519211d8208a3d06a3460d8404db87dad48a8234
PYTHON_COMMIT: d51cc838c5eec3dc6ab17d0be4fe9c83291ef1c9
PYTHON_BYTES: 6999
PYTHON_SHA256: fb3c11ccf9c119d39b000ede78c12529b2dd7e7d6f090c5ae3d2dde70f6e0296
PYTHON_GIT_BLOB: d8576d1f1b25676e6ee4db70cd90463b71dc8041
JSON_COMMIT: 3310ce012c342fd861e15b8796d80c59cfea7f8f
JSON_BYTES: 4045
JSON_SHA256: ebf1816c66774b070c7c6f2d47b9f582737e998391e2bcce9a66f1972493770b
JSON_GIT_BLOB: 73468b7eb755d14b588874ea94a5cc4b1c1356a6
SOURCE_CROSSWALK_MATCH: 19/19
OUTSTANDING_SOURCE_TYPE_MISMATCH: 0
MATHEMATICAL_VERDICT: SOURCE_NOTATION_CONSISTENT_WITH_DECLARED_TYPING
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE
OPTIONAL_GLOSSARY_ENRICHMENT: RECOMMENDED_NON_MANDATORY
NEXT: FAS-F2-APPB-STAT-001 / NOT_STARTED
F2_WHOLE_MANUSCRIPT_FPA: OPEN
INDEPENDENT_EXTERNAL_VALIDATION: not_established
ORIGINAL_PDF_ZENODO: unchanged
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged
```

The source PDF printed p.30 was inspected using both `pdftotext -layout` and **a rendered page image** to avoid mangling the math scripts in the Appendix A table. This source-table audit assumes the already separately checked definitions and propositions as dependencies; it does **not** produce new mathematical theorems.

## 1. Exact source-table-to-main-text crosswalk (19 grouped rows)

| ID | Printed source table symbol group | Primary body source | Outcome and exact meaning |
|---|---|---|---|
| A01 | `B, Supp(B)` | §§2.1–2.2 | **MATCH**. Fixed candidate base and **typed support carrier**; source sets, not a class-sized background model carrier. |
| A02 | `mathcal M_L, M_B^L` | §2.2 | **MATCH**. Material **record structure** versus its **carrier**; induced relations and externally valued annotations distinguished. |
| A03 | `E_B^L,P_B^L` | §§2.2,6.1 | **MATCH**. Full **candidate** expression/configuration carriers, including candidates that ultimately fail. |
| A04 | `Adm_expr^L,Des_expr^L` | §2.2, Primitive I | **MATCH**. Different expression predicates on E, with `Des_expr⇒Adm_expr`, not converse. |
| A05 | `Adm_cfg^L,LC_L,BC_L` | §2.2, Primitive III/Closure IV | **MATCH**. Primitive gates on P; **`Des_cfg` is derived** from Ψ, not a fourth primitive gate. |
| A06 | `Res_L,Realize_L` | §2.2, Primitives II/III | **MATCH**. Relations E×E and E×P respectively; source does **not** impose restriction transitivity (optional Appendix D). |
| A07 | `Psi_L,A_L^*` | §2.2 Definition2.1 | **MATCH**. Ψ **uses only primitive vocabulary** but **is itself defined**, not independently supplied. A* is union of act(p) over primitive Ψ-witnessed p. |
| A08 | `K_des^L,A_L` | §3.1 Clause IV | **MATCH**. Derived describable configurations and structural union; for full models `A_L=A_L^*`. |
| A09 | `V_{L,λ},0_{L,λ}` | §2.2 | **MATCH**. A **pointed value SET**, not generally a vector space; do not conflate it with F-vector term space W. |
| A10 | `Q_{L,λ},q_{L,λ},Gamma_{L,λ}` | §3.2 Primitive V | **MATCH**. ONE regime-global partial function `q:Q→V`; Γ its **graph**. Local Γ(p) are restrictions, not independent assignments. |
| A11 | `U_L,C_L,T_L` | §3.2 Clause VI and post-VI supply | **MATCH**. U candidate five-tuples, C **admitted** subset, supplied `T:C→W`, not a total `T:U→W`. |
| A12 | `D_L^comp,Comp_L` | §3.2 Clause VII | **MATCH**. All finite SETS of admitted C, including empty, without repetition; `Comp(∅)=0_W`. |
| A13 | `F_{L≤k},F_k(B,F),pi_{j,i}` | §2.3 Definition2.4/Proposition2.5 | **MATCH**. Truncation record from a full model versus **metatheoretic class** of well-typed stage records; reductions erase later coordinates; truncations need not be full models. |
| A14 | `Tr_L(c)` | §3.3 Definition3.5/Theorem3.6 | **MATCH**. Formation trace of **candidate** c∈U; for admitted c∈C iff the trace is nonempty. Trace histories not part of five-tuple identity. |
| A15 | `Sigma_L` | §6.1 Definition6.1 | **MATCH**. Full static descriptor, including unsuccessful candidate universe and term data, not just K_des. |
| A16 | `FormDesc_{B,F}` | §§2.1,6.1 | **MATCH**. A possibly proper **metatheoretic CLASS** of set-coded full descriptors, not a set carrier of a descriptor. |
| A17 | `Phi,hatPhi` | §6.2 Definition6.2/Proposition6.3 | **MATCH**. Forward map and induced map on **candidate** five-tuples, taking C into C; injectivity on C is necessary for the cited **general finite SET-family sum-preservation law**. |
| A18 | `cong_B^fix` | §6.3 Definition6.10/Theorem6.14 | **MATCH**. Strict base-fixed formation isomorphism for same fixed **(B,F)** and typed bijections, J F-linear iso; not unqualified heterogeneous-base comparison. |
| A19 | `I_k(L,M),b(L,M)` | §6.4 Definition6.15/Theorems6.16–6.19 | **MATCH**. Stage0..7 nested comparison sets and first empty level for strictly nonisomorphic pairs; Stage0 can block, Stage4 cannot be first independent branch. |

The footnote is correct: **every function is used only on its declared domain**. In particular, `q_{L,λ}(a)` meaningful iff a∈Q, channel formula uses Γ, and `T_L(c)` meaningful only if c∈C. No totalization with a numerical zero is permitted for q or T outside its domain.

## 2. Adversarial boundary findings

**Undefined assignment vs defined zero.** If q(a)=0 and a∈Q, the assignment is defined, Γ contains (a,0), and a Role tuple on a describable p can create an admitted channel, even if T(c)=0. If a∉Q, no q(a) exists and the corresponding candidate is absent from C. Both can yield Comp(∅)=0, so zero output cannot identify admission state.

**Candidate trace domain.** A candidate five-tuple with incorrect quantity value or missing global assignment has Tr(c)=∅, while a genuinely admitted candidate has a nonempty h→p formation trace. Being a candidate in U does **not** mean c is admitted in C or makes T(c) defined.

**Stage reductions.** For all 0≤i≤j≤k≤7, coordinate erasure satisfies `pi_{j,i}◦pi_{k,j}=pi_{k,i}`, and `pi_{k,k}=id`. **120 nested index triples**, not 120 arbitrary DSD objects, were checked in the selected ordered-record fixture. Stage0 denotes inherited background and carrier typing, not an eighth formation axiom.

**Forward map collision illustrates why Proposition6.3 has a condition.** Take two source admitted channels distinguished by roles ρ1≠ρ2, both with term 1. A forward map can identify the two source role labels to one target ρ (noninjective role map), with identity material/configuration/quantity maps and J=id, and preserve both individual component terms. Its induced channel image is a one-element SET. Then the sum of the source two-element family is **2**, while the sum of its one-element image family is **1**. Therefore composite preservation is NOT unconditional for all forward maps: the source correctly requires injectivity on the admitted channel set for Proposition6.3’s general finite-family equation. The table claims only “induced candidate-channel map” and makes **no mistaken unconditional composite claim**.

**Records versus categories.** `FormDesc_{B,F}` is a possibly large class outside the set-coded descriptor; `F_k(B,F)` likewise denotes a metatheoretic stage-record class. The checker does not and cannot enumerate all these classes. Strict comparison is base/field-fixed; a preselected J in Definition6.21 is not a substitute for all strict typed comparison maps.

## 3. Non-listed symbols — useful optional clarity, not source error

Appendix A is a **selective summary table** rather than the full primitive signature. The body separately defines `Role_L`, `Chan_L`, `Des_cfg^L`, `ConfAdm_L`, `W_L`, the map `J:W_L→W_M`, `Lambda_delta`, negligible size functions and thresholds, configuration-local `Q(p),Gamma(p)`, and `Form_{B,F},EmbForm_{B,F}`. Their absence as **separate table rows** does not make the present 19 symbol explanations false: each appears in the main source.

An **optional—not mandatory—editorial enhancement** would add 3–5 extra rows for (i) supplied vector term space W and F-linear J, (ii) Role/Chan derived relation difference, (iii) primitive-vocabulary Ψ versus derived Des_cfg, (iv) negligible-size data and its λ-domain, and (v) the possibly large categories Form/EmbForm. These are independent from the existing historic §8 D10 logical comparison wording, §7.3 boundary-inheritance/axis naming, and T4.7 optional scope notes. None justifies changing core mathematical statements.

## 4. Reproducible file evidence and computational scope

- [Prospective PRECOMMIT](FAS-F2-APPA-TYP-001_PRECOMMIT.md)
- [Actual executed Python](../scripts/verify_appa_typing_notation.py)
- [Actual deterministic JSON](../results/appa_typing_notation.json)

Local `python -m py_compile` and `python -W error` passed after making the Windows path usage docstring raw to eliminate an **invalid escape sequence** warning. The **exact locally run 6999-byte script** was uploaded and fetched from GitHub; Git blob **d8576d1f1b25676e6ee4db70cd90463b71dc8041** matched local Git blob and SHA256 **fb3c11ccf9c119d39b000ede78c12529b2dd7e7d6f090c5ae3d2dde70f6e0296**. Its **4045-byte JSON** similarly matched remote Git blob **73468b7eb755d14b588874ea94a5cc4b1c1356a6** and SHA256 **ebf1816c66774b070c7c6f2d47b9f582737e998391e2bcce9a66f1972493770b**.

The program evaluates **one-point legal source-typed examples**, domain/status distinctions, a forward map role-label collision, the 19 **manually source-inspected** crosswalk entries and the 120 stage-index reduction triples. It does NOT parse LaTeX into a formal language, mechanically infer that the Appendix A printed page has 19 rows, construct the ZFC universe or certify all proofs in F2. That 19-row reading and source-page crosswalk were independently inspected from the supplied PDF.

Windows repository root:

```powershell
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_appa_typing_notation.py
```

Default output: `DSD_Audit/audits/formal_proof/formation_axiom_system/results/appa_typing_notation.json`; optional first command argument sets output JSON file. Standard-library Python only.

## 5. FPA v0.1 gates and final status

- G01 **PASS** original attached PDF SHA, printed p.30, rendering plus text extraction.
- G02 **PASS** nineteen source table groups each mapped to body definition, no identified source type contradiction.
- G03 **PASS** distinction material record structure vs carrier, primitive Ψ vocabulary vs derived closure, pointed V vs term W.
- G04 **PASS** partial q global domain guards, Γ vs independent local assignment, q defined zero vs undefined.
- G05 **PASS** candidate U vs admitted C, T only on C, Tr on candidates, empty trace exactly nonadmission.
- G06 **PASS** finite set families and Comp(∅)=0, admit zero term not equated with channel absence.
- G07 **PASS** stage record/class, reduction 120 triples, Stage0 not eighth formation axiom.
- G08 **PASS** typed forward map induced channel map and its **injectivity condition** for forward sum preservation.
- G09 **PASS** strict ≅_B^fix and branching comparisons scoped correctly to common (B,F) and full tuples.
- G10 **PASS_WITH_BOUNDARY** table intentionally selective; optional glossary extension not a source error or required edit.
- G11 **PASS_WITH_BOUNDARY** finite Python selected assertions and the human source crosswalk, not full formal mechanical proof.
- G12 **PASS** GitHub local byte-for-byte Python/JSON identity verified, no original PDF/Zenodo modification or outside reviewer evaluation.

**MATHEMATICAL_VERDICT: SOURCE_NOTATION_CONSISTENT_WITH_DECLARED_TYPING**
**DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY**
**REVISION_NEED: NONE**.

Existing named FPA results **14 theorems / 2 propositions / 9 corollaries** unchanged. The unnumbered original §§7.3,7.4,8,9 audits plus this **Appendix A** bring the separate source-section tally to **5**, and must not be counted as new theorems. The full F2 manuscript FPA remains **OPEN**, external independent verification is not established, Method Family internal standardization **22/22 unchanged**.

**NEXT NOT_STARTED:** `FAS-F2-APPB-STAT-001` — Appendix B *Formation-Stage Status and Result Map*, first prospectively freeze its original exact table.
