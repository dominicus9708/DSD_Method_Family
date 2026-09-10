# REL Extension 006 — Tidal Geodesic-Deviation / Curvature-Reconstruction / Local-Observable Gate

Date: 2026-09-10  
Status: **PASS_WITH_BOUNDARY**  
Program: **Core-Theory Reconstruction Challenge — Standard Relativity Extension Track**

## 1. Purpose

REL Extension 005 separated local inertial removability of connection coefficients, curvature, acceleration fields, gravitational clock-rate gradients, and Einstein dynamics.

This gate asks the next operational question:

> How much of spacetime curvature is recoverable from relative accelerations of neighboring freely falling test bodies, and which extra observer/probe configurations are required before one may claim reconstruction of the full Riemann tensor?

The central firewall is

\[
\text{one tidal readout}
\neq
\text{full curvature reconstruction}.
\]

The audit also keeps curvature measurement distinct from Einstein source dynamics and from any generic DSD claim.

---

## 2. DSD baseline

The current DSD Structural Reorganization Dynamics paper states that dynamic coefficients and operators are supplied by a constitutive dynamic bridge or as separate dynamic data; the model family is not a universal DSD law. Its finite-propagation construction likewise requires a supplied metric localization carrier and metric time when speed is interpreted.

Therefore this gate does not identify

```text
DSD localization metric = physical spacetime metric
DSD lineage = geodesic congruence
DSD residual = tidal acceleration
DSD c_info = relativistic c
```

without an explicit downstream bridge.

---

## 3. Standard theorem lock: geodesic deviation

For a timelike reference geodesic with tangent \(u^\mu\) and a connecting vector \(\xi^\mu\), use the standard GR comparator

\[
\frac{D^2\xi^\mu}{D\tau^2}
=
-R^\mu{}_{\nu\rho\sigma}
 u^\nu \xi^\rho u^\sigma,
\]

with the sign convention fixed only for this audit.

For an orthonormal frame comoving with the reference observer,

\[
u^\mu=(1,0,0,0),\qquad \xi^0=0,
\]

the leading spatial relative acceleration is controlled by

\[
A^i=-R^i{}_{0j0}\xi^j.
\]

Thus a fixed comoving observer samples the tidal/electric block \(R_{0i0j}\).

This equation is treated as an external standard-relativity law, not as a theorem of generic DSD.

---

## 4. Algebraic-curvature parameter-space witness

A four-dimensional algebraic Riemann tensor has the pair antisymmetries, pair-exchange symmetry, and first Bianchi identity.

The regression code represents it as a symmetric bilinear form on the six-dimensional bivector space

```text
01, 02, 03, 12, 13, 23
```

and imposes the single four-dimensional algebraic Bianchi relation

\[
R_{0123}+R_{0231}+R_{0312}=0.
\]

The resulting exact rational basis has dimension 20. Every basis tensor is checked against the full algebraic first Bianchi identity and the index symmetries.

This is a finite algebraic representation of the usual 20-component local curvature space in general four-dimensional pseudo-Riemannian geometry.

---

## 5. Fixed-observer rank gate

For

\[
u=(1,0,0,0)
\]

and one, two, then three independent spatial separation vectors, the exact rational measurement-map ranks are

```text
1 separation direction -> rank 3
2 separation directions -> rank 5
3 separation directions -> rank 6
```

Hence the full three-direction fixed-observer tidal experiment determines at most the six-dimensional symmetric \(R_{0i0j}\) sector in the general nonvacuum algebraic-curvature space.

Therefore

\[
\boxed{
\text{fixed-observer tidal matrix}
\not\Rightarrow
\text{full 20-component Riemann tensor}.
}
\]

---

## 6. Hidden-curvature countermodel

Construct an algebraic curvature perturbation whose only independent nonzero bivector entry is

\[
\Delta R_{1212}=1.
\]

It satisfies the required Riemann symmetries and algebraic Bianchi identity.

For the fixed comoving observer \(u=(1,0,0,0)\),

\[
\Delta R_{0i0j}=0
\]

for all spatial \(i,j\), so all three comoving deviation readouts are unchanged.

Yet a moving observer configuration, for example with

\[
u=(1,1/5,0,0),
\]

and an orthogonal separation in the second spatial direction detects the perturbation.

Thus two different full Riemann tensors can produce the same fixed-observer tidal matrix:

\[
\boxed{
R_{0i0j}\text{ agreement for one observer}
\not\Rightarrow
R_{\alpha\beta\gamma\delta}\text{ agreement}.
}
\]

---

## 7. Multi-configuration reconstruction gate

The code then varies observer velocities and orthogonal separation directions. The measurement-map rank is checked exactly over rational arithmetic.

The rank grows beyond 6 and reaches the full algebraic-curvature dimension 20. In this particular deterministic witness, full rank is first reached after 14 observer/separation configurations.

The number 14 is **not** proposed as an optimal physical gravitational-compass count. It is only the first full-rank point of this deliberately simple regression configuration.

External comparator literature is stronger and more operationally optimized. Puetzfeld and Obukhov (2016) provide exact curvature solutions using standard and generalized deviation equations. Their later gravitational-compass summary gives an explicit setup requiring 13 test bodies in a general spacetime for the standard deviation equation, with fewer in vacuum.

The audit therefore records only the structural conclusion:

\[
\boxed{
\text{full curvature recovery requires sufficiently rich multi-probe data}.
}
\]

---

## 8. Fermi-normal local-observable interface

In Fermi normal coordinates along a freely falling reference geodesic, the metric is Minkowskian on the reference worldline and the leading spatial-distance corrections are quadratic and curvature-controlled. In the common convention,

\[
g_{00}=-1-R_{0i0j}x^ix^j+O(|x|^3),
\]

with analogous curvature-dependent terms in \(g_{0i}\) and \(g_{ij}\).

This reinforces the distinction:

```text
local inertial frame on the reference geodesic
!=
absence of tidal curvature around the reference geodesic
```

and

```text
one numerical component table
!=
the frame-independent existence of curvature
```

The local tetrad/frame is part of the operational specification for component readout.

---

## 9. Linear-deviation scope boundary

The standard geodesic deviation equation is a neighboring-worldline/linear-deviation relation. Finite separations, higher-order relative motion, arbitrary worldlines, and extended-body effects require additional structure or generalized deviation equations.

Puetzfeld and Obukhov explicitly derive and use a generalized deviation equation and show how both standard and generalized deviation equations can determine curvature.

Therefore this audit does not turn the linear Jacobi equation into an exact finite-separation law.

---

## 10. Provenance classification

```text
R0 PRE_EXISTING_DSD
  typed status/applicability discipline
  explicit downstream bridge discipline
  external evolution time not automatically proper time
  supplied localization metric not automatically spacetime metric

R1 GENERAL_MATHEMATICAL_STRUCTURAL
  tensor-index symmetries
  linear-map rank
  underdetermination / kernel reasoning
  local-frame component bookkeeping

R2 RELATIVITY_SPECIALIZATION
  Lorentzian metric
  Levi-Civita connection
  timelike geodesic congruence
  proper time
  separation vector
  local orthonormal frame
  geodesic-deviation equation
  Riemann-curvature interpretation

R3 STANDARD_THEOREM_CONSEQUENCE
  fixed-observer tidal projection R_0i0j
  Fermi-normal curvature expansion
  curvature reconstruction from sufficiently rich supplied probe data

R4 REMAINS_EXTERNAL_NOT_DERIVED
  why physical spacetime is four-dimensional Lorentzian
  why test bodies obey the required geodesic law
  why the physical connection is Levi-Civita
  actual measured curvature values
  Einstein field equation and source law
  G, c, Lambda and matter data
```

A successful curvature reconstruction from R2 probes is not back-counted as an R0 DSD derivation.

---

## 11. Deterministic regression result

Run from repository root:

```bash
python audits/science/2026-09-10_rel_extension_006_tidal_geodesic_deviation_curvature_reconstruction_local_observable_gate.py --mode all
```

Observed result:

```text
ALGEBRAIC_RIEMANN_SPACE:             PASS
FIXED_OBSERVER_TIDAL_RANK:           PASS
HIDDEN_CURVATURE_COUNTERMODEL:       PASS
MULTI_CONFIGURATION_RECONSTRUCTION:  PASS
FERMI_LOCAL_OBSERVABLE:              PASS
DSD_PROVENANCE:                      PASS
COMPARATOR_SCOPE:                    PASS

TOTAL: 71/71 checks passed
OVERALL: PASS_WITH_BOUNDARY
```

The 71 checks include repeated algebraic basis and rank consistency checks. They are not 71 independent empirical tests or physical theorems.

---

## 12. Verdict

**PASS_WITH_BOUNDARY**.

The key result is

\[
\boxed{
\text{tidal relative acceleration is a local curvature probe}
}
\]

but

\[
\boxed{
\text{one observer / one tidal matrix}
\not\Rightarrow
\text{full local Riemann reconstruction}.
}
\]

A sufficiently rich set of observer velocities, separation vectors, and relative-acceleration measurements can reconstruct the curvature under the supplied GR assumptions. This remains conditional reconstruction within standard relativity.

No contradiction with the current DSD core papers was found, and no structural-gravity hypothesis was used.

---

## 13. External references

- D. Puetzfeld, Y. N. Obukhov, *Generalized deviation equation and determination of the curvature in general relativity*, Phys. Rev. D 93, 044073 (2016), DOI: 10.1103/PhysRevD.93.044073, arXiv:1511.08465.
- D. Puetzfeld, Y. N. Obukhov, C. Lämmerzahl, *Gravitational clock compass in general relativity*, Phys. Rev. D 98, 024032 (2018), DOI: 10.1103/PhysRevD.98.024032, arXiv:1805.10673.
- A. Ito, J. Soda, *A formalism for magnon gravitational wave detectors*, Eur. Phys. J. C 80, 545 (2020), which reviews Fermi-normal-coordinate curvature expansions used here as a standard comparator.

These references are external comparators and are not counted as DSD-derived evidence.

---

## 14. Next target

**REL Extension 007 — Ricci / Weyl Decomposition / Matter-Source / Vacuum-Curvature Gate**.

The next audit will separate

```text
full measured Riemann curvature
Ricci curvature
Weyl curvature
vacuum condition R_mu_nu = 0
matter stress-energy
Einstein field equation
source attribution
```

with the central firewalls

\[
R_{\mu\nu}=0
\not\Rightarrow
R_{\alpha\beta\gamma\delta}=0,
\]

and

\[
\text{measured curvature decomposition}
\neq
\text{independent derivation of its material source or Einstein dynamics}.
\]
