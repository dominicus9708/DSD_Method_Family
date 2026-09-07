# PHY-REL-006 — Configuration-State Audit of Cauchy Data, Domain of Dependence, and Reconstruction

Date: 2026-09-08
Status: **PASS_WITH_REFINEMENT**
Track: **2 — Full DSD structural analysis of standard quantum mechanics and relativity**

## 1. Purpose

This audit tests the fourth detailed Track-2 target:

```text
Relativity
  Cauchy / initial data
  completeness of one-slice data
  explicit evolution relation
  domain of dependence
  local determination
  global reconstruction
  geometric uniqueness boundary
```

The target distinction is

\[
\boxed{
\text{one-slice state}
\neq
\text{evolution law}
\neq
\text{domain of dependence}
\neq
\text{global reconstruction}
}.
\]

The question is whether the current DSD comparison-state interface can represent a standard relativistic Cauchy problem without silently turning the field equations into state coordinates or treating domain-limited determination as global completeness.

No quantum-gravity candidate or alternative-gravity premise is used.

---

## 2. Standard-theory source lock

### 2.1 Hyperbolic comparator

The finite reproducibility witness uses the standard 1+1 wave equation with units \(c=1\),

\[
\partial_t^2u-\partial_x^2u=0,
\]

with Cauchy data

\[
f(x)=u(0,x),
\qquad
g(x)=\partial_tu(0,x).
\]

The d'Alembert formula is

\[
u(t,x)
=\frac12\bigl[f(x-t)+f(x+t)\bigr]
+\frac12\int_{x-t}^{x+t}g(s)\,ds.
\]

This comparator is standard hyperbolic PDE mathematics. Waldmann, *Geometric Wave Equations* (arXiv:1208.4706), treats Cauchy problems for normally hyperbolic operators on globally hyperbolic manifolds.

### 2.2 General-relativity boundary

For full general relativity, the relevant standard result is the Choquet-Bruhat–Geroch Cauchy-development theorem: constraint-satisfying Einstein initial data admit a maximal globally hyperbolic development, with the standard geometric uniqueness statement. Original reference:

```text
Y. Choquet-Bruhat and R. Geroch,
Global aspects of the Cauchy problem in general relativity,
Communications in Mathematical Physics 14 (1969), 329–335.
DOI: 10.1007/BF01645389
```

This audit does not reproduce that theorem computationally. It uses it only to lock the standard-GR placement of Cauchy data, constraints, field equations, and geometric development.

### 2.3 DSD interface lock

The audit-level comparison state remains

\[
\Sigma_{R,t}
=(F_{R,t},P_{R,t},R_{R,t},A_{R,t},\Phi_{R,t}),
\]

where these entries are comparison roles rather than new DSD core coordinates.

The standard field equation, constraint equations, gauge conditions, and well-posedness assumptions remain explicit external standard-domain relations. They are not absorbed into \(\Sigma_{R,t}\) merely to force closure.

The DSD Structural Reorganization Dynamics paper already requires supplied dynamic laws/constitutive bridges and treats hyperbolic realizations conditionally rather than deriving a unique equation from DSD itself. The same restraint is preserved here.

---

## 3. A Cauchy state requires the data needed by the locked evolution problem

In the wave comparator, \(f\) alone is not complete Cauchy data. Both

\[
(f,g)
\]

are required.

The script compares

```text
Data A:
  f = 0
  g = 0

Data B:
  f = 0
  g = 1 on [-1,1], 0 elsewhere
```

at the target

\[
(t,x)=(0.5,0).
\]

The d'Alembert formula gives

\[
u_A(0.5,0)=0,
\qquad
u_B(0.5,0)=0.5.
\]

Thus the same initial field value \(f\) with different initial velocity \(g\) produces different future solutions.

### Scoped outcomes

```text
complete pair (f,g) for the locked wave Cauchy problem:
  VALID_IN_DOMAIN

field value f alone -> unique future wave solution:
  NOT_SUFFICIENT_FOR_EXTENSION
```

This is not a failure of \(f\) as an instantaneous field record. It is a failure of the stronger claim that \(f\) alone is a complete Cauchy state for this second-order equation.

---

## 4. One-slice data do not determine a future without an evolution relation

Take the same one-slice data

\[
u(0,x)=0,
\qquad
\partial_tu(0,x)=0.
\]

The standard wave solution

\[
u_{\rm wave}(t,x)=0
\]

shares those data with the alternative continuation

\[
u_{\rm alt}(t,x)=t^2.
\]

But

\[
\partial_t^2u_{\rm alt}-\partial_x^2u_{\rm alt}=2\neq0.
\]

Therefore the initial state alone does not select the standard future. The wave equation is required as an additional relation.

### Scoped outcomes

```text
one-slice data without an evolution relation -> unique continuation:
  REJECTED

standard wave relation + complete admissible Cauchy data:
  VALID_IN_DOMAIN for the stated comparator
```

### DSD interpretation

This directly supports the current layered form

\[
\boxed{
\Sigma_t
+\text{ explicit standard-domain relation}
+\Gamma_{t\to t'}
}
\]

where the middle term is an audit-level placeholder for independently locked domain equations/constraints, not a new permanent DSD core object.

The important point is

\[
\boxed{
\text{state content}
\not\Rightarrow
\text{law of evolution}
}
\]

without an explicit relation.

---

## 5. Domain of dependence gives target-relative completeness

For the unit-speed 1+1 wave equation, the value at \((t,x)\) depends only on initial data in

\[
[x-t,x+t].
\]

Let the initial interval be

\[
I=[-2,2].
\]

Then the future domain determined entirely by data on \(I\) is the diamond

\[
D^+(I)
=\{(t,x):t\ge0,\ x-t\ge-2,\ x+t\le2\}.
\]

Construct two globally distinct initial data sets:

```text
A:
  f_A = 0 everywhere
  g_A = 0 everywhere

B:
  f_B = compact triangular bump supported on [3,5]
  g_B = 0 everywhere
```

They agree exactly on \(I\) but differ globally.

The script evaluates the two solutions at the sampled points

```text
(0.0, 0.0)
(0.5, 0.0)
(1.0, 0.0)
(1.0, 0.5)
(1.5, 0.0)
(0.5, 1.0)
```

all lying in \(D^+(I)\), and obtains equal values for both data sets at every sample.

Outside that dependence domain, at

\[
(t,x)=(0.5,4),
\]

the solutions differ:

\[
u_A(0.5,4)=0,
\qquad
u_B(0.5,4)=0.5.
\]

### Scoped outcomes

```text
initial data on I -> solution on D^+(I) under the locked wave equation:
  VALID_IN_DOMAIN

determination on D^+(I) -> determination of the full global solution:
  NOT_SUFFICIENT_FOR_EXTENSION

global reconstruction from I-only data:
  RECONSTRUCTION_LOSS relative to the global target
```

The exact theorem is the domain-of-dependence property of the hyperbolic equation. The sampled diamond is only a finite reproducibility witness of that theorem.

---

## 6. Reconstruction is target-relative, not absolute

The same restricted data can be simultaneously

```text
complete for one target domain,
incomplete for a larger target domain.
```

Thus the correct distinction is

\[
\boxed{
\text{Cauchy completeness for }D^+(I)
\neq
\text{global reconstruction completeness}
}.
\]

This extends the refinements already found in Track 2:

```text
PHY-QM-050:
  configuration completeness is relative to declared system boundary.

PHY-QM-051:
  completeness is also relative to the target/query family.

PHY-REL-005:
  representation completeness != access completeness != global reconstruction completeness.

PHY-REL-006:
  dynamical determination completeness is additionally relative to
  supplied Cauchy data + evolution relation + target dependence domain.
```

A more complete audit-level statement is therefore

\[
\boxed{
\text{completeness}
=\text{relative to declared carrier, query, supplied relation, and target domain}
}
\]

for the standard-theory comparison interface.

This is a reporting/analysis refinement, not a new DSD axiom.

---

## 7. General relativity placement

The wave comparator prevents the audit from confusing several roles. The same distinctions transfer structurally to standard GR, but the physical/mathematical content remains supplied by GR itself.

A conservative placement is:

```text
ONE-SLICE STATE:
  chosen Cauchy hypersurface + admissible initial geometric/matter data

STANDARD-DOMAIN RELATIONS:
  Einstein equations
  constraint equations
  gauge / regularity structure where required

TRANSITION / DEVELOPMENT:
  standard Cauchy evolution under the locked equations

DOMAIN:
  domain of dependence / globally hyperbolic development

RECONSTRUCTION / UNIQUENESS:
  standard geometric uniqueness statement of the Cauchy development
```

Important boundary:

```text
standard-GR geometric uniqueness
!= DSD strict formation/property equivalence by default
```

No identification is made here. Comparison between standard relativistic equivalence/invariance and DSD strict equivalence remains a separate roadmap task requiring explicit maps.

---

## 8. Relation to DSD dynamics and static reconstruction discipline

The result is consistent with the current DSD source layers.

Structural Reorganization Dynamics is component-resolved and time-indexed, requires supplied dynamic laws/bridges, and uses standard hyperbolic mathematics only conditionally under well-posedness and finite-propagation assumptions. It explicitly does not select a unique evolution equation from the DSD core.

Channel-Indexed Static Aggregation separately records that reduced outputs need not reconstruct their source without injectivity/support-retaining information.

PHY-REL-006 adds a standard-relativity comparator showing that reconstruction limits arise not only from static reduction but also from the declared target domain of a well-posed dynamical problem.

These are different mechanisms and must not be merged:

\[
\boxed{
\text{static noninjective reduction}
\neq
\text{domain-limited dynamical determination}
}
\]

although both can produce a stronger-target reconstruction obstruction.

---

## 9. Status classification

### Mathematical / structural theorem layer

- d'Alembert's formula for the stated 1+1 wave problem;
- the solution at \((t,x)\) depends only on initial data on \([x-t,x+t]\);
- one-slice data without an evolution equation do not determine a unique arbitrary continuation.

### Finite / toy witness layer

- same \(f\), different \(g\), different future value;
- two global initial data sets agreeing on \([-2,2]\), identical values on sampled points of \(D^+([-2,2])\), different value outside;
- explicit non-wave continuation \(u=t^2\) with the same zero initial pair.

### Conditional standard-physics / GR layer

- constraint-satisfying Einstein initial data and the Einstein equations admit the standard maximal globally hyperbolic Cauchy-development result under its theorem assumptions;
- this theorem remains an external GR result and is not derived by DSD.

### Unresolved / not established

- no new Einstein evolution law is derived;
- no DSD causal cone is derived;
- no identification of relativistic \(c\) with \(c_{info}\) is made;
- no quantum-gravity conclusion follows;
- no equivalence between standard-GR geometric uniqueness and DSD strict equivalence is asserted;
- no claim is made that every DSD dynamical realization is hyperbolic or well posed.

---

## 10. Scoped outcome ledger

```text
complete Cauchy pair for locked wave problem:
  VALID_IN_DOMAIN

field value alone -> complete second-order Cauchy state:
  NOT_SUFFICIENT_FOR_EXTENSION

one-slice state without evolution relation -> unique future:
  REJECTED

interval data -> its standard domain of dependence:
  VALID_IN_DOMAIN

domain-limited determination -> global determination:
  NOT_SUFFICIENT_FOR_EXTENSION

global reconstruction from restricted initial domain:
  RECONSTRUCTION_LOSS

standard-GR geometric equivalence = DSD strict equivalence:
  NON_IDENTICAL / not mapped in this audit
```

No standard wave or GR object tested here is labeled `FAIL` merely for having a restricted domain of validity.

---

## 11. DSD core impact

No revision of the Formation Axiom System, Property Axiom System, Channel-Indexed Static Aggregation, or Structural Reorganization Dynamics is required by this audit.

The result reinforces the current separation:

\[
\boxed{
\text{state}
\neq
\text{domain relation / field equation}
\neq
\text{transition}
\neq
\text{reconstruction target}
}
\]

and adds the refinement that a state can be dynamically complete only relative to a declared evolution problem and target dependence domain.

---

## 12. Verdict

\[
\boxed{\textbf{PASS\_WITH\_REFINEMENT}}
\]

The DSD comparison-state architecture survives the Cauchy/domain-of-dependence audit. The strongest refinement is:

\[
\boxed{
\text{one-slice data become predictive only relative to an explicit standard evolution relation,}
}
\]

and even then the resulting completeness is domain-relative rather than automatically global.

---

## 13. Reproducibility

Script:

```text
audits/science/2026-09-08_rel_cauchy_domain_reconstruction.py
```

Run from repository root:

```bash
python audits/science/2026-09-08_rel_cauchy_domain_reconstruction.py --mode all
```

Dependency:

```text
Python standard library only
```

---

## 14. Next target

Proceed to the fifth detailed Track-2 target:

```text
Standard-domain relation layer
  symmetry
  curvature
  Einstein equation
  conservation
```

The next audit should test which structures belong to a one-slice state and which are irreducibly relations among states, derivatives, geometric fields, or trajectories. It should also keep standard relativistic geometric equivalence distinct from DSD strict equivalence until an explicit comparison map is supplied.
