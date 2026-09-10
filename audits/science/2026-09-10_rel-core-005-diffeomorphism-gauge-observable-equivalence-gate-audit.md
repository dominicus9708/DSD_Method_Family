# REL Core 005 — Diffeomorphism / Gauge / Observable / Equivalence Gate

Date: 2026-09-10  
Status: **PASS_WITH_BOUNDARY**  
Program: **Core-Theory Reconstruction Challenge — Standard Relativity Track**

## 1. Purpose

REL Core 001R fixed the relativity provenance classes, REL Core 002 separated Lorentzian metric admission from causal/differential geometry, REL Core 003 separated geodesic/transport/curvature response, and REL Core 004 separated Einstein dynamics, constraints, conservation, and Cauchy development.

REL Core 005 audits the representation/equivalence layer:

```text
passive coordinate change
active diffeomorphism pullback
isometry
GR gauge-related configuration
tensor/scalar covariance
gauge-invariant or relational observable
local chart/invariant agreement
global geometric equivalence
DSD strict descriptive equivalence
```

The central firewall is

\[
\boxed{
\text{coordinate relabelling}
\neq
\text{active field pullback}
\neq
\text{isometry}
\neq
\text{gauge equivalence}
\neq
\text{DSD strict descriptive equivalence}.
}
\]

No claim is made that generic DSD derives diffeomorphism invariance, the Einstein gauge structure, a preferred observable algebra, or a unique relational reference system.

---

## 2. Provenance lock

The established relativity provenance classes remain:

```text
R0  PRE_EXISTING_DSD
R1  GENERAL_MATHEMATICAL_STRUCTURAL
R2  RELATIVITY_SPECIALIZATION
R3  STANDARD_THEOREM_CONSEQUENCE
R4  REMAINS_EXTERNAL_NOT_DERIVED
```

### R0 — pre-existing DSD

Relevant DSD structure already present before this gate includes:

```text
typed identity/status
explicit bridges
restriction vs strict equivalence
support/reconstruction discipline
presentation-sensitive strict base-fixed formation isomorphism
```

Formation strict descriptive equivalence compares the full candidate-level formation structure, including unsuccessful candidates, over a fixed base. It is therefore not definitionally identical to GR diffeomorphism/gauge equivalence.

### R1 — general mathematical structure

```text
charts and chart transitions
diffeomorphisms as smooth invertible maps
pullback/pushforward of geometric objects
isometry as metric-preserving diffeomorphism
tensorial/scalar transformation rules
local-vs-global reconstruction distinction
```

### R2 — relativity specialization

```text
Lorentzian spacetime model
the field content regarded as physically relevant
general covariance / GR gauge interpretation
boundary and asymptotic conditions
admissible diffeomorphism class
relational reference-field or dressing rule when used
```

### R3 — conditional standard consequences

Given the supplied geometric and gauge structure:

```text
coordinate-independent tensor equations
naturality under pullback
isometry-preserved geometric quantities
diffeomorphism-related Einstein solutions when all fields are dragged
gauge-invariant relational readouts under their declared construction
```

### R4 — remains external

Generic DSD does not independently determine:

```text
which spacetime diffeomorphisms are gauge-trivial
which boundary/asymptotic transformations carry physical charges
a preferred relational clock/rod system
a complete observable algebra for GR
a complete global isometry classifier
GR gauge equivalence from DSD strict descriptive equivalence
```

---

## 3. Passive coordinate change is not information loss

Take a \(1+1\) Minkowski vector with coordinates \((t,x)\) and a Lorentz boost

\[
t'=\gamma(t-\beta x),\qquad
x'=\gamma(x-\beta t),
\qquad
\gamma=(1-\beta^2)^{-1/2}.
\]

For the finite witness

\[
(t,x)=(2,0.7),\qquad \beta=0.4,
\]

the coordinate components change, while

\[
-t'^2+x'^2=-t^2+x^2.
\]

The inverse boost with \(-\beta\) recovers the original coordinates.

Therefore

\[
\boxed{
\text{passive coordinate change}
\not\Rightarrow
\text{physical information loss}.
}
\]

This continues PHY-REL-001 and PHY-REL-005: invertible representation change and causal/access limitation remain separate questions.

---

## 4. Active diffeomorphism is not the same predicate as isometry

Let \(\eta=-dt^2+dx^2\).

For the translation

\[
\phi_a(t,x)=(t+a,x),
\]

the derivative is the identity, hence

\[
\phi_a^*\eta=\eta.
\]

This active diffeomorphism is an isometry.

For the dilation

\[
\phi_\lambda(t,x)=(\lambda t,\lambda x),
\qquad \lambda\neq1,
\]

one has

\[
\phi_\lambda^*\eta
=
\lambda^2\eta
\neq
\eta.
\]

Thus it is a diffeomorphism but not an isometry of \((M,\eta)\).

Therefore

\[
\boxed{
\text{isometry}
\subsetneq
\text{diffeomorphism}
}
\]

for this standard geometric role distinction.

The point is logical, not merely terminological: an active diffeomorphism always defines a pullback action on the fields, while an isometry additionally fixes the metric field.

---

## 5. Covariant scalar transformation is not same-coordinate invariance

Use the Lorentzian conformal family

\[
g_b=e^{2bx^2}(-dt^2+dx^2)
\]

with the curvature convention already used in REL Core 002:

\[
R[g_b](x)
=
-4b e^{-2bx^2}.
\]

Let

\[
\phi_a(t,x)=(t,x+a).
\]

Naturality gives

\[
R[\phi_a^*g_b](p)
=
(\phi_a^*R[g_b])(p)
=
R[g_b](\phi_a(p)).
\]

For \(b=1/4\), \(a=0.6\), and \(p=(0,0)\),

\[
R[\phi_a^*g_b](p)
=
R[g_b](0,0.6)
\neq
R[g_b](0,0).
\]

Hence a scalar is coordinate-independent in its transformation law, but its value at a fixed labelled manifold point is not invariant under an active pullback unless the comparison point is dragged as well or is defined relationally.

The correct firewall is

\[
\boxed{
R[\phi^*g](p)=R[g](\phi(p))
}
\]

rather than

\[
R[\phi^*g](p)=R[g](p)
\]

for arbitrary active \(\phi\).

---

## 6. Tensor components are not observables by themselves

Under a passive Lorentz-frame change, vector components generally change. In the finite witness

\[
v=(1.5,0.2),
\]

a boost with \(\beta=0.3\) changes the component pair, while

\[
g(v,v)
\]

remains invariant and the timelike classification is preserved.

Therefore

```text
component equality
!=
tensorial/geometric equality
```

and coordinate-component readouts must retain their chart/frame provenance.

This is a direct fit to the existing DSD rule that a reduced or represented value is not automatically a complete classifier of its upstream structure.

---

## 7. Diffeomorphism-related configuration and GR gauge equivalence

If a GR configuration is represented by the full field tuple

\[
\Psi=(g,\text{matter fields},\ldots),
\]

an active diffeomorphism acts by simultaneous pullback

\[
\Psi\mapsto\phi^*\Psi.
\]

General covariance implies that the geometric field equations are natural under this action: when \(\Psi\) is a solution, the pulled configuration is again a solution under the corresponding hypotheses.

However, the stronger physical statement

```text
phi-related configurations are the same physical state
```

requires a gauge interpretation and a declared admissible diffeomorphism class.

This gate therefore does **not** use the unrestricted shortcut

\[
\boxed{\text{all diffeomorphisms are automatically gauge-trivial}.}
\]

Boundary/asymptotic conditions can distinguish proper gauge transformations from transformations that act nontrivially on boundary data or charges.

Thus:

\[
\boxed{
\text{diffeomorphism covariance}
\neq
\text{unqualified gauge triviality}.
}
\]

---

## 8. Scalar invariants do not by themselves reconstruct global geometry

A flat Lorentzian plane and a flat Lorentzian cylinder can have the same local dimension and the same local scalar curvature

\[
R=0,
\]

while differing globally in topology.

The audit records the standard global obstruction:

```text
plane:
  fundamental group = trivial

cylinder:
  fundamental group = Z
```

Hence local chart agreement or equality of a selected family of local scalar invariants is not sufficient, by itself, to certify global isometry or global diffeomorphism type.

The safe reconstruction rule is

\[
\boxed{
\text{local invariant agreement}
\not\Rightarrow
\text{global geometric equivalence}.
}
\]

No claim is made here that the chosen topology metadata constitute a computational proof of classification; the script uses them only as a provenance guard around the standard mathematical counterexample.

---

## 9. Gauge-invariant observables require an explicit construction

Coordinate-labelled local values such as

```text
R at coordinate x=0
g_tt at coordinate x=0
field value at manifold label p
```

are not automatically invariant under active diffeomorphisms.

A gauge-invariant observable can instead require a relational rule, for example:

```text
evaluate curvature where a supplied scalar clock/rod field takes declared values
```

or another admissible dressing/reference construction.

This does not mean that DSD supplies such a relational system automatically.

DSD can type and preserve:

```text
field identity
reference-system identity
applicability conditions
readout map
gauge-orbit relation
reconstruction target
```

but the physical choice of relational reference fields and the proof of gauge invariance remain additional target-theory data.

Relational-observable constructions are a substantial subject in GR and canonical/quantum gravity; this gate uses only the conservative interface requirement that the gauge/relational rule be explicit.

---

## 10. DSD strict descriptive equivalence is not GR gauge equivalence

This is the main DSD-specific result of REL Core 005.

Formation strict descriptive equivalence is a strict base-fixed formation isomorphism over the full formation descriptor. It includes complete candidate classes and is presentation-sensitive by definition.

GR gauge equivalence instead concerns target-theory geometric field configurations related by an admissible diffeomorphism action under the adopted gauge/boundary convention.

Therefore the predicates have different input objects and different preservation requirements:

```text
DSD strict descriptive equivalence:
  full candidate-level formation descriptor
  unsuccessful candidates included
  base fixing
  formation isomorphism

GR diffeomorphism/gauge equivalence:
  spacetime manifold
  metric and other physical fields
  admissible diffeomorphism
  simultaneous pullback
  gauge/boundary interpretation
```

Hence neither identification is licensed merely by the word "equivalence":

\[
\boxed{
\sim_{\mathrm{DSD,strict}}
\neq
\sim_{\mathrm{GR,gauge}}.
}
\]

A later application may supply an explicit bridge and prove compatibility between the two relations on a restricted model class. That bridge would be a downstream result, not part of either definition.

---

## 11. Reconstruction ladder

```text
TARGET: coordinate representation
  retain:
    chart + component data + transition map

TARGET: geometric tensor/scalar
  retain:
    underlying tensor field + chart transformation rule

TARGET: isometry
  retain:
    diffeomorphism phi + metric fields
  test:
    phi^* g = g

TARGET: GR gauge-related configuration
  retain:
    full target-theory field tuple
    admissible diffeomorphism
    boundary/asymptotic convention
    simultaneous pullback rule

TARGET: relational observable
  retain:
    field content
    gauge action
    relational reference/dressing rule
    applicability domain

TARGET: global geometric equivalence
  retain:
    global manifold/topology
    metric/field structure
    global map and regularity conditions

TARGET: DSD strict descriptive equivalence
  retain:
    full DSD candidate-level formation descriptor
    base-fixing data
    strict formation-isomorphism witness
```

Completeness remains target-relative.

---

## 12. DSD core impact

No revision of the Formation Axiom System, Property Axiom System, Channel-Indexed Static Aggregation, or Structural Reorganization Dynamics is required.

The current source hierarchy already contains the required firewalls:

```text
strict formation equivalence != aggregate coincidence
representation bridge != abstract property core
reduced readout != automatic reconstruction
dynamic coefficient/operator != property label
optional geometric specialization != universal DSD structure
```

In particular, the Formation paper states that strict descriptive equivalence compares the entire candidate-level formation structure and is presentation-sensitive, while the Static Aggregation paper treats covariance only under declared comparison/transport structure rather than as an automatic physical gauge principle.

---

## 13. Rejected shortcuts

The following implications are rejected:

\[
\text{coordinate components changed}
\not\Rightarrow
\text{physical state changed},
\]

\[
\text{diffeomorphism}
\not\Rightarrow
\text{isometry},
\]

\[
\text{scalar quantity}
\not\Rightarrow
\text{same-point active-gauge invariant},
\]

\[
\text{same selected local scalar invariants}
\not\Rightarrow
\text{global isometry},
\]

\[
\text{diffeomorphism covariance}
\not\Rightarrow
\text{every admissible-looking diffeomorphism is gauge-trivial},
\]

and

\[
\text{GR gauge equivalence}
\not\Rightarrow
\text{DSD strict descriptive equivalence}.
\]

The reverse final implication is also not automatic.

---

## 14. Finite/reconstruction audit

The reproducibility script checks:

```text
PASSIVE_COORDINATE_CHANGE                       5/5
ACTIVE_DIFFEOMORPHISM_VS_ISOMETRY              5/5
SCALAR_COVARIANCE_AND_POINT_LABEL              4/4
COMPONENT_VS_GEOMETRIC_INVARIANT               4/4
LOCAL_VS_GLOBAL_GEOMETRY                       5/5
PROVENANCE_AND_EQUIVALENCE_FIREWALL            8/8
```

Observed result:

```text
TOTAL: 31/31 checks passed
OVERALL: PASS_WITH_BOUNDARY
```

The script is a finite/special-case and provenance audit. It is not a proof of the complete global gauge structure of GR.

---

## 15. Verdict

\[
\boxed{\textbf{PASS\_WITH\_BOUNDARY}}
\]

More precisely:

```text
passive coordinate change separated from active pullback: YES
diffeomorphism separated from isometry: YES
scalar covariance separated from same-point active invariance: YES
component values separated from geometric invariants: YES
local invariant agreement separated from global equivalence: YES
GR gauge equivalence separated from DSD strict equivalence: YES
boundary/asymptotic gauge caveat retained: YES
generic DSD derivation of GR gauge structure: NO
DSD core contradiction found: NO
DSD core revision required: NO
```

The strongest safe conclusion is

\[
\boxed{
\begin{aligned}
&\text{DSD can type representation, map, equivalence, and readout roles explicitly;}\\
&\text{after the GR geometric/gauge structure is supplied, diffeomorphism-related}\\
&\text{representations and relational observables can be audited without conflating}\\
&\text{them with DSD strict descriptive equivalence.}
\end{aligned}
}
\]

---

## 16. Reproducibility

Script:

```text
audits/science/2026-09-10_rel_core_005_diffeomorphism_gauge_observable_equivalence_gate.py
```

Run from repository root:

```bash
python audits/science/2026-09-10_rel_core_005_diffeomorphism_gauge_observable_equivalence_gate.py --mode all
```

Dependency:

```text
Python standard library only
```

---

## 17. External standard references

- Sean M. Carroll, *Lecture Notes on General Relativity*, arXiv:gr-qc/9712019.
- Johannes Tambornino, *Relational Observables in Gravity: a Review*, arXiv:1109.0740.
- Standard differential-geometric definitions of diffeomorphism, pullback, isometry, scalar/tensor covariance, and global topology are used only as the external comparator layer.

---

## 18. Next target

Proceed to:

```text
REL Core 006 — Linearized Gravity / Gauge Perturbation / Radiative-Degree Gate
```

The next audit should separate at least:

```text
background metric vs perturbation
h_mu_nu component gauge dependence
infinitesimal diffeomorphism gauge transformation
trace reversal
Lorenz gauge
residual gauge freedom
linearized Einstein equation
vacuum wave equation
transverse-traceless specialization
Riemann/tidal radiative response
coordinate wave amplitude vs gauge-invariant physical response
DSD propagation/c_info vs relativistic gravitational-wave speed
```

The supplied GR weak-field/linearized structure must not be retroactively counted as a DSD-native gravity law or as evidence that \(c_{\rm info}=c\).
