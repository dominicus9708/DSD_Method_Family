# QM Core Reconstruction 004D — Convex Mixture / Affine Readout / Ordered Carrier Gate

Date: 2026-09-08  
Status: **PASS_WITH_REFINEMENT**  
Program: **Core-Theory Reconstruction Challenge**  
Target: whether randomized preparation, operational equivalence, and DSD readout structure can produce the convex/affine ordered-linear carrier used by finite-dimensional generalized probabilistic theories without presupposing Hilbert space.

## 1. Research question

QM Core 004C left the largest theorem-interface gap as:

```text
CONVEX MIXTURE
AFFINE READOUT
ORDERED LINEAR STATE CARRIER
```

The present gate asks:

1. Does generic DSD already imply convex closure under probabilistic mixing?
2. If an external classical randomizer is admitted as a physical preparation operation, does operational equivalence force convex mixture structure?
3. Does the same assumption force measurement readouts to be affine?
4. Do mixture-preserving transformations become affine?
5. Can an ordered positive cone and normalization functional be reconstructed from the resulting operational state classes?
6. Does this reconstruction also imply no-restriction/effect completeness?

The answers are:

```text
generic DSD -> convex closure                         NO
admitted randomizer + operational equivalence        YES, conditionally
randomized-preparation consistency -> affine readout YES
mixture-preserving transformations -> affine         YES
finite separating readouts -> ordered carrier        YES, conditionally
ordered carrier -> no-restriction                     NO
```

## 2. Source-locked DSD facts

The integrated DSD four-layer architecture does not already contain a universal randomized-preparation operation.

Formation Clause VII provides finite composition only after admitted channels have been formed and a post-Stage-VI term map has been supplied. It does not state that arbitrary probabilistic mixtures of physical preparations are admitted preparations.

The Static Aggregation paper proves linearity of the Bochner integral in the local term field after channel formation, while explicitly separating this analytic linearity from structural admission, quantity assignment, role formation, applicability, and property assignment. Therefore existing analytic linearity cannot be promoted into preparation convexity.

The Property Axiom System uses model-specific declared property families and partial assignments. Hence neither the availability of all convexly mixed preparations nor the availability of all affine effects follows from the generic property core.

Structural Reorganization Dynamics allows supplied dynamic operators and time-indexed static slices, but it does not silently add mixture closure or affine transformation laws.

Thus the gap is real:

\[
\boxed{
\text{linear downstream aggregation}
\not\Rightarrow
\text{convex closure of physical preparations}.
}
\]

## 3. DSD-native operational mixing condition

Let \(\mathcal P\) be a declared preparation carrier and \(\mathcal E\) a declared effect/readout family.

Define operational equivalence of preparations by complete declared statistics:

\[
P\sim Q
\iff
p(e|P)=p(e|Q)
\quad\forall e\in\mathcal E.
\]

Now introduce an explicit external classical randomizer. For \(\lambda\in[0,1]\), let

\[
R_\lambda(P,Q)
\]

mean: prepare \(P\) with probability \(\lambda\) and \(Q\) with probability \(1-\lambda\), while discarding the randomizer record before the downstream readout.

The randomizer is not inferred from DSD Formation. It is a declared physical preparation operation.

### Operational Randomization Equivalence — ORE

Require

\[
\boxed{
p(e|R_\lambda(P,Q))
=
\lambda p(e|P)+(1-\lambda)p(e|Q)
}
\]

for every declared effect \(e\).

This is the law of total probability for an explicitly supplied classical randomizer.

## 4. Conditional convexity theorem

Let

\[
\Omega:=\mathcal P/\!\sim
\]

be the quotient by complete declared readout equivalence.

Define

\[
\lambda[P]+(1-\lambda)[Q]
:=[R_\lambda(P,Q)].
\]

ORE makes this operation well-defined on equivalence classes, because replacing \(P,Q\) by operationally equivalent preparations preserves every effect statistic of the randomized preparation.

Therefore the operational state quotient is convex under every declared randomizer weight:

\[
\boxed{
[P],[Q]\in\Omega
\Longrightarrow
\lambda[P]+(1-\lambda)[Q]\in\Omega.
}
\]

This is a **conditional structural theorem**:

```text
DSD typed preparations/readouts
+ explicit randomizer
+ operational equivalence
+ total-probability consistency
-> convex operational state quotient.
```

It is not a theorem of generic DSD without the randomizer operation.

## 5. Affine readout is forced by randomized-preparation consistency

For every declared effect \(e\), define the quotient readout

\[
\hat e([P]) := p(e|P).
\]

ORE gives

\[
\boxed{
\hat e(\lambda\omega+(1-\lambda)\sigma)
=
\lambda\hat e(\omega)+(1-\lambda)\hat e(\sigma).
}
\]

Hence every declared readout is affine on the operational state space.

### Finite witness

For two preparations with effect statistics

\[
A=(1/4,3/4),
\qquad
B=(3/4,1/4),
\]

and \(\lambda=2/5\), the randomized preparation has

\[
\lambda A+(1-\lambda)B
=
(11/20,9/20).
\]

The exact Python witness verifies the identity.

## 6. Non-affine readout counterexample

Take a one-coordinate preparation representation \(x\in[0,1]\), with endpoint preparations \(x=0\) and \(x=1\).

A 50-50 randomization yields \(x=1/2\).

If one proposes the nonlinear readout

\[
e(x)=x^2,
\]

then

\[
e(1/2)=1/4,
\]

whereas randomization consistency requires

\[
\frac12e(0)+\frac12e(1)=1/2.
\]

Thus

\[
\boxed{1/4\ne1/2}.
\]

So a nonlinear readout of this type is incompatible with the declared meaning of operational mixing.

The point is not that all physical quantities must be affine. The result concerns **probability readouts on the quotient state carrier defined by randomized preparations**.

## 7. Mixture-preserving transformations are affine

Let \(T\) be a declared transformation on preparations.

If applying \(T\) after randomization is operationally equivalent to randomizing the transformed preparations,

\[
T(R_\lambda(P,Q))
\sim
R_\lambda(TP,TQ),
\]

then the induced state transformation obeys

\[
\boxed{
T(\lambda\omega+(1-\lambda)\sigma)
=
\lambda T(\omega)+(1-\lambda)T(\sigma).
}
\]

Hence it is affine.

The finite witness checks that \(T(x)=1-x\) commutes with mixing, while the nonlinear candidate \(N(x)=x^2\) does not.

This gives a DSD-compatible route from declared randomized preparation semantics to the affine reversible transformations used in GPT reconstruction.

## 8. Operational quotient and evaluation embedding

For a finite separating effect family \(\mathcal E=\{e_1,\ldots,e_m\}\), map every operational state to its full evaluation vector

\[
\iota(\omega)
=
(1,e_1(\omega),\ldots,e_m(\omega))
\in\mathbb R^{m+1}.
\]

If the effect family separates the declared operational states, \(\iota\) is injective.

ORE implies

\[
\iota(\lambda\omega+(1-\lambda)\sigma)
=
\lambda\iota(\omega)+(1-\lambda)\iota(\sigma).
\]

Thus the normalized operational state space is represented as a convex subset of a real vector space without assuming Hilbert structure.

## 9. Ordered carrier construction

Define

\[
V:=\operatorname{span}\iota(\Omega)
\]

and the positive cone

\[
V_+
:=
\operatorname{cone}\iota(\Omega)
=
\left\{
\sum_k a_k\iota(\omega_k):a_k\ge0
\right\}.
\]

Define the normalization functional

\[
u(v):=\text{first coordinate of }v.
\]

Then normalized states satisfy

\[
u(\iota(\omega))=1.
\]

For every nonzero \(v\in V_+\), \(u(v)>0\), so the cone is pointed in this evaluation representation.

The finite Python witness verifies closure under positive addition and positive scaling.

Thus, under finite separating readouts, DSD operational classes plus ORE yield the standard ordered-linear **carrier shape** used by finite-dimensional GPTs:

\[
\boxed{
(V,V_+,u,\Omega).
}
\]

This is not yet Hilbert space and does not select the quantum cone.

## 10. No-restriction remains independent

The ordered carrier construction does not imply

\[
E_{\mathrm{phys}}=E_{\max}(\Omega).
\]

A classical two-state witness can possess a perfectly valid convex ordered state carrier while the physically declared effects form a strict subset of all mathematically admissible affine effects.

The exact grid witness retains only four effects out of nine admissible grid effects while preserving the ordered state carrier.

Hence

\[
\boxed{
\text{convex ordered carrier}
\not\Rightarrow
\text{no-restriction}.
}
\]

QM Core 004C's NR-QM therefore remains an independent quantum-specialization selector.

## 11. Relation to QM Core 003

QM Core 003's effect valuation should now be read in the following order:

```text
randomized preparation semantics
-> convex operational states
-> affine probability readouts
-> declared effect-domain gluing/normalization
-> finite additivity/coarse-graining
-> full Born trace form only under sufficient quantum effect-domain assumptions.
```

Thus 004D strengthens the structural basis of 003 without removing 004C's effect-domain qualification.

## 12. Relation to current DSD papers

The new result must not be confused with existing Static Aggregation linearity.

The static paper proves linearity of the Bochner integral at fixed channel data. That result is downstream analytic linearity.

004D instead derives **affinity of operational probability readouts** from an explicitly supplied randomized preparation semantics.

Therefore the two statements occupy different layers:

\[
\boxed{
\text{analytic term linearity}
\neq
\text{operational mixture affinity}.
}
\]

No current DSD core paper needs to be rewritten to pretend that preparation convexity was already present.

## 13. Proposed DSD interfaces

### 13.1 Operational Randomization Declaration — ORD

Whenever a DSD physical specialization uses probabilistic preparation mixing, declare:

```text
PREPARATION_CARRIER
RANDOMIZER_WEIGHT_DOMAIN
RANDOMIZED_PREPARATION_OPERATION
RANDOMIZER_RECORD_RETAINED_OR_DISCARDED
READOUT_CONSISTENCY_RULE
OPERATIONAL_EQUIVALENCE_RELATION
```

### 13.2 Operational Randomization Equivalence — ORE

For discarded randomizer record:

\[
\boxed{
p(e|R_\lambda(P,Q))
=
\lambda p(e|P)+(1-\lambda)p(e|Q).
}
\]

### 13.3 Mixture-Preserving Transformation criterion — MPT

For a declared state transformation \(T\):

\[
\boxed{
T\circ R_\lambda
\sim
R_\lambda\circ(T\times T)
}
\]

on the preparation quotient.

This yields affine state transformations.

## 14. Comparison with standard GPT structure

Mueller's GPT lecture notes motivate convexity from the ability to probabilistically mix preparations, define a finite-dimensional real vector space carrying a compact convex normalized state set, construct the positive state cone, and use a linear normalization functional.

The notes' reconstruction theorem later assumes finite-dimensionality, no-restriction, Tomographic Locality, the Subspace Axiom, and Continuous Reversibility.

The DSD quantum-reconstruction package now has explicit counterparts for the operational content of all of these except that the exact theorem-interface equivalences still require a dedicated lock audit.

Current package:

```text
ORD/ORE  operational randomized preparation and convexity
MPT      affine mixture-preserving transformations
OCD      operational capacity
EDD      effect-domain declaration
NR-QM    no-restriction selector
CRD      explicit composite declaration
LDC-QM   local descriptive completeness
RRDE-QM  recursive restriction equivalence
CRR-QM   continuous reversible reachability
```

External comparators:

- Markus P. Mueller, *Probabilistic Theories and Reconstructions of Quantum Theory*, arXiv:2011.01286.
- Lluis Masanes and Markus P. Mueller, *A derivation of quantum theory from physical requirements*, arXiv:1004.1483.

## 15. What is and is not established

Established conditionally:

\[
\boxed{
\text{declared classical randomizer}
+
\text{complete operational quotient}
\Rightarrow
\text{convex state structure + affine readouts}.
}
\]

With finite separating readouts:

\[
\boxed{
\text{convex operational states}
\Rightarrow
\text{finite-dimensional ordered evaluation carrier}.
}
\]

Not established:

```text
generic DSD automatically contains randomization
compactness for arbitrary infinite state families
no-restriction from convexity
complex Hilbert geometry from ordered convexity alone
exact equivalence of DSD selectors to every hypothesis of the external reconstruction theorem
```

## 16. Next target — QM Core 004E

The next gate should be an **exact theorem-interface lock** rather than adding another principle.

Questions:

1. Does ORD/ORE + finite separation reproduce the precise convex-state assumptions used by the chosen GPT theorem?
2. Does MPT reproduce the required affine transformation structure?
3. Does LDC-QM exactly imply the theorem's Tomographic Locality once CRD is fixed?
4. Does RRDE-QM exactly match the theorem's Subspace Axiom on both states and reversible transformations?
5. With NR-QM explicitly adopted, is there any remaining hypothesis gap before the external theorem can be invoked conditionally?
6. If no gap remains, state the result only as a **conditional external reconstruction theorem instantiated by a DSD specialization**, not as a derivation of quantum mechanics from generic DSD.

## 17. Reproducibility

Python:

```text
audits/science/2026-09-08_qm_core_004d_convex_mixture_ordered_carrier_gate.py
```

Run from repository root:

```bash
python audits/science/2026-09-08_qm_core_004d_convex_mixture_ordered_carrier_gate.py --mode all
```

Expected final line:

```text
OVERALL: PASS_WITH_REFINEMENT
```

Finite witnesses implemented:

```text
randomized preparation -> affine statistics
non-affine readout counterexample
operational quotient convexity
ordered cone construction
mixture-preserving transformation -> affine
ordered carrier != no-restriction
```

## 18. Verdict

\[
\boxed{\textbf{PASS\_WITH\_REFINEMENT}}
\]

Refinements established:

1. Generic DSD does not itself imply operational convexity.
2. Explicit classical randomization plus operational equivalence yields convex state classes.
3. Probability readouts are forced to be affine under randomized-preparation consistency.
4. Transformations commuting with randomization are affine on the quotient state space.
5. Finite separating readouts yield a real ordered evaluation carrier with a positive cone and normalization functional.
6. Ordered convex structure does not imply no-restriction.
7. Existing DSD analytic linearity and new operational mixture affinity are distinct layers.
8. The next step is an exact interface audit against the external GPT reconstruction theorem.
