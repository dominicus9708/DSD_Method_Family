# QM Core Reconstruction 005G — Naimark / Measurement-Dilation / Instrument Realization Gate

Date: 2026-09-09  
Status: **PASS_WITH_REFINEMENT**  
Program: **Core-Theory Reconstruction Challenge**  
Target: reconstruct the finite-dimensional bridge from POVMs to projective measurements on an enlarged space, then separate outcome statistics from post-measurement state dynamics and from claims about a unique laboratory implementation.

## 1. Question

QM Core 003 reconstructed the Born valuation conditionally on the Hilbert effect carrier.  
QM Core 005B separated deterministic normalization from selective branches.  
QM Core 005F reconstructed the CPTP/Kraus/Stinespring/unitary-dilation representation gate.

The present question is:

> Given a finite-dimensional POVM, what follows mathematically from Naimark dilation, what extra data are needed to specify a quantum instrument, and what may DSD legitimately infer about a physical measurement implementation?

The critical distinctions are:

```text
POVM_EFFECT_FAMILY
PROJECTIVE_MEASUREMENT_ON_DILATED_SPACE
NAIMARK_ISOMETRY
ANCILLA_PLUS_UNITARY_REALIZATION
QUANTUM_INSTRUMENT_BRANCH_MAPS
CONDITIONAL_POST_MEASUREMENT_STATE
LABORATORY_IMPLEMENTATION_CLAIM
```

These are related but not identical structures.

## 2. Standard finite-dimensional POVM gate

Let \(\mathcal H\) be a finite-dimensional complex Hilbert space and let

\[
\mathsf E=\{E_i\}_{i\in\Omega}
\]

be a POVM:

\[
E_i\ge 0,
\qquad
\sum_i E_i=I.
\]

For a state \(\rho\), the outcome probabilities are

\[
\boxed{
p(i|\rho)=\operatorname{Tr}(\rho E_i)
}.
\]

This fixes the measurement statistics.  
It does not by itself fix the post-measurement state.

## 3. Naimark dilation gate

The standard finite-dimensional Naimark theorem gives an enlarged Hilbert space \(\mathcal K\), an isometry

\[
V:\mathcal H\to\mathcal K,
\qquad
V^\dagger V=I,
\]

and a projective measurement \(\{P_i\}\) on \(\mathcal K\) satisfying

\[
P_i=P_i^\dagger=P_i^2,
\qquad
P_iP_j=0\quad(i\ne j),
\qquad
\sum_iP_i=I_{\mathcal K},
\]

such that

\[
\boxed{
E_i=V^\dagger P_iV
}.
\]

Therefore

\[
\boxed{
\operatorname{Tr}(\rho E_i)
=
\operatorname{Tr}(V\rho V^\dagger P_i)
}.
\]

Define the target selector:

```text
NMD-QM  Naimark Measurement Dilation

1. fixed finite-dimensional complex Hilbert carrier,
2. finite POVM effect family {E_i},
3. enlarged Hilbert carrier K,
4. isometry V : H -> K,
5. orthogonal projectors {P_i} summing to I_K,
6. E_i = V† P_i V.
```

Then

\[
\boxed{
\mathrm{NMD\!-\!QM}
\Longrightarrow
\text{projective-dilation representation of the same POVM statistics}
}
\]

by a standard quantum-measurement theorem.

This is a representation theorem.  
It is not a derivation of the Hilbert effect carrier from generic DSD.

## 4. Ancilla-plus-unitary form

A common finite-dimensional realization writes the dilation space as

\[
\mathcal H\otimes\mathcal H_A
\]

with a fixed ancilla state \(|0_A\rangle\), a unitary \(U\), and a projective measurement \(\{\Pi_i\}\) on the ancilla.

Then

\[
p(i|\rho)
=
\operatorname{Tr}
\left[
U(\rho\otimes|0_A\rangle\langle0_A|)U^\dagger
(I\otimes\Pi_i)
\right].
\]

Equivalently, for measurement operators

\[
M_i=\langle i_A|U|0_A\rangle,
\]

the POVM effects are

\[
\boxed{
E_i=M_i^\dagger M_i
}
\]

and

\[
p(i|\rho)=\operatorname{Tr}(M_i\rho M_i^\dagger).
\]

The existence of one such dilation does not identify a unique ancilla basis, unitary coupling, device Hamiltonian, or laboratory apparatus.

## 5. Quantum instrument gate

A POVM gives probabilities only.

A quantum instrument additionally supplies outcome-conditioned CP maps

\[
\mathcal I_i.
\]

For a finite outcome set, require

\[
\mathcal I_i
\quad\text{completely positive and trace-nonincreasing},
\]

while the nonselective map

\[
\boxed{
\sum_i\mathcal I_i
}
\]

is CPTP.

The associated POVM effect is determined through

\[
\boxed{
E_i=\mathcal I_i^*(I)
}
\]

or, equivalently,

\[
\boxed{
\operatorname{Tr}\mathcal I_i(\rho)
=
\operatorname{Tr}(\rho E_i)
}.
\]

For a nonzero branch probability

\[
p_i=\operatorname{Tr}\mathcal I_i(\rho)>0,
\]

the conditional state is

\[
\boxed{
\rho_i=
\frac{\mathcal I_i(\rho)}{p_i}
}.
\]

The zero-probability rule from QM Core 005B remains unchanged:

```text
branch operator I_i(rho) = 0        DEFINED_ZERO
branch probability p_i = 0          DEFINED_ZERO
normalized conditional state        UNDEFINED
```

## 6. Finite witness — genuine unsharp qubit POVM

Use

\[
E_0=
\begin{pmatrix}
0.8&0\\
0&0.2
\end{pmatrix},
\qquad
E_1=
\begin{pmatrix}
0.2&0\\
0&0.8
\end{pmatrix}.
\]

Then

\[
E_0+E_1=I,
\]

but neither effect is a projection:

\[
E_i^2\ne E_i.
\]

Choose

\[
M_0=\sqrt{E_0},
\qquad
M_1=\sqrt{E_1}.
\]

The canonical isometry

\[
V|\psi\rangle
=
M_0|\psi\rangle\otimes|0\rangle
+
M_1|\psi\rangle\otimes|1\rangle
\]

satisfies

\[
V^\dagger V=I.
\]

With

\[
P_i=I\otimes|i\rangle\langle i|,
\]

the audit verifies exactly

\[
\boxed{
V^\dagger P_iV=E_i
}.
\]

Thus a genuinely non-projective POVM is represented by a projective measurement on the enlarged carrier without changing its outcome probabilities.

## 7. Explicit unitary realization

For the same binary POVM, the audit constructs a \(4\times4\) unitary \(U\) acting on system plus qubit ancilla.

With the ancilla initialized in \(|0\rangle\),

\[
U(\rho\otimes|0\rangle\langle0|)U^\dagger
\]

followed by computational-basis measurement of the ancilla gives branches

\[
M_i\rho M_i^\dagger.
\]

For every tested state,

\[
\operatorname{Tr}(M_i\rho M_i^\dagger)
=
\operatorname{Tr}(\rho E_i).
\]

Therefore the POVM readout is reproduced by an ordinary projective measurement on a larger system.

## 8. Same POVM, different instruments

The central boundary is that

\[
\boxed{
\text{POVM effects do not determine a unique instrument}
}.
\]

Take the baseline single-Kraus branches

\[
\mathcal I_i(\rho)=M_i\rho M_i^\dagger.
\]

Now set

\[
N_0=M_0,
\qquad
N_1=XM_1,
\]

where \(X\) is the Pauli-\(X\) unitary.

Then

\[
N_0^\dagger N_0=E_0,
\qquad
N_1^\dagger N_1
=
M_1^\dagger X^\dagger X M_1
=
E_1.
\]

Hence the alternative instrument

\[
\mathcal J_i(\rho)=N_i\rho N_i^\dagger
\]

has exactly the same POVM:

\[
\operatorname{Tr}\mathcal J_i(\rho)
=
\operatorname{Tr}\mathcal I_i(\rho)
=
\operatorname{Tr}(\rho E_i).
\]

But the post-measurement states can differ.

For

\[
\rho=|+\rangle\langle+|,
\]

the outcome-\(1\) probability is \(1/2\) for both instruments, while

\[
\rho_{1,\mathcal I}
=
\begin{pmatrix}
0.2&0.4\\
0.4&0.8
\end{pmatrix},
\]

and

\[
\rho_{1,\mathcal J}
=
\begin{pmatrix}
0.8&0.4\\
0.4&0.2
\end{pmatrix}.
\]

The nonselective channels also differ:

\[
\sum_i\mathcal I_i(\rho)
=
\begin{pmatrix}
0.5&0.4\\
0.4&0.5
\end{pmatrix},
\]

whereas

\[
\sum_i\mathcal J_i(\rho)
=
\begin{pmatrix}
0.8&0.4\\
0.4&0.2
\end{pmatrix}.
\]

Thus identical measurement statistics do not identify identical state-update dynamics.

## 9. Dilation non-uniqueness

The alternative instrument can be realized by appending an outcome-controlled system unitary after the baseline dilation.

Let

\[
W
=
I\otimes|0\rangle\langle0|
+
X\otimes|1\rangle\langle1|.
\]

Then \(W\) is unitary and commutes with the ancilla outcome projectors.

Therefore

\[
U'=WU
\]

gives the same ancilla outcome probabilities as \(U\), while the retained system state in the outcome-\(1\) branch is transformed by \(X\).

Consequently,

\[
\boxed{
\text{same POVM}
\not\Rightarrow
\text{unique dilation unitary}
}
\]

and

\[
\boxed{
\text{same POVM}
\not\Rightarrow
\text{unique post-measurement dynamics}
}.
\]

Minimal Naimark dilations have a standard uniqueness-up-to-unitary-equivalence statement under the appropriate minimality conditions.  
That mathematical equivalence still does not identify one unique physical apparatus.

## 10. DSD placement

The most conservative DSD placement is:

```text
Formation
    stable identity of system, protocol, outcome labels, apparatus roles if supplied

Property
    quantum state records
    POVM effects
    outcome probabilities
    branch status

Static Aggregation
    probability vector / outcome readout

Dynamics
    instrument branch maps
    nonselective state-update map
    post-measurement trajectory or transition law

Quantum specialization
    Hilbert carrier
    POVM positivity/completeness
    Naimark dilation
    CP instrument structure
```

The important separation is

\[
\boxed{
\text{readout describability}
\neq
\text{state-transition describability}
}.
\]

A POVM effect family belongs to the probability/readout interface.  
An instrument contains additional transition information.

## 11. What DSD does and does not establish

### Established conditionally

Given the finite-dimensional Hilbert quantum carrier and a POVM:

\[
\boxed{
\text{POVM}
\Longrightarrow
\text{Naimark projective dilation exists}
}
\]

by the standard theorem.

Given an instrument, its associated effects reproduce branch probabilities.

The finite witness verifies that one POVM admits different instruments and different unitary measurement realizations.

### Not established

The following are not implied by generic DSD:

\[
\text{DSD contextual prerequisite}
\not\Rightarrow
\text{POVM structure},
\]

\[
\text{POVM}
\not\Rightarrow
\text{unique instrument},
\]

\[
\text{Naimark dilation}
\not\Rightarrow
\text{unique physical ancilla},
\]

\[
\text{Naimark dilation}
\not\Rightarrow
\text{unique laboratory device},
\]

\[
\text{same outcome probabilities}
\not\Rightarrow
\text{same post-measurement state}.
\]

No new quantum prediction is obtained at this gate.

## 12. Provenance classification

```text
DSD typed status / applicability / branch distinction            A PRE_EXISTING_DSD
DSD readout-vs-transition separation                              A PRE_EXISTING_DSD
zero-probability conditional-state boundary                       B/C carried from 005B
finite-dimensional Hilbert carrier                                C TARGET SPECIALIZATION
POVM effect family                                                C TARGET SPECIALIZATION
NMD-QM dilation selector                                          C TARGET SPECIALIZATION
Naimark theorem                                                   CONDITIONAL STANDARD-QM/MATH
quantum instrument CP/TNI branch structure                        CONDITIONAL STANDARD-QM
instrument -> associated POVM                                     CONDITIONAL STANDARD-QM
same POVM / different instrument counterexample                   GENERAL FINITE-DIM WITNESS
physical apparatus uniqueness rejection                           REPRESENTATION/IDENTIFIABILITY BOUNDARY
```

## 13. Audit verdict

**PASS_WITH_REFINEMENT**.

QM Core 005G closes the finite-dimensional generalized-measurement representation gate:

\[
\boxed{
\text{POVM statistics}
\leftrightarrow
\text{projective statistics on a dilation}
}
\]

at the standard representation level, while preserving the stronger distinction

\[
\boxed{
\text{POVM}
\neq
\text{instrument}
\neq
\text{unique physical implementation}.
}
\]

Together with 005F:

```text
CPTP map
    -> Kraus / Stinespring / unitary dilation          [005F]

POVM
    -> Naimark projective dilation                     [005G]

instrument
    -> POVM statistics + post-measurement CP branches [005G]
```

The remaining major boundary is no longer finite-dimensional measurement representation itself.  
It is the extension of the reconstruction beyond finite-dimensional bounded-operator QM and the unresolved origin of the Hilbert carrier.

## 14. Reproducibility

GitHub paths:

```text
audits/science/2026-09-09_qm_core_005g_naimark_measurement_dilation_instrument_gate.py
audits/science/2026-09-09_qm-core-005g-naimark-measurement-dilation-instrument-gate-audit.md
methodology/QUANTUM_NAIMARK_MEASUREMENT_INSTRUMENT_INTERFACE.md
```

Run from repository root:

```bash
python audits/science/2026-09-09_qm_core_005g_naimark_measurement_dilation_instrument_gate.py --mode all
```

Expected:

```text
OVERALL: PASS_WITH_REFINEMENT
```

## 15. Standard external references used for theorem checking

- John Watrous, *Theory of Quantum Information* lecture notes, especially Lecture 5: Naimark's theorem and characterizations of channels.
- Matteo G. A. Paris, *The modern tools of quantum mechanics*, arXiv:1110.6815.
- Giulio Chiribella, Giacomo Mauro D'Ariano, Paolo Perinotti, *Realization schemes for quantum instruments in finite dimensions*, arXiv:0810.3211.

These references supply the standard quantum-measurement theorems.  
They are not counted as DSD-derived structure.

## 16. Next target

**QM Core 006 — Infinite-Dimensional Hilbert / Unbounded-Operator / Domain Gate**.

The next audit should determine which finite-dimensional reconstruction statements survive unchanged, which require topology/domain hypotheses, and where unbounded observables or generators force a stricter distinction between:

```text
operator existence
operator domain
self-adjointness
spectral measure
state applicability
strong continuity
strong differentiability
```

This is the natural boundary before the canonical \(Q,P\)/CCR gate.
