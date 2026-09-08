# DSD-AUDIT-20260908-MATH-039 — depth-36 q=24 partitioned Hensel-event audit

## Verdict

`CONFIRMED WITHIN q=24 LAYER / EXTERNAL-PARTITION EXACT / SPARSE EVENT STRUCTURE`

Collatz conjecture remains `OPEN`.

The first universal Farey cell remains `OPEN`.

## Audited claim

The complete coefficient-surviving q=24 Hensel child layer at depth 36 is generated from exactly two parent sources:

- depth-35 q=24 even children;
- depth-35 q=23 odd children.

An exact 128-way residue partition yields:

\[
169{,}991{,}585\text{ child records}
\]

and

\[
169{,}991{,}555\text{ distinct Hensel classes}.
\]

Thus exactly 30 collision classes occur in this q=24 layer, all multiplicity two.

Source decomposition:

\[
\boxed{0\text{ even/even}+20\text{ odd/odd}+10\text{ even/odd}}.
\]

Therefore all twenty q=23 collision events from MATH-038 are inherited through odd transition, no depth-35 q=24 parent collision is inherited through even transition, and ten genuinely new cross-branch q=24 mergers are formed.

## DSD tuple

### D — Describability

Each child record contains the exact Hensel residue and its parent-source bit. Collision events are counted only after exact equality of residues modulo `3^24`.

### R — Resolution

Exact finite depth 36, exact q=24, exact modulo `3^24`. External partitioning is only a storage decomposition; it does not lower mathematical resolution.

### S — Selection

The generator prunes all parent q values except 23 and 24 because only those can produce q=24 at the next step. Coefficient survival is enforced before emission.

### E — Exclusion

No candidate is excluded by partition assignment. Buckets form a disjoint exact cover of the residue records. Candidate exclusion from a collision still requires a separately audited positive ordinary-start credit.

### T — Transition

Source tagging distinguishes:

- inherited even/even collision;
- inherited odd/odd collision;
- new even/odd merger.

The exact observed decomposition is `0 / 20 / 10`.

### C — Consistency

The totals satisfy

\[
169{,}991{,}585-169{,}991{,}555=30,
\]

matching the 30 multiplicity-two collision classes and zero higher multiplicity.

### N — Norm

`ESTABLISHED_WITHIN q=24 FINITE SCOPE`.

The full depth-36 all-q Hensel collision set is not claimed closed by this audit.

### O — Outcome

The sparse-event route remains computationally viable after replacing a monolithic sort with exact external partitioning. At the audited minimal-next q layer the event set is only 30 classes despite roughly 170 million child records.

## Next-step boundary

A depth-37 q=24 one-shot partition job exceeded the current single-run execution budget. That failed execution is not evidence. The next calculation should further partition the job or construct a class-level two-pass intersection so the event set is evaluated without a single 258M-record run.

## Prohibited upgrades

- q=24 finite layer ⇒ full depth-36 closure — **PROHIBITED**;
- 5→20→30 finite event counts ⇒ asymptotic event law — **PROHIBITED**;
- storage partition ⇒ mathematical quotient — **PROHIBITED**;
- collision event ⇒ ordinary-start exclusion without credit verification — **PROHIBITED**.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_coefficient_hensel_depth36_q24_partition_certificate.cpp`

Certificate commit:

`0a8e40dc2bffd978f8020edefc590b949608ad83`

Explanatory note:

`collatz/notes/2026-09-08-coefficient-hensel-depth36-q24-partitioned-events.md`

Note commit:

`0709406abd3204da4a3e9acbe01d7610581bfb6c`
