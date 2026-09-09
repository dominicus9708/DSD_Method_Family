# REL Core 003 — Geodesic / Parallel-Transport / Curvature-Response Gate

Date: 2026-09-10  
Status: **PASS_WITH_BOUNDARY**  
Program: **Core-Theory Reconstruction Challenge — Standard Relativity Track**

## 1. Purpose

REL Core 002 separated the supplied Lorentzian metric from causal classification, time orientation, proper time, Levi-Civita connection, and curvature. REL Core 003 now audits the next standard-relativity layer:

```text
metric / Levi-Civita connection
-> covariant acceleration
-> affinely parametrized geodesic
-> parallel transport
-> curvature / holonomy response
-> geodesic deviation
```

The goal is not to derive geodesic motion from generic DSD. It is to determine exactly what follows after the standard Lorentzian/Levi-Civita package is supplied, and to prevent coordinate acceleration, DSD trajectory typing, or generic transition/lineage structure from being mistaken for the standard geodesic law.

The critical separation is

\[
\boxed{
\text{coordinate acceleration}
\neq
\text{covariant acceleration}
\neq
\text{geodesic law}
\neq
\text{parallel transport}
\neq
\text{curvature response}.
}
\]

No Einstein field equation, stress-energy source, or DSD gravity constitutive law is used in this gate.

---

## 2. Source and provenance lock

### 2.1 DSD source hierarchy

The DSD predecessor order remains

```text
Formation Axiom System
-> Property Axiom System
-> Channel-Indexed Static Aggregation
-> Structural Reorganization Dynamics
```

The current Structural Reorganization Dynamics manuscript permits a dynamic model to add time dependence, locality, constitutive operators, lineage, transition relations, propagation structure, and optional realized-axis geometry, while preserving inherited Stage-VI identity and predecessor status distinctions. The manuscript does not promote any one geometric or constitutive specialization to a universal prerequisite.

Therefore a DSD admissible trajectory or transition relation is not, merely by being a trajectory, a Levi-Civita geodesic.

### 2.2 Standard source lock

The standard differential-geometric/relativity facts used here are independently supplied. Checked references include:

```text
Sean M. Carroll,
Lecture Notes on General Relativity,
arXiv:gr-qc/9712019.

David Tong,
General Relativity lecture notes,
Sections 1 and 3 on geodesics, parallel transport,
and geodesic deviation.
https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S1.html
https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S3.html

H. S. Reall,
General Relativity lecture notes,
section on geodesics and extremal proper time.
https://www.damtp.cam.ac.uk/user/hsr1000/part3_gr_lectures.pdf
```

These are not counted as DSD-derived results.

### 2.3 Provenance classes

REL Core 001R classes remain active:

```text
R0  PRE_EXISTING_DSD
R1  GENERAL_MATHEMATICAL_STRUCTURAL
R2  RELATIVITY_SPECIALIZATION
R3  STANDARD_THEOREM_CONSEQUENCE
R4  REMAINS_EXTERNAL_NOT_DERIVED
```

Relevant placement for this gate:

```text
R0:
  typed state / property / transition / lineage roles
  explicit bridge discipline
  reconstruction and applicability discipline

R1:
  coordinate component equality is not tensorial equality
  ordinary derivative data are representation-dependent
  path-dependent maps require declared path/domain

R2:
  smooth Lorentzian metric
  Levi-Civita connection
  chosen time orientation when directed causal language is used
  worldline / initial tangent data

R3:
  covariant acceleration
  affine geodesic equation
  parallel-transport equation
  geodesic existence/uniqueness locally from smooth connection + initial data
  proper-time extremal characterization for timelike Levi-Civita geodesics
  curvature-controlled holonomy/deviation consequences

R4:
  why physical free fall must be described by this supplied connection
  why the supplied metric/connection is selected by nature
  Einstein dynamics and matter coupling
  DSD-native derivation of the geodesic principle
```

---

## 3. Coordinate acceleration is not the geodesic criterion

A geodesic with affine parameter \(\tau\) satisfies

\[
\boxed{
\frac{d^2x^\mu}{d\tau^2}
+
\Gamma^\mu{}_{\nu\rho}
\frac{dx^\nu}{d\tau}
\frac{dx^\rho}{d\tau}
=0,
}
\]

or invariantly

\[
\boxed{\nabla_u u=0.}
\]

The ordinary coordinate second derivative is not by itself invariant.

### 3.1 Exact flat-spacetime witness

Start with flat \(1+1\) Minkowski spacetime

\[
ds^2=-dt^2+dx^2.
\]

On the patch \(y>0\), set

\[
x=y^2.
\]

Then

\[
ds^2=-dt^2+4y^2dy^2,
\]

and the only nonzero Christoffel coefficient relevant here is

\[
\Gamma^y{}_{yy}=\frac1y.
\]

Take the inertial straight worldline

\[
t=\tau,
\qquad
x=x_0+v\tau.
\]

In the \(y\)-coordinate,

\[
y(\tau)=\sqrt{x_0+v\tau},
\]

so

\[
\dot y=\frac{v}{2y},
\qquad
\ddot y=-\frac{v^2}{4y^3}\neq0.
\]

Nevertheless

\[
\ddot y
+
\Gamma^y{}_{yy}\dot y^2
=
-\frac{v^2}{4y^3}
+
\frac1y\frac{v^2}{4y^2}
=0.
\]

Therefore

\[
\boxed{
\ddot y\neq0
\quad\text{while}\quad
\nabla_u u=0.
}
\]

Conversely, the coordinate curve

\[
y(\tau)=y_0+w\tau
\]

has \(\ddot y=0\) but

\[
(\nabla_u u)^y
=
\Gamma^y{}_{yy}w^2
=
\frac{w^2}{y}\neq0.
\]

Hence

\[
\boxed{
\text{zero coordinate acceleration}
\not\Rightarrow
\text{geodesic motion}.
}
\]

### Scoped outcome

```text
coordinate second derivative alone -> geodesic classification:
  REJECTED

connection + tangent + affine parameter -> covariant geodesic test:
  VALID_IN_DOMAIN
```

---

## 4. Nonzero Christoffel coefficients do not imply curvature

The same nonlinear coordinate representation of flat Minkowski spacetime has

\[
\Gamma^y{}_{yy}=1/y\neq0.
\]

Yet the underlying spacetime remains flat. In the explicit witness, the derivative and quadratic connection terms cancel:

\[
\partial_y\Gamma^y{}_{yy}
+
(\Gamma^y{}_{yy})^2
=
-\frac1{y^2}
+
\frac1{y^2}
=0.
\]

The exact tensor calculation gives vanishing Riemann curvature, as required by the coordinate transformation from Minkowski space.

Thus

\[
\boxed{
\Gamma^\mu{}_{\nu\rho}\neq0
\not\Rightarrow
R^\mu{}_{\nu\rho\sigma}\neq0.
}
\]

This reinforces REL Core 002: connection coefficients are coordinate-dependent, while curvature is the invariant obstruction measured by the Riemann tensor.

---

## 5. Proper-time extremality is conditional standard geometry, not a DSD transition rule

For a specified timelike curve \(\gamma\), proper time is

\[
\tau[\gamma]
=
\int
\sqrt{-g(u,u)}\,d\lambda.
\]

For a supplied Lorentzian metric and Levi-Civita connection, extremizing this functional yields the timelike geodesic equation under the usual variational hypotheses.

The finite Minkowski witness reuses the endpoints

\[
O=(0,0),
\qquad
P=(2,0).
\]

The straight inertial path has

\[
\tau_{\rm straight}=2,
\]

while the broken timelike path through \((1,0.6)\) has

\[
\tau_{\rm broken}
=2\sqrt{1-0.6^2}
=1.6.
\]

Therefore the straight geodesic exceeds this selected variation in proper time.

This finite witness is not promoted into the stronger false statement that every timelike geodesic is a unique global maximizer between arbitrary endpoints in arbitrary spacetimes. Global maximality requires additional global hypotheses and is obstructed by phenomena such as conjugate/cut points.

### DSD boundary

```text
DSD trajectory exists
!= trajectory extremizes proper time
!= trajectory is Levi-Civita geodesic
```

The proper-time variational principle remains an R3 consequence after the R2 metric/connection/worldline package is supplied.

---

## 6. Parallel transport requires both connection and path

For a curve with tangent \(X\), a vector \(V\) is parallel transported when

\[
\boxed{\nabla_XV=0.}
\]

In coordinates along \(x^\mu(\tau)\),

\[
\frac{dV^\mu}{d\tau}
+
\Gamma^\mu{}_{\nu\rho}
\frac{dx^\nu}{d\tau}V^\rho
=0.
\]

Thus a connection alone does not define an endpoint-to-endpoint vector comparison without a path.

### 6.1 Exact curved Lorentzian path-dependence witness

Use

\[
g=e^{2\phi(x)}(-dt^2+dx^2),
\qquad
\phi(x)=bx^2.
\]

The relevant connection matrices for vector transport are

\[
A_x=\phi'(x)I,
\qquad
A_t=\phi'(x)\sigma_x.
\]

Compare two paths from \((0,0)\) to \((T,L)\):

```text
Path A: x first, then t
Path B: t first, then x
```

Since \(\phi'(0)=0\) and \(\phi'(L)=2bL\), the two transport maps differ by

\[
\exp[-2bLT\,\sigma_x].
\]

For \(bLT\neq0\), this is not the identity.

Hence

\[
\boxed{
\text{same endpoints + same connection}
\not\Rightarrow
\text{same parallel-transport result}.
}
\]

### 6.2 Closed-loop holonomy

Transport around the corresponding rectangle returns to the starting point with holonomy

\[
H_\square
=
\exp[-2bLT\,\sigma_x],
\]

which is nontrivial when \(b\neq0\). For \(b=0\), the same construction is the identity.

At \(x=0\), under the convention used in REL Core 002,

\[
R=-4b.
\]

The witness therefore explicitly connects nonzero curvature with nontrivial small-loop transport response in this model without identifying the numerical holonomy parameter with a new DSD invariant.

---

## 7. Geodesic deviation is relative acceleration, not ordinary coordinate acceleration

For a one-parameter family of affinely parametrized geodesics with tangent \(u\) and deviation vector \(S\), the standard Jacobi/geodesic-deviation equation is, in the convention used here,

\[
\boxed{
\frac{D^2S^\mu}{D\tau^2}
=
R^\mu{}_{\nu\rho\sigma}
 u^\nu u^\rho S^\sigma.
}
\]

The overall component sign depends on Riemann-tensor convention; the structural content is convention-independent once one convention is fixed.

### 7.1 Exact \(1+1\) FLRW-type witness

Take

\[
ds^2=-dt^2+a(t)^2dx^2,
\qquad
a(t)=1+kt^2.
\]

Comoving worldlines \(x=\text{const}\) are timelike geodesics. For a neighboring comoving geodesic with coordinate separation \(S^x=\Delta x\),

\[
\frac{D^2S^x}{Dt^2}
=
\frac{\ddot a}{a}S^x.
\]

Under the chosen Riemann convention,

\[
R^x{}_{ttx}=\frac{\ddot a}{a},
\]

so the deviation equation is satisfied exactly:

\[
\frac{D^2S^x}{Dt^2}
=
R^x{}_{ttx}S^x.
\]

Meanwhile every comoving curve has

\[
\frac{d^2x}{dt^2}=0,
\]

while its physical separation from a neighboring comoving geodesic is

\[
\ell(t)=a(t)\Delta x,
\qquad
\ddot\ell=\ddot a\,\Delta x.
\]

Thus

\[
\boxed{
\text{zero individual coordinate acceleration}
\not\Rightarrow
\text{zero relative tidal acceleration}.
}
\]

This is exactly the role for which curvature, rather than Christoffel coefficients alone, is the relevant standard-relativity object.

---

## 8. Reconstruction and applicability ladder

The gate supports the following target-relative requirements:

```text
TARGET: affinely parametrized geodesic test
  retain:
    curve / tangent data
    affine parameter
    connection along the curve
  insufficient:
    coordinate second derivative alone

TARGET: parallel transport
  retain:
    path
    connection along the path
    initial transported tensor/vector
  insufficient:
    endpoints alone

TARGET: closed-loop holonomy
  retain:
    connection over the loop neighborhood
    loop identity/orientation
  insufficient:
    one point connection coefficient

TARGET: geodesic deviation
  retain:
    geodesic congruence or neighboring family
    deviation vector
    curvature along the reference geodesic
    affine/proper-time parameterization as applicable
  insufficient:
    one geodesic coordinate acceleration alone
```

Therefore

\[
\boxed{
\text{describability of a trajectory}
\not\Rightarrow
\text{describability of its geodesic/transport/curvature-response role}
}
\]

without the required typed geometric inputs.

---

## 9. DSD placement

A conservative placement is:

```text
Formation
  identity of spacetime model, curve, endpoint and comparison objects

Property
  metric, tangent, connection, curvature, orientation,
  acceleration and proper-time records when applicable/defined

Static Aggregation
  optional path/readout summaries;
  no aggregate is presumed to reconstruct full path or connection

Dynamics
  admissible trajectories, transition relations and lineage
  only after a constitutive/evolution rule is supplied

Relativity specialization
  Lorentzian metric
  Levi-Civita connection
  geodesic/autoparallel equation
  parallel transport
  Jacobi/geodesic-deviation equation
```

The current DSD Dynamics architecture explicitly permits optional geometry and supplied constitutive operators while refusing to promote one specialization to a universal prerequisite. This is exactly the firewall needed here.

---

## 10. Rejected shortcuts

The following are rejected:

\[
\ddot x^\mu=0
\not\Rightarrow
\nabla_u u=0,
\]

\[
\ddot x^\mu\neq0
\not\Rightarrow
\nabla_u u\neq0,
\]

\[
\Gamma\neq0
\not\Rightarrow
R\neq0,
\]

\[
\text{same endpoints}
\not\Rightarrow
\text{same parallel transport},
\]

\[
\text{geodesic}
\not\Rightarrow
\text{global proper-time maximum in every spacetime},
\]

\[
\text{zero coordinate acceleration}
\not\Rightarrow
\text{zero geodesic deviation},
\]

and

\[
\text{DSD admissible trajectory/lineage}
\not\Rightarrow
\text{Levi-Civita geodesic dynamics}.
\]

---

## 11. DSD core impact

No revision of the four current core papers is required.

The existing architecture already separates:

```text
static/property geometry
from
constitutive dynamics,

instantaneous state
from
trajectory/transition,

optional geometric specialization
from
generic DSD prerequisites,

reduced readout
from
reconstructive completeness.
```

The refinement belongs in the relativity methodology interface.

---

## 12. Verdict

\[
\boxed{\textbf{PASS\_WITH\_BOUNDARY}}
\]

More precisely:

```text
coordinate acceleration usable as invariant geodesic criterion: NO
covariant acceleration / affine geodesic test after connection supply: YES
nonzero Christoffel coefficient implies curvature: NO
proper-time extremal witness in Minkowski: PASS
proper-time extremal theorem counted as generic DSD dynamics: NO
parallel transport requires path + connection: YES
curved conformal witness exhibits path dependence/holonomy: YES
geodesic deviation matches curvature response in FLRW witness: YES
DSD trajectory/lineage implies geodesic motion: NO
DSD core contradiction found: NO
DSD core revision required: NO
```

The strongest safe conclusion is

\[
\boxed{
\text{after a standard Lorentzian metric and Levi-Civita connection are supplied,}
\text{ geodesic, transport, holonomy and deviation structures can be typed and audited in DSD,}
}
\]

while the selection of that physical geometry and the geodesic principle remain external to generic DSD.

---

## 13. Reproducibility

Script:

```text
audits/science/2026-09-10_rel_core_003_geodesic_parallel_transport_curvature_response_gate.py
```

Run from repository root:

```bash
python audits/science/2026-09-10_rel_core_003_geodesic_parallel_transport_curvature_response_gate.py --mode all
```

Dependency:

```text
Python standard library only
```

Observed result:

```text
OVERALL: PASS_WITH_BOUNDARY
```

The script checks 23 explicit predicates/witnesses grouped under:

```text
coordinate vs covariant acceleration
proper-time selected-variation witness
parallel transport / closed-loop holonomy
geodesic deviation
DSD reconstruction/provenance role firewall
```

---

## 14. Next target

Proceed to:

```text
REL Core 004 — Einstein Field Equation / Constraint / Conservation / Initial-Value Gate
```

The next audit should separate at least:

```text
metric kinematics
Einstein tensor
stress-energy tensor
field-equation satisfaction
contracted Bianchi identity
covariant conservation
constraint equations
initial data
maximal globally hyperbolic development
matter-model closure
boundary/asymptotic data
DSD constitutive bridge
```

The key question will be whether relation satisfaction and initial-value development can be reconstructed without silently turning a typed metric/state record into the Einstein dynamical law itself.
