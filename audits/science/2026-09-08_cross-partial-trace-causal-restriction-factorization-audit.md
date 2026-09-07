# Cross-Standard Countermodel Audit — Partial Trace vs Causal/Domain Restriction

Date: 2026-09-08  
Status: **PASS_WITH_BOUNDARY**  
Track: **2 — second-depth common-role stress test**

## 1. Purpose

This audit tests whether the structural similarity between

```text
standard-QM subsystem reduction by partial trace
and
relativistic causal/domain restriction
```

supports a genuinely common theorem, and exactly where the physical comparison must stop.

The intended common layer is only

\[
\boxed{
\text{map}\to\text{fiber}\to\text{query factorization / reconstruction condition}
}.
\]

The audit explicitly rejects the stronger identifications

```text
partial trace = causal restriction,
quantum subsystem = spacetime domain,
entanglement = causal inaccessibility,
local quantum observability = causal-past membership,
```

unless an independent theory-specific bridge is supplied and proved.

No quantum-gravity candidate or nonstandard gravity/quantum premise is used.

---

## 2. Source lock

### 2.1 Standard quantum mechanics

For a declared bipartite system

\[
\mathcal H_{AB}=\mathcal H_A\otimes\mathcal H_B,
\]

the subsystem reduction is

\[
\alpha_A(\rho_{AB})=\operatorname{Tr}_B\rho_{AB}.
\]

The partial trace and tensor-product structure are supplied by standard QM. Watrous, *The Theory of Quantum Information*, Chapter 2, defines state reduction by partial trace and treats the reduced density operator as the state of the retained register.

The prior DSD audit

```text
audits/science/2026-09-08_phy-qm-051-configuration-state-composite-access-audit.md
```

already established the exact Bell-state witness

\[
|\Phi^\pm\rangle=(|00\rangle\pm|11\rangle)/\sqrt2,
\]

with identical local reductions but distinct global correlations.

### 2.2 Standard relativity

For the finite comparator, use a declared event domain

\[
D=J^-(O)\cap\Omega_{\rm finite}
\]

in 1+1 Minkowski spacetime and the restriction map

\[
\alpha_D(G)=G|_D.
\]

The causal relation is supplied by standard relativity. Carroll's GR lecture notes treat causal structure, initial-value structure, and domains of dependence as standard spacetime-geometric notions.

The prior DSD audit

```text
audits/science/2026-09-08_phy-rel-005-configuration-state-frame-causal-access-audit.md
```

already established a finite witness with two globally distinct records that agree on the selected causal domain.

### 2.3 DSD source lock

The current DSD papers already contain the abstract restraint required here:

```text
Formation:
  equality after composition is weaker than strict formation equivalence.

Static aggregation:
  reduced outputs do not reconstruct source structure without injectivity;
  an exact kernel criterion is given on fixed support.

Dynamics:
  a descriptive projection Pi_O need not be injective;
  equality after projection defines a coarser descriptive equivalence;
  latent structural distinctions are precisely unequal source states with equal projections.
```

Therefore the present audit does not need a new DSD primitive for `reduction`.

---

## 3. Common map theorem

Let

\[
f:X\to Y
\]

be any map and define its fiber equivalence

\[
x\sim_f x'\iff f(x)=f(x').
\]

Let

\[
q:X\to Z
\]

be a target query or quantity to be recovered from the reduced output.

### Theorem 3.1 — fiber-factorization criterion

There exists a unique map

\[
\bar q:f(X)\to Z
\]

such that

\[
q=\bar q\circ f
\]

if and only if \(q\) is constant on every fiber of \(f\):

\[
f(x)=f(x')\Longrightarrow q(x)=q(x').
\]

#### Proof

If \(q=\bar q\circ f\), then equal \(f\)-outputs immediately give equal \(q\)-outputs.

Conversely, if \(q\) is constant on each fiber, define

\[
\bar q(y)=q(x)
\]

for any \(x\) with \(f(x)=y\). Fiber constancy makes this well defined. Uniqueness holds on \(f(X)\).

### Corollary 3.2 — reconstruction obstruction

A full left inverse

\[
r:Y\to X,
\qquad
r\circ f=\operatorname{id}_X
\]

can exist only if \(f\) is injective.

Equivalently, a non-singleton fiber is an exact obstruction to unrestricted source reconstruction from \(f(x)\) alone.

### Status

**General mathematical/set-theoretic theorem.**

It is independent of both quantum mechanics and relativity. The two theories below instantiate the theorem with different physical maps.

This theorem is also consistent with the DSD Dynamic projection definition and the Static Aggregation injectivity discipline; it is not a new physical DSD law.

---

## 4. Quantum specialization

Take

\[
f_Q=\operatorname{Tr}_B.
\]

For

\[
\rho_+=|\Phi^+\rangle\langle\Phi^+|,
\qquad
\rho_-=|\Phi^-\rangle\langle\Phi^-|,
\]

we have

\[
f_Q(\rho_+)=f_Q(\rho_-)=I_2/2.
\]

Thus the fiber is non-singleton.

### 4.1 A global query that does not factor

Let

\[
q_{XX}(\rho)=\operatorname{Tr}[\rho(X\otimes X)].
\]

Then

\[
q_{XX}(\rho_+)=+1,
\qquad
q_{XX}(\rho_-)=-1.
\]

Therefore \(q_{XX}\) is not constant on the partial-trace fiber, and Theorem 3.1 gives

\[
\boxed{
q_{XX}\text{ does not factor through }\operatorname{Tr}_B.
}
\]

A reduced state of subsystem \(A\) cannot reconstruct this global correlation query.

### 4.2 Local queries do factor

For every local effect/operator \(E_A\), standard QM gives

\[
q_{E_A}(\rho_{AB})
=\operatorname{Tr}[(E_A\otimes I_B)\rho_{AB}]
=\operatorname{Tr}[E_A\operatorname{Tr}_B(\rho_{AB})].
\]

Hence

\[
q_{E_A}=\bar q_{E_A}\circ\operatorname{Tr}_B,
\qquad
\bar q_{E_A}(\rho_A)=\operatorname{Tr}(E_A\rho_A).
\]

So the reduced density operator is sufficient for the declared local-query family even though it is insufficient for unrestricted global reconstruction.

### Scoped outcomes

```text
partial trace as standard-QM subsystem reduction:
  VALID_IN_DOMAIN

partial trace -> unrestricted global reconstruction:
  RECONSTRUCTION_LOSS

local quantum query family through the reduced state:
  VALID_IN_DOMAIN

global correlation query through one local reduction:
  NOT_SUFFICIENT_FOR_EXTENSION
```

---

## 5. Relativistic finite-domain specialization

Let the finite event carrier be

```text
P1 = (0, 0)
P2 = (1, 0.5)
P3 = (1, 2)
P4 = (3, 0)
```

and fix

\[
O=(2,0).
\]

In the prior PHY-REL-005 comparator,

\[
D=J^-(O)\cap\{P1,P2,P3,P4\}=\{P1,P2\}.
\]

Take two global records

```text
G1:
  P1 = alpha
  P2 = beta
  P3 = outside-1
  P4 = future-1

G2:
  P1 = alpha
  P2 = beta
  P3 = outside-2
  P4 = future-2
```

and define

\[
f_R(G)=G|_D.
\]

Then

\[
f_R(G_1)=f_R(G_2),
\qquad
G_1\neq G_2.
\]

### 5.1 An outside-domain query does not factor

Let

\[
q_{P3}(G)=G(P3).
\]

Since

\[
q_{P3}(G_1)\neq q_{P3}(G_2),
\]

this query is not constant on the restriction fiber. Therefore

\[
\boxed{
q_{P3}\text{ does not factor through }G\mapsto G|_D.
}
\]

### 5.2 A declared domain-local query does factor

For example,

\[
q_{P1}(G)=G(P1)
\]

is determined by \(G|_D\), so it factors through the restriction map.

This is a set-theoretic statement about the declared finite record. It must not be strengthened to the physical claim that every datum in \(J^-(O)\) is actually measured, stored, or operationally accessible to the observer/system.

### Scoped outcomes

```text
causal/domain record restriction:
  VALID_IN_DOMAIN

restricted record -> unrestricted global record:
  RECONSTRUCTION_LOSS

query explicitly depending only on retained record:
  VALID_IN_DOMAIN

outside-domain query from restricted record alone:
  NOT_SUFFICIENT_FOR_EXTENSION
```

---

## 6. What is genuinely common

The two specializations share the following theorem-level skeleton:

\[
\boxed{
X\xrightarrow{f}Y,
\quad
\mathcal F_y=f^{-1}(y),
\quad
q\text{ recoverable from }f(x)
\iff
q\text{ constant on }\mathcal F_y.
}
\]

This gives a real common theorem rather than a vocabulary-level analogy.

The common conclusion is only:

```text
non-injective reduction
  -> non-singleton fibers
  -> unrestricted source reconstruction fails
  -> selected queries remain recoverable exactly when they are fiber-constant.
```

### Status

**COMMON MAP-LEVEL THEOREM: ADMITTED.**

This is the first Track-2 common-theorem-gate result that is explicitly proved from abstract map structure rather than imported from QM or relativity.

---

## 7. Where the physical analogy stops

The following differences are essential.

### 7.1 Carrier decomposition

Quantum reduction requires a supplied tensor factorization

\[
\mathcal H_{AB}=\mathcal H_A\otimes\mathcal H_B.
\]

Relativistic domain restriction uses a spacetime/event domain selected through geometry and causal relations.

Therefore

\[
\boxed{
\text{tensor factor}\neq\text{spacetime subset/domain}.
}
\]

### 7.2 Map type

The partial trace is a specific linear positive trace-preserving quantum map between operator spaces.

A domain restriction is fundamentally a restriction/pullback-type operation on fields or records. It may be linear in a chosen field representation, but linearity is not part of the abstract record restriction used here.

Hence

\[
\boxed{
\operatorname{Tr}_B\neq(-)|_D.
}
\]

### 7.3 Meaning of locality

For standard QM, local observables on \(A\) satisfy an exact trace identity through \(\rho_A\).

For relativity, \(P\in J^-(O)\) expresses causal eligibility. It does not by itself prove actual measurement access, storage, readout completeness, or reconstruction by a physical observer/system.

Thus

\[
\boxed{
\text{QM local-query sufficiency}
\neq
\text{relativistic causal eligibility}.
}
\]

### 7.4 Lost information type

Partial trace can erase global correlation information even when the global state and both subsystems are defined at the same time slice.

Causal/domain restriction erases records outside a declared spacetime domain. It does not, merely by being a restriction, define quantum-style correlation loss or entanglement.

Therefore

```text
entanglement has no counterpart derivable from the causal restriction map alone.
```

### 7.5 Extra standard-theory relations can change reconstruction scope

A relativistic field equation and Cauchy/domain-of-dependence theorem can make data on one region sufficient to determine another region under explicit hypotheses.

A single quantum marginal does not recover erased global correlations without additional assumptions/data or a separate reconstruction theorem.

The common fiber theorem therefore concerns only the declared reduction map and query. It does not override theory-specific dynamics or completion theorems.

---

## 8. DSD consequence

The current DSD interface should retain a generic role such as

\[
\Pi_O:X\to X_O
\]

or another explicitly declared reduction/readout map, with fibers recording erased distinctions.

But the DSD layer must not infer the physical meaning of \(\Pi_O\) from the existence of a nontrivial fiber.

In particular, from

\[
\Pi_O(x)=\Pi_O(x')
\]

one may infer only relative descriptive indistinguishability under the declared projection. One may not infer, without an external specialization,

```text
quantum entanglement,
causal disconnection,
spatial separation,
hidden dimension,
measurement collapse,
or physical information destruction.
```

This is already consistent with Structural Reorganization Dynamics, which defines latent structural distinction only as a distinction erased by the selected descriptive projection.

No core DSD revision is required.

---

## 9. Verdict

```text
GENERIC FIBER EQUIVALENCE                           : PASS
FIBER-FACTORIZATION CRITERION                       : PROVED
NONINJECTIVE MAP -> UNRESTRICTED RECONSTRUCTION LOSS: PROVED
QM PARTIAL TRACE INSTANTIATES THE MAP THEOREM        : PASS
RELATIVISTIC DOMAIN RESTRICTION INSTANTIATES IT      : PASS
QM LOCAL QUERY = RELATIVISTIC CAUSAL ACCESS          : NON_IDENTICAL
TENSOR FACTOR = SPACETIME DOMAIN                     : NON_IDENTICAL
PARTIAL TRACE = CAUSAL RESTRICTION                    : NON_IDENTICAL
ENTANGLEMENT FROM GENERIC NONINJECTIVITY              : REJECTED
CAUSAL INACCESSIBILITY FROM GENERIC NONINJECTIVITY    : REJECTED
NEW DSD CORE AXIOM REQUIRED                           : NO
NEW QUANTUM OR RELATIVISTIC LAW DERIVED               : NO
QUANTUM-GRAVITY CLAIM                                 : NO
```

Overall verdict:

\[
\boxed{\textbf{PASS\_WITH\_BOUNDARY}}
\]

The common structure is stronger than analogy because the fiber-factorization theorem is genuinely shared. The physical meanings are nevertheless theory-specific and must remain separated.

---

## 10. Reproducibility

Script:

```text
audits/science/2026-09-08_cross_restriction_factorization_firewall.py
```

Run from repository root:

```bash
python audits/science/2026-09-08_cross_restriction_factorization_firewall.py --mode all
```

Dependencies:

```text
Python standard library only
```

The script independently calculates the Bell-state partial traces and local/global queries, reconstructs the finite Minkowski causal-domain witness, and tests finite fiber-factorization conditions.

---

## 11. Next target

Continue the countermodel search by testing whether the role

```text
reversible representation change
```

is genuinely common across QM and relativity or only superficially similar.

Recommended comparator:

```text
QM:
  unitary basis/representation change vs physical unitary state evolution

Relativity:
  invertible coordinate/frame change vs physical spacetime/state evolution
```

The key stress test is whether DSD can keep

\[
\boxed{
\text{passive representation change}
\neq
\text{active physical transition}
}
\]

without importing either theory's group action as a DSD primitive.