# PHY-QFT-012~014 — Semiclassical Gravity, Relative Cauchy Evolution, and Local Covariance Audit

Date: 2026-09-07

## Scope
The semiclassical Einstein equation, renormalized stress-energy tensor, Hadamard condition, relative Cauchy evolution, and locally covariant QFT are external standard-theory structures. This audit asks which of them can be connected to current DSD layers without silently importing a physical law.

## PHY-QFT-012 — Semiclassical gravity is a real QM-relativity junction, but not yet a DSD-gravity bridge
A schematic semiclassical Einstein equation is

G_{mu nu} + Lambda g_{mu nu} + [renormalized local curvature terms]
    = 8*pi*G <T_{mu nu}>_{omega,ren}.

The right-hand side is not a raw finite aggregate. It depends on

- a quantum field theory on the chosen curved spacetime,
- a suitable state omega,
- a renormalized stress-energy prescription,
- local/covariant renormalization data and finite renormalization freedoms.

Hadamard/microlocal conditions are central in standard QFT in curved spacetime for controlling the short-distance singular structure and defining renormalized composite observables such as the stress-energy tensor.

### DSD audit
Current DSD Property and Static Aggregation layers do not supply a quantum field algebra, a Hadamard state, a stress tensor, or the Einstein coupling. Therefore none of the following identifications is licensed:

```text
DSD static aggregate = <T_mu nu>_ren
DSD source density rho = full quantum stress tensor
DSD gravity mu_0 = 1/(8*pi*G)
Hadamard admissibility = DSD resolution
```

The strongest safe conclusion is that semiclassical gravity supplies an **external bridge candidate** at which a future DSD quantum specialization and DSD gravity specialization could be compared quantitatively.

Candidate audit label:

```text
SEMICLASSICAL-SOURCE BRIDGE AUDIT
```

## PHY-QFT-013 — Relative Cauchy evolution supplies a background-response comparator
Locally covariant QFT compares the theory on a spacetime with the theory after a compactly supported perturbation of the background metric through relative Cauchy evolution. In standard free-field settings, the infinitesimal response to metric variation is related to the stress-energy tensor.

### Structural contact with DSD
This has a genuine pattern-level resemblance to a DSD constitutive response:

```text
background perturbation
    -> response automorphism / observable change
    -> generator tied to stress-energy
```

Current DSD dynamics, however, requires physical roles to enter through an explicit constitutive bridge. The resemblance therefore supports an audit target, not an identification.

Unsafe claims:

```text
DSD constitutive bridge = relative Cauchy evolution
DSD axis/progression response generator = quantum stress tensor
metric variation automatically defines DSD gravity source
```

Safe research question:

```text
Given an explicit DSD quantum representation and an explicit DSD gravity metric/progression representation,
can their response maps be compared with relative Cauchy evolution on a common admissible state class?
```

Candidate audit label:

```text
BACKGROUND-RESPONSE AUDIT
```

## PHY-QFT-014 — Local covariance and DSD covariance are analogous in role, not identical in mathematics
Locally covariant QFT is formulated functorially: suitable globally hyperbolic spacetimes and admissible embeddings are mapped to algebras and algebra morphisms while preserving the theory's local structure.

Current DSD comparison/representation layers instead use their own typed records, forward maps, embeddings, strict equivalence conditions, optional representations, and downstream transport/covariance assumptions.

### Comparison

```text
LCQFT:
  spacetime category
    -> observable-algebra category
    -> natural/local covariant structure

DSD:
  typed formation/property state
    -> optional representation / analytic bridge
    -> map-specific covariance or strict-equivalence conditions
```

The shared methodological pattern is "state the carrier/category and preservation conditions before calling a transformation covariant." The mathematical categories and preserved objects are nevertheless different.

Therefore

```text
LCQFT local covariance = DSD strict equivalence
```

is rejected.

A future common interface would need an explicit functor or representation bridge from a DSD-admitted physical specialization to the spacetime/algebra structures used by LCQFT.

Candidate audit labels:

```text
LOCAL-COVARIANCE TYPE AUDIT
LOCAL-ALGEBRA / SUBSYSTEM AUDIT
```

## Impact on DSD Gravity
The standard semiclassical equation makes a useful boundary visible:

```text
quantum state + local QFT + renormalized stress tensor
    -> semiclassical source
    -> classical geometric response
```

whereas the present DSD-gravity chain is separately

```text
DSD formation/property
    -> explicit physical constitutive specialization
    -> progression/axis response sectors
    -> conditional gravity-like dynamics.
```

The two chains currently have no proved equality map. This is a productive open interface rather than a defect to hide.

## External references
- S. Hollands, R. M. Wald, Quantum fields in curved spacetime, arXiv:1401.2026.
- C. J. Fewster, R. Verch, Algebraic Quantum Field Theory in Curved Spacetimes, arXiv:1504.00586.
- K. Sanders, Aspects of locally covariant quantum field theory, arXiv:0809.4828.
- Recent semiclassical-gravity reviews and Hadamard/RSET initial-value analyses.

## Verdict
PASS_WITH_BOUNDARY.

Semiclassical gravity is the first standard-theory interface in this audit where quantum state data and relativistic geometry are explicitly coupled. It does not close the DSD-gravity normalization/source problem; instead it specifies additional data that any future DSD-QFT-gravity bridge would have to supply or reproduce.
