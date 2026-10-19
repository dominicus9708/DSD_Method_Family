# FAS-F2-T6.16-001 — First-branching obstruction: source-bound formal proof audit

**2026-10-19 KST · FPA v0.1 · Bounded theorem-level mathematical audit (not external independent certification)**

```text
AUDIT_CASE: FAS-F2-T6.16-001
METHOD: Existing DSD Audit / Formal Proof Audit v0.1
SOURCE: Kwon Dominicus, DSD_Formation_Axiom_System_EN(5).pdf, 33 pages
ATTACHED_SOURCE_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
SOURCE_LOCUS: §6.4 Definition 6.15 and Theorem 6.16, printed pp.20–21
PRECOMMIT_COMMIT: 4b8fce7fc7b2133aa9d1a85b3a075a77889b42d4
REPRODUCIBLE_PYTHON_COMMIT: 06806b855360fa3a76f5c9e3128938c901f75cfb
FINITE_JSON_COMMIT: 4587ba6c86859cdeefa26b055874af69ad6b7287
MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND
FPA_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE
NEW_AXIOM_OR_ASSUMPTION: not needed
F2_WHOLE_PAPER_AUDIT: OPEN
INDEPENDENT_EXTERNAL_VALIDATION: not_established
ORIGINAL_PDF_ZENODO: unchanged
NEXT: FAS-F2-T6.17-001 / NOT_STARTED
```

## 1. Exact source obligations and stage inventory

Theorem 6.16 (First-branching obstruction) makes **exactly** three claims for full source descriptors `Sigma_L,Sigma_M∈FormDesc_(B,F)`:

1. For every `0≤k<7`, `I_(k+1)(L,M)⊆I_k(L,M)`.
2. `I_7(L,M)≠∅` if and only if `Sigma_L≅^fix_B Sigma_M`.
3. If `I_7=∅`, the first branching index `b=min{k∈{0,...,7}:I_k=∅}` exists; strict base-fixed formation isomorphism fails, and when `b>0`, every earlier stage `I_j`, `j<b`, is nonempty.

**Locked Definition 6.15 stage inventory**:

| Stage | Added requirement |
|---|---|
| I0 | (E1) material-record isomorphism, exact anchored material/active structure |
| I1 | (E2) expression admission and describability preservation/reflection |
| I2 | Restriction part of (E3) |
| I3 | Realization part of (E3) and 3 primitive configuration predicates of (E4) |
| I4 | Derived configuration describability and exact `K_des` image per (E4) |
| I5 | (E5) domain, (E6) assignment graphs, (E7) qualified negligible size/threshold |
| I6 | (E8) role relation |
| I7 | `J` must be F-linear isomorphism and (E9) component-term transport |

The **ambient population is common across all I0–I7** and consists of *full comparison tuples*
`Theta=(Phi_M,Phi_E,Phi_P,tau_Lambda,tau_R,{I_lambda},J)`.
Carrier/kind/role/pointed-value components are source-typed **bijections**, with distinguished-zero preservation for `I_lambda`. However, `J:W_L→W_M` is initially an **arbitrary map** and only becomes constrained to be an F-linear isomorphism at I7. This distinction is essential; demanding a linear or bijective J in I0 would shift legitimate first-obstruction stages and invalidate the locked construction.

## 2. General mathematics / exhaustive proof of the source claims

Let `A(L,M)` denote the declared common ambient collection of full comparison tuples. Let `P_0(Theta),...,P_7(Theta)` represent the eight stage predicates above. By Definition 6.15,

```text
I_k(L,M) = { Theta ∈ A(L,M) : P_0(Theta) ∧ ... ∧ P_k(Theta) }.
```

For every 0≤k<7, a conjunction through `P_(k+1)` implies the conjunction through `P_k`. Therefore `I_(k+1)⊆I_k`, independently of whether any set is empty, whether the ambient class is large, or whether one tuple fails one particular predicate.

The source's E1–E9 are **exhaustively partitioned by I0–I7**: I0 covers E1; I1 E2; I2 and I3 E3; I3 and I4 E4 (including its derived configuration-describability consequence); I5 E5–E7; I6 E8; I7 E9 and the separately required linear bijective `J`. The ambient tuple already supplies the source-required bijective carrier/kind/role/zero-pointed `I_lambda` maps. No missing requirement of Definition 6.10 is left at Stage 7, and no stricter requirement is added. Consequently:

```text
Theta ∈ I_7(L,M)  iff  Theta is a strict base-fixed formation isomorphism.
I_7(L,M) ≠ ∅     iff  Sigma_L ≅^fix_B Sigma_M.
```

If `I_7=∅`, the subset of `{0,...,7}` defined by `{k : I_k=∅}` contains 7 and is thus a **nonempty finite set**. It possesses a minimum `b`. For any `j<b`, minimality entails `I_j≠∅`; nestedness further entails all `I_k` with `k≥b` are empty. Since `I_7=∅`, the source descriptors cannot be strictly isomorphic by the previous equivalence.

There is **no statement that each descriptor pair is comparable**, nor that a failure of one candidate tuple implies failure of the entire stage: `I_k=∅` quantifies over the *whole* ambient family of comparison tuples. An isomorphic pair can have many failing comparison tuples and at least one final survivor.

**Stage 0 boundary:** `b=0` means no candidate survives ambient typing plus anchored-background (E1), not "formation Stage 0" as an eighth formation stage. The first formation-stage obstruction `b>0` begins at index 1. The theorem does **not** assert `I_3=I_4`; this independent consequence of definitional closure belongs to subsequent Theorem 6.17 (not promoted here).

## 3. Source-typed finite adversarial fixture (supplement, not a general proof)

[Executable finite Python](../scripts/verify_t616_branching.py) and [deterministic results JSON](../results/t616_first_branching.json). The executable was **actually run locally** on the attached source case's reconstructed typed interface; the stored code mirrors the locally tested implementation. A separate external review or a fresh GitHub checkout-run is not asserted.

All eight source-target pairs use two candidate expression records, a candidate configuration, material anchor codes `s0/s1`, one quantity kind with a zero-preserving bijective pointed space, one role kind and a finite F2-vector term space. The fixture explicitly checks the source-relevant admission, des expression, identity restriction, Res/Realize material inheritance and anchor, partial assignment-domain active-area, role typing, and admitted-channel term domain. It then **exhaustively enumerates all full ambient comparison tuples of this finite chosen signature**, including every set-map `J` before Stage 7, and filters the SAME tuple identifiers at every stage.

| Case | Ambient tuple count | I0,I1,I2,I3,I4,I5,I6,I7 survival counts | First b |
|---|---:|---|---:|
| A strict-isomorphic baseline | 8 | 8,8,8,4,4,4,4,1 | undefined |
| Anchor incompatibility | 8 | 0,0,0,0,0,0,0,0 | 0 |
| Expression admission mismatch | 8 | 8,0,0,0,0,0,0,0 | 1 |
| Restriction relation mismatch | 8 | 8,8,0,0,0,0,0,0 | 2 |
| Realization mismatch | 8 | 8,8,8,0,0,0,0,0 | 3 |
| Assignment graph/domain mismatch | 8 | 8,8,8,4,4,0,0,0 | 5 |
| Role mismatch | 8 | 8,8,8,4,4,4,0,0 | 6 |
| W-vector dimension mismatch (J not isomorphism) | 32 | 32,32,32,16,16,16,16,0 | 7 |

**Finite checker assertions**:
- 7 inclusions per fixture × 8 fixtures = **56** successful set-inclusion assertions.
- All **8** tests verify equivalence of final-stage nonemptiness and whether the first branching index is undefined.
- All 8 first indices agree with predicted `None,0,1,2,3,5,6,7`.
- **Most important adversarial check:** one *strict-isomorphic* example has eight candidate full tuples at I0; seven ultimately fail, but one survives I7. Its first branching index stays undefined. Choosing an early failing candidate is therefore not a valid stage-level obstruction argument.
- In these selected legal fixtures `I3=I4` is also observed; this is **not proof** of Theorem 6.17 for all models, and this result does not count it as a completed obligation.
- The Stage 7 dimension-mismatch example demonstrates why J must remain an arbitrary map through I6; if it had been prematurely required to be a vector-space isomorphism at I0, the source's genuine `b=7` example would disappear.
- Results are **not a finite exhaustive search over all possible full Formation models**. The enumerated ambient tuple space is exhaustive only *within each selected finite fixture*.

Reproduce from the root of cloned `dominicus9708/DSD_Method_Family` on Windows:

```powershell
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_t616_branching.py
```

Default output is `DSD_Audit/audits/formal_proof/formation_axiom_system/results/t616_first_branching.json`; optional first CLI positional argument overrides the output path. The script uses Python standard library only.

## 4. Audit gates and publication scope

- G01 source lock: **PASS**, checked current attached PDF 33 pp and SHA256; Zenodo bytes not independently compared.
- G02 source order/noncircularity: **PASS**, stage definitions and original E1–E9 suffice; not reliant on desired T6.16 itself.
- G03 type/quantifiers: **PASS_WITH_BOUNDARY**, full comparison tuples, fixed (B,F), arbitrary J at pre-7 stages, collective emptiness rather than failure of individual maps.
- G04 axioms versus closure: **PASS**, no new axiom; Stage 4 is the derived closure check.
- G05 mathematical proof: **PASS**, staged conjunction nestedness, exact strict-E1–E9 coverage and nonempty finite minimum.
- G06 existence/uniqueness: **PASS_WITH_BOUNDARY**, b only defined when I7 empty; full tuple failure must be collective.
- G07 adversarial: **PASS**, invalid stage inference from one failing map refuted by strict-isomorphic baseline.
- G08 finite/general: **PASS_WITH_BOUNDARY**, typed finite exhaustive ambient enumeration within chosen examples, not universal model certification.
- G09 invariance: **PASS_WITH_BOUNDARY**, no statement here that b is symmetric or strict-isomorphism invariant (reserved for T6.19).
- G10 background set/class algebra: **PASS**, ordinary set predicates/finite minimum, fixed-base metatheoretic class convention.
- G11 downstream: **PASS_WITH_BOUNDARY**, Theorem 6.17, Corollary 6.18, Theorem 6.19 etc. remain NOT_REVIEWED.
- G12 external evaluation: **PASS**, internal author-assisted source audit not third-party certification.

**Scoped mathematical verdict:** `PROVED_IN_DECLARED_BACKGROUND`. **FPA verdict:** `PASS_WITH_BOUNDARY`. **Revision need:** `NONE`. The boundaries are the source's full descriptor and common ambient tuples, `b`'s conditional definedness, and scope of selected finite evidence; there is no new substantive premise needed to prove Theorem 6.16.

The preexisting Theorem 4.7 residual-constraint wording-clarification recommendation remains unchanged. No original English PDF or Zenodo revision is required by this scoped finding. The 22/22 method-family internal standardization is unaffected. **F2 full-manuscript audit remains OPEN.**

**Resumable checkpoint:** `FAS-F2-T6.17-001`, *Staged determinacy and nonbranching of definitional closure* (including `I3=I4` as a **general** theorem), **NOT_STARTED**. Do not assert it completed based on these finite samples.
