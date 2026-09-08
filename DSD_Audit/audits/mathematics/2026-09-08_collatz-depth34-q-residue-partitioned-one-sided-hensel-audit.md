# DSD-AUDIT-20260908-MATH-044 — depth-34 q/residue-partitioned one-sided Hensel audit

## Verdict

`CONFIRMED / FINITE EXACT / ONE-SIDED ROOT-HENSEL / RESOURCE-PARTITION REFINEMENT`

Collatz and the first universal cell remain `OPEN`.

## D

The object is the depth-34 candidate language after coefficient survival and one-sided unrestricted root-Hensel maximality at every prior prefix.

## R

Exact depth 34; exact final q; exact Hensel residue `C mod 3^q`; exact correction maximum inside each class.

## S

Candidate side comes only from MATH-043 survivors and must satisfy the depth-34 coefficient threshold `q>=22`.  Competitor side is unrestricted among arbitrary length-34 parity words of the same q.

## E

A candidate is removed iff its correction is not the unrestricted maximum of its exact Hensel class.  Candidate-candidate class collisions are therefore only one subcase of one-sided elimination.

## T

For the 17+17 MITM split,

\[
C=3^{q-t}C_{17,t}+2^{17}C_{17,q-t}.
\]

The q=23 layer is additionally partitioned into four disjoint exact residue buckets.  Since equal Hensel residues always fall in the same bucket, class maxima cannot cross buckets; the four-bucket sum is exactly the full layer result.

## C

Exact totals:

- pre-Hensel candidates: `124,547,105`;
- all-prefix survivors: `124,486,440`;
- newly pruned: `60,665`;
- full coefficient language: `151,917,636`;
- cumulative Hensel-removed coefficient classes: `27,431,196`.

For q=22:

- candidates `32,474,274`;
- distinct candidate Hensel classes `32,474,270`;
- survivors `32,432,663`;
- total candidate removals `41,611`;
- credit range `2..287`.

For q=23:

- candidates `39,151,495`;
- survivors `39,138,196`;
- newly pruned `13,299`;
- credit range `2..71`.

The failed monolithic q=23 run is excluded from evidence; only the completed four-bucket audit is used.

## N

`ESTABLISHED_WITHIN_SCOPE / FINITE EXACT`.

## O

One q-layer no longer suffices as the computational partition at this depth.  A second residue partition is now part of the exact calculation engine.  This changes resource layout only; it does not strengthen the theorem beyond finite depth 34.

## Reproducibility

- Math-verification ledger: `collatz/results/2026-09-08-depth34-q-partitioned-one-sided-hensel.tsv`
- Math-verification note: `collatz/notes/2026-09-08-depth34-q-partitioned-one-sided-hensel.md`

## Prohibited upgrades

- finite depth 34 ⇒ arbitrary depth — **PROHIBITED**;
- resource partition ⇒ mathematical quotient — **PROHIBITED**;
- candidate-class collision count ⇒ total Hensel-pruning count — **PROHIBITED**;
- prefix survivors ⇒ first-cell terminal survivors — **PROHIBITED**.
