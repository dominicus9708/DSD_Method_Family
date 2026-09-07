# DSD-AUDIT-20260908-MATH-020 — Collatz ordered endpoint separation through depths 80–81

## Verdict

`CONFIRMED / FINITE EXACT / ORDERED-SEPARATION PERSISTS THROUGH DEPTH 81`

Global status remains:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Audited result

MATH-019 established that at depth 79 every common `(boundary,Q)` cell has strict one-sided endpoint order

\[
\max E_L<\min E_R.
\]

Because depths 80 and 81 satisfy

\[
k-q_{\min}(k)=29,
\]

the same complete local halo can be reused with only a larger exact tail descriptor.

The exact range audit gives:

### Depth 80

- common `(boundary,Q)` cells: `4,993`;
- common-Q-count distribution: `14→114`, `15→203`, `16→22` boundaries;
- every cell satisfies strict left-below-right order;
- minimum same-Q endpoint separation: `1253`;
- minimum witness cell: boundary `1275`, `Q=51`.

### Depth 81

- common `(boundary,Q)` cells: `4,899`;
- common-Q-count distribution: `13→6`, `14→179`, `15→149`, `16→5` boundaries;
- every cell satisfies strict left-below-right order;
- minimum same-Q endpoint separation: `1880`;
- minimum witness cell: boundary `1073`, `Q=52`.

Combined with MATH-019:

\[
\Delta_{79}^{\min}=837,
\quad
\Delta_{80}^{\min}=1253,
\quad
\Delta_{81}^{\min}=1880.
\]

No internal adjacent-block endpoint collision exists through depth 81 within the audited candidate-language halo scope.

## DSD tuple

### D — Describability

The state is described by exact boundary label, final odd-count `Q`, and normalized endpoint interval.  No probabilistic or average state is introduced.

Outcome: `ESTABLISHED_WITHIN_SCOPE`.

### R — Resolution

Depths 80 and 81 both reuse the complete `m=29` halo because

\[
80-q_{\min}(80)=81-q_{\min}(81)=29.
\]

Tail resolution is increased exactly to `2^19` and `2^20`, respectively.

Outcome: `ESTABLISHED_WITHIN_SCOPE`.

### S — Selection

Every local state must satisfy all coefficient-survival prefix inequalities before entering its normalized endpoint cell.

No state is selected by heuristic margin or sampled phase.

Outcome: `CONFIRMED`.

### E — Exclusion

All common-Q cells are excluded from endpoint equality by strict interval order:

\[
Z_L^{\max}<Z_R^{\min}+3^Q.
\]

Equivalently,

\[
\max E_L<\min E_R.
\]

Outcome: `CONFIRMED` for depths 80 and 81.

### T — Transition

The same normalized endpoint identity used in MATH-019 is retained at each tail length:

\[
Z_k=2^{k-61}E_k-a3^Q.
\]

The computation is exact, but the three-depth persistence is **not** promoted to an arbitrary-depth transition theorem.

Outcome: `CONFIRMED FINITE / RECURSIVE LAW OPEN`.

### C — Consistency

The depth-80 and depth-81 range calculations were run independently for left/right state sets and then checked by a separate post-audit.

Expected summary constants are asserted in the post-audit.

Outcome: `CONFIRMED`.

### N — Norm

Classification:

`FINITE EXACT`.

The sequence of positive minimum separations is evidence for a structural target, not an asymptotic theorem.

### O — Outcome

The active proof-search line is now the **ordered-separation recurrence problem** rather than blind depth extension.

Define

\[
\Delta_k(b,Q)=\min E_R-\max E_L.
\]

For every defined common-Q cell at `k=79,80,81`,

\[
\Delta_k(b,Q)>0.
\]

The next DSD target is the smallest exact endpoint-residue refinement that makes the sign of `Delta` closed under one-step propagation.

A scalar interval alone is not sufficient because the next shortcut branch depends on endpoint parity.  Therefore residue information must be retained explicitly.

Depth 82 also introduces a new `m=30` outer halo shell, so future work must separate core propagation from shell injection.

## Prohibited upgrades

Do not infer:

- finite ordered separation through depth 81 => arbitrary-depth separation;
- `837,1253,1880` => asymptotic growth law;
- candidate-set order => global Collatz monotonicity;
- internal-boundary exclusion => first-cell closure.

## Reproducibility

Range generator:

`collatz/src/2026_09_08_depth80_81_normalized_range_generator.cpp`

Commit:

`f9763f3e54290a76ed371b70d1f0e4d79de3a542`

Post-audit:

`collatz/src/2026_09_08_depth80_81_normalized_range_postaudit.py`

Commit:

`05b72fab5151ae37787aa4002608c838d82c49c8`

Explanatory note:

`collatz/notes/2026-09-08-depth80-81-ordered-endpoint-separation.md`

Commit:

`a3f7d27da10e53814e86c2a05a8c2f9c0e77f946`
