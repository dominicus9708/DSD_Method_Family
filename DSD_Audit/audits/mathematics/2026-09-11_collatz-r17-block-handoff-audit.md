# DSD Audit — Collatz r=17 block handoff closure

Date: 2026-09-11
Status: `SAFE WITHIN FIRST-CELL PAID-COUNT SCOPE`

Canonical math result: `dominicus9708/Math-verification`, MATH-068.

## Audit object

The remaining `r=17` medium-multiplicity negative-candidate cylinders satisfy

\[
65\le m\le1023.
\]

MATH-068 propagates them by two exact 8-step shortcut blocks before ordinary-integer continuation.

## Information preserved

For one target AP

\[
n=a+bk,
\qquad b\text{ odd},
\]

splitting `k` modulo `2^8` fixes `n mod 2^8` and therefore the complete next 8-step parity word. Each residue slice maps exactly to another AP.

Preserved coordinates:

1. exact ordinary-integer lineage;
2. exact AP base and odd step;
3. exact finite multiplicity;
4. exact low-8-bit parity selector;
5. exact floor comparison.

No density or independence approximation is used.

## Resolution transitions

The following statements are distinct and must not be merged:

1. `family split`: one AP becomes exact residue-slice APs;
2. `family contraction`: after one block each surviving AP has multiplicity at most 4;
3. `singleton handoff`: after two blocks every survivor has multiplicity 1;
4. `ordinary closure`: every unique singleton is directly continued to `<=2^71`;
5. `layer closure`: only after 1–4 may `r=17` be declared closed.

MATH-068 satisfies all five levels.

## Exact counts

- input medium core: 76,866 cylinders / 14,980,075 occurrences;
- first 8-step block closes 9,587,872 occurrences;
- second 8-step block closes 2,777,528 additional occurrences;
- remaining singleton occurrences: 2,614,675;
- unique singleton states: 1,826,810;
- maximum tail descent after handoff: 318 steps;
- total safe bound from original medium target: 334 steps.

Together with MATH-066/067, `r=17` is closed.
Together with MATH-065, every `r>=17` multi-paid layer is closed.

## Open boundary

The audit does not transfer this finite layer result to `r<=16`, first-cell emptiness, later Farey cells, or the Collatz conjecture.

Current detailed paid-count frontier:

\[
\boxed{2\le r\le16.}
\]
