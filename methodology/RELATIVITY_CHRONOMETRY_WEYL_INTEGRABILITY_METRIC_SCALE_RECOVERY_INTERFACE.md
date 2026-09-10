# Relativity Chronometry / Weyl Integrability / Metric-Scale Recovery Interface

Status: **ACTIVE — AUDITED INTERFACE**  
Audit source: **REL Extension 003**

## Purpose

This interface provides a provenance-safe way to use chronometric and Weyl-geometric reconstruction arguments inside DSD analysis without conflating a successful conditional reconstruction with an independent derivation of physical clock structure.

The interface is downstream and optional. It is not a Formation, Property, static-aggregation, or universal DSD dynamics axiom.

---

## Required separation

Keep the following objects logically distinct:

```text
conformal class
Weyl scale connection
closed Weyl one-form
exact Weyl one-form
local integrability
global integrability
standard-clock rule
proper-time parametrization
second-clock-effect criterion
physical clock calibration
metric dynamics
```

A shared vocabulary or a successful reconstruction map does not identify these roles.

---

## DSD firewall

The DSD dynamics time parameter is an external evolution parameter in the general model. A numerical speed requires metric time, but this requirement does not select a Lorentzian proper-time law, a clock mechanism, or an absolute unit.

Therefore use the following rule:

```text
DSD external evolution parameter != relativistic proper time
DSD metric-time requirement      != physical clock calibration
DSD propagation bound c_info     != relativistic c without an explicit bridge
```

Any identification must be supplied and audited separately.

---

## Conditional chronometric route

Within the EPS/Perlick/Avalos comparator framework, the admissible reconstruction chain is:

```text
Weyl geometry
+ standard-clock definition
+ adopted proper-time / transport rule
+ empirical no-second-clock-effect selector
+ sufficient global topology assumptions
-> integrable Weyl geometry
-> pseudo-Riemannian representative
```

Each premise retains its original provenance after reconstruction.

Do not rewrite this chain as

```text
DSD -> metric proper time
```

or as an assumption-free derivation of Lorentzian spacetime.

---

## Closed versus exact rule

Treat

```text
d omega = 0
```

as a local closedness condition.

Treat

```text
omega = d phi
```

as an exactness condition.

Global exactness additionally depends on the domain topology. The canonical audit witness is

\[
\omega=
-\frac{y}{x^2+y^2}\,dx
+
\frac{x}{x^2+y^2}\,dy
\]

on \(\mathbb R^2\setminus\{0\}\): it is closed away from the origin but has

\[
\oint\omega=2\pi,
\]

so it is not globally exact.

Never collapse local integrability and global integrability into one status field.

---

## Second-clock-effect rule

In the adopted EPS/Perlick/Avalos clock comparison, path dependence of the Weyl integral can yield history dependence of the clock-rate comparison.

The regression witness

\[
\omega=x\,dy
\]

has

\[
d\omega=dx\wedge dy\neq0
\]

and two same-endpoint paths with integrals 1 and 0, giving a comparison factor \(e^{1/2}\).

This implication is **comparator-dependent**. Alternative Weyl-covariant/nonmetric transport prescriptions may alter the second-clock conclusion. Therefore record the adopted clock and transport convention as an explicit selector.

---

## Residual scale rule

If

\[
\omega=d\phi,
\]

then an allowed Weyl gauge can set the one-form to zero. But

\[
\phi\mapsto\phi+C
\]

leaves \(d\phi\) unchanged while multiplying the corresponding zero-Weyl metric representative by a constant factor.

Likewise a standard proper-time parameter remains affine-ambiguous:

\[
\widetilde\tau=a\tau+b.
\]

Therefore distinguish:

```text
connection-level / local metric recovery
from
absolute numerical scale and clock-zero calibration
```

The latter remains physical/operational data unless supplied by an additional theory or standard.

---

## Provenance classes

Use the established relativity ledger:

```text
R0 PRE_EXISTING_DSD
  typed applicability/status
  explicit bridge discipline
  state/relation/transition separation
  ordered-history versus metric-time separation

R1 GENERAL_MATHEMATICAL_STRUCTURAL
  closed versus exact forms
  local versus global integrability
  topology/path-independence
  affine reparametrization ambiguity

R2 RELATIVITY_CHRONOMETRY_SPECIALIZATION
  Weyl/Lorentzian geometry
  timelike curves
  standard-clock definition
  second-clock comparison rule

R3 STANDARD_THEOREM_CONSEQUENCE
  conditional local clock reparametrization
  exact Weyl -> zero-one-form gauge
  no-SCE -> local closedness in the adopted framework
  closed + suitable topology -> global exactness

R4 REMAINS_EXTERNAL_NOT_DERIVED
  empirical SCE bounds
  clock hardware and calibration
  absolute numerical proper-time unit
  actual topology/dimension/signature/orientation
  Einstein field equation and physical constants
```

Only R0/R1 may be counted as target-independent DSD evidence.

---

## Reproducibility

Run from repository root:

```bash
python audits/science/2026-09-10_rel_extension_003_clock_weyl_integrability_metric_scale_recovery_gate.py --mode all
```

Expected audited result:

```text
TOTAL: 57/57 checks passed
OVERALL: PASS_WITH_BOUNDARY
```

The regression is a finite algebraic/topological/provenance audit, not an empirical clock experiment and not a proof of all cited external reconstruction theorems.

---

## Next interface target

**REL Extension 004 — Clock Hypothesis / Accelerated Proper-Time / Operational Calibration Gate**

Keep metric proper time, the ideal-clock hypothesis, accelerated worldlines, real clock mechanisms, finite-size/systematic effects, coordinate time, observer readout, initial calibration, and Einstein dynamics distinct.
