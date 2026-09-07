# DSD Gravity-Principle Research Log — Experiments 647–655

Date: 2026-09-07

Active comparator policy:

```text
methodology/STANDARD_THEORY_COMPARATOR_POLICY.md
```

The current gravity/QM/relativity line uses standard theories as the primary external basis. Historical interface work involving semiclassical or other unification literature is preserved but is not used as a premise here.

---

## Experiment 647 — standard-theory comparator firewall

### Result

The active research line now separates three layers before comparison:

```text
standard-theory primitives locked independently,
DSD primitives locked independently,
only then explicit comparison maps.
```

Shared vocabulary, equal index counts, or similar mathematical roles do not create a bridge.

Preferred external sources are domain-standard structures such as standard QM, SR/GR, thermodynamics, electromagnetism, classical/statistical mechanics, and standard particle/QFT structures when actually required.

Alternative or speculative unification theories may later be research objects, but not current validation premises.

### Verdict

- nonstandard unification theory as present foundation: **REJECTED**
- standard-domain theory chosen minimally by task: **CONFIRMED POLICY**
- historical records deleted because policy changed: **REJECTED; preserve history**

---

## Experiment 648 — three kinds of dimension must remain typed

### Result

At least three independent dimensions can coexist:

\[
d_H=\dim\mathcal H,
\qquad
n_M=\dim M,
\qquad
N_D=\text{selected DSD channel/term count or DSD-specific finite rank}.
\]

Even if

\[
d_H=n_M=N_D,
\]

only the numerical cardinality agrees.

Equal cardinality permits mathematical bijections between finite label sets but supplies no canonical physical identification.

Hence

\[
\boxed{
\text{Hilbert index}
\neq
\text{spacetime index}
\neq
\text{DSD channel index}
}
\]

without an explicit bridge.

### Consequence

This blocks a major source of predefinition contamination in a DSD theory that itself uses dimension, term, channel, and rank language.

### Verdict

- equal count implies same physical dimension: **REJECTED**
- typed dimension lock before comparison: **CONFIRMED**

---

## Experiment 649 — standard-QM tomography as describability fiber

### Result

For a density operator \(\rho\) and POVM/effect family \(\{E_i\}\), define the standard Born readout

\[
\Phi_{\mathcal M}(\rho)
=
(\operatorname{Tr}(\rho E_i))_i.
\]

A measurement family uniquely reconstructs the state only if

\[
\boxed{
X=X^\dagger,
\ \operatorname{Tr}X=0,
\ \operatorname{Tr}(XE_i)=0\ \forall i
\Rightarrow X=0
}
\]

on the admissible difference space.

For a qubit in Bloch coordinates:

```text
Z-only readout rank = 1
XYZ readout rank    = 3
```

so measurement completeness is a readout/fiber property, not a property automatically inherited from the existence of the quantum state.

### DSD consequence

Quantum state describability, selected measurement describability, and reconstructibility must remain different records.

### Verdict

- one selected measurement equals complete state description: **REJECTED**
- informational completeness as fiber/kernel condition: **CONFIRMED**

---

## Experiment 650 — relativity: coordinate representation and invariant structure

### Result

A valid chart

\[
\chi:U\to\mathbb R^n
\]

is injective on its chart domain. Valid chart transitions are invertible where defined. Lorentz transformations supply the flat-spacetime control case.

Thus an invertible coordinate change is not itself information loss.

With signature \((-+++)\), proper time along a timelike worldline satisfies

\[
\tau[\gamma]
=
\frac1c\int
\sqrt{-g_{\mu\nu}\dot x^\mu\dot x^\nu}\,d\lambda,
\]

and is independent of which valid coordinates are used to calculate it.

### DSD consequence

Separate:

```text
event/object,
coordinate representation,
chart applicability,
invariant relation,
causal accessibility,
reduced/coarse readout.
```

### Verdict

- coordinate change = describability loss: **REJECTED**
- full valid coordinate transformation as invertible representation: **CONFIRMED**

---

## Experiment 651 — product-carrier countermodel to forced unification

### Result

Let \(Q\) be an admissible standard-QM state set and \(R\) an admissible relativistic state set.

If the only joint premise is that both descriptions are valid, a minimal joint carrier is

\[
Q\times R.
\]

For fixed \(q\in Q\), the projection fiber is

\[
\pi_Q^{-1}(q)=\{q\}\times R.
\]

If \(|R|>1\), the relativistic state is not reconstructible from \(q\) alone.
The symmetric statement holds for reconstructing the quantum state from a relativistic state when \(|Q|>1\).

Therefore

\[
\boxed{
\text{standard QM} + \text{standard relativity}
\not\Rightarrow
\text{a unique cross-dynamics}
}
\]

without an extra constitutive bridge.

This is a logical countermodel only; it does not assert that physical reality factorizes exactly as a Cartesian product.

### Verdict

- coexistence of the two standard theories forces quantum-to-geometry law: **REJECTED**
- cross-dynamics must be an additional bridge: **CONFIRMED**

---

## Experiment 652 — common typed experiment record

### Result

A minimum cross-domain experiment record can be represented schematically as

\[
\mathcal R
=(\rho,\mathcal M,o;
  e,\chi(e),\gamma,\tau;
  C).
\]

The quantum and relativistic entries retain separate roles:

```text
rho       quantum state descriptor
M         quantum measurement/operation context
o         outcome record
e         spacetime event
chi(e)    coordinate representation
gamma     worldline/trajectory where relevant
tau       proper-time record where defined
C         other experimental/contextual conditions
```

Standard QM supplies probability/transition structure for the quantum portion. Relativity supplies coordinate, causal, metric, and proper-time structure for the spacetime portion.

DSD can analyze the typed combined record without adding a quantum-to-curvature law.

### Verdict

- common record requires primitive unification: **REJECTED**
- typed product/interface record is sufficient for structural comparison: **CONFIRMED**

---

## Experiment 653 — spacelike frame-order reversal vs factorized quantum operations

### Result

Special relativity permits the coordinate-time order of spacelike-separated events to reverse between inertial frames.

For a standard bipartite quantum carrier \(\mathcal H_A\otimes\mathcal H_B\), factorized operations

\[
\mathcal E_A\otimes\operatorname{id}_B,
\qquad
\operatorname{id}_A\otimes\mathcal E_B
\]

commute:

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

in the stated specialization.

The reproducibility control uses

```text
U_A = X tensor I
U_B = I tensor Z
```

and verifies exact commutation.

### DSD lineage consequence

A frame-dependent coordinate order must not automatically be promoted to a unique physical predecessor-successor lineage for such factorized operations.

### Boundary

The result is not generalized to arbitrary relativistically localized quantum operations. The tensor-factor bridge is an explicit assumption.

### Verdict

- coordinate time order alone determines DSD lineage: **REJECTED**
- factorized local operations commute in the stated standard-QM case: **CONFIRMED**

---

## Experiment 654 — effect on the DSD gravity-principle source question

### Result

The standard-only split now assigns different tasks to the quantum and relativistic branches.

```text
QM branch:
  distinguishability,
  measurement completeness,
  state reconstruction,
  operation structure.

Relativity branch:
  geometry,
  causal relation,
  coordinate/invariant separation,
  proper time,
  classical gravity benchmarks.

DSD gravity-principle branch:
  independent source/response bridge,
  distortion/progression/axis response,
  c_info and downstream dynamics.
```

Quantum mechanics may determine whether a proposed source descriptor is operationally reconstructible under a stated measurement family. That does not make the descriptor a gravitational source.

Relativity may determine what a correct classical gravitational benchmark must reproduce. That does not determine the quantum state.

### Verdict

- quantum readout sufficiency = gravitational-source sufficiency: **REJECTED**
- relativistic geometry = quantum-state law: **REJECTED**
- both can independently constrain a future DSD bridge: **CONFIRMED**

---

## Experiment 655 — next standard-only benchmark fixed

### Target

Use no alternative quantum-gravity theory.

Construct a controlled benchmark from:

```text
A. standard relativistic weak-field/proper-time structure
B. standard quantum wavepacket or internal-clock evolution on an externally supplied classical potential/background
C. DSD typed describability comparison
```

The classical background remains supplied from standard theory; it is not derived from the quantum state.

Audit separately:

```text
coordinate-time change,
proper-time change,
quantum phase/state change,
measurement/readout change,
DSD describability change,
DSD gravity-principle response if and only if a separate bridge is supplied.
```

### Expected value of the benchmark

This next stage can test whether DSD successfully separates several quantities that are often verbally merged under the word `time`, while avoiding any assumption that a quantum-gravity theory has already decided their relationship.

### Verdict

- target admitted: **CONFIRMED**
- quantum-gravity interpretation preinstalled: **REJECTED**

---

## Combined result

The current safe architecture is

```text
STANDARD QM
  -> state / measurement / operation / reconstruction

STANDARD RELATIVITY
  -> spacetime / coordinates / causal structure / proper time / gravity benchmark

DSD METHOD FAMILY
  -> typed structure / describability / dimension-term separation
  -> readout-fiber and bridge audits
  -> lineage audit

DSD GRAVITY-PRINCIPLE RESEARCH
  -> independent constitutive branch
  -> compared with standard relativity when a gravitational claim is made
```

No DSD core-paper modification is required.

## Reproducibility

Run from repository root:

```bash
python audits/science/2026-09-07_qm_sr_typed_interface.py --mode all
```

The script uses only the Python standard library.
