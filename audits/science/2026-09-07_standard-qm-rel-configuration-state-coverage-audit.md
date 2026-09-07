# Standard QM / Relativity — DSD Configuration-State Coverage Audit

Date: 2026-09-07
Status: **TRACK 2 ACTIVE — FIRST-PASS COVERAGE AUDIT**

## Purpose

Test how much of the previously listed foundations of **standard quantum mechanics** and **standard relativity** can be carried by the newly clarified DSD conditional describability/configuration state, and distinguish three outcomes:

1. structures that fit a single time-slice configuration state directly;
2. structures that require an explicit standard-domain relation or optional specialization in addition to the state;
3. structures that are inherently transition/trajectory-level and therefore require a separate temporal map.

This audit does **not** attempt to derive quantum mechanics, special relativity, or general relativity from DSD. It tests re-description and structural placement only.

Quantum-gravity and unification proposals are not used as premises.

---

## 1. DSD source lock

The current DSD papers imply the following separation.

- Formation gives the seven-stage static typed path to describable configurations, partial assignments, admitted channels, and finite composition.
- Property gives typed declarations, applicability, contextual prerequisites, and partial assignment over a fixed Stage-VI formation background.
- Static aggregation is downstream and explicitly not a complete state descriptor.
- Structural Reorganization Dynamics keeps a component-resolved time-indexed state and requires explicit cross-time lineage for formation-level changes; property data affect dynamics only through explicit constitutive dynamic data.

Accordingly, the one-slice configuration state used here is an audit-level profile

\[
\Sigma_t^\alpha
=
\bigl(F_{\alpha,t},P_{\alpha,t},R_{\alpha,t},A_{\alpha,t},\Phi_{\alpha,t}\bigr),
\qquad
\alpha\in\{Q,R\},
\]

where:

```text
F  DSD formation/admission status supplied for the selected description regime
P  DSD typed property/applicability/prerequisite status
R  standard-theory representation/carrier data
A  accessible subsystem/domain/carrier
Phi selected readout/representation-output map
```

This tuple is not a new DSD core axiom. It is the current comparison-state interface.

Temporal change is kept separate:

\[
\Gamma^\alpha_{t\to t'}:\Sigma_t^\alpha\to\Sigma_{t'}^\alpha.
\]

Standard equations, symmetry constraints, differential identities, and other theory-defining relations are not silently inserted into \(\Sigma_t\). When they are required, this audit labels them **RELATION / SPECIALIZATION** data.

---

## 2. Coverage labels

```text
STATE
  The full roadmap target can be structurally represented in one time-slice Sigma,
  provided the standard-theory primitive data are supplied externally.

RELATION
  A time-slice Sigma can carry the participating objects and values, but the full
  target also requires an explicit standard-domain relation, compatibility rule,
  group action, differential/geometric specialization, or global completion rule.

TRANSITION
  The full target is inherently post-state, trajectory, or multi-time and therefore
  requires Gamma or an equivalent explicit transition structure.
```

These labels classify structural placement, not originality, importance, or physical validity.

---

## 3. Standard quantum-mechanics coverage

| Roadmap target | First-pass placement | DSD re-description that survives | Boundary |
|---|---|---|---|
| State carrier and density operator | **STATE** | the density operator remains external QM state data in `R_Q`; DSD tracks whether it is admitted, accessible, and distinguishable under selected readouts | DSD does not derive positivity, trace-one normalization, Hilbert structure, or Born rule |
| Observable and POVM families | **STATE** | typed measurement context plus readout map `rho -> (Tr rho E_i)_i` fits `P_Q` and `Phi_Q` | POVM positivity/completeness and Born probabilities remain QM |
| Projective measurement and general instruments | **TRANSITION** | outcome/readout belongs to `Phi_Q`; post-measurement state change belongs to `Gamma_Q` | a POVM outcome and an instrument transition must not be collapsed into one state property |
| Composite systems, tensor products, subsystem restriction, partial trace | **STATE** | tensor decomposition is supplied in `R_Q`; subsystem access is an `A_Q` restriction; partial trace is a standard-QM restriction/readout map | tensor product and partial trace are not DSD-derived |
| Entanglement, separability, reconstruction boundary | **STATE** | separability/entanglement can be typed properties whose prerequisite includes the supplied tensor decomposition; local-access noninjectivity is a reconstruction issue | DSD property typing is not quantum entanglement |
| Contextuality: local contexts, overlaps, global completion | **RELATION** | local context-indexed records fit the Property layer; cross-context overlap/gluing is a separate compatibility/completion relation | the current Property core does not by itself derive Kochen–Specker contextuality |
| Symmetry/unitary representation and invariance | **RELATION** | states and transformed representations can sit in `R_Q`; invariance/equivalence is audited through explicit group action and comparison maps | group representation law and physical symmetry are standard-QM/domain input |
| Schrödinger/unitary and open-system CPTP evolution | **TRANSITION** | time-indexed state profiles can be related by `Gamma_Q`; closed/open evolution remain distinct typed transition classes | Hamiltonian, master equation, CPTP law are not obtained from static describability |
| Conservation relations | **TRANSITION** | conservation is a property of a trajectory/evolution law plus the relevant observable, not of a single snapshot merely by label | conservation requires standard dynamical assumptions such as symmetry/Hamiltonian structure |
| Identical-particle exchange structure | **RELATION** | particle labels, tensor carriers, and candidate state records can be typed; symmetric/antisymmetric sector restriction is an explicit standard-domain compatibility rule | Bose/Fermi exchange structure is not a generic DSD formation rule |

### Quantum first-pass count

```text
STATE      4 / 10
RELATION   3 / 10
TRANSITION 3 / 10
```

This count is only roadmap-item accounting. It is not a percentage of quantum mechanics.

The important result is that every listed finite-system target has a structural location without identifying a quantum primitive with a DSD primitive.

---

## 4. Standard relativity coverage

| Roadmap target | First-pass placement | DSD re-description that survives | Boundary |
|---|---|---|---|
| Manifold/event carrier and chart-domain structure | **STATE** | events and chart-domain data remain external relativistic representation data in `R_R`; chart applicability can be typed | DSD does not derive manifold dimension or smooth structure |
| Coordinate charts and invertible chart transitions | **STATE** | chart representation and reversible recoding fit `R_R`; invertibility preserves the distinction between representation change and information loss | coordinate change is not automatically a describability change |
| Frames, tetrads/congruences, worldline-dependent measurements | **STATE** | the frame/worldline/tetrad is a typed contextual input to `P_R`, `A_R`, or `Phi_R` as appropriate | a human observer is not required as a primitive |
| Metric structure, invariant interval, proper time | **STATE** | metric data and a supplied worldline/segment can determine typed invariant readouts; proper time is not identified with DSD temporal progression | metric signature, Lorentzian geometry, and proper-time law are standard relativity |
| Timelike/null/spacelike relations and causal accessibility | **STATE** | causal relation can be a typed relation on event pairs; causal-access restriction belongs to `A_R` | DSD does not derive the light cone from describability alone |
| Geodesic and accelerated motion | **TRANSITION** | current position/tangent/connection data can be stored in a snapshot, but geodesic/accelerated motion is a trajectory law | geodesic equation and force law are external standard dynamics |
| Curvature tensors and local/global geometry | **RELATION** | metric/connection data can be carried in `R_R`; curvature requires explicit differential-geometric specialization and compatibility relations | curvature is not generated by Property typing alone |
| Einstein field equation | **RELATION** | geometry-side and stress-energy-side typed records can be present simultaneously; the Einstein equation is an explicit standard-domain relation between them | no DSD aggregate is identified with `T_{mu nu}` and no gravitational normalization is derived |
| Weak-field limit and benchmark hierarchy | **RELATION** | exact and approximate representations can be placed in distinct typed regimes and compared by an explicit limit/approximation map | weak-field equations remain standard-relativity results |
| Initial-value/Cauchy structure and domain of dependence | **TRANSITION** | initial data, accessible domain, reconstruction, and future development fit `Sigma + Gamma` particularly well | uniqueness/existence/domain-of-dependence theorems remain standard hyperbolic/GR results |
| Stress-energy conservation and Bianchi consistency | **RELATION** | tensor fields and local identities can be typed; differential conservation/identity is a theory constraint on admissible geometry/matter records | it is not a static aggregate identity of DSD |
| Coordinate/gauge redundancy vs information loss | **STATE** | reversible gauge/coordinate representation changes can be distinguished from noninjective restriction/readout maps | physical gauge equivalence must be supplied by the standard theory |

### Relativity first-pass count

```text
STATE      6 / 12
RELATION   4 / 12
TRANSITION 2 / 12
```

Again, this is roadmap-item accounting only.

---

## 5. Combined first-pass result

Across the 22 non-QFT roadmap targets currently under direct comparison:

```text
STATE      10 / 22
RELATION    7 / 22
TRANSITION  5 / 22
UNPLACED    0 / 22  (first-pass structural placement only)
```

The strongest defensible interpretation is therefore:

\[
\boxed{
\text{the one-slice DSD configuration state captures a broad kinematic / applicability / access / readout layer,}
}
\]

but

\[
\boxed{
\text{it should not be enlarged until it also contains laws, symmetries, and trajectories as if they were state coordinates.}
}
\]

To preserve typing, the fuller analysis object should remain layered:

\[
\boxed{
\text{one-slice state }\Sigma_t
\quad + \quad
\text{explicit standard-domain relations}
\quad + \quad
\text{temporal transition }\Gamma.
}
\]

This is a structural organization claim, not an ontological hierarchy claim.

---

## 6. Where DSD re-description is genuinely useful

The comparison does more than rename standard objects in five places.

### 6.1 State / readout / reconstructibility separation

In standard QM a density operator, an accessible subsystem, and a selected POVM are not the same object. DSD keeps them in different roles. Hence equal measurement records need not reconstruct the underlying state, and subsystem restriction can enlarge indistinguishability fibers without saying that the underlying global state ceased to exist.

### 6.2 Outcome / transition separation

A measurement outcome and a post-measurement state update are structurally different. `Phi_Q` carries the readout; `Gamma_Q` carries the transition. This avoids treating measurement merely as a static property assignment.

### 6.3 Representation / access separation in relativity

An invertible chart or frame change can preserve all relevant information, whereas causal/domain restriction can remove access. DSD can represent both without using `observer difference` as a generic explanation.

### 6.4 Static geometry / geometric law separation

A metric, curvature record, stress-energy tensor, and Einstein equation have different logical roles. DSD can carry the records without making the law another ordinary property value or identifying the two sides by name.

### 6.5 Cauchy development as state + access + transition + reconstruction

The initial-value/domain-of-dependence structure is one of the strongest cross-checks for the current organization: a time slice carries initial data and access conditions, a standard evolution law supplies development, and reconstructibility is limited to the relevant domain of dependence. These roles are naturally distinct in DSD.

---

## 7. First genuine boundaries exposed by the comparison

The first pass also finds boundaries that should **not** be hidden by extending `Sigma` indiscriminately.

1. **Cross-context gluing** is not the same thing as a local Property prerequisite.
2. **Group/symmetry law** is not the same thing as a value attached to a state.
3. **Differential geometry and field equations** require explicit standard-domain relational structure.
4. **Evolution and conservation** are multi-time/trajectory structures, not one-snapshot descriptors.
5. **A complete placement of a standard object is not a derivation of its physics.**

These boundaries are positive audit results because they prevent a category mistake in which all external mathematics is absorbed into one oversized `configuration state` tuple.

---

## 8. Status of the challenge

### Confirmed in the first pass

- Every currently selected non-QFT foundational roadmap target has a structurally coherent place in the layered DSD analysis.
- Ten targets fit the present one-slice configuration state directly once their standard primitives are supplied.
- Seven require explicit relation/specialization data in addition to the state.
- Five require an explicit transition/trajectory layer.
- No core DSD paper must be changed on the basis of this first-pass coverage audit.

### Not established

- DSD does not derive Hilbert space, the Born rule, tensor-product composition, quantum contextuality, Lorentzian geometry, Einstein's equation, or the Cauchy theorems.
- The accounting above is not evidence that DSD is physically more fundamental than the standard theories.
- Structural re-description alone is not a quantum-gravity theory.

### Next detailed audit order

Proceed from the targets that most sharply test the state boundary:

```text
1. QM measurement: POVM readout vs instrument transition
2. QM composite access: tensor product / partial trace / entanglement
3. Relativity: chart/frame representation vs causal accessibility
4. Relativity: Cauchy data / domain of dependence / reconstruction
5. Standard-domain relation layer: symmetry, curvature, Einstein equation, conservation
```

---

## Standard-theory comparator references used for this first pass

- John Preskill, *Quantum Computation* lecture materials, Caltech: density operators, generalized measurements, quantum operations, entanglement, channels.
- Matteo G. A. Paris, *The modern tools of quantum mechanics*, arXiv:1110.6815: density operators, POVMs, quantum operations, completely positive maps.
- Sean M. Carroll, *Lecture Notes on General Relativity*, arXiv:gr-qc/9712019: manifolds, geometry, Einstein equations and standard GR structure.
- Standard globally-hyperbolic/Cauchy-problem literature is used only for the domain-of-dependence classification; no quantum-gravity premise is imported.

## Verdict

**PASS_WITH_BOUNDARY.**

The newly clarified DSD configuration state is broad enough to hold a substantial portion of the static/kinematic, applicability, access, representation and readout structure of standard QM and relativity. It is intentionally not broad enough to absorb every law or temporal relation into one snapshot. The correct generalization is layered state + explicit relation + transition, not a single totalizing state tuple.
