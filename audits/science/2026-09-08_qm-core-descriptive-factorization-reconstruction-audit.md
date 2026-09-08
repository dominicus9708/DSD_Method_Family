# QM Core Reconstruction 001 — DSD Descriptive-Factorization Representation

Date: 2026-09-08  
Status: **PASS_WITH_BOUNDARY**  
Program: **Core-Theory Reconstruction Challenge**  
Target: **finite-dimensional quantum mechanics — state / readout / Born pairing / dynamics**

## 1. Research question

This audit deliberately moves past a purely defensive DSD comparison.

The question is not whether standard quantum mechanics is correct, nor whether DSD replaces it.

The question is:

> Can the finite-dimensional core of standard quantum prediction be reconstructed as a DSD-style typed composition of admission, state, transition, readout, and reconstruction roles, strongly enough that the standard predictions can be recovered exactly and the Schrödinger/Heisenberg distinction appears as a change of factorization rather than as two unrelated formalisms?

The first target is intentionally narrow:

```text
admitted quantum state
+
admitted effect/readout
+
Born pairing
+
supplied quantum channel
+
reconstruction from a declared readout family
```

Continuous-variable quantum mechanics, unbounded operators, measurement instruments with post-measurement states, composite-system entanglement structure, and QFT are not included in this first core reconstruction.

---

## 2. DSD source lock

The current DSD sources support the following roles.

### Formation

The Formation Axiom System provides staged admission, assignment, channel formation, and finite composition. Assigned value, undefinedness, channel absence, and zero contribution remain formally distinct.

### Property

The Property Axiom System permits typed property profiles, applicability, contextual prerequisites, partial assignments, and optional downstream representations without fixing one geometric realization.

### Static aggregation

Channel-Indexed Static Aggregation explicitly treats reduced analytic outputs as downstream maps and states that aggregate equality need not reconstruct typed support. The static layer introduces no evolution law.

### Dynamics

Structural Reorganization Dynamics uses component-resolved time-indexed states and supplied dynamic laws. Reduced readouts do not replace the full state without a reconstruction/closure result, and a constitutive bridge is required when supplied property data enter evolution.

These source constraints allow a downstream quantum specialization in which standard quantum primitives are supplied externally and then organized by DSD roles.

---

## 3. Standard finite-dimensional quantum primitive lock

Fix a finite-dimensional complex Hilbert space \(\mathcal H\).

### Admitted states

\[
\mathcal S(\mathcal H)
=
\{\rho\in\mathcal L(\mathcal H):
\rho\ge 0,\ \operatorname{Tr}\rho=1\}.
\]

### Admitted effects

\[
\operatorname{Eff}(\mathcal H)
=
\{E\in\mathcal L(\mathcal H):
0\le E\le I\}.
\]

### Born readout

For each effect \(E\),

\[
\Phi_E:\mathcal S(\mathcal H)\to[0,1],
\qquad
\Phi_E(\rho)
=
\operatorname{Tr}(\rho E).
\]

### Supplied transition

A quantum channel is a completely positive trace-preserving linear map

\[
\mathcal E:
\mathcal L(\mathcal H_{\rm in})
\to
\mathcal L(\mathcal H_{\rm out}).
\]

For a Kraus representation,

\[
\mathcal E(\rho)
=
\sum_k K_k\rho K_k^\dagger,
\qquad
\sum_k K_k^\dagger K_k=I.
\]

The adjoint map is defined by the Hilbert-Schmidt pairing:

\[
\operatorname{Tr}\!\left[\mathcal E(X)Y\right]
=
\operatorname{Tr}\!\left[X\,\mathcal E^*(Y)\right].
\]

For a channel, \(\mathcal E^*\) is completely positive and unital.

External standard references used for this lock:

- MIT OpenCourseWare, 8.321 Quantum Theory I, Lectures 6–7, Schrödinger and Heisenberg pictures.
- John Watrous, *The Theory of Quantum Information*, Chapter 2, positive maps, adjoints, and quantum channels.

---

## 4. Candidate DSD quantum descriptive record

For this specialization define the typed record

\[
\boxed{
\mathfrak Q
=
(\mathcal S,\mathcal F,\mathcal A,\mathcal M,\Gamma,\Phi)
}
\]

with roles:

```text
S  admitted quantum-state carrier
F  formation/admission conditions for state candidates
A  allowed effect/readout carrier
M  selected measurement/readout family or access context
Gamma  supplied quantum transition/channel
Phi  Born readout family
```

This is not a claim that DSD Formation derives positivity, the Born rule, or complete positivity.

The point of the reconstruction is stronger than renaming but weaker than deriving the standard primitives: once the quantum primitives are locked, the full prediction is represented by a typed composition.

For a future effect \(F\),

\[
\boxed{
P_{\Gamma,F}(\rho)
=
\Phi_F(\Gamma(\rho)).
}
\]

The object of direct predictive comparison is therefore the composed evaluation, not the state coordinate, transition coordinate, or readout coordinate in isolation.

---

## 5. Exact picture-factorization theorem

Let \(\mathcal E\) be a finite-dimensional quantum channel and let \(F\) be an output effect.

Then

\[
\Phi_F\circ\mathcal E
=
\Phi_{\mathcal E^*(F)}.
\]

Indeed,

\[
(\Phi_F\circ\mathcal E)(\rho)
=
\operatorname{Tr}[\mathcal E(\rho)F]
=
\operatorname{Tr}[\rho\,\mathcal E^*(F)]
=
\Phi_{\mathcal E^*(F)}(\rho).
\]

Hence

\[
\boxed{
\text{state-forward evolution}
\quad\text{and}\quad
\text{effect/readout pullback}
}
\]

are two factorizations of the same prediction functional.

For a unitary \(U\),

\[
\mathcal E_U(\rho)=U\rho U^\dagger,
\qquad
\mathcal E_U^*(F)=U^\dagger F U,
\]

so the theorem recovers the standard Schrödinger/Heisenberg equivalence.

### Audit interpretation

This is the first place in the present challenge where the DSD role decomposition does more than relabel nouns.

The invariant predictive object is

\[
\boxed{
(\rho,\mathcal E,F)
\mapsto
\operatorname{Tr}[\mathcal E(\rho)F],
}
\]

while the time dependence may be placed on the state side or transferred to the readout side through the adjoint.

---

## 6. General-channel extension

The same identity is not restricted to reversible unitary evolution.

For a non-unitary CPTP channel,

\[
\mathcal E(\rho)=\sum_k K_k\rho K_k^\dagger,
\]

the dual readout map is

\[
\mathcal E^*(F)
=
\sum_k K_k^\dagger F K_k.
\]

Then

\[
\boxed{
\operatorname{Tr}[\mathcal E(\rho)F]
=
\operatorname{Tr}[\rho\,\mathcal E^*(F)]
}
\]

exactly.

Therefore the DSD-style prediction factorization naturally extends from picture equivalence for unitary motion to general finite-dimensional channel/readout duality.

This extension is standard quantum-information mathematics; no novelty claim is made for the adjoint-channel identity itself.

---

## 7. Contravariant composition result

Let

\[
\mathcal E_1:\mathcal L(\mathcal H_0)\to\mathcal L(\mathcal H_1),
\qquad
\mathcal E_2:\mathcal L(\mathcal H_1)\to\mathcal L(\mathcal H_2).
\]

Then

\[
\boxed{
(\mathcal E_2\circ\mathcal E_1)^*
=
\mathcal E_1^*\circ\mathcal E_2^*.
}
\]

Thus forward state evolution and backward readout transport reverse composition order.

The prediction can be written as

\[
\operatorname{Tr}
[
(\mathcal E_2\circ\mathcal E_1)(\rho)F
]
=
\operatorname{Tr}
[
\rho
(\mathcal E_1^*\circ\mathcal E_2^*)(F)
].
\]

In DSD terms, a sequence of active transitions on the state side induces a reverse-order pullback chain on the readout side.

This provides a nontrivial compositional structure for the reconstruction.

---

## 8. Complete readout-functional state representation

Define the complete prediction functional of a state by

\[
\omega_\rho:
\operatorname{Eff}(\mathcal H)\to[0,1],
\qquad
\omega_\rho(E)
=
\operatorname{Tr}(\rho E).
\]

In finite dimensions, the density-operator representation and the positive normalized linear-functional representation are equivalent.

### Proposition

The map

\[
\rho\mapsto\omega_\rho
\]

is injective.

More strongly, every positive normalized linear functional

\[
\omega:\mathcal L(\mathcal H)\to\mathbb C
\]

has a unique density operator \(\rho_\omega\) such that

\[
\omega(X)=\operatorname{Tr}(\rho_\omega X)
\]

for all \(X\).

### Proof sketch

The Hilbert-Schmidt pairing is nondegenerate, so every linear functional has a unique representing operator \(R\).

Positivity of the functional implies \(R\ge0\), and normalization

\[
\omega(I)=1
\]

implies

\[
\operatorname{Tr}R=1.
\]

Hence \(R\) is a unique density operator.

### DSD interpretation

A finite-dimensional quantum state can therefore be represented exactly by its **complete typed readout capacity**.

This gives an exact bidirectional bridge:

\[
\boxed{
\rho
\longleftrightarrow
\omega_\rho
}
\]

provided the complete effect algebra is retained.

This is substantially stronger than identifying one selected POVM output with the state.

---

## 9. Restricted readout and reconstruction loss

For a selected effect family \(\mathcal M\subseteq\operatorname{Eff}(\mathcal H)\), define

\[
R_{\mathcal M}(\rho)
=
(\operatorname{Tr}\rho E)_{E\in\mathcal M}.
\]

Then the selected readout represents the state exactly only when \(R_{\mathcal M}\) is injective on the declared state family.

The qubit witness uses

\[
|+\rangle\langle+|,
\qquad
|-\rangle\langle-|.
\]

A Z-basis measurement gives

\[
P(0)=\frac12
\]

for both states, so the Z-only readout has a nontrivial fiber.

By contrast, the three Pauli expectations

\[
x=\operatorname{Tr}(\rho X),\quad
y=\operatorname{Tr}(\rho Y),\quad
z=\operatorname{Tr}(\rho Z)
\]

reconstruct a qubit state through

\[
\boxed{
\rho
=
\frac12
(I+xX+yY+zZ).
}
\]

Thus the DSD reconstruction rule appears directly:

\[
\boxed{
\text{selected readout equality}
\neq
\text{state equality}
}
\]

unless the selected readout family is separating.

---

## 10. Finite computational witnesses

The reproducibility script checks four items.

### 10.1 Unitary picture witness

Initial state:

\[
\rho_0=|+\rangle\langle+|.
\]

Unitary:

\[
U=e^{-i\pi Z/4}.
\]

Readout:

\[
E=|+\rangle\langle+|.
\]

The script verifies

\[
\operatorname{Tr}
[
U\rho_0U^\dagger E
]
=
\operatorname{Tr}
[
\rho_0 U^\dagger E U
]
=
\frac12.
\]

It also verifies that the state changes in the Pauli readout:

\[
\langle X\rangle:1\to0,
\qquad
\langle Y\rangle:0\to1.
\]

### 10.2 Non-unitary channel witness

Use amplitude damping with

\[
\gamma=\frac14.
\]

For initial \(|+\rangle\) and excited-state effect \(P_1\),

\[
\operatorname{Tr}
[
\mathcal E(\rho)P_1
]
=
0.375.
\]

The dual effect is

\[
\mathcal E^*(P_1)
=
0.75\,P_1,
\]

and

\[
\operatorname{Tr}
[
\rho\,\mathcal E^*(P_1)
]
=
0.375.
\]

The script also verifies

\[
\mathcal E^*(I)=I.
\]

### 10.3 Reconstruction witness

The script verifies the Z-only degeneracy of \(|+\rangle\) and \(|-\rangle\), and reconstructs an amplitude-damped qubit density matrix exactly up to floating-point tolerance from its Pauli profile.

### 10.4 Composition witness

The script composes amplitude damping followed by a unitary rotation and verifies that the dual pullback reverses order while preserving the final prediction.

---

## 11. What has actually been reconstructed

The following finite-dimensional quantum core is now represented coherently in DSD roles:

```text
candidate state admission
-> admitted quantum state
-> selected/allowed effect family
-> supplied quantum transition
-> Born readout
-> reconstruction fiber
-> complete prediction-functional state
-> adjoint readout pullback
-> composition
```

The strongest current equation is

\[
\boxed{
\omega_{\mathcal E(\rho)}(F)
=
\omega_\rho(\mathcal E^*(F)).
}
\]

This says that evolution of a state and pullback of a future readout are equivalent at the level of complete prediction functionals.

---

## 12. Challenge verdict

### Mathematical equivalence layer

**PASS.**

The density-operator state and complete positive normalized prediction-functional state are equivalent in finite dimensions.

The state-forward and readout-backward channel descriptions give identical Born predictions.

### DSD reconstruction layer

**PASS_WITH_BOUNDARY.**

The DSD role structure is strong enough to reconstruct the finite-dimensional state/readout/channel prediction core without reducing the result to a mere vocabulary substitution.

The nontrivial content is the factorization:

\[
\text{prediction}
=
\text{readout}\circ\text{transition}
=
\text{pulled-back readout},
\]

together with exact reconstruction when the readout family is complete.

### Independent-formalism claim

**NOT YET ESTABLISHED.**

This first reconstruction does not yet justify a claim comparable in historical status to wave mechanics versus matrix mechanics.

The prediction-functional representation is mathematically standard and closely related to the Heisenberg and algebraic/operator viewpoints.

A stronger DSD-specific formalism would require the DSD primitives and composition rules to generate a self-contained calculus that recovers further quantum structure without simply importing each standard object one by one.

### New physical prediction

**NOT ESTABLISHED.**

No new quantum prediction appears in this first reconstruction.

---

## 13. Why this first result matters for the challenge

The result narrows the next question.

The problem is no longer whether DSD can merely *describe* quantum state, observable, and evolution roles.

It can already organize an exact finite-dimensional prediction-equivalent representation.

The next decisive challenge is whether DSD can reconstruct a quantum feature whose structure is not exhausted by the simple bilinear state/effect pairing.

The strongest next target is:

\[
\boxed{
\text{measurement update / instrument}
}
\]

because a POVM probability readout alone does not determine post-measurement state transition.

The next audit should therefore attempt to reconstruct:

```text
effect probability
+
outcome-conditioned transition
+
unconditioned channel
+
repeatability/disturbance
```

as one DSD typed structure and determine whether the state/readout/transition factorization remains sufficient or must be enlarged.

---

## 14. Reproducibility

Script:

```text
audits/science/2026-09-08_qm_core_descriptive_factorization.py
```

Run from repository root:

```bash
python audits/science/2026-09-08_qm_core_descriptive_factorization.py --mode all
```

Dependency:

```text
Python standard library only
```
