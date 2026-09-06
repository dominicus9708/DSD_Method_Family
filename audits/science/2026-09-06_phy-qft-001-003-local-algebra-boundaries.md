# PHY-QFT-001~003 — Relativistic QFT Boundary Audit for DSD Describability

Date: 2026-09-06

Status: PASS_WITH_MAJOR_BOUNDARY

This batch deliberately crosses the boundary from nonrelativistic quantum mechanics into relativistic quantum field theory / algebraic QFT. No QFT structure below is claimed to follow from the DSD core.

## PHY-QFT-001 — Microcausality is an algebraic locality condition, not automatically a DSD propagation-speed theorem

In algebraic/relativistic QFT, a spacetime region O is associated with a local observable algebra A(O). Standard locality/microcausality requires observables in spacelike separated regions to commute:

`[A(O1), B(O2)] = 0` when `O1` and `O2` are spacelike separated.

This gives an exact algebraic compatibility condition between spacelike local operations/observables.

DSD comparison:

- QFT microcausality presupposes a Lorentzian causal structure / spacelike separation.
- DSD `c_info` is only defined after localization, metric time, discrepancy convention, and evolution data are supplied.
- Therefore `microcausality = c_info` is rejected.

A future DSD-QFT specialization may relate the two only through an explicit bridge that maps the supplied DSD propagation support into the relativistic local-algebra net.

Verdict: **STRUCTURAL CONTACT, NOT IDENTIFICATION**.

## PHY-QFT-002 — Reeh-Schlieder and type-III local algebras defeat naive sharp-region tensor factorization

The Reeh-Schlieder theorem states, under standard AQFT hypotheses, that the vacuum is cyclic for the local algebra of any suitable nonempty open region. In practical terms, the orbit of the vacuum under local operators is dense in the Hilbert space.

This does not provide a bounded-energy deterministic superluminal remote-control protocol and does not violate operational relativistic causality.

A second boundary is that local von Neumann algebras in relativistic QFT are generically type III rather than the type-I factor structure familiar from finite-dimensional quantum mechanics.

DSD consequence:

A sharp spatial region should not automatically be represented as

`H = H_O tensor H_Oc`

with an ordinary reduced density matrix for every exact local region.

Thus the nonrelativistic DSD quantum specialization used in earlier audits,

`state -> subsystem tensor factors -> partial trace`,

cannot be promoted unchanged into a universal QFT rule.

The safer QFT-level typed object is something like

`LOCAL_ALGEBRA(region, causal geometry, representation)`

with subsystem factorization treated as an additional specialization when justified.

Verdict: **CORRECTION / BOUNDARY ADDED**.

## PHY-QFT-003 — Split property gives a conditional subsystem bridge

The split property addresses the previous obstruction. For suitable nested regions with a nonzero buffer, one may have a type-I factor N inserted between local algebras,

`A(O1) subset N subset A(O2)`.

This supports a subsystem-like interpretation between separated/nested localization regions under additional hypotheses such as nuclearity-type conditions.

DSD consequence:

The correct hierarchy is not

`spatial region -> tensor factor` universally,

but rather

`local region -> local algebra`

then, conditionally,

`buffer/separation + split property -> subsystem-like type-I bridge`.

This is highly compatible with DSD's existing rule that application-specific geometric/analytic/physical structure must be supplied at the layer where it is used rather than silently promoted into the universal Property core.

Verdict: **CONDITIONAL BRIDGE SURVIVES**.

## Combined QFT boundary map

The QFT extension therefore changes the DSD quantum interface from a purely tensor-product language into a two-level structure:

1. finite/nonrelativistic quantum specialization: Hilbert tensor factors, density operators, quantum instruments;
2. relativistic QFT specialization: causal spacetime regions, nets of local algebras, microcausality, with tensor-factor language only where a split/type-I bridge is actually available.

This avoids three overclaims:

- Bell nonlocality does not imply violation of microcausality;
- Reeh-Schlieder nonlocal-looking cyclicity does not imply signal propagation outside the light cone;
- local QFT regions are not automatically ordinary finite subsystems.

## External references

- Haag-Kastler / algebraic QFT locality: spacelike separated local observables commute.
- Fewster, C. J. (2015), *The split property for locally covariant quantum field theories in curved spacetime*, Lett. Math. Phys. / arXiv:1501.02682.
- Yngvason, J. (2005), *The role of type III factors in quantum field theory*, Rep. Math. Phys. 55, 135-147.
- Reeh-Schlieder reviews: local vacuum cyclicity under the standard AQFT hypotheses.
