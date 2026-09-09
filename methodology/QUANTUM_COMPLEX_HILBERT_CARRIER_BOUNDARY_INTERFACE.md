# Quantum Complex-Hilbert Carrier Boundary Interface

Status: **ACTIVE — QM Core 008 PASS_WITH_BOUNDARY**

## Purpose

Prevent the standard quantum carrier from being treated as if generic DSD had already derived it.

```text
generic DSD
general operational structure
quantum reconstruction selectors
complex Hilbert comparator
```

These are separate provenance layers.

## Generic DSD

Generic DSD supplies typed identity/status, applicability, prerequisites, defined/undefined/defined-zero, restriction versus equivalence, aggregation/readout diagnostics, and Formation/Property/Dynamics separation.

Do not infer a scalar field from these items.

## General operational layer

With explicit randomized preparation, probabilistic readout, finite separation, and mixture-preserving transformations, a finite-dimensional convex affine description in a real ordered vector space can be obtained.

This is not yet quantum theory.

## Quantum selectors

```text
LDC-QM   local descriptive completeness / local tomography
RRDE-QM  recursive restriction-equivalence
CRR-QM   continuous pure-state reversible reachability
NR-QM    no-restriction/full effect-domain
```

Boundary rules:

```text
CRR-QM alone != complex Hilbert
NR-QM alone  != complex Hilbert
LDC-QM excludes standard real-Hilbert composites
LDC-QM alone != unique complex-QM characterization
```

## Two-rebit tomography witness

\[
K_{\mathbb R}(2)=3,\qquad K_{\mathbb R}(4)=10,
\]

but local product coordinates span only \(3\times3=9\).

For

\[
\rho_\pm=\frac14(I\otimes I\pm cY\otimes Y),\qquad0<c<1,
\]

all local products generated from \(I,X,Z\) have equal statistics, while

\[
\operatorname{Tr}(\rho_\pm Y\otimes Y)=\pm c.
\]

Therefore ordinary local tomography fails for the standard two-rebit composite.

## Complex-QM compatibility

For complex Hermitian carriers,

\[
K_{\mathbb C}(d)=d^2,
\qquad
K_{\mathbb C}(d_Ad_B)=K_{\mathbb C}(d_A)K_{\mathbb C}(d_B).
\]

Do not reverse this into `local tomography -> complex QM` without a complete reconstruction theorem.

## Provenance rule

```text
A PRE_EXISTING_DSD
B GENERAL_OPERATIONAL_DERIVATION
C TARGET_SPECIALIZATION_SELECTOR
D EXACT_COMPARATOR_LOCK
```

The complex Hilbert carrier remains C/D-side structure, not A-side structure.

## Allowed claim

```text
DSD reconstructs substantial standard-QM structure conditionally on an explicit
Hilbert/quantum specialization, while target-independent operational assumptions
reach a real ordered carrier before that specialization.
```

Do not claim:

```text
DSD independently derives complex Hilbert space.
```

## Next interface

Proceed to **QM Core 009 — Integrated Standard-QM Reconstruction Synthesis / Provenance Closure Gate**.