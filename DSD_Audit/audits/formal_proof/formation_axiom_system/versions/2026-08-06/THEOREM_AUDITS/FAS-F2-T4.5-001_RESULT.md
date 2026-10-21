# FAS-F2-T4.5-001 — primitive-axiom independence audit / 원시공리 독립성 감사

**2026-10-19 · FPA v0.1 · One-theorem result only.**

```text
AUDIT_ID: FAS-F2-T4.5-001
SOURCE: DSD_Formation_Axiom_System_EN(5).pdf / 33 pages / §4.1 pp.9–10
SOURCE_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
PRECOMMIT_COMMIT: 4d7ed1e6a16c01f0bc2a4d17fc5d3bc1a0472f45
PRECOMMIT_BLOB: 89993ec145be104eace74049098a94c9b5e0abe1
MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE
CHECKS: 10/10 reviewed and supported
FINITE_COUNTERINTERPRETATIONS: 4/4 reproducible (same-project)
INDEPENDENT_EXTERNAL_VALIDATION: not_established
PAPER_WIDE_F2_CERTIFICATE: not_issued
NEXT_AUDIT: FAS-F2-T4.7-001 / not_started
ZENODO_CHANGE: none
```

## A. Exact theorem and applicable logical standard

Theorem 4.5 of the frozen manuscript asserts **mutual independence of Primitive Axioms I, II, III and V, relative to its typed background and Definitional Closure Clauses IV, VI and VII**. The named Countermodels 4.1–4.4 are finite **typed counterinterpretations of the axiom-deleted theory**. By Definition 2.2, no interpretation that violates one of the four axioms is itself a full Formation model. The word *countermodel* is therefore interpreted in the ordinary relative-independence sense, not as an admitted full DSD model.

Mathematical obligation for each `i ∈ {I,II,III,V}`: construct `M_i` satisfying the declared typed background, the other three primitive axioms, and the definitional closures, with `M_i ⊭ i`. Under ordinary sound mathematical reasoning this refutes any derivability of `i` from the other three in that fixed background. No axiom is claimed to be independent of the typing rules that already force part of its clauses.

## B. Frozen common finite base (§4.1, printed pp.9–10)

- `Supp(B)={s0,s1}`, `s0 ≠ s1`; material-record set `M_B={a,b}` with **empty relational material signature** (inheritance of relations/annotations is therefore vacuous).
- Original admitted, describable expression `g` has `mat(g)={a}` and `anch_g(a)=s0`.
- Configuration `p` has `act(p)={a}`, `anch_p(a)=s0`; all three admission/coherence/boundary predicates true at p.
- `Res(g,g)`, `Realize(g,p)`; these are sound, and the identity restriction required for the admitted g exists.
- `Λ={λ}`, `V_λ=ℝ`, `Q_λ={a}`, `q_λ(a)=1`; `Λ^δ=∅`, `R={ρ}`, `Role(p,a,λ,ρ)`, `W=ℝ`, `T(c_g)=1`.
- Unlisted predicates and relations are false, as explicitly stated by the manuscript. Derived `Ψ(p)=true`, `K_des={p}`, `A*={a}`, and Clause VI `C={c_g=(p,a,λ,1,ρ)}`. Clause VII yields `Comp(∅)=0`, `Comp({c_g})=1`.

## C. Countermodel-by-countermodel mathematical verification

| Source counterinterpretation | I | II | III | V | Unique violated requirement |
|---|---|---|---|---|---|
| Countermodel 4.1 | **FALSE** | TRUE | TRUE | TRUE | `Desexpr(x)` but `¬Admexpr(x)`, with x excluded from all restriction/realization relations |
| Countermodel 4.2 | TRUE | **FALSE** | TRUE | TRUE | `Res(H,h)` with `mat(H)=mat(h)={b}` but `anch_H(b)=s0 ≠ s1=anch_h(b)` |
| Countermodel 4.3 | TRUE | TRUE | **FALSE** | TRUE | `Realize(h,p')` with `act(p')=mat(h)={b}` but anchors disagree |
| Countermodel 4.4 | TRUE | TRUE | TRUE | **FALSE** | `Q_λ={a,b}` while `A*={a}` |

### Countermodel 4.1: Primitive Axiom I
The extra `x` uses inert material `{b}` and a legal anchor `s0`, with `Desexpr(x)=true` and `Admexpr(x)=false`. Neither `Res` nor `Realize` involves x; thus Axiom II's target-admission restriction does not force x to be admitted. I fails and II, III, V remain satisfied. The active p/g/c_g kernel is unchanged.

### Countermodel 4.2: Primitive Axiom II
Admitted, **non-describable** expressions H and h both have material `{b}`. Sound identity restrictions `Res(H,H)` and `Res(h,h)` satisfy the admitted-expression identity obligation; the added `Res(H,h)` preserves its target's admission and material-domain inclusion but **fails anchor inheritance**, which is a residual II condition. With no other new realization and no new describable expression, I, III, V hold. No implicit transitivity is assumed.

### Countermodel 4.3: Primitive Axiom III
Add admitted, non-describable h with `Res(h,h)` sound. Add p' with `act(p')={b}`, opposite anchor `s1` and `Realize(h,p')`; the restriction source anchor of h is `s0`, so III fails its realization anchoring requirement. The three configuration-admission predicates are all false at p'; hence `Ψ(p')=false`, p' does not enter `K_des` or `A*`, and q's unchanged domain `{a}` still satisfies V. I and II remain true.

### Countermodel 4.4: Primitive Axiom V
Extend only the **function domain** and the function by q(b)=1. The regime-global partial map remains a well-typed single-valued function into ℝ. But b is not in any describable configuration's active material; `Q={a,b} ⊄ A*={a}`. This is the actual V violation; single-valuedness follows from typed-function declaration, not from a second independent axiom. I–III, p and c_g remain unchanged.

## D. Verification beyond just one violated predicate

1. Every extra expression and configuration has a legal material subset and total support-anchor map over that subset. All material-internal relation restrictions satisfy the *empty material signature* convention.
2. Admitted-expression identity restrictions hold **unless II itself is targeted**; the II target case 4.2 still preserves all identity restrictions and fails only its chosen cross-anchoring clause.
3. Every `Realize` pair other than the deliberately bad 4.3 pair satisfies III's inclusion and anchor requirement. The unrealized new expressions introduce no hidden realization defects.
4. All `Ψ` and `Des_cfg` predicates are re-evaluated from source relations, including when a primitive axiom is deliberately false. Every case retains exactly `K_des={p}`, `A*={a}`, `C={c_g}`.
5. Axiom IV, VI, VII are **definitional** and can be interpreted for every well-typed primitive input (including one violating I/II/III/V), under Theorem 3.3's stated source-relative supplied W/T regime.
6. Term map `T(c_g)=1` is defined and the finite-composite family is not empty: `P_fin({c_g})={∅,{c_g}}`. Nonvacuity is genuine for all four cases.
7. No other axiom is violated under the source-listed declarations; the four distinct finite structures supply four relative non-entailment certificates.

## E. Reproducibility: bounded same-project checks, not a formal proof assistant

A standard-library Python script reconstructs exactly the common finite base and the four source-listed modifications, computes the full truth table for I, II, III, V and rederives `K_des,A*,C` and the two finite composites.
- [Executable script](../scripts/verify_t45_countermodels.py)
- [Frozen deterministic JSON results](../results/t45_axiom_independence.json)
- Script source commit: `c43478cd4570d0cbc3aabf0cb9cf976021ca89b7`
- Results commit: `55aaa3979e6998d51b9af47e95ed5fdf53b8a104`
- The local run of the verifier produced the output line: `4/4 source-listed axiom-independence counterinterpretations reproduced`.
- No external input files are required; the source-listed example data are embedded and validated by assertions.

From **repository root** on Windows 11 / PowerShell:
```powershell
py -3.11 DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_t45_countermodels.py --output DSD_Audit\audits\formal_proof\formation_axiom_system\results\t45_axiom_independence.json
```
The generated file is a reproducibility supplement; reasoning that one counterinterpretation per omitted axiom refutes a corresponding implication is ordinary mathematics. The run is **not** independent third-party replication, not a machine-checked formal proof of all Formation results, and does not audit Theorem 4.7.

## F. Predeclared ten gates

```text
G01 typed carriers/identity restrictions: PASS
G02 four complete axiom truth tables: PASS
G03 restriction/realization anchor soundness & inherited data: PASS
G04 closure IV and full describable status recomputed: PASS
G05 VI/VII and nonempty admitted-channel kernel: PASS
G06 non-vacuity of each axiom-deleted interpretation: PASS
G07 valid distinction counterinterpretation vs full DSD model: PASS_WITH_BOUNDARY
G08 adverse edge cases as specified in precommit: PASS
G09 independence theorem vs residual clausewise Theorem 4.7: PASS_WITH_BOUNDARY
G10 mathematical/audit/revision/evidence scope separated: PASS
```

## G. Final scoped judgment and next theorem

**Theorem 4.5 (mutual independence of the four primitive axioms) is justified relative to the source's typed background and definitional closure regime.** Each independent failure is witnessed by a legal finite counterinterpretation with an active channel. No essential assumption omission or internal contradiction was found for this theorem. No amendment to the frozen English manuscript or its Zenodo record is warranted by this finding.

**Separate questions remain open**: Theorem 4.7 residual-clausewise independence; exact external literature novelty; independent outside replication; other F2 theorems; and any issue requiring different source versions.

```text
NEXT_EXECUTION: FAS-F2-T4.7-001
NEXT_STATUS: NOT_STARTED
SOURCE_LOCK: preserved
METHOD_FAMILY_22_OF_22: unchanged
```
