# Relativity Accelerated-Clock / Proper-Time Provenance Interface

Status: active methodology interface  
Track: REL Extension  
Introduced by: REL Extension 004

## Purpose
Prevent the provenance collapse `metric defines proper time -> every real accelerated clock must read it exactly -> no extra operational bridge is needed`.

## Layer A — Geometric chronometry
Given a supplied Lorentzian metric and timelike worldline,
\[
d\tau=\sqrt{-g_{\mu\nu}dx^\mu dx^\nu}.
\]
This is the geometric proper-time functional. In flat spacetime it depends on the tangent and contains no universal explicit acceleration correction.

## Layer B — Clock realization
A physical clock has internal dynamics. The identification
\[
T_{clock}\approx\tau
\]
must be supported by an explicit route such as `CLOCK_CONDITION`, `DEVICE_DYNAMICAL_DERIVATION`, `CONTROLLED_APPROXIMATION`, or `EXPERIMENTAL_CALIBRATION`. Do not infer it from the metric definition alone.

## Layer C — Numerical calibration
Even an accepted proper-time clock may report
\[
T_{display}=\alpha\tau+\beta.
\]
The zero and display scale remain calibration data unless separately fixed.

## Required provenance labels
```text
GEOMETRY_SUPPLIED
PROPER_TIME_DEFINED
CLOCK_CONDITION_SUPPLIED
DEVICE_MODEL_SUPPLIED
EXPERIMENTAL_SUPPORT
CALIBRATION_SUPPLIED
DSD_STRUCTURAL_ONLY
```

## Accelerated-observer firewall
At fixed event and fixed tangent, the Lorentzian line element fixes the same infinitesimal proper time independently of the worldline second derivative. This does not prohibit acceleration-sensitive behavior of nonideal hardware:
\[
\text{no acceleration term in }d\tau\not\Rightarrow\text{no acceleration effect in arbitrary hardware}.
\]

## Circularity firewall
If a quantity is inferred under special relativity, do not reuse it as independent validation of the same relativistic transformation. Keep `RAW/INDEPENDENTLY_CALIBRATED OBSERVATION`, `MODEL-DEPENDENT DERIVED QUANTITY`, and `THEORY-COMPARISON RESULT` distinct.

## DSD boundary
Do not automatically identify DSD numerical time with relativistic proper time. Likewise `DSD c_info != relativistic c`, `DSD lineage != accelerated-clock law`, `DSD channel/property != physical clock mechanism`, and `DSD structural compatibility != Einstein dynamics` unless an explicit downstream bridge is supplied.

## Regression witnesses
```text
uniform proper-acceleration hyperbola normalization
u dot u = -1
A dot A = a^2
u dot A = 0
sqrt(1-v^2) dt/dtau = 1
same-tangent / different-acceleration device countermodel
piecewise-inertial twin-path proper-time comparison
affine display recalibration
experiment-versus-derived-quantity provenance ledger
```

Use `PASS_WITH_BOUNDARY` when geometric proper time is reconstructed correctly, accelerated paths remain consistent, clock realization and calibration remain explicit, experimental evidence is not circularly reused, and no independent DSD derivation of relativistic chronometry is claimed.
