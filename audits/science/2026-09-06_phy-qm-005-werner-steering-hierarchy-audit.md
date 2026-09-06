# PHY-QM-005 — Werner-state steering hierarchy audit

Date: 2026-09-06

## Aim
Separate four logically different thresholds in the two-qubit Werner family:

1. entanglement,
2. exact EPR steerability,
3. detection by a finite three-setting steering witness,
4. CHSH violation.

The objective is not to derive quantum mechanics from DSD. Standard quantum mechanics supplies the state space, Born rule, projective/POVM measurements, and steering/LHS definitions. DSD analysis is used to classify which completion or reconstruction problem fails at each threshold.

## External specialization
Use the two-qubit Werner state

\[
\rho_W(p)=p|\Psi^-\rangle\langle\Psi^-|+(1-p)I_4/4,
\qquad 0\le p\le1.
\]

Equivalently,

\[
\rho_W(p)=\frac14\left(I\otimes I-p\sum_{j=x,y,z}\sigma_j\otimes\sigma_j\right).
\]

For Alice's projective measurement along unit direction \(n\),

\[
M_{a|n}=\frac12(I+a\,n\cdot\sigma),\qquad a\in\{\pm1\},
\]

the subnormalized state prepared for Bob is

\[
\boxed{
\sigma_{a|n}=\operatorname{Tr}_A[(M_{a|n}\otimes I)\rho_W]
=\frac14\left(I-a p\,n\cdot\sigma\right).
}
\]

The no-signalling consistency condition is immediate:

\[
\sum_a\sigma_{a|n}=I/2
\]

independently of Alice's direction \(n\).

## LHS completion problem
An assemblage is unsteerable from Alice to Bob if it admits a local-hidden-state completion

\[
\sigma_{a|x}=\sum_\lambda p(\lambda)\,p(a|x,\lambda)\,\rho_\lambda.
\]

This is an asymmetric completion problem: Alice's outputs are untrusted classical response data, while Bob's conditional quantum states are trusted objects.

In DSD terms, this is not the same question as whether the assemblage itself is well-defined or reconstructs the global density operator. It is a feasibility question for a restricted explanatory factorization.

## Three-setting finite witness
For three orthogonal Pauli directions, use the normalized linear steering witness

\[
F_3=\frac1{\sqrt3}\sum_{k=x,y,z}\langle A_k\sigma_k^B\rangle.
\]

For any LHS model, a hidden Bob state has Bloch vector \(r\) with \(|r|\le1\), while Alice may choose deterministic signs \(A_k=\pm1\). Therefore

\[
\sum_k A_k r_k\le \sqrt3,
\]

and hence

\[
\boxed{F_3\le1\quad\text{for all LHS models}.}
\]

For the Werner singlet family, choosing Alice's declared sign to align the anticorrelation gives

\[
F_3=\sqrt3\,p.
\]

Thus this finite witness detects steering only when

\[
\boxed{p>1/\sqrt3\approx0.5773502692.}
\]

## Exact steering threshold
External quantum-steering results establish that the two-qubit Werner state admits an LHS model for all POVMs when \(p\le1/2\), while it is steerable when \(p>1/2\). The 2024 exact-bound results close the previous POVM gap.

Therefore

\[
\boxed{p_{\rm steer}^{\rm exact}=1/2.}
\]

This is strictly below the three-setting witness threshold.

## Entanglement threshold
The partial-transpose eigenvalues are

\[
\frac{1+p}{4}\quad(\times3),
\qquad
\frac{1-3p}{4}\quad(\times1).
\]

Hence

\[
\boxed{p>1/3\iff\rho_W(p)\text{ is entangled}.}
\]

## CHSH threshold
For the Werner correlation tensor \(T=-pI_3\), the Horodecki CHSH maximum is

\[
S_{\max}=2\sqrt2\,p.
\]

Thus CHSH is violated iff

\[
\boxed{p>1/\sqrt2\approx0.7071067812.}
\]

This is a CHSH-detection threshold. It is not asserted here to be the exact threshold for Bell nonlocality under all possible Bell inequalities and measurements.

## Surviving hierarchy
The safe hierarchy for this controlled family is

\[
\boxed{
\frac13
<
\frac12
<
\frac1{\sqrt3}
<
\frac1{\sqrt2}.
}
\]

Interpretation by interval:

- \(0\le p\le1/3\): separable.
- \(1/3<p\le1/2\): entangled but unsteerable even for arbitrary POVMs.
- \(1/2<p\le1/\sqrt3\): steerable in principle, but not detected by this three-setting linear witness.
- \(1/\sqrt3<p\le1/\sqrt2\): detected by the three-setting steering witness, but no CHSH violation.
- \(p>1/\sqrt2\): CHSH violation as well.

## DSD audit conclusions

### Confirmed

1. `entanglement = steering`: false.
2. `steering = CHSH violation`: false.
3. `failure of one finite witness = absence of the property`: false.
4. LHS completion is a different problem from local marginal no-signalling.
5. Steering must be typed directionally as \(A\to B\) or \(B\to A\); it is not intrinsically a symmetric property label.
6. Operational no-signalling can coexist with steering.

### DSD interpretation
A useful separation is

```text
ASSEMBLAGE_DEFINED
ASSEMBLAGE_RECONSTRUCTIVE_POWER
LHS_COMPLETION_EXISTS
FINITE_STEERING_WITNESS_VIOLATED
CHSH_WITNESS_VIOLATED
CAUSAL_SUPPORT_BOUND
```

These fields must not be collapsed into one scalar `nonlocality` flag.

## Status
PASS_WITH_BOUNDARY.

DSD provides a clean classification of distinct quantum-correlation and completion questions, but it does not derive the Born rule, the LHS set, the exact steering threshold, or the Bell inequalities. Those remain supplied quantum-domain structures.

## Reproducibility

```bash
python audits/science/2026-09-06_werner_dsd_steering_hierarchy.py
```

References used for the external quantum facts:

- H. M. Wiseman, S. J. Jones, A. C. Doherty, Phys. Rev. Lett. 98, 140402 (2007).
- Y. Zhang, E. Chitambar, Phys. Rev. Lett. 132, 250201 (2024).
- M. J. Renner, Phys. Rev. Lett. 132, 250202 (2024).
