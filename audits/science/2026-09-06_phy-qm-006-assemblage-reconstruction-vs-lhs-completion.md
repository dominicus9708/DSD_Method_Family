# PHY-QM-006 — Assemblage reconstruction versus LHS completion

Date: 2026-09-06

## Aim
Test whether quantum steering can be reduced to an ordinary DSD reconstruction/injectivity failure.

Result: no. A measurement assemblage can be informationally complete for the underlying two-qubit state while still failing an LHS completion test.

## General two-qubit Bloch representation
Write a trace-one two-qubit state as

\[
\rho=\frac14\left[
I\otimes I
+r_i\sigma_i\otimes I
+s_jI\otimes\sigma_j
+T_{ij}\sigma_i\otimes\sigma_j
\right].
\]

The real parameter count is

\[
3+3+9=15.
\]

For Alice's projective measurement along a unit vector \(n\),

\[
M_{a|n}=\frac12(I+a\,n\cdot\sigma),
\]

the Bob assemblage element is

\[
\boxed{
\sigma_{a|n}
=
\frac14\left[
(1+a\,r\cdot n)I
+
(s+aT^Tn)\cdot\sigma
\right].
}
\]

## One-, two-, and three-axis identifiability
Take Alice's known axes from \(X,Y,Z\).

The linear map from the 15-dimensional trace-one Hermitian perturbation space to assemblage coordinates has numerically verified ranks

```text
1 axis : rank 7,  kernel dimension 8
2 axes : rank 11, kernel dimension 4
3 axes : rank 15, kernel dimension 0
```

These numbers can also be read analytically:

- the common Bob marginal supplies \(s\in\mathbb R^3\);
- each new independent Alice axis supplies one component of \(r\) and three components of the corresponding row of \(T\), for four new real coordinates.

Hence

\[
\operatorname{rank}\Phi_m=3+4m,
\qquad m=1,2,3,
\]

until saturation at 15.

Therefore the three-axis Pauli assemblage is injective on the full two-qubit trace-one Hermitian state space:

\[
\boxed{\ker\Phi_{XYZ}=\{0\}.}
\]

## Explicit inverse
Let

\[
\rho_B=\sum_a\sigma_{a|i},
\]

which is independent of the Alice setting \(i\). Then

\[
s_j=\operatorname{Tr}(\rho_B\sigma_j).
\]

For each Alice Pauli direction \(i\), define

\[
\Delta_i=\sigma_{+|i}-\sigma_{-|i}.
\]

Then

\[
r_i=\operatorname{Tr}(\Delta_i),
\]

and

\[
T_{ij}=\operatorname{Tr}(\Delta_i\sigma_j).
\]

Thus \((r,s,T)\), and therefore \(\rho\), can be reconstructed exactly from the three-axis assemblage.

## Steering still remains a separate question
An LHS completion requires

\[
\sigma_{a|x}=\sum_\lambda p(\lambda)p(a|x,\lambda)\rho_\lambda.
\]

This asks whether the already-defined and potentially informationally complete assemblage belongs to a restricted convex model class.

Therefore

\[
\boxed{
\text{state reconstruction completeness}
\neq
\text{LHS completion existence}.
}
\]

A steerable state can have an assemblage from which the state is fully reconstructible. Steering is therefore not an information-loss/kernel phenomenon by itself.

## DSD consequence
The readout-fiber diagnostic

\[
\mathcal F_C(s)=\Phi_C^{-1}(\Phi_C(s))
\]

is powerful for reconstruction questions, but it is insufficient as a universal diagnostic for quantum nonclassicality.

A second class of tests is required:

\[
\boxed{
\text{RECONSTRUCTION TEST: }\ker\Phi_C\overset{?}=0
}
\]

versus

\[
\boxed{
\text{MODEL-COMPLETION TEST: }\Phi_C(s)\overset{?}\in\mathcal M_C,
}
\]

where \(\mathcal M_C\) is a supplied restricted explanatory model class such as the LHS set, Bell-local set, separable set, or noncontextual set.

This produces a more general DSD-analysis distinction:

```text
READOUT_COLLISION / NON-INJECTIVITY
    versus
MODEL-CLASS NON-COMPLETABILITY
```

Neither implies the other in general.

## Directionality
Steering is asymmetric because the trusted quantum-state side is part of the definition. DSD typing should therefore use an ordered role structure such as

```text
STEERING_TEST(
  untrusted_party=A,
  trusted_party=B,
  context_family=C,
  assemblage=Sigma,
  model_class=LHS(A->B)
)
```

rather than a symmetric binary property `STEERED(A,B)`.

The Werner family used in PHY-QM-005 is symmetric, so it does not itself witness one-way steering; the directionality conclusion comes from the structure of the steering definition, not from that symmetric control family.

## Audit verdict

- `steering = readout non-injectivity`: REJECTED.
- `informationally complete assemblage -> unsteerable`: REJECTED.
- reconstruction and restricted-model completion must be separate DSD audit stages: CONFIRMED.
- steering must preserve trusted/untrusted party roles: CONFIRMED.

## Status
PASS_WITH_CORRECTION.

The correction is methodological: DSD quantum analysis must not treat every nonclassicality witness as a loss-of-describability problem. Some are instead impossibility-of-completion problems inside a supplied model class.

## Reproducibility

```bash
python audits/science/2026-09-06_werner_dsd_steering_hierarchy.py
```
