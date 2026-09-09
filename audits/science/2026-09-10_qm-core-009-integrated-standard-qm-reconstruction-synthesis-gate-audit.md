# QM Core Reconstruction 009 — Integrated Standard-QM Reconstruction Synthesis / Provenance Closure Gate

Date: 2026-09-10  
Status: **PASS_WITH_BOUNDARY**  
Program: **Core-Theory Reconstruction Challenge**  
Scope: integrate QM Core 001R–008 and determine exactly which parts of ordinary standard quantum mechanics are pre-existing DSD structure, general operational consequences, quantum-specific selectors, standard theorem consequences, or still external/not independently derived.

## 1. Final synthesis question

The sequence began by asking whether standard quantum mechanics could be reconstructed inside the four-layer DSD architecture

```text
Formation Axiom System
Property Axiom System
Channel-Indexed Static Aggregation
Structural Reorganization Dynamics
```

without silently treating a quantum specialization as if it had already been implied by generic DSD.

The final questions are:

1. What was already present in DSD before the quantum target?
2. What follows from target-independent operational assumptions?
3. Which specifically quantum structures still have to be selected or supplied?
4. Which familiar quantum formulas and representations then follow from standard theorems?
5. Does the complete 001R–008 chain amount to an independent derivation of ordinary complex quantum mechanics?

The final answer to Question 5 is **no**.

The chain gives a strong **conditional reconstruction**, not an independent derivation of the complex Hilbert carrier.

## 2. Source hierarchy fixed for this synthesis

The DSD side is read in the following dependency order.

```text
Formation
    -> admitted typed operational channels and status distinctions

Property
    -> typed property profiles, applicability, prerequisites, partial assignments

Static Aggregation
    -> explicit downstream readouts with information-loss / injectivity criteria

Dynamics
    -> time-indexed admissible slices, regular evolution, lineage,
       constitutive bridges, and transition typing
```

The core papers explicitly keep downstream representation choices separate from predecessor definitions. In particular:

- Formation keeps undefined assignment, defined zero, channel absence, and zero contribution distinct.
- Property keeps undeclared, inapplicable, prerequisite-unsatisfied, undefined, defined-zero, and defined-nonzero statuses distinct.
- Static Aggregation does not identify an aggregate with the full typed support and states exact kernel/injectivity conditions for reconstruction.
- Dynamics fixes the Stage-VI formation background during a regular epoch and requires explicit lineage for formation-level change.

These are the DSD structures that are allowed to count as pre-quantum evidence.

## 3. Final provenance classes

The synthesis uses five final classes.

```text
P0  PRE_EXISTING_DSD
P1  GENERAL_OPERATIONAL
P2  QUANTUM_SELECTOR
P3  STANDARD_THEOREM_CONSEQUENCE
P4  REMAINS_EXTERNAL / NOT INDEPENDENTLY DERIVED
```

They refine the earlier 004 ledger.

```text
A PRE_EXISTING_DSD                -> P0
B GENERAL_OPERATIONAL_DERIVATION  -> P1
C TARGET SPECIALIZATION SELECTOR  -> P2
D EXACT COMPARATOR LOCK           -> P2 or P4 depending on role
```

Only P0 and independently validated P1 items count as target-independent reconstruction evidence.

P2 items may be coherent and physically standard, but they are still supplied target structure.

P3 items are genuine deductions once their P2/P1 hypotheses are present, but they do not retroactively turn those hypotheses into DSD theorems.

## 4. P0 — what DSD independently contributes

### 4.1 Typed identity and status discipline

Formation and Property independently provide distinctions later needed in quantum measurement theory:

```text
absent
inapplicable
prerequisite-unsatisfied
undefined
defined zero
defined nonzero
```

This is the structural reason the 005B instrument gate can correctly separate

```text
branch operator = 0       DEFINED_ZERO
branch probability = 0    DEFINED_ZERO
conditional normalized state
                         UNDEFINED
```

without zero-padding undefined data.

### 4.2 Restriction versus equivalence

Formation and Property already distinguish submodel/restriction structure from strict structure-preserving equivalence.

This blocks an invalid quantum shortcut:

```text
subset / restricted face
therefore same as a lower quantum system
```

unless an explicit recursive-equivalence selector or theorem is supplied.

### 4.3 Full support versus reduced readout

Static Aggregation establishes that equal aggregates need not reconstruct equal supports and gives exact kernel criteria for when a readout is injective.

This is the DSD source of the later tomography discipline:

\[
\boxed{
\text{same readout}
\not\Rightarrow
\text{same underlying typed state}
}
\]

unless reconstruction conditions are explicitly satisfied.

### 4.4 Regular evolution versus formation transition

Dynamics distinguishes regular time-indexed evolution over a fixed formation background from a change of formation identity requiring lineage.

This supports the later separation between

```text
state evolution
representation equivalence
physical channel invertibility
formation-level transition
```

without implying unitary dynamics by itself.

### P0 conclusion

The pre-existing DSD contribution is therefore best described as a **typed descriptive and reconstruction discipline**.

It is not quantum kinematics.

## 5. P1 — target-independent general operational layer

QM Core 004 established the strongest layer that can be reached without supplying Hilbert geometry.

### 5.1 Convexity from randomized preparation

If a preparation procedure randomly chooses preparation \(P\) with probability \(\lambda\) and \(Q\) with probability \(1-\lambda\), and the randomizer record is discarded before readout, operational equivalence yields a convex mixture.

Thus randomized preparation supplies convex state structure.

### 5.2 Affine probability readouts

Probability readouts respect those mixtures:

\[
e(\lambda\omega+(1-\lambda)\sigma)
=
\lambda e(\omega)+(1-\lambda)e(\sigma).
\]

### 5.3 Affine transformations

Mixture-preserving transformations act affinely on the operational carrier.

### 5.4 Operational capacity

The maximum number of states jointly distinguishable by one measurement defines an operational capacity.

It is not identified with:

```text
DSD channel count
vector-space dimension
realized-axis rank
Hilbert dimension
```

without an additional theorem.

### 5.5 Finite real ordered carrier

Under finite separation by affine readouts, states embed in a finite-dimensional real ordered vector space with a positive cone and normalization functional.

Therefore the strongest target-independent carrier result is

\[
\boxed{
\text{DSD + explicit general operational assumptions}
\Longrightarrow
\text{real ordered operational carrier}.
}
\]

This does **not** imply real-Hilbert quantum theory and does not select complex scalars.

## 6. P2 — quantum selectors that remain supplied

The 004 and 008 audits identify the central target-specific structures.

### 6.1 Complex Hilbert carrier

The scalar field, inner product, projective pure-state geometry, and operator structure of a complex Hilbert space are not selected by generic DSD.

Therefore

\[
\boxed{
\text{generic DSD}
\not\Rightarrow
\mathbb C\text{-Hilbert structure}.
}
\]

### 6.2 Full Hilbert effect carrier

The full effect set

\[
\mathrm{Eff}(\mathcal H)=\{E:0\le E\le I\}
\]

is also quantum-specific supplied structure.

Once it is supplied, the Born pairing itself need no longer remain primitive.

### 6.3 Composition / ancilla structure

Standard complex tensor-product composition and the admissibility of arbitrary ancilla extensions are not implied by generic DSD.

They are needed for the 005A complete-positivity gate.

### 6.4 Local tomography

Local tomography is a useful selector, but not a generic DSD theorem.

QM Core 008 explicitly showed:

\[
K_{\mathbb R}(2)=3,\qquad
K_{\mathbb R}(4)=10,\qquad
3^2=9,
\]

so ordinary two-rebit composites contain one locally inaccessible parameter.

Thus local tomography excludes the straightforward standard real-Hilbert composite rule, but

\[
\boxed{
\text{local tomography alone}
\not\Rightarrow
\text{complex quantum theory}.
}
\]

### 6.5 Reversibility, no-restriction, and exact reconstruction packages

The selectors retained from 004 include:

```text
LDC-QM   local descriptive completeness / local tomography
RRDE-QM  recursive restriction-equivalence
CRR-QM   continuous pure-state reversible reachability
NR-QM    no-restriction / full effect domain
```

The 008 witness sharpened:

```text
CRR-QM alone != complex Hilbert
NR-QM alone  != complex Hilbert
LDC-QM excludes standard real-Hilbert composites
LDC-QM alone != unique complex-QM characterization
```

Hence a full operational reconstruction theorem may still be used conditionally, but its quantum selectors remain external inputs unless separately obtained from DSD.

## 7. P3 — standard theorem consequences successfully reconstructed

Once the relevant P2 structures are admitted, a large portion of ordinary QM follows by standard theorems or direct finite-dimensional arguments.

### 7.1 Born trace representation — QM Core 003

Given the full complex Hilbert effect carrier, a globally glued effect valuation normalized on every finite POVM obeys finite effect additivity.

A generalized Gleason/Busch effect-valuation theorem then yields a unique density operator \(\rho\) such that

\[
\boxed{
\omega(E)=\operatorname{Tr}(\rho E).
}
\]

Therefore the Born trace pairing is a conditional representation theorem, not an additional free DSD probability scalar.

### 7.2 Complete positivity — QM Core 005A

A positive trace-preserving subsystem map need not be physically admissible on arbitrary ancilla extensions.

Under the supplied quantum composite and ancilla-compatibility selector, admissibility requires complete positivity.

Thus

\[
\boxed{
\text{ancilla-compatible quantum dynamics}
\Longrightarrow
\text{CP}.
}
\]

### 7.3 Trace normalization and instruments — QM Core 005B

On the normalized ordered carrier, deterministic dynamics preserves the normalization functional.

Combined with CP this yields the CPTP deterministic-channel condition, while selective branches are CPTNI and sum to a CPTP nonselective map.

### 7.4 Reversible physical channels — QM Core 005C

For equal finite dimensions,

\[
\boxed{
\Phi\text{ has a CPTP inverse}
\iff
\Phi(\rho)=U\rho U^\dagger
}
\]

for a unitary \(U\).

Algebraic invertibility alone is insufficient.

### 7.5 Continuous unitary groups — QM Core 005D

For a continuous one-parameter unitary group,

\[
U(t)=e^{-itH/\hbar}
\]

with a self-adjoint/Hermitian generator under the relevant finite/infinite-dimensional Stone hypotheses.

A differentiable unitary path without the group law instead has a generally time-dependent generator.

### 7.6 CPTP semigroups — QM Core 005E

A continuous time-homogeneous CPTP semigroup satisfies

\[
\Phi_t=e^{t\mathcal L}
\]

with finite-dimensional GKSL generator

\[
\mathcal L(\rho)
=
-\frac{i}{\hbar}[H,\rho]
+
\sum_\alpha
\left(
L_\alpha\rho L_\alpha^\dagger
-\frac12\{L_\alpha^\dagger L_\alpha,\rho\}
\right).
\]

The audit separately established that CP-divisibility does not imply time-homogeneous semigroup structure.

### 7.7 Kraus / Stinespring dilation — QM Core 005F

Every finite-dimensional CPTP channel admits Kraus and Stinespring representations.

However:

\[
\boxed{
\text{dilation existence}
\not\Rightarrow
\text{unique physical environment}.
}
\]

### 7.8 Naimark / instrument realization — QM Core 005G

Every finite-dimensional POVM admits a projective dilation.

But

\[
\boxed{
\text{same POVM}
\not\Rightarrow
\text{same instrument}
}
\]

and therefore does not determine unique post-measurement dynamics or a unique apparatus.

### 7.9 Infinite-dimensional operator/domain gate — QM Core 006

For unbounded observables the object is

\[
(A,D(A)),
\]

not a formal operator symbol alone.

The synthesis therefore retains:

\[
\boxed{
\text{normalized state}
\not\Rightarrow
\text{every unbounded operator action is applicable}.
}
\]

Spectral probabilities may remain defined where \(A\psi\) itself is not.

### 7.10 Canonical CCR / Weyl representation — QM Core 007

For the standard Schrödinger pair on \(L^2(\mathbb R)\),

\[
[Q,P]\psi=i\hbar\psi
\]

holds on a common core such as \(\mathcal S(\mathbb R)\).

The exponentiated Weyl form, strong continuity, irreducibility, fixed nonzero central character, and finite canonical degree count are separate hypotheses.

Under those conditions Stone–von Neumann yields the Schrödinger representation up to unitary equivalence.

The finite trace obstruction remains exact:

\[
[A,B]=i\hbar I_d
\]

cannot hold for finite matrices.

## 8. P4 — what remains external or non-identifiable

The completed reconstruction does not establish the following from generic DSD:

```text
independent origin of the complex Hilbert carrier
numerical value of hbar
unique physical environment behind a Stinespring dilation
unique measurement apparatus behind a Naimark dilation
unique microscopic interaction Hamiltonian behind a reduced channel
unique dissipative mechanism from a GKSL generator representation
QFT representation uniqueness from finite-DOF Stone-von Neumann
```

More generally:

\[
\boxed{
\text{mathematical representation equivalence}
\neq
\text{physical implementation identity}.
}
\]

This non-identifiability boundary is one of the recurrent results of 005F–007.

## 9. Integrated dependency graph

The complete ordinary-QM core reconstructed in this program is best represented as

```text
PRE_EXISTING DSD
    typed identity / status
    applicability / prerequisites
    restriction / equivalence
    support-vs-readout reconstruction discipline
    regular evolution / lineage
        |
        v
GENERAL OPERATIONAL
    convexity
    affine probabilities
    affine transformations
    capacity
    finite real ordered carrier
        |
        v
QUANTUM SELECTORS
    complex Hilbert carrier
    full effect carrier
    complex composition / ancilla closure
    local tomography and stronger reconstruction selectors
    canonical/Weyl regularity assumptions
        |
        v
STANDARD THEOREM CONSEQUENCES
    Born trace rule
    CP / CPTP / instrument structure
    unitary reversible channels
    Hamiltonian generator
    GKSL generator
    Kraus / Stinespring
    Naimark
    unbounded-operator domain discipline
    canonical Schrödinger representation up to unitary
```

The arrow into `QUANTUM SELECTORS` is not an independent DSD derivation arrow.

It is an explicit specialization boundary.

## 10. Reconstruction coverage judgment

### 10.1 Conditional reconstruction

The reconstruction is strong.

Once the complex-Hilbert quantum carrier and the explicitly identified composition/symmetry/regularity selectors are supplied, the program reconstructs or rederives a broad standard chain:

```text
state/effect valuation
    -> Born representation

quantum composites + ancilla consistency
    -> complete positivity
    -> CPTP / instruments

physical reversibility
    -> unitary conjugation

continuous unitary group
    -> Hamiltonian generator

continuous CPTP semigroup
    -> GKSL generator

CPTP
    -> Kraus / Stinespring dilation

POVM
    -> Naimark dilation

infinite-dimensional Hilbert specialization
    -> domain-aware unbounded observables

regular irreducible finite-DOF Weyl representation
    -> Schrödinger canonical representation up to unitary
```

### 10.2 Independent reconstruction

The independent reconstruction is narrower:

```text
DSD descriptive architecture
+
general operational convex/affine structure
+
finite real ordered carrier
```

It stops before the complex Hilbert carrier.

### 10.3 No new empirical prediction

No gate in 001R–009 yields an experimentally distinct prediction from standard QM while retaining all standard quantum hypotheses.

Whenever the same full state/effect/channel structure is kept, the standard representation theorems recover standard QM.

A future deviation would therefore require an explicitly changed assumption and independent empirical evidence.

## 11. Final claim allowed after QM Core 009

The strongest justified statement is

\[
\boxed{
\begin{aligned}
&\text{DSD independently contributes a typed descriptive/reconstruction architecture,}\\
&\text{and with general operational assumptions reaches a real ordered carrier;}\\
&\text{after explicit quantum specialization, a broad ordinary-QM structure is}\\
&\text{reconstructed by standard mathematical consequences.}
\end{aligned}
}
\]

At the same time,

\[
\boxed{
\text{DSD does not presently independently derive the complex Hilbert carrier.}
}
\]

Therefore the phrase

```text
DSD reconstructs standard QM conditionally
```

is supported.

The stronger phrase

```text
DSD independently derives standard QM from its generic axioms
```

is not supported.

## 12. Relation to the four DSD core papers

The synthesis remains compatible with the canonical DSD paper hierarchy.

```text
Formation
    fixes admitted structural/channel identity and formation provenance

Property
    supplies typed applicability/dependency/partial-assignment structure

Static Aggregation
    supplies explicit readout maps and reconstruction-loss criteria

Dynamics
    supplies time-indexed regular trajectories, constitutive bridges,
    and transition/lineage structure
```

None of these papers identifies an application-level scalar field, Hilbert representation, quantum effect cone, tensor-product rule, Hamiltonian, or dissipator merely from a label.

Therefore the provenance closure used by QM Core 009 agrees with the source-level scope boundaries of the DSD papers.

## 13. Reproducibility audit

The accompanying Python script encodes the final provenance ledger and dependency graph.

It verifies:

```text
all nodes have one declared provenance class
all dependency targets exist
the dependency graph is acyclic
all major standard-QM target components are classified
complex Hilbert structure is not counted as independent DSD evidence
theorem consequences are not retroactively counted as A/B evidence
the conditional standard-QM chain is represented
the independent complex-Hilbert-origin claim remains external
```

Run from repository root:

```bash
python audits/science/2026-09-10_qm_core_009_integrated_standard_qm_reconstruction_synthesis_gate.py --mode all
```

Observed result:

```text
OVERALL: PASS_WITH_BOUNDARY
```

## 14. Verdict

\[
\boxed{\textbf{PASS\_WITH\_BOUNDARY}}
\]

QM Core 001R–009 closes the current **ordinary standard-QM reconstruction program**.

The main positive result is not that DSD secretly contained quantum mechanics in its generic axioms.

The positive result is that DSD supplies a stable pre-target descriptive architecture, the operational layer can be cleanly derived without Hilbert assumptions, and once the quantum specialization boundary is made explicit, the subsequent standard quantum structures can be reconstructed in a dependency-transparent way.

The principal unresolved boundary is now frozen rather than left ambiguous:

\[
\boxed{
\text{complex Hilbert carrier = supplied quantum specialization at the current DSD level}.
}
\]

## 15. Next program

Do not restart relativity from zero.

The Notion record already contains PHY-REL-001–007 audits on coordinate changes, causal accessibility, Cauchy reconstruction, relation layers, proper time, and standard relativity/QM separation.

The next program should therefore be:

**REL Core 001R — Integrated Standard-Relativity Rebaseline / Provenance Gate**.

Its first task is to collect the existing PHY-REL-001–007 results into the same provenance classes used here, identify which results are standard-relativity theorems, which are DSD descriptive distinctions, and which metric/causal/geometric structures remain externally supplied before any further relativity reconstruction is attempted.
