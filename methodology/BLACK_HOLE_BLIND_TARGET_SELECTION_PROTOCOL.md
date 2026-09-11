# Black-Hole Blind Target-Selection Protocol

```text
METHOD_ID: DSD-METHOD-20260911-BH-BLIND-TARGET-SELECT-001
STATUS: ACTIVE_REFINEMENT
DATE: 2026-09-11
DOMAIN: structural gravity / black-hole critical radius
```

## Purpose

This protocol governs attempts to determine the normalized strong-field support target \(B_*\) and its minimum generalized eigenvalue \(\Psi_*\) without fitting the Schwarzschild coefficient.

## Current normalized object

Use

\[
B(S)=L(S)^{-1/2}H_0(S)L(S)^{-1/2},
\qquad
\Psi_*(S)=\lambda_{\min}B(S).
\]

The current critical-radius candidate remains

\[
R_{\rm crit}
=\frac{K_{\rm eff}M}{c_{\rm info}^2\Psi_*}.
\]

A universal black-hole coefficient therefore requires a source-independent normalized target or at minimum a source-independent \(\Psi_*\).

## Blindness rule

The target selector must be fixed before the Schwarzschild comparator is opened.

Forbidden as derivation inputs:

- \(R_S=2GM/c^2\);
- EHT ring/shadow sizes;
- the desired value \(\Psi_*=1/2\);
- a determinant, condition number, anisotropy ratio, or coupling constant chosen because it is algebraically equivalent to \(\Psi_*=1/2\).

## Natural fixed-trace objective audit

For the two-mode control

\[
\operatorname{spec}B=(x,2-x),
\qquad 0<x\le1,
\]

with trace fixed to two:

- maximum determinant selects \(x=1\);
- maximum spectral entropy selects \(x=1\);
- maximum coercivity / minimum Frobenius norm selects \(x=1\);
- corresponding boundary-minimizing objectives drive \(x\to0\).

Hence none of these natural symmetric objectives blind-selects \(x=1/2\).

## Equivalent half constraints

Within the same control family,

\[
\Psi_*=\frac12
\]

is equivalent to

\[
\det B=\frac34,
\]

\[
\frac{\lambda_{\max}}{\lambda_{\min}}=3,
\]

and

\[
\frac{\lambda_{\max}-\lambda_{\min}}{\operatorname{tr}B}=\frac12.
\]

These are useful diagnostic equivalences only. They are not independent derivations unless a separate DSD bridge selects one of them.

## Lineage rule

A lineage-compatible variational objective may retain predecessor information. If

\[
J_S(x)=J_{\rm lineage}(x;x_{\rm pre})+\alpha J_{\rm common}(x),
\]

then a finite lineage weight generically preserves source dependence.

A universal target requires either:

1. a sufficiently dominant common objective with a source-independent unique minimizer;
2. predecessor differences lying entirely in null directions invisible to the target readout;
3. a transition/coarse-graining law that explicitly removes the relevant predecessor dependence.

Lineage compatibility itself does not determine the target spectrum.

## Axis-crossing geometry rule

When a realized-axis specialization is supplied, a pair of unoriented lines can contribute the geometric invariant

\[
s_{ab}=\operatorname{tr}(P_aP_b)=\cos^2\theta_{ab}.
\]

This is only a geometric/relational input. A support-pencil contribution still requires a constitutive map such as

\[
g=\beta F(s_{ab}).
\]

The geometry does not uniquely fix \(F\) or \(\beta\). Rotation-invariant examples such as

\[
F(s)=s,
\qquad
1-s,
\qquad
s(1-s),
\qquad
1
\]

produce different normalized support spectra for the same crossing angle.

Therefore neither a 45-degree crossing, cyclic triadic closure, nor realized-axis rank is accepted as an independent half-coefficient selector unless a separate constitutive law fixes both the geometric input and the coupling normalization.

The current rule is:

\[
\boxed{
\text{axis geometry}
\not\Rightarrow
\text{support anisotropy}
}
\]

without an explicit geometry-to-operator bridge.

## Acceptance criterion for a future half-coefficient result

A result may be labeled `BLIND_HALF_RECOVERY_CANDIDATE` only if all are satisfied:

1. the selector was defined without using the Schwarzschild coefficient or an algebraically equivalent fitted constraint;
2. the selector has a unique or demonstrably source-independent admissible target;
3. the target gives \(\Psi_*=1/2\) analytically or within a predeclared numerical tolerance;
4. the result survives changes of source mass and internal profile without retuning;
5. every constitutive bridge is explicitly identified;
6. the same rule survives at least one independent target family before comparison to GR;
7. if axis geometry is used, both the geometric invariant and the geometry-to-coupling normalization are independently fixed rather than fitted.

## Current verdict

```text
BLIND TARGET SELECTION STATUS:
OPEN

NEGATIVE RESULTS:
- natural fixed-trace determinant/entropy/coercivity extrema do not select one-half;
- axis-crossing geometry alone does not select one-half;
- triadic closure/rank alone does not determine the support pencil.

NEW BOTTLENECK:
Find an independently motivated combined constitutive invariant linking geometry/state data to the normalized support/load spectrum.
```

## Reproducibility

```bash
python audits/science/2026-09-11_structural_gravity_blind_extremum_target_selection_audit.py --mode all
python audits/science/2026-09-11_structural_gravity_axis_crossing_anisotropy_audit.py --mode all
```
