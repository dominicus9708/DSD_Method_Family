# Quantum Canonical CCR / Weyl Representation Interface

Status: **ACTIVE — QM Core 007 PASS_WITH_REFINEMENT**

## Purpose

This interface prevents the following statements from being collapsed:

```text
formal canonical commutator
CCR on a common domain/core
self-adjoint canonical pair
Weyl relations
strong continuity / regularity
irreducibility
Stone-von Neumann equivalence
finite truncation
physical position/momentum implementation
```

It is downstream of the infinite-dimensional Hilbert/operator-domain interface from QM Core 006.

It is not a generic DSD axiom.

## 1. Common-core rule

For the standard Schrödinger pair on \(L^2(\mathbb R)\), use

\[
(Q\psi)(x)=x\psi(x),
\qquad
(P\psi)(x)=-i\hbar\psi'(x).
\]

On the common invariant Schwartz core,

\[
\boxed{
[Q,P]\psi=i\hbar\psi,
\qquad \psi\in\mathcal S(\mathbb R).
}
\]

Never omit the domain/core clause when using the unbounded commutator as an operator statement.

## 2. Weyl interface

Define

\[
T(a)=e^{-iaP/\hbar},
\qquad
M(b)=e^{ibQ/\hbar}.
\]

In the Schrödinger representation,

\[
(T(a)\psi)(x)=\psi(x-a),
\]

\[
(M(b)\psi)(x)=e^{ibx/\hbar}\psi(x).
\]

Use the convention

\[
\boxed{
T(a)M(b)=e^{-iab/\hbar}M(b)T(a).
}
\]

Core rule:

```text
CCR_ON_CORE
!=
WEYL_RELATION
```

unless exponentiation/regularity conditions are explicitly supplied.

## 3. CWR-QM selector

```text
CWR-QM  Canonical Weyl Representation

input:
    finite canonical degree count
    complex Hilbert carrier H
    fixed nonzero hbar / central character

supply:
    unitary T(a)
    unitary M(b)

constraints:
    T(a1+a2)=T(a1)T(a2)
    M(b1+b2)=M(b1)M(b2)
    T(a)M(b)=exp(-iab/hbar) M(b)T(a)
    strong continuity
    irreducibility
```

Standard consequence:

\[
\boxed{
\mathrm{CWR\!-\!QM}
\Longrightarrow
\text{Schrödinger representation up to unitary equivalence}
}
\]

by Stone–von Neumann.

## 4. Irreducibility rule

Never use:

```text
Weyl relation
therefore irreducible
```

A direct sum of two Schrödinger representations obeys the same Weyl relation but has a nontrivial copy projection commuting with all Weyl operators.

Therefore:

\[
\boxed{
\text{Weyl}
\not\Rightarrow
\text{irreducible}.
}
\]

## 5. Regularity rule

Strong continuity/regularity is a theorem prerequisite.

Do not use:

```text
abstract twisted unitary relation
therefore standard Q and P generators exist
```

without continuity sufficient for Stone's theorem.

Nonregular representations are outside the ordinary Stone–von Neumann gate.

## 6. Central-character rule

The value/convention of \(\hbar\) is supplied by the quantum specialization.

Stone–von Neumann uniqueness is stated for a fixed nonzero central character.

Do not count the theorem as deriving \(\hbar\) from DSD.

## 7. Finite-truncation warning

For finite matrices,

\[
\operatorname{Tr}[A,B]=0,
\]

so

\[
[A,B]=i\hbar I_d
\]

cannot hold exactly.

For the truncated oscillator,

\[
Q_d=\frac{a+a^\dagger}{\sqrt2},
\qquad
P_d=\frac{a-a^\dagger}{i\sqrt2},
\]

and

\[
\boxed{
[Q_d,P_d]
=i\left(I_d-d|d-1\rangle\langle d-1|\right).
}
\]

Interpret finite cutoffs as approximations with an explicit boundary defect, not as exact CCR realizations.

## 8. Finite-DOF boundary

Stone–von Neumann uniqueness applies to finitely many canonical degrees of freedom.

Do not export:

```text
finite-DOF regular irreducible uniqueness
```

to

```text
QFT / infinitely many degrees of freedom
```

where unitarily inequivalent representations can occur.

## 9. DSD role separation

```text
Formation:
    system and canonical-role identity
    representation-sector identity if supplied

Property:
    state
    domain/core membership
    spectral records
    representation labels

Static Aggregation:
    bounded/spectral readouts

Continuous transformation specialization:
    T(a), M(b)

Quantum specialization:
    Hilbert carrier
    self-adjoint Q,P
    CCR/Weyl structure
    strong continuity
    irreducibility
    Stone-von Neumann theorem
```

The parameters \(a,b\) are not automatically physical time.

## 10. Core inference rule

Allowed:

```text
Hilbert + fixed hbar + regular irreducible Weyl representation + finite DOF
=> Schrödinger representation up to unitary equivalence
```

Disallowed:

```text
formal commutator
=> unique representation
```

```text
Weyl relation
=> irreducible
```

```text
finite truncation looks canonical at low levels
=> exact finite-dimensional CCR
```

```text
Stone-von Neumann for finite DOF
=> QFT uniqueness
```

## 11. Provenance

```text
typed applicability / definedness          PRE_EXISTING_DSD
operator-domain discipline                 QM CORE 006 + STANDARD MATH
Hilbert / Q / P / hbar                     TARGET SPECIALIZATION
CCR / Weyl relations                       STANDARD QM/MATH
strong continuity / irreducibility         STANDARD REPRESENTATION THEORY
Stone-von Neumann                          STANDARD MATH
finite trace obstruction                   GENERAL ALGEBRA
truncation boundary witness                GENERAL FINITE-DIM WITNESS
```

## 12. Next interface

Proceed to:

**QM Core 008 — Complex-Hilbert Carrier Closure / Independent-Origin Boundary Gate**

Return to the unresolved Hilbert-carrier origin problem from QM Core 004 before writing the integrated QM reconstruction synthesis.
