# DSD Gravity Charge Hierarchy Audit — BH-RB-005

Date: 2026-09-13

Status: **PASS_WITH_BOUNDARY / GLOBAL_GAUGE_CHARGE_REQUIRED**

## Purpose

Continue the active QM/relativity-based DSD gravity rebaseline after BH-RB-004.

BH-RB-003 separated the mass hierarchy, and BH-RB-004 separated the angular-momentum hierarchy. The present step closes the charge sector without identifying a DSD value named `charge`, a local charge density, a matter-current integral, an electromagnetic flux charge, and the black-hole solution parameter by definition.

The discarded structural-gravity branch (`K_g`, `Theta_*`, `Psi_*`, support-threshold/spectral-target constructions) is not used.

## DSD-side constraints inherited from the current papers

The current general Property Axiom System keeps undeclared, inapplicable, prerequisite-unsatisfied, applicable-but-undefined, defined-zero, and defined-nonzero statuses distinct. A defined property record retains the property kind, the complete ordered typed input, and the assigned value.

The static aggregation layer allows selected typed property data to be mapped through an explicit downstream bridge, but property kinds, units, input sorts, and physical interpretations are not fixed by the abstract property system. Multi-input data are not reassigned to one channel unless an application explicitly supplies such an association.

The dynamics layer likewise does not permit undefined data to be padded with zero without retaining the lost status information, and physical constitutive laws or conservation rules are downstream model conditions.

Therefore:

\[
\boxed{\text{undefined charge-like DSD status} \neq \text{physical neutral charge }Q=0}
\]

and a property label `charge` does not itself establish an electric/gauge charge.

## Charge hierarchy

Use the following separation:

\[
Q0\to Q1\to Q2\to Q3\to Q4\to Q5.
\]

### Q0 — DSD typed property / channel record

This is a DSD-native typed record with its status, complete typed input profile, and abstract value.

At this layer there is no automatic Coulomb unit, gauge group, electromagnetic field, spacetime localization, conserved current, orientation, integration measure, or black-hole charge meaning.

### Q1 — local physical charge density/current

After an explicit physical/gauge bridge, selected records may receive a local current interpretation

\[
j^\mu(x)
\]

or an observer/slice-dependent charge density.

This is already an R2/R4 specialization. It requires physical units, localization, a spacetime carrier, and a declared gauge/matter interpretation.

### Q2 — slice matter charge

On a supplied spacelike hypersurface \(\Sigma\), one may define a matter charge schematically by

\[
Q_{\Sigma}^{\rm matter}
=
\int_\Sigma j^\mu\,d\Sigma_\mu,
\]

with the sign convention determined by the chosen metric/orientation convention.

The local current or density does not determine this integral without a domain, measure/volume element, normal/orientation, and localization.

### Q3 — conserved gauge charge sector

A slice charge becomes a conserved charge only when the external physical model supplies the relevant conservation law, for example

\[
\nabla_\mu j^\mu=0,
\]

together with the required boundary-flux conditions.

This conservation is not produced by DSD typing alone.

### Q4 — Gauss/asymptotic electromagnetic charge

In four-dimensional Einstein-Maxwell theory, the electric charge of an asymptotically flat end can be represented, up to the convention-dependent normalization, by a flux integral at spatial infinity,

\[
Q_{\infty}\propto
\int_{S_\infty^2}\star F.
\]

For the common geometric-unit normalization used in the black-hole literature,

\[
Q_e=\frac{1}{4\pi}\int_{S_\infty^2}\star F.
\]

This is a boundary/global gauge charge. It can remain nonzero in a vacuum exterior where the local matter current vanishes.

### Q5 — black-hole comparator charge parameter

Only after a valid global physical electric charge has been obtained may it be normalized for the external Kerr-Newman comparator.

In SI-compatible notation define

\[
\hat q
=
\frac{Q_{\rm phys}}
{\sqrt{4\pi\varepsilon_0G}\,M}.
\]

Together with

\[
\chi=\frac{Jc}{GM^2},
\qquad
r_g=\frac{GM}{c^2},
\]

the external Kerr-Newman outer horizon is

\[
r_+
=
r_g
\left(
1+\sqrt{1-\chi^2-\hat q^2}
\right),
\]

subject to

\[
\chi^2+\hat q^2\le1.
\]

This is an R3/R4 standard-GR/electromagnetic comparator, not a DSD-native law.

## Density/domain witness

Take the same uniform externally interpreted charge density

\[
\rho=1
\]

on two domains of volumes

\[
V_A=1,\qquad V_B=2.
\]

Then

\[
Q_A=\rho V_A=1,
\qquad
Q_B=\rho V_B=2.
\]

Therefore

\[
\boxed{\rho\ \text{alone does not determine}\ Q.}
\]

The integration domain and measure are required.

## Vacuum-exterior Gauss witness

Consider a nonzero enclosed test charge \(Q=1\,{\rm C}\) and a spherical surface at \(r=2\,{\rm m}\) in an otherwise vacuum exterior.

The local exterior source density is

\[
\rho_{\rm ext}=0,
\]

while the Coulomb field on the sphere is

\[
E(r)=\frac{Q}{4\pi\varepsilon_0r^2}.
\]

Hence

\[
\varepsilon_0
\int_{S^2} \mathbf E\cdot d\mathbf A
=
\varepsilon_0 E(r)\,4\pi r^2
=
Q
=
1\,{\rm C}.
\]

Thus

\[
\boxed{
j^\mu_{\rm local}=0\ \text{in a vacuum exterior}
\not\Rightarrow
Q_\infty=0.
}
\]

This is the charge-sector analogue of the BH-RB-003/004 separation between local matter data and global relativistic charges.

## Undefined is not neutral

A missing or undefined charge-like DSD record cannot be replaced by

\[
Q=0.
\]

Doing so would collapse the Property Axiom System's explicit distinction between undefined and defined zero.

Therefore a Kerr comparator cannot be selected merely because no charge bridge has yet been supplied. The neutral specialization must itself be established as

\[
Q_{\rm phys}=0
\]

or introduced as an explicit external model assumption.

## Horizon-radius sign-loss witness

For fixed \(M\) and \(J\),

\[
r_+(\hat q)
=
r_+(-\hat q)
\]

because the horizon equation depends on \(\hat q^2\).

Therefore

\[
\boxed{
r_+\ \text{does not reconstruct the sign of}\ Q.
}
\]

The radius is consequently a reduced readout of the full charge state, consistent with the general DSD warning that aggregate equality need not reconstruct the underlying typed support.

## Fully supplied M/J/Q comparator control

Using the active Sgr A* mass benchmark only as an external mass input,

\[
M=4.297\times10^6M_\odot,
\]

gives

\[
r_g\approx6.3452497\times10^6\ {\rm km}.
\]

For the purely illustrative parameter-control values

\[
\chi=0.9,
\qquad
\hat q=0.3,
\]

we have

\[
\chi^2+\hat q^2=0.90<1,
\]

and therefore

\[
r_+
=
r_g\left(1+\sqrt{0.10}\right)
\approx
8.3517938\times10^6\ {\rm km}.
\]

Neither \(\chi=0.9\) nor \(\hat q=0.3\) is asserted to be a Sgr A* measurement. They are only control parameters used to verify that the now-separated \(M,J,Q\) inputs enter the standard external comparator consistently.

The corresponding SI charge magnitude for \(|\hat q|=0.3\) is very large and is printed by the reproduction script only as a unit-conversion control. It is not an astrophysical claim.

## Audit result

The reproduction script passes 7/7 checks:

1. undefined charge-like DSD status is not silently converted to physical zero;
2. the physical bridge retains the complete typed input profile;
3. local charge density alone does not determine total charge without domain and measure;
4. zero local exterior source density does not force zero enclosed/asymptotic charge;
5. DSD typing alone does not enforce charge conservation;
6. Kerr-Newman horizon radius loses the sign of charge;
7. once global \(M,J,Q\) are supplied externally and satisfy the horizon-existence condition, the Kerr-Newman comparator is well defined.

## Verdict

- raw DSD property value by the label `charge` -> physical electric charge: **FAIL**.
- undefined DSD charge status -> physical \(Q=0\): **FAIL**.
- local density/current -> global charge without domain/measure/conservation: **FAIL**.
- generic DSD typing -> charge conservation: **FAIL**.
- vacuum local current \(j^\mu=0\) -> global charge \(Q=0\): **FAIL**.
- explicit Maxwell/gauge sector + conserved current + boundary/asymptotic flux construction -> global physical charge: **REQUIRED**.
- global \(M,J,Q\) -> Kerr-Newman comparator: **PASS WITH EXTERNAL PROVENANCE**.
- horizon radius -> sign of \(Q\): **FAIL / INFORMATION LOSS**.

Final status:

\[
\boxed{
\text{PASS\_WITH\_BOUNDARY / GLOBAL\_GAUGE\_CHARGE\_REQUIRED}
}
\]

## External standard references

- Kunduri, H. K. & Lucietti, J., *Classification of near-horizon geometries of extremal black holes*, Living Reviews in Relativity **16**, 8 (2013). In four-dimensional Einstein-Maxwell theory it gives electric charge as a flux integral at spatial infinity.
- Standard curved-spacetime Maxwell notes use \(d\star F\propto\star j\) and Stokes' theorem to connect hypersurface charge to boundary flux. This is used here only as an external electromagnetic comparator structure.

## Next step

BH-RB-006 should integrate the three independently audited global charge sectors and audit **black-hole comparator-family selection** without collapsing undefined values to zero:

\[
(M,J,Q)
\longrightarrow
\begin{cases}
\text{Schwarzschild}, & J=0,\ Q=0,\\
\text{Kerr}, & J\neq0,\ Q=0,\\
\text{Reissner--Nordström}, & J=0,\ Q\neq0,\\
\text{Kerr--Newman}, & J\neq0,\ Q\neq0.
\end{cases}
\]

The key gate is that `undefined`, `not bridged`, and `defined zero` must remain distinct when selecting the external comparator family.

Reproduction script:

`audits/science/2026-09-13_dsd_gravity_charge_hierarchy_audit.py`
