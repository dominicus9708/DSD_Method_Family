# QM Core Reconstruction 005C — Reversible Channel / Unitary Gate

Date: 2026-09-08  
Status: **PASS_WITH_REFINEMENT**  
Program: **Core-Theory Reconstruction Challenge**  
Target: distinguish algebraic invertibility from physically admissible quantum reversibility, and determine exactly when reversible finite-dimensional quantum dynamics collapses to unitary conjugation.

## 1. Question

QM Core 005A separated positivity from complete positivity, while QM Core 005B separated complete positivity from normalization preservation. The next question is:

> If a deterministic quantum channel is physically reversible, must its dynamics be unitary?

The critical ambiguity is the word `invertible`. A linear superoperator can possess an algebraic inverse even when that inverse does not map quantum states to quantum states. The present gate therefore distinguishes:

```text
algebraic invertibility
state-space invertibility
physically admissible channel reversibility
```

before comparing with DSD lineage or ordinary reversible dynamics.

## 2. Standard finite-dimensional lock

Let

\[
\Phi:M_d(\mathbb C)\to M_d(\mathbb C)
\]

be a quantum channel, i.e. a completely positive trace-preserving linear map.

Define **physical channel reversibility** by requiring another quantum channel

\[
\Psi:M_d(\mathbb C)\to M_d(\mathbb C)
\]

such that

\[
\boxed{
\Psi\circ\Phi=\Phi\circ\Psi=\operatorname{id}.
}
\]

For equal finite input/output dimension, the standard theorem is:

\[
\boxed{
\Phi\text{ has a CPTP inverse}
\iff
\exists U\text{ unitary such that }\Phi(X)=UXU^\dagger.
}
\]

A useful general reference is A. Nayak and P. Sen, *Invertible Quantum Operations and Perfect Encryption of Quantum States* (2006). Their more general characterization allows a fixed ancillary state when dimensions differ; in the same-system equal-dimension case the reversible channel reduces to unitary conjugation.

## 3. Why algebraic invertibility is too weak

Use the qubit depolarizing channel

\[
\Phi_\lambda(X)
=
\lambda X
+(1-\lambda)\operatorname{Tr}(X)\frac I2,
\qquad 0<\lambda\le1.
\]

For \(\lambda=1/2\), this is CPTP and algebraically invertible as a linear map. Its inverse is

\[
\Phi_{1/2}^{-1}(Y)
=
2Y-\operatorname{Tr}(Y)\frac I2.
\]

The inverse correctly recovers every vector in the image of the forward linear map. For example,

\[
\Phi_{1/2}(|0\rangle\langle0|)
=
\begin{pmatrix}
3/4&0\\
0&1/4
\end{pmatrix}
\]

and the algebraic inverse returns \(|0\rangle\langle0|\).

But apply the same inverse to the perfectly valid density operator \(|0\rangle\langle0|\):

\[
\Phi_{1/2}^{-1}(|0\rangle\langle0|)
=
\begin{pmatrix}
3/2&0\\
0&-1/2
\end{pmatrix}.
\]

This operator is not positive. Hence

\[
\boxed{
\text{CPTP + algebraically invertible}
\not\Rightarrow
\text{CPTP inverse}.
}
\]

This is an implication counterexample, not a counterexample to standard quantum mechanics or DSD.

## 4. Distinguishability proof pressure

Every CPTP map contracts trace distance. If both \(\Phi\) and its inverse \(\Psi\) are CPTP, then for any states \(\rho,\sigma\),

\[
\|\rho-\sigma\|_1
\ge
\|\Phi(\rho)-\Phi(\sigma)\|_1
\ge
\|\Psi\Phi(\rho)-\Psi\Phi(\sigma)\|_1
=
\|\rho-\sigma\|_1.
\]

Therefore every inequality is equality:

\[
\boxed{
\|\Phi(\rho)-\Phi(\sigma)\|_1
=
\|\rho-\sigma\|_1.
}
\]

Physical reversibility thus forbids irreversible distinguishability loss.

For the \(\lambda=1/2\) depolarizing witness,

\[
\||0\rangle\langle0|-|1\rangle\langle1|\|_1=2,
\]

while after the channel the norm is only

\[
1.
\]

So the channel cannot possess a physical CPTP inverse even though its underlying superoperator is algebraically invertible.

The full unitary conclusion is the standard finite-dimensional reversible-channel theorem, not a theorem of DSD alone.

## 5. Exact unitary control

Use the Pauli-X unitary

\[
U=X=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

The channel

\[
\mathcal U(\rho)=U\rho U^\dagger
\]

is CPTP and its inverse is

\[
\mathcal U^{-1}(\rho)=U^\dagger\rho U.
\]

Here \(U=U^\dagger=U^{-1}\), so

\[
|0\rangle\langle0|
\mapsto
|1\rangle\langle1|
\mapsto
|0\rangle\langle0|.
\]

This is the positive control for genuine physical channel reversibility.

## 6. Antiunitary / transpose boundary

A state-space symmetry can be bijective without being an ordinary quantum channel. Matrix transposition is involutive and positive on an isolated system,

\[
T^2=\operatorname{id},
\]

but QM Core 005A showed that

\[
T\otimes\operatorname{id}
\]

fails positivity on an entangled state. Thus transposition is not CP.

This cleanly separates:

```text
Wigner-type unitary/antiunitary state-space symmetry
from
physically admissible CPTP dynamical channel.
```

The CPTP requirement eliminates the antiunitary/transposition branch from ordinary channel dynamics.

## 7. DSD interpretation

The pre-existing DSD dynamics layer distinguishes:

```text
one admissible time-indexed trajectory
physical transition law
cross-time lineage
strict representation/equivalence structure
```

and does not identify them automatically.

A regular trajectory can therefore be continuous without being reversible, and a structural equivalence can exist without being the physical inverse of a dynamic law.

Define the quantum specialization selector

```text
PCR-QM  Physical Channel Reversibility
```

by requiring, for a same-system deterministic quantum map \(\Phi\), another admitted deterministic quantum map \(\Psi\) such that

\[
\Psi\Phi=\Phi\Psi=\operatorname{id}
\]

on the complete declared quantum state carrier, with both maps satisfying the 005A/005B channel admissibility conditions.

Then, in the supplied finite-dimensional Hilbert specialization,

\[
\boxed{
\mathrm{PCR\!-\!QM}
+
\text{CPTP channel structure}
\Longrightarrow
\Phi(\rho)=U\rho U^\dagger.
}
\]

The implication is a conditional standard quantum theorem.

## 8. What is not implied

The following implications are rejected:

\[
\boxed{
\text{continuous DSD evolution}
\not\Rightarrow
\text{unitary quantum evolution}
}
\]

and

\[
\boxed{
\text{algebraically invertible quantum superoperator}
\not\Rightarrow
\text{physically reversible quantum channel}.
}
\]

Likewise, DSD temporal lineage does not by itself supply a reverse channel. Lineage identifies succession; it is not an inverse-dynamics axiom.

## 9. Provenance

Conservative classification:

```text
DSD dynamic slice admissibility / supplied-law discipline       A  PRE_EXISTING_DSD
DSD transition-versus-equivalence separation                     A  PRE_EXISTING_DSD
normalization preservation from 005B                             B  GENERAL_OPERATIONAL_RESULT
Hilbert state/operator carrier                                   SUPPLIED / C
complete positivity / ACE-QM                                     C + conditional standard result
PCR-QM physical inverse requirement                              C  TARGET_SPECIALIZATION_SELECTOR
unitary-conjugation conclusion                                   CONDITIONAL STANDARD-QM THEOREM
```

Thus this gate does not count as an independent DSD derivation of unitary dynamics.

It does show that once the standard quantum admissibility structure is supplied, DSD's pre-existing distinction between an actual admissible transition and a mere mathematical inverse prevents algebraic invertibility from being mistaken for physical reversibility.

## 10. Reproducibility

Python:

```text
audits/science/2026-09-08_qm_core_005c_reversible_channel_unitary_gate.py
```

Run from repository root:

```bash
python audits/science/2026-09-08_qm_core_005c_reversible_channel_unitary_gate.py --mode all
```

Expected summary:

```text
Pauli-X channel maps |0><0| to |1><1|                              PASS
Pauli-X inverse channel recovers the input                         PASS
unitary channel preserves normalization                            PASS
depolarizing outputs normalized diagonal states                    PASS
depolarizing output on |0> is diag(3/4,1/4)                       PASS
algebraic depolarizing inverse recovers an on-range input           PASS
algebraic inverse maps a valid state to diag(3/2,-1/2)             PASS
algebraic inverse is therefore not positive                         PASS
orthogonal-state trace norm starts at 2                             PASS
depolarizing trace norm contracts to 1                              PASS

OVERALL: PASS_WITH_REFINEMENT
```

## 11. Verdict

**PASS_WITH_REFINEMENT**

For finite-dimensional same-system quantum dynamics, physical reversibility is strictly stronger than algebraic invertibility. A CPTP map with a CPTP inverse is necessarily unitary conjugation, whereas a depolarizing channel gives an exact CPTP and algebraically invertible counterexample whose inverse is not positive. The unitary result remains conditional on the supplied Hilbert/CPTP specialization rather than being a generic DSD theorem.

Next target: **QM Core 005D — continuous reversible unitary family / Hamiltonian generator gate**, separating a general time-indexed unitary propagator from a time-homogeneous one-parameter group and testing exactly when the Schrödinger generator form follows.
