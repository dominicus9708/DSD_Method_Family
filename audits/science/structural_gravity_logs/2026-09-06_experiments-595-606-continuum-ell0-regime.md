# DSD Gravity Research Log — Experiments 595–606

Date: 2026-09-06
Status: continuum audit of the reciprocal/common-action `ell_A=0` radial branch and correction of small-ell finite-grid interpretation

Historical repository path retains `structural_gravity_logs` for continuity. Current research name: DSD Gravity / Gravity in Dimensional-Structural Describability.

## Experiment 595 — Exact continuum elimination at `ell_A=0`

For the reciprocal/common-action branch,

\[
a=2\beta_A\chi_A e^{-2\beta_Aa/3}U_s^2.
\]

Define

\[
z=\frac{2\beta_Aa}{3},
\qquad
A=\frac{4\beta_A^2\chi_A}{3}.
\]

Then

\[
z e^z=A U_s^2,
\]

so on the principal local branch

\[
\boxed{
z=W(AU_s^2),
\qquad
a=\frac{3}{2\beta_A}W(AU_s^2).
}
\]

This removes the axis variable pointwise without a radial grid.

### Verdict

The `ell_A=0` reciprocal branch admits an exact Lambert-W reduction. Finite-grid continuation is therefore not required to define its continuum local constitutive law.

---

## Experiment 596 — Continuum radial shooting formulation

Let

\[
q=pU_s,
\qquad
p=e^{-z},
\qquad
w=-q\ge0.
\]

Using

\[
q^2=\frac{z e^{-z}}{A},
\]

the uniform-sphere field equation becomes

\[
U_s=-\sqrt{\frac{ze^z}{A}},
\]

\[
w_s+\frac{2w}{s}=\frac{3\epsilon}{2}U.
\]

The exterior normalization is

\[
\boxed{U(1)-w(1)=1.}
\]

The branch is parameterized by the boundary axis amplitude `a_b`. For a supplied `a_b`,

\[
z_b=\frac{2\beta_Aa_b}{3},
\qquad
w_b^2=\frac{z_be^{-z_b}}{A},
\qquad
U_b=1+w_b.
\]

Shooting solves for `U(0)` and `epsilon` directly in the continuum.

### Verdict

This supplies an independent continuum control for the finite-difference pseudo-arclength calculations.

---

## Experiment 597 — Small-ell finite-grid boundary is strongly resolution-sensitive

At

\[
(\chi_A,\ell_A)=(0.5,0),
\]

the finite-grid fold/saturation collision inferred from `a_max(fold)=1` shifts upward as resolution increases:

| radial grid N | beta_FS* |
|---:|---:|
| 41 | 1.28330390 |
| 61 | 1.33293106 |
| 81 | 1.36283083 |
| 101 | 1.38327634 |

A log-log fit of the deficit `1.5-beta_FS*` against grid spacing gives an effective pre-asymptotic exponent of about `0.67`; this is a diagnostic only, not an error theorem.

### Verdict

The earlier coarse-grid `ell_A -> 0` boundary must not be interpreted as a continuum value. The small-stiffness map requires continuum or dedicated convergence control.

---

## Experiment 598 — `chi_A=0.5`: continuum branch reaches the exact local boundary

For `chi_A=0.5`, continuum shooting finds

\[
\frac{d\epsilon}{da_b}\bigg|_{a_b=1}>0
\]

through the tested range `beta_A<1.5`, with the derivative tending to zero as `beta_A -> 1.5^-`.

At

\[
\boxed{\beta_A=\frac32,\quad a_b=1,}
\]

the continuum endpoint is

\[
\boxed{\epsilon\simeq0.5946598244,}
\]

\[
U(0)\simeq1.864244598.
\]

### Verdict

For this tested `chi_A=0.5`, `ell_A=0` uniform-sphere branch, no pre-saturation global fold was found before the exact local constitutive degeneracy at `beta_A=3/2`.

This is a specialization result, not a universal DSD constant.

---

## Experiment 599 — Local constitutive boundary remains exactly `beta_A=3/2`

The reduced flux derivative is

\[
\frac{dq}{dU_s}
=e^{-z}\frac{1-z}{1+z}.
\]

Hence local monotonicity is lost at

\[
z=1.
\]

Because

\[
z=\frac{2\beta_Aa}{3},
\]

the local fold amplitude is

\[
\boxed{a_{\rm fold}^{\rm local}=\frac{3}{2\beta_A}.}
\]

The local fold reaches the admissibility wall `a=1` at

\[
\boxed{\beta_A=\frac32.}
\]

### Verdict

`beta_A=3/2` is an exact local constitutive fold/saturation boundary of the reciprocal `ell_A=0` specialization. It need not equal the global coupled fold boundary.

---

## Experiment 600 — Global fold can precede the local `3/2` boundary

For smaller susceptibility, continuum shooting shows a zero of

\[
\frac{d\epsilon}{da_b}\bigg|_{a_b=1}
\]

at `beta_A<1.5`.

For

\[
\chi_A=0.25,
\]

the first global fold/saturation collision is

\[
\boxed{\beta_{\rm global}^*\simeq1.36452460,}
\]

with

\[
\boxed{\epsilon^*\simeq0.754288144.}
\]

### Verdict

A global branch fold may occur while the local flux law is still monotone. Therefore

\[
\boxed{\text{global Schur/fold boundary}\ne\text{local constitutive fold boundary}.}
\]

---

## Experiment 601 — Continuum boundary sample: `chi_A=0.20`

For

\[
\chi_A=0.20,
\]

the continuum shooting control gives

\[
\boxed{\beta_{\rm global}^*\simeq1.23512744,}
\]

\[
\boxed{\epsilon^*\simeq0.830802187.}
\]

---

## Experiment 602 — Continuum boundary sample: `chi_A=0.15`

For

\[
\chi_A=0.15,
\]

the continuum shooting control gives

\[
\boxed{\beta_{\rm global}^*\simeq1.08431893,}
\]

\[
\boxed{\epsilon^*\simeq0.927412019.}
\]

---

## Experiment 603 — Continuum boundary sample: `chi_A=0.28`

For

\[
\chi_A=0.28,
\]

the first global collision is approximately

\[
\boxed{\beta_{\rm global}^*\simeq1.43474738,}
\]

\[
\boxed{\epsilon^*\simeq0.715327556.}
\]

---

## Experiment 604 — Continuum boundary sample: `chi_A=0.30`

For

\[
\chi_A=0.30,
\]

the first global collision is approximately

\[
\boxed{\beta_{\rm global}^*\simeq1.47861027,}
\]

\[
\boxed{\epsilon^*\simeq0.691783772.}
\]

The global boundary is now very close to, but still below, the exact local `3/2` boundary.

---

## Experiment 605 — Transition to the local-limited regime occurs near `chi_A ~ 0.30–0.31`

A near-boundary control at `beta_A=1.49` gives opposite signs:

- `chi_A=0.30`: `d epsilon / d a_b |_(a_b=1) < 0`;
- `chi_A=0.31`: `d epsilon / d a_b |_(a_b=1) > 0`.

### Verdict

The present shooting control places the takeover from a pre-saturation global fold to the local `beta_A=3/2` limit near `chi_A ~ 0.30–0.31`.

No sharp critical `chi_A` is claimed yet because the derivative becomes degenerate as `beta_A -> 3/2` and requires a dedicated asymptotic expansion.

---

## Experiment 606 — Revised `ell_A=0` regime logic

The surviving continuum logic is now:

\[
\boxed{
\beta_{FS}^{(\ell=0)}(\chi_A)
=
\begin{cases}
\beta_{\rm global}^*(\chi_A), & \text{if a global fold reaches }a_b=1\text{ first},\\
3/2, & \text{otherwise through the tested local branch}.
\end{cases}}
\]

Thus `3/2` is an exact **local cap/boundary**, while the actual global fold-first/saturation-first transition can lie below it and depends on `chi_A`.

The earlier finite-grid small-`ell_A` map remains useful as a qualitative control, but its numerical boundary values near `ell_A=0` are resolution-sensitive and must not be extrapolated without continuum verification.

## Consolidated verdict

The reciprocal/common-action branch survives the continuum `ell_A=0` audit, but the regime structure is more precise than the previous grid map suggested:

\[
\boxed{
\text{local constitutive degeneracy}
\quad/\quad
\text{global branch fold}
\quad/\quad
\text{axis admissibility saturation}
}
\]

are distinct boundaries.

For `chi_A=0.5`, the tested continuum branch is saturation-first up to the exact local boundary `beta_A=3/2`. For smaller `chi_A`, a global fold can precede that local boundary.

## Reproducibility

Added:

`audits/science/structural_gravity_logs/2026-09-06_local_continuum_ell0_boundary.py`

Examples from the repository root:

```bash
python audits/science/structural_gravity_logs/2026-09-06_local_continuum_ell0_boundary.py --mode endpoint --beta 1.5 --chi 0.5 --a 1
```

```bash
python audits/science/structural_gravity_logs/2026-09-06_local_continuum_ell0_boundary.py --mode boundary --chi 0.25 --beta-lo 1.35 --beta-hi 1.40
```

```bash
python audits/science/structural_gravity_logs/2026-09-06_local_continuum_ell0_boundary.py --mode local --beta 2.0 --chi 0.5
```

## Next audit target

1. derive the asymptotic expansion near `(beta_A,a_b)=(3/2,1)` and determine whether the `chi_A ~ 0.30–0.31` crossover has a well-defined continuum critical value;
2. replace small nonzero `ell_A` finite differences with a continuum two-field boundary-value solver and recompute the `beta_FS(chi_A,ell_A)` surface;
3. only after that surface is stable, add `mu_A` and damping for time-dependent hysteresis/overshoot calculations.
