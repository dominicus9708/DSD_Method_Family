# Quantum CPTP Semigroup / GKSL Interface

Date: 2026-09-09

## Purpose

This interface prevents the following notions from being conflated in DSD quantum specializations:

```text
CPTP_AT_EACH_TIME
CP_DIVISIBLE_FAMILY
CPTP_SEMIGROUP
TIME_LOCAL_GKSL_GENERATOR
TIME_HOMOGENEOUS_GKSL_GENERATOR
UNITARY_GROUP_SUBCASE
```

## QDS-QM — Quantum Dynamical Semigroup

For a fixed finite-dimensional Hilbert carrier, declare a family

\[
\{\Phi_t\}_{t\ge0}
\]

to satisfy `QDS-QM` only if:

```text
1. Phi_0 = id.
2. Every Phi_t is an admitted CPTP channel.
3. Phi_(t+s) = Phi_t o Phi_s for all s,t >= 0.
4. t -> Phi_t is continuous.
5. The semigroup law is explicitly supplied as temporal structure.
```

Under these conditions, the standard finite-dimensional GKSL theorem gives

\[
\boxed{\Phi_t=e^{t\mathcal L}}
\]

with

\[
\boxed{
\mathcal L(\rho)
=
-\frac{i}{\hbar}[H,\rho]
+
\sum_\alpha
\left(
L_\alpha\rho L_\alpha^\dagger
-\frac12\{L_\alpha^\dagger L_\alpha,\rho\}
\right).
}
\]

This is a conditional standard-quantum theorem, not a generic DSD theorem.

## Channel / generator typing

Keep separate:

```text
STATE
CPTP_CHANNEL
GENERATOR
```

For a trace-preserving semigroup,

\[
\operatorname{Tr}\mathcal L(\rho)=0,
\]

so \(\mathcal L(\rho)\) is a tangent vector in operator space, not a normalized state.

The generator \(\mathcal L\) is not required to be CPTP.

Its exponential \(e^{t\mathcal L}\) is the CPTP channel family.

## Non-implications

Do not infer:

\[
\text{CPTP at every time}
\Rightarrow
\text{semigroup},
\]

or

\[
\text{smooth CPTP family}
\Rightarrow
\text{one fixed GKSL generator},
\]

or

\[
\text{CP-divisible family}
\Rightarrow
\text{time-homogeneous semigroup}.
\]

The Gaussian dephasing family with coherence factor

\[
e^{-t^2}
\]

is the control for the last two boundaries.

It is smooth and CP-divisible for \(t\ge0\), but

\[
e^{-(t+s)^2}\ne e^{-t^2}e^{-s^2}
\]

in general.

Its time-local rate is

\[
\kappa(t)=2t,
\]

so its local generator is GKSL-shaped but time-dependent.

## Reversible subcase

If the dissipative sector vanishes,

\[
L_\alpha=0,
\]

then

\[
\mathcal L(\rho)
=
-\frac{i}{\hbar}[H,\rho],
\]

and the semigroup extends to the unitary group of QM Core 005D.

Thus the Hamiltonian branch is a reversible subcase of the finite-dimensional GKSL architecture.

A semigroup with strict trace-distance contraction does not have a physical CPTP inverse even if its finite-time linear superoperator is algebraically invertible.

## Terminology discipline

Do not use `Markovian` as an unqualified synonym for all of the following at once:

```text
time-homogeneous semigroup
CP-divisible dynamics
absence of trace-distance backflow
time-local GKSL equation
```

These are related but distinct structures in open quantum dynamics.

When the distinction matters, name the exact condition.

## Infinite-dimensional boundary

The interface above is locked to finite-dimensional systems.

Infinite-dimensional quantum dynamical semigroups can have unbounded generators and require domain-sensitive operator-algebraic treatment.

Do not export the finite-dimensional bounded GKSL formula without additional hypotheses.

## Provenance

```text
DSD supplied-law / temporal-slice discipline       A  PRE_EXISTING_DSD
normalization preservation                         B  GENERAL_OPERATIONAL_RESULT
Hilbert/CPTP carrier                               C  TARGET/SUPPLIED
QDS-QM semigroup law                               C  TARGET_SPECIALIZATION_SELECTOR
GKSL generator form                                CONDITIONAL STANDARD-QM THEOREM
CP-divisibility distinction                        STANDARD OPEN-QM STRUCTURE
```

Primary standard references:

```text
V. Gorini, A. Kossakowski, E. C. G. Sudarshan (1976)
Completely positive dynamical semigroups of N-level systems
J. Math. Phys. 17, 821-825
DOI: 10.1063/1.522979

G. Lindblad (1976)
On the generators of quantum dynamical semigroups
Commun. Math. Phys. 48, 119-130
DOI: 10.1007/BF01608499
```
