# FAS-F2-T6.17-001 — Staged determinacy and nonbranching of definitional closure

**2026-10-19 KST · Formal Proof Audit v0.1 · Source-bound internal mathematical review, NOT independent external validation.**

```text
AUDIT_CASE: FAS-F2-T6.17-001
PARENT_METHOD: existing DSD Audit / FPA v0.1
SOURCE: Kwon Dominicus, DSD_Formation_Axiom_System_EN(5).pdf (33 pages)
ATTACHED_SOURCE_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
SOURCE_LOCUS: Theorem 6.17 (printed pp.21–22); Definition 2.1/2.4; Clauses IV/VI/VII; Definition 6.15
PRECOMMIT_COMMIT: e3893b65d5783e160f24a50cd3484a513f81de00
PYTHON_COMMIT: 810994061f9ef17f432cbd3dd4d20dfa7dd978cf
FINITE_JSON_COMMIT: 5a123ade1a74e39eb6e5ec64b5ab9292fb0dc8de
MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE
GENERAL_I3_EQUALS_I4: PROVED
NEXT: FAS-F2-C6.18-001 / NOT_STARTED
F2_WHOLE_PAPER: NOT_COMPLETE
INDEPENDENT_EXTERNAL_VALIDATION: not_established
ORIGINAL_PDF_ZENODO: unchanged
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged
```

## 1. Locked statement: four logically distinct claims

The exact source Theorem 6.17 makes four claims over **full** formation models L,M:

**(i) Unique staged determination:** the Stage 4 truncation is uniquely determined by Stage 3. Stage 6 is uniquely determined by Stage 5 **together with Role_L**, and Stage 7 is uniquely determined by Stage 6 **together with supplied W_L and T_L**. There is no claim that Stage 5 alone determines the Role predicate, or Stage 6 alone determines the vector-space and term map.

**(ii) No independent Stage-4 comparison obstruction:** `I_3(L,M)=I_4(L,M)` for Definition 6.15 stage-comparison subsets of the **same ambient full comparison-tuple universe**.

**(iii) Stage-6 channel bijection:** every `Theta∈I_6(L,M)` induces a bijection of **candidate-channel** universes `U_L→U_M`, preserves and reflects `Chan`, and restricts to a bijection `C_L→C_M`. A Stage-6 term-space component `J` is still arbitrary and need not be linear.

**(iv) Stage-7 family/composite transport:** every `Theta∈I_7(L,M)` gives the induced bijection `P_fin(C_L)→P_fin(C_M)` and preserves finite composite descriptions under the **now F-linear isomorphism** `J`, together with (E9). The term map is defined on admitted channels, not all candidate channels.

These are scope-specific source claims, not a statement that arbitrary staged *records* are themselves full formation models or that all two regimes are strictly isomorphic.

## 2. General mathematical proof (not derived from finite tests)

### 2.1 Claim (i): definitional determination

For any candidate configuration `p∈P_B^L`, Definition 2.1 declares the primitive witness formula (all six conjuncts essential):

```text
Psi_L(p) :=
 exists H,h [
     Res_L(H,h) and Desexpr_L(h) and Realize_L(h,p)
     and Admcfg_L(p) and LC_L(p) and BC_L(p)
 ].
```

All sorts, restriction and realization, expression describability and the three primitive configuration predicates occur by Stage 3. This data determines `Psi_L` pointwise. Then `A*_L := union_{Psi_L(p)} act_L(p)`, `Descfg_L(p) iff Psi_L(p)`, `K_des,L := {p:Descfg_L(p)}` and `A_L := union_{p∈K_des,L}act_L(p)=A*_L` are uniquely determined by Closure IV. Thus the **Stage 4 truncation** is unique.

Given a fixed Stage 5 truncation and the separately **supplied Role_L**, the kind-indexed disjoint union

```text
U_L := disjoint_union_{lambda∈Lambda_L}
            (P_B^L × M_B^L × {lambda} × V_L,lambda × R_L)
```

is uniquely defined by the typed Stage-0/5 data. For every `p`, the global partial graph `Gamma_L,lambda` determines the local graph `Gamma_L,lambda(p)=Gamma_L,lambda∩(act_L(p)×V_L,lambda)`; no undefined assignment is padded by zero. Closure VI sets

```text
Chan_L(p,a,lambda,v,rho)
  iff Descfg_L(p)
   and (a,v)∈Gamma_L,lambda(p)
   and Role_L(p,a,lambda,rho);
C_L := {c∈U_L:Chan_L(c)}.
```

Therefore Stage 6 is unique **relative to Role_L**, even when `U_L` is infinite. Given that stage, and *independently supplied* `F`-vector space `W_L` and `T_L:C_L→W_L`, Closure VII makes `Dcomp_L=P_fin(C_L)` and `Comp_L(F)=∑_{c∈F}T_L(c)` unique, for each finite `F`, including the empty family. This is the precisely **relative** uniqueness of Stage 7. It introduces no new primitive datum beyond the declared supplied `W_L,T_L`.

### 2.2 Claim (ii): general proof of I3=I4

Nestedness already proved in T6.16 yields `I_4⊆I_3`. For the reverse direction, let an **arbitrary** full comparison tuple `Theta∈I_3(L,M)`, with bijections `Phi_M,Phi_E,Phi_P,tau_Lambda,tau_R,{I_lambda}` and arbitrary `J` before Stage 7.

By I0–I3 requirements, E2 ensures `Desexpr_L(h) iff Desexpr_M(Phi_E(h))`, E3 preserves and reflects `Res` and `Realize`, and I3 preserves and reflects `Admcfg,LC,BC`. If `(H,h)` witnesses `Psi_L(p)`, its image `(Phi_E(H),Phi_E(h))` witnesses `Psi_M(Phi_P(p))`. Conversely, if `(H',h')` witnesses the latter, surjectivity of the *expression* bijection supplies `H=Phi_E^{-1}(H')` and `h=Phi_E^{-1}(h')`; backwards E2/E3 and config-predicate iff return a source witness. Hence

```text
for every source p:
   Psi_L(p) iff Psi_M(Phi_P(p)).
```

Closure IV gives the same iff for `Descfg`. **Surjectivity of Phi_P** (not merely injectivity) ensures `Phi_P[K_des,L]=K_des,M`.

To check the further derived active-material aggregate explicitly, E1 makes `Phi_M[act_L(p)]=act_M(Phi_P(p))`. As image under a function distributes across arbitrary unions and `Phi_P` carries `K_des,L` onto `K_des,M`,

```text
Phi_M[A*_L]
 = Phi_M[union_{p∈K_des,L} act_L(p)]
 = union_{p∈K_des,L} act_M(Phi_P(p))
 = union_{p'∈K_des,M} act_M(p')
 = A*_M.
```

`A_L=A*_L` holds on both full models, so its exact image agrees too. **No new comparison constraint** arises at I4. Thus `Theta∈I4`, `I3⊆I4`, and together `I3=I4` for **all** fixed-base full Formation descriptors. This is a general proof, not inference from eight earlier T6.16 finite cases.

### 2.3 Claim (iii): candidate/channel bijection at I6

For `Theta∈I6`, its ambient components give bijective maps on configurations, material items, kinds and roles. For each kind `lambda`, the zero-preserving **bijective** pointed value map `I_lambda:V_L,lambda→V_M,tauLambda(lambda)` completes the typed candidate map

```text
hatTheta(p,a,lambda,v,rho) =
   (Phi_P(p), Phi_M(a), tauLambda(lambda), I_lambda(v), tau_R(rho)).
```

This is a bijection `U_L→U_M`: to invert a target candidate, **first invert tauLambda to identify source kind**, then use that kind's `I_lambda^{-1}` and inverse remaining component bijections. Its surjectivity is over the **entire disjoint candidate-channel universe**, not merely `C_L`.

I3/I4 and Closure IV give the configuration describability iff. I0/E1 gives exact active-material image, and I5/E5/E6 gives regime-global assignment graph iff; therefore the **local graph** condition `(a,v)∈Gamma_L,lambda(p)` is equivalent to its target image (including defined zero versus undefined). I6/E8 gives the role iff. Each conjunct of Closure VI is now reflected and preserved:

```text
for every c∈U_L:
    Chan_L(c) iff Chan_M(hatTheta(c)).
```

Hence restriction of `hatTheta` to admitted channels is bijective `C_L→C_M`. No F-linearity, invertibility or term preservation for `J` was invoked. Such restrictions are added only at I7.

### 2.4 Claim (iv): finite families and F-linear transport

At I7, the induced channel bijection yields the finite-powerset bijection with inverse `G↦hatTheta_C^{-1}[G]`. E9 and the now-required F-linear isomorphism `J:W_L→W_M` give, for every finite `F⊆C_L`,

```text
J(Comp_L(F))
 = J(sum_{c∈F}T_L(c))
 = sum_{c∈F} J(T_L(c))
 = sum_{c∈F} T_M(hatTheta_C(c))
 = sum_{d∈hatTheta_C[F]}T_M(d)
 = Comp_M(hatTheta_C[F]).
```

The second-to-last identity uses channel **injectivity**: neither multiplicities nor identity collisions may be silently introduced into a finite **set** sum. The empty-set case uses `J(0)=0`. A defined-zero assignment `v=0` may still produce a nonzero term, and positive/negative terms may cancel: neither possibility changes channel membership.

Therefore **all four source assertions are proved relative to the declared full-model/typed-map background**. There is no hidden additional axiom, and this theorem does **not** imply that Stage 6 uniquely determines the independently supplied Role relation, nor Stage 7 the independently supplied term map.

## 3. Executed selected finite fixture and adversarial probes

The source-typed Python implementation is [verify_t617_closure_nonbranching.py](../scripts/verify_t617_closure_nonbranching.py); frozen [JSON](../results/t617_closure_nonbranching.json). Both were generated from the **locally executed** successful verifier on 2026-10-19; uploaded GitHub source was not separately executed by an independent external runner.

Two related formation-finite full-model fixtures include two material items, three expressions (H,h,x) with an **actual proper restriction H→h**, three configurations (one with a valid Stage-IV witness, one failing configuration-admission, one with no realization witness), full anchor/restriction/realization inheritance, two quantity kinds with three-value pointed sets, two role kinds and two admitted operational channels. One assigned channel has **defined value 0**; assignments for material b remain undefined. Source terms are `+5,-5` and target terms `+15,-15` under F-linear `J(t)=3t` on `W=Q`.

| Finite selected test | Recorded outcome |
|---|---|
| Material/expression/configuration bijection triples examined | **72** |
| Triples satisfying complete Stage-3 conditions | **1**; also satisfied Stage-4 |
| All source candidate channel typed-membership equivalences | **72/72** |
| Admitted source/target channel bijection | **2 to 2** |
| Finite channel-family terms transported under J | **4/4**, including empty set |
| Nonempty cancellation (sum 0) | **1** verified |
| Defined-zero versus undefined assignment | Distinguished |
| Change independently supplied Role, Stage-5 unchanged | Different Stage-6 admitted channels |
| Change supplied T with Stage-6 unchanged | Different Stage-7 composites |
| Break LC or Realize while otherwise using maps | Rejected at Stage-3, cannot falsify I3=I4 |
| Use ordinary J=id with transported term factor 3 | Not E9-compatible; admissible pre-Stage7, rejected at I7 |

The selected fixture demonstrates actual dependencies, but **72** is the number of carrier/expression/configuration triples of *these two models*; it is neither an exhaustive enumeration of all full comparison tuples including arbitrary `J` and all value maps, nor of all possible Formation models. The general proof of I3=I4 is §2.2, not a computational extrapolation.

Run from the cloned `dominicus9708/DSD_Method_Family` repository root on Windows (standard-library Python):

```powershell
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_t617_closure_nonbranching.py
```

Default output: `DSD_Audit/audits/formal_proof/formation_axiom_system/results/t617_closure_nonbranching.json`. The first optional CLI argument may override the output path.

## 4. Formal audit gates and determination

- G01 source SHA/version: **PASS**; SHA-256 of attached 33-page PDF matched; Zenodo byte-equivalence not claimed.
- G02 source dependencies: **PASS**; Definition 2.1/2.4, Clauses IV/VI/VII, Definition 6.15 and type background; no circular import from T6.17.
- G03 typed quantified inference: **PASS**; expression/configuration surjectivity in (ii), kind-indexing of pointed maps in (iii), source full-model limitation.
- G04 axioms versus definitional stages: **PASS**; `W_L,T_L` and Role are **supplied** inputs, not silently derived.
- G05 general mathematical derivation: **PASS**; all parts (i)–(iv) and `I3=I4` proven as separate obligations.
- G06 existence and uniqueness: **PASS_WITH_BOUNDARY**; uniqueness *relative to declared supplied data*, not canonical `Role,W,T` for a fixed lower truncation.
- G07 adversarial: **PASS**; missing witness, changed primitive predicate, role/term modification and zero-vs-undefined separated.
- G08 selected finite vs universal: **PASS_WITH_BOUNDARY**; one source-compatible finite family, not full-model class certification.
- G09 comparisons and composites: **PASS**; Stage6 arbitrary `J`, Stage7 F-linear `J`; injectivity for set sums.
- G10 external mathematics/background: **PASS**, ordinary typed set/function reasoning, F-vector finite sum.
- G11 dependency impact: **PASS_WITH_BOUNDARY**, Corollary 6.18 now has a mathematical premise but is **NOT independently audited**; downstream T6.19/T6.20 remain open.
- G12 independent status: **PASS**, internal source-bound reasoning not an external certified review.

**Scoped verdict:** `PROVED_IN_DECLARED_BACKGROUND / PASS_WITH_BOUNDARY / REVISION_NEED=NONE`.

**No** original PDF or Zenodo edit. Historic Theorem 4.7 wording-clarification recommendation remains separately open. **The full Formation F2 manuscript remains not completely audited.** The user's previously standardized 22/22 DSD Method Family methods remain unchanged.

**Resumable checkpoint:** `FAS-F2-C6.18-001`, Corollary 6.18 (closure-stage exclusion, b≠4), **NOT_STARTED** pending its own prospective precommit.

[Notion synchronized FAS-F2-T6.17-001 audit](https://app.notion.com/p/3fe81f51e7fa81c0a65dcb1005d56f71)
