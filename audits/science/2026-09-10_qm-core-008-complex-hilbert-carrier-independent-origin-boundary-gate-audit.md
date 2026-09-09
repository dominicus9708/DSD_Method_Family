# QM Core Reconstruction 008 — Complex-Hilbert Carrier Closure / Independent-Origin Boundary Gate

Date: 2026-09-10  
Status: **PASS_WITH_BOUNDARY**  
Program: **Core-Theory Reconstruction Challenge**

## Question

QM Core 003–007 reconstructed substantial standard-QM structure conditionally on a complex Hilbert carrier. The remaining issue is whether generic DSD itself forces that carrier.

Critical separation:

```text
GENERIC_DSD
GENERAL_OPERATIONAL_STRUCTURE
REAL_ORDERED_LINEAR_CARRIER
QUANTUM_RECONSTRUCTION_SELECTORS
COMPLEX_HILBERT_CARRIER
STANDARD_QM COMPARATOR
```

## Generic DSD contribution

Generic DSD supplies typed identity/status, applicability and prerequisites, defined/undefined/defined-zero distinctions, restriction versus equivalence, readout aggregation, and Formation/Property/Dynamics separation.

None of these chooses a scalar field. Therefore

\[
\boxed{\text{generic DSD}\not\Rightarrow\mathbb C\text{-Hilbert structure}.}
\]

## General operational layer

With explicit operational assumptions, randomized preparations yield convexity, probabilities are affine on mixtures, finite separating effects embed states in a finite-dimensional real vector space, and mixture-preserving transformations act affinely.

Thus, under the relevant finite-dimensional/separation hypotheses,

\[
\boxed{\text{operational convexity + affine probabilities}\Longrightarrow\text{real ordered carrier}.}
\]

This `real` carrier is the ordinary real vector space of probability parameters, not real-Hilbert quantum theory.

## Continuous reversibility is insufficient

A rebit admits continuous reversible orthogonal rotations

\[
R(\theta)=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix},
\]

acting continuously on real pure-state rays. Hence

\[
\boxed{\text{continuous reversible pure-state motion}\not\Rightarrow\text{complex scalars}.}
\]

## Full effects are insufficient

Real-Hilbert quantum theory has the natural real-symmetric effect cone \(0\le E\le I\), so a no-restriction/full-effect principle alone does not select \(\mathbb C\).

## Local-tomography pressure against real-Hilbert QM

For real symmetric \(d\times d\) matrices,

\[
K_{\mathbb R}(d)=\frac{d(d+1)}2.
\]

Thus

\[
K_{\mathbb R}(2)=3,\qquad K_{\mathbb R}(4)=10,
\]

while local products of two rebits span only

\[
3\times3=9.
\]

Therefore the two-rebit composite has one locally inaccessible real parameter.

For complex Hermitian carriers,

\[
K_{\mathbb C}(d)=d^2,
\]

and

\[
K_{\mathbb C}(d_Ad_B)=K_{\mathbb C}(d_A)K_{\mathbb C}(d_B),
\]

which is compatible with ordinary local tomography.

## Explicit two-rebit witness

One-rebit real observables are spanned by \(I,X,Z\). \(Y\) itself is not real symmetric, but \(Y\otimes Y\) is.

For \(0<c<1\), define

\[
\rho_\pm=\frac14(I\otimes I\pm cY\otimes Y).
\]

Since \((Y\otimes Y)^2=I\), both states are positive and normalized. The audit verifies for every \(A,B\in\{I,X,Z\}\):

\[
\operatorname{Tr}[\rho_+(A\otimes B)]=\operatorname{Tr}[\rho_-(A\otimes B)],
\]

while

\[
\operatorname{Tr}(\rho_+Y\otimes Y)=c,
\qquad
\operatorname{Tr}(\rho_-Y\otimes Y)=-c.
\]

Hence

\[
\boxed{\text{all local real-product statistics equal}\not\Rightarrow\text{same global rebit state}.}
\]

This is the explicit one-coordinate local-tomography defect.

## What this proves and what it does not

Ordinary local tomography excludes the straightforward real-Hilbert composite rule. But local tomography alone does not imply complex Hilbert quantum theory; many generalized probabilistic theories are locally tomographic.

Operational reconstruction programs can characterize complex quantum theory only with stronger packages of assumptions. Those packages are external assumptions unless each item is independently obtained from generic DSD.

## Provenance closure

```text
A PRE_EXISTING_DSD
  typed status, applicability, restriction/equivalence,
  aggregation/readout, Formation/Property/Dynamics separation

B GENERAL_OPERATIONAL_DERIVATION
  convexity from randomized preparation
  affine probabilities and transformations
  finite-dimensional real ordered carrier

C TARGET_SPECIALIZATION_SELECTOR
  local tomography
  continuous reversible reachability
  no-restriction/full effects
  homogeneity/self-duality or Jordan/C*-type assumptions
  complex scalar field / Hilbert inner product / standard composition

D EXACT COMPARATOR LOCK
  complex Hilbert space
  density operators, POVMs, CPTP maps
  Born trace rule, standard complex tensor product
```

The selectors from QM Core 004 remain selectors:

```text
LDC-QM   local descriptive completeness / local tomography
RRDE-QM  recursive restriction-equivalence
CRR-QM   continuous pure-state reversible reachability
NR-QM    no-restriction/full effect-domain
```

Sharpened results:

```text
CRR-QM alone != complex Hilbert
NR-QM alone  != complex Hilbert
LDC-QM excludes standard real-Hilbert composites
LDC-QM alone != unique complex-QM characterization
```

## DSD interpretation

The strongest valid reconstruction statement is

\[
\boxed{
\begin{aligned}
&\text{DSD + general operational assumptions}\Rightarrow\text{real ordered descriptive carrier},\\
&\text{quantum selectors + external reconstruction theorem}\Rightarrow\text{complex Hilbert representation under its hypotheses}.
\end{aligned}}
\]

## Verdict

**PASS_WITH_BOUNDARY**.

The independent-origin question is resolved negatively at the present level:

\[
\boxed{\text{generic DSD}\not\Rightarrow\text{complex Hilbert quantum theory}.}
\]

This is not a failure of the conditional reconstruction. It identifies precisely where target-independent DSD stops and standard quantum specialization begins.

## Reproducibility

```text
audits/science/2026-09-10_qm_core_008_complex_hilbert_carrier_independent_origin_boundary_gate.py
audits/science/2026-09-10_qm-core-008-complex-hilbert-carrier-independent-origin-boundary-gate-audit.md
methodology/QUANTUM_COMPLEX_HILBERT_CARRIER_BOUNDARY_INTERFACE.md
```

Run:

```bash
python audits/science/2026-09-10_qm_core_008_complex_hilbert_carrier_independent_origin_boundary_gate.py --mode all
```

Observed result:

```text
OVERALL: PASS_WITH_BOUNDARY
```

## Standard external references used for theorem checking

- Lucien Hardy, *Quantum Theory From Five Reasonable Axioms*, arXiv:quant-ph/0101012.
- Lucien Hardy and William K. Wootters, *Limited Holism and Real-Vector-Space Quantum Theory*, arXiv:1005.4870.
- Howard Barnum and Alexander Wilce, *Local tomography and the Jordan structure of quantum theory*, arXiv:1202.4513.
- Lucien Hardy, *Reconstructing quantum theory*, arXiv:1303.1538.

These references supply external reconstruction/local-tomography results and are not counted as DSD-derived structure.

## Next target

**QM Core 009 — Integrated Standard-QM Reconstruction Synthesis / Provenance Closure Gate**.

Integrate QM Core 001R–008 into a single dependency/provenance graph and classify each standard-QM component as PRE_EXISTING_DSD, GENERAL_OPERATIONAL, QUANTUM_SELECTOR, STANDARD_THEOREM_CONSEQUENCE, or NOT_DERIVED/REMAINS_EXTERNAL.