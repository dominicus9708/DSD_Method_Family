# QM Core Reconstruction 004G — Connected Reversible Group Gate

Date: 2026-09-08  
Status: **PASS_WITH_BOUNDARY**  
Program: **Core-Theory Reconstruction Challenge**  
Target: whether the CRG-QM lock isolated by QM Core 004E can be derived from current DSD dynamics/lineage or from the weaker continuous pure-state reachability selector already used in QM Core 004A.

## 1. Research question

QM Core 004E isolated

```text
CRG-QM = connected reversible group + pure-state transitivity
```

as one of the exact theorem-interface locks used by the selected finite-dimensional GPT reconstruction comparator.

The external comparator states Continuous Reversibility as two simultaneous requirements:

1. the reversible-transformation group is connected;
2. every pair of pure states is related by some reversible transformation.

The present DSD specialization had previously used the weaker idea that pure states may be continuously reachable through reversible evolution. This audit asks whether that weaker requirement, or DSD's own lineage/dynamics structure, forces connectedness of the entire allowed reversible group.

The answer is:

```text
pure-state continuous reachability -> full reversible-group connectedness   NO
Formation strict equivalence -> connected transformation topology          NO
regular time-indexed DSD dynamics -> connected full reversible group       NO
lineage preservation -> connected full reversible group                    NO
all allowed reversibles path-realizable from identity -> path-connected    YES
```

Therefore CRG-QM is **not derived** from current Class-A/Class-B structure.

## 2. Source-locked DSD distinctions

### 2.1 Formation equivalence is algebraic/model-theoretic, not topological

The Formation Axiom System defines forward formation maps, embeddings, and strict base-fixed formation isomorphisms. Identities, inverses, and compositions give categorical/equivalence structure.

This establishes a class of reversible comparison maps, but does not equip that class with:

```text
a topology
a Lie-group structure
an operator-norm topology
path components
connectedness
one-parameter generation from identity
```

Hence:

\[
\boxed{
\text{strict DSD equivalence}
\not\Rightarrow
\text{connected reversible transformation group}.
}
\]

### 2.2 Structural Reorganization Dynamics supplies trajectories, not exhaustion of all reversible symmetries

Structural Reorganization Dynamics is component-resolved and time-indexed. During a regular epoch it preserves the Stage-VI formation background while downstream property values, analytic fields, weights, and other coordinates may evolve according to supplied laws. Formation-level changes require explicit cross-time lineage.

The manuscript also keeps constitutive laws and analytic regularity specialization-dependent. A regular trajectory can therefore provide a continuous path of transformations in one part of the reversible set without implying that every admitted reversible comparison or symmetry lies on such a path.

Thus:

\[
\boxed{
\text{continuous regular trajectory}
\not\Rightarrow
\text{connectedness of the full allowed reversible set}.
}
\]

### 2.3 Lineage is succession identity, not group connectedness

Cross-time lineage records succession when literal Stage-VI identity cannot be retained. It answers which later structure descends from which earlier structure.

It does not state that every reversible endomorphism of a state carrier is realizable by a continuous regular-epoch trajectory from the identity.

Therefore lineage does not close the CRG-QM gap.

## 3. Exact countermodel — the circle with O(2)

Let the pure-state carrier be the unit circle

\[
S^1=\{(x,y)\in\mathbb R^2:x^2+y^2=1\}.
\]

Let all orthogonal transformations be admitted reversible transformations:

\[
G=O(2).
\]

### 3.1 Continuous pure-state reachability holds

For any two pure states

\[
x(\theta_1)=(\cos\theta_1,\sin\theta_1),
\qquad
x(\theta_2)=(\cos\theta_2,\sin\theta_2),
\]

define

\[
R_t=R\bigl(t(\theta_2-\theta_1)\bigr),
\qquad t\in[0,1].
\]

Then every \(R_t\in SO(2)\subset O(2)\), the path is continuous, and

\[
R_1x(\theta_1)=x(\theta_2).
\]

Thus every pair of pure states is connected by a continuous reversible path.

### 3.2 The full reversible group is nevertheless disconnected

The determinant map

\[
\det:O(2)\to\{+1,-1\}
\]

is continuous.

The identity has determinant \(+1\), while the reflection

\[
F=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}
\]

has determinant \(-1\).

Because a continuous image of a connected path must be connected, no continuous path in \(O(2)\) can join the identity to \(F\). Hence \(O(2)\) has at least two connected components.

Therefore:

\[
\boxed{
\text{continuous pure-state reachability}
\not\Rightarrow
\text{connected full reversible group}.
}
\]

This is the decisive countermodel for the current CRR-QM -> CRG-QM implication.

## 4. Why this countermodel is DSD-compatible

A DSD quantum specialization may place the circle states in one fixed operational carrier.

Regular dynamics may supply the rotation trajectories

\[
t\mapsto R_t
\]

while preserving the same formation background and lineage.

Separately, a reflection can be an admitted reversible representation/symmetry of the same carrier.

Nothing in the existing Formation or Dynamics cores requires the reflection to be generated by a continuous regular trajectory from the identity.

Therefore the DSD architecture is compatible with:

```text
continuous regular reversible dynamics in the identity component
+
a discrete reversible symmetry in another component
```

without contradiction.

## 5. Stronger sufficient lock

To obtain connectedness, the relevant extra condition is not merely continuous time dependence of some trajectories.

Define:

### RGPR-QM — Reversible-Group Path Realizability

Fix an explicit topology on the declared reversible transformation group \(G_N\). Require that for every

\[
T\in G_N
\]

there exists a continuous path

\[
\gamma_T:[0,1]\to G_N
\]

with

\[
\gamma_T(0)=I,
\qquad
\gamma_T(1)=T.
\]

Then \(G_N\) is path-connected, hence connected.

Pure-state transitivity must still be stated or derived separately:

\[
\forall\varphi,\omega\in\mathrm{Pure}(\Omega_N),
\quad
\exists T\in G_N:
T\omega=\varphi.
\]

Together these give the exact CRG-QM content required by the selected comparator.

## 6. Provenance classification

RGPR-QM/CRG-QM is not promoted to generic DSD.

Current provenance:

```text
CRG-QM / RGPR-QM    D  EXACT_COMPARATOR_LOCK
```

Reasons:

- generic Formation gives reversible isomorphism structure but no topology on the transformation class;
- generic Dynamics gives supplied trajectories but does not require all reversible maps to be dynamically generated;
- lineage gives succession identity but not transformation-group path connectedness;
- the stronger all-reversibles path-realizability condition is isolated here because the external reconstruction theorem explicitly requires a connected reversible group.

The earlier `CRR-QM` remains a weaker target-specialization selector and must not be treated as equivalent to CRG-QM.

## 7. Why generic DSD should not impose connectedness

Generic DSD must be able to represent discrete symmetries, permutation-like reversible maps, disconnected admissibility sectors, and regime changes without forcing all reversible descriptions into one continuous component.

Imposing connectedness universally would silently remove such models.

Therefore:

\[
\boxed{
\text{reversible-map connectedness is a physical specialization assertion, not a generic describability law}.
}
\]

## 8. Audit outcomes

```text
Claim: strict Formation equivalence implies connected reversible topology
Outcome: REJECTED

Claim: continuous regular DSD trajectories imply all reversibles lie in one component
Outcome: REJECTED

Claim: lineage preservation implies full reversible-group connectedness
Outcome: REJECTED

Claim: continuous pure-state reachability implies connected full reversible group
Outcome: REJECTED
Countermodel: O(2) acting on S^1

Claim: RGPR-QM + pure-state transitivity yields CRG-QM
Outcome: VALID_IN_DOMAIN
```

Overall audit verdict:

\[
\boxed{\textbf{PASS\_WITH\_BOUNDARY}}
\]

The gate succeeds by replacing an over-strong inference with an exact countermodel and by isolating the sufficient theorem-interface assumption without reclassifying it as DSD-derived.

## 9. Effect on QM Core 004E

The 004E entry

```text
CRG-QM  connected reversible group + pure-state transitivity
```

is now resolved as:

```text
NOT DERIVED FROM CLASS A/B
CRR-QM IS STRICTLY WEAKER
EXPLICIT CLASS-D RGPR-QM/CRG-QM ASSUMPTION REQUIRED FOR THE CHOSEN THEOREM INTERFACE
```

The theorem-transfer gate remains blocked by the remaining unresolved locks:

```text
ETC-QM
ULRRDE-QM
CFE-QM
```

OSC-QM and CRG-QM are now both classified rather than left as unspecified gaps.

## 10. External comparator note

Primary comparator:

- Markus P. Mueller, *Probabilistic Theories and Reconstructions of Quantum Theory (Les Houches 2019 lecture notes)*, arXiv:2011.01286.

In the reconstruction section, Continuous Reversibility is explicitly stated as connectedness of the reversible group together with pure-state transitivity. This external condition is used only as the comparator target; it is not imported into generic DSD.

## 11. Next target — QM Core 004H

Proceed to:

```text
ETC-QM = exact tomographic composite tensor lock
```

The next audit should distinguish:

1. injectivity of local-product readout,
2. vector-space dimension multiplication,
3. exact tensor-product carrier identity,
4. product-state/effect embeddings,
5. global relational degrees of freedom permitted by generic DSD,
6. whether CRD + LDC-QM can derive any of these without target fitting.

## 12. Reproducibility

Python:

```text
audits/science/2026-09-08_qm_core_004g_connected_reversible_group_gate.py
```

Run from repository root:

```bash
python audits/science/2026-09-08_qm_core_004g_connected_reversible_group_gate.py --mode all
```

Expected final line:

```text
OVERALL: PASS_WITH_BOUNDARY
```

Finite/algebraic witnesses implemented:

```text
continuous SO(2) rotation path between pure states
O(2) determinant-separated reversible components
pure-state continuous reachability without full-group connectedness
lineage-compatible regular dynamics plus discrete reflection symmetry
all-reversibles path-realizability as a sufficient connectedness lock
```
