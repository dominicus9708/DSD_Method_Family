# REL Core 002 — Lorentzian Metric / Causal Geometry Admission and Reconstruction Gate

Date: 2026-09-10  
Status: **PASS_WITH_BOUNDARY**  
Program: **Core-Theory Reconstruction Challenge — Standard Relativity Track**

## 1. Purpose

REL Core 001R established that the ordinary standard-relativity package is not to be counted as a generic DSD derivation. REL Core 002 now opens the first supplied package and asks which later structures are fixed once a Lorentzian metric is supplied, which need additional choices, and which reduced records fail to reconstruct stronger geometric targets.

The dependency chain audited here is

```text
smooth manifold
-> Lorentzian metric
-> tangent causal class
-> time orientation
-> directed causal curves / causal relations
-> proper time on a timelike curve
-> Levi-Civita connection
-> curvature
```

The arrows are not all of the same logical type.

The gate therefore tests the distinction

\[
\boxed{
\text{carrier admission}
\neq
\text{metric supply}
\neq
\text{causal classification}
\neq
\text{orientation choice}
\neq
\text{curve functional}
\neq
\text{connection}
\neq
\text{curvature}
}.
\]

No Einstein field equation, matter source, quantum-gravity premise, or DSD gravity law is used.

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

The Property Axiom System places tensor/operator/geometric representations downstream of the abstract property core. Channel-Indexed Static Aggregation treats analytic realizations and bridges as additional downstream data and separately records reconstruction loss under reduced outputs. Structural Reorganization Dynamics permits optional geometric specializations but does not silently alter inherited formation identity or derive a unique physical constitutive law.

Therefore the existence of a DSD typed record capable of storing a metric is not evidence that the Lorentzian metric was derived by DSD.

### 2.2 Standard-relativity source lock

The standard mathematical/relativity facts used here are independently supplied. The main references checked for this stage are:

```text
Sean M. Carroll,
Lecture Notes on General Relativity,
arXiv:gr-qc/9712019.

David Tong,
General Relativity lecture notes,
sections on Lorentzian manifolds, causal vectors,
proper time, Levi-Civita connection, normal coordinates and curvature.

Claude Warnick,
Introduction to Mathematical Relativity,
section on the metric and causal geometry.

H. S. Reall,
General Relativity lecture notes,
section on the Levi-Civita connection.
```

The standard source structure supports the following separation:

```text
Lorentzian metric supplied
-> timelike/null/spacelike classification at a tangent space

time-orientability + a chosen time orientation
-> future/past labeling

timelike curve + metric along the curve
-> proper-time functional

smooth metric field
-> unique torsion-free metric-compatible Levi-Civita connection

connection / metric derivatives
-> curvature
```

---

## 3. Provenance classification for this gate

Use the REL Core 001R classes:

```text
R0  PRE_EXISTING_DSD
R1  GENERAL_MATHEMATICAL_STRUCTURAL
R2  RELATIVITY_SPECIALIZATION
R3  STANDARD_THEOREM_CONSEQUENCE
R4  REMAINS_EXTERNAL_NOT_DERIVED
```

### R0 — pre-existing DSD

```text
typed status / applicability
explicit bridge discipline
representation vs source separation
readout / reconstruction discipline
state / relation / transition separation
strict-equivalence firewall
```

### R1 — target-independent structural facts

```text
same carrier can support different additional structures
reconstruction requires fiber constancy / sufficient retained data
a reduced record can answer one query while failing a stronger query
pointwise equality does not imply equality of derivatives or global fields
```

### R2 — supplied relativity package at this stage

```text
smooth spacetime manifold M
spacetime dimension n
smooth nondegenerate Lorentzian metric g of chosen signature convention
time-orientability when needed
a chosen time orientation when directed causal language is used
specified curve when proper time is queried
```

### R3 — standard consequences under the supplied hypotheses

```text
g_p(v,v) sign -> tangent causal class
metric + chosen time orientation -> future/past-directed causal vectors
timelike curve + metric -> proper time
smooth pseudo-Riemannian metric -> unique Levi-Civita connection
Levi-Civita connection / metric derivatives -> curvature
```

### R4 — not independently derived here

```text
why spacetime is Lorentzian rather than Riemannian or another signature
why the physical dimension is four
which Lorentzian metric nature realizes
which time orientation is physically selected
Einstein dynamics selecting/evolving the metric
matter/source content
boundary/topology/initial data
identification of relativistic c with DSD c_info
```

The central boundary is therefore

\[
\boxed{
\text{DSD can type a Lorentzian metric record}
\not\Rightarrow
\text{DSD selects the Lorentzian metric of nature}.
}
\]

---

## 4. Metric admission is not supplied by the smooth manifold alone

Take the same smooth carrier \(M=\mathbb R^2\) and compare the diagonal bilinear forms

\[
\eta=\operatorname{diag}(-1,+1),
\qquad
h=\operatorname{diag}(+1,+1).
\]

The first has Lorentzian signature \((-+ )\). The second is positive definite.

Thus the smooth manifold carrier does not by itself choose the causal metric structure.

A DSD formation or property carrier may retain either representation after an explicit specialization, but the choice of Lorentzian signature is R2 data rather than R0/R1 output.

### Scoped outcome

```text
smooth manifold -> unique Lorentzian metric:
  REJECTED

supplied Lorentzian metric -> admissible causal quadratic form:
  VALID_IN_DOMAIN
```

---

## 5. Tangent causal class is metric-relative

For a nonzero tangent vector \(v\), using signature \((-+)\), standard causal classification is

\[
g(v,v)<0 \Rightarrow \text{timelike},
\]

\[
g(v,v)=0 \Rightarrow \text{null},
\]

\[
g(v,v)>0 \Rightarrow \text{spacelike}.
\]

Use on the same \(\mathbb R^2\) carrier

\[
g_1=\operatorname{diag}(-1,+1),
\qquad
g_2=\operatorname{diag}(-4,+1),
\]

and

\[
v=(1,3/2).
\]

Then

\[
g_1(v,v)=\frac54>0,
\qquad
g_2(v,v)=-\frac74<0.
\]

Hence the same tangent vector is spacelike for \(g_1\) and timelike for \(g_2\).

Likewise \((1,1)\) is null for \(g_1\) but timelike for \(g_2\).

Therefore

\[
\boxed{
\text{manifold point + tangent vector}
\not\Rightarrow
\text{causal class}
}
\]

without the metric.

Conversely, once \(g_p\) is supplied, the sign of \(g_p(v,v)\) is sufficient for the local tangent causal class.

### Reconstruction classification

```text
point metric g_p + tangent vector v_p -> local tangent causal class:
  VALID_IN_DOMAIN

carrier/vector alone -> tangent causal class:
  NOT_SUFFICIENT_FOR_EXTENSION
```

---

## 6. Time orientation is not the same datum as the Lorentzian metric

A Lorentzian metric determines the two connected timelike cone components locally, but it does not by itself label one component `future` and the other `past`.

On Minkowski \(\eta\), both

\[
T_+=(1,0),
\qquad
T_-=(-1,0)
\]

are timelike.

With the conventional future-directed test

\[
g(v,T)<0,
\]

the vector \(v=(1,0)\) is future-directed relative to \(T_+\), while reversing the orientation field to \(T_-\) reverses that label.

Thus

\[
\boxed{
\text{causal cone}
\neq
\text{chosen future/past orientation}.
}
\]

The existence of a global time orientation is itself a property of the Lorentzian manifold. When it exists, the physical/mathematical choice of one orientation remains extra data for directed causal language.

### Scoped outcome

```text
Lorentzian metric -> local timelike cone components:
  VALID_IN_DOMAIN

Lorentzian metric alone -> unique future direction:
  REJECTED

metric + chosen time orientation -> future/past-directed classification:
  VALID_IN_DOMAIN
```

---

## 7. Proper time requires a curve, not merely endpoints or a coordinate interval

For a timelike curve \(\gamma\), in units \(c=1\), proper time is

\[
\tau[\gamma]
=
\int
\sqrt{-g_{\mu\nu}\dot x^\mu\dot x^\nu}
\,d\lambda.
\]

### 7.1 Same coordinate curve, different metric

For \(\gamma(t)=(t,0)\), \(t\in[0,1]\),

\[
\tau_{g_1}=1,
\qquad
\tau_{g_2}=2.
\]

The coordinate curve has not changed; the supplied metric has.

### 7.2 Same endpoints, different timelike path

In \(1+1\) Minkowski spacetime use endpoints

\[
O=(0,0),
\qquad P=(2,0).
\]

The straight path has

\[
\tau_{\rm straight}=2.
\]

The piecewise-linear path through \((1,0.6)\) has two timelike segments, each with proper time

\[
\sqrt{1-0.6^2}=0.8,
\]

so

\[
\tau_{\rm broken}=1.6.
\]

Therefore

\[
\boxed{
\text{endpoints}
\not\Rightarrow
\text{proper time}
}
\]

without specifying the curve or an additional extremal/geodesic condition.

### DSD consequence

Keep distinct:

```text
coordinate endpoints
coordinate parameter interval
curve identity / tangent data
metric along the curve
timelike applicability
proper-time readout
```

---

## 8. Pointwise metric value does not reconstruct the Levi-Civita connection

The standard Levi-Civita theorem gives a unique torsion-free metric-compatible connection for a supplied smooth pseudo-Riemannian metric field.

This uniqueness is a theorem **relative to the full metric field**, not a statement that the metric value at one point contains its own derivatives.

Use the Lorentzian conformal family

\[
g_a=e^{2ax}(-dt^2+dx^2).
\]

At the origin,

\[
g_a(0)=\eta
\]

for every \(a\).

But

\[
\Gamma^x{}_{tt}(0)=a.
\]

Hence \(a=0\) and \(a=1/2\) have the same pointwise metric value while their Levi-Civita coefficients at the origin differ.

Therefore

\[
\boxed{g_p\text{ alone does not reconstruct }\nabla_p.}
\]

A local metric germ carrying the required first-derivative data does determine the Levi-Civita connection through the standard theorem/formula.

### Scoped outcome

```text
full smooth metric field -> unique Levi-Civita connection:
  VALID_IN_DOMAIN

metric value at one point -> Levi-Civita connection at that point:
  NOT_SUFFICIENT_FOR_EXTENSION
```

---

## 9. Metric plus first derivatives at a point do not reconstruct curvature there

Use

\[
g_b=e^{2bx^2}(-dt^2+dx^2).
\]

At \((t,x)=(0,0)\), for every \(b\),

\[
g_b(0)=\eta,
\qquad
\partial g_b(0)=0,
\qquad
\Gamma[g_b](0)=0.
\]

Under the Riemann-sign convention used by the reproducibility script,

\[
R^\rho{}_{\sigma\mu\nu}
=
\partial_\mu\Gamma^\rho{}_{\nu\sigma}
-
\partial_\nu\Gamma^\rho{}_{\mu\sigma}
+
\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}
-
\Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma},
\]

the scalar curvature is

\[
R=-4b e^{-2bx^2},
\]

so at the origin

\[
R(0)=-4b.
\]

For \(b=0\) and \(b=1/4\),

\[
R_0(0)=0,
\qquad
R_{1/4}(0)=-1.
\]

Thus the two metrics agree in value and first derivative at the point and have identical Christoffel symbols there, yet have different curvature.

This is the Lorentzian counterpart of the already-used normal-coordinate warning:

\[
\boxed{
\text{connection can vanish at a point in a coordinate system}
\not\Rightarrow
\text{curvature vanishes there}.
}
\]

### Scoped outcome

```text
metric + first derivative at one point -> curvature at that point:
  NOT_SUFFICIENT_FOR_EXTENSION

sufficient metric second-order germ / connection-derivative data -> curvature:
  VALID_IN_DOMAIN
```

---

## 10. Reconstruction ladder

The gate supports the following target-relative ladder:

```text
TARGET: tangent causal class at p
  retain: g_p and v_p
  status: sufficient

TARGET: future/past label
  retain: g_p, v_p, chosen time orientation
  status: metric alone insufficient

TARGET: proper time
  retain: metric along specified timelike curve + curve tangent data
  status: endpoints alone insufficient

TARGET: Levi-Civita connection at p
  retain: sufficient first-order metric germ
  status: g_p alone insufficient

TARGET: curvature at p
  retain: sufficient second-order metric germ / connection derivative data
  status: g_p + first derivatives alone insufficient
```

Therefore `the metric` must not be treated as one undifferentiated scalar record. The amount of retained metric data needed is query-dependent.

This is an instance of the established DSD/common-method rule:

\[
\boxed{
\text{completeness is relative to the declared target/query.}
}
\]

---

## 11. DSD placement

A conservative DSD placement is:

```text
Formation
  identity of the represented spacetime/model/curve records

Property
  typed metric, tangent-vector, orientation, connection,
  curvature and proper-time records when supplied/defined

Static Aggregation
  optional reduced geometric readouts;
  reconstruction claims require retained support/injectivity

Dynamics
  only when worldline evolution, geodesic motion,
  transport, or metric evolution is separately supplied

Relativity specialization
  smooth manifold
  Lorentzian signature/metric
  time orientation
  standard differential-geometric definitions/theorems
```

No coordinate is padded with a value when a geometric object is absent or undefined. This follows the current DSD status discipline.

---

## 12. Rejected shortcuts

The following shortcuts are rejected:

\[
\text{smooth manifold}
\not\Rightarrow
\text{Lorentzian metric},
\]

\[
\text{Lorentzian metric}
\not\Rightarrow
\text{unique future orientation},
\]

\[
\text{endpoints}
\not\Rightarrow
\text{proper time},
\]

\[
g_p
\not\Rightarrow
\nabla_p,
\]

\[
(g_p,\partial g_p)
\not\Rightarrow
R_p,
\]

and

\[
\text{DSD geometric representation}
\not\Rightarrow
\text{DSD derivation of relativistic geometry}.
\]

---

## 13. DSD core impact

No revision of the Formation Axiom System, Property Axiom System, Channel-Indexed Static Aggregation, or Structural Reorganization Dynamics is required.

The current papers already permit the needed separation:

```text
abstract property core != optional geometric representation
static reduced output != guaranteed reconstruction
instantaneous state != constitutive dynamic law
optional geometric specialization != generic DSD prerequisite
```

The refinement belongs in the relativity methodology interface.

---

## 14. Verdict

\[
\boxed{\textbf{PASS\_WITH\_BOUNDARY}}
\]

More precisely:

```text
Lorentzian metric storable/typable in DSD: YES
Lorentzian metric independently selected by generic DSD: NO
local causal class reconstructible from point metric + vector: YES
future/past orientation reconstructible from metric alone: NO
proper time reconstructible from endpoints alone: NO
Levi-Civita connection determined by full smooth metric: YES
Levi-Civita connection determined by point metric alone: NO
curvature determined by metric + first derivatives at one point: NO
DSD core contradiction found: NO
DSD core revision required: NO
```

The strongest safe conclusion is

\[
\boxed{
\text{once Lorentzian metric data are supplied at the required resolution,}
\text{ standard causal and differential geometry can be represented and audited in DSD,}
}
\]

while the physical selection of that Lorentzian geometry remains external.

---

## 15. Reproducibility

Script:

```text
audits/science/2026-09-10_rel_core_002_lorentzian_metric_causal_geometry_gate.py
```

Run from repository root:

```bash
python audits/science/2026-09-10_rel_core_002_lorentzian_metric_causal_geometry_gate.py --mode all
```

Dependency:

```text
Python standard library only
```

Observed result:

```text
OVERALL: PASS_WITH_BOUNDARY
```

The script checks:

```text
Lorentzian vs Euclidean signature
metric-relative causal classification
time-orientation reversal
proper-time metric dependence
same-endpoint / different-curve proper time
same point metric / different Levi-Civita coefficients
same metric + first derivative / different curvature
reconstruction ladder status
```

---

## 16. Next target

Proceed to:

```text
REL Core 003 — Geodesic / Parallel-Transport / Curvature-Response Gate
```

The next audit should separate at least:

```text
coordinate acceleration
covariant acceleration
geodesic/autoparallel equation
proper-time extremal statement
parallel transport
connection coefficients
curvature / holonomy response
geodesic deviation
DSD transition/lineage roles
```

The standard geodesic and curvature-response laws remain R3 consequences of supplied R2 geometry; they must not be retroactively counted as a DSD-derived dynamics.
