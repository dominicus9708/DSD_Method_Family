# FAS-F2-SEC4.3-001 — Section 4.3 Structural consequences and non-implications
**2026-10-19 · FPA v0.1 · seven-item, source-bound internal mathematical audit; not paper-wide F2 completion**

```text
SOURCE: DSD_Formation_Axiom_System_EN(5).pdf (Kwon Dominicus; 33 pp.)
SOURCE_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
SOURCE_LOCUS: Section 4.3, printed pp. 11–12
PRECOMMIT: dae15972d8cb3d800bdef4a9f3bcc7d4acfe97b8
ITEMS: Corollary 4.8; Countermodel 4.9; Lemma 4.10;
       Corollary 4.11; Proposition 4.12; Lemma 4.13; Corollary 4.14
MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND (all seven, their original scoped meanings)
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: CLARIFICATION_OPTIONAL (Countermodel 4.9's obligatory identity restriction)
FINITELY_RECONSTRUCTED_WITNESSES: 2 (4.9 and stronger nonvacuous witness for 4.12)
INDEPENDENT_EXTERNAL_VALIDATION: not established
SOURCE_OR_ZENODO_CHANGED: no
F2_FULL_PAPER_VERDICT: not issued
NEXT_UNIT: FAS-F2-G0-001 (Section 2 foundation/typing audit), NOT_STARTED
```

## A. Exact dependency discipline
The mathematical standard is ordinary classical logic and ZFC-relative set-theoretic structures with the manuscript's typed carriers, primitive axioms I–III and V, and definitional closure IV, VI, VII. This section uses:
- **Axiom I**: `Desexpr(x) ⇒ Admexpr(x)`;
- **Axiom II**: if `Res(H,h)`, then `mat(h)⊆mat(H)`, `anch_h=anch_H|mat(h)`, restriction-target admission and induced relational data; also `Admexpr(H)⇒Res(H,H)`;
- **Axiom III**: if `Realize(h,p)`, then `act(p)⊆mat(h)`, `anch_p=anch_h|act(p)`;
- **Closure IV**: `Des_cfg(p) iff Psi(p)`, with `Psi` requiring `ConfAdm(p)` and a witness `Res(H,h)∧Desexpr(h)∧Realize(h,p)`.
Source convention `f|A` restricts to `A∩dom(f)`; all retained material relations are induced on subsets. Distinguish primitive `Res` membership from the derived material/anchor inheritance identities.

## B. Individual items with independent proof/attack

### Corollary 4.8 — non-admission obstruction
For every candidate expression x, from `Desexpr(x) ⇒ Admexpr(x)`, classical contraposition directly yields `¬Admexpr(x) ⇒ ¬Desexpr(x)`. No converse follows. **PASS**. This is an elementary logical consequence, not a novel theorem of contraposition.

### Countermodel 4.9 — admission not sufficient
The manuscript gives `E_B^L={x}`, `Admexpr(x)` true, `Desexpr(x)` false, and says other data can be empty/zero subject to Stages II–VII. **The admitted x still requires `Res(x,x)` under Axiom II**, so setting the entire restriction relation empty would NOT be a legal completion. We completed the source outline as follows:
- `Supp(B)={s0}`, material carrier `M_B^L={a}`, one expression x with `mat(x)={a}`, `anch_x(a)=s0`;
- optional candidate configuration p0 with `act(p0)={a}`, `anch_p0(a)=s0` and configuration-admission/coherence/boundary predicates false; `Realize=∅`;
- `Admexpr(x)=true`, `Desexpr(x)=false`, `Res={(x,x)}`; induced material relations are empty (source allows empty relational material signature);
- assignment domains empty, roles absent, derived `K_des=∅`, `A*=∅`, `C=∅`; supply any F-vector space including zero space with the unique empty term map, `P_fin(C)={∅}`, `Comp(∅)=0_W`.
All primitive axioms are satisfied. Yet `Admexpr(x)∧¬Desexpr(x)`, so converse of Axiom I is not a theorem. **PASS_WITH_OPTIONAL_EXPOSITORY_CLARIFICATION**. This is a slightly more explicit/nonempty principal-carrier realization of the paper's underspecified countermodel, not a verbatim list of its data. No premise strengthening or theorem alteration required.

### Lemma 4.10 — two successive restrictions
From `Res(H,h)`, `Res(h,g)`, obtain `mat(g)⊆mat(h)⊆mat(H)`. Anchor maps satisfy
```text
anch_g = anch_h|mat(g)
       = (anch_H|mat(h))|mat(g)
       = anch_H|mat(g).
```
The equality holds using the source's restriction semantics and the just-proved nestedness. For retained relational material structures and maps to fixed external codomains, induced restriction to two nested subsets equals restriction directly to the smallest subset. **PASS**. Crucially `Res(H,g)` is NOT derived.

### Corollary 4.11 — finite restriction chain
For `H=h0,...,hn` with `Res(h_(i-1),h_i)`, apply Lemma 4.10 inductively to obtain material inclusion and `anch_hn=anch_H|mat(hn)`. If `n=0`, the conclusion is the trivial identity `anch_H=anch_H|mat(H)`, so no unstated positive-length condition is necessary. **PASS**. Nonfinite chains are not asserted.

### Proposition 4.12 — restriction transitivity not implied
Construct distinct expressions `H,h,t` over an inert material b, `mat(H)=mat(h)=mat(t)={b}`, all anchored at s0 and admitted but not describable. Include identity restrictions `Res(H,H)`, `Res(h,h)`, `Res(t,t)`. Declare **`Res(H,h)`, `Res(h,t)`** true but **`Res(H,t)`** false. All true restrictions satisfy Axiom II's target admission, domain/anchor and induced-record requirements. Axiom II contains **no transitivity clause**, so this is legal.

The executed **stronger nonvacuous** witness additionally has admitted/describable g0 and configuration p on material a, `Res(g0,g0)`, `Realize(g0,p)`, all configuration-admission predicates true, `Q_λ={a}`, `q_λ(a)=1`, `Role(p,a,λ,ρ)`, `W=R,T(c)=1`. It has `K_des={p}`, `A*={a}`, `C={c=(p,a,λ,1,ρ)}`. Further candidate configurations p_blocked and p_nowitness on inert b are not describable. This is a **full** Formation model satisfying all four primitive axioms and the supplied closures, yet its primitive Res is nontransitive. **PASS**: genuine non-implication.

### Lemma 4.13 — base inheritance under realization
If `Res(H,h)` and `Realize(h,p)`, Axioms II and III give `act(p)⊆mat(h)⊆mat(H)` and `anch_p=(anch_H|mat(h))|act(p)=anch_H|act(p)`. Induced records transmit by restriction composition within the declared material signature. **PASS**. This does not turn realization or restriction into a transitive primitive relation.

### Corollary 4.14 — two configuration obstructions
From `Des_cfg(p) ⇔ ConfAdm(p) ∧ ∃H,h[Res(H,h)∧Desexpr(h)∧Realize(h,p)]`, the two stated conditions `¬ConfAdm(p)` and `¬∃H,h(...)` each suffice for `¬Des_cfg(p)` by Boolean logic. **PASS**. Neither absence of one selected witness nor negative status of all expressions is inferred from this condition. The nonvacuous witness exercises p_blocked (first obstruction) and p_nowitness (second, despite true configuration-admission predicates).

## C. Adversarial findings

1. **Source 4.9 is abbreviated but repair-free:** since admitted x must have an identity restriction, an interpretation with empty `Res` would be invalid; however the original instruction "remaining sorts by ... data satisfying Stages II–VII" permits and requires `Res(x,x)`. A concrete valid model is exhibited above. This justifies `REVISION_NEED=CLARIFICATION_OPTIONAL`, not `PROOF_GAP` or `DISPROVED`.
2. **Nontransitivity is of the primitive relation:** inherited anchoring/data through two restrictions is valid and does not create a third primitive `Res` edge. The nonvacuous witness separates these.
3. **Finite-chain induction needs no hidden n≥1:** the n=0 case is tautological.
4. **Obstruction is necessary, not sufficient:** 4.14 cannot be inverted; the audit retained the exact direction.
5. **No material new physical implication:** results are logical consequences and counterexamples inside the formation schema.

## D. Computational reproducibility and limits
- [Finite witness Python](../scripts/verify_sec43.py), commit `23aac767ca055965c89f50cb781e46ad6e540c38` (Python 3.10+ stdlib).
- [Finite witness JSON](../results/sec43_witnesses.json) — generated from the local executable witness checker. Same-project checks only.
- Local execution produced:
```text
PASS: 4.9 admitted-not-describable, identity restriction preserved
PASS: 4.12 nontransitive Res with active channel
PASS: 4.10/4.11/4.13 restricted-anchor inheritance checks
PASS: 4.8/4.14 edge and obstruction fixtures
```
- For a checked-out repository root, on Windows 11:
```powershell
py -3.11 DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_sec43.py --output DSD_Audit\audits\formal_proof\formation_axiom_system\results\sec43_witnesses.json
```
- The executable enumerates model-specific finite restriction chains, and checks typed anchoring/relations for its chosen finite witness models. The universally quantified proof conclusions rely on the **separate written mathematical derivations** above, not numerical sampling; no proof-assistant certification or external replication is claimed.

## E. Gate-by-gate disposition
```text
G01 Cor 4.8 contrapositive: PASS
G02 Countermodel 4.9 full-model legality and required Res(x,x): PASS_WITH_EXPOSITION_BOUNDARY
G03 Lemma 4.10 anchor/composition: PASS
G04 Cor 4.11 all finite n incl. n=0: PASS
G05 Prop 4.12 nontransitivity, all axioms and active kernel: PASS
G06 Lemma 4.13 relation/anchor inheritance: PASS
G07 Cor 4.14 two independent necessary-condition obstructions: PASS
G08 typed / closure / supplied term layers: PASS_WITH_SCOPE
G09 possible overstrong text and under-specification: PASS_WITH_OPTIONAL_CLARIFICATION
G10 seven verdicts separated and limits recorded: PASS
G11 finite witness code and bounded evidence: PASS
G12 stop and future source lock: PASS
```

## F. Verdict and checkpoint
**Within the declared typed set-theoretic background, all seven mathematical claims in Section 4.3 are supported by direct derivations and explicit legal countermodels.** The only identified adjustment is an **optional detailed formulation of Countermodel 4.9** to make its Axiom-II identity restriction unmistakable. No primitive axiom, theorem statement, definition or Zenodo manuscript revision is currently required. This disposition does not erase the earlier separate **Theorem 4.7 language clarification**.

**STOP HERE.** Next suggested logically upstream work unit: `FAS-F2-G0-001`, a foundational Section 2 type/signature/primitive-status audit, or otherwise the pre-existing G1 Theorem 3.6 according to dependency order. The exact scope of the next case must be prospectively locked; neither case has begun. F2 whole-paper verdict: OPEN.
