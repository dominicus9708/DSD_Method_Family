# QM Core Reconstruction 004B — Subspace / Restriction Principle Gate

Date: 2026-09-08  
Status: **PASS_WITH_REFINEMENT**  
Program: **Core-Theory Reconstruction Challenge**  
Target: **whether the DSD notion of sound restriction, formation/property submodel structure, strict comparison, static reconstruction, and dynamics can themselves yield the quantum subspace principle used in operational reconstructions**

## 1. Research question

QM Core 004A identified a DSD-native next question.

The standard quantum-reconstruction subspace principle says, schematically, that for a system of capacity `N`, excluding one outcome of a maximal perfectly distinguishing measurement by assigning it probability zero should leave a face equivalent to the theory's system of capacity `N-1`, together with the corresponding face-preserving reversible dynamics.

The DSD question is stronger than mere representability:

```text
Does DSD sound restriction itself force this recursive lower-capacity equivalence?
```

The answer is **no**.

However, the current DSD architecture supplies unusually natural machinery for stating the missing condition without importing Hilbert space at the start.

## 2. Source-locked DSD facts

The current Formation Axiom System distinguishes a restriction relation from later realization, channel formation, and finite composition. Forward formation maps preserve restriction and realization, while formation embeddings add injectivity and reflection. Formation submodels therefore require closure/reflection conditions; an arbitrary family of induced subsets is explicitly not automatically a formation submodel.

Strict formation equivalence is base-fixed and presentation-sensitive. Consequently, a face of a system of capacity `N` and an independently declared system of capacity `N-1` are not automatically comparable by the current strict base-fixed isomorphism unless they are first placed under a compatible comparison base or a separate typed specialization bridge is supplied.

The Property Axiom System similarly has property embeddings, inclusion submodels, and strict Stage-VI-fixed property isomorphisms. Inclusion alone is not the same thing as a claim that a restricted physical model is the same lower-capacity physical system.

Static Aggregation keeps reconstruction/injectivity separate from output equality, and Structural Reorganization Dynamics requires each time slice to remain an admissible predecessor slice while distinguishing regular value evolution from formation-level change.

Therefore the present question is not blocked by paper scope language. It is a genuine cross-paper structural gap:

\[
\boxed{
\text{restriction/submodel existence}
\not\Rightarrow
\text{recursive physical-system equivalence}.
}
\]

## 3. Standard operational target

Following the standard GPT reconstruction literature, let a system type `Q_N` have capacity `N`, with a measurement

\[
\mathcal M_N=\{e^{(1)},\ldots,e^{(N)}\}
\]

that perfectly distinguishes `N` states.

For one excluded outcome define the zero-probability face

\[
F_{N,i}
:=
\{\omega\in\Omega_N: e^{(i)}(\omega)=0\}.
\]

The reconstruction-style subspace principle requires

\[
\boxed{F_{N,i}\simeq \Omega_{N-1}}
\]

and also requires the transformations preserving `F_{N,i}` to induce the lower-capacity transformation theory.

This is stronger than saying that `F_{N,i}` is a subset, a valid restriction, or even an inclusion submodel.

## 4. Positive quantum witness — qutrit to qubit

Take the standard qutrit carrier and exclude the third sharp outcome

\[
P_3=|3\rangle\langle3|.
\]

If

\[
\rho\ge0,
\qquad
\operatorname{Tr}\rho=1,
\qquad
\operatorname{Tr}(\rho P_3)=\rho_{33}=0,
\]

then positivity forces every matrix element in the third row and third column to vanish.
Indeed, for each retained index `i`, positivity of the `2×2` principal minor on `i,3` gives

\[
\det
\begin{pmatrix}
\rho_{ii}&\rho_{i3}\\
\rho_{3i}&0
\end{pmatrix}
=-|\rho_{i3}|^2\ge0,
\]

hence `rho_i3=0`.

Therefore every state in the zero-probability face has the form

\[
\rho=
\begin{pmatrix}
\tilde\rho&0\\
0&0
\end{pmatrix},
\qquad
\tilde\rho\ge0,
\quad
\operatorname{Tr}\tilde\rho=1.
\]

Thus the state face is exactly a qubit density-matrix state space under the obvious support embedding.

Face-preserving unitary transformations act on the retained support by

\[
\tilde\rho\mapsto U_2\tilde\rho U_2^\dagger,
\]

so the induced reversible dynamics reproduces the lower-capacity quantum transformation rule.

This is a **positive standard-QM specialization witness**.
It is not yet a DSD derivation of Hilbert space.

## 5. Counterexample — square bit fails recursive restriction

Let the normalized state space be the square

\[
\Omega_\square
=
\operatorname{conv}\{(\pm1,\pm1)\}.
\]

Use the effect

\[
e_{X+}(x,y)=\frac{1+x}{2}.
\]

The zero-probability face is

\[
F=\{(-1,y):-1\le y\le1\}.
\]

This face contains two pure endpoints

\[
(-1,-1),\qquad(-1,1),
\]

which are still perfectly distinguishable by the `Y` measurement.
Hence the restricted face still has capacity at least two.

But a capacity-two system satisfying the subspace recursion would have to reduce to a capacity-one system, whose normalized state space is a singleton.

Therefore

\[
\boxed{
\text{square bit violates the subspace recursion}.
}
\]

This is useful because QM Core 004 had already shown that the square bit satisfies much weaker bounded/readout/transitivity conditions.
The restriction principle removes that earlier countermodel.

## 6. Control — classical simplex also satisfies recursive restriction

A classical trit has normalized state space

\[
\Delta_2
=
\{(p_1,p_2,p_3):p_i\ge0,\ p_1+p_2+p_3=1\}.
\]

Excluding the third outcome gives

\[
p_3=0,
\]

which is exactly a classical bit simplex.
More generally,

\[
\Delta_{N-1}\cap\{p_N=0\}
\cong
\Delta_{N-2}.
\]

Thus the subspace principle by itself does **not** uniquely characterize quantum theory.
It is compatible with classical probability theory as well.

## 7. Core result — DSD restriction is infrastructure, not the full subspace axiom

The crucial separation is

\[
\boxed{
\text{DSD sound restriction}
\neq
\text{GPT/quantum subspace recursion}.
}
\]

DSD restriction says that a restricted structural expression/realization relation can be well formed and transported by structure-preserving maps.
The subspace principle additionally requires all of the following:

```text
1. a capacity function N,
2. a maximal perfectly distinguishing measurement,
3. a probability-zero face selected by one outcome,
4. closure of the retained physical state/effect structure,
5. equivalence of that face to the declared N-1 system type,
6. equivalence of the face-preserving reversible dynamics to the N-1 dynamics.
```

None of items 1, 2, 5, or 6 follows from the generic Formation restriction relation alone.

## 8. Proposed DSD quantum-specialization criterion

### Restriction-Recursive Descriptive Equivalence — RRDE-QM

For a declared family of quantum candidate system types `Q_N`, define a maximal distinguishability capacity `Cap(Q_N)=N` and a maximal measurement `M_N`.
For every excluded maximal outcome `e_i`, let

\[
F_{N,i}
=
\{s\in S_N:\omega_s(e_i)=0\}.
\]

The specialization satisfies **RRDE-QM** when there exists a typed equivalence bridge

\[
J_{N,i}:Q_{N-1}\longrightarrow F_{N,i}
\]

that is bijective on the retained state carrier and preserves/reflects the declared state/effect/readout structure, while also intertwining the retained reversible dynamics:

\[
J_{N,i}\circ\Gamma_{N-1}
=
\Gamma_{N}^{F_{N,i}}\circ J_{N,i}.
\]

Where static readouts are used, they must commute with the bridge.
Where property statuses are used, applicability, prerequisite satisfaction, definedness, and zero/undefined distinctions must be preserved.

RRDE-QM is **not** proposed as a universal DSD axiom.
It is a quantum-reconstruction selector expressed in DSD-native restriction, embedding, readout, and dynamics language.

## 9. DSD-wide rule that is promotable

A weaker rule *is* suitable for the general DSD theory:

### Restriction Equivalence Declaration — RED

Whenever a physical DSD specialization claims

```text
"this restricted regime is the same system type as X"
```

it must supply or derive an explicit equivalence bridge that preserves the coordinates relevant to that claim.
Subset inclusion, sound restriction, aggregate equality, or one-way embedding alone is insufficient.

This rule is already strongly motivated by the current papers:

- arbitrary induced subsets need not be formation submodels;
- property inclusion submodels require embedding conditions;
- strict equivalence is stronger than output equality;
- reduced static/dynamic readouts require reconstruction results before replacing complete state.

## 10. Relation to known quantum reconstruction theorems

The external GPT reconstruction literature gives a stronger result.
In the finite-dimensional GPT framework used in Mueller's reconstruction notes, Tomographic Locality is assumed; the reconstruction section also works with the no-restriction hypothesis. Under that framework, the Subspace Axiom plus Continuous Reversibility yields the standard finite-dimensional complex quantum state spaces and unitary-conjugation reversible dynamics.

This result is highly relevant but cannot yet be imported as a DSD theorem, because the current DSD quantum specialization has not established all framework identifications required by that theorem.
In particular, DSD has not yet derived or adopted:

```text
a GPT capacity function,
the no-restriction hypothesis for effects,
a proof that the DSD composite/readout carrier satisfies the exact GPT assumptions,
a cross-system equivalence notion adequate for Q_N <-> restricted Q_(N+1).
```

Therefore the standard theorem is a **target comparator**, not a transferred proof.

Primary comparator:

- Markus P. Mueller, *Probabilistic Theories and Reconstructions of Quantum Theory*, arXiv:2011.01286, especially the definitions of Tomographic Locality, the Subspace Axiom, Continuous Reversibility, and Theorem 21.
- Lluis Masanes and Markus P. Mueller, *A derivation of quantum theory from physical requirements*, arXiv:1004.1483.

## 11. What 004B changes

Before 004B the unresolved Hilbert selector package was roughly

```text
continuous reversible reachability
explicit composition
local descriptive completeness
additional structural principle
```

004B identifies the most DSD-native additional principle as recursive restriction equivalence.

The resulting candidate chain is

\[
\boxed{
\text{CRR-QM}
+
\text{CRD}
+
\text{LDC-QM}
+
\text{RRDE-QM}
}
\]

with an important caution:
this package is not yet proven equivalent to the exact assumptions of any external GPT reconstruction theorem.

## 12. Next target — QM Core 004C

The next gate should audit the two missing comparator assumptions that now matter most:

```text
CAPACITY
NO-RESTRICTION / EFFECT COMPLETENESS
```

Questions:

1. Can DSD define capacity purely as maximal jointly distinguishable typed outcomes without importing Hilbert dimension?
2. Does the DSD Property/readout architecture naturally allow every mathematically positive normalized effect, or is a no-restriction hypothesis genuinely additional?
3. If effect completeness is too strong for generic DSD, can it be isolated as a quantum-specialization condition without contaminating Formation/Property core?
4. After capacity and effect completeness are locked, does the DSD package match the hypothesis set of the standard reconstruction theorem closely enough to use it as an external conditional result?

## 13. Reproducibility

Python:

```text
audits/science/2026-09-08_qm_core_004b_subspace_restriction_gate.py
```

Run from repository root:

```bash
python audits/science/2026-09-08_qm_core_004b_subspace_restriction_gate.py --mode all
```

Expected final line:

```text
OVERALL: PASS_WITH_REFINEMENT
```

Finite witnesses implemented:

```text
square-bit restriction counterexample
classical simplex restriction control
qutrit-to-qubit quantum face witness
subset does not imply lower-type equivalence
```

## 14. Verdict

\[
\boxed{\textbf{PASS\_WITH\_REFINEMENT}}
\]

Refinements established:

1. Current DSD sound restriction does not derive the quantum/GPT subspace axiom.
2. The square-bit countermodel is removed by recursive restriction equivalence.
3. Standard qutrit-to-qubit restriction supplies an exact positive quantum witness.
4. Classical simplices also satisfy the recursion, so the principle is not uniquely quantum by itself.
5. DSD requires a cross-system restriction-equivalence bridge because current strict formation equivalence is base-fixed.
6. A general Restriction Equivalence Declaration is promotable across DSD physical specializations.
7. RRDE-QM is a natural quantum-specialization selector.
8. The next missing comparison gates are capacity and the no-restriction/effect-completeness hypothesis.
