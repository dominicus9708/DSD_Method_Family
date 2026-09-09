# REL Core 001R — Integrated Standard-Relativity Rebaseline / Provenance Gate

Date: 2026-09-10  
Status: **PASS_WITH_BOUNDARY**  
Program: **Core-Theory Reconstruction Challenge — Standard Relativity Track**

## 1. Purpose

The relativity track already contains PHY-REL-001 through PHY-REL-007. This gate does not restart that work. It reclassifies the existing results under the provenance discipline used to close QM Core 009.

The central question is:

> Which relativity-facing structures were already supplied by generic DSD, which are target-independent mathematical/structural consequences, which are supplied standard-relativity structure, which then follow by standard theorems, and which remain external or not independently derived?

The gate is deliberately conservative. A successful DSD re-description of a relativistic object is not counted as a derivation of that object.

---

## 2. Source hierarchy

The DSD source order is locked as:

```text
Formation Axiom System
-> Property Axiom System
-> Channel-Indexed Static Aggregation
-> Structural Reorganization Dynamics
```

The standard-relativity comparison corpus reused here is:

```text
PHY-REL-001  coordinate representation vs information loss
PHY-REL-002  typed-dimension non-identification
PHY-REL-003  frame-order / lineage / cross-dynamics firewall
PHY-REL-004  weak-field proper-time / quantum-phase separation
PHY-REL-005  representation vs causal accessibility vs reconstruction
PHY-REL-006  Cauchy data / domain of dependence / reconstruction
PHY-REL-007  symmetry / curvature / Einstein equation / conservation relation layer
```

The previous Track-2 synthesis is also retained: common typed-map/reconstruction structure does not create a common physical primitive or cross-theory dynamics.

---

## 3. Provenance classes

```text
R0  PRE_EXISTING_DSD
R1  GENERAL_MATHEMATICAL_STRUCTURAL
R2  RELATIVITY_SPECIALIZATION
R3  STANDARD_THEOREM_CONSEQUENCE
R4  REMAINS_EXTERNAL_NOT_DERIVED
```

Only R0 and R1 count as target-independent structure available before standard relativity is selected.

R2 is admissible and necessary for a standard-relativity specialization, but it is not evidence that DSD independently derived relativity.

R3 contains results that follow once the relevant R2 structure and theorem hypotheses are supplied.

R4 records unresolved origins, empirical data, constants, or bridges that the current DSD core does not determine.

---

## 4. R0 — Pre-existing DSD contribution

The following distinctions were already present before the relativity target.

### 4.1 Typed status and applicability

Formation and Property preserve typed status rather than collapsing all missing, undefined, zero, or inapplicable cases into one numerical value.

This is useful for chart/domain/access questions, but does not itself create a spacetime chart or causal domain.

### 4.2 Explicit bridge discipline

A cross-structure identification requires a declared map. Equal counts, similar labels, or shared vocabulary do not create a physical bridge.

This is the basis of PHY-REL-002 and the later prohibition on identifying DSD `c_info`, rank, channel count, or strict equivalence with a relativistic object by name or cardinality alone.

### 4.3 Readout/reconstruction discipline

Static Aggregation explicitly separates full support from reduced aggregates and requires injectivity/support-retaining information for reconstruction.

This directly supports the distinction between a valid restricted/domain record and a globally reconstructive record.

### 4.4 Strict-equivalence firewall

Formation strict descriptive equivalence is a full formation-model relation. Equality of selected outputs or invariants is weaker.

Therefore standard relativistic isometry, diffeomorphism equivalence, coordinate covariance, or geometric uniqueness must not be identified with DSD strict equivalence without an explicit preservation-and-reflection theorem.

### 4.5 State / relation / transition separation

DSD Dynamics permits time-indexed static slices and explicitly supplied constitutive dynamics while keeping formation-level transitions and lineage distinct from ordinary value evolution.

This supports the relativity result that storing operands in a state does not derive a symmetry action, field equation, conservation law, or evolution relation.

---

## 5. R1 — General mathematical / structural results

These results do not require specifically relativistic physics.

### 5.1 Invertible representation change is not information loss by itself

If a representation map is invertible on its declared domain, the change of coordinates alone does not create a nontrivial reconstruction fiber.

This is a general map-theoretic statement. Lorentz transformations and chart transitions are standard-relativity instances.

### 5.2 Equal dimensions do not identify typed carriers

Numerical equality such as

```text
d_H = n_M = N_D
```

does not identify Hilbert dimension, spacetime dimension, and DSD channel/rank count as physical structures.

### 5.3 State data do not select an evolution law

One-slice data can admit multiple continuations unless an evolution relation is supplied. PHY-REL-006 exhibited this with the wave-equation comparator.

### 5.4 Fiber/factorization reconstruction gate

A reduced/domain readout determines a target quantity only if that target is constant on the readout fibers. This is the target-independent kernel behind domain-restricted reconstruction results.

### 5.5 Passive representation vs active transition

A passive re-description and a physical state transition satisfy different semantic commuting relations. Coordinate/frame relabeling is therefore not promoted to physical progression merely because both are represented as maps.

---

## 6. R2 — Relativity specialization supplied externally

The following structures are not obtained from generic DSD in the current program:

```text
smooth spacetime manifold
Lorentzian metric
spacetime dimension and signature
time orientation where required
Einstein field equation
matter / stress-energy model
constraint-satisfying initial data
weak-field background specialization
```

This classification is central.

In particular:

\[
\boxed{\text{generic DSD}\not\Rightarrow\text{Lorentzian metric}}
\]

and

\[
\boxed{\text{generic DSD}\not\Rightarrow\text{Einstein field equation}.}
\]

The current DSD papers explicitly leave geometric representations and constitutive dynamics downstream rather than building them into the abstract core.

---

## 7. R3 — Standard theorem consequences after specialization

Once the standard geometric/dynamical inputs and theorem hypotheses are supplied, familiar relativistic structures follow in the ordinary way.

### 7.1 Levi-Civita connection

Given a smooth pseudo-Riemannian/Lorentzian metric, the torsion-free metric-compatible connection is uniquely determined by the standard fundamental theorem of metric geometry.

This is a mathematical theorem consequence, not an independent DSD result.

### 7.2 Causal cone structure

A Lorentzian metric supplies the timelike/null/spacelike cone structure; a time orientation is additionally needed for a global future/past orientation where applicable.

Thus causal accessibility is not a coordinate label and is not generated by DSD channel identity.

### 7.3 Proper time

For a timelike curve, proper time is computed from the supplied Lorentzian metric and is invariant under valid coordinate re-description.

PHY-REL-001 and PHY-REL-004 already used this distinction.

### 7.4 Curvature

Curvature is determined from the supplied differential-geometric structure; it is not a pointwise metric label. PHY-REL-007 explicitly demonstrated that identical pointwise metric and first-derivative data at one point can coexist with different curvature.

### 7.5 Lorentz-frame interval/causal invariance

In the Minkowski specialization, the supplied Lorentz action preserves the Minkowski metric/interval and hence causal class. This is compatible with frame-dependent coordinate-time ordering for spacelike events.

### 7.6 Covariant stress-energy conservation

Under the standard Einstein equation with constant cosmological term, Levi-Civita metric compatibility, and the contracted Bianchi identity,

\[
\nabla_\mu T^{\mu\nu}=0
\]

follows as the usual local covariant consistency relation.

The converse does not hold in general, and local covariant conservation is not a universal global scalar-energy conservation theorem.

### 7.7 Maximal globally hyperbolic development

For admissible constraint-satisfying Einstein initial data, the standard Choquet-Bruhat–Geroch result gives the maximal globally hyperbolic development with geometric uniqueness in the theorem's sense.

This result does not identify that equivalence notion with DSD strict formation equivalence.

### 7.8 Weak-field proper-time relation

Under the supplied static weak-field approximation,

\[
\Delta\tau\approx\frac{\Delta\Phi}{c^2}T
\]

is a standard specialization result. PHY-REL-004 already separated it from coordinate time and downstream quantum phase/readout structure.

---

## 8. R4 — Remains external / not independently derived

The current program does not derive:

```text
why physical spacetime has four dimensions
why the physical metric has Lorentzian signature
why the Einstein field equation is the gravitational field law
the numerical values of G, c, or Lambda
actual matter content, topology, boundary conditions, or initial data
c_info = relativistic c
DSD strict equivalence = GR diffeomorphism/isometry/geometric equivalence
a unique QM-GR cross-dynamics or quantum-to-geometry map
```

These are not hidden failures. They specify the exact boundary of the present reconstruction claim.

---

## 9. Reclassification of PHY-REL-001–007

```text
PHY-REL-001
  DSD contribution: representation/readout typing, reconstruction discipline      R0
  invertible-map no-loss statement                                                R1
  Lorentz/chart specialization                                                     R2/R3

PHY-REL-002
  explicit typed-bridge discipline                                                 R0
  equal-cardinality non-identification                                             R1
  spacetime dimension itself                                                       R2

PHY-REL-003
  lineage/transition distinction                                                   R0
  passive/active and product-underdetermination logic                              R1
  SR causal/frame structure                                                        R2/R3
  unique QM-GR cross-dynamics                                                      R4

PHY-REL-004
  typed descriptor/readout separation                                              R0
  weak-field metric/background                                                     R2
  proper-time/weak-field relation                                                  R3

PHY-REL-005
  access/readout/reconstruction role separation                                    R0/R1
  Lorentzian causal structure                                                      R2/R3

PHY-REL-006
  state vs supplied evolution relation                                             R0/R1
  Einstein/Cauchy initial-data specialization                                      R2
  standard domain-of-dependence / maximal-development results                      R3

PHY-REL-007
  state vs relation firewall                                                       R0/R1
  Lorentzian metric, EFE, matter model                                              R2
  connection/curvature/Bianchi/conservation consequences                           R3
  DSD-derived EFE or equivalence identification                                    R4
```

No earlier result needs to be discarded. The rebaseline changes provenance labels, not the successful in-domain mathematics of the earlier audits.

---

## 10. Strongest justified reconstruction statement

The strongest current statement is:

\[
\boxed{
\begin{aligned}
&\text{DSD independently supplies typed representation, status, bridge,}\\
&\text{reconstruction, equivalence, and transition disciplines;}\\
&\text{general map/domain mathematics supplies further target-independent gates;}\\
&\text{standard Lorentzian geometry and Einstein dynamics remain supplied;}\\
&\text{their standard consequences are then reproduced conditionally.}
\end{aligned}}
\]

Therefore:

\[
\boxed{
\text{DSD-compatible reconstruction of relativity}
\neq
\text{independent derivation of general relativity from generic DSD}.
}
\]

This is the relativity analogue of the provenance boundary fixed in QM Core 009.

---

## 11. External theorem verification

Standard claims were checked against:

- Sean M. Carroll, *Lecture Notes on General Relativity*, arXiv:gr-qc/9712019.
- Choquet-Bruhat–Geroch Cauchy-development literature and later Living Reviews summaries of the Einstein Cauchy problem.
- Standard fundamental theorem for the Levi-Civita connection on a pseudo-Riemannian metric.

These are standard-relativity/mathematical sources and are not counted as DSD-derived evidence.

---

## 12. Reproducibility gate

The companion Python ledger checks:

```text
all provenance classes are declared
all dependencies exist
dependency graph is acyclic
no supplied relativity primitive is counted as R0/R1
Lorentzian metric and Einstein equation remain supplied
causal geometry depends on metric/time orientation
curvature depends on geometric structure
Cauchy development depends on GR initial data/equations
c_info = c remains not derived
GR equivalence = DSD strict equivalence remains not derived
unique QM-GR cross-dynamics remains not derived
PHY-REL-001 through PHY-REL-007 all have coverage nodes
```

Observed result:

```text
PRE_EXISTING_DSD                             5
GENERAL_MATHEMATICAL_STRUCTURAL              5
RELATIVITY_SPECIALIZATION                    8
STANDARD_THEOREM_CONSEQUENCE                 8
REMAINS_EXTERNAL_NOT_DERIVED                 8

OVERALL: PASS_WITH_BOUNDARY
```

The counts are ledger-node counts, not measures of physical importance.

Run from repository root:

```bash
python audits/science/2026-09-10_rel_core_001r_integrated_standard_relativity_rebaseline_provenance_gate.py --mode all
```

---

## 13. Verdict

**PASS_WITH_BOUNDARY**.

The previous standard-relativity corpus remains internally consistent after provenance reclassification. The rebaseline makes the central boundary explicit:

\[
\boxed{
\text{generic DSD does not independently select Lorentzian geometry or Einstein dynamics.}
}
\]

At the same time, the DSD source layers supply a stable typed/reconstruction interface in which standard-relativity structures and theorem consequences can be represented without collapsing representation, causal access, state, relation, transition, and reconstruction roles.

No DSD core-paper revision is required at this gate.

---

## 14. Next target

**REL Core 002 — Lorentzian Metric / Causal Geometry Admission and Reconstruction Gate**.

The next stage should isolate the geometric chain before Einstein dynamics:

```text
smooth manifold
-> Lorentzian metric
-> signature / time orientation
-> timelike-null-spacelike classification
-> proper time / causal relation
-> Levi-Civita connection
-> curvature
```

The audit should determine exactly which steps are definitional or theorem consequences once a Lorentzian metric is supplied, and test whether any weaker DSD/general structural assumptions can select that metric without importing relativity-specific structure.
