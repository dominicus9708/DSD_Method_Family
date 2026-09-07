# Active Roadmap — Full DSD Structural Analysis of Standard Quantum Mechanics and Relativity

Date: 2026-09-07
Status: **ACTIVE TRACK (Track 2)**

## Activation note

Track 2 was activated after the first configuration-state coverage audit:

```text
audits/science/2026-09-07_standard-qm-rel-configuration-state-coverage-audit.md
```

First-pass accounting over the 22 non-QFT roadmap targets:

```text
STATE      10 / 22
RELATION    7 / 22
TRANSITION  5 / 22
UNPLACED    0 / 22  (structural placement only)
```

This count is a roadmap classification, not a measure of theoretical content and not a claim that DSD derives the standard theories.

The principal result is that the one-slice DSD configuration state should remain distinct from explicit standard-domain relations and temporal transition laws:

\[
\text{one-slice state }\Sigma_t
+\text{ explicit standard-domain relations}
+\text{ transition }\Gamma.
\]

## Purpose

Systematically test how far the foundations of **standard quantum mechanics** and **standard relativity** can be represented and audited through the DSD hierarchy without claiming that DSD derives, replaces, or is physically more fundamental than either standard theory.

The intended research question is:

> Can the principal foundational structures of standard QM and relativity be analyzed at a common DSD structuring level while preserving their independent physical primitives, and where does that common structuring cease to be adequate without additional domain-specific structure?

This is a formal/descriptive hierarchy question, not an ontological-unification claim.

---

## Comparator firewall

```text
PRIMARY BASE:
  standard quantum mechanics
  special relativity
  general relativity
  standard mathematical structures required by those theories

EXCLUDED AS PREMISES:
  quantum-gravity candidate theories
  unification theories
  speculative emergence identifications
  alternative gravity assumptions

RULE:
  lock standard-theory primitives independently;
  lock DSD primitives independently;
  only then declare explicit comparison maps.
```

Historical non-primary records may be retained as archived research objects but do not validate DSD and do not supply premises to this track.

---

## Common analysis order

For every standard-theory target, audit the following layers separately where applicable:

```text
1. Formation / admission
2. Typed Property declaration and applicability
3. Contextual prerequisites
4. Representation
5. Access / domain restriction
6. Readout
7. Fiber / identifiability
8. Reconstruction / completion
9. Dynamics / transition / lineage
10. Symmetry, invariance, conservation, and domain validation
```

Do not force every target through layers that are not mathematically meaningful for that target.

Scoped negative-looking outcomes are reported under:

```text
methodology/AUDIT_OUTCOME_SEMANTICS.md
```

so `FAIL` is not used for a valid in-domain object that is merely insufficient for an extension, non-identical to another object, or lossy for a stronger reconstruction target.

---

## Quantum-mechanics worklist

- [x] First-pass structural placement of state carrier and density-operator structure.
- [x] First-pass structural placement of observable and POVM families.
- [x] First-pass separation of projective/general measurement readout from instrument transition.
- [x] First-pass structural placement of composite systems, tensor products, subsystem restriction, and partial trace.
- [x] First-pass placement of entanglement, separability, and reconstruction boundaries without renaming them as DSD properties.
- [x] First-pass boundary: contextuality local records fit, cross-context gluing remains an explicit relation/extension.
- [x] First-pass boundary: symmetry/unitary representation requires explicit group/relation data.
- [x] First-pass placement of Schrödinger/unitary and open-system CPTP evolution in transition layer.
- [x] First-pass placement of conservation relations in trajectory/domain-validation layer.
- [x] First-pass placement of identical-particle exchange structure as explicit standard-domain relation.
- [ ] Standard QFT only as a later standard-domain extension, with a fresh primitive lock and without importing quantum-gravity assumptions.

Detailed audits remain pending even where first-pass placement is checked, except where explicitly marked complete below.

---

## Relativity worklist

- [x] First-pass placement of manifold/event carrier and chart-domain structure.
- [x] First-pass placement of coordinate charts and invertible chart transitions.
- [x] First-pass placement of reference frames, tetrads/congruences, and worldline-dependent measured quantities.
- [x] First-pass placement of metric structure and invariant interval/proper time.
- [x] First-pass placement of timelike/null/spacelike relations and causal accessibility.
- [x] First-pass placement of geodesic and accelerated motion in the transition/trajectory layer.
- [x] First-pass boundary: curvature requires explicit differential-geometric relation/specialization.
- [x] First-pass boundary: Einstein field equation remains an explicit standard-domain relation; no DSD source identification.
- [x] First-pass placement of weak-field limit and standard benchmark hierarchy as explicit comparison/approximation structure.
- [x] First-pass placement of initial-value/Cauchy structure and domain-of-dependence analysis in state + transition + reconstruction layers.
- [x] First-pass placement of stress-energy conservation and Bianchi consistency as standard-theory constraints.
- [x] First-pass separation of coordinate/gauge redundancy from genuine information loss/reconstruction.

Detailed audits remain pending even where first-pass placement is checked.

---

## Cross-standard-theory comparison worklist

- [x] First-pass common roles: formation, typed properties, representation, access, readout, reconstruction, dynamics survive as structural roles.
- [x] First-pass separation of reversible representation changes from non-injective restrictions in both theories.
- [x] First-pass comparison of subsystem access in QM with causal/domain access in relativity without identifying them.
- [ ] Compare standard invariants with DSD strict equivalence only through explicit maps.
- [x] Typed dimensions remain separated: Hilbert dimension, manifold dimension, probe count, DSD channel/term/rank counts.
- [ ] Search for detailed countermodels where one common role fails, becomes incomparable, or requires theory-specific extension.
- [ ] Record any genuinely common theorem only after it is proved from the abstract map/typing structure rather than imported from either theory.

---

## Detailed audit order now active

```text
1. DONE 2026-09-08 / PHY-QM-050
   QM measurement — POVM readout vs instrument transition
   result: PASS_WITH_REFINEMENT
   refinement: configuration-state completeness is relative to the declared system boundary;
               currently describable apparatus/control data belong in an experiment-complete
               one-slice record, while the actual instrument transition remains in Gamma.

2. DONE 2026-09-08 / PHY-QM-051
   QM composite access — tensor product / partial trace / entanglement
   result: PASS_WITH_REFINEMENT
   refinement: a reduced subsystem configuration state may be complete for its declared
               local query family while remaining insufficient for global reconstruction
               or entanglement classification; completeness is target/query-relative.

3. DONE 2026-09-08 / PHY-REL-005
   Relativity — chart/frame representation vs causal accessibility
   result: PASS_WITH_REFINEMENT
   refinement: invertible representation change, causal eligibility, operational access,
               and global reconstruction are distinct roles; a causally restricted record
               can be valid in-domain while non-injective for a global-reconstruction target.

4. NEXT
   Relativity — Cauchy data / domain of dependence / reconstruction

5. Standard-domain relation layer — symmetry, curvature, Einstein equation, conservation
```

Detailed audit records:

```text
audits/science/2026-09-08_phy-qm-050-configuration-state-povm-instrument-audit.md
audits/science/2026-09-08_phy-qm-051-configuration-state-composite-access-audit.md
audits/science/2026-09-08_phy-rel-005-configuration-state-frame-causal-access-audit.md
```

Reproducibility records:

```text
audits/science/2026-09-06_sequential_quantum_instrument_dsd_order.py
audits/science/2026-09-06_werner_dsd_entanglement_chsh.py
audits/science/2026-09-08_rel_chart_frame_causal_access.py
```

---

## Success criteria

The track succeeds even if the result is negative or limited.

Possible outcomes include:

```text
A. broad common structuring survives;
B. common structuring survives only for selected layers;
C. specific foundational sectors require new optional DSD interfaces;
D. an apparent commonality is only vocabulary-level and must be rejected;
E. standard-theory structure exposes a contradiction or overreach in a proposed DSD specialization.
```

A successful analysis does not require a quantum-gravity claim.

---

## Relation to Track 3

Track 3 applies existing DSD static aggregation and structural-reorganization dynamics to the already isolated common structuring roles.

Track 2 is now active as the breadth and boundary audit for that construction. Track 2 must not be backfilled with assumptions inferred from Track-3 outcomes.
