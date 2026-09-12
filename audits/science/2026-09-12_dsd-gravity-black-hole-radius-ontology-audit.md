# DSD Gravity Black-Hole Radius Ontology Audit — BH-RB-001

Date: 2026-09-12

Status: PASS_WITH_BOUNDARY / RADIUS_TYPES_SEPARATED

## Scope and provenance firewall

This audit belongs to the active QM/relativity-based DSD gravity rebaseline.

It does **not** reuse the discarded 2026-09-11 structural-gravity branch based on `K_g`, `Theta_*`, `Psi_*`, normalized support pencils, target selection, or the former Sgr A* critical-radius fit.

The standard Schwarzschild/Kerr expressions below are external GR comparators. They are not claimed as generic DSD derivations.

## Radius ontology gate

At least four objects must be kept distinct:

1. **Curvature-singularity locus** — where the external GR solution becomes curvature-singular.
2. **Event-horizon radius/coordinate** — a causal boundary supplied by a relativistic specialization.
3. **Shadow/ring readout** — an observationally reconstructed image scale; not the horizon itself.
4. **DSD-native radius candidate** — remains undefined until an explicit localization/metric bridge supplies the required geometric meaning.

Therefore a finite `black-hole radius` must not automatically be called a `singularity radius`.

## Schwarzschild external comparator

For a nonrotating uncharged GR specialization,

\[
r_g=\frac{GM}{c^2},
\qquad
r_H=2r_g=\frac{2GM}{c^2}.
\]

The curvature singularity is at areal coordinate

\[
r_{\rm sing}=0,
\]

whereas the finite horizon is at `r_H`. Thus the singularity and the black-hole causal boundary are different objects.

## Sgr A* benchmark

Using the GRAVITY stellar-orbit mass

\[
M=(4.297\pm0.012_{\rm stat}\pm0.040_{\rm sys})\times10^6 M_\odot,
\]

we obtain

\[
r_g\approx 6.3452497\times10^6\ {\rm km},
\]

with statistical and quoted systematic mass-propagated uncertainties of approximately

\[
\delta r_{g,\rm stat}\approx1.7720\times10^4\ {\rm km},
\qquad
\delta r_{g,\rm sys}\approx5.9067\times10^4\ {\rm km}.
\]

The Schwarzschild horizon comparator is

\[
r_H\approx1.2690499\times10^7\ {\rm km}
\approx0.08483075\ {\rm AU},
\]

with

\[
\delta r_{H,\rm stat}\approx3.5440\times10^4\ {\rm km},
\qquad
\delta r_{H,\rm sys}\approx1.1813\times10^5\ {\rm km}.
\]

The Schwarzschild curvature-singularity areal radius remains exactly `r=0`; the finite number above is the horizon comparator, not a singularity radius.

Reference for the mass input: GRAVITY Collaboration, *Astronomy & Astrophysics* 657, L12 (2022), DOI: 10.1051/0004-6361/202142465.

## Kerr external comparator

If angular momentum survives the property-reduction bridge, define the external Kerr dimensionless spin

\[
\chi=\frac{Jc}{GM^2},
\qquad
|\chi|\le1,
\]

and

\[
a=\chi r_g.
\]

The horizon coordinates are

\[
r_\pm=r_g\left(1\pm\sqrt{1-\chi^2}\right).
\]

The Kerr curvature singularity is the ring locus

\[
\Sigma=r^2+a^2\cos^2\theta=0
\quad\Longrightarrow\quad
r=0,\;\theta=\frac\pi2.
\]

The parameter `|a|` may be represented as the coordinate-ring parameter in Kerr-Schild-type descriptions, but it must not be relabeled as a regular proper-radius observable at the singularity.

For the Sgr A* mass above, a parameter scan gives:

| chi | |a| (km) | r_+ (km) |
|---:|---:|---:|
| 0.00 | 0 | 12,690,499 |
| 0.10 | 634,525 | 12,658,693 |
| 0.50 | 3,172,625 | 11,840,397 |
| 0.90 | 5,710,725 | 9,111,080 |
| 0.99 | 6,281,797 | 7,240,357 |
| 1.00 | 6,345,250 | 6,345,250 |

This table is a parameter scan, not a measurement of the Sgr A* spin.

## DSD consequence

The active DSD gravity line cannot yet assign a native black-hole radius because the rebaseline explicitly forbids identifying an arbitrary DSD distance/readout with Schwarzschild or Boyer-Lindquist radius.

The radius problem therefore factorizes into two separate bridge problems:

\[
\mathcal I_{\rm DSD}
\longrightarrow
(M,J,Q,\ldots)_{\rm physical}
\]

and

\[
\mathcal I_{\rm DSD}+B_{\rm REL}
\longrightarrow
\text{relativistic localization/metric structure}
\longrightarrow
\{\mathcal S_{\rm sing},\mathcal H,\text{readouts}\}.
\]

A scalar radius is allowed only after the target object is specified. In particular, the curvature-singularity set need not admit a single nonzero scalar radius.

## Audit result

- `singularity radius = horizon radius`: **FAIL / category error**.
- Schwarzschild curvature singularity at `r=0`: **PASS as external GR comparator**.
- Schwarzschild finite horizon `r_H=2GM/c^2`: **PASS as external GR comparator**.
- Kerr ring singularity represented by a single ordinary proper radius: **FAIL**.
- DSD-native horizon/singularity radius before localization/metric bridge: **UNDEFINED**.
- Reuse of the discarded `K_g/Theta/Psi` critical-radius law: **PROHIBITED**.

## Next active step

Proceed from the current rebaseline target: audit the typed-property / matter bridge that can legitimately supply mass-energy-momentum-stress data, and separately identify which records can supply angular momentum or charge. Only after that bridge is explicit should the external Schwarzschild/Kerr/Kerr-Newman radius relations be used as comparison consequences.

Reproduction script:

`audits/science/2026-09-12_dsd_gravity_black_hole_radius_ontology_audit.py`
