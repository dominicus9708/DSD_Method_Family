# BH-RB-012 — Rotating Successor-Core Scale / Anisotropy Gate

Date: 2026-09-14

Status:

`PASS_WITH_BOUNDARY / ROTATION_SCALE_IDENTIFIED / POLAR_SUPPORT_STILL_REQUIRED / FINITE_CORE_NOT_DERIVED`

## 1. Purpose

Open the `J != 0` branch of the restarted DSD gravity program without assuming that rotation automatically produces a finite black-hole core.

This audit also separates three notions that must not be conflated:

- spatial / flow anisotropy produced by axisymmetric rotation,
- material stress anisotropy,
- directional transport anisotropy in the surrounding accretion flow.

The discarded structural-gravity branch is not reused.

## 2. Provenance firewall

The Kerr formulas and rotating-fluid comparisons are external standard GR / relativistic-fluid inputs. They are not claimed to be derived from generic DSD.

A rotating object can be stationary and axisymmetric while its matter is still modeled as a perfect fluid in the comoving frame. Therefore

`spatial/flow anisotropy != stress anisotropy`.

If the successor-core matter itself has anisotropic stresses, a separate constitutive closure is still required.

## 3. Kerr external comparator

Define

```text
r_g = GM/c^2
chi = J c / (G M^2)
r_+ = r_g [1 + sqrt(1-chi^2)]
```

for `0 <= chi <= 1`.

The black-hole mean specific angular momentum is

```text
j_BH = J/M = chi r_g c.
```

Two diagnostic length scales follow:

```text
r_j    = j_BH/c = chi r_g
r_circ = j_BH^2/(GM) = chi^2 r_g.
```

`r_circ` is only a Newtonian circularization control. It is not a relativistic interior equilibrium radius.

## 4. Horizon comparison

The ratio obeys

```text
r_circ/r_+
= chi^2 / [1 + sqrt(1-chi^2)]
= 1 - sqrt(1-chi^2)
<= 1.
```

Also

```text
r_j/r_+
= chi / [1 + sqrt(1-chi^2)]
<= 1.
```

Hence the simple scale built from the central object's *mean* specific angular momentum does not automatically generate an equilibrium radius outside the Kerr horizon. Equality is reached only in the extremal `chi=1` limit.

This does **not** prove that rotation is dynamically unimportant. It only blocks the shortcut

```text
nonzero J -> centrifugal support outside horizon.
```

## 5. Sgr A* scale control

Using the independently reintroduced mass benchmark

```text
M = 4.297e6 M_sun
r_g ~= 6.3452497e6 km,
```

for `chi=0.9`:

```text
r_+      ~= 1.4358899 r_g ~= 9.11108e6 km
r_circ   =  0.81 r_g      ~= 5.13965e6 km
r_circ/r_+ ~= 0.5641101.
```

Thus the mean-spin circularization control is substantial but remains sub-horizon in scale for this example.

## 6. Directional rotation control

For a nearly spherical weak-field shell, use the diagnostic

```text
q = Omega^2 R^3/(GM)
f_rot(theta) ~ q sin^2(theta).
```

This is a Newtonian directional control, not a GR interior field equation.

It immediately gives

```text
f_rot(0) = 0
```

on the rotation axis and the maximum at the equator.

For `chi=0.9` and the ring-like mean-angular-momentum control evaluated at `R=r_+`, one obtains

```text
q_equator ~= 0.5641101.
```

Representative directional values are

```text
theta = 0 deg   -> 0
theta = 45 deg  -> 0.2820551
theta = 90 deg  -> 0.5641101.
```

Therefore rotation alone cannot provide support in the polar direction. Any finite three-dimensional successor core must have a non-rotational polar support mechanism: stress, magnetic field, additional field content, or continuing dynamics.

## 7. External accretion circularization gate

For accreting matter define

```text
ell = j_acc/(r_g c).
```

The same simple circularization control gives

```text
r_circ,acc = ell^2 r_g.
```

To circularize outside the Kerr horizon,

```text
ell > sqrt(r_+/r_g)
    = sqrt[1 + sqrt(1-chi^2)].
```

For `chi=0.9`:

```text
ell > 1.1982862.
```

Accreting gas can have a specific angular momentum larger than the central black hole's mean `J/M`. Therefore an accretion disk is naturally interpreted as an external angular-momentum / circularization barrier, not as evidence that ordinary spatial volume has literally been filled up.

## 8. Jet / polar-funnel firewall

Standard GRMHD simulations and reviews show flows separated into disk, corona/wind and highly magnetized polar-funnel regions, with Poynting-flux-dominated jets possible in the polar region, especially for rotating black holes.

This is compatible with the directional asymmetry identified above, but it does not establish

```text
finite successor core -> jet.
```

Jet launching remains an external Kerr+GRMHD benchmark. The safe link is only

```text
rotation -> axial geometry / directional transport differences,
```

with the detailed jet mechanism supplied by external MHD and electromagnetic physics.

## 9. Audit checks

The Python audit verifies:

1. the Kerr/rotation ratio identity,
2. `r_circ <= r_+` over `0 <= chi <= 1`,
3. `r_j <= r_+` over the same range,
4. extremal equality,
5. zero rotational support on the axis in the directional control,
6. maximum at the equator,
7. the external circularization threshold from above,
8. the same threshold from below,
9. sub-unity `q` for `chi=0.9` at `R=r_+`,
10. zero polar support there,
11. the spinless limit,
12. the nonzero-spin length-scale gate.

Result: **12/12 PASS**.

## 10. Verdict

```text
PASS_WITH_BOUNDARY /
ROTATION_SCALE_IDENTIFIED /
POLAR_SUPPORT_STILL_REQUIRED /
FINITE_CORE_NOT_DERIVED
```

The `J != 0` branch remains open, but rotation alone does not yet produce a self-consistent finite successor core. In particular, polar support remains missing.

## 11. Next audit

BH-RB-013 should compare two branches:

- rotating perfect-fluid / spatially axisymmetric matter,
- genuinely anisotropic successor stress with `p_r`, `p_theta`, `p_phi` and optionally magnetic support.

The goal is to determine what can close the polar support deficit without assuming the desired finite core in advance. After that, return to the outward-flux / mass-loss gate.

## 12. External references

- Paschalidis, V. & Stergioulas, N. (2017), *Rotating stars in relativity*, Living Reviews in Relativity 20, 7.
- Abramowicz, M. A. & Fragile, P. C. (2013), *Foundations of Black Hole Accretion Disk Theory*, Living Reviews in Relativity 16, 1.
- Martí, J. M. & Müller, E. (2015), *Grid-based Methods in Relativistic Hydrodynamics and Magnetohydrodynamics*, Living Reviews in Computational Astrophysics.
