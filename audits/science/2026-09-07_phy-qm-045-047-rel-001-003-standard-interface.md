# PHY-QM-045~047 / PHY-REL-001~003 — Standard Quantum Mechanics and Relativity Typed-Interface Audit

Date: 2026-09-07

## Method-family record

```text
METHODS: Analysis + Audit + Comparison + Reconstruction restraint
PRIMARY_EXTERNAL_BASE:
  standard finite-dimensional quantum mechanics
  special relativity
  general-relativistic geometric language only where explicitly stated
NONPRIMARY_QUANTUM_GRAVITY_PREMISES: not used
DSD_LAYERS_USED:
  Formation background where channel typing is needed
  General Property for typed descriptors
  Static Aggregation/reconstruction discipline for readout maps
  Dynamics only for ordering/transition questions
REPRODUCIBILITY_RECORD:
  audits/science/2026-09-07_qm_sr_typed_interface.py
```

The comparator-admission rule for this and later work is fixed in:

```text
methodology/STANDARD_THEORY_COMPARATOR_POLICY.md
```

Historical semiclassical or other unification-interface records remain archived as comparison history, but this continuation does not use them as premises.

---

## 1. Research question

The active task is not to force a quantum-gravity unification.

It is to ask what can be concluded from the independently standard structures of quantum mechanics and relativity when DSD tracks:

```text
structure,
describability,
dimension / term typing,
readout loss,
representation changes,
causal/ordering conditions,
explicit bridges.
```

The main firewall is:

```text
standard QM primitives are fixed from QM,
relativistic primitives are fixed from relativity,
DSD primitives are fixed from DSD,
then comparison maps are declared.
```

No cross-theory primitive is created from similar words or equal index counts.

---

# PHY-QM-045 — Quantum readout completeness is a fiber problem

Let the finite-dimensional quantum state carrier be

\[
\mathcal S_d
=
\{\rho\ge0:\operatorname{Tr}\rho=1\}
\]

on a Hilbert space of dimension \(d\).

For a measurement family \(\mathcal M=\{E_i\}\), the standard Born readout is

\[
\Phi_{\mathcal M}(\rho)
=
\bigl(\operatorname{Tr}(\rho E_i)\bigr)_i.
\]

Two states are operationally indistinguishable under the selected measurement family exactly when they lie in the same readout fiber:

\[
\Phi_{\mathcal M}(\rho_1)
=
\Phi_{\mathcal M}(\rho_2).
\]

Define \(X=\rho_1-\rho_2\). Then

\[
\operatorname{Tr}X=0,
\qquad
\operatorname{Tr}(XE_i)=0\quad\forall i.
\]

Therefore the measurement family is informationally complete on the state space precisely when

\[
\boxed{
X=X^\dagger,
\ \operatorname{Tr}X=0,
\ \operatorname{Tr}(XE_i)=0\ \forall i
\Longrightarrow X=0
}
\]

on the admissible difference space.

For a qubit, the traceless-Hermitian sector is three-dimensional. In Bloch coordinates:

```text
Z-only readout rank = 1
X,Y,Z readout rank  = 3
```

so Z-only measurement leaves a two-dimensional unresolved direction while the X/Y/Z family is informationally complete.

### DSD interpretation

This gives a clean standard-theory instance of

```text
underlying admissible state
!= selected operational readout
!= reconstructible state under a complete readout family.
```

The result is not a DSD quantum postulate. DSD contributes the fiber/reconstruction audit language.

### Verdict

- one measurement result family automatically describes the full quantum state: **REJECTED**
- informational completeness is a map/fiber condition: **CONFIRMED**
- equal output statistics under one measurement imply equal density operators: **REJECTED unless the family is informationally complete**

---

# PHY-REL-001 — Relativistic coordinate change is representation change, not automatic information loss

Let \(M\) be an \(n\)-dimensional spacetime manifold and let

\[
\chi:U\to\mathbb R^n
\]

be a coordinate chart.

By the chart construction, \(\chi\) is one-to-one on its domain \(U\). On an overlap of two valid charts, the transition map

\[
\chi'\circ\chi^{-1}
\]

is invertible where defined.

A Lorentz transformation in flat spacetime is a standard example of such an invertible representation change.

For a boost in one spatial direction,

\[
\det\Lambda=1
\]

and \(\Lambda^{-1}\) exists.

Therefore

\[
\boxed{
\text{invertible coordinate transformation}
\not\Rightarrow
\text{describability loss}
}
\]

by itself.

Loss appears only when the chosen readout is itself reduced, incomplete, outside a chart domain, quotient-like, or otherwise non-injective.

### Invariant relation example

Using signature \((-+++)\), proper time along a timelike curve \(\gamma\) is

\[
\tau[\gamma]
=
\frac1c\int
\sqrt{-g_{\mu\nu}\dot x^\mu\dot x^\nu}\,d\lambda.
\]

Its value is coordinate-independent even though the coordinate components used in the integrand change.

### DSD interpretation

DSD should separate at least:

```text
object/event carrier,
coordinate representation,
chart applicability,
invariant relation/property,
causal accessibility,
coarse readout.
```

### Verdict

- coordinate difference = information loss: **REJECTED**
- full valid chart change = invertible representation: **CONFIRMED**
- a coordinate scalar or partial projection may be lossy: **CONFIRMED**

---

# PHY-QM-046 / PHY-REL-002 — Typed-dimension non-identification

Three numerical dimensions may coexist in one analysis:

```text
d_H  : Hilbert-space dimension
n_M  : spacetime-manifold dimension
N_D  : number of selected DSD channels/terms or a DSD-specific finite rank
```

Even if

\[
d_H=n_M=N_D=4,
\]

this gives only an equality of cardinalities.

Mathematically, finite sets of equal cardinality admit bijections. But there is no canonical physical identification unless a bridge is separately declared.

Thus

\[
\boxed{
|A|=|B|
\not\Rightarrow
A\equiv B
\text{ as typed physical structures}
}
\]

and likewise

```text
Hilbert basis index
!= spacetime coordinate index
!= DSD channel index
```

unless an explicit mapping with independent justification is supplied.

### DSD consequence

This is especially important because DSD uses dimension, term, channel, and rank language. Equal counts must never be allowed to create a hidden cross-theory predefinition.

### Verdict

- equal index count creates a physical bridge: **REJECTED**
- typed dimension must be recorded before comparison: **CONFIRMED**
- numerical coincidence may motivate a later mapping search: **ALLOWED AS A QUESTION, NOT AS EVIDENCE**

---

# Combined theorem — product compatibility does not imply cross-dynamics

Let

\[
Q\subseteq S_Q
\]

be the admissible state set of a selected standard quantum model and

\[
R\subseteq S_R
\]

the admissible state set of a selected relativistic model.

If the only joint assumption is that both descriptions are simultaneously available, the minimal common carrier is simply

\[
Q\times R.
\]

Projection onto the quantum side is

\[
\pi_Q:Q\times R\to Q.
\]

For any fixed \(q\in Q\),

\[
\pi_Q^{-1}(q)=\{q\}\times R.
\]

If \(R\) contains more than one admissible relativistic state, this fiber is not a singleton. Therefore the relativistic state is not reconstructible from the quantum state under the product assumption alone.

Symmetrically, the quantum state is not reconstructible from the relativistic state if \(Q\) has more than one admissible element.

Hence

\[
\boxed{
\text{QM validity} + \text{relativity validity}
\not\Rightarrow
\text{a unique quantum-to-geometry or geometry-to-quantum law}
}
\]

without an additional constitutive bridge.

This is a logical countermodel to forced unification, not a claim that nature is literally a Cartesian product of independent sectors.

### DSD consequence

DSD may compare the two typed structures without pre-installing a cross-law. A cross-law is a new bridge and must carry its own evidence.

---

# PHY-QM-047 / PHY-REL-003 — Frame-order reversal and factorized quantum operations

Special relativity permits two spacelike-separated events \(A\) and \(B\) to have different coordinate-time order in different inertial frames.

Now consider a standard bipartite quantum carrier

\[
\mathcal H_A\otimes\mathcal H_B.
\]

Let an operation on subsystem \(A\) act as

\[
\mathcal E_A\otimes\operatorname{id}_B
\]

and an operation on subsystem \(B\) as

\[
\operatorname{id}_A\otimes\mathcal E_B.
\]

Because they act on separate tensor factors,

\[
\boxed{
(\mathcal E_A\otimes\operatorname{id}_B)
\circ
(\operatorname{id}_A\otimes\mathcal E_B)
=
(\operatorname{id}_A\otimes\mathcal E_B)
\circ
(\mathcal E_A\otimes\operatorname{id}_B)
}
\]

for the factorized operations under consideration.

The reproducibility script checks the elementary unitary instance

```text
U_A = X tensor I
U_B = I tensor Z
U_A U_B = U_B U_A
```

exactly.

### DSD lineage consequence

A coordinate-time ordering of two spacelike-separated, factorized operations must not automatically be promoted to a unique physical predecessor-successor lineage.

The relevant records are different:

```text
coordinate ordering,
causal relation,
operation carrier,
operation algebra,
DSD lineage claim.
```

A unique lineage requires additional physical structure beyond frame-dependent coordinate order.

### Boundary

This result does not say that every pair of relativistically localized quantum operations commutes. The statement is conditional on the explicitly supplied tensor-factor form above.

### Verdict

- frame-dependent coordinate order alone fixes unique physical lineage: **REJECTED**
- factorized operations on disjoint tensor factors commute: **CONFIRMED in the stated standard-QM specialization**
- DSD transition order should be inferred from coordinate labels alone: **REJECTED**

---

# Common operational record

A minimal typed experiment record can now be written schematically as

\[
\mathcal R
=
(\rho,\mathcal M,o;
 e,\chi(e),\gamma,\tau;
 C).
\]

The entries have different roles:

```text
rho        quantum state descriptor
M          quantum measurement / operation context
o          outcome record
e          spacetime event
chi(e)     coordinate representation of the event
gamma      worldline or trajectory where relevant
tau        invariant proper-time record where defined
C          additional experimental/contextual conditions
```

Standard quantum mechanics supplies probability/transition rules for the quantum portion.
Relativity supplies coordinate, causal, metric, and proper-time structure for the spacetime portion.
DSD supplies a typed structural-analysis layer over the combined record.

No quantum-to-curvature map is contained in this tuple by default.

---

# Consequence for the DSD gravity-principle line

The current standard-only architecture is therefore

```text
STANDARD QM BRANCH
  state -> selected measurement/operation -> readout fibers/reconstruction

STANDARD RELATIVITY BRANCH
  event/manifold -> coordinate representation -> causal/invariant structure

DSD TYPED COMPARISON
  keep dimensions, carriers, relations, and readouts distinct
  -> test explicit bridges only when supplied

DSD GRAVITY-PRINCIPLE BRANCH
  remains an independent constitutive/dynamical research line
  -> benchmark against standard relativity when gravity is tested
```

Quantum mechanics can constrain what source or state information is operationally distinguishable or reconstructible. It does not, by that fact alone, determine the DSD gravity response law.

Relativity can constrain geometric and causal behavior. It does not, by that fact alone, determine the quantum state law.

---

# Core-paper impact

No revision of the Formation Axiom System, Property Axiom System, Channel-Indexed Static Aggregation, or Structural Reorganization Dynamics is required by this stage.

The results reinforce existing DSD disciplines:

```text
typed carriers,
explicit bridges,
representation vs information-loss separation,
reconstruction only under injectivity/sufficiency,
lineage not inferred from coordinate labels alone.
```

---

# Verdict

**PASS_WITH_BOUNDARY.**

A standard-only QM/relativity interface is sufficient to produce several nontrivial structural constraints without importing another unification theory:

1. quantum reconstruction is readout-family dependent;
2. coordinate transformation and information loss are distinct;
3. Hilbert, spacetime, and DSD dimensions must be typed independently;
4. simultaneous validity of QM and relativity does not force a cross-dynamics;
5. frame-dependent coordinate order does not by itself define DSD lineage for factorized spacelike operations.

---

# Next target

Continue using standard theories only.

The next physically sharper comparison should be built from two independently standard controls:

```text
A. standard relativistic weak-field / proper-time benchmark
B. standard quantum wavepacket or internal-clock evolution on a supplied external potential/background
```

The audit should keep the background classical and externally supplied, then ask which observables distinguish:

```text
coordinate-time change,
proper-time change,
quantum phase/state change,
DSD describability/readout change.
```

No claim of quantum gravity is licensed by such a benchmark.

## Reproducibility

Run from the repository root:

```bash
python audits/science/2026-09-07_qm_sr_typed_interface.py --mode all
```

The script uses only the Python standard library.
