# BH-RB-011 — Finite-core turning-point / trapping compatibility gate

Date: 2026-09-14

Status: **PASS_WITH_BOUNDARY / TURNING_POINT_REQUIRES_NONTRAPPED_OR_MARGINAL_STATE / FINITE_CORE_NOT_DERIVED**

## Scope

This audit continues the QM/relativity-based DSD gravity rebaseline without reusing the discarded structural-gravity branch. The purpose is not to derive a DSD gravity law, but to determine what standard spherical GR already permits or forbids for a finite-radius successor core.

The target is a timelike, spherically symmetric material shell with areal radius `R(t,r)` and Misner–Sharp mass `m(t,r)`.

## Standard spherical-GR kinematic gate

In geometrized units `G=c=1`, define

\[
U=D_T R,
\qquad
\Gamma=\frac{R'}{B}.
\]

The Misner–Sharp constraint is

\[
\Gamma^2
=
1+U^2-\frac{2m}{R}.
\]

For a material-shell turning point,

\[
U=0,
\]

so

\[
\Gamma^2
=
1-\frac{2m}{R}.
\]

Therefore a regular real `Gamma` requires

\[
\boxed{\frac{2m}{R}\le 1}
\]

at the turning event.

Hence

\[
\boxed{
\frac{2m}{R}>1
\quad\Longrightarrow\quad
U\ne0
}
\]

for the regular comoving timelike-fluid branch.

This is stronger than the previous statement that a finite-radius body can temporarily exist in a trapped region. BH-RB-009 remains valid: `0<R<2m` is possible during continuing collapse. However, a shell cannot *stop its areal-radius motion* there while the same shell remains strictly trapped.

## Correction/refinement to BH-RB-010

BH-RB-010 separated “matter bounce” from “causal untrapping” at a conceptual level. BH-RB-011 sharpens this for the present spherical Misner–Sharp branch:

\[
\boxed{
\text{strictly trapped material shell}
+U=0
\text{ is kinematically incompatible}
}
\]

Thus a genuine shell bounce

\[
U<0\rightarrow U=0\rightarrow U>0
\]

must reach a marginal or untrapped local state by the turning event, unless one abandons at least one of the assumptions used here (regular spherical comoving timelike matter, the standard Misner–Sharp relation, or the same shell description across the transition).

This does not imply that the global event horizon must already have disappeared; event horizons are global objects. The statement is local and concerns the Misner–Sharp trapping condition of the turning shell.

## Minimum velocity magnitude in a trapped region

For compactness

\[
C=\frac{2m}{R}>1,
\]

reality of `Gamma` requires

\[
U^2\ge C-1,
\]

or

\[
\boxed{|U|\ge\sqrt{C-1}}.
\]

`U` is the proper-time derivative of areal radius, not an ordinary local special-relativistic speed.

Therefore a strictly trapped shell cannot asymptote to a fixed positive radius with `U->0` while keeping `C>1` fixed. If a future-complete finite radius is to survive, either `C` must approach `<=1`, the mass/radius relation must change, or the present material-shell description must cease to apply.

## Weakest nondissipative anisotropic acceleration gate

For a nondissipative anisotropic fluid with energy density `mu`, radial pressure `p_r`, tangential pressure `p_t`, standard spherical GR gives

\[
(\mu+p_r)D_TU
=
-(\mu+p_r)\left(\frac{m}{R^2}+4\pi p_rR\right)
-\Gamma^2
\left[
D_Rp_r+\frac{2(p_r-p_t)}{R}
\right].
\]

At a kinematically admissible turning point with `C<1`,

\[
\Gamma^2=1-C>0.
\]

Assuming `mu+p_r>0`, outward acceleration requires

\[
\boxed{
-\Gamma^2
\left[
D_Rp_r+\frac{2(p_r-p_t)}{R}
\right]
>
(\mu+p_r)
\left(\frac{m}{R^2}+4\pi p_rR\right)
}.
\]

Equivalently,

\[
D_Rp_r+\frac{2(p_r-p_t)}{R}
<
-\frac{(\mu+p_r)(m/R^2+4\pi p_rR)}{\Gamma^2}.
\]

If the numerator remains finite and positive, the required stress-gradient magnitude diverges as

\[
C\to1^-.
\]

Therefore ordinary finite stress support becomes progressively less able to produce a turning point arbitrarily close to the marginal surface. At `C=1`, the finite hydrodynamic term is suppressed by `Gamma^2=0`; with positive `mu+p_r` and positive `m/R^2+4*pi*p_r*R`, the reduced equation does not produce an outward bounce.

This does **not** close special branches with radial tension, heat flow, nonzero dissipation, vanishing effective inertial density, singular gradients, or a formation-level change of the material description. Those must be audited separately rather than inserted by assumption.

## Toy control

Using dimensionless geometrized controls

\[
R=1,\quad \mu=1,\quad p_r=0.1,\quad p_t=0.5,
\quad D_Rp_r=-20,
\]

the same finite stress profile produces:

- `C=0.80`: `D_T U > 0` (turnaround acceleration possible),
- `C=0.95`: `D_T U < 0`,
- `C=0.99`: `D_T U < 0`,
- `C=1.00`: hydrodynamic contribution is suppressed and `D_T U < 0`,
- `C=1.20`: `U=0` is kinematically inadmissible because `Gamma^2<0`.

This is a control witness only; it is not a black-hole-core EOS or a prediction.

## DSD interpretation boundary

The result is standard GR provenance, not an R0/R1 DSD derivation. It nevertheless provides a useful external gate for the active DSD gravity research:

\[
\text{finite 3D support during collapse}
\neq
\text{finite 3D support at a trapped turning point}.
\]

BH-RB-009 showed that finite-radius 3D matter can exist *while continuing to collapse* inside a trapped region. BH-RB-011 shows that a regular areal-radius stop/bounce of the same spherical timelike material shell requires the shell to be marginal or untrapped at that event.

No spatial-dimension downgrade is invoked anywhere in this argument.

## Verdict

\[
\boxed{
\text{PASS\_WITH\_BOUNDARY /}
\text{TURNING\_POINT\_REQUIRES\_NONTRAPPED\_OR\_MARGINAL\_STATE /}
\text{FINITE\_CORE\_NOT\_DERIVED}
}
\]

The next audit should test the remaining escape mechanisms one by one: mass loss / outward flux, radial tension (`p_r<0`), dissipative terms, and formation-level replacement of the original constituent fluid by a successor stress-energy structure. The first question is whether any of these can lower `2m/R` to `<=1` before `R` reaches zero while satisfying selected energy and causality conditions.

## Reproducibility

From repository root:

```powershell
python audits/science/2026-09-14_dsd_gravity_finite_core_turning_point_gate.py --mode all
```

Expected audit result: **10/10 PASS**.

## External standard-GR references

1. Misner, C. W. & Sharp, D. H. (1964), *Relativistic Equations for Adiabatic, Spherically Symmetric Gravitational Collapse*, Physical Review 136, B571. DOI: 10.1103/PhysRev.136.B571.
2. Musco et al. review of spherically symmetric relativistic hydrodynamics and the Misner–Sharp constraint, *Universe* 8, 66 (2022).
3. Herrera, L. et al. (2004), *Spherically symmetric dissipative anisotropic fluids: A general study*, Physical Review D 69, 084026. DOI: 10.1103/PhysRevD.69.084026.
