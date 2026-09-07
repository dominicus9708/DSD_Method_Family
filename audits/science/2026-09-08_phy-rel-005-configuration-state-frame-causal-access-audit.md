# PHY-REL-005 — Configuration-State Audit of Frame/Representation and Causal Accessibility

Date: 2026-09-08
Status: **PASS_WITH_REFINEMENT**
Track: **2 — Full DSD structural analysis of standard quantum mechanics and relativity**

## 1. Purpose

This audit tests the third detailed Track-2 target:

```text
Relativity
  chart / coordinate representation
  inertial-frame representation
  causal classification
  causal/domain accessibility
  coordinate ordering
  reconstruction after domain restriction
```

The target distinction is

\[
\boxed{
\text{representation change}
\neq
\text{causal-access change}
\neq
\text{reconstruction loss}
}.
\]

The question is whether the current DSD configuration-state interface can preserve these distinctions without identifying coordinate/frame labels with causal accessibility or DSD lineage.

No quantum-gravity candidate or alternative-gravity premise is used.

---

## 2. Source and interface lock

### Standard relativity

For special relativity, use standard Minkowski spacetime and proper orthochronous Lorentz boosts. For a boost in one spatial direction with units \(c=1\),

\[
\begin{pmatrix}t'\\x'\end{pmatrix}
=
\begin{pmatrix}
\gamma & -\gamma\beta\\
-\gamma\beta & \gamma
\end{pmatrix}
\begin{pmatrix}t\\x\end{pmatrix},
\qquad
\gamma=(1-\beta^2)^{-1/2}.
\]

The Minkowski interval with signature \((-+)\) is

\[
\Delta s^2=(\Delta x)^2-(\Delta t)^2.
\]

A coordinate chart in general relativity is a separate but related representation notion: valid chart-transition maps are invertible on their overlap. The finite computation in this audit uses inertial Lorentz frames only; it does not numerically model arbitrary curved-spacetime chart transitions.

Standard background reference:

```text
Sean M. Carroll, Lecture Notes on General Relativity,
arXiv:gr-qc/9712019.
```

### DSD interfaces

The present comparison-state interface keeps representation and access as separate entries:

\[
\Sigma_{R,t}=(F_{R,t},P_{R,t},R_{R,t},A_{R,t},\Phi_{R,t}).
\]

Here the symbols are audit-level roles, not new DSD core axioms.

The Property Axiom System places optional representations downstream of the completed core descriptor, while Static Aggregation separately requires injectivity/support information for reconstruction from reduced outputs. Structural Reorganization Dynamics additionally separates state/domain transitions from ordinary value evolution.

---

## 3. Invertible Lorentz-frame change is representation change, not information loss

For \(|\beta|<1\), the 1+1 boost matrix has

\[
\det\Lambda
=
\gamma^2(1-\beta^2)
=1.
\]

Hence the boost is invertible.

The reproducibility script evaluates \(\beta=0.6\) and confirms numerically

```text
det Lambda = 1
invertible = True
```

while also checking preservation of the Minkowski interval.

### Scoped outcome

```text
Lorentz representation change: VALID_IN_DOMAIN
representation change = information loss: REJECTED
```

The coordinate components change, but no distinction is discarded merely by the invertible frame transformation.

This does not imply that every coordinate representation is global or that every chart covers the full spacetime. A chart-domain restriction is a separate issue.

---

## 4. Spacelike coordinate-time order can reverse without changing causal class

Take

\[
A=(t,x)=(0,-1),
\qquad
B=(0,+1).
\]

Then

\[
\Delta s^2=4>0,
\]

so the separation is spacelike.

For \(\beta=+0.6\), the script obtains

```text
A': t' = +0.75
B': t' = -0.75
```

so \(B\) is earlier in coordinate time.

For \(\beta=-0.6\),

```text
A': t' = -0.75
B': t' = +0.75
```

so \(A\) is earlier.

The interval remains \(+4\) in both frames.

Therefore

\[
\boxed{
\text{coordinate-time order of spacelike events}
\not\Rightarrow
\text{frame-independent causal order}
}.
\]

### Scoped outcome

```text
coordinate-time ordering for spacelike events:
  VALID_IN_DOMAIN as a frame-coordinate record

coordinate-time ordering -> causal lineage:
  NOT_SUFFICIENT_FOR_EXTENSION
```

This is not a failure of coordinate time. It is a scope boundary on what that record can determine.

As a control, the script also checks a timelike pair and confirms that future order is preserved under the tested proper orthochronous boosts.

---

## 5. Causal accessibility is not a coordinate-frame label

Fix an event

\[
O=(2,0)
\]

in 1+1 Minkowski spacetime. The standard causal past is

\[
J^-(O)
=
\{P:\ O-P\text{ is future-directed causal}\}.
\]

For the finite point set

```text
P1 = (0, 0)
P2 = (1, 0.5)
P3 = (1, 2)
P4 = (3, 0)
```

the script finds

```text
P1 in J^-(O): True
P2 in J^-(O): True
P3 in J^-(O): False
P4 in J^-(O): False
```

After the same Lorentz boost is applied to \(O\) and all four points, the membership pattern is unchanged.

Thus the causal-access classification is compatible with the Lorentz representation change while remaining a different structural role from the coordinate labels themselves.

### Scoped outcome

```text
frame representation and causal accessibility: NON_IDENTICAL
Lorentz-frame change automatically changes causal eligibility: REJECTED
```

Important boundary: membership in \(J^-(O)\) is only a causal-eligibility condition. It does not assert that a physical system has actually measured, stored, or reconstructed every datum in its causal past. Additional operational readout restrictions may exist.

---

## 6. Causal-domain restriction can be locally valid and globally non-reconstructive

Let a finite global record assign values to the four events above. Construct two records

```text
G1:
  P1 = alpha
  P2 = beta
  P3 = outside-value-1
  P4 = future-value-1

G2:
  P1 = alpha
  P2 = beta
  P3 = outside-value-2
  P4 = future-value-2
```

They are globally distinct but agree on every point in \(J^-(O)\).

Define the restriction

\[
\mathcal A_O(G)=G|_{J^-(O)}.
\]

Then

\[
G_1\neq G_2,
\qquad
\mathcal A_O(G_1)=\mathcal A_O(G_2).
\]

Therefore the finite restriction map is non-injective relative to the global-reconstruction target.

### Scoped outcomes

```text
causal-domain record for questions restricted to J^-(O):
  VALID_IN_DOMAIN

causal-domain record -> full global record:
  NOT_SUFFICIENT_FOR_EXTENSION
  RECONSTRUCTION_LOSS
```

This is a finite structural witness inside a standard Minkowski causal specialization. It is not a theorem that every relativistic physical readout has exactly this finite-record form.

---

## 7. DSD configuration-state refinement

The audit supports the following separation:

\[
R_{R,t}
=
\text{representation/chart/frame data},
\]

\[
A_{R,t}
=
\text{declared access/domain data},
\]

\[
\Phi_{R,t}
=
\text{selected readout/restriction data when supplied}.
\]

The three must not be collapsed merely because an application often discusses them together.

The stronger refinement is

\[
\boxed{
\text{representation completeness}
\neq
\text{access completeness}
\neq
\text{global reconstruction completeness}
}.
\]

This mirrors, without identifying, the quantum result from PHY-QM-051:

```text
QM:
  local-state completeness for local queries
  != global-state reconstruction completeness

Relativity:
  frame/chart completeness on its declared domain
  != causal/global accessibility
  != global reconstruction from a restricted domain
```

The two standard theories exhibit a common map/scope pattern, not a common physical primitive.

---

## 8. Outcome-semantics application

This audit is the first detailed Track-2 audit to use the reporting rule

```text
methodology/AUDIT_OUTCOME_SEMANTICS.md
```

The negative-looking results are therefore not written as generic failures.

```text
Lorentz transformation:
  VALID_IN_DOMAIN

frame representation = causal access:
  NON_IDENTICAL

spacelike coordinate-time order -> causal lineage:
  NOT_SUFFICIENT_FOR_EXTENSION

causal-domain restriction -> full global reconstruction:
  NOT_SUFFICIENT_FOR_EXTENSION
  RECONSTRUCTION_LOSS
```

No tested standard-relativity object failed its own declared domain criteria in this audit.

---

## 9. DSD core impact

No revision of the Formation Axiom System, Property Axiom System, Channel-Indexed Static Aggregation, or Structural Reorganization Dynamics is required by this result.

The audit reinforces existing disciplines:

```text
representation is downstream data;
valid maps are used only on declared domains;
reduced records do not reconstruct full inputs without injectivity;
domain/access status must remain distinct from value evolution and lineage;
coordinate labels do not create causal or successor identity by themselves.
```

---

## 10. Status classification

### Exact standard-relativity / mathematical results used

- proper Lorentz boosts are invertible;
- the Minkowski interval is Lorentz invariant;
- spacelike-separated event coordinate-time order can reverse between inertial frames;
- causal classification is preserved by Lorentz transformation.

### Finite witness produced here

- a four-event causal-domain restriction with two distinct global records giving the same restricted record;
- explicit numerical order reversal at \(\beta=\pm0.6\).

### DSD structural interpretation

- representation, access, readout, and reconstruction must remain separate roles;
- valid in-domain representation/access records need not support a stronger global reconstruction claim.

### Not established

- no new relativistic law is derived from DSD;
- no DSD causal cone is derived;
- no identification of relativistic causal speed with \(c_{info}\) is made;
- no quantum-gravity conclusion follows;
- no claim is made that causal past membership alone equals actual measurement accessibility.

---

## 11. Verdict

\[
\boxed{\textbf{PASS\_WITH\_REFINEMENT}}
\]

The current DSD configuration-state interface survives the relativity frame/access test, with the refinement that representation-domain completeness, causal eligibility, operational access, and global reconstruction are separate notions.

---

## 12. Reproducibility

Script:

```text
audits/science/2026-09-08_rel_chart_frame_causal_access.py
```

Run from repository root:

```bash
python audits/science/2026-09-08_rel_chart_frame_causal_access.py --mode all
```

Dependencies:

```text
Python standard library only
```

Prior compatible control:

```text
audits/science/2026-09-07_qm_sr_typed_interface.py
```

which independently checks Lorentz-boost invertibility in the earlier typed-interface audit.

---

## 13. Next target

Continue Track 2 with:

```text
Relativity — Cauchy data / domain of dependence / reconstruction
```

The next audit should distinguish at least:

```text
initial data on a supplied hypersurface,
constraint satisfaction,
standard evolution relation,
domain of dependence,
uniqueness/reconstruction only under the standard theorem hypotheses,
DSD state/access/transition roles.
```

The standard Cauchy theorem remains an external relativity result and must not be converted into a DSD theorem by re-description alone.
