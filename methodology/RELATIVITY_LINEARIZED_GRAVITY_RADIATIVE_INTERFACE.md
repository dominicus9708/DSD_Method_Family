# Relativity Linearized-Gravity / Radiative Interface

Status: **REL Core 006 — PASS_WITH_BOUNDARY**

## Purpose

Use this interface whenever DSD analysis handles weak-field metric perturbations, gravitational waves, gauge-fixed perturbation variables, TT polarizations, or comparisons between relativistic propagation and DSD structural-information propagation.

The interface prevents the following silent identifications:

```text
metric perturbation == physical radiation
gauge condition == physical law
TT representative == unique physical representation
linearized-GR wave speed == generic DSD c_info
```

## Required provenance

```text
R0  PRE_EXISTING_DSD
R1  GENERAL_MATHEMATICAL_STRUCTURAL
R2  RELATIVITY_SPECIALIZATION
R3  STANDARD_THEOREM_CONSEQUENCE
R4  REMAINS_EXTERNAL_NOT_DERIVED
```

Typical R2 supply:

```text
Minkowski background eta
four spacetime dimensions
weak-field split g = eta + h
first-order truncation
standard infinitesimal diffeomorphism rule
linearized Einstein equation
source/vacuum choice
```

Typical R3 consequences:

```text
trace reversal
de Donder/Lorenz form
residual gauge freedom
vacuum wave equation
null plane-wave dispersion
TT reduction
two radiative polarizations
linearized Riemann/tidal response
```

## Weak-field split firewall

Always declare the supplied background:

\[
g_{\mu\nu}=g^{(0)}_{\mu\nu}+h_{\mu\nu}.
\]

For REL Core 006,

\[
g^{(0)}_{\mu\nu}=\eta_{\mu\nu}.
\]

Do not treat the background/perturbation split as a generic DSD identity decomposition.

## Gauge firewall

For a standard infinitesimal diffeomorphism around Minkowski,

\[
h_{\mu\nu}
\mapsto
h_{\mu\nu}
+
\partial_\mu\xi_\nu
+
\partial_\nu\xi_\mu
\]

up to coordinate-sign convention.

Required distinction:

```text
nonzero h != nonzero gauge-invariant radiation
```

Pure-gauge perturbations may have \(h\neq0\) with

\[
R^{(1)}_{\alpha\beta\gamma\delta}=0.
\]

## Trace-reversal gate

Use

\[
\bar h_{\mu\nu}
=
h_{\mu\nu}
-\frac12\eta_{\mu\nu}h.
\]

In four spacetime dimensions:

\[
\bar{\bar h}=h,
\qquad
\bar h^\mu{}_{\mu}=-h.
\]

Do not transfer this exact involution formula unchanged to arbitrary dimension without checking the dimension-dependent trace-reversal convention.

## de Donder/Lorenz gate

Declare the gauge condition explicitly:

\[
\partial^\mu\bar h_{\mu\nu}=0.
\]

Residual gauge freedom remains when

\[
\Box\xi_\nu=0.
\]

Therefore:

```text
de Donder gauge fixed != all gauge freedom exhausted
```

## Radiative-degree gate

For a nonzero null plane wave in 4D linearized GR:

```text
10 symmetric components
-4 de Donder constraints
-4 residual gauge directions
=2 radiative degrees of freedom
```

A standard TT representative for propagation along \(z\) retains the \(+\) and \(\times\) polarizations.

Do not infer that "two channels" in a generic DSD model are gravitational-wave polarizations.

## Propagation-speed gate

The standard vacuum equation is

\[
\Box\bar h_{\mu\nu}=0.
\]

With physical \(c\) retained explicitly, nonzero plane waves satisfy

\[
-\frac{\omega^2}{c^2}+|\mathbf{k}|^2=0,
\]

hence

\[
v_{\rm phase}=v_{\rm group}=c
\]

for this nondispersive standard linearized-GR vacuum sector.

Mandatory firewall:

\[
\boxed{
v_{\rm GW}=c
\not\Rightarrow
c_{\rm info}=c.
}
\]

DSD \(c_{\rm info}\) is defined only relative to a supplied localization/metric-time/evolution/discrepancy structure.

## Tidal-response gate

In TT gauge and the REL Core 006 sign convention,

\[
R^{(1)}_{i0j0}
=
-\frac12\ddot h^{TT}_{ij}.
\]

Physical detector response should be tied to curvature/geodesic-deviation or another explicitly gauge-controlled observable, not to one coordinate component by name alone.

Required distinction:

```text
coordinate position of test mass
!=
proper separation / tidal response
```

## Flat-background qualification

The first-order Riemann tensor is gauge invariant under pure-gauge perturbations in this gate because the background Riemann tensor is zero.

Do not generalize this without qualification to a curved background. For a generic background tensor \(Q^{(0)}\), first-order gauge shifts involve the Lie derivative \(\mathcal L_\xi Q^{(0)}\).

## DSD role mapping

```text
Formation:
  identity of model/background/perturbative regime

Property:
  typed metric, perturbation, gauge-status, source-status,
  wavevector and curvature records

Static Aggregation:
  optional reduced waveform/readout summaries;
  equality need not reconstruct full perturbation or gauge orbit

Dynamics:
  component-resolved evolution under supplied operators;
  generic c_info remains separately defined

Relativity specialization:
  linearized Einstein operator, gauge structure,
  null gravitational-wave characteristics, TT/tidal formulas
```

## Mandatory non-identifications

```text
h != physical radiation by itself
gauge-fixed h != unique physical field representation
de Donder gauge != no remaining gauge freedom
TT gauge != new dynamical law
two TT polarizations != generic DSD two-channel structure
GW speed c != generic DSD c_info
linearized GR != full nonlinear GR
one waveform != unique physical source history
```

## Reconstruction checklist

Before asserting a linearized gravitational-wave result, retain at least:

```text
background metric
perturbative-order convention
gauge transformation convention
gauge condition if used
source/vacuum status
field equation
wavevector/solution class
observable or curvature quantity used for physical interpretation
```

Before comparing with DSD propagation, additionally retain:

```text
DSD localization carrier
propagation metric
metric-time scale
discrepancy convention
component support/readout relation
evolution operator or constitutive bridge
support-faithfulness / propagation-completeness assumptions
```

If those data are absent, report the comparison as not established.

## Claim template

Preferred:

> Given the standard four-dimensional Minkowski weak-field specialization and the linearized Einstein equation, de Donder gauge yields a vacuum massless wave equation whose plane-wave sector has null characteristics and two TT radiative polarizations; this standard-GR result may be represented and audited through DSD without identifying its light-cone speed with generic DSD \(c_{\rm info}\).

Do not write:

> DSD derives gravitational waves at \(c\).

unless both the Einstein-type dynamics and the identification of the DSD propagation structure with the relativistic light cone have been independently established.

## Current closure

```text
trace-reversal identities checked: YES
de Donder residual gauge retained: YES
10-4-4 two-DOF quotient checked: YES
null vacuum dispersion checked with explicit c: YES
pure-gauge flat-background R^(1)=0 checked: YES
plus/cross tidal response checked: YES
generic c_info=c derived: NO
full nonlinear GR derived: NO
DSD core revision required: NO
```

Next gate:

```text
REL Core 007 — Horizon / Coordinate-Singularity / Curvature-Singularity / Causal-Boundary Gate
```
