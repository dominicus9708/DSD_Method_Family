# Quantum Continuous Unitary / Hamiltonian Interface

Date: 2026-09-09

## Purpose

This interface prevents the following temporal notions from being collapsed in DSD quantum specializations:

```text
UNITARY_AT_EACH_TIME
CONTINUOUS_UNITARY_PATH
UNITARY_PROPAGATOR
ONE_PARAMETER_UNITARY_GROUP
TIME_DEPENDENT_HAMILTONIAN
TIME_INDEPENDENT_HAMILTONIAN
```

QM Core 005C establishes only the pointwise reversible-channel/unitary gate under the supplied Hilbert/CPTP specialization.

Hamiltonian generation requires additional temporal structure.

## CUG-QM — Coherent Unitary Group

For an operator-level quantum specialization, declare `CUG-QM` only when:

```text
1. one fixed Hilbert carrier is declared,
2. U(0)=I,
3. U(t+s)=U(t)U(s),
4. every U(t) is unitary,
5. t -> U(t) is strongly continuous,
6. the chosen unitary representatives form one coherent group rather than
   unrelated phase representatives of separate density-channel slices.
```

Then Stone's theorem gives a unique self-adjoint generator \(H\) such that

\[
\boxed{
U(t)=e^{-itH/\hbar}.
}
\]

In finite dimension, \(H\) is bounded and the Schrödinger equation holds for every state vector.

In infinite dimension, \(H\) may be unbounded and the differential equation is restricted to the generator domain \(D(H)\).

## General differentiable unitary path

Do not require the group law merely to define an instantaneous generator.

If a finite-dimensional unitary path is differentiable, then

\[
\boxed{
H(t)=i\hbar\,\dot U(t)U(t)^\dagger
}
\]

is Hermitian and

\[
i\hbar\dot U(t)=H(t)U(t).
\]

Therefore:

\[
\text{differentiable unitary path}
\Rightarrow
\text{time-dependent Hermitian generator},
\]

but not necessarily a time-independent one.

The standard control is

\[
U(t)=e^{-it^2H_0/\hbar},
\]

which is smooth and unitary but violates

\[
U(t+s)=U(t)U(s).
\]

Its instantaneous generator is

\[
H(t)=2tH_0.
\]

## Continuity is weaker than differentiability

The path

\[
U(t)=e^{-i|t|H_0/\hbar}
\]

is continuous and unitary but is not differentiable at \(t=0\) for nonzero \(H_0\).

Hence:

\[
\boxed{
\text{continuous unitary path}
\not\Rightarrow
\text{ordinary pointwise }H(t)\text{ at every time}.
}
\]

This does not contradict Stone's theorem because the path is not a one-parameter group.

## Propagator interface

A time-dependent unitary evolution should generally use

\[
U(t,s)
\]

with

\[
U(t,t)=I,
\qquad
U(t,s)U(s,r)=U(t,r),
\qquad
U(t,s)^\dagger=U(s,t).
\]

When differentiable,

\[
H(t)
=
i\hbar\,\partial_tU(t,s)U(s,t)
\]

is the instantaneous Hermitian generator.

Only after time homogeneity,

\[
U(t,s)=V(t-s),
\]

does the propagator reduce to a one-parameter group.

## Density-channel phase boundary

At density-operator level,

\[
\Phi_t(\rho)=U(t)\rho U(t)^\dagger
\]

does not determine the unitary phase.

In particular,

\[
H\mapsto H+cI
\]

leaves the channel unchanged:

\[
\operatorname{Ad}_{e^{-it(H+cI)/\hbar}}
=
\operatorname{Ad}_{e^{-itH/\hbar}}.
\]

Likewise the channel generator

\[
\mathcal L_H(\rho)
=
-\frac{i}{\hbar}[H,\rho]
\]

is invariant under \(H\to H+cI\).

Therefore a density-channel reconstruction determines the Hamiltonian only modulo the standard additive identity freedom unless an energy-zero/phase convention is separately supplied.

## Non-implications

Do not infer:

\[
\text{unitary at every time}
\Rightarrow
\text{one-parameter group},
\]

or

\[
\text{continuous DSD trajectory}
\Rightarrow
U(t)=e^{-itH/\hbar},
\]

or

\[
\text{density-channel family}
\Rightarrow
\text{unique absolute Hamiltonian}.
\]

## Provenance

```text
DSD time-slice / transition / equivalence discipline    A  PRE_EXISTING_DSD
005C reversible channel -> unitary conjugation          C + CONDITIONAL STANDARD QM
Hilbert carrier                                          SUPPLIED / C
propagator/group/continuity conditions                  C  TARGET SPECIALIZATION
Stone generator theorem                                  CONDITIONAL STANDARD MATH
differentiable-path H(t) formula                         GENERAL FINITE-DIMENSIONAL RESULT
H ~ H+cI channel ambiguity                              STANDARD REPRESENTATION BOUNDARY
```

This provenance must be retained in later synthesis work.

The correct DSD claim is not that generic DSD generates Hamiltonians, but that DSD makes explicit which temporal assumptions must be supplied before the standard Hamiltonian-generator theorem can be invoked.
