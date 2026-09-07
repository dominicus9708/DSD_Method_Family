# PHY-QM/QFT/QRF-046~049 — Expanded Interface Synthesis

Date: 2026-09-07
Method: DSD analysis + DSD general audit
Status: SYNTHESIS

## PHY-046 — Describability needs at least six distinct diagnostics in advanced quantum/relativistic domains
The combined audits now separate:

1. IDENTIFIABILITY — does the supplied readout distinguish the underlying state/record?
2. COMPLETABILITY — does the observed object belong to a specified model class?
3. RECOVERABILITY — can an allowed recovery operation reconstruct lost distinctions?
4. ACCESSIBILITY — can the specified observer/protocol access the relevant support?
5. CAUSALITY — can distinguishability/signals propagate between supports under the supplied evolution?
6. REPRESENTATION/FRAME COVARIANCE — which quantities change under admissible representation/reference-frame transformations and which structural content remains invariant?

No scalar has been found that safely replaces these six typed questions in general.

## PHY-047 — Relative/observer-indexed description does not imply subjective ontology
Lorentz frames, QRFs, Wigner-friend controls, local algebras, and observer projections all show that a description may be indexed by a frame/observer/access algebra while the underlying formal model remains objective and mathematically specified.

DSD rule candidate:
`description relative to X` must specify whether X changes coordinates, accessible algebra, subsystem decomposition, protocol, or physical state. Do not collapse all forms of relativity into one observer-dependence label.

## PHY-048 — Structure-first and representation-first reasoning must be audited in both directions
Failures found:
- coordinate singularity -> physical singularity: invalid without invariant audit;
- region -> Hilbert tensor factor: invalid in generic QFT;
- property name -> constitutive law/pointer basis: invalid;
- frame-relative entanglement -> formation change: invalid without invariant audit.

Conversely, refusing all representations is also unhelpful: explicit Lorentz, Hilbert, local-algebra, QRF, and constitutive bridges are needed for actual calculation.

Recommended discipline:

DSD core/typed structure
-> explicit domain bridge
-> representation-specific calculation
-> invariant/reconstruction audit back to typed structure.

## PHY-049 — Current frontier boundary
The first expanded QM/relativity/QFT contact map is now sufficiently populated to close as a first-stage interface study.

What remains as second-stage research rather than missing first-stage work:
- full modular theory specialization and half-sided modular inclusions;
- curved-spacetime relative entropy/QNEC applications;
- quantum clocks/relational time and Page-Wootters-type models;
- quantum reference frames with indefinite/quantum causal structures;
- gauge constraints and edge-mode/subsystem reconstruction;
- semiclassical gravity and backreaction;
- comparison with DSD Gravity only after each external bridge is separately audited.

No claim is made that DSD derives quantum mechanics, QFT, relativity, modular theory, or quantum gravity.
