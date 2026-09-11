# DSD Audit — Collatz singleton-resolution handoff and paid-layer repair

Date: 2026-09-11
Domain: mathematics / Collatz proof attempt
Status: `AUDIT CORRECTION APPLIED / r>=18 PAID LAYERS CLOSED WITH REPAIRED LINEAGE / GLOBAL PROOF OPEN`

## 1. Audited failure mode

The historical MATH-064 pipeline correctly proved that 752 `r=22` phase/address cells could contain only singleton completed parity cylinders.

The information-loss error occurred at the next inference:

\[
\text{singleton in symbolic graph}
\not\Rightarrow
\text{ordinary-integer branch closed}.
\]

A state whose source multiplicity has collapsed from a family to one ordinary integer has changed representation.  It has not disappeared.

In DSD terms, this is a **resolution handoff**, not an elimination rule.

The required lineage is

\[
\boxed{
\text{symbolic cylinder}
\to
\text{singleton source}
\to
\text{ordinary target}
\to
\text{descent/cost verdict}.
}
\]

Skipping the last two arrows loses proof-relevant information.

## 2. Repaired invariant

The repaired MATH-065 state carries at every parity prefix:

1. the exact phase cell;
2. the original source-lift congruence
   \[
   t\equiv\tau\pmod{2^h};
   \]
3. the exact affine endpoint after the same substitution;
4. accumulated paid penalty;
5. a rigorous minimum possible future penalty.

A branch may be removed only if

- its exact source congruence has empty intersection with the allowed source interval; or
- its current cost plus rigorous future minimum already reaches the target slope; or
- after completion, every represented ordinary target is directly closed by descent.

Source multiplicity `1` is not itself a removal condition.

## 3. Repaired r=22 result

The complete r=22 audit is now

\[
\begin{array}{lr}
\text{phase/address cells} &1192\\
\text{cost-safe} &433\\
\text{singleton-only} &752\\
\text{multi-source critical} &7\\
\text{negative-candidate cylinders} &2184\\
\text{target occurrences} &2188\\
\text{unique targets} &1338.
\end{array}
\]

All 1338 unique targets reach the frozen verified floor `2^71`; maximum additional shortcut length is 123.

Thus `r=22` closure survives the audit, but the historical 18-target argument was only a partial subcalculation on the seven multi-source-critical cells.

## 4. Frontier transcription correction

MATH-063 proves

\[
r=23\text{ is not automatically multi-source safe},
\qquad
r=24\text{ is the first such count}.
\]

The historical MATH-064 prose accidentally promoted the automatic range to start at 23.  MATH-065 corrects this and audits `r=23` directly.

This is classified as a **dependency-transcription error**, distinct from the singleton information-loss error.

## 5. Uniform repaired audit result

The same exact branch-and-bound method was applied without a singleton shortcut to every paid count from 18 through 64.

Finite ordinary-target continuation closes `r=18..26`.

For every

\[
27\le r\le64,
\]

no completed cylinder remains whose rigorous lower adjusted cost can be negative.

MATH-062 separately proves the analytic cost closure for every

\[
r\ge65.
\]

Hence

\[
\boxed{r\ge18\text{ is closed for the current first-cell multi-paid calculation}.}
\]

The remaining detailed paid-count frontier is

\[
\boxed{2\le r\le17.}
\]

## 6. DSD status table

### SAFE

- exact phase refinement;
- exact dyadic same-source lineage;
- exact affine endpoint lineage;
- rigorous future-cost lower-bound pruning;
- explicit singleton-to-ordinary-integer handoff;
- direct finite descent certificates;
- MATH-062 analytic `r>=65` closure.

### CORRECTED

- `singleton => closed` — rejected;
- historical `r>=23 automatic multi-source safety` — corrected to `r>=24` before direct r=23 audit.

### OPEN

- paid counts `2<=r<=17`;
- mixed one-paid / remaining multi-paid Bellman closure;
- full first universal Farey cell;
- later cells;
- Collatz conjecture.

### PROHIBITED UPGRADES

- resolution handoff may never be counted as elimination without a terminal verdict;
- finite paid-layer closure may not be promoted to first-cell closure;
- first-cell closure, if later obtained, may not be promoted to full Collatz without later-cell coverage.

## 7. Reusable general audit rule

Whenever an exact quotient or compression maps a family to a singleton, DSD Audit must ask:

> What proof obligation moved to the singleton, and where is its terminal verdict recorded?

The correct state transition is

\[
\text{many candidates}
\to
\text{one candidate}
\to
\text{audit that candidate},
\]

not

\[
\text{many candidates}
\to
\text{one candidate}
\to
\varnothing.
\]

This rule should be reused in later Collatz layers and in other exact-search proof programs.
