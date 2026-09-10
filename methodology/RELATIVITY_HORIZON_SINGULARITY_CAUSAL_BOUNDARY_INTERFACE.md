# Relativity Horizon / Singularity / Causal-Boundary Interface

Status: **REL Core 007 — PASS_WITH_BOUNDARY**  
Author: Kwon Dominicus  
Date: 2026-09-10

## Purpose

This interface prevents five distinct notions from being silently identified:

\[
\boxed{
\text{coordinate failure}
\neq
\text{event horizon}
\neq
\text{curvature singularity}
\neq
\text{geodesic incompleteness}
\neq
\text{descriptive inaccessibility}
}
\]

## Standard-relativity specialization

Supply a positive-mass Schwarzschild spacetime,

\[
f(r)=1-\frac{2M}{r}.
\]

Schwarzschild coordinates fail at \(r=2M\), but ingoing Eddington–Finkelstein coordinates

\[
ds^2=-f\,dv^2+2dvdr+r^2d\Omega^2
\]

have a nondegenerate \((v,r)\) block with determinant \(-1\).

The invariant curvature witness is

\[
K=\frac{48M^2}{r^6},
\]

so \(K(2M)=3/(4M^4)\) is finite while \(K\to\infty\) as \(r\to0\).

For outgoing radial null curves in ingoing Eddington–Finkelstein coordinates,

\[
\frac{dr}{dv}=\frac12f(r),
\]

which is positive outside, zero at, and negative inside the horizon once the standard future orientation is supplied.

For the \(E=1\) radial timelike geodesic,

\[
\Delta\tau_{2M\to0}=\frac{4M}{3}<\infty.
\]

## Global-causal boundary

The event horizon is not inferred from a single local metric coefficient or from \(g_{tt}=0\). It is a global causal/asymptotic property of the supplied spacetime.

Therefore local null-cone calculations may witness one-way behavior, but event-horizon status stays tied to the global Schwarzschild extension and asymptotic structure.

## Singularity firewall

A curvature blow-up is an invariant witness in Schwarzschild, but singular spacetime behavior is not universally defined by curvature divergence alone.

Geodesic incompleteness must remain logically separate. A restricted flat Minkowski region can be geodesically incomplete despite vanishing curvature.

## DSD interface

Current DSD descriptive projection

\[
\Pi_O:X\to X_O
\]

may be noninjective. Hence restricted descriptive access can erase distinctions without implying equality or nonexistence of the underlying full state.

Permitted application-level statement:

\[
\boxed{
\text{DSD can type and audit an externally supplied causal-access restriction.}
}
\]

Forbidden automatic identifications:

```text
DSD descriptive projection = GR event horizon
DSD undefined assignment = causal inaccessibility
coordinate failure = structural nonexistence
structural-gravity local collapse = Schwarzschild horizon
```

Any such relation requires an explicit bridge and an independent compatibility/derivation argument.

## Provenance rule

```text
R0 PRE_EXISTING_DSD
  typed access/status/readout distinctions

R1 GENERAL_MATHEMATICAL_STRUCTURAL
  chart regularity, invariant scalar, geodesic completeness distinctions

R2 RELATIVITY_SPECIALIZATION
  Schwarzschild solution, M>0, asymptotic/global causal interpretation

R3 STANDARD_THEOREM_CONSEQUENCE
  EF regularity, Kretschmann behavior, null-slope signs, finite E=1 proper time

R4 REMAINS_EXTERNAL_NOT_DERIVED
  black-hole geometry from generic DSD
  event horizon from DSD projection alone
  Schwarzschild identification of structural-gravity collapse notions
```

## Reproducibility

```bash
python audits/science/2026-09-10_rel_core_007_horizon_coordinate_curvature_causal_boundary_gate.py --mode all
```

Expected result:

```text
TOTAL: 39/39 checks passed
OVERALL: PASS_WITH_BOUNDARY
```

## Next gate

**REL Core 008 — Integrated Standard-Relativity Reconstruction Synthesis / Provenance Closure Gate**.
