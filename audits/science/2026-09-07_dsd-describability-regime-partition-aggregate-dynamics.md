# DSD Describability-Regime Partition and Difference-Aggregate Dynamics

Date: 2026-09-07

## Status

```text
TRACK: 3 — DSD common-structuring construction
METHODS: Analysis + Audit + Static Aggregation + Dynamics + Reconstruction restraint
PRIMARY_EXTERNAL_BASE:
  standard quantum mechanics
  standard relativity
NONPRIMARY_QUANTUM_GRAVITY_PREMISES: not used
CORE_PAPER_REVISION: not required by this stage
REPRODUIBILITY:
  audits/science/2026-09-07_describability_regime_partition_dynamics.py
```

This continuation starts from the previously separated DSD–quantum and DSD–relativity describability regimes and adds the time-dependent difference regions explicitly.

The aim is not to make a quantum-gravity coupling law. The aim is to track, at each time slice, which typed descriptions belong only to the quantum-side regime, to the shared overlap, only to the relativity-side regime, or to neither selected regime, and then to separate two different causes of aggregate change:

```text
A. movement of support between describability sectors;
B. change of the aggregated data while support is retained or after it arrives in a sector.
```

---

## 1. Compatibility with the current DSD static and dynamic layers

The current Channel-Indexed Static Aggregation paper is static. It keeps Stage-VI formation-channel aggregation and optional typed-property aggregation distinct and joins them only as an ordered pair. It does not provide an evolution law.

The current Structural Reorganization Dynamics paper requires every time slice using the static interface to reduce to an admissible static construction. During a regular epoch the Stage-VI formation background remains fixed. Property values, applicability regions, analytic fields, weights, and other downstream coordinates may evolve under supplied laws. A change that alters formation-channel identity is a formation-level transition and requires explicit cross-time lineage.

Therefore the present construction is downstream of the existing core and does not replace either predecessor layer.

---

## 2. Time-dependent describability partition

Fix a comparison universe \(\Omega\) containing the items whose describability status is being compared.

At time \(t\), let

\[
Q_t\subseteq\Omega
\]

be the DSD–quantum-mechanics describability set and

\[
R_t\subseteq\Omega
\]

be the DSD–relativity describability set.

Define

\[
Q_t^{\circ}:=Q_t\setminus R_t,
\qquad
I_t:=Q_t\cap R_t,
\qquad
R_t^{\circ}:=R_t\setminus Q_t,
\]

and, when closure relative to the supplied comparison universe is useful,

\[
N_t:=\Omega\setminus(Q_t\cup R_t).
\]

Then

\[
\Omega
=
Q_t^{\circ}\;\dot\cup\;I_t\;\dot\cup\;R_t^{\circ}\;\dot\cup\;N_t.
\]

The primary three-cell descriptor is therefore

\[
\mathcal D_t
=
\bigl(Q_t^{\circ},I_t,R_t^{\circ}\bigr),
\]

with \(N_t\) retained only when the selected universe needs explicit outside bookkeeping.

This is a partition of describability status, not an identification of quantum and relativistic physical state spaces.

---

## 3. Static aggregation on the difference regions

The difference regions are set differences, not numerical differences of physical quantities.

Accordingly, the safest full typed static record is sectorwise:

```text
Q_ONLY sector:
  quantum-side admissible static descriptor restricted to Q_t minus R_t

OVERLAP sector:
  quantum-side and relativity-side typed static descriptors both retained
  unless an additional common typed aggregate is independently supplied

R_ONLY sector:
  relativity-side admissible static descriptor restricted to R_t minus Q_t
```

No subtraction such as

\[
A_Q-A_R
\]

is licensed merely because the two sectors are called a difference pair. A cross-sector subtraction requires a common additive carrier or explicit comparison/transport maps.

For a generic structural audit only, suppose a common bookkeeping Banach carrier \(B\) and a finite term map

\[
T_t:\Omega\to B
\]

are supplied. Then for each partition cell \(b\) define

\[
A_b(t)
=
\sum_{x:\,s_t(x)=b}T_t(x),
\]

where

\[
s_t(x)\in
\{Q^{\circ},I,R^{\circ},N\}.
\]

This bookkeeping specialization does not identify \(T_t\) with a quantum observable, a metric quantity, a DSD gravity source, or any other physical scalar.

---

## 4. Exact partition-aggregate balance identity

For one discrete step \(t\to t+1\), define the old-term membership flux

\[
F_{ab}(t)
:=
\sum_{x:\,s_t(x)=a,\,s_{t+1}(x)=b}T_t(x).
\]

Define the final-sector intrinsic term

\[
G_b(t)
:=
\sum_{x:\,s_{t+1}(x)=b}
\bigl(T_{t+1}(x)-T_t(x)\bigr).
\]

Then, by direct finite partitioning,

\[
\boxed{
A_b(t+1)-A_b(t)
=
\sum_{a\neq b}F_{ab}(t)
-
\sum_{c\neq b}F_{bc}(t)
+
G_b(t)
}
\]

for every sector \(b\).

### Status

**Mathematical / structural theorem.**

It is a finite set-partition identity once the common additive bookkeeping carrier is supplied. It is not a physical conservation law.

---

## 5. Explicit difference-sector dynamics

For the DSD–quantum-only difference region,

\[
\begin{aligned}
\Delta A_{Q^{\circ}}
={}&F_{I,Q^{\circ}}
+F_{R^{\circ},Q^{\circ}}
+F_{N,Q^{\circ}}\\
&-F_{Q^{\circ},I}
-F_{Q^{\circ},R^{\circ}}
-F_{Q^{\circ},N}
+G_{Q^{\circ}}.
\end{aligned}
\]

For the overlap,

\[
\begin{aligned}
\Delta A_I
={}&F_{Q^{\circ},I}
+F_{R^{\circ},I}
+F_{N,I}\\
&-F_{I,Q^{\circ}}
-F_{I,R^{\circ}}
-F_{I,N}
+G_I.
\end{aligned}
\]

For the DSD–relativity-only difference region,

\[
\begin{aligned}
\Delta A_{R^{\circ}}
={}&F_{Q^{\circ},R^{\circ}}
+F_{I,R^{\circ}}
+F_{N,R^{\circ}}\\
&-F_{R^{\circ},Q^{\circ}}
-F_{R^{\circ},I}
-F_{R^{\circ},N}
+G_{R^{\circ}}.
\end{aligned}
\]

Thus the change of each static difference aggregate has two logically different parts:

```text
membership / boundary motion
+
intrinsic aggregate evolution.
```

This distinction must be retained even if a reduced scalar readout later makes the two contributions numerically equal.

---

## 6. DSD interpretation of the two terms

### 6.1 Membership-flow term

A change

\[
Q_t^{\circ}\to I_{t+1}
\]

means that a record previously satisfying only the selected quantum-side describability conditions now also satisfies the selected relativity-side conditions.

Likewise

\[
I_t\to Q_{t+1}^{\circ}
\]

means loss of the selected relativity-side membership while the quantum-side membership remains.

These statements concern describability-regime membership, not conversion of a quantum object into a relativistic object.

### 6.2 Intrinsic term

The term \(G_b\) records change of the supplied aggregate term itself. In a regular DSD epoch this may represent permitted downstream evolution such as property-value, applicability, analytic-field, weight, access, or readout change under the chosen specialization.

If the relevant change alters Stage-VI formation-channel identity, it must not be hidden inside an ordinary regular intrinsic update. It is a formation-level transition and requires explicit cross-time lineage under the existing Structural Reorganization Dynamics rules.

---

## 7. Static snapshots do not reconstruct the dynamics

A finite two-element counterexample shows that the sequence of static difference aggregates is not enough to recover membership flow.

Let both elements have unit bookkeeping weight.

At \(t_0\):

```text
x in Q_ONLY
y in OVERLAP
```

At \(t_1\):

```text
x in OVERLAP
y in Q_ONLY
```

Then

\[
A_{Q^{\circ}}(t_0)=A_{Q^{\circ}}(t_1)=1,
\qquad
A_I(t_0)=A_I(t_1)=1,
\]

although the actual flow contains

\[
Q^{\circ}\to I
\quad\text{and}\quad
I\to Q^{\circ}.
\]

Therefore

\[
\boxed{
\Delta\mathcal A_t=0
\not\Rightarrow
\text{no describability-regime dynamics}
}
\]

and, more generally,

\[
\boxed{
\{A_b(t),A_b(t+1)\}_b
\text{ does not reconstruct }\{F_{ab}(t)\}_{a,b}
}
\]

without extra information.

### Status

**Finite counterexample / reconstruction obstruction.**

This is the dynamic counterpart of the existing DSD rule that aggregate equality does not reconstruct support or the complete typed state.

---

## 8. Time-resolution dependence

The finite witness also contains

\[
Q^{\circ}
\to I
\to R^{\circ}
\]

for one element over \(t_0,t_1,t_2\).

If only \(t_0\) and \(t_2\) are sampled, the observed transition is

\[
Q^{\circ}\to R^{\circ},
\]

and the intermediate overlap passage disappears from the coarse record.

Hence

\[
\boxed{
\text{observed transition graph depends on temporal resolution}
}
\]

unless an independent theorem guarantees that no intermediate sector was crossed.

This is a structural finite witness, not a claim that every direct quantum-only to relativity-only change must pass through the overlap.

---

## 9. Numerical finite witness

The reproducibility script gives the static weighted aggregates

```text
t0: Q_ONLY=3.0, OVERLAP=7.0,  R_ONLY=5.0, NEITHER=6.0
t1: Q_ONLY=9.0, OVERLAP=10.0, R_ONLY=2.5, NEITHER=0.0
t2: Q_ONLY=3.8, OVERLAP=13.7, R_ONLY=4.0, NEITHER=0.0
```

For both \(t_0\to t_1\) and \(t_1\to t_2\), every sector balance residual is zero up to floating-point roundoff.

The script separately verifies:

```text
static aggregate unchanged + nonzero membership flow : confirmed
fine Q_ONLY -> OVERLAP -> R_ONLY path                : confirmed
coarse Q_ONLY -> R_ONLY readout                       : confirmed
AUDIT RESULT                                           : PASS_WITH_BOUNDARY
```

---

## 10. What changed relative to the previous Track-3 stage

The previous common-structuring audit used a block-structured common record and showed that common structuring does not force cross-dynamics.

The present stage adds a different object:

\[
\boxed{
\mathcal D_t
=
(Q_t\setminus R_t,\;Q_t\cap R_t,\;R_t\setminus Q_t)
}
\]

and makes the **differences themselves time-dependent**.

The new dynamic information is therefore not only

```text
how a quantum-side variable changes,
how a relativity-side variable changes,
```

but also

```text
which records enter or leave Q_ONLY,
which records enter or leave OVERLAP,
which records enter or leave R_ONLY,
and how each sector's static aggregate changes while those transfers occur.
```

This is closer to a describability-regime partition dynamics than to the earlier block-diagonal variable evolution.

---

## 11. Boundary and next formal target

### Confirmed at this stage

1. Time-dependent Q-only / overlap / R-only partitions are mathematically well-defined once the comparison universe and membership predicates are supplied.
2. Sectorwise static aggregation can be applied without collapsing the sector types.
3. In a common bookkeeping carrier, sector-aggregate change has an exact flow-plus-intrinsic decomposition.
4. Static aggregate time series does not reconstruct sector membership flow.
5. Temporal coarse-graining can erase intermediate overlap membership.

### Not established

1. No unique physical law determines the motion of \(Q_t\) or \(R_t\).
2. No quantum-gravity coupling is derived.
3. No physical scalar subtraction between the Q-only and R-only aggregates is licensed without a common carrier or explicit maps.
4. No claim is made that overlap is physically more fundamental than either difference sector.
5. No claim is made that every direct difference-sector transition must pass through the overlap.

### Next formal target

The next extension should add a **transition-cause label** to each membership change, separating at least

```text
FORMATION_CHANGE
PROPERTY_APPLICABILITY_OR_PREREQUISITE_CHANGE
ACCESS_CHANGE
READOUT_OR_RESOLUTION_CHANGE
REGULAR_DYNAMIC_VALUE_CHANGE
```

so that geometrically identical movement of a Venn-region boundary is not treated as one mechanism when its DSD layer of origin is different.

---

## Reproducibility

Run from the repository root:

```bash
python audits/science/2026-09-07_describability_regime_partition_dynamics.py --mode all
```

The script uses only the Python standard library.

## Verdict

**PASS_WITH_BOUNDARY.**

The proposed Venn-style picture can be made mathematically sharper as a time-dependent partition of describability regimes. The two difference regions and the overlap can each carry static aggregate records, while their changes split into membership/boundary transfer and intrinsic aggregate evolution. The distinction is necessary because unchanged static aggregates can hide active sector exchange, and changing aggregates can occur without the same boundary motion. This extends the previous Track-3 common-structuring construction without introducing a quantum-gravity premise.
