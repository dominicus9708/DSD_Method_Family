# DSD Audit — Collatz depth 1--41 unified re-audit

Date: 2026-09-12

Verdict: `PASS WITH SCOPE BOUNDARIES / DEPTH 1--41 FINITE RESULTS INTERNALLY CONSISTENT`

This audit applies the current DSD analysis/audit rules to the canonical Collatz depth results from depth 1 through 41. Paid-count layers `2<=r<=13` are explicitly outside scope because they have not been closed.

## 1. Evidence classes

The audit distinguishes four evidence classes.

1. **Exact algebraic identity** — valid independently of finite depth.
2. **Exact finite computation** — valid only for the stated depth/range.
3. **Representation quotient** — valid only for the future question whose sufficient state is proved.
4. **Observed finite pattern** — hypothesis-generating only.

No finite observation is promoted to a global theorem.

## 2. Formation completeness

Coefficient-surviving parity prefixes are defined by the all-prefix condition

\[
3^{q_j}\ge2^j
\]

for every prefix depth `j`.

The new unified certificate reconstructs the complete prefix language exactly for every depth 1--41 and reproduces all canonical anchor counts, including

\[
L_{20}=27,328,
\quad L_{24}=286,581,
\quad L_{28}=3,524,586,
\quad L_{32}=41,347,483,
\quad L_{41}=12,805,670,000.
\]

**PASS:** no terminal-only approximation is substituted for the all-prefix formation rule.

## 3. Exact state closure

The earlier integrated DSD state

\[
\Xi_k=(r_k,y_k,R_k,u_k,v_k,Q_k,e_k)
\]

satisfies

\[
2^k y_k=3^{Q_k}r_k+R_k.
\]

The canonical integrated audit checked 100,701,368 exact branch transitions through depth 32 with zero closure and transition-identity failures.

The present reanalysis normalizes

\[
S=R_k/3^q,
\qquad
\rho=2^k/3^q,
\]

giving

\[
\boxed{\rho y=r+S}.
\]

**PASS:** the new common-coordinate description is an exact reparameterization of the prior depth state, not a new fitted model.

## 4. State redundancy audit

At fixed depth/state lineage:

- `u_k=3^q` is derived from q;
- `v_k=2^k` is derived from k;
- the old correction numerator is `R_k=3^q S`;
- `rho=2^k/3^q` is derived from `(k,q)`;
- `y=(r+S)/rho`;
- coefficient excess `e_k` is derived from `(k,q)`.

Thus the older seven/eight-field description contains substantial redundancy.

A minimal exact depth-state description may be written

\[
\boxed{(k,q,r,S)}.
\]

**PASS WITH CONDITION:** the exact address `r` cannot be removed. `(S,rho)` alone is not future-complete for parity/macro compatibility.

## 5. Notation collision audit

The repository has used `R` in two distinct roles:

1. old depth-state `R_k`: correction numerator;
2. recent Bellman-resolution `R(M)=ceil(log2 M)`: address-resolution height.

These are mathematically unrelated quantities.

**REQUIRED RULE:** future combined documents must write the old correction as `C_k` or `R_corr`, and reserve `R_res(M)` (or another explicit symbol) for resolution height.

This is a notation-risk finding, not a mathematical contradiction.

## 6. Same-integer lineage

The exact depth cylinder has source residue/address `r mod 2^k`. The block identity maps its lifts affinely.

The endpoint quotient `y_i=y_j` is future-complete only for forward ordinary-integer dynamics after the common endpoint. It is not automatically source-lineage preserving.

Similarly, MATH-051's bounded-carry quotient is future-complete for the question of existence of a positive Hensel translation witness, not for arbitrary next-macro compatibility.

Therefore the current address state must be split:

\[
\boxed{
\mathcal A=(\mathcal A_{compat},\mathcal A_{dom}).
}
\]

- `A_compat`: exact dyadic source/endpoint compatibility;
- `A_dom`: Hensel/carry dominance state.

**PASS:** the current framework keeps these roles separate.

**PROHIBITED:** replacing `A_compat` by the bounded-carry state alone.

## 7. Hensel/common-coordinate bridge

MATH-051 and MATH-072 give

\[
\Sigma=S+\rho-1.
\]

At fixed `(k,q)`, `rho` is fixed, hence

\[
\Delta\Sigma=\Delta S.
\]

The integral Hensel translation condition is therefore an integral normalized-correction difference.

Combined with

\[
y=(r+S)/\rho,
\]
this explains why Hensel translation and endpoint/source translation are closely related but not identical: exact source address must still satisfy the corresponding integer/dyadic relation.

**PASS:** common quantity identified without collapsing address compatibility into Hensel class membership.

## 8. Nested Hensel lineage audit, depths 32--41

For every `k=33..41` and every admissible q-layer, the canonical prefilter obeys

\[
P_{k,q}=S_{k-1,q}+S_{k-1,q-1}.
\]

The new certificate verifies the identity exactly at every q-layer.

For each depth 32--41,

\[
P_k-S_k=\text{new pruning},
\]

and

\[
L_k-S_k=\text{cumulative Hensel removal}.
\]

**PASS:** no unexplained population, hidden independent filter, or cross-depth candidate loss is present in the canonical ledgers.

## 9. Representation-change audit

Depths 32--41 were computed using several exact implementations:

- q-partitioned ledgers;
- residue buckets;
- partitioned/mixed shards;
- flat/tail hashes;
- fixed-d bounded-carry finite states.

These are representation changes, not changes to the accepted mathematical language.

The depth-41 finite-state solver was explicitly regressed against canonical depth-40 central-layer counts before being accepted.

**PASS:** representation efficiency is separated from mathematical pruning.

## 10. Finite trend audit

Observed on depths 32--41:

- cumulative one-sided Hensel removal remains near 18% of the coefficient language;
- incremental new-depth pruning is only about 0.03--0.05% of the nested prefilter;
- at depth 41, about 98.99% of new pruning lies within `q<=q_min+3`.

**STATUS:** `FINITE PATTERN ONLY`.

These observations support the interpretation that Hensel dominance is concentrated near the coefficient boundary, but they do not prove an asymptotic density, limiting fraction, or eventual saturation theorem.

## 11. Depth-range verdicts

### Depth 1--31

`PASS — formation/state dynamics`.

These depths lie inside the exhaustive integrated depth-32 dynamics computation. Exact formation, branch transitions, and block identities are covered. A separate modern complete fixed-d Hensel ledger is not asserted for every one of these depths.

### Depth 32

`PASS — bridge checkpoint`.

Integrated DSD dynamics + q-partitioned Hensel ledger coexist and agree on the coefficient language.

### Depth 33--34

`PASS — q-partitioned nested Hensel`.

Nested lineage identity passes. Depth 34 records four candidate-class representation collisions explicitly; they are accounted for, not silently discarded.

### Depth 35--40

`PASS — complete one-sided Hensel finite ledgers`.

Different implementation strategies preserve exact ledger semantics.

### Depth 41

`PASS — complete finite-state one-sided Hensel checkpoint`.

The exact result remains finite. No inference to arbitrary depth is permitted.

## 12. Current common-state candidate

The audit supports the following decomposition for cross-method work:

\[
\boxed{
\text{analytic state}\times\text{compatibility state}\times\text{dominance state}
}
\]

with analytic coordinates

\[
(S,\rho,\Omega),
\]

compatibility coordinates containing exact dyadic address/resolution, and dominance coordinates containing the Hensel carry/subset state when needed.

For a depth-only exact state, `(k,q,r,S)` is sufficient.

For Bellman/paid analysis, the currently useful expanded state is

\[
(S,\rho,\Omega,R_{res},\mathcal A_{compat},\mathcal A_{dom}).
\]

## 13. Claim boundaries

This audit does **not** establish:

- closure of paid layers `2<=r<=13`;
- arbitrary-depth bounded carry size;
- a uniform Hensel removal ratio;
- sufficiency of `(S,rho,Omega)` without address information;
- first universal cell emptiness;
- the Collatz conjecture.

## 14. Audit result

\[
\boxed{
\text{Depths 1--41 are internally consistent under the current DSD state, lineage, and claim-scope rules.}
}
\]

The most important new result of the re-audit is not an additional finite depth. It is the exact reduction

\[
\boxed{2^k y=3^q r+C\quad\Longleftrightarrow\quad \rho y=r+S}
\]

and the consequent separation of redundant analytic coordinates from irreducible dyadic compatibility information.

Reproducibility companion:

`dominicus9708/Math-verification/collatz/src/2026_09_12_depth1_41_unified_dsd_reaudit_certificate.py`
