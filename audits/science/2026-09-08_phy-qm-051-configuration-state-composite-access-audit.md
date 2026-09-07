# PHY-QM-051 — Configuration-State Audit of Composite Access, Partial Trace, and Entanglement

Date: 2026-09-08
Status: **PASS_WITH_REFINEMENT**
Track: **2 — Full DSD structural analysis of standard quantum mechanics and relativity**

## 1. Purpose

This audit tests the second detailed Track-2 target:

```text
QM composite access
  tensor-product carrier
  partial trace
  entanglement/separability
  local accessibility
  global-state reconstruction
```

The target distinction is

\[
\boxed{
\text{global state existence}
\neq
\text{subsystem accessibility}
\neq
\text{global reconstructibility from local data}
}.
\]

The question is whether the current DSD configuration-state decomposition can preserve these distinctions without identifying standard-QM subsystem structure with DSD internal/external status.

No quantum-gravity or nonstandard quantum premise is used.

---

## 2. Source and interface lock

### Standard quantum mechanics

For a declared bipartite decomposition,

\[
\mathcal H_{AB}=\mathcal H_A\otimes\mathcal H_B,
\]

a global state is a density operator \(\rho_{AB}\). The reduced states are

\[
\rho_A=\operatorname{Tr}_B\rho_{AB},
\qquad
\rho_B=\operatorname{Tr}_A\rho_{AB}.
\]

The tensor-product decomposition, density-operator formalism, partial trace, and the standard definitions/criteria used for separability or entanglement are external standard-QM data. DSD does not derive them.

A standard reference for the reduction map is John Watrous, *The Theory of Quantum Information*, Chapter 2, where state reduction is defined by partial trace.

### DSD interfaces

The current Property Axiom System can retain supplied subsystem labels, state data, and other quantum-specialization coordinates through explicit typed profiles or auxiliary carriers. It does not generate a Hilbert-space tensor product from DSD channel counts or shared terminology.

The current Static Aggregation layer separately warns that a reduced readout does not reconstruct its source without injectivity or additional support data. This reconstruction discipline is the DSD-side comparator used below.

---

## 3. Partial trace is a one-slice restriction, not a temporal transition

For the present audit, define the local-access maps

\[
\alpha_A(\rho_{AB})=\operatorname{Tr}_B\rho_{AB},
\qquad
\alpha_B(\rho_{AB})=\operatorname{Tr}_A\rho_{AB}.
\]

These maps compare a global state with its subsystem reductions at one time slice. They are therefore placed in the access/restriction/readout part of the configuration-state analysis, not in the temporal transition layer \(\Gamma\).

Thus

\[
\boxed{
\operatorname{Tr}_B\rho_{AB}
\text{ is not, by itself, a claim that the global physical state evolved in time.}
}
\]

An open-system dynamical model may later contain a time evolution followed by a reduction, but those are two distinct operations and are not conflated here.

---

## 4. Local reduced state is sufficient for local quantum queries

For every operator/effect \(E_A\) on subsystem \(A\), standard QM gives

\[
\operatorname{Tr}\!\left[(E_A\otimes I_B)\rho_{AB}\right]
=
\operatorname{Tr}(E_A\rho_A).
\]

Therefore the reduced state \(\rho_A\) is sufficient for all observables or measurement effects that are genuinely local to \(A\) in the supplied tensor-product specialization.

This gives an important refinement:

\[
\boxed{
\text{complete for the declared local query family}
\not\Rightarrow
\text{complete for global-state reconstruction}
}.
\]

### Status

**Conditional standard-QM theorem under the supplied tensor-product specialization.**

DSD contributes the distinction between query-relative sufficiency and global reconstruction; it does not derive the trace identity.

---

## 5. Exact global reconstruction obstruction

Consider the Bell states

\[
|\Phi^{\pm}\rangle
=\frac{|00\rangle\pm|11\rangle}{\sqrt2}.
\]

Their density operators are globally distinct and the state vectors are orthogonal:

\[
\langle\Phi^+|\Phi^-\rangle=0.
\]

Nevertheless,

\[
\operatorname{Tr}_B|\Phi^+\rangle\langle\Phi^+|
=
\operatorname{Tr}_B|\Phi^-\rangle\langle\Phi^-|
=rac{I_2}{2},
\]

and similarly on subsystem \(B\).

The lost distinction remains globally observable. For example,

\[
\langle X\otimes X\rangle_{\Phi^+}=+1,
\qquad
\langle X\otimes X\rangle_{\Phi^-}=-1.
\]

Hence the pair-of-marginals map

\[
\mathcal L:\rho_{AB}\mapsto(\rho_A,\rho_B)
\]

is not injective.

Define its local-data fiber by

\[
\mathcal F_{\rm loc}(\rho_A,\rho_B)
=
\left\{
\sigma_{AB}:
\operatorname{Tr}_B\sigma_{AB}=\rho_A,
\operatorname{Tr}_A\sigma_{AB}=\rho_B
\right\}.
\]

The Bell-state pair lies in the same non-singleton fiber.

### Status

**Exact standard-QM finite witness.**

---

## 6. Exact two-qubit kernel accounting

Write a trace-one two-qubit Hermitian state in Pauli coordinates as

\[
\rho
=\frac14\left[
I\otimes I
+r_i\sigma_i\otimes I
+s_j I\otimes\sigma_j
+T_{ij}\sigma_i\otimes\sigma_j
\right].
\]

The affine state carrier has 15 real coordinates:

```text
r_i       : 3 local-A coordinates
s_j       : 3 local-B coordinates
T_ij      : 9 correlation coordinates
```

On the traceless-Hermitian difference space, the linear map

\[
L(X)=\left(\operatorname{Tr}_B X,\operatorname{Tr}_A X\right)
\]

retains the \(r\) and \(s\) sectors and annihilates every correlation direction

\[
\sigma_i\otimes\sigma_j.
\]

Therefore

\[
\operatorname{rank}L=6,
\qquad
\dim\ker L=9,
\]

with the correlation sector spanning the kernel.

### Status

**Mathematical/structural theorem for the standard two-qubit Pauli representation.**

This is not a claim about arbitrary multipartite reconstruction dimensions without separate proof.

---

## 7. Local unreconstructibility is not entanglement

The maximally mixed product state

\[
\rho_{\rm mix}=\frac{I_4}{4}
=\frac{I_2}{2}\otimes\frac{I_2}{2}
\]

is separable and has

\[
\rho_A=\rho_B=\frac{I_2}{2}.
\]

The Bell state \(|\Phi^+\rangle\) is entangled and has exactly the same one-party marginals.

A second control already present in PHY-QM-004 is the separable classically correlated state

\[
\rho_{CC}=\frac12
\left(
|00\rangle\langle00|+|11\rangle\langle11|
\right),
\]

which also has maximally mixed one-party marginals.

Thus neither the existence of a non-singleton local-data fiber nor the local marginals alone determine entanglement:

\[
\boxed{
\text{LOCAL\_TO\_GLOBAL\_UNRECONSTRUCTIBILITY}
\neq
\text{ENTANGLEMENT}
}.
\]

Equivalently, over this exhibited family there is no function

\[
\mathrm{Ent}_{A|B}=g(\rho_A,\rho_B)
\]

that recovers the global entanglement classification from the local marginals alone.

### Status

**Exact standard-QM finite witness.**

---

## 8. Configuration-state refinement

The result sharpens the current DSD configuration-state interpretation.

A global one-slice quantum record may schematically retain

\[
\Sigma^{AB}_{Q,t}
\supset
R_t[\rho_{AB},A|B],
\]

where the bipartition label \(A|B\) is supplied by the quantum specialization.

A subsystem-access record may instead retain only

\[
\Sigma^{A}_{Q,t}
\supset
R_t[\rho_A,A].
\]

The second record can be complete for the declared family of \(A\)-local queries while being incomplete for claims about global correlations, separability, or entanglement.

Accordingly, configuration-state completeness is not only relative to the declared system boundary; it is also relative to the **declared target/query family** within that boundary.

A safe statement is

\[
\boxed{
\Sigma^{A}_{Q,t}
\text{ may be locally sufficient}
\quad\text{while}\quad
\Sigma^{A}_{Q,t}
\not\Rightarrow
\Sigma^{AB}_{Q,t}.
}
\]

This is a refinement of completeness language, not a new DSD axiom.

---

## 9. Tensor-product and internal/external firewalls

The quantum decomposition

\[
\mathcal H_A\otimes\mathcal H_B
\]

must remain an external standard-QM structure.

It must not be identified with

```text
DSD channel composition,
DSD rank,
DSD internal/external status,
a count of DSD terms,
or a geometric dimension
```

without an explicit separately justified bridge.

Likewise, `subsystem A` does not automatically mean `DSD internal observer/system`, and `AB` does not automatically mean `DSD external system`.

The DSD access record states what the declared system can retain or query; the quantum tensor factorization states how the standard-QM carrier is decomposed. Their logical roles are different.

---

## 10. Relation to static aggregation

Partial trace is already a standard-QM reduction from global to local state data. Any later DSD static aggregation of those local records is an additional downstream reduction.

Therefore the safe order is

\[
\rho_{AB}
\xrightarrow{\operatorname{Tr}_B}
\rho_A
\xrightarrow{\text{optional DSD readout/aggregation}}
A_A.
\]

A later aggregate cannot restore the lost global correlation sector unless an independent reconstruction theorem supplies sufficient extra information.

This is consistent with the current Static Aggregation paper, which requires injectivity/kernel control before reduced outputs can support reconstruction claims.

---

## 11. Audit verdict

```text
STANDARD-QM TENSOR-PRODUCT SPECIALIZATION SUPPLIED       : PASS
PARTIAL TRACE AS ONE-SLICE ACCESS/RESTRICTION            : PASS
LOCAL REDUCED STATE SUFFICIENT FOR LOCAL QUERIES         : PASS
LOCAL MARGINALS RECONSTRUCT GLOBAL STATE                 : FAIL
LOCAL MARGINALS DETERMINE ENTANGLEMENT                   : FAIL
TWO-QUBIT LOCAL-MARGINAL KERNEL DIMENSION = 9            : PASS
LOCAL UNRECONSTRUCTIBILITY = ENTANGLEMENT                : FAIL
PARTIAL TRACE IDENTIFIED WITH TEMPORAL GAMMA             : NO
TENSOR PRODUCT DERIVED FROM DSD CHANNEL/RANK STRUCTURE   : NO
NEW DSD CORE AXIOM REQUIRED                              : NO
NEW QUANTUM LAW DERIVED                                  : NO
QUANTUM-GRAVITY CLAIM                                    : NO
```

Overall verdict: **PASS_WITH_REFINEMENT**.

The current configuration-state architecture survives the composite-system test. The main refinement is that `configuration-state completeness` must be indexed not merely by system boundary but also by the family of questions the state is claimed to answer. A subsystem reduced state may be fully sufficient for every local quantum prediction while being provably insufficient for global reconstruction or entanglement classification.

---

## 12. Reproducibility

No new Python file is created because the relevant two-qubit reconstruction and Werner-family controls already exist in the repository.

Run from the repository root:

```bash
python audits/science/2026-09-06_werner_dsd_entanglement_chsh.py
```

Dependency:

```text
numpy
```

Related prior audit:

```text
audits/science/2026-09-06_phy-qm-004-werner-entanglement-chsh-reconstruction-audit.md
```

---

## 13. Next target

Proceed to detailed audit 3:

```text
Relativity
  chart/frame representation
  invertible representation changes
  causal accessibility/domain restriction
  invariant readout
```

The central question is whether the same configuration-state discipline can distinguish reversible representation changes from genuine access restrictions without treating coordinate or frame difference as information loss.