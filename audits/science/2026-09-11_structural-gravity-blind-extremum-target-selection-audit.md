# Structural Gravity Blind Extremum Target-Selection Audit

```text
AUDIT_ID: DSD-SG-20260911-BH-TARGET-EXTREMUM-001
STATUS: PASS_WITH_NEGATIVE_RESULT / BLIND_HALF_NOT_SELECTED_BY_NATURAL_FIXED_TRACE_EXTREMA
DATE: 2026-09-11
DOMAIN: structural gravity / black-hole critical-radius benchmark
```

## 1. Question

Can a blind, source-independent target-selection principle pick

\[
\Psi_*=\frac12
\]

from the normalized support pencil without using the Schwarzschild coefficient as an input?

This audit tests four natural candidate classes in the two-mode fixed-trace control family:

1. determinant extremization;
2. spectral-entropy extremization;
3. coercivity / norm extremization;
4. lineage-compatible variational regularization.

No EHT, Schwarzschild-radius, or Kerr quantity is used to choose the target.

## 2. Control family

Fix the normalized spectrum

\[
\operatorname{spec}B=(x,2-x),
\qquad 0<x\le1,
\]

so that

\[
\operatorname{tr}B=2,
\qquad
\Psi_*=\lambda_{\min}(B)=x.
\]

This is a dimensionless two-mode target-selection control, not a physical black-hole law.

## 3. Fixed-trace symmetric extrema

At fixed trace,

\[
\det B=x(2-x),
\]

which is maximized uniquely at

\[
x=1.
\]

The normalized spectral Shannon entropy is also maximized at the equal spectrum

\[
(1,1),
\]

and the Frobenius norm is minimized there.

Thus these three standard symmetry-favoring extrema select

\[
\boxed{\Psi_*=1}
\]

rather than \(1/2\).

Conversely, minimum determinant and minimum entropy approach the positive-definite boundary

\[
x\downarrow0,
\]

so they drive

\[
\Psi_*\to0.
\]

The same conclusion applies to maximizing the minimum eigenvalue/coercivity under fixed trace: the maximum is attained at equal eigenvalues, hence \(\Psi_*=1\).

## 4. Why one-half needs an extra condition

At trace two,

\[
\Psi_*=\frac12
\]

is equivalent to any of the following additional normalized constraints:

\[
\det B=\frac34,
\]

\[
\kappa(B)=\frac{\lambda_{\max}}{\lambda_{\min}}=3,
\]

or

\[
\frac{\lambda_{\max}-\lambda_{\min}}{\operatorname{tr}B}
=\frac12.
\]

Therefore the half coefficient is not selected by the fixed-trace constraint alone. Any successful blind derivation must explain one of these equivalent anisotropy conditions, or another independent condition that implies them.

## 5. Lineage-compatible variational selector

Use the scalarized predecessor threshold \(x_{\rm pre}\) and minimize

\[
J_S(x)
=\frac12(x-x_{\rm pre})^2
+\frac\alpha2(x-x_0)^2.
\]

For the tested universal symmetric objective, \(x_0=1\), giving

\[
x_S^*
=\frac{x_{\rm pre}+\alpha}{1+\alpha}.
\]

For every finite \(\alpha\), source dependence remains whenever the predecessor values differ.

Only the limit \(\alpha\to\infty\) removes lineage dependence, but then the selected value is

\[
\Psi_*=1,
\]

not \(1/2\).

Hence lineage compatibility alone does not select the desired half coefficient.

## 6. DSD boundary

The Structural Reorganization Dynamics framework allows typed transition relations and optional relaxation/coupling dynamics only after explicit constitutive bridges are supplied. It does not provide a canonical determinant, entropy, coercivity, or lineage variational functional for this black-hole target-selection problem.

Therefore these objective functions are control mathematics, not imported DSD theorems.

## 7. Verdict

```text
PASS WITH NEGATIVE RESULT

SURVIVES:
- a common target can still be selected by an additional physical law;
- fixed-trace target selection is mathematically auditable;
- Psi_*=1/2 is representable as a normalized anisotropic spectrum.

REJECTED AS BLIND HALF SELECTORS:
- maximum determinant at fixed trace;
- maximum spectral entropy at fixed trace;
- maximum coercivity / minimum Frobenius norm at fixed trace;
- finite lineage-compatible regularization toward the symmetric target.

NEW REQUIREMENT:
A successful half-coefficient derivation must supply an independent dimensionless anisotropy/constraint law. Under trace 2, det=3/4 or condition number=3 are equivalent witnesses.
```

## 8. Reproducibility

From the repository root:

```bash
python audits/science/2026-09-11_structural_gravity_blind_extremum_target_selection_audit.py --mode all
```

The audit returns 11/11 passing logical/numerical checks.

## 9. Next target

Do not search further among arbitrary symmetric scalar objectives merely to obtain \(1/2\).

Instead audit whether an independently motivated DSD structural quantity can impose a normalized anisotropy constraint, for example through:

- axis-crossing/coupling geometry;
- support-vs-load spectral ratio;
- a transition invariant that survives normalization;
- a dimensional/rank relation that is explicitly connected to the support pencil by a constitutive bridge.

The Schwarzschild comparator remains sealed while such a constraint is searched.