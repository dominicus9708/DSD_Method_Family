# Quantum Kraus–Stinespring Dilation Interface

Status: **Methodology interface / downstream quantum specialization**  
Audit source: **QM Core 005F**

## 1. Purpose

This interface prevents a finite-dimensional CPTP map from being conflated with one particular Kraus list, one particular Stinespring environment coordinate system, or one literal microscopic environment.

It is a representation package, not a new DSD primitive axiom.

## 2. Terminology lock

```text
DSD_FORMATION_CHANNEL
  = Stage-VI DSD tuple with formation identity.

QUANTUM_CHANNEL_MAP
  = target-theory CPTP linear map on operators.

KRAUS_REPRESENTATION
  = one operator-sum representation of the quantum channel map.

STINESPRING_ISOMETRY
  = one isometric dilation whose environment partial trace gives the map.

UNITARY_PLUS_ANCILLA_REALIZATION
  = a unitary completion after an initialized ancilla and any required dimension padding.

PHYSICAL_ENVIRONMENT_CLAIM
  = an additional physical interpretation that is not supplied by the representation theorem alone.
```

Never infer equality between the first two merely from the shared word `channel`.

## 3. Finite-dimensional gate

For finite-dimensional complex Hilbert spaces, admit a CPTP map

\[
\Phi:\mathcal L(\mathcal H_A)\to\mathcal L(\mathcal H_B).
\]

Then standard quantum information theory supplies a Kraus family

\[
\Phi(X)=\sum_aK_aXK_a^\dagger,
\qquad
\sum_aK_a^\dagger K_a=I_A,
\]

and an isometry

\[
V:\mathcal H_A\to\mathcal H_B\otimes\mathcal H_E
\]

such that

\[
\Phi(X)=\operatorname{Tr}_E(VXV^\dagger).
\]

A minimal environment may be chosen with

\[
\dim\mathcal H_E=\operatorname{rank}J(\Phi),
\]

where \(J(\Phi)\) is the Choi operator.

## 4. Equivalence discipline

Primary comparison object:

\[
\Phi.
\]

Representation coordinates are secondary.

A different Kraus list or Stinespring coordinate package does not define a different quantum channel if the induced linear map is identical.

Recommended representation fiber:

\[
\mathcal R_{\mathrm{KSD}}(\Phi)
=
\{\text{admitted Kraus/Stinespring packages inducing }\Phi\}.
\]

The fiber may contain many elements.

## 5. Kraus branch warning

A Kraus label \(a\) is not automatically:

```text
an observed outcome,
a classical event,
a unique physical trajectory,
a uniquely identified environmental state.
```

To give a branch operational meaning, require an explicit instrument or measurement bridge.

## 6. Environment warning

A Stinespring auxiliary space is mathematically sufficient for dilation.

Do not infer from that theorem alone:

```text
literal bath identity,
microscopic composition,
unique environment basis,
unique interaction Hamiltonian,
DSD geometric dimension,
realized-axis rank.
```

## 7. Unitary-extension rule

When input and output system dimensions match, identify

\[
\mathcal H_S\cong\mathcal H_S\otimes|0_E\rangle
\]

as an input subspace and extend the Stinespring isometry to a unitary on the larger joint space.

For unequal input/output dimensions, explicitly add padding/ancilla spaces until the total input and output dimensions match. Do not write a square unitary without this bookkeeping.

## 8. DSD placement

```text
Formation:
  stable DSD structural/operational identities

Property:
  optional typed state/effect/property records

Static Aggregation:
  reduced time-slice readouts after explicit bridges

Dynamics:
  supplied quantum transition map Phi

Quantum representation package:
  Kraus family
  Stinespring isometry
  environment coordinate choice
  optional unitary completion
```

Representation data remain downstream unless an application explicitly promotes selected coordinates into typed physical data.

## 9. Reversibility rule

Do not infer reduced reversibility from global unitary dilation.

A system channel can lose distinguishability after the environment is discarded even though the enlarged joint evolution is exactly unitary.

Use the physical inverse criterion from QM Core 005C when reduced reversibility matters.

## 10. Provenance label

```text
finite Hilbert carrier                 TARGET SPECIALIZATION
CPTP status                            QM Core 005A+005B
Kraus/Stinespring equivalence          STANDARD QM
Choi-rank minimality                   STANDARD QM
unitary completion                     STANDARD FINITE-DIM LINEAR ALGEBRA
DSD representation separation          PRE-EXISTING DSD DISCIPLINE
literal physical environment           NOT DERIVED
```

## 11. Next interface

QM Core 005G should use this package to audit Naimark dilation and quantum instruments, with explicit separation among POVM effects, projective dilation, ancilla coordinates, outcome records, and laboratory implementation.
