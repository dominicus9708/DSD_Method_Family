# PHY-QM-009 — Arbitrary-POVM lift and measurement-class typing

Date: 2026-09-06

## Purpose
Check whether the one-way-steering / role-sensitive conclusion is merely an artifact of restricting the external quantum bridge to projective measurements, and determine whether the allowed measurement family must be retained as an explicit DSD input.

## External result
Quintino et al., Phys. Rev. A 92, 032107 (2015), prove the following construction.

If a state \(\rho\in\mathbb C^d\otimes\mathbb C^d\) is unsteerable from Alice to Bob for projective measurements but steerable from Bob to Alice, define

\[
\rho' = \frac{1}{d+1}\left[\rho+dP_\perp\otimes\rho_B\right],
\]

where \(P_\perp\) is a projector onto a one-dimensional subspace orthogonal to the support of Alice's reduced state. Then \(\rho'\) is unsteerable from Alice to Bob for arbitrary single-round POVMs while remaining steerable from Bob to Alice.

Thus one-way steering survives a change from the projective-measurement class to the full single-round POVM class, although the physical state is changed by the lift.

## Explicit d=2 control
Use the paper's two-qubit seed

\[
\rho_{1W}=\frac12\left[
\Psi_-+\frac35|1\rangle\langle1|\otimes\frac{I_2}{2}
+\frac25\frac{I_2}{2}\otimes|0\rangle\langle0|
\right].
\]

In the computational basis,

\[
\rho_{1W}=
\begin{pmatrix}
1/10&0&0&0\\
0&1/4&-1/4&0\\
0&-1/4&1/2&0\\
0&0&0&3/20
\end{pmatrix}.
\]

Its Bob marginal is

\[
\rho_B=\operatorname{diag}(3/5,2/5).
\]

For \(d=2\), the POVM lift is a qutrit-qubit state

\[
\boxed{
\rho'_{1W}
=\frac13\rho_{1W}
+\frac23|2\rangle\langle2|\otimes\rho_B.
}
\]

In the ordered basis \(|00\rangle,|01\rangle,|10\rangle,|11\rangle,|20\rangle,|21\rangle\),

\[
\rho'_{1W}=\operatorname{diag-block}\left(
\frac13\rho_{1W},\frac23\rho_B
\right).
\]

The numerical eigenvalues are approximately

\[
0.0318305,\ 0.0333333,\ 0.05,\ 0.2181695,\ 0.2666667,\ 0.4,
\]

so the state is positive and normalized. Its partial transpose contains

\[
\lambda_{\min}\approx-0.04208229684,
\]

hence the lifted state remains entangled.

## Local-filter recovery
Project Alice's qutrit back onto the original two-dimensional support. The success probability is

\[
P_{\rm filter}=1/3,
\]

and the normalized postselected state is exactly \(\rho_{1W}\). The reproducibility script verifies zero numerical recovery error up to floating-point precision.

This is consistent with the paper's proof: local filtering cannot create the seed's steering/entanglement from a state lacking the required resource.

## DSD measurement-class coordinate
The safe downstream profile is therefore

```text
STEERING(state, untrusted-party, trusted-party, measurement-class, protocol-class)
```

rather than a bare `STEERING(state)` label.

The measurement family is not a decorative annotation. Statements such as

```text
unsteerable for all projective measurements
unsteerable for all single-round POVMs
steerable after a sequential local filter
```

refer to different model classes and must not be merged.

## Audit verdict
- `one-way steering is only a projective-measurement artifact`: **REJECT**.
- `measurement class can be erased from the typed input without loss`: **REJECT**.
- `PVM and arbitrary-POVM one-way steering are the same state-level statement`: **REJECT**. The POVM theorem uses an explicit lifted state.
- `DSD Property core derives the POVM lift`: **REJECT**. The lift is imported quantum theory.
- `DSD can represent the distinction by auxiliary typed input and explicit specialization`: **PASS**.

## DSD impact
The previous distinction between readout reconstruction and model-class completion is strengthened. Steering status is indexed not only by state and party direction but also by the allowed operation/measurement family.

A useful downstream notation is

\[
\mathsf{LHSComp}(\rho;U\to T,\mathcal M,\mathcal P),
\]

where \(\mathcal M\) is the measurement class and \(\mathcal P\) the allowed preprocessing/protocol class.

This remains a specialization-level diagnostic, not a new universal DSD axiom.

## Reproducibility

```bash
python audits/science/2026-09-06_one_way_steering_dsd_role_audit.py
```

External source:
- M. T. Quintino et al., *Inequivalence of entanglement, steering, and Bell nonlocality for general measurements*, Phys. Rev. A 92, 032107 (2015), doi:10.1103/PhysRevA.92.032107.
