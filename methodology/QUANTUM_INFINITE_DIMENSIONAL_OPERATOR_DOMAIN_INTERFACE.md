# Quantum Infinite-Dimensional Operator / Domain Interface

Status: **ACTIVE — QM Core 006 PASS_WITH_REFINEMENT**

## Purpose

This interface prevents the finite-dimensional matrix intuition from collapsing the following structures:

```text
state
operator symbol
operator domain
self-adjoint realization
spectral probability
operator action
generator derivative
```

It is downstream of the Hilbert-space quantum specialization.  
It is not a generic DSD axiom.

## 1. Operator identity rule

For an unbounded operator, record

\[
(A,D(A))
\]

rather than only the formal symbol \(A\).

Core rule:

\[
\boxed{
\text{same formal expression}
\not\Rightarrow
\text{same operator}
}
\]

when domains differ.

## 2. Self-adjointness gate

```text
SYMMETRIC
    <phi,A psi> = <A phi,psi> on D(A)

SELF_ADJOINT
    A = A*
    including D(A) = D(A*)

ESSENTIALLY_SELF_ADJOINT
    closure of A is self-adjoint
```

Never replace `SELF_ADJOINT` with `SYMMETRIC` in an observable/generator claim.

## 3. IDU-QM selector

```text
IDU-QM  Infinite-Dimensional Unbounded-Operator Gate

input:
    Hilbert carrier H
    state psi or rho
    operator label A

supply when A is unbounded:
    domain D(A)
    adjoint/domain relation
    self-adjoint or extension status
    spectral PVM E_A for observable use
    topology for limiting/evolution claims

state prerequisites:
    SPECTRAL_PROBABILITY      psi in H
    FINITE_FIRST_MOMENT       psi in D(|A|^(1/2))
    OPERATOR_ACTION           psi in D(A)
    GENERATOR_DERIVATIVE      psi in D(generator)
```

## 4. Spectral readout interface

For self-adjoint \(A\),

\[
A=\int \lambda\,dE_A(\lambda).
\]

For every normalized vector state,

\[
\mu_\psi(\Delta)
=
\langle\psi,E_A(\Delta)\psi\rangle
\]

is defined.

Thus:

```text
state defined
spectral probability defined
A psi undefined
```

is a legitimate status combination when \(\psi\notin D(A)\).

Do not mark the state itself undefined merely because an operator action is inapplicable.

## 5. Position and momentum exemplars

Position:

\[
(Q\psi)(x)=x\psi(x),
\qquad
D(Q)=\{\psi:x\psi\in L^2\}.
\]

Momentum on the line:

\[
P=-i\hbar\,d/dx
\]

with its self-adjoint Sobolev domain.

Both are unbounded.

A finite matrix is therefore an approximation/representation choice, not the literal full operator.

## 6. Stone/dynamics rule

For a strongly continuous one-parameter unitary group,

\[
U(t)=e^{-itA}
\]

with unique self-adjoint generator \(A\).

But

\[
\frac{d}{dt}U(t)\psi
\]

is a strong Hilbert-space derivative only for vectors in the generator domain.

Therefore:

```text
UNITARY_GROUP_APPLICABLE        all psi in H
GENERATOR_DERIVATIVE_APPLICABLE only psi in D(A)
```

Do not infer everywhere differentiability from strong continuity.

## 7. Boundary-condition identity rule

For differential operators, a boundary condition can be part of the operator identity.

Example on \(L^2(0,1)\):

\[
P_\theta=-i\,d/dx,
\qquad
D(P_\theta)=\{\psi\in H^1(0,1):\psi(1)=e^{i\theta}\psi(0)\}.
\]

Different \(\theta\) values are distinct self-adjoint realizations of the same formal differential expression.

## 8. Earlier-interface compatibility

```text
005D Stone/Hamiltonian:
    survives with generator-domain refinement

005E finite GKSL:
    do not export bounded finite-dimensional formula blindly
    unbounded generators require extra domain/conservativity hypotheses

005F Stinespring:
    general dilation survives
    finite environment/Kraus bookkeeping does not automatically survive

005G Naimark:
    general dilation survives
    dilation space may be infinite-dimensional
```

## 9. Finite-truncation warning

For finite matrices,

\[
\operatorname{Tr}[A,B]=0.
\]

Hence

\[
[A,B]=i\hbar I
\]

cannot hold exactly in finite dimension.

A truncated oscillator matrix may be a numerical approximation, but it is not an exact proof of the canonical commutation relation.

## 10. DSD role separation

```text
Formation:
    system / observable / boundary-convention identity

Property:
    state
    domain membership
    extension label
    spectral probability
    finite-moment status

Static Aggregation:
    selected bounded readouts / spectral probabilities

Dynamics:
    unitary or semigroup law
    generator-domain applicability

Quantum specialization:
    Hilbert / self-adjoint / spectral / Stone structure
```

Core rule:

\[
\boxed{
\text{state describability}
\not\Rightarrow
\text{universal operator applicability}
}
\]

## 11. Provenance

```text
typed applicability                         PRE_EXISTING_DSD
undefined-vs-defined distinction            PRE_EXISTING_DSD
Hilbert carrier                             TARGET SPECIALIZATION
operator-domain discipline                  STANDARD FUNCTIONAL ANALYSIS
self-adjoint observable structure           STANDARD QM/MATH
spectral theorem                            STANDARD QM/MATH
Stone theorem                               STANDARD QM/MATH
unbounded-generator warning                 STANDARD OPEN-QM BOUNDARY
```

## 12. Next interface

Proceed to:

**QM Core 007 — Canonical Position–Momentum / CCR / Weyl Representation Gate**

with exact common-domain and Stone-von Neumann prerequisites.
