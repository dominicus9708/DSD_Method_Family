# QM Core Reconstruction 004A — Composition / Local Tomography / Continuous Reversibility Gate

Date: 2026-09-08  
Status: **PASS_WITH_REFINEMENT**  
Program: **Core-Theory Reconstruction Challenge**  
Target: **whether the integrated DSD four-layer architecture already forces the three most promising selection conditions from QM Core 004 — continuous reversible pure-state reachability, an explicit composite-system rule, and local descriptive tomography — or whether they remain additional quantum-specialization principles**

## 1. Research question

QM Core 004 established that bounded convex state/effect structure plus normalized readout and finite composition do not uniquely force complex Hilbert geometry.

The present step asks three narrower questions.

```text
H3  continuous reversible pure-state transitivity
H6  explicit composite-system rule
H7  local descriptive tomography
```

For each condition we ask:

1. Is it already a consequence of the four current DSD papers when their scope defenses are ignored and the papers are treated as one theory?
2. If not, can its failure be exhibited by an explicit finite or analytic witness compatible with the existing DSD interfaces?
3. If it is useful for quantum reconstruction, where should it live in DSD without falsely making it universal to every describable system?

The hard gates are mathematical well-definedness, consistency with the current DSD formation/property/static/dynamic interfaces, and exact separation between a generic DSD consequence and a quantum-specialization selector.

## 2. Relevant DSD structure

### 2.1 Formation

Formation Stage VII constructs finite composites only relative to supplied post-Stage-VI term data.
A bijection of admitted channels induces a bijection of finite channel families and preserves the corresponding finite sums, but the post-Stage-VI term space and term map are supplied.

Therefore Formation finite composition is real structure, but it is not yet a physical tensor-product rule for two independently specified systems.

### 2.2 Property

The Property Axiom System permits unary, binary, higher-order, and mixed typed input profiles.
A multi-input property record is not automatically owned by one formation channel or one subsystem.
Optional matrix/tensor/geometric representations are downstream.

Therefore the existence of relational or genuinely global property data is compatible with the current core.

### 2.3 Static aggregation

Reduced static readouts may be non-injective.
Equal aggregate outputs need not reconstruct the complete typed support.
The framework already requires a separate injectivity/reconstruction result before a reduced readout can replace the underlying state.

### 2.4 Dynamics

Structural Reorganization Dynamics is component-resolved and lineage-based.
A reduced readout is not automatically a complete state classifier.
Reversible maps, continuity of transformation groups, and a topology on pure-state orbits are not supplied by the generic dynamic interface.

These points make H3, H6, and H7 genuine questions rather than paper-scope artifacts.

## 3. H3 — continuous reversible pure-state transitivity is not derived

Take the square-bit pure-state set

\[
P_\square=\{(1,1),(1,-1),(-1,1),(-1,-1)\}.
\]

Its signed coordinate-permutation symmetry group has exactly eight elements.
The orbit of \((1,1)\) under this reversible group contains all four pure states.
Hence the reversible action is pure-state transitive.

However the group is finite and therefore discrete.
Any continuous map from a connected interval into this finite discrete group has connected image and is therefore constant.
Thus the square bit has no nontrivial continuous one-parameter reversible path connecting distinct pure states.

So

\[
\boxed{
\text{reversible pure-state transitivity}
\not\Rightarrow
\text{continuous reversible pure-state transitivity}.
}
\]

More importantly for DSD,

\[
\boxed{
\text{strict isomorphism / reversible structural equivalence}
\not\Rightarrow
\text{a connected topology on the transformation group}.
}
\]

### H3 verdict

**NOT_DERIVED_FROM_CURRENT_DSD**.

A topology and continuity requirement must be supplied or derived from additional structure.
H3 is therefore a quantum-specialization selector, not a universal DSD axiom.

## 4. H6 — local systems do not determine a unique composite rule

Let local systems be

\[
S_A=S_B=\{0,1\}.
\]

Two global constructions are possible.

### Product composite

\[
S_{AB}^{\mathrm{prod}}=\{(a,b):a,b\in\{0,1\}\},
\]

with four global states.

### Relational composite

\[
S_{AB}^{\mathrm{rel}}=\{(a,b,h):a,b,h\in\{0,1\}\},
\]

with eight global states, where \(h\) is a globally retained relational coordinate.

Both have the same local state carriers and the same local projections onto \(A\) and \(B\).
Therefore local subsystem data alone do not distinguish which composite rule has been chosen.

This gives

\[
\boxed{
(S_A,S_B)
\not\Rightarrow
S_{AB}\text{ uniquely}.
}
\]

The result mirrors the current Formation architecture: Clause VII composes already admitted channel terms relative to supplied term-space data, but does not manufacture a unique physical subsystem-composition law from the local carriers alone.

### H6 verdict

The *need for an explicit composite rule* is effectively promoted by the integrated DSD architecture:

\[
\boxed{
\text{a physical composite claim requires declared composite carrier and local/global maps}.
}
\]

But the *content* of that rule — tensor product, Cartesian product, Jordan composite, relational extension, or another construction — is **NOT_DERIVED_FROM_CURRENT_DSD**.

Accordingly H6 splits into two levels:

```text
H6a  explicit-composition discipline     PROMOTABLE as cross-paper DSD requirement
H6b  a particular quantum composition    still unresolved
```

## 5. H7 — local descriptive tomography is not generic DSD

For the relational composite define the complete family of local readouts by

\[
R_{\mathrm{loc}}(a,b,h)=(a,b).
\]

Every local readout fiber has size two:

\[
R_{\mathrm{loc}}(a,b,0)=R_{\mathrm{loc}}(a,b,1).
\]

Hence

\[
\boxed{
R_{\mathrm{loc}}\text{ is not injective}.
}
\]

But the full global readout

\[
R_{\mathrm{full}}(a,b,h)=(a,b,h)
\]

is injective.

Thus the current DSD distinction between complete state and reduced readout permits a globally real distinction that is invisible to all declared local readouts.
This is not a bug: the static and dynamic papers explicitly preserve such reconstruction-loss possibilities unless injectivity is separately established.

Therefore local tomography cannot be promoted to a universal DSD axiom without excluding legitimate DSD models containing irreducibly global or relational information.

### H7 quantum-specialization form

For a declared quantum composite state class \(S_{AB}\), define the local-product readout family

\[
R_{AB}^{\mathrm{loc}}(s)
=
\bigl(\omega_s(e_A\boxtimes e_B)\bigr)_{e_A,e_B}.
\]

The DSD form of local tomography is

\[
\boxed{
R_{AB}^{\mathrm{loc}}(s)=R_{AB}^{\mathrm{loc}}(s')
\Longrightarrow
s=s'
}
\]

within the declared quantum state carrier.

Call this the **Local Descriptive Completeness criterion (LDC-QM)**.
It is a reconstruction criterion on a specialization, not a universal DSD identity principle.

## 6. Standard real-vs-complex dimension witness

For complex \(d\)-level quantum theory the real dimension of the unnormalized Hermitian state space is

\[
K_{\mathbb C}(d)=d^2.
\]

For two complex qubits,

\[
K_{\mathbb C}(4)=16
=
K_{\mathbb C}(2)^2
=4^2.
\]

This is compatible with local tomography.

For real-vector-space quantum theory,

\[
K_{\mathbb R}(d)=\frac{d(d+1)}2.
\]

For two real qubits,

\[
K_{\mathbb R}(4)=10,
\qquad
K_{\mathbb R}(2)^2=3^2=9.
\]

Thus

\[
\boxed{10\ne9}
\]

and one global parameter is not reconstructible from local product statistics.
This reproduces the standard distinction that complex quantum theory is locally tomographic whereas real-vector-space quantum theory is not locally tomographic in the same sense.

External standard references:

- L. Hardy and W. K. Wootters, *Limited Holism and Real-Vector-Space Quantum Theory*, arXiv:1005.4870.
- H. Barnum and A. Wilce, *Local tomography and the Jordan structure of quantum theory*, arXiv:1202.4513.

## 7. H3 + H6 + H7 are still not sufficient for complex quantum theory

A further counterfamily survives.

Take an \(n\)-ball generalized probabilistic state space with \(n=4\).
Its normalized pure states form the sphere \(S^3\), and the rotation group \(SO(4)\) acts continuously and transitively on the pure states.
The unnormalized linear dimension is

\[
K=n+1=5.
\]

A locally tomographic product vector space has

\[
K_{AB}=K_AK_B=25.
\]

Therefore the following can all hold:

```text
continuous reversible pure-state transitivity
explicit composite rule
local tomography
```

while the one-system normalized state space is a 4-ball, not the complex-qubit Bloch 3-ball.

Hence

\[
\boxed{
H_3+H_6+H_7
\not\Rightarrow
\text{complex Hilbert quantum theory}.
}
\]

This agrees with standard GPT reconstruction literature: additional structural principles are required.
Masanes and Mueller derive finite-dimensional quantum theory from a stronger package of operational requirements, and later expositions emphasize tomographic locality, continuous reversibility, and a subspace axiom as a key reconstruction route.

References:

- L. Masanes and M. P. Mueller, *A derivation of quantum theory from physical requirements*, arXiv:1004.1483.
- M. P. Mueller, *Probabilistic Theories and Reconstructions of Quantum Theory*, arXiv:2011.01286.

## 8. DSD status of the three conditions

| Condition | Current DSD status | 004A disposition |
|---|---|---|
| H3 continuous reversible pure-state transitivity | no topology/connected transformation law in the generic core | quantum-specialization selector |
| H6 explicit composite-system rule | finite composition exists only relative to supplied term data | explicit-composition discipline promotable; quantum composite content unresolved |
| H7 local descriptive tomography | reconstruction is conditional; reduced readouts may be non-injective | quantum-specialization reconstruction criterion |

## 9. Candidate cross-paper interface promoted by 004A

### Composite Rule Declaration (CRD)

Whenever a DSD physical specialization claims a composite system \(AB\), it must declare or derive at least:

```text
GLOBAL_CARRIER        S_AB
LOCAL_EMBEDDINGS      A -> AB, B -> AB or their operational analogue
LOCAL_READOUT_FAMILY  R_loc
GLOBAL_READOUT_FAMILY R_full when required
REDUCTION_MAPS        AB -> A, AB -> B when defined
COMPOSITE_DYNAMICS    Gamma_AB or its constitutive source
```

No particular tensor product is built into this interface.

### Local Descriptive Completeness (LDC-QM)

For the quantum specialization only:

\[
\boxed{
R_{AB}^{\mathrm{loc}}(s)=R_{AB}^{\mathrm{loc}}(s')
\Rightarrow s=s'.
}
\]

This is a selection principle for the candidate quantum composite family.

### Continuous Reversible Reachability (CRR-QM)

For pure states \(p,q\) of one fixed quantum system type, require a continuous path \(g_t\) of reversible transformations with

\[
g_0p=p,
\qquad
g_1p=q.
\]

This requires an explicitly supplied topology on the reversible transformation group.

## 10. Main result

The strongest justified result is

\[
\boxed{
\text{DSD already explains why composite and reconstruction rules must be explicit,}
}
\]

but

\[
\boxed{
\text{it does not yet force continuous reversibility or local tomography as universal laws.}
}
\]

For quantum reconstruction, H3 and H7 are useful selectors, while H6a is elevated to a DSD-wide declaration discipline.

The failure of H3/H7 to be universal is structurally appropriate because DSD is intended to include discrete systems and systems carrying irreducibly global relational information.

## 11. Next target — QM Core 004B

The next pressure test should not simply add H4 and H5 as arbitrary axioms.
A more DSD-native route is to test the **subspace/restriction principle** used in operational reconstructions:

> if one perfectly distinguishable outcome is excluded, is the remaining face of the state space structurally equivalent to a lower-capacity system of the same theory?

This is especially promising because DSD Formation already contains sound restriction, formation submodels, embeddings, and strict comparison.

QM Core 004B should therefore test whether a quantum subspace axiom can be obtained from or naturally specialized from:

```text
sound restriction
formation/property submodel structure
strict equivalence
local descriptive completeness
continuous reversible reachability
```

If successful, this would connect a genuinely DSD-native operation — restriction — to a known route that narrows GPT state spaces toward complex quantum theory.

## 12. Reproducibility

Python:

```text
audits/science/2026-09-08_qm_core_004a_composition_local_tomography_gate.py
```

Run from repository root:

```bash
python audits/science/2026-09-08_qm_core_004a_composition_local_tomography_gate.py --mode all
```

Expected final line:

```text
OVERALL: PASS_WITH_REFINEMENT
```

## 13. Verdict

\[
\boxed{\textbf{PASS\_WITH\_REFINEMENT}}
\]

Refinements established:

1. H3 is not derived by strict structural equivalence or reversible transitivity alone.
2. H6 splits into a promotable DSD explicit-composition discipline and an unresolved physical composition law.
3. H7 is exactly expressible as a DSD reconstruction/injectivity criterion, but is not universal.
4. Real-vs-complex parameter counting confirms that local tomography can select against real quantum theory.
5. H3+H6+H7 still do not uniquely select complex Hilbert geometry.
6. The next most DSD-native discriminator is a subspace/restriction principle rather than an arbitrary new Hilbert axiom.
