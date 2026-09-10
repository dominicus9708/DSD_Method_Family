# Relativity Equivalence / Local-Inertial / Clock-Rate Provenance Interface

Status: **Active downstream audit interface**  
Source audit: **REL Extension 005**

## Interface rule

Do not collapse local inertial coordinates, equivalence-principle statements, curvature, clock-rate gradients, and Einstein dynamics into one concept.

Maintain the dependency order

```text
supplied Lorentzian metric/connection
    -> local inertial representation at an event
    -> curvature/tidal tensors remain independent of connection removal

supplied static metric + stationary observer model
    -> clock-rate ratio

supplied weak-field metric/potential bridge
    -> weak-field redshift approximation

supplied Einstein dynamics/source data
    -> physical metric solution
```

None of the reverse arrows is automatic.

## Hard firewalls

\[
\Gamma(p)=0 \not\Rightarrow R(p)=0.
\]

\[
\text{clock-rate gradient}\not\Rightarrow\text{curvature}.
\]

\[
\text{equivalence principle}\not\Rightarrow\text{Einstein field equation}.
\]

\[
\text{metric redshift calculation}\not\Rightarrow\text{metric-source derivation}.
\]

## DSD mapping

Keep separate typed records for:

```text
COORDINATE_CONNECTION
LOCAL_INERTIAL_STATUS
TIDAL_CURVATURE
CLOCK_RATE_READOUT
STATIC_LAPSE_OR_METRIC
EMPIRICAL_REDSHIFT_DATA
FIELD_EQUATION_AND_SOURCE
```

DSD's numerical evolution parameter is not automatically relativistic proper time. Its supplied localization metric is not automatically the physical spacetime metric. Its finite-propagation bound c_info is not automatically relativistic c.

## Minimal countermodels retained

1. Curved local-inertial witness:

\[
ds^2=-(1+kx^2)dt^2+dx^2.
\]

At \(x=0\), relevant Christoffel symbols vanish while \(R=-2k\neq0\).

2. Flat accelerated clock-gradient witness:

\[
ds^2=-(1+ax)^2dt^2+dx^2,
\qquad R=0,
\]

but

\[
d\tau=(1+ax)dt.
\]

These two witnesses prevent both directions of a common conflation:

```text
connection/acceleration appearance <-> curvature
```

is not an equivalence.

## Scope

This interface audits standard relativity and does not import structural-gravity hypotheses. Empirical redshift experiments remain external evidence, and the Einstein field equation, G, actual source content, physical c, and actual spacetime solution remain supplied/external unless another theory explicitly derives them.
