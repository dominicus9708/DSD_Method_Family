# PHY-QFT-004~010 — Modular Theory and Curved-Spacetime QFT Audit

Date: 2026-09-07
Method: DSD analysis + DSD general audit
Status: PASS_WITH_BOUNDARY

## PHY-QFT-004 — Local von Neumann entropy is not a universal sharp-region descriptor in QFT
Relativistic local algebras are generally type III in standard AQFT settings; naive sharp-region density-matrix/von-Neumann entropy therefore requires care/regulation and should not be treated as a primitive universal local observable.

DSD verdict:
REGION -> DENSITY MATRIX is not a universal bridge.

Use region-indexed local algebra as the more robust primary representation when working at QFT level.

## PHY-QFT-005 — Modular flow is algebra-and-state relative
For a von Neumann algebra with a suitable faithful/cyclic-separating state, Tomita-Takesaki modular data depend on the pair (algebra,state). Even the finite faithful-state control K=-log(rho) changes when rho changes while the matrix algebra is held fixed.

Therefore:
MODULAR FLOW != universal physical time.

A DSD time/progression sector cannot be identified with modular flow without an explicit specialization theorem.

## PHY-QFT-006 — Bisognano-Wichmann is a conditional bridge, not a universal identity
For the Minkowski vacuum and wedge algebra under the theorem's hypotheses, modular flow has a geometric identification with Lorentz boosts. This is a powerful junction among state, algebra, and spacetime symmetry, but the hypotheses matter.

DSD verdict:
(algebra,state,symmetry hypotheses) -> geometric modular flow
is a conditional downstream bridge.

It does not justify:
`modular flow = spacetime time` in arbitrary region/state/spacetime.

## PHY-QFT-007 — Relative entropy is better behaved than naive sharp-region entropy for some AQFT questions
Araki-type relative entropy can be formulated algebraically and is widely used in QFT/modular theory, including curved-spacetime applications. This makes it a useful comparison diagnostic after the local algebra and states are supplied.

DSD verdict:
relative entropy is a robust domain-specific distinguishability diagnostic, not the definition of structural describability.

## PHY-QFT-008 — Curved-spacetime QFT has no generic preferred Minkowski-like vacuum/particle decomposition
On a globally hyperbolic curved background the rigorous framework emphasizes local covariance, hyperbolic propagation, Hadamard/microlocal admissibility, and local observables. A unique globally preferred particle/vacuum notion is not generally available.

DSD consequence:
`particle count` is representation/observer/state-structure dependent in this domain and cannot be promoted automatically to a primitive formation/property label.

## PHY-QFT-009 — Hadamard admissibility is not a value assignment
The Hadamard condition constrains the singularity structure/ultraviolet behavior of admissible states so local composite observables can be defined/renormalized appropriately. It does not by itself pick one unique physical state.

DSD verdict:
ADMISSIBILITY != REALIZATION SELECTION.

This is an external QFT witness for the DSD distinction between admissibility conditions and later realized assignments.

## PHY-QFT-010 — Local covariance is closer to a representation-consistency rule than to a new causal speed
Locally covariant QFT transports algebraic structures consistently under admissible spacetime embeddings. This should be kept separate from microcausality and from a finite propagation-speed bound such as DSD c_info.

Keep distinct:
- local covariance,
- microcausality/commutation,
- hyperbolic support propagation,
- observer accessibility,
- DSD c_info specialization.

## Synthesis
The strongest DSD-QFT interface after this audit is:

spacetime region
-> local algebra
-> admissible state class
-> local/covariant dynamics
-> state-algebra modular/relative-entropy diagnostics

with no automatic promotion of entropy, modular flow, particle number, or tensor-factor subsystem structure to DSD primitives.
