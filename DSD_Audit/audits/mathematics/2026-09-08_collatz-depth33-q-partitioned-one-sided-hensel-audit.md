# DSD-AUDIT-20260908-MATH-043 — depth-33 q-partitioned one-sided Hensel audit

## Verdict

`CONFIRMED / FINITE EXACT / ONE-SIDED ROOT-HENSEL`

Collatz and the first universal cell remain `OPEN`.

## D

The audited object is the depth-33 candidate language after coefficient survival and all-prefix one-sided root-Hensel maximality through depth 32.

## R

Exact finite depth 33; exact final q and exact correction residue modulo `3^q`.

## S

Candidate side uses the `33,880,411` MATH-042 survivors.  Competitor side remains unrestricted within each `(k,q,r)` Hensel class.

Since `q_min(33)=21`, both children of every MATH-042 state pass the coefficient gate, giving exactly `67,760,822` pre-Hensel candidates.

## E

Each q-layer is independently compared against the maximum correction among all arbitrary length-33 parity words with that q.

## T

For a 16+17 split and `t` odd positions in the lower half,

\[
C=3^{q-t}C_{16,t}+2^{16}C_{17,q-t}.
\]

This is an exact decomposition, so the MITM enumeration covers exactly `binom(33,q)` arbitrary words per layer.

## C

Exact totals:

- pre-Hensel: `67,760,822`;
- newly pruned: `33,545`;
- all-prefix survivors: `67,727,277`;
- full coefficient language: `82,694,966`;
- cumulative Hensel-removed coefficient classes: `14,967,689`.

The q=21 layer was separately audited with the reverse-Hensel oracle; the q=22 and q=23 MITM layers contain `193,536,720` and `92,561,040` arbitrary words respectively and return exact class maxima without candidate-class collisions.

## N

`ESTABLISHED_WITHIN_SCOPE / FINITE EXACT`.

## O

The q-partitioned route remains computationally viable through depth 33.  Depth 34 crosses into roughly `1.25e8` pre-Hensel candidates, so a second residue-bucket partition is the next required calculation refinement.

## Reproducibility

- certificate: `Math-verification/collatz/src/2026_09_08_depth33_q_partitioned_mitm_hensel_certificate.cpp`
- result ledger: `Math-verification/collatz/results/2026-09-08-depth33-q-partitioned-one-sided-hensel.tsv`
- depth-33 checkpoint SHA-256: `e8696c1f6b9cc027f7d782d288c9cc054a051bae918ee89caf15453fec154941`

## Prohibited upgrades

- finite depth 33 ⇒ arbitrary depth — **PROHIBITED**;
- newly-pruned count ⇒ asymptotic density — **PROHIBITED**;
- q-layer decomposition ⇒ independence of actual Collatz trajectories — **PROHIBITED**;
- prefix survivors ⇒ first-cell survivors — **PROHIBITED**.
