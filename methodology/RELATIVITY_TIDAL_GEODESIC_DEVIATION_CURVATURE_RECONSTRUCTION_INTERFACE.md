# Relativity Tidal / Geodesic-Deviation / Curvature-Reconstruction Interface

## Status

Validated in **REL Extension 006** with `PASS_WITH_BOUNDARY`.

## Core separation

Keep the following objects distinct:

```text
reference geodesic
neighboring geodesic family
separation vector
relative acceleration
fixed-observer tidal matrix R_0i0j
full Riemann tensor
local tetrad/frame
Einstein source dynamics
DSD typed structural data
```

## Audit rule 1 — one tidal projection is not full curvature

For a fixed comoving observer,

\[
A^i=-R^i{}_{0j0}\xi^j.
\]

Three independent spatial separation directions recover only the symmetric six-component tidal block in a general four-dimensional nonvacuum algebraic-curvature space.

Do not infer the full 20-component Riemann tensor from that block alone.

## Audit rule 2 — require a kernel/hidden-curvature test

Before claiming full curvature reconstruction, search for a nonzero algebraic curvature perturbation \(\Delta R\) lying in the measurement kernel.

REL Extension 006 uses

\[
\Delta R_{1212}\neq0,
\qquad
\Delta R_{0i0j}=0,
\]

which is invisible to one fixed comoving observer but becomes visible to a suitable moving-observer configuration.

## Audit rule 3 — full reconstruction requires sufficiently rich probes

A full reconstruction claim must state the supplied observer velocities, separation vectors, relative-acceleration readouts, frame conventions, and the rank/invertibility condition of the resulting measurement map.

A successful inversion under these premises remains a conditional GR reconstruction theorem.

## Audit rule 4 — retain linear-deviation scope

The Jacobi/geodesic-deviation equation is a neighboring-worldline relation. Do not silently extend it to arbitrary finite separation or extended-body dynamics.

Use an explicit generalized-deviation framework where the claimed regime requires it.

## Audit rule 5 — preserve DSD provenance

Do not identify without an explicit bridge:

```text
DSD lineage -> geodesic congruence
DSD residual -> tidal acceleration
DSD localization metric -> physical spacetime metric
DSD c_info -> relativistic c
DSD dynamic operator -> geodesic-deviation operator
```

DSD may type and audit supplied relativistic records without deriving the relativistic specialization.

## Audit rule 6 — curvature measurement is not source dynamics

Even full local Riemann reconstruction does not by itself derive

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}
=\frac{8\pi G}{c^4}T_{\mu\nu}.
\]

Curvature measurement, Ricci/Weyl decomposition, matter-source attribution, and Einstein dynamics are separate gates.

## Regression command

```bash
python audits/science/2026-09-10_rel_extension_006_tidal_geodesic_deviation_curvature_reconstruction_local_observable_gate.py --mode all
```

Validated result:

```text
TOTAL: 71/71 checks passed
OVERALL: PASS_WITH_BOUNDARY
```

## Next interface

REL Extension 007 should audit Ricci/Weyl decomposition, vacuum curvature, and source attribution.
