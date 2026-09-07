# PHY-QFT-004~008 — Relative Entropy, Modular Flow, and Curved-Spacetime QFT Audit

Date: 2026-09-07

## Scope
The QFT mathematics below is external standard theory. DSD is used only to classify what is representation-dependent, state-dependent, recoverable, locally accessible, or causally available.

## PHY-QFT-004 — Sharp-region entanglement entropy is not a universal local information coordinate
In continuum QFT, spatial entanglement entropy for sharp regions is ultraviolet-sensitive/divergent, and sharp local algebras are generally not ordinary finite-dimensional tensor factors. Relative entropy and algebraic entanglement measures are often better behaved and can compare states directly at the local-algebra level.

### DSD consequence
A single scalar called "entropy" must not be promoted to the complete local structural descriptor.

```text
entropy readout != local algebra != complete state != recoverability
```

This supports the current DSD rule that reduced entropy/aggregate readouts remain secondary unless an injectivity or reconstruction theorem is supplied.

## PHY-QFT-005 — Modular flow is state-dependent in the generic algebraic setting
Finite control: let

rho = diag(0.8,0.2)

on M_2(C). For the matrix unit A=|0><1|, the faithful-state modular automorphism is

sigma_t(A) = rho^(it) A rho^(-it)
           = exp[i t ln(0.8/0.2)] A
           = exp[i t ln 4] A.

At t=1,

```text
ln 4 = 1.386294361119891
phase = 0.183456974743302 + 0.983027740411244 i
```

Changing the state spectrum changes this modular flow.

### DSD consequence
The modular parameter is not automatically DSD progression time, metric time, or universal physical time. A theorem/bridge is required before identifying them.

## PHY-QFT-006 — Bisognano-Wichmann is a special geometric identification
For suitable relativistic QFTs, the modular group of a wedge algebra with the vacuum state coincides, up to the standard rescaling, with the Lorentz boosts preserving that wedge.

This is an important positive contact between algebraic state-dependent structure and spacetime geometry, but it is conditional on the specified algebra, region, state, and QFT assumptions.

### DSD consequence
Safe chain:

```text
local algebra + selected state
    -> modular data
    -> [special theorem]
    -> geometric spacetime flow
```

Unsafe chain:

```text
modular flow -> universal physical time/metric
```

Thus modular theory gives a strong test bed for DSD representation/bridge auditing rather than a shortcut to deriving spacetime.

## PHY-QFT-007 — Curved-spacetime QFT removes the generic preferred-vacuum assumption
On a general globally hyperbolic curved spacetime, Poincare symmetry and a unique preferred vacuum need not exist. Modern formulations emphasize local covariance and admissible state classes such as Hadamard states.

### DSD consequences
1. "Vacuum" cannot be treated as a universal property value independent of geometry/state-selection context.
2. Hadamard admissibility is an external microlocal/UV condition; it must not be renamed as DSD resolution without an explicit bridge.
3. Local covariance in QFT is not automatically identical to DSD strict equivalence/covariance; the relevant spacetime-to-algebra functorial structure must be supplied.
4. State selection and observable algebra are distinct inputs.

## PHY-QFT-008 — Unruh-type thermality is an accessibility/dynamics statement, not global-state branching
The Minkowski vacuum can produce thermal response for uniformly accelerated observers / Rindler-accessible descriptions without the global Minkowski state having been replaced by a different global state.

### DSD consequence
The safe classification is

```text
global state
+ observer trajectory/access region
+ local algebra/detector dynamics
-> observer-dependent thermal readout
```

Therefore

```text
observer-dependent thermality
    != global structural branching
    != superluminal propagation
    != automatic change of complete-state identity.
```

This is the QFT analogue of the earlier Lorentz-coordinate negative control: a change in observer-accessible representation or response does not by itself establish a change in complete underlying structure.

## External references
- S. Hollands, R. M. Wald, Quantum fields in curved spacetime, arXiv:1401.2026.
- C. J. Fewster, R. Verch, Algebraic quantum field theory in curved spacetimes, arXiv:1504.00586.
- R. Brunetti, D. Guido, R. Longo, Modular Structure and Duality in Conformal Quantum Field Theory, arXiv:funct-an/9302008.
- S. Hollands, K. Sanders, Entanglement measures and their properties in quantum field theory, arXiv:1702.04924.
- N. Lashkari, Relative Entropies in Conformal Field Theory, arXiv:1404.3216.

## Verdict
PASS_WITH_BOUNDARY.

QFT strengthens the DSD distinction among local algebra, state, observer access, reduced entropy, modular flow, and spacetime geometry. The main surviving rule is that a representation-level or state-dependent structure may acquire geometric meaning only under an explicit theorem/bridge.
