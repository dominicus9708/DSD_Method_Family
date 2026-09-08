# QM Core Reconstruction 004H — Exact Tomographic Composite Tensor Gate

Date: 2026-09-08  
Status: **PASS_WITH_REFINEMENT**  
Program: **Core-Theory Reconstruction Challenge**  
Target: resolve the `ETC-QM` gap isolated by QM Core 004E by separating local-readout injectivity from independent product composition and from exact tensor-carrier equality.

## 1. Research question

QM Core 004E recorded

```text
ETC-QM = exact tomographic composite tensor lock
```

because the existing DSD quantum specialization had `CRD + LDC-QM`, but had not shown the full finite-dimensional GPT composite interface.

The present gate asks:

1. Does `LDC-QM` alone imply `V_AB = V_A tensor V_B`?
2. Does the existence of all independent product preparations alone imply local tomography?
3. Which precursor assumptions actually generate the two dimension inequalities needed for exact tensor equality?
4. Are those precursor assumptions already consequences of generic DSD?
5. Which part of the old monolithic `ETC-QM` lock can now be demoted from an assumption to a conditional theorem?

The answer is:

```text
LDC-QM alone -> exact tensor carrier                         NO
independent product availability alone -> local tomography   NO
independent local-product composition + finite linearization
  -> K_AB >= K_A K_B                                         YES
local-product descriptive completeness
  -> K_AB <= K_A K_B                                         YES
both sides together -> K_AB = K_A K_B                        YES
and the product linear map becomes an isomorphism             YES
```

Therefore the old `ETC-QM` entry is too coarse.

Its tensor-equality component can be **conditionally derived**, but only after an explicit product-composition interface is supplied. That interface is not currently a generic DSD consequence.

## 2. Source-locked DSD side

### 2.1 Formation finite composition is not subsystem tensor composition

Formation Stage VII forms finite sums over already admitted channels relative to supplied post-Stage-VI term data.

That is a real composition operator, but it does not take two independently specified physical system carriers `A` and `B` and uniquely construct a joint carrier `AB`.

Hence:

\[
\boxed{
\text{Formation finite channel composition}
\not\Rightarrow
\text{physical subsystem tensor product}.
}
\]

### 2.2 Property permits genuinely relational multi-input data

The general Property layer permits unary, binary, higher-order, and mixed typed input profiles.

A multi-input property datum is not automatically owned by one channel or one subsystem, and tensor/matrix representations are downstream choices.

Therefore generic DSD remains compatible with global or relational information not reducible to a predeclared local product carrier.

### 2.3 Static and dynamic reconstruction remain conditional

Static aggregation explicitly allows non-injective summaries and requires a separate reconstruction condition before aggregate equality can recover support.

Dynamics likewise treats a reduced readout as potentially non-complete and does not provide a converse reconstruction without injectivity or another recovery theorem.

Thus `LDC-QM` is a real specialization constraint rather than a generic DSD identity law.

## 3. External comparator decomposition

Primary comparator:

- Markus P. Mueller, *Probabilistic Theories and Reconstructions of Quantum Theory (Les Houches 2019 lecture notes)*, arXiv:2011.01286.

In the finite-dimensional GPT composite construction, independent local preparations and local effects supply product statistics and a bilinear product operation after probabilistic mixing is linearized. Tomographic Locality then says that all local-product statistics determine the global state. Under these conditions the composite linear carrier has the tensor-product dimension and can be identified with the tensor product of the local carriers.

This is used only as an external theorem-interface comparator.

## 4. Algebraic countermodel A — LDC without full product availability

Let

\[
V_A=V_B=\mathbb R^2.
\]

The full algebraic tensor carrier has dimension

\[
\dim(V_A\otimes V_B)=4.
\]

Instead choose a restricted global carrier

\[
W=\operatorname{span}\{e_{00},e_{01},e_{10}\}
\subset\mathbb R^4.
\]

Thus

\[
\dim W=3.
\]

Restrict the four coordinate local-product readouts to `W`. Their joint map is injective on `W`: three independent coordinates separate every vector in the three-dimensional carrier.

So the local-product readout criterion can hold on the declared global carrier.

However the fourth independent product direction

\[
e_{11}
\]

is absent from `W`.

Therefore:

\[
\boxed{
\text{local-product readout injectivity on the declared }V_{AB}
\not\Rightarrow
V_{AB}=V_A\otimes V_B.
}
\]

The missing ingredient is independent availability of the full local product family.

This is an algebraic interface countermodel, not a proposed alternative physical theory.

## 5. Algebraic countermodel B — full product subspace without LDC

Now choose

\[
V_{AB}=\mathbb R^5.
\]

Let its first four basis directions contain a complete copy of

\[
V_A\otimes V_B\cong\mathbb R^4,
\]

and let the fifth direction `h` be an additional global relational coordinate.

All four independent product preparations can therefore exist.

Let all local-product readouts depend only on the first four coordinates. Then

\[
R_{\rm loc}(0,0,0,0,1)=0.
\]

Hence `h` lies in the readout kernel and

\[
\operatorname{rank}R_{\rm loc}=4<5=\dim V_{AB}.
\]

Therefore:

\[
\boxed{
\text{independent product availability}
\not\Rightarrow
\text{local tomography}.
}
\]

Again this is exactly the kind of globally retained distinction that generic DSD reconstruction discipline permits unless an injectivity theorem is supplied.

## 6. Independent Local Product Composition — ILPC-QM

The missing precursor interface is isolated as:

### ILPC-QM — Independent Local Product Composition

For a declared composite `AB`, supply or derive:

```text
LOCAL_OPERATIONAL_CARRIERS      V_A, V_B
GLOBAL_OPERATIONAL_CARRIER      V_AB
PRODUCT_PREPARATION_OPERATION   beta
PRODUCT_EFFECT_OPERATION
LOCAL_RANDOMIZER_COMPATIBILITY
PRODUCT_PROBABILITY_FACTORIZATION
PRODUCT_UNIT_EFFECT / NORMALIZATION
LOCAL_TRANSFORMATION_PRODUCTS   when the comparator requires them
```

On normalized preparations, compatibility with independent randomization requires separate affinity in each input.

After the ordered-carrier linearization from QM Core 004D, this gives a bilinear map

\[
\beta:V_A\times V_B\to V_{AB},
\]

hence a unique linear map

\[
\widetilde\beta:V_A\otimes V_B\to V_{AB}.
\]

Product effects satisfy

\[
(e_A\boxtimes e_B)(\beta(a,b))
=e_A(a)e_B(b).
\]

When the local effect families span the two local duals, product effects span the tensor dual sufficiently to separate nonzero tensor directions. Therefore

\[
\ker\widetilde\beta=\{0\}
\]

and

\[
\boxed{
\dim V_{AB}\ge\dim V_A\dim V_B.
}
\]

This is the **product-availability lower bound**.

## 7. LDC-QM supplies the opposite bound

Let the local effect families span `V_A^*` and `V_B^*`.

Their product span has dimension at most

\[
K_AK_B,
\qquad
K_A:=\dim V_A,
\quad
K_B:=\dim V_B.
\]

If `LDC-QM` holds, the resulting local-product readout is injective on `V_AB`.

A linear injection of `V_AB` into a readout carrier of dimension at most `K_A K_B` gives

\[
\boxed{
\dim V_{AB}\le K_AK_B.
}
\]

This is the **tomographic upper bound**.

## 8. Conditional tensor-carrier theorem

Combining Sections 6 and 7 gives

\[
K_AK_B
\le
K_{AB}
\le
K_AK_B.
\]

Therefore

\[
\boxed{K_{AB}=K_AK_B}.
\]

Since

\[
\widetilde\beta:V_A\otimes V_B\to V_{AB}
\]

is already injective and the two finite-dimensional spaces now have equal dimension, it is an isomorphism:

\[
\boxed{
V_{AB}\cong V_A\otimes V_B.
}
\]

With the declared product unit effect,

\[
u_{AB}\circ\widetilde\beta=u_A\otimes u_B,
\]

so after the isomorphism is fixed the normalization functional has the required product form.

If local transformation products are also explicitly admitted and intertwine with `beta`, their linearized action is transported to

\[
T_A\otimes T_B.
\]

Thus the exact tensor equality need not be a separate primitive assumption once the correct precursor product semantics and LDC are present.

## 9. Provenance / anti-post-hoc classification

This is the most important methodological result of 004H.

Current provenance:

```text
CRD                       A-like DSD-wide declaration discipline
ORD/ORE linearization     B  GENERAL_OPERATIONAL_DERIVATION
LDC-QM                     C  TARGET_SPECIALIZATION_SELECTOR
ILPC-QM                    D  PROVISIONAL EXACT-COMPARATOR PRECURSOR
ETC tensor equality        CONDITIONAL_DERIVATION from ILPC-QM + LDC-QM + finite linearization
```

`ILPC-QM` is operationally meaningful outside quantum theory, but it was isolated during the exact target-comparator stage. To avoid retroactive target fitting, it is **not** reclassified as Class B merely because its wording is general.

It may be reconsidered only after an independent non-QM derivation/validation program.

Consequently the conditional tensor theorem contributes **zero independent A/B evidence** that generic DSD derived complex quantum theory.

## 10. Audit outcomes

```text
Claim: Formation finite composition already gives physical tensor composition
Outcome: REJECTED

Claim: CRD + LDC-QM alone imply V_AB = V_A tensor V_B
Outcome: REJECTED
Countermodel: three-dimensional restricted carrier W inside R^4

Claim: full independent product subspace alone implies LDC-QM
Outcome: REJECTED
Countermodel: R^5 with one globally retained relational coordinate

Claim: ILPC-QM gives the product-dimension lower bound
Outcome: VALID_IN_DOMAIN

Claim: LDC-QM gives the local-readout dimension upper bound
Outcome: VALID_IN_DOMAIN

Claim: ILPC-QM + LDC-QM + finite operational linearization imply exact tensor-carrier isomorphism
Outcome: CONDITIONAL_DERIVATION / VALID_IN_DOMAIN
```

Overall verdict:

\[
\boxed{\textbf{PASS\_WITH\_REFINEMENT}}
\]

The refinement is that `ETC-QM` should no longer be treated as one opaque tensor-equality assumption. Its tensor equality is a theorem once the independently declared product-composition semantics and local tomography are both present.

## 11. Effect on QM Core 004E

The old entry

```text
ETC-QM  exact tomographic composite tensor lock
```

is resolved as:

```text
GENERIC DSD / CRD ALONE:                  NOT SUFFICIENT
LDC-QM ALONE:                             NOT SUFFICIENT
ILPC-QM ALONE:                            NOT SUFFICIENT
ILPC-QM + LDC-QM + finite linearization:  CONDITIONAL DERIVATION OF TENSOR CARRIER
PROVENANCE OF ILPC-QM:                    PROVISIONAL CLASS D
```

Thus the unresolved 004E targets are now:

```text
ULRRDE-QM
CFE-QM
```

The theorem-transfer gate remains blocked until those are classified and all required Class-C/D assumptions are explicitly declared.

## 12. Next target — QM Core 004I

Proceed to:

```text
ULRRDE-QM = universal linear recursive restriction equivalence
```

The next audit must test whether the earlier RRDE-QM result can be strengthened from a designated maximal measurement to **every** maximal perfectly distinguishing measurement, and whether the retained face-equivalence becomes a genuine linear dynamical equivalence after QM Core 004D's ordered-carrier construction.

The key pressure tests are:

```text
designated restriction vs universal quantifier
state-space equivalence vs full dynamical conjugacy
DSD sound restriction vs capacity-recursive physical equivalence
symmetry/transitivity assumptions needed to transport one face result to all faces
```

## 13. Reproducibility

Python:

```text
audits/science/2026-09-08_qm_core_004h_exact_tomographic_tensor_gate.py
```

Run from repository root:

```bash
python audits/science/2026-09-08_qm_core_004h_exact_tomographic_tensor_gate.py --mode all
```

Expected final line:

```text
OVERALL: PASS_WITH_REFINEMENT
```

Implemented witnesses:

```text
restricted composite with LDC but incomplete product availability
full product subspace with one local-readout-invisible global coordinate
exact 2x2 tensor dimension squeeze 4 <= K_AB <= 4
product probability factorization
product normalization
explicit tensor-product action of declared local transformations
```
