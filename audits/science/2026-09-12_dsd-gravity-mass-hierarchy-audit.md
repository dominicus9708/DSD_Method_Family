# DSD Gravity Mass Hierarchy Audit — BH-RB-003

Date: 2026-09-12

Status: **PASS_WITH_BOUNDARY / GLOBAL_RELATIVISTIC_MASS_REQUIRED**

## Purpose

Continue the active QM/relativity-based DSD gravity rebaseline after BH-RB-002.

The immediate question is which notion of `mass/energy` is eligible to enter a standard-GR black-hole radius comparator. The audit deliberately separates local matter energy density, slice-integrated matter energy, symmetry/conservation charges, and global geometric mass instead of identifying them by name.

The discarded 2026-09-11 structural-gravity branch (`K_g`, `Theta_*`, `Psi_*`, normalized support pencils, target selection) is not used.

## DSD-side source constraints

The current DSD Property Axiom System retains the complete ordered typed input of every property record and places physical specialization downstream.

The channel-indexed static aggregation paper treats scalarization, contraction, constitutive interpretation, and empirical readout as later maps. Equal reduced aggregates need not reconstruct equal component-resolved states.

The Structural Reorganization Dynamics paper states that a property label does not determine a physical coefficient or quantity by name alone. A constitutive dynamic bridge is required. It also states that conservation or redistribution laws are additional model conditions rather than generic consequences of DSD typing.

Therefore no DSD scalar aggregate is promoted directly to black-hole mass.

## Mass hierarchy

### M0 — abstract DSD typed property value

A DSD property record has the abstract typed form

\[
(\varpi,x,z),
\]

with the full typed input `x` retained. Before a physical bridge, the numerical value `z` is not kilograms, joules, energy density, invariant mass, ADM mass, or a black-hole solution parameter merely because of a property label.

### M1 — local matter energy density

After an explicit relativistic matter bridge supplies a stress-energy tensor and an observer four-velocity,

\[
\varepsilon_{(u)} = T_{\mu\nu}u^\mu u^\nu.
\]

This is an observer-dependent local quantity.

For pressureless dust,

\[
T_{\mu\nu}=\rho_0 U_\mu U_\nu,
\]

so an observer with relative Lorentz factor `gamma` measures

\[
\varepsilon_{(u)}=\rho_0\gamma^2.
\]

Thus local energy density is not an observer-independent mass scalar.

### M2 — slice-integrated matter energy

A local density does not yet define a total energy. One must additionally supply a spacelike hypersurface `Sigma`, its future unit normal, induced volume element, integration domain, and observer or symmetry field.

Schematically,

\[
E^{\rm mat}_{\Sigma,\xi}
=
\int_\Sigma T_{\mu\nu}\,\xi^\mu n^\nu\,d\Sigma.
\]

Without a conservation law and suitable boundary conditions this quantity need not be independent of the chosen slice.

### M3 — conserved matter/symmetry charge

If

\[
\nabla_\mu T^{\mu\nu}=0
\]

and `xi^mu` is a suitable Killing/symmetry vector, then

\[
J^\mu=T^{\mu\nu}\xi_\nu
\]

is divergence-free and the associated charge can be conserved under appropriate boundary-flux assumptions.

This is already an external physical/relativistic specialization. It is not forced by generic DSD typing.

More importantly, a conserved matter charge is still not generically the total gravitational mass of a spacetime.

### M4 — global relativistic/gravitational mass

For asymptotically flat initial data, standard GR defines ADM energy-momentum from the asymptotic metric and extrinsic-curvature data. The ADM mass is the invariant norm of that global energy-momentum under the standard assumptions.

For stationary asymptotically flat spacetimes, the Komar mass at infinity agrees with ADM mass under the standard normalization/regularity conditions.

These are geometric/asymptotic charges. They are not obtained by simply summing local DSD property values or by integrating `T_munu` alone.

The vacuum black-hole exterior is the decisive witness: a region may have

\[
T_{\mu\nu}=0
\]

while the Schwarzschild or Kerr geometry still has nonzero global mass and, when applicable, angular momentum.

### M5 — black-hole solution parameter

Only after the standard-GR solution family and global charge identification are supplied may the relevant global mass be used as the parameter `M` in an external Schwarzschild/Kerr/Kerr-Newman comparator.

For Schwarzschild,

\[
r_H=\frac{2GM}{c^2}.
\]

The symbol `M` at this stage is not an arbitrary observer energy divided by `c^2`.

## Frame-dependence control witness

Take an isolated system of invariant mass `M` in special relativity.

An observer moving relative to its rest frame measures

\[
E=\gamma Mc^2,
\qquad
p=\gamma M\beta c.
\]

The invariant mass is recovered from the full four-momentum:

\[
M^2
=
\left(\frac{E}{c^2}\right)^2
-
\left(\frac{p}{c}\right)^2.
\]

Therefore `E/c^2` alone is not the invariant mass when `beta != 0`.

If one incorrectly inserted observer energy as the Schwarzschild mass parameter,

\[
r_H^{\rm wrong}
=
\frac{2G(E/c^2)}{c^2}
=
\gamma\frac{2GM}{c^2},
\]

the alleged horizon radius would change with observer frame. This is a category error and gives a direct rejection test for any proposed DSD bridge that maps an arbitrary energy readout directly to black-hole `M`.

## Numerical control using the existing Sgr A* benchmark mass

Using the externally supplied benchmark

\[
M=4.297\times10^6M_\odot,
\]

standard Schwarzschild comparison gives

\[
r_H\approx1.2690499\times10^7\ {\rm km}.
\]

For a deliberately hypothetical SR control boost `beta=0.6`,

\[
\gamma=1.25.
\]

If one wrongly replaced global/invariant mass by `E_observer/c^2`, one would obtain

\[
r_H^{\rm wrong}\approx1.5863124\times10^7\ {\rm km},
\]

which is 25% larger solely because the observer frame was changed.

This `beta=0.6` is **not a Sgr A* velocity measurement**. It is only a non-circular frame-dependence witness.

## Promotion gates

1. **DSD typed value -> local energy density:** requires an explicit physical interpretation, units, localization, Lorentzian metric, observer field, and stress-energy representation.
2. **Local density -> slice matter energy:** requires a supplied spacelike slice, normal, induced measure, domain, and boundary data.
3. **Slice matter energy -> conserved matter charge:** requires a supplied divergence/conservation law, symmetry such as a Killing field, and appropriate boundary-flux conditions.
4. **Conserved matter charge -> global gravitational mass:** not automatic; requires standard gravitational dynamics plus metric/extrinsic-curvature and asymptotic or other explicit global-mass structure.
5. **Global mass -> black-hole radius parameter:** requires the relevant external standard-GR solution class and its boundary/symmetry assumptions.

## Audit verdict

- raw DSD scalar -> local physical energy density by label: **FAIL**.
- local energy density -> invariant/global mass: **FAIL**.
- slice-integrated matter energy -> conserved total energy without extra law: **FAIL**.
- generic DSD typing -> `nabla_mu T^{mu nu}=0`: **FAIL**.
- conserved matter charge -> ADM/Komar mass by identity: **FAIL**.
- ADM mass without asymptotically flat/geometric initial data: **UNDEFINED**.
- Komar mass without stationary Killing structure and normalization: **UNDEFINED**.
- observer `E/c^2` -> Schwarzschild/Kerr mass parameter: **FAIL**.
- explicitly supplied global relativistic mass -> standard black-hole radius comparator: **PASS AS R3/R4 EXTERNAL SPECIALIZATION**.

Overall:

**PASS_WITH_BOUNDARY / GLOBAL_RELATIVISTIC_MASS_REQUIRED**

The mass input gate is now separated strongly enough to prevent the black-hole radius calculation from using a local DSD scalar, a static aggregate, or an arbitrary observer energy as `M`.

## Consequence for the active DSD gravity pipeline

The mass sector should now be written as

\[
\mathcal I_{\rm DSD}
\xrightarrow{B_{\rm MAT}}
T_{\mu\nu}
\xrightarrow{\text{slice/observer/symmetry specialization}}
E^{\rm mat}_{\Sigma,\xi}
\xrightarrow{\text{external GR + geometric boundary data}}
P^\mu_{\rm ADM}
\xrightarrow{\text{invariant norm}}
M_{\rm ADM}
\xrightarrow{\text{standard BH solution}}
r_H(M,J,Q,\ldots).
\]

This is a provenance chain, not a derivation of Einstein dynamics from DSD.

## External standard-GR verification used in this audit

- Living Reviews in Relativity, *Quasi-Local Energy-Momentum and Angular Momentum in General Relativity*: ADM energy-momentum requires asymptotically flat hypersurface data and is a global asymptotic charge.
- Living Reviews in Relativity, *The General Relativistic Constraint Equations*: ADM mass is defined from asymptotically flat geometric data.
- Standard GR lecture notes/reviews: observer energy density is `T_ab u^a u^b`; a conserved stress-energy tensor plus a Killing vector gives a conserved current.
- Standard stationary asymptotically flat result: Komar mass at infinity equals ADM mass under the corresponding assumptions.

## Reproduction

From the repository root:

```powershell
python audits/science/2026-09-12_dsd_gravity_mass_hierarchy_audit.py
```

Optional SR control boost:

```powershell
python audits/science/2026-09-12_dsd_gravity_mass_hierarchy_audit.py --beta 0.8
```

The `--beta` value is a control parameter for the frame-dependence witness, not an astrophysical input.

## Next step

BH-RB-004 should close the **angular-momentum sector** with the same discipline:

1. local momentum density / stress-energy information,
2. rotational symmetry or asymptotic rotational generator,
3. slice/global angular-momentum charge,
4. distinction between matter angular momentum and total spacetime angular momentum,
5. eligibility of the resulting `J` for the external Kerr/Kerr-Newman horizon comparator.

Kerr remains an external comparator, not a DSD target imposed in advance.
