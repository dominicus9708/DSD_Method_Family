# QM Core Reconstruction 004 — Synthesis Gate

Date: 2026-09-08  
Status: **PASS_WITH_BOUNDARY**  
Program: **Core-Theory Reconstruction Challenge**  
Target: synthesize QM Core 004 through 004J, freeze provenance, and determine exactly what was independently reconstructed, what was conditionally reconstructed, what was supplied, and what must move to QM Core 005.

## 1. Synthesis question

QM Core 004 began with the question:

\[
\boxed{\text{Why is the admissible quantum state/effect carrier Hilbertian?}}
\]

The 004A–004J sequence then isolated the operational and exact-comparator assumptions needed to distinguish complex quantum structure from weaker convex, non-Hilbert, or incompletely compositional alternatives.

The synthesis gate asks:

1. Which results genuinely trace back to pre-existing DSD structure or general operational semantics?
2. Which conditions were introduced only while specializing toward quantum theory?
3. Which conditions were introduced specifically to make an external reconstruction theorem exact?
4. Are any of the five exact-interface items isolated in 004E still unclassified?
5. Does the completed 004 chain independently derive the complex Hilbert carrier?

## 2. Provenance rule

The governing classification remains:

```text
A  PRE_EXISTING_DSD
B  GENERAL_OPERATIONAL_DERIVATION
C  TARGET_SPECIALIZATION_SELECTOR
D  EXACT_COMPARATOR_LOCK
```

Only A and independently validated B items count as evidence that DSD reached a target structure without fitting itself to quantum theory.

Class-C and Class-D assumptions may establish a coherent quantum specialization and permit conditional theorem transfer, but they do not count as independent derivation evidence.

## 3. Class-A structure actually present before the quantum target

The four-paper DSD core already supplied the following relevant distinctions before the present quantum reconstruction challenge.

### 3.1 Typed identity and status separation

Formation distinguishes channel absence, undefined assignment, defined zero, defined nonzero, and zero contribution rather than collapsing them into one numerical state.

Property retains declaration, applicability, contextual-prerequisite satisfaction, partial assignment, defined-zero, and defined-nonzero as distinct typed states.

This is the structural basis for the later zero-probability/undefined-conditioned-state distinction used in quantum instruments.

### 3.2 Restriction, submodel, and strict-equivalence discipline

Formation and Property already distinguish restriction or inclusion from a structure-preserving embedding/isomorphism. Therefore a restricted face cannot be declared to be a lower physical system merely because it is a subset.

This motivated the later RED/RRDE family but does not itself imply the quantum Subspace Axiom.

### 3.3 Aggregate/readout information loss

Static Aggregation already separates full typed support from a reduced aggregate and gives injectivity/kernel criteria for reconstruction.

Dynamics likewise does not allow a reduced readout to replace a full state without an explicit reconstruction result.

This is the pre-existing DSD basis for tomography, readout-fiber, and local/global reconstruction audits.

### 3.4 Regular evolution versus formation transition

Dynamics already distinguishes regular time-indexed evolution on a fixed Stage-VI background from formation-level change requiring lineage.

This supports the distinction between a physical evolution, a representation equivalence, and a cross-domain transition, but does not force a particular reversible group topology.

## 4. Class-B operational results derived without inserting Hilbert geometry

The strongest target-independent operational results of QM Core 004 are:

### 4.1 ORE — randomized preparation gives convexity

If a preparation is physically implemented by choosing `P` with probability `lambda` and `Q` with probability `1-lambda`, and the randomizer record is discarded before the readout, then operational equivalence induces

\[
\lambda[P]+(1-\lambda)[Q].
\]

Thus convex mixture structure follows from randomized preparation semantics rather than being inserted as a Hilbert-space axiom.

### 4.2 Probability readouts become affine

For every admitted probability readout `e`,

\[
e(\lambda\omega+(1-\lambda)\sigma)
=
\lambda e(\omega)+(1-\lambda)e(\sigma).
\]

A nonlinear rule such as `e(x)=x^2` fails this operational mixture requirement.

### 4.3 Mixture-preserving transformations become affine

A transformation that commutes operationally with randomized preparation induces an affine state-space map.

### 4.4 Operational capacity

Capacity is defined by the maximum number of states jointly, not merely pairwise, perfectly distinguishable by one measurement.

This quantity is not identified with DSD channel count, vector-space dimension, realized-axis rank, or Hilbert dimension.

### 4.5 Finite ordered carrier

A finite separating family of affine readouts yields a finite real linear embedding and a positive cone/normalization functional.

This establishes a pre-Hilbert ordered operational carrier under explicit finite-separation assumptions.

## 5. Class-C quantum selectors

The following remain quantum-specialization choices rather than generic DSD consequences:

```text
LDC-QM   local descriptive completeness / local tomography selector
RRDE-QM  recursive restriction-equivalence selector
CRR-QM   continuous pure-state reversible reachability selector
NR-QM    no-restriction / full physical effect-domain selector
```

Their existence is useful for a quantum specialization, but none may be retroactively counted as a pre-existing DSD prediction.

## 6. Class-D exact-comparator locks and decompositions

QM Core 004E isolated five exact-interface items.

### 6.1 OSC-QM

Operational-state compactness is not implied by finite dimension, boundedness, convexity, affine readouts, Formation closure, Property completion, Banach codomain completeness, or regular dynamics.

A limit-admission condition such as SOLA-QM is required.

Status:

```text
Class D / explicit comparator lock
```

### 6.2 CRG-QM

Continuous reversible reachability of pure states does not imply that the full reversible group is connected. The `O(2)` countermodel separates these claims.

A stronger path-realizability condition such as RGPR-QM is required.

Status:

```text
Class D / explicit comparator lock
```

### 6.3 ETC-QM

Exact tensor-carrier equality need not be assumed as one monolithic primitive.

With finite operational linearization, independent local-product composition and local descriptive completeness give opposite dimension inequalities and hence

\[
\boxed{V_{AB}\cong V_A\otimes V_B.}
\]

Status:

```text
conditional derivation from Class-C/D inputs
```

### 6.4 ULRRDE-QM

One designated recursive restriction does not universalize automatically to every maximal distinguishing measurement.

If a reference measurement has full linear recursive equivalence and the reversible structure is transitive on complete measurements, then universal recursion follows.

\[
\boxed{\mathrm{LFRR\!-\!QM}+\mathrm{CMT\!-\!QM}\Rightarrow\mathrm{ULRRDE\!-\!QM}.}
\]

Status:

```text
conditional derivation from Class-D inputs
```

### 6.5 CFE-QM

The existence of a system of every positive integer capacity need not be assumed as one family-wide primitive.

If there is one nontrivial finite-capacity seed, arbitrarily iterated independent finite product composition, and an intrinsic exact one-step capacity descent, then every finite capacity is realized.

\[
\boxed{\text{seed}+\mathrm{IFPC\!-\!QM}+\mathrm{IDDC\!-\!QM}\Rightarrow\mathrm{CFE\!-\!QM}.}
\]

Status:

```text
conditional derivation from Class-D inputs
```

## 7. Exact-interface closure result

All five exact-interface items originally isolated in QM Core 004E are now classified or decomposed.

```text
OSC-QM       classified
CRG-QM       classified
ETC-QM       conditional derivation
ULRRDE-QM    conditional derivation
CFE-QM       conditional derivation
```

Therefore:

\[
\boxed{\text{QM Core 004 exact-interface unclassified gaps}=0.}
\]

This is an interface-completion result, not a proof that generic DSD derives complex quantum mechanics.

## 8. Born-rule status after the 004 sequence

QM Core 003 remains valid under its stated supplied carrier.

Given the full finite-dimensional complex Hilbert effect carrier, cross-context gluing and normalized finite POVM aggregation directly imply finite effect additivity. A generalized Gleason/Busch representation theorem then yields

\[
\omega(E)=\operatorname{Tr}(\rho E).
\]

Therefore the Born trace pairing is not required as an additional free numerical primitive once the full Hilbert effect carrier and the valuation assumptions are supplied.

However:

\[
\boxed{\text{the complex Hilbert/effect carrier itself remains supplied.}}
\]

Hence Born representation is a **conditional reconstruction**, not an independent derivation of quantum state-space geometry from generic DSD.

## 9. What QM Core 004 did and did not establish

### Established

1. Minimal DSD-compatible operational assumptions do not uniquely force Hilbert geometry.
2. Several non-Hilbert countermodels survive weak conditions and are removed only by stronger restriction/composition/tomography requirements.
3. Randomized preparation yields convex/affine operational structure without presupposing Hilbert space.
4. Capacity is an operational invariant distinct from DSD structural counts.
5. Exact tensor composition, universal recursive restriction, and full capacity-family existence can be decomposed into more primitive assumptions and conditional theorems.
6. The exact external reconstruction interface is now fully classified.

### Not established

1. Generic DSD does not independently derive the complex Hilbert carrier.
2. Generic DSD does not independently derive no-restriction.
3. Generic DSD does not independently derive operational compactness.
4. Generic DSD does not independently derive connectedness of the full reversible group.
5. Class-C/D assumptions must not be counted as independent DSD evidence merely because they complete a standard quantum reconstruction theorem interface.

## 10. Strongest justified synthesis statement

The strongest claim supported by QM Core 004 is:

\[
\boxed{
\begin{array}{c}
\text{DSD, which was not designed as a quantum reconstruction theory,}\
\text{independently supplies several typed/reconstruction distinctions and,}\
\text{with general randomized-preparation semantics, reaches a finite convex}\
\text{ordered operational architecture.}
\end{array}
}
\]

At the same time:

\[
\boxed{
\text{complex Hilbert uniqueness still requires target/comparator-specific inputs.}
}
\]

This preserves the predefinition-contamination advantage without hiding post-hoc fitting.

## 11. Consequence for the reconstruction program

QM Core 004 is complete as a state/effect/composition/restriction/capacity reconstruction gate.

The next unresolved quantum structure is dynamical:

\[
\boxed{\text{positivity}\rightarrow\text{ancilla consistency}\rightarrow\text{complete positivity}\rightarrow\text{CPTP/instrument structure}.}
\]

This becomes **QM Core 005**.

The principal question is not whether standard CPTP maps can be inserted into DSD Dynamics; QM Core 001–002 already showed that they can. The aggressive question is:

> Under an already declared quantum composite specialization, what consistency requirement makes positivity on a subsystem insufficient and forces complete positivity when arbitrary admissible ancillas are included?

## 12. Verdict

\[
\boxed{\textbf{PASS\_WITH\_BOUNDARY}}
\]

The 004 sequence substantially narrows and classifies the Hilbert-reconstruction interface, but does not convert target/comparator assumptions into independent DSD theorems. The boundary is now explicit enough to close QM Core 004 and move to quantum dynamics.

## 13. Reproducibility

Python:

```bash
python audits/science/2026-09-08_qm_core_004_synthesis_gate.py --mode all
```

The script checks the provenance ledger, confirms that the five 004E exact-interface items are no longer unclassified, and prevents the supplied Hilbert carrier or Class-C/D assumptions from being counted as independent A/B evidence.
