# REL Extension 005 — Equivalence Principle / Local Inertial Frame / Gravitational Clock-Rate Gate

Date: 2026-09-10  
Status: **PASS_WITH_BOUNDARY**  
Program: **Core-Theory Reconstruction Challenge — Standard Relativity Extension Track**

## 1. Purpose

REL Extension 004 separated Lorentzian metric proper time from the operational response law and calibration of actual accelerated clocks.

This gate moves from accelerated clocks in special relativity to the local-inertial/equivalence-principle interface of general relativity. The central questions are:

1. Does removal of connection coefficients at one event remove spacetime curvature?
2. Does an acceleration field or gravitational clock-rate gradient by itself diagnose curvature?
3. Does the equivalence principle independently derive the Einstein field equation?
4. Can DSD distinguish local inertial describability, tidal curvature, clock readout, metric specialization, and source dynamics without identifying them?

The audit preserves the standard-relativity provenance classes already fixed in REL Core 001R–008.

---

## 2. Provenance classes used here

```text
R0 PRE_EXISTING_DSD
  typed status/applicability
  explicit downstream bridge discipline
  external numerical evolution time is not automatically relativistic proper time
  c_info is not automatically relativistic c

R1 GENERAL_MATHEMATICAL_STRUCTURAL
  coordinate connection coefficients
  curvature tensor/scalar
  normal-coordinate/local-inertial construction given suitable metric/connection data
  tensorial versus non-tensorial transformation distinction

R2 RELATIVITY_SPECIALIZATION
  Lorentzian spacetime metric
  local freely falling / inertial interpretation
  equivalence-principle formulation
  physical clock bridge
  static observer/lapse interpretation
  physical relativistic c

R3 STANDARD_THEOREM_CONSEQUENCE
  stationary-clock rate from a supplied static metric
  Rindler accelerated-coordinate rate gradient
  weak-field clock-rate/redshift approximation
  curvature/tidal response from supplied metric

R4 REMAINS_EXTERNAL / NOT INDEPENDENTLY DERIVED
  actual spacetime solution/source content
  Einstein field equation
  Newton constant G
  empirical redshift data
  claim that DSD metric time equals relativistic proper time
  claim that c_info equals relativistic c
```

Only R0/R1 are eligible as target-independent DSD/general-structure content.

---

## 3. Standard theorem lock: local inertial coordinates are local

For a regular pseudo-Riemannian/Lorentzian metric, normal coordinates can be chosen at an event so that the metric has its canonical value there and the Levi-Civita connection coefficients vanish at that event.

This does **not** imply that curvature vanishes.

A finite exact witness is the 1+1-dimensional metric

\[
 ds^2=-(1+kx^2)dt^2+dx^2,
 \qquad k>0.
\]

Let

\[
 A(x)=1+kx^2.
\]

For

\[
 ds^2=-A(x)dt^2+dx^2,
\]

the relevant connection coefficients are

\[
\Gamma^t{}_{tx}=\frac{A'}{2A},
\qquad
\Gamma^x{}_{tt}=\frac{A'}{2}.
\]

At \(x=0\), \(A'(0)=0\), so both vanish.

But the scalar curvature is

\[
R=\frac{-AA''+\tfrac12(A')^2}{A^2},
\]

hence

\[
R(0)=-2k\neq0.
\]

The tidal component in the convention used by the regression code is

\[
R^x{}_{txt}(0)=k\neq0.
\]

Therefore

\[
\boxed{
\Gamma^\alpha{}_{\beta\gamma}(p)=0
\not\Rightarrow
R^\alpha{}_{\beta\gamma\delta}(p)=0.
}
\]

This is the exact firewall needed between local inertial removability and tidal curvature.

External comparator: Riemann-normal-coordinate constructions explicitly impose vanishing connection coefficients at a regular event while retaining curvature in higher-order metric structure; see Hari K. and D. Kothawala, *Normal coordinates based on curved tangent space*, arXiv:2003.10169.

---

## 4. Equivalence-principle scope gate

The phrase “equivalence principle” has multiple inequivalent formulations in the literature. This audit therefore does not merge universality of free fall, Einstein equivalence principle, and stronger formulations into one DSD label.

For the local freely falling formulation used here, the essential idealization is that tidal effects are neglected over a sufficiently local region. Thus local nongravitational experiments in a freely falling frame may reproduce Lorentz-frame behavior to the stated approximation, while curvature can remain detectable by sufficiently extended/tidal measurements.

This follows the careful scope emphasized in R. Samaroo, *The principle of equivalence as a criterion of identity*, Synthese 197 (2020) 3481–3505, DOI 10.1007/s11229-018-01897-w.

The audit therefore rejects the following inference:

\[
\text{equivalence principle}
\Rightarrow
\text{global flatness}.
\]

It also rejects:

\[
\text{equivalence principle}
\Rightarrow
\text{Einstein field equation}.
\]

The latter would erase the distinction between a local kinematical/operational principle and a global dynamical field law.

---

## 5. Flat accelerated countermodel: Rindler clock gradient without curvature

Use the 1+1-dimensional Rindler metric

\[
 ds^2=-(1+ax)^2dt^2+dx^2,
 \qquad 1+ax>0.
\]

Set

\[
A(x)=(1+ax)^2.
\]

Substitution into

\[
R=\frac{-AA''+\tfrac12(A')^2}{A^2}
\]

gives

\[
R=0.
\]

Nevertheless stationary Rindler observers have nonzero proper acceleration

\[
\alpha(x)=\frac{|a|}{1+ax},
\]

and a stationary clock at fixed \(x\) satisfies

\[
d\tau=(1+ax)dt.
\]

For two stationary clocks,

\[
\frac{d\tau_2}{d\tau_1}
=
\frac{1+ax_2}{1+ax_1}.
\]

Thus

\[
\boxed{
\text{stationary clock-rate gradient}
\not\Rightarrow
\text{nonzero spacetime curvature}.
}
\]

Likewise, nonzero coordinate connection/acceleration does not by itself establish curvature.

This is a particularly important equivalence-principle boundary because it prevents an observed or calculated rate gradient from being silently promoted into a curvature measurement.

A modern interpretive comparison is J. Fankhauser and J. Read, *Gravitational redshift revisited: inertia, geometry, and charge*, Studies in History and Philosophy of Science 108 (2024) 19–27, arXiv:2309.10499. They emphasize that the original Pound–Rebka sensitivity can be accounted for within an accelerated-frame/SR treatment, whereas more sensitive redshift phenomena require additional structure; curvature is not the only possible gravitational representation.

---

## 6. Static metric clock-rate gate

For a supplied static metric written schematically as

\[
 ds^2=-N(\mathbf x)^2dt^2+h_{ij}dx^i dx^j,
\]

a stationary observer has

\[
d\tau=N(\mathbf x)dt.
\]

Therefore for two stationary observers,

\[
\frac{d\tau_2}{d\tau_1}
=
\frac{N(\mathbf x_2)}{N(\mathbf x_1)}.
\]

A rescaling of the coordinate label \(t'=\lambda t\) rescales the lapse representative to \(N'=N/\lambda\), leaving the physical rate ratio unchanged.

Hence coordinate time units and the invariant comparison encoded by the supplied metric are distinct.

In the weak-field specialization

\[
g_{00}\simeq-(1+2\Phi/c^2),
\]

one obtains

\[
\frac{d\tau_2}{d\tau_1}
=\sqrt{\frac{1+2\Phi_2/c^2}{1+2\Phi_1/c^2}}
\simeq
1+\frac{\Phi_2-\Phi_1}{c^2}.
\]

The regression code verifies the first-order approximation on several small-potential samples.

The provenance firewall is

\[
\boxed{
\text{clock-rate prediction from supplied }g_{00}
\neq
\text{derivation of }g_{00}
\neq
\text{derivation of Einstein dynamics}.
}
\]

---

## 7. Experimental redshift gate

Pound and Rebka's nuclear-resonance work established the classic laboratory gravitational redshift program:

- R. V. Pound and G. A. Rebka Jr., *Gravitational Red-Shift in Nuclear Resonance*, Phys. Rev. Lett. 3, 439 (1959), DOI 10.1103/PhysRevLett.3.439.
- R. V. Pound and G. A. Rebka Jr., *Apparent Weight of Photons*, Phys. Rev. Lett. 4, 337 (1960), DOI 10.1103/PhysRevLett.4.337.

Modern satellite-clock tests provide substantially more precise redshift tests; for example S. Herrmann et al., *Test of the Gravitational Redshift with Galileo Satellites in an Eccentric Orbit*, Phys. Rev. Lett. 121, 231102 (2018), DOI 10.1103/PhysRevLett.121.231102.

These empirical results are external evidence for relativistic clock/redshift predictions under their respective models.

They are **not** back-counted as:

```text
proof that DSD independently generated the metric,
proof that a clock-rate gradient uniquely identifies curvature,
proof that the equivalence principle uniquely determines Einstein dynamics,
or proof that c_info = c.
```

The interpretive literature around Pound–Rebka is itself nontrivial, which is another reason to keep the experimental readout, accelerated-frame description, metric description, curvature, and field dynamics as distinct typed records.

---

## 8. DSD boundary

The current DSD Structural Reorganization Dynamics layer explicitly states that numerical time is an external evolution parameter whenever metric time is required; a purely ordered history may be considered without numerical metric time, and speed requires supplied metric time. The time parameter is not automatically an input sort, geometric axis, or realized line.

The same paper lists the localization metric carrier and dynamic operators as supplied downstream data, and the static aggregation paper states that no dynamical or physical constitutive law is introduced at the static layer.

Accordingly this audit preserves:

\[
t_{\mathrm{DSD}}\not\equiv\tau_{\mathrm{GR}}
\]

without an explicit bridge, and also

\[
c_{\mathrm{info}}\not\equiv c
\]

without an explicit bridge.

DSD can type and compare

```text
local coordinate connection record,
curvature/tidal record,
clock-rate readout,
static metric/lapse specialization,
empirical redshift record,
and source/dynamical law,
```

while preserving their distinct provenance.

No structural-gravity hypothesis is imported into this standard-relativity gate.

---

## 9. Deterministic regression result

Run from repository root:

```bash
python audits/science/2026-09-10_rel_extension_005_equivalence_principle_local_inertial_gravitational_clock_rate_gate.py --mode all
```

Observed result:

```text
LOCAL_INERTIAL_CURVATURE:          PASS
RINDLER_FLAT_ACCELERATION:         PASS
STATIC_CLOCK_RATE:                 PASS
WEAK_FIELD_CLOCK_RATE:             PASS
EQUIVALENCE_PRINCIPLE_SCOPE:       PASS
REDSHIFT_INTERPRETATION_FIREWALL:  PASS
DSD_PROVENANCE:                    PASS
COMPARATOR_SCOPE:                  PASS

TOTAL: 122/122 checks passed
OVERALL: PASS_WITH_BOUNDARY
```

The large check count includes repeated parameter samples. It must not be interpreted as 122 independent physical proofs. The code is a deterministic algebraic/provenance regression audit, not an empirical test of general relativity.

---

## 10. Verdict

**PASS_WITH_BOUNDARY**.

The decisive separations are

\[
\boxed{
\Gamma(p)=0
\not\Rightarrow
R(p)=0,
}
\]

\[
\boxed{
\text{accelerated-frame clock gradient}
\not\Rightarrow
\text{curvature},
}
\]

and

\[
\boxed{
\text{equivalence principle / local inertial structure}
\not\Rightarrow
\text{Einstein field dynamics}.
}
\]

The standard-relativity reconstruction remains compatible with DSD's bridge discipline, but no new independent derivation of GR from generic DSD is obtained.

No DSD core-paper contradiction or required core revision was found at this gate.

---

## 11. Next target

**REL Extension 006 — Tidal Geodesic-Deviation / Curvature-Reconstruction / Local-Observable Gate**.

The next audit should separate:

```text
single free-fall worldline
family of neighboring worldlines
relative acceleration / geodesic deviation
Riemann curvature contraction
full curvature reconstruction from finite directional probes
Ricci versus Weyl curvature
local tidal observable
coordinate artifacts
Einstein source dynamics
DSD distinguishability/readout resolution
```

The principal firewall will be

\[
\text{one locally inertial worldline}
\neq
\text{enough information to reconstruct full curvature},
\]

while a sufficiently rich family of tidal probes can constrain or reconstruct curvature components only under explicit geometric and measurement assumptions.
