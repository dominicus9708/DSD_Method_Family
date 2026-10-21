# FAS-F2-APPD-RESTRICT-001 — Source-bound FPA of optional restriction coherence

**2026-10-21 KST · Kwon Dominicus · FPA v0.1 · unnumbered original Appendix D, printed page 32.**  
This is an audit of an *optional* extension, not a new numbered theorem, primitive axiom, or completion of the Formation F2 manuscript.

## 1. Source/version/prospective evidence lock

- PDF: `DSD_Formation_Axiom_System_EN(5).pdf`, 33 pages, SHA256 `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a`.
- Original Appendix D exact scope: (a) optional global transitivity `Res(H,h) ∧ Res(h,g) => Res(H,g)`; (b) `E_adm={x:Adm_expr(x)}`; (c) the restriction of `Res` to `E_adm×E_adm` is a preorder, using the required identity restrictions; (d) a separate optional induced-subexpression rule `(H|Y)|Z=H|Z` for suitable `Z⊆Y`; (e) the extension is not used by the core results.
- Dependencies actually checked against source: Primitive Axioms I and II, Definition 2.1 (primitive/derived status), Closure IV/VI/VII, Lemma 4.10, Corollary 4.11 and Proposition 4.12.
- **Prospective precommit**: `7c0cc4225cb5657c295af229ad17916108504f61`; [frozen audit obligations](FAS-F2-APPD-RESTRICT-001_PRECOMMIT.md), created before this execution.
- Locally executed and then GitHub-fetched [Python](../scripts/verify_appd_restriction.py), commit `af0da5134c0ed2657d0db67cfb08bc7ae11edf0e`, 4861 bytes, SHA256 `0be6b5a9371535fd2e35b67695a85ce8a807b93056f1b9b3dd99831d762c6b9c`, Git blob `3893e04e16a6c22994eb88cca741e7abab9ee5b0` (same as actual local source).
- Locally executed and GitHub-fetched [deterministic JSON](../results/appd_restriction.json), commit `13e3a32921d6d3162477ecbfca54cd19a5bb86d1`, 1100 bytes, SHA256 `9c1dfb90b01b6b3ff3fb54ec8b48cfdd2f4cddd88de3d66a24bb17c6ebb23598`, Git blob `cb14079344c7ae1d17299b2ca932772190d95f38` (exact local match).

## 2. Source proof: preorder is sound under the added global clause

Let `A=E_L^adm={x:Adm_expr_L(x)}`. Primitive Axiom II gives `Adm_expr_L(H) => Res_L(H,H)`. Hence for every `H∈A`, the restricted relation `Res_L∩(A×A)` is **reflexive**.

Assume the **optional** global transitivity clause. If `H,h,g∈A`, `Res(H,h)` and `Res(h,g)`, then `Res(H,g)`. Therefore the restricted relation is **transitive**. It is a **preorder** on A. The argument does not infer antisymmetry or totality; distinct candidate-expression tags may mutually restrict each other. A preorder does not, in general, define a partial order without quotienting by mutual reachability or imposing antisymmetry.

The text's global clause quantifies over all candidate expression triples. This is **stronger than merely imposing transitivity of the admitted–admitted subrelation**, because the source of a restriction may be unadmitted while its target is admitted by Primitive II. A legal three-tag boundary witness has an unadmitted source U, admitted h,g, `Res(U,h)`, `Res(h,g)`, required admitted identities, and lacks `Res(U,g)`; the admitted subrelation is already a preorder while the *global* appendix clause fails. Thus the original quantifier scope matters. This is not a defect in the source.

## 3. Non-implication and finite source-typed witnesses

Primitive Axiom II is **locally sound** and does not itself imply transitivity (original Proposition 4.12). For any n admitted candidate-expression tags with the same singleton material, the same anchor, identical inherited relational data, and empty configuration/assignment/channel carriers, **every reflexive binary relation** on those tags is a legal original Formation restriction interpretation. This is a deliberately restricted fixture family, not all DSD models.

Exhaustive check over the exact finite fixture universes:

| Number of admitted tags | Reflexive relations enumerated | Preorders (also transitive) | Nontransitive legal core relations | Preorders permitting mutual distinct tags |
| --- | ---: | ---: | ---: | ---: |
| 3 | 64 | 29 | 35 | 10 |
| 4 | 4,096 | 355 | 3,741 | 136 |

All source-typed transitive closures preserve identity and become transitive. The underlying proof of inheritance soundness is **Lemma 4.10**, not enumeration: if `Res(H,h)` and `Res(h,g)`, then `mat(g)⊆mat(h)⊆mat(H)`, `anch_g=anch_H|mat(g)`, and induced relational material records agree. Inductively, any added edge in a finite restriction chain has a legal admitted target and inherited structure. Closure must be recomputed as a primitive relation, not mistaken for a theorem asserting the original edge was already present.

A separately constructed active-channel example has three admitted expressions H,h,g with equal material and anchors; g is describable, `Realize(g,p)`, all three configuration gates true, `q(0)=1`, and one `Role(p,0,lambda,rho)`. Initially `Res(H,h)`, `Res(h,g)`, identity edges hold but `Res(H,g)` does not. Original Formation admits one nonzero channel. The optional transitive closure adds `Res(H,g)`, with the same single channel, while the number of compatible restriction histories for p rises from **2 to 3**. The Python checker tests the finite relation and trace-count shadow, while the full Formation typing is justified in this written construction. It is not an automated universal model checker.

## 4. Source identity `(H|Y)|Z=H|Z` and its actual domain

The Appendix D formula is **further optional**, conditional on an application providing **uniquely induced subexpressions** and defined restriction-selection operations. The basic system supplies a typed binary relation `Res`, not a primitive total function `H|Y`. For an actual induced-subexpression operation, the natural domain is `Z⊆Y⊆mat(H)` together with existence of the selected restricted expressions.

For a uniquely selected induced material structure with anchor restriction, two successive restrictions to nested material domains agree with the direct restriction: `(anch_H|Y)|Z=anch_H|Z`; retained relational records behave analogously. The finite checker executes **341** nested subset triples for sizes 0..4, all consistent with this identity. This demonstrates a finite selected encoding, not a universal proof by enumeration; the abstract identity follows when the induced-restriction operation and extensional uniqueness actually exist.

**Boundary witness:** distinguish two expression tags `g1≠g2` that share the empty induced material/anchor record and are both sound restrictions of H. A globally transitive primitive `Res` still permits the choices `H|∅=g2`, `(H|{0})|∅=g1`. Hence the expression identity need not follow from transitivity *alone*. This violates the extra uniqueness premise, and therefore does **not** refute Appendix D's conditional statement.

## 5. Additional derived observation — not an original Appendix D theorem

For a fixed valid primitive Formation background, adding **only** Axiom-II-sound transitive closure to `Res` does not alter `Ψ(p)` because `Des_expr(h)=>Adm_expr(h)=>Res(h,h)`. Thus the restriction witness in `Ψ` exists whenever a describable h realizes p, with no need for an unrelated source expression H. Holding other primitive data fixed, `K_des`, `A*=A`, assignment domains, admitted channels and finite composites remain unchanged. Nevertheless the *full primitive descriptor* and the detailed `Tr(c)` histories may change (2→3 in the selected witness). This conclusion is a source-derived **audit observation**, not a proposition explicitly stated in Appendix D; its proof depends on the original identity-restriction convention and must not be exported to models where that convention is changed.

## 6. Reproducible execution and audit limits

Executed locally with Python warnings treated as errors, after `python -W error -m py_compile`. GitHub saved code and JSON match the local executed-byte Git blobs.

From cloned repository root on Windows 11:

```powershell
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_appd_restriction.py
```

Default output: `DSD_Audit/audits/formal_proof/formation_axiom_system/results/appd_restriction.json`. An optional first argument supplies another output JSON path.

Finite relation count is exhaustive only among all **reflexive graphs on 3 or 4 labeled tags** under the chosen singleton typed material interpretation; 341 tests are only chosen nested subsets. No external independent validation or proof assistant certification is claimed.

## 7. Verdict and next checkpoint

```text
AUDIT_ID: FAS-F2-APPD-RESTRICT-001
MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND (conditional preorder; relative to original primitive Axiom II plus optional global transitivity)
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE (Appendix D as written)
SOURCE_FORMAL_SCOPE: optional restriction coherence, NOT universal primitive core
INDEPENDENT_EXTERNAL_VALIDATION: not_established
F2_FULL_PAPER_FPA: OPEN
THEOREM_FPA_COMPLETED: 14
PROPOSITION_FPA_COMPLETED: 2
COROLLARY_FPA_COMPLETED: 9
UNNUMBERED_ORIGINAL_SECTION_AUDITS_COMPLETED: 8
ORIGINAL_PDF_ZENODO: unchanged
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged
NEXT: FAS-F2-APPE-INFINITE-001 / NOT_STARTED
```

Previous independent advisories remain outstanding: T4.7 residual-six wording; Section 7.3 D2 boundary inheritance; Section 8 fixed-J logical-strength comparison. The successful optional Appendix D audit does **not** clear them. The Appendix E infinite-family extension is the next independently precommitted unit, not yet begun.


**Notion reciprocal audit page:** https://app.notion.com/p/3ff81f51e7fa816aaf76e9d9fc7ee857
