# REL Core 006 — Linearized Gravity / Gauge Perturbation / Radiative-Degree Gate

Date: 2026-09-10  
Status: **PASS_WITH_BOUNDARY**  
Program: **Core-Theory Reconstruction Challenge — Standard Relativity Track**

## 1. Purpose

REL Core 005 separated passive coordinate change, active diffeomorphism, isometry, GR gauge equivalence, and DSD strict descriptive equivalence.

REL Core 006 audits the weak-field radiative layer:

```text
supplied Minkowski background
-> weak-field split g = eta + h
-> infinitesimal diffeomorphism gauge freedom
-> trace reversal
-> de Donder/Lorenz gauge
-> residual gauge freedom
-> supplied linearized Einstein equation
-> vacuum wave equation
-> null dispersion
-> TT specialization
-> two radiative polarizations
-> linearized Riemann / tidal response
```

The central firewall is

\[
\boxed{
\text{metric perturbation}
\neq
\text{gauge-invariant radiative content}
\neq
\text{generic DSD propagation}.
}
\]

No generic DSD claim is allowed to identify \(c_{\rm info}\) with the relativistic light speed \(c\) merely because standard linearized GR has null gravitational-wave characteristics.

---

## 2. Standard-relativity package supplied at this gate

The following are treated as **R2 RELATIVITY_SPECIALIZATION** inputs, not as pre-existing DSD consequences:

```text
four-dimensional Minkowski background eta_{mu nu}
weak-field perturbative split g_{mu nu} = eta_{mu nu} + h_{mu nu}
linearization to first order in h
Einstein field equation as the target dynamical law
standard infinitesimal diffeomorphism action
de Donder/Lorenz gauge choice when imposed
```

Standard weak-field GR gives, to first order,

\[
h_{\mu\nu}\mapsto
h_{\mu\nu}
+\partial_\mu\xi_\nu+\partial_\nu\xi_\mu
\]

up to the sign convention chosen for the coordinate transformation.

Define the trace reverse

\[
\bar h_{\mu\nu}
=
h_{\mu\nu}
-\frac12\eta_{\mu\nu}h,
\qquad
h=\eta^{\mu\nu}h_{\mu\nu}.
\]

In four spacetime dimensions,

\[
\bar{\bar h}_{\mu\nu}=h_{\mu\nu},
\qquad
\bar h=-h.
\]

The audit checks both identities exactly.

External standard-theory references used for this gate:

- David Tong, *General Relativity*, weak-field and gravitational-wave section.
- Cambridge/DAMTP linearized-GR lecture notes.
- Caltech gravitational-wave lecture notes for TT tidal response.

---

## 3. de Donder/Lorenz gauge is a gauge condition, not a new physical law

The de Donder condition is

\[
\partial^\mu \bar h_{\mu\nu}=0.
\]

Under a further infinitesimal gauge transformation,

\[
\bar h_{\mu\nu}\mapsto
\bar h_{\mu\nu}
+
\partial_\mu\xi_\nu
+
\partial_\nu\xi_\mu
-
\eta_{\mu\nu}\partial_\rho\xi^\rho,
\]

the de Donder condition remains satisfied when

\[
\Box \xi_\nu=0.
\]

Hence fixing de Donder gauge does **not** exhaust the gauge freedom.

For a plane wave with null wavevector

\[
k^\mu=(1,0,0,1),
\qquad
k_\mu k^\mu=0,
\]

the polarization tensor \(\bar H_{\mu\nu}\) obeys four transversality constraints

\[
k^\mu \bar H_{\mu\nu}=0.
\]

The finite exact rank audit gives:

```text
symmetric tensor amplitude dimension : 10
Lorenz/de Donder constraint rank      : 4
constraint-satisfying amplitude dim   : 6
residual gauge-image rank             : 4
physical quotient dimension           : 2
```

Thus

\[
\boxed{10-4-4=2}
\]

for the standard massless spin-2 plane-wave sector in four-dimensional linearized GR.

This counting is classified as **R3 STANDARD_THEOREM_CONSEQUENCE** after the R2 background/dynamics/gauge package is supplied.

---

## 4. TT specialization and the two radiative representatives

For propagation in the \(+z\) direction, the audit uses the standard transverse-traceless representatives

\[
H_+
=
\begin{pmatrix}
0&0&0&0\\
0&1&0&0\\
0&0&-1&0\\
0&0&0&0
\end{pmatrix},
\qquad
H_\times
=
\begin{pmatrix}
0&0&0&0\\
0&0&1&0\\
0&1&0&0\\
0&0&0&0
\end{pmatrix}.
\]

Both satisfy

\[
k^\mu H_{\mu\nu}=0,
\qquad
H^\mu{}_{\mu}=0,
\qquad
H_{0\mu}=0,
\]

and add two independent non-gauge directions to the residual-gauge image.

The audit therefore confirms the standard result that the TT sector has the \(+\) and \(\times\) polarizations.

The boundary is equally important:

\[
\boxed{
\text{TT gauge representative}
\neq
\text{unique physical metric representation}.
}
\]

TT is a convenient specialization inside the standard linearized theory, not a generic DSD identity rule.

---

## 5. Linearized Einstein equation and vacuum wave propagation

In de Donder gauge, the standard linearized Einstein equation is

\[
\Box \bar h_{\mu\nu}
=
-16\pi G\,T_{\mu\nu}
\]

in the usual \(c=1\) convention.

In vacuum,

\[
\Box \bar h_{\mu\nu}=0.
\]

For a nonzero plane-wave amplitude,

\[
\bar h_{\mu\nu}
=
H_{\mu\nu}e^{ik_\rho x^\rho},
\]

this requires

\[
k_\mu k^\mu=0.
\]

The Python witness keeps \(c\) explicit rather than setting all speeds to one. With

\[
c=\frac73,\qquad
k_z=\frac52,\qquad
\omega=c\,k_z,
\]

the wave symbol

\[
-\frac{\omega^2}{c^2}+k_z^2
\]

vanishes exactly, while replacing the propagation speed by \(2\) does not.

Therefore the standard result is

\[
\boxed{
v_{\rm GW}=c
}
\]

for the vacuum plane-wave characteristics of supplied linearized GR.

This is **not** used to infer any value for DSD \(c_{\rm info}\).

---

## 6. Gauge perturbation versus curvature response

On a flat background, a pure-gauge perturbation

\[
h^{(\xi)}_{\mu\nu}
=
\partial_\mu\xi_\nu+\partial_\nu\xi_\mu
\]

may be nonzero while its first-order Riemann tensor vanishes:

\[
R^{(1)}_{\alpha\beta\gamma\delta}
[h^{(\xi)}]
=
0.
\]

The finite plane-wave audit checks all \(4^4=256\) indexed Riemann components for a nonzero pure-gauge amplitude and finds all of them zero.

This yields the explicit separation

\[
\boxed{
h_{\mu\nu}\neq0
\not\Rightarrow
R^{(1)}_{\alpha\beta\gamma\delta}\neq0.
}
\]

For the TT representatives, however, the tidal components are nonzero. In the adopted sign convention,

\[
R^{(1)}_{i0j0}
=
-\frac12\ddot h^{TT}_{ij}.
\]

The finite witness confirms:

```text
plus mode:
  R_x0x0 = - R_y0y0 != 0

cross mode:
  R_x0y0 != 0
```

Thus physical relative acceleration of nearby geodesics can be carried by curvature even when a chosen TT coordinate system keeps freely falling test masses at fixed spatial coordinate labels.

Important boundary:

\[
\boxed{
\text{flat-background linearized Riemann gauge invariance}
}
\]

must not be promoted without qualification to arbitrary curved backgrounds. In general perturbation theory, the gauge transformation of a perturbed tensor includes the Lie derivative of the background tensor; the flat-background result works here because the background Riemann tensor vanishes.

---

## 7. DSD propagation firewall

The current DSD Structural Reorganization Dynamics defines \(c_{\rm info}\) only after supplying:

```text
localization carrier
propagation metric
metric-time scale
discrepancy convention
evolution family
regularity / well-posedness assumptions
```

and defines it as the infimal admissible bound for component-resolved distinguishability-support expansion.

Therefore

\[
\boxed{
c_{\rm info}
\text{ is model/interface dependent in generic DSD.}
}
\]

By contrast, in this gate the null characteristic speed \(c\) is obtained only after supplying the standard linearized Einstein system on Minkowski spacetime.

Hence the mandatory non-identification is

\[
\boxed{
v_{\rm GW}=c
\not\Rightarrow
c_{\rm info}=c.
}
\]

An application could later impose an explicit bridge under which a DSD propagation bound is compared with the relativistic characteristic cone. Such a bridge would be additional model data and would require locality, support-faithfulness, and the relevant propagation-completeness conditions.

---

## 8. Provenance ledger

```text
R2 RELATIVITY_SPECIALIZATION
  Minkowski background
  weak-field split
  first-order truncation
  infinitesimal diffeomorphism rule
  linearized Einstein equation
  de Donder gauge choice

R3 STANDARD_THEOREM_CONSEQUENCE
  trace-reversal identities
  residual gauge condition
  vacuum wave equation
  null plane-wave dispersion
  TT reduction
  two radiative polarizations
  flat-background pure-gauge R^(1)=0
  TT tidal-curvature response

R4 REMAINS_EXTERNAL_NOT_DERIVED
  generic DSD c_info = relativistic c
  nonlinear GR from one linearized witness
  unique physical gauge from TT gauge
  unique physical source from one observed waveform
```

No R3 result is counted retroactively as evidence that generic DSD supplied the R2 target structure.

---

## 9. Reproducibility

GitHub files:

```text
audits/science/2026-09-10_rel_core_006_linearized_gravity_gauge_radiative_degree_gate.py
audits/science/2026-09-10_rel-core-006-linearized-gravity-gauge-radiative-degree-gate-audit.md
methodology/RELATIVITY_LINEARIZED_GRAVITY_RADIATIVE_INTERFACE.md
```

Run from repository root:

```bash
python audits/science/2026-09-10_rel_core_006_linearized_gravity_gauge_radiative_degree_gate.py --mode all
```

Actual result:

```text
TRACE:       4/4 PASS
DOF:         9/9 PASS
WAVE:        5/5 PASS
CURVATURE:   7/7 PASS
PROVENANCE: 10/10 PASS

TOTAL: 35/35 checks passed
OVERALL: PASS_WITH_BOUNDARY
```

The script uses the Python standard library only.

---

## 10. Final verdict

**PASS_WITH_BOUNDARY**.

The standard linearized-GR chain is internally reconstructible after the standard relativity specialization is explicitly supplied:

\[
\boxed{
\text{linearized Einstein dynamics}
\Longrightarrow
\text{vacuum wave equation}
\Longrightarrow
k^2=0
\Longrightarrow
\text{two TT radiative modes}
}
\]

with nontrivial tidal curvature.

But this does not establish

\[
\boxed{
\text{generic DSD}
\Longrightarrow
\text{linearized Einstein gravity}
}
\]

and does not establish

\[
\boxed{
c_{\rm info}=c.
}
\]

No DSD core-paper revision is required by this gate.

Next target:

```text
REL Core 007 — Horizon / Coordinate-Singularity / Curvature-Singularity / Causal-Boundary Gate
```

The next gate should separate Schwarzschild-coordinate failure, regular horizon geometry, invariant curvature, causal one-way structure, trapped/null surfaces, genuine curvature singularity, geodesic incompleteness, and DSD descriptive-access restrictions before the final integrated relativity closure.
