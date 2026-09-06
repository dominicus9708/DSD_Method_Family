# PHY-QM-007 — One-way steering as ordered-role describability

Date: 2026-09-06

## Purpose
Test whether the DSD Property core's ordered typed-input discipline is materially required, rather than cosmetic, in a standard quantum-information setting where the same bipartite state has different steering status under exchanged operational roles.

## External quantum bridge
Use the two-qubit family of Bowles, Vértesi, Quintino, and Brunner, Phys. Rev. Lett. 112, 200402 (2014),

\[
\rho_{AB}(\alpha)
=\alpha\Psi_-
+\frac{1-\alpha}{5}\left(
2|0\rangle\langle0|\otimes\frac{I}{2}
+3\frac{I}{2}\otimes|1\rangle\langle1|
\right).
\]

The external paper proves that for projective measurements:

- \(\rho_{AB}(\alpha)\) is unsteerable from Bob to Alice for \(\alpha\le 1/2\);
- a 14-setting steering test detects Alice-to-Bob steering for \(\alpha\gtrsim0.4983\);
- at \(\alpha=1/2\), an explicit 13-setting steering inequality is also available.

These steering facts are imported external results. The accompanying DSD script does not re-prove the SDP/LHS theorem.

## Exact state control at alpha = 1/2
In the computational basis \(|00\rangle,|01\rangle,|10\rangle,|11\rangle\),

\[
\rho_{AB}(1/2)=
\begin{pmatrix}
0.10&0&0&0\\
0&0.50&-0.25&0\\
0&-0.25&0.25&0\\
0&0&0&0.15
\end{pmatrix}.
\]

Its eigenvalues are approximately

\[
0.0954915,\ 0.10,\ 0.15,\ 0.6545085,
\]

so the state is positive. The partial transpose contains the negative eigenvalue

\[
\lambda_{\min}(\rho^{T_B})\approx-0.1262468905,
\]

hence the state is entangled. The analytic PPT threshold of the family is

\[
\alpha_{\rm ent}=\frac{-6+5\sqrt6}{19}\approx0.3288130902.
\]

## Local and correlation data
For the family,

\[
\rho_A=\frac12 I+\frac{1-\alpha}{5}Z,
\qquad
\rho_B=\frac12 I-\frac{3(1-\alpha)}{10}Z,
\]

or in Bloch-vector form

\[
r_A=\left(0,0,\frac{2(1-\alpha)}5\right),
\qquad
r_B=\left(0,0,-\frac{3(1-\alpha)}5\right).
\]

At \(\alpha=1/2\),

\[
r_A=(0,0,0.2),\qquad r_B=(0,0,-0.3).
\]

The correlation tensor is

\[
T=-\alpha I_3,
\]

so at \(\alpha=1/2\), \(T=-I_3/2\).

The local purities are unequal:

\[
\operatorname{Tr}\rho_A^2=0.52,
\qquad
\operatorname{Tr}\rho_B^2=0.545.
\]

Thus this concrete one-way-steering witness is not swap-symmetric as a labeled bipartite state. Role asymmetry is not being created by notation alone.

## Directional steering status
At \(\alpha=1/2\), with the measurement class fixed to arbitrary local projective measurements,

\[
\boxed{
\operatorname{Steer}_{\rm PVM}(A\to B)=1,
\qquad
\operatorname{Steer}_{\rm PVM}(B\to A)=0.
}
\]

The two queries use the same density operator but different ordered operational roles: untrusted measuring party versus trusted tomographic party.

## DSD specialization
A safe typed profile is therefore not

```text
STEERING(state, party-pair)
```

but at least

```text
STEERING(state, untrusted-party, trusted-party, measurement-class)
```

with an ordered profile. This matches the current Property Axiom System rule that the order of typed coordinates is retained unless an explicit symmetry condition is supplied.

## Audit verdict
- `steering is an intrinsic scalar label of the unlabeled bipartite state`: **REJECT**.
- `STEERING(A,B) may be silently symmetrized in A,B`: **REJECT**.
- `the role order must be retained in the typed property input`: **PASS**.
- `one-way steering is caused by DSD role labels alone`: **REJECT**. The external state itself is asymmetric under swap.
- `different steering direction implies superluminal signalling`: **REJECT**. The assemblage still satisfies the standard no-signalling sum rule.

## DSD impact
This is a nontrivial external witness for the Property-core design choice that ordered typed input profiles must remain ordered unless symmetry is separately supplied. It does not add a new Property axiom; it supplies a quantum specialization in which deleting the order destroys physically relevant information.

## Reproducibility

```bash
python audits/science/2026-09-06_one_way_steering_dsd_role_audit.py
```

External sources:
- J. Bowles, T. Vértesi, M. T. Quintino, N. Brunner, *One-way Einstein-Podolsky-Rosen Steering*, Phys. Rev. Lett. 112, 200402 (2014), doi:10.1103/PhysRevLett.112.200402.
