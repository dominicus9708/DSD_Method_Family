# PHY-QM-044 / PHY-QFT-009~011 — Accessibility, Time Typing, and Special Modular-Geometric Bridge Audit

Date: 2026-09-07

## Scope
All quantum-relative-entropy, modular, Lorentz-boost, and Unruh formulas below are supplied by standard QM/QFT as external specialization data. DSD is used only to audit type distinctions and bridge conditions.

## PHY-QM-044 — Nested-access distinguishability
Take

rho_A = diag(0.8,0.2),
sigma_A = I/2,
rho_B = |0><0|,
sigma_B = I/2,

and

rho_AB = rho_A tensor rho_B,
sigma_AB = sigma_A tensor sigma_B.

The finite control gives

```text
D_A  = 0.192744757021757
D_AB = 0.885891937581703
D_AB - D_A = 0.693147180559945 = ln 2
```

The A-only description is obtained from AB by a CPTP coarse-graining (partial trace), so the standard data-processing inequality guarantees that relative entropy cannot be larger after the restriction.

### DSD consequence
For a nested family of quantum-access maps of the form

Phi_1 = C o Phi_2

with C a valid CPTP coarse-graining and quantum relative entropy used as the supplied distinguishability diagnostic,

```text
more complete accessible record
    can retain at least as much pairwise relative-entropy distinguishability
as its CPTP coarse-graining.
```

This is a conditional accessibility-monotonicity result. It must NOT be generalized to every DSD descriptive projection Pi_O, because the current DSD definition does not require Pi_O to be linear, CPTP, or even quantum.

Candidate audit label:

```text
NESTED-ACCESS MONOTONICITY AUDIT
```

## PHY-QFT-009 — Five different time/flow coordinates must remain typed
At the present DSD/QFT interface, distinguish at least:

1. DSD external metric/evolution time t used by a supplied dynamic realization.
2. DSD-gravity progression factor N = exp(psi), which is a field/response sector, not by itself a time coordinate.
3. Modular parameter s of an algebra-state pair.
4. Observer proper time tau along a worldline.
5. Geometric boost rapidity eta in Minkowski/Rindler geometry.

No current DSD theorem identifies any pair of these universally.

### Negative-control verdict
The following shortcuts are rejected:

```text
modular parameter = DSD metric time
modular flow = DSD progression field
proper time = modular parameter
Unruh temperature = DSD structural entropy
```

Any positive identification requires an explicit map with domain, codomain, state/region assumptions, and normalization.

## PHY-QFT-010 — Bisognano-Wichmann + Unruh gives a special bridge, not a universal clock
In the vacuum-wedge setting covered by the Bisognano-Wichmann property, the modular group is implemented by the Lorentz boosts preserving the wedge, with a conventional 2*pi rescaling of the modular parameter.

Using magnitudes to avoid the convention-dependent overall sign,

|eta| = 2*pi*|s|.

For a uniformly accelerated Rindler observer,

|eta| = a*|tau|,

so within this special setup

|tau| = 2*pi*|s|/a.

The Unruh temperature in natural units is

T_U = a/(2*pi).

Control point:

```text
a = 2
|s| = 0.25
|eta| = pi/2 = 1.570796326794897
|tau| = pi/4 = 0.785398163397448
T_U = 1/pi = 0.318309886183791
```

### DSD consequence
This is the strongest positive time-interface contact found so far:

```text
wedge algebra + vacuum + BW property + uniformly accelerated trajectory
    -> modular parameter <-> boost rapidity <-> proper time
```

but the proportionality contains the observer acceleration and depends on a special algebra/state/geometric setup. The DSD progression field N does not appear in this theorem. Therefore the chain cannot be extended to DSD gravity without a new constitutive/geometric bridge.

Candidate audit label:

```text
TIME/FLOW TYPE AUDIT
```

## PHY-QFT-011 — Local-algebra accessibility and relative entropy
In algebraic QFT, restriction from a larger observable algebra to a smaller accessible subalgebra is a coarse-graining. Standard relative-entropy monotonicity supplies a quantitative version of the statement that removing accessible observables cannot increase distinguishability of a fixed pair of states.

### DSD consequence
A useful conditional pattern is

```text
A_small subset A_large
+ well-defined state restrictions
+ standard relative entropy
    -> D_large >= D_small.
```

This may serve as a model for DSD accessibility ladders only after a specific quantum representation is supplied. It is not a theorem about arbitrary DSD accessibility specifications.

## Audit verdict
PASS_WITH_BOUNDARY.

The standard theory supplies a genuine special bridge among modular flow, Lorentz boosts and accelerated-observer proper time, while simultaneously showing why modular time cannot be promoted to a universal DSD clock. Nested-access relative entropy also gives a quantitative accessibility diagnostic, but only inside the explicitly supplied quantum/CPTP representation.

## External references
- M. Junge, R. Renner, D. Sutter, M. M. Wilde, A. Winter, Universal recovery maps and approximate sufficiency of quantum relative entropy, arXiv:1509.07127.
- E. A. Carlen, A. Vershynina, Recovery map stability for the Data Processing Inequality, arXiv:1710.02409.
- R. Brunetti, D. Guido, R. Longo, Modular Structure and Duality in Conformal Quantum Field Theory, arXiv:funct-an/9302008.
- Standard Bisognano-Wichmann/Unruh relation under the stated wedge-vacuum/accelerated-observer assumptions.
