# Relativity Scalar-Invariant / Frame-Classification / Degeneracy Interface

Status: **Active after REL Extension 008**  
Audit verdict: **PASS_WITH_BOUNDARY**

## Purpose

Use this interface when a DSD analysis attempts to reconstruct or compare relativistic geometry from curvature scalars, invariant readouts, frame components, or curvature classification data.

## Mandatory separation

Keep the following objects distinct:

```text
full metric geometry
full Riemann tensor
scalar polynomial curvature invariants (SPI)
raw coordinate components
raw frame components
frame-normalized Cartan invariants
local-isometry class
physical solution selection
Einstein dynamics
DSD structural descriptors
```

## Primary reconstruction firewall

Do not infer

\[
\text{same SPIs}
\Rightarrow
\text{same full curvature}
\]

or

\[
\text{same SPIs}
\Rightarrow
\text{local isometry}
\]

without a theorem establishing invariant nondegeneracy for the target class.

## Canonical countermodel

Use the pair

\[
g_{\rm flat}=2dudv+dx^2+dy^2
\]

and

\[
g_{\rm wave}
=
2dudv+A(x^2-y^2)du^2+dx^2+dy^2,
\qquad
A\neq0.
\]

The second metric is nonflat and vacuum, while the complete scalar curvature-invariant family vanishes for the plane wave just as it does for Minkowski spacetime.

This is the preferred minimal witness against universal SPI reconstruction.

## Readout-fiber formulation

For an SPI readout map

\[
\Phi_{\rm SPI}:\mathcal G\to\mathcal I,
\]

a nontrivial fiber

\[
\Phi_{\rm SPI}^{-1}(I)
\]

means the invariant family does not uniquely reconstruct the target metric within the admitted class.

Treat this as an analysis diagnostic, not as a new DSD primitive.

## Nondegenerate-class exception

Do not generalize the VSI countermodel into the statement that curvature scalars are always insufficient.

In four-dimensional Lorentzian geometry, \(\mathcal I\)-non-degenerate metrics are locally characterized by their scalar polynomial curvature invariants; failure occurs in the degenerate Kundt sector.

Accordingly, every reconstruction claim must state its admitted geometric class and nondegeneracy hypothesis.

## Frame-normalization rule

Raw tensor components depend on coordinate or frame choice.

A claim based on frame components must therefore specify:

```text
observer/frame carrier
normalization rule
residual frame freedom
curvature derivative order
equivalence criterion
```

For degenerate pp-wave cases, use the Cartan–Karlhede strategy or another explicitly justified invariant equivalence procedure.

Do not treat a convenient coordinate basis as an invariant physical frame.

## DSD provenance rule

Generic DSD may diagnose:

```text
readout noninjectivity
information lost by scalar contraction
need for richer comparison structure
typed separation of geometry / readout / classification
```

Generic DSD does not by itself supply:

```text
Lorentzian spacetime metric
Riemann curvature
Einstein dynamics
VSI theorem
Kundt classification
Cartan–Karlhede normalization
physical metric selection
```

These remain downstream/external unless separately derived under explicit assumptions.

## Forbidden shortcut claims

Reject the following:

```text
Kretschmann = 0 => flat spacetime
all familiar curvature scalars = 0 => Riemann = 0
same complete SPI list => local isometry, without nondegeneracy conditions
raw frame components = invariant classification
VSI behavior = DSD prediction
Cartan invariants = generic DSD properties
DSD residual = physical curvature
c_info = c
```

## Required reporting language

Preferred:

> Scalar polynomial curvature invariants provide a noninjective readout on the admitted degenerate Lorentzian class. Additional frame-normalized tensorial data are required for invariant equivalence classification.

Avoid:

> DSD proves that curvature scalars are wrong.

Also avoid:

> DSD reconstructs pp-wave geometry from zero invariants.

## External comparator set

- Roche, Aazami, Cederbaum (2023), *Exact parallel waves in general relativity*, DOI 10.1007/s10714-023-03083-x.
- Pravda, Pravdová, Coley, Milson (2002), *All spacetimes with vanishing curvature invariants*, DOI 10.1088/0264-9381/19/23/318.
- Coley, Hervik, Pelavas (2009), *Spacetimes characterized by their scalar curvature invariants*, DOI 10.1088/0264-9381/26/2/025013.
- Milson, McNutt, Coley (2013), *Invariant classification of vacuum PP-waves*, DOI 10.1063/1.4791691.

## Next closure

After this interface, the ordinary standard-relativity extension line proceeds to:

**REL Extension 009 — Integrated Independent-Origin / Reconstruction Closure Gate**

No additional special-solution family should be added unless the final synthesis exposes a genuine unresolved provenance gap.
