# FAS-F2-T7.1-001 — Theorem 7.1: Existence of a full formation model

**2026-10-20 KST · DSD Audit / Formal Proof Audit v0.1 · One theorem scoped, source locked**

```text
AUDIT_CASE: FAS-F2-T7.1-001
PRIMARY_SOURCE: Kwon Dominicus, DSD_Formation_Axiom_System_EN(5).pdf, 33 pages
PRIMARY_SOURCE_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
SOURCE_LOCATION: Section 7.1, Theorem 7.1 printed p.24
PRECOMMIT_COMMIT: 4c9c9eaf9a14e232c9cdb780356eb1c0a90f46e6
EXACT_EXECUTED_PYTHON_COMMIT: 59071adc9ba1461f4378a7627d32b973baf78973
EXECUTED_PYTHON_SHA256: 34b41774a6ede404fae2a2adc5c2b5f6c3c12567afdb5cca997467b49fcc2759
EXECUTED_PYTHON_GIT_BLOB_SHA: 391da3622147bcafb996e82f86b2a930427f7663
EXECUTED_JSON_COMMIT: 3cc2cc6901607320a0ac3de34cf05dc40c855592
EXECUTED_JSON_SHA256: fb390b2faf5148b03dd765b0da6881dd448883f3bcd4aeb186bc738c7d571bdc
EXECUTED_JSON_GIT_BLOB_SHA: 652bd1ecc5aadc8218fad796c800b8d610e6142e
MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND
FPA_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE
FULL_F2_MANUSCRIPT: OPEN
INDEPENDENT_EXTERNAL_VALIDATION: not_established
SOURCE_PDF_ZENODO: unchanged
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged
NEXT: FAS-F2-C7.2-001 / NOT_STARTED
```

## 1. Frozen theorem and all quantified hypotheses

The exact source **Theorem 7.1 (Existence of a full formation model)**, §7.1 printed p.24, asserts:

> Let F be a field and let B have a nonempty support carrier. Then there is a set-sized choice of typed formation data over (B,F) that is a full DSD formation model.

The parameter pair `(B,F)` is **already fixed**, with both set-sized in the manuscript's ZFC background (§2.1). This is **for every field F and every such B**, not only for a field selected afterward or only for singleton support. The theorem is an **existence claim**, not uniqueness, nonzero terms, large carrier counts, or that every possible primitive input makes a full model. The following verifies the precise construction in its proof, not a substituted external construction.

## 2. Universal explicit set-coded construction and axiom-by-axiom proof

Fix ANY declared field F and ANY set-sized base B with `Supp(B)≠∅`. Choose `s∈Supp(B)`. This is an **individual witness selection**, not an axiom of choice needed across a family of nonempty supports. Choose the explicitly source-permitted **empty material-record relational signature**, so all induced material-record structures on retained subsets are trivially inherited.

Define all primitive sorts as small sets:
```text
M_B={a}, E_B={h}, P_B={p}.
mat(h)=act(p)={a}.
anch_h:{a}→Supp(B), a↦s;
anch_p:{a}→Supp(B), a↦s.

Adm_expr(h)=true, Des_expr(h)=true.
Res={(h,h)}, Realize={(h,p)}.
Adm_cfg(p)=LC(p)=BC(p)=true.

Λ={λ}, V_λ={0_λ} pointed at 0_λ.
Q_λ={a}, q_λ(a)=0_λ, Γ_λ={(a,0_λ)}.
Λ_δ=∅; role label set R={ρ};
Role={(p,a,λ,ρ)}.
```
The source's **primitive interface** convention (§2.2) means that `Des_expr`, `Adm_cfg`, `LC`, `BC` are freely supplied primitive predicates subject to the stated axioms; setting them true is an allowed input, not an already-derived conclusion.

**Primitive Axiom I (admission):** The only describable expression h is admitted. Hence `Des_expr(h)⇒Adm_expr(h)`.

**Primitive Axiom II (soundness of restrictions):** The only restriction `Res(h,h)` has `mat(h)⊆mat(h)`; its anchor equals its own restriction to `mat(h)`; h is admitted. Every admitted expression has an identity restriction (the same declared `Res(h,h)`). The empty material-record signature has no hidden internal relation/annotation constraints. Thus II holds.

**Primitive Axiom III (realization):** For the single `Realize(h,p)`, `act(p)={a}⊆mat(h)={a}`; `anch_p=anch_h|act(p)`, and the inherited relational record is trivially consistent. Thus III holds.

**Definitional Closure IV (genuine configuration witness):** The pair `(H,h)=(h,h)` is in Res; `Des_expr(h)`, `Realize(h,p)`, and all three configuration-admission inputs are true. Thus the exact primitive witness `Ψ(p)` holds, not merely a stipulated derived predicate. Clause IV therefore fixes `Des_cfg(p)=true`, `K_des={p}`, `A*=A=act(p)={a}`.

**Primitive Axiom V (global partial assignment):** `Q_λ={a}⊆A*={a}` and `q_λ:{a}→{0_λ}` is the total function on the **declared partial domain**, with `q_λ(a)=0_λ`. It is a **defined zero value**, not an undefined assignment. `Λ_δ=∅` means the axiom imposes no optional negligible-size map or threshold. Thus V holds.

**Definitional Closure VI (one channel):** The candidate operational-channel universe is `U=P_B×M_B×{λ}×V_λ×R` and has the one candidate
```text
c=(p,a,λ,0_λ,ρ).
```
All Clause VI conjuncts are true: derived `Des_cfg(p)`, `(a,0_λ)∈Γ_λ(p)`, and `Role(p,a,λ,ρ)`. Therefore `Chan(c)=true`, `C={c}`. Its formation trace contains exactly the seven-tuple `(h,h,p,a,λ,0_λ,ρ)`, so Definition 3.5 / Theorem 3.6's trace iff is satisfied. Restriction–realization witnesses are **not** part of five-tuple channel identity.

**Post-Stage-VI term input and Closure VII:** For **the already fixed arbitrary F**, choose the **zero F-vector space** `W={0_W}`. It exists over every field because its addition and scalar multiplication are uniquely determined by `0_W+0_W=0_W` and `α·0_W=0_W` for all `α∈F`. Supply the total component-term map `T:C→W`, `T(c)=0_W`. There is **no axiom** `0_λ=0_W` (they have different types), and `T` is not required to be an F-linear map from its set-valued channel domain. Clause VII forces
```text
D_comp=P_fin({c})={∅,{c}};
Comp(∅)=0_W; Comp({c})=T(c)=0_W.
```
All chosen carriers, primitive relations, maps, the zero term space, channels and composite-family domain are **sets**. No infinite summability or choice principle is needed. By source Definition 2.2, this primitive core with the derived IV/VI/VII interpretations and separately supplied W,T **is a full DSD Formation model** over the *arbitrary fixed (B,F)*. This completes the quantified existence proof. The earlier separately audited Theorem 3.3 gives uniqueness of closure relative to fixed post-VI W,T, but it is not needed to choose those data in this explicit witness.

## 3. Adversarial boundaries and verified finite computation

[Prospective precommit](FAS-F2-T7.1-001_PRECOMMIT.md) · [exact executed portable Python](../scripts/verify_t71_full_model_existence.py) · [result JSON](../results/t71_full_model_existence.json).

The source-typed standard-library Python checker constructs and audits **four** concrete combinations of selected fields and support sizes:

| Field | Base support size | Primitive axioms | Closure | Candidate U | Admitted C | Trace witnesses | Finite families |
|---|---:|---|---|---:|---:|---:|---:|
| `F₂` | 1 | I/II/III/V | IV/VI/VII | 1 | 1 | 1 | 2 |
| `F₂` | 3 | I/II/III/V | IV/VI/VII | 1 | 1 | 1 | 2 |
| `Q` | 1 | I/II/III/V | IV/VI/VII | 1 | 1 | 1 | 2 |
| `Q` | 3 | I/II/III/V | IV/VI/VII | 1 | 1 | 1 | 2 |

Aggregate: **4** correctly typed full-model instances, **4** admitted channels, **4** trace witnesses and **8** finite-family sum checks. Each family composition is `0_W`. The code independently represents `0_λ` by `('V_lambda','0')` and `0_W` by `('W','0')`, ensuring their types remain distinct. Selected rational scalar samples test the zero space, whereas the **proof for all α∈F** is the one-line algebraic definition above, not finite sampling.

**Negative/alternative safeguards:**
- **Empty support**: violates **the hypothesis of this theorem**. The supplied construction chooses `s∈Supp(B)`; the construction cannot be applied to empty support, but this says nothing about all hypothetical empty-material models or the axiom system under different hypotheses.
- **Missing identity restriction**: with h still admitted, deleting `Res(h,h)` violates Axiom II in this particular candidate. It is not a countermodel to the theorem's existence conclusion, since the theorem explicitly includes the identity restriction.
- **Remove q(a) assignment**: keeping the other source-compatible primitive inputs and using empty `Q_λ` yields another **legal full model**, with `U` still containing the candidate but `C=∅`, empty T and only the empty composable family. The theorem does **not** require every full model to have a channel; it asserts existence of at least one, and chooses a model with one channel.
- **No false generalization**: Theorem 7.1 alone does not prove formal `ZFC⊢σ_DSD` (that is the next separately auditable Corollary 7.2), arbitrarily large finite models (Corollary 7.4), or the later D2 example.

**Code execution and byte identity:** The **exact locally executed 8,218-byte Python file** was run with `python -W error` and returned PASS. Its SHA-256 was `34b41774a6ede404fae2a2adc5c2b5f6c3c12567afdb5cca997467b49fcc2759`; its Git blob SHA was `391da3622147bcafb996e82f86b2a930427f7663`. GitHub upload and read-back yielded **exactly the same Git blob SHA**. The locally produced JSON (3,245 bytes) had SHA-256 `fb390b2faf5148b03dd765b0da6881dd448883f3bcd4aeb186bc738c7d571bdc` and Git blob SHA `652bd1ecc5aadc8218fad796c800b8d610e6142e`, also matched on GitHub read-back. This establishes byte identity between the **locally executed and committed reproducible artifacts**. It does **not** establish outside/third-party independent code execution or general full-model enumeration.

Windows repository-root command:

```powershell
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_t71_full_model_existence.py
```
Default output location: `DSD_Audit/audits/formal_proof/formation_axiom_system/results/t71_full_model_existence.json`; optional first argument overrides. Standard-library Python only.

## 4. Twelve FPA gates and source-bound verdict

- G01 **PASS** frozen source: attached English PDF 33 pages and SHA verified; exact §7.1 T7.1 printed p.24.
- G02 **PASS** quantifiers: for **each** set-sized field F and **each** B with nonempty support, not just F₂ or one B.
- G03 **PASS** typing: set-sized material/expr/config/kind/role/vectors/relations/anchors with a genuine s from support.
- G04 **PASS** primitive I/II/III/V: all clauses checked including identity restriction and global domain q.
- G05 **PASS** derived IV/VI/VII: real Ψ witness, singleton candidate and admitted channel, zero-space term, exactly two finite families.
- G06 **PASS_WITH_BOUNDARY** existence/zero: 0λ typed distinctly from 0W; arbitrary F has zero vector space, no positivity or nonzero term requirement.
- G07 **PASS** hostile controls: empty B support outside theorem scope, missing Res invalid particular core, empty q yields alternate full model with C empty.
- G08 **PASS_WITH_BOUNDARY** finite/general: four explicit finite instances reinforce but do not establish universal theorem; universal proof is the arbitrary-(B,F) construction.
- G09 **PASS** external base/carrier scope: a selected s can anchor all material even if Supp(B) contains other elements; no global surjectivity of anchors demanded.
- G10 **PASS** set theory: all carrier/term/function choices set-sized; no axiom of choice invoked beyond selecting one witness in one nonempty set.
- G11 **PASS_WITH_BOUNDARY** dependency propagation: Section 7 Corollary 7.2 and Theorem 7.3 later are **NOT_STARTED**; Theorem 7.1 does not certify full manuscript.
- G12 **PASS** provenance/external: exact executable Python and JSON Git blob hashes confirmed, yet independent external mathematical validation remains not established.

**MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND**
**DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY**
**REVISION_NEED: NONE**

Boundaries are the theorem's *nonempty set-sized support* hypothesis, the distinction between *existence* versus uniqueness/arbitrary model properties, and finite-computation limits. They do **not** indicate a gap in the explicit construction. Theorem 4.7's earlier optional statement-scope wording recommendation remains separate. Original source PDF and Zenodo are **unchanged**. The existing DSD Method Family **22/22** internal standardization count is unaffected. **F2 whole-paper FPA remains OPEN.**

**Next separate audit: `FAS-F2-C7.2-001` — Corollary 7.2 (ZFC realizability and set-coded satisfiability), NOT_STARTED.**
