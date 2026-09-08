# DSD-AUDIT-20260908-MATH-042 — depth-32 q-partitioned one-sided Hensel audit

## Verdict

`CONFIRMED / FINITE EXACT / ONE-SIDED ROOT-HENSEL`

Collatz and the first universal cell remain `OPEN`.

## D

The audited object is the intersection of the frozen coefficient-surviving candidate language with unrestricted root-Hensel class maximality at every prefix through depth 32.

## R

Exact finite depth 32.  Hensel class key is `(q,C mod 3^q)`.  Candidate state is retained at full correction resolution; no coarse quotient is introduced.

## S

Candidate side: coefficient-surviving and already Hensel-maximal through depth 31.

Competitor side: arbitrary parity word of the same depth and q.  This is the required one-sided selection and corrects the earlier two-sided interpretation of MATH-037~039.

## E

A candidate is removed iff an arbitrary competitor in the same Hensel class has larger correction.  Positive credit is

\[
d=(C_{\max}-C_{\rm cand})/3^q.
\]

## T

MATH-013 downstream dominance ensures a prefix that is not class-maximal cannot regain maximality under a common suffix.  Hence pruning at every depth is exact and descendants of removed prefixes need not be generated.

## C

Depth-31 checkpoint is independently regenerated at `19,347,686` states.  Depth-32 q-layers sum to:

- pre-Hensel candidates: `33,894,412`;
- newly pruned: `14,001`;
- all-prefix survivors: `33,880,411`.

The independent full coefficient language count is `41,347,483`, so cumulative Hensel removal is `7,467,072` classes.

Large q=21 and q=22 layers and representative q=24,26,30 layers were cross-checked by a separate MITM enumeration and the reverse-Hensel oracle with exact agreement.

## N

`ESTABLISHED_WITHIN_SCOPE / FINITE EXACT`.

## O

Depth-32 Hensel pruning is now exact without materializing the global unrestricted class table.  This improves the computation route but does not empty the first cell.

## Reproducibility

- checkpoint generator: `Math-verification/collatz/src/2026_09_08_depth31_packed_hensel_checkpoint_generator.cpp`
- q-layer certificate: `Math-verification/collatz/src/2026_09_08_depth32_q_partitioned_one_sided_hensel_certificate.cpp`
- result ledger: `Math-verification/collatz/results/2026-09-08-depth32-q-partitioned-one-sided-hensel.tsv`
- depth-32 checkpoint SHA-256: `35093b29775e538c99ba692851c4fe6112e86437ddbdae9ad4ea177cd4698013`

## Prohibited upgrades

- finite depth 32 ⇒ arbitrary depth — **PROHIBITED**;
- prefix survivors ⇒ terminal first-cell survivors — **PROHIBITED**;
- high-q near-vacuity ⇒ universal high-q vacuity — **PROHIBITED**;
- Hensel maximality ⇒ Collatz convergence — **PROHIBITED**.
