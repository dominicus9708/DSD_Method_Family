# Cross-Standard Countermodel Audit — Composition of Reductions/Readouts vs Order Dependence

Date: 2026-09-08  
Status: **PASS_WITH_BOUNDARY**  
Track: **2 — second-depth common-role stress test, B5**

## 1. Purpose

This audit tests whether the mere existence of two individually valid reductions, readouts, or coarse-graining operations is sufficient to infer that they can be composed in either order or that the two orders agree.

The target firewall is

\[
\boxed{
\text{two valid maps}
\not\Rightarrow
\text{typed composability}
\not\Rightarrow
\text{commutation}.
}
\]

The audit first separates typing, sequential composition, parallel joint readout, factorization, and commutation. It then tests standard-QM and relativity/domain-restriction specializations without identifying their physical meanings.

No quantum-gravity, alternative-gravity, or new DSD physical premise is introduced.

---

## 2. Abstract typed-composition gate

Let

\[
R_1:X\to Y_1,
\qquad
R_2:U_2\to Y_2.
\]

The expression

\[
R_2\circ R_1
\]

is meaningful only when the output of \(R_1\) lies in the declared input domain of \(R_2\), or when an explicit bridge/coercion is supplied.

Likewise, the reverse expression

\[
R_1\circ R_2
\]

requires its own independent typing condition.

Therefore the equation

\[
R_2R_1=R_1R_2
\]

is not even a proposition until both sides are well-typed with a common comparison codomain.

For two endomaps

\[
P,Q:S\to S,
\]

commutation is the additional condition

\[
\boxed{
P(Q(s))=Q(P(s))
\quad\forall s\in S.
}
\]

It is not implied by either map being well-defined, surjective, injective, idempotent, or interpretable as a reduction.

### Parallel joint readout is not sequential composition

If two maps share a source,

\[
R_1:S\to Y_1,
\qquad
R_2:S\to Y_2,
\]

then the product map

\[
J=(R_1,R_2):S\to Y_1\times Y_2
\]

is a parallel joint record whenever the product codomain is admitted.

This does **not** imply

\[
R_2\circ R_1
\]

or

\[
R_1\circ R_2
\]

exists. It also does not imply either map factors through the other.

This distinction is important for DSD because a combined descriptor or paired readout is not automatically a sequential reduction pipeline.

---

## 3. Conditional structural theorem — commuting idempotent reductions

Let

\[
P,Q:S\to S
\]

be idempotent endomaps:

\[
P^2=P,
\qquad
Q^2=Q.
\]

If they commute,

\[
PQ=QP,
\]

then

\[
(PQ)^2=PQ,
\]

so their composite is again idempotent.

Moreover, because the image of an idempotent map equals its fixed-point set,

\[
\boxed{
\operatorname{im}(PQ)
=
\operatorname{im}P\cap\operatorname{im}Q.
}
\]

Proof:

\[
P(PQx)=PQx,
\qquad
Q(PQx)=PQx
\]

using idempotence and commutation, hence every point in \(\operatorname{im}(PQ)\) lies in both images. Conversely, if \(y\) lies in both images, then \(P(y)=Q(y)=y\), so \(PQ(y)=y\).

This is an elementary structural theorem under explicit common-carrier, idempotence, and commutation assumptions. It is not a theorem that all objects called "reductions" commute.

---

## 4. Generic finite counterexample

Take

```text
S = {0,1,2}

R1:
  0 -> 0
  1 -> 0
  2 -> 2

R2:
  0 -> 0
  1 -> 1
  2 -> 1
```

Both are idempotent endomaps.

However

```text
R2 o R1:
  0 -> 0
  1 -> 0
  2 -> 1

R1 o R2:
  0 -> 0
  1 -> 0
  2 -> 0
```

so

\[
R_2R_1\neq R_1R_2.
\]

Thus even

\[
\boxed{
\text{valid}
+
\text{idempotent}
+
\text{same carrier}
}
\]

does not imply order independence.

---

## 5. Standard-QM specialization

### 5.1 External standard lock

Standard quantum mechanics supplies tensor-product systems and partial traces. For a multi-register state, tracing out one register is a standard reduction map. John Watrous defines the reduction of a multipartite state by the corresponding partial trace and gives its tensor-product action explicitly.

Reference:

```text
John Watrous,
The Theory of Quantum Information,
Chapter 2, Basic notions of quantum information.
https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf
```

The same source treats channels; Chapter 4 includes pinching channels and completely dephasing channels.

Reference:

```text
John Watrous,
The Theory of Quantum Information,
Chapter 4, Unital channels and majorization.
https://cs.uwaterloo.ca/~watrous/TQI/TQI.4.pdf
```

These are standard-QM structures, not DSD-derived operations.

### 5.2 Positive control — disjoint partial traces commute

For

\[
\rho_{ABC}
\]

the two disjoint subsystem reductions satisfy

\[
\boxed{
\operatorname{Tr}_B\operatorname{Tr}_C\rho_{ABC}
=
\operatorname{Tr}_C\operatorname{Tr}_B\rho_{ABC}
=
\operatorname{Tr}_{BC}\rho_{ABC}.
}
\]

The finite script verifies the equality on a nontrivial three-qubit pure-state density matrix.

This commutation follows from the specific tensor-product/trace structure. It is not inherited merely from both maps being reductions.

### 5.3 Counterexample — idempotent quantum coarse-grainings can be order-sensitive

For a qubit define the dephasing/pinching channel associated with an axis \(n\):

\[
\Delta_n(\rho)
=
P_{n,+}\rho P_{n,+}
+
P_{n,-}\rho P_{n,-}.
\]

Each such channel is idempotent:

\[
\Delta_n^2=\Delta_n.
\]

Use

\[
\rho_0=|0\rangle\langle0|,
\qquad
n=z,
\qquad
m=\frac{x+z}{\sqrt2}.
\]

The script obtains

\[
\Delta_m\Delta_z(\rho_0)
=
\begin{pmatrix}
3/4 & 1/4\\
1/4 & 1/4
\end{pmatrix},
\]

while

\[
\Delta_z\Delta_m(\rho_0)
=
\begin{pmatrix}
3/4 & 0\\
0 & 1/4
\end{pmatrix}.
\]

Therefore

\[
\boxed{
\Delta_m\Delta_z
\neq
\Delta_z\Delta_m
}
\]

on this witness.

Both operations are individually valid idempotent quantum channels. Their order sensitivity is not a failure of either channel.

Important role boundary:

```text
dephasing/pinching channel = quantum operation/coarse-graining channel
POVM probability readout   = readout map
partial trace              = subsystem reduction
```

They are not identified merely because all can reduce retained information.

---

## 6. Relativity/domain-restriction specialization

### 6.1 Nested domain restriction

Let a global record be defined on \(X\), and let

\[
D_2\subseteq D_1\subseteq X.
\]

Then typed restriction satisfies

\[
\boxed{
r_{D_2}^{D_1}\circ r_{D_1}^{X}
=
r_{D_2}^{X}.
}
\]

This is an absorption law for nested restrictions.

The reverse expression

\[
r_{D_1}\circ r_{D_2}
\]

is generally **ill-typed**: data already restricted to \(D_2\) do not contain the missing points of \(D_1\setminus D_2\). An extension/reconstruction rule would have to be supplied.

Thus nested domain restriction is not best described by saying that "both orders commute." One order is canonical; the reverse may not exist.

### 6.2 Passive Lorentz representation vs causal-domain restriction

Sean Carroll's standard relativity notes treat Lorentz transformations, spacetime intervals, causal structure, worldlines, and proper time as standard independent structures.

Reference:

```text
Sean M. Carroll,
Lecture Notes on General Relativity,
Chapter 1: Special Relativity and Flat Spacetime.
https://arxiv.org/abs/gr-qc/9712019
```

Let \(L\) be a Lorentz transformation, let \(D\) be a semantic causal domain, and let \(T_L\) denote passive re-expression of a field/record.

When the domain is transported together with the representation,

\[
D\mapsto L(D),
\]

the correctly typed square is

\[
\boxed{
T_L^{D}\circ r_D
=
r_{L(D)}\circ T_L.
}
\]

For

\[
D=J^-(O),
\]

Lorentz transformations preserve the causal classification, so

\[
L(J^-(O))=J^-(L(O)).
\]

The finite witness uses four events and a \(\beta=0.6\) boost and verifies that restricting to the finite causal-past sample then boosting gives the same record as boosting first and then restricting to the transported causal domain.

The result does **not** say that an arbitrary fixed coordinate window commutes with a frame change. A coordinate-defined window that is not transported denotes a different representation-dependent selection and must not be silently identified with the same causal-access domain.

---

## 7. Cross-standard result

The common conclusion is more limited than a universal commutation theorem:

\[
\boxed{
\text{composition requires typing first;}
\quad
\text{order independence requires an additional compatibility condition.}
}
\]

The examples separate three cases:

```text
1. compatible and commuting:
   disjoint QM partial traces;

2. individually valid but noncommuting:
   nonorthogonal QM dephasing channels;

3. one canonical composition, reverse order ill-typed:
   nested domain restrictions.
```

A fourth case is a commuting **typed square** rather than same-carrier commutation:

```text
passive Lorentz re-expression
+
transported causal-domain restriction.
```

Therefore no single statement such as

```text
all reductions commute
```

or

```text
all information-losing maps are order-sensitive
```

survives.

---

## 8. DSD interpretation

The DSD static layer already distinguishes parallel outputs and further postprocessing. The current static paper defines the combined static descriptor as an ordered pair and states that later scalarization, contraction, constitutive interpretation, or empirical readout is a further map. It does not imply that arbitrary downstream maps commute.

Likewise, Structural Reorganization Dynamics requires declared typing and a separate constitutive dynamic bridge where dynamics are used. A static bridge does not determine a dynamic operator.

Accordingly, the DSD audit rule should be:

```text
before composing two maps:
  1. lock each map's role;
  2. lock source and target types;
  3. test whether the requested order is composable;
  4. if both orders exist, test commutation rather than assume it;
  5. distinguish sequential composition from a parallel joint record;
  6. if one map factors through another, record the factorization explicitly;
  7. never infer physical equivalence from algebraic commutation alone.
```

In particular,

\[
\boxed{
\text{finite-sum commutativity in static aggregation}
\neq
\text{commutativity of arbitrary reduction/readout maps}.
}
\]

The DSD core does not require modification.

---

## 9. Common-theorem gate

B5 admits one **conditional** structural theorem:

\[
\boxed{
P,Q:S\to S,\;
P^2=P,\;
Q^2=Q,\;
PQ=QP
\Longrightarrow
(PQ)^2=PQ
}
\]

and

\[
\boxed{
\operatorname{im}(PQ)
=
\operatorname{im}P\cap\operatorname{im}Q.
}
\]

However the audit rejects promoting this into a universal "reduction theorem" because partial traces and domain restrictions are often not endomaps on one unchanged carrier.

The more general cross-standard rule is therefore a **typing/compatibility gate**, not a claim that the physical reductions in QM and relativity are instances of one physical operation.

---

## 10. Status classification

### Mathematical / structural theorem layer

- requested compositions must first be well-typed;
- two same-carrier maps commute iff their pointwise compositions agree;
- two valid idempotent endomaps need not commute;
- commuting idempotent endomaps compose to an idempotent whose image is the intersection of the two images;
- the product map \((R_1,R_2)\) is a parallel joint record and is not sequential composition;
- nested restrictions obey typed absorption.

### Finite / exact witness layer

- two three-state idempotent maps that do not commute;
- three-qubit disjoint partial traces that commute;
- two nonorthogonal qubit dephasing channels that are individually idempotent but order-sensitive;
- nested record restrictions whose reverse order is ill-typed;
- finite Lorentz/causal-domain transported-square commutation.

### Conditional standard-physics layer

- tensor products, partial trace, pinching/dephasing channels are supplied by standard QM;
- Lorentz transformations and causal relations are supplied by standard relativity.

### Unresolved / not established

- no universal DSD reduction algebra is derived;
- no arbitrary DSD readout pair is assumed to commute;
- no QM partial trace is identified with a relativistic restriction map;
- no dephasing channel is identified with a DSD static aggregate;
- no algebraic commutation is promoted to physical equivalence;
- no quantum-gravity implication follows.

---

## 11. Scoped outcome ledger

```text
two valid reductions -> both composition orders exist:
  REJECTED

two valid idempotent endomaps -> commute:
  REJECTED

disjoint standard-QM partial traces commute:
  VALID_IN_DOMAIN

nonorthogonal dephasing/pinching channels commute:
  REJECTED by exact witness

nested domain restriction:
  VALID_IN_DOMAIN with typed absorption

reverse nested restriction without extension:
  ILL_TYPED / NOT_DEFINED

Lorentz re-expression + transported causal-domain restriction:
  VALID typed commuting square

parallel joint readout = sequential composition:
  NON_IDENTICAL
```

No valid map is labeled `FAIL` merely because another valid map cannot be composed with it in a requested order.

---

## 12. DSD core impact

No revision of the Formation Axiom System, Property Axiom System, Channel-Indexed Static Aggregation, or Structural Reorganization Dynamics is required.

The current source architecture already supports the result:

- Formation maps are typed and composition is asserted only for the declared structure-preserving map class;
- Property representations and later aggregation/dynamics are separate downstream interfaces;
- static combined outputs are ordered/typed and later postprocessing is a further map;
- dynamics does not infer operators from static bridges.

B5 therefore strengthens an audit rule rather than adding a core axiom.

---

## 13. Verdict

\[
\boxed{\textbf{PASS\_WITH\_BOUNDARY}}
\]

The common structuring survives, but in a stricter form:

\[
\boxed{
\text{map existence}
\to
\text{typing}
\to
\text{composability}
\to
\text{compatibility/commutation test}.
}
\]

Order independence is never inferred solely from the word "reduction", "access", "readout", or "coarse-graining".

---

## 14. Reproducibility

Script:

```text
audits/science/2026-09-08_cross_composition_order_typed_reductions.py
```

Run from repository root:

```bash
python audits/science/2026-09-08_cross_composition_order_typed_reductions.py --mode all
```

Dependency:

```text
Python standard library only
```

---

## 15. Next target

B1–B5 are now complete.

Proceed to the **Track-2 common-theorem gate and synthesis**:

```text
1. collect every admitted abstract theorem/lemma;
2. separate theorem-level results from audit rules and theory-specific witnesses;
3. test redundancy/dependence among the admitted results;
4. state the exact common DSD structuring kernel that survived QM/relativity stress tests;
5. state the hard physical non-identification boundary;
6. decide which parts can be promoted into the reusable DSD Method Family interface;
7. hand the surviving kernel to Track 3 without importing new physical premises.
```

Standard QFT remains a separate later extension with a fresh primitive lock.
