# DSD Audit — Collatz MATH-084/085 one-paid finite horizon and depth-6 Bellman replay

Date: 2026-09-12

Status: `PASS MATH-084 AS EXACT HORIZON THEOREM / PASS MATH-085 AS FINITE EXACT REPLAY CLAIM / GLOBAL ONE-PAID BELLMAN CLOSURE STILL OPEN`

## 1. Scope

This audit reviews two new claims:

1. MATH-084: multi-source one-paid symbolic chains have a finite macro horizon in the current first-cell source window;
2. MATH-085: every newly singleton-resolved terminal at macro depths 4, 5, and 6 is Bellman-safe under the MATH-082 universal wedge or the exact current-phase penalty infimum.

The audit does not include paid-count layers `2<=r<=13` and does not claim first-cell emptiness or the Collatz conjecture.

## 2. MATH-084 source-window argument

The audited source window is

\[
2^{71}<Y<2U,
\qquad
U=1364\cdot2^{61}+Q_0/3.
\]

Exact arithmetic gives

\[
2U-2^{71}<2^{72}.
\]

A composed source cylinder has spacing \(2^H\). If two ordinary source anchors remain in one cylinder, their displacement is at least \(2^H\), and that displacement must fit inside the source window. Therefore

\[
\boxed{\text{multi-source}\Rightarrow H\le71.}
\]

This is an exact width argument. It does not use density, random parity, or an average-count approximation.

`PASS`.

## 3. Finite macro horizon

Every one-paid macro has

\[
H_e=L+2+\varepsilon\ge3.
\]

After \(t\) macros,

\[
H\ge3t.
\]

Combining with the multi-source requirement \(H\le71\) gives

\[
\boxed{t\le23.}
\]

Thus a 24th one-paid macro cannot still have a multi-source source cylinder in the audited window.

This is a finite symbolic-horizon theorem. It is not a Bellman-safety theorem for the eventual singleton.

`PASS`.

## 4. Relation to the earlier 73-bit Bellman potential

MATH-082 used

\[
B(H)=\max(0,73-H)
\]

as a coarse potential based on the absolute source upper bound below \(2^{73}\).

MATH-084 uses the narrower actual source-window width to prove

\[
H\ge72\Rightarrow\text{source count}\le1.
\]

These are related but not identical statements:

- `73-bit potential`: a coarse Bellman bookkeeping device with an audited root boundary allowance;
- `H<=71 multi-source theorem`: an exact source-window multiplicity statement.

Do not silently replace one by the other inside an existing Bellman inequality without rechecking its boundary term.

`PASS WITH NOTATION/SEMANTIC SEPARATION REQUIRED`.

## 5. MATH-085 current-phase coordinate

MATH-085 stores current phase rather than initial phase history:

\[
J=(\Omega^-_{cur},\Omega^+_{cur}),
\qquad
\mathcal P=\alpha\Omega_{cur}.
\]

For one exact macro edge,

\[
J'=\rho_e(J\cap I_e),
\]

\[
\alpha'=\alpha/\rho_e+c_e,
\qquad c_e\in\{1/4,1/8\}.
\]

This follows algebraically from

\[
\Omega' = \rho_e\Omega
\]

and

\[
p_e=c_e\Omega'.
\]

No phase information required for the next edge is discarded.

`PASS`.

## 6. Address compatibility is retained

MATH-085 does **not** use the failed phase-only quotient. For each next edge it still enforces the exact dyadic condition

\[
B+3^Q s\equiv A_e\pmod{2^{H_e}}.
\]

Because \(3^Q\) is odd, this fixes one exact residue class of the current source parameter. The child source count is then computed exactly.

The historical composed `source_A` is not used in future transition tests, but the current target intercept, odd-count exponent, source count, and next-edge source residue are preserved. This is a projection of unused lineage metadata, not removal of compatibility information.

`PASS`.

## 7. Finite depth-4/5/6 terminal results

The recorded exact replay gives:

| macro depth | new terminal handoffs | universal-wedge safe | exact-phase safe total | ordinary residual | multi-source survivors |
|---:|---:|---:|---:|---:|---:|
| 4 | 76,585 | 76,564 | 76,585 | 0 | 442,957 |
| 5 | 372,841 | 372,834 | 372,841 | 0 | 1,689,024 |
| 6 | 1,358,935 | 1,358,914 | 1,358,935 | 0 | 4,943,810 |

At depth 6 the largest terminal accumulated depth is

\[
H=90.
\]

Every multi-source survivor at depths 4--6 satisfies \(H\le71\), consistent with MATH-084. For the latter statement MATH-084 supplies the general proof, so the finite observation is no longer carrying theorem weight.

`PASS AS FINITE EXACT REPLAY CLAIM`.

## 8. Sharding and streaming audit

Depth 6 is evaluated by exact disjoint source-index shards and streaming depth-5 children into depth 6.

These operations affect only memory scheduling:

\[
S=\bigsqcup_i S_i.
\]

Every source parent belongs to exactly one shard; every child transition is computed by the same rule. Cross-shard duplicates, if any, create repeated proof work but cannot delete a candidate.

`PASS`.

## 9. What the finite success suggests

Depths 4--6 show that after exact address compatibility and source resolution, the universal wedge plus exact current-phase penalty bound is strong enough to remove every new terminal from the low-cost Bellman search without ordinary continuation.

This supports the search for a general terminal inequality over the finite MATH-084 horizon.

However, the observed sequence

\[
0,0,0\text{ ordinary residuals at depths }4,5,6
\]

is not itself an induction rule.

## 10. Prohibited upgrades

Do not infer:

- `t<=23 multi-source` => every one-paid chain is Bellman-safe;
- depth 4--6 terminal safety => depths 7--24 are automatically safe;
- Bellman-safe terminal => ordinary Collatz descent has been independently proved for that integer;
- source-window singleton resolution => first-cell emptiness;
- phase coordinate compression => dyadic address may be discarded;
- finite one-paid horizon => mixed one-paid/multi-paid problem is closed.

## 11. Verdict

MATH-084 is accepted as an exact structural theorem:

\[
\boxed{\text{multi-source one-paid macro depth}\le23.}
\]

MATH-085 is accepted as an exact finite replay through macro depth 6 under the canonical compatibility rules:

\[
\boxed{\text{ordinary Bellman residual}=0\text{ at depths }4,5,6.}
\]

The next proof-facing target is no longer unbounded symbolic depth. It is to derive a depth-independent terminal inequality, valid over the finite horizon \(1\le t\le24\), that combines exact address resolution with the current-phase penalty lower bound.
