# DSD-AUDIT-20260908-MATH-018 — Collatz depth-61→79 tail complete descriptor

## Verdict

`CONFIRMED / EXACT FINITE DESCRIPTOR / COMPUTATIONAL ACCELERATION`

Global status remains:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Audited claim

For `0 <= r < 2^18`, define

\[
G_{18}(r)=\bigl(H_{18}(r),s_{18}(r),T^{18}(r)\bigr),
\]

where

\[
H_{18}(r)=\max_{1\le j\le18}\bigl(q_{\min}(61+j)-s_j(r)\bigr).
\]

For a depth-61 endpoint decomposed as

\[
n=h2^{18}+r,
\]

this descriptor is complete for the following finite downstream predicates:

1. coefficient survival through depths 62..79;
2. final odd-count at depth 79;
3. exact endpoint at depth 79.

Specifically,

\[
q_{61}\ge H_{18}(r)
\]

is equivalent to coefficient survival through the whole 18-step tail, and

\[
T^{18}(n)=T^{18}(r)+h3^{s_{18}(r)}.
\]

## DSD tuple

### D — Describability

The state is explicitly represented as low dyadic residue plus high affine coordinate:

\[
n=h2^{18}+r.
\]

The descriptor retains every quantity needed by the audited tail predicates.

Outcome: `ESTABLISHED_WITHIN_SCOPE`.

### R — Resolution

The descriptor uses the full exact modulus `2^18`.  No coarser residue substitution is made.

Outcome: `ESTABLISHED_WITHIN_SCOPE`.

### S — Selection

Tail survival is selected by exactly one threshold test:

\[
q_{61}\ge H_{18}(r).
\]

The threshold itself is computed from every intermediate prefix depth, so no intermediate coefficient condition is skipped.

Outcome: `ESTABLISHED_WITHIN_SCOPE`.

### E — Exclusion

Failure of the threshold rejects the finite depth-79 coefficient-survival mechanism only.  It does not reject the ordinary integer as a Collatz candidate globally.

Outcome: `ESTABLISHED_WITHIN_SCOPE` with scope guard.

### T — Transition

Because the first 18 parity bits depend only on residue modulo `2^18`, addition of `h*2^18` preserves the tail parity word.  The exact affine shortcut formula then yields

\[
T^{18}(h2^{18}+r)=T^{18}(r)+h3^{s_{18}(r)}.
\]

Outcome: `CONFIRMED`.

### C — Consistency

Certificate checks:

- all `262,144` residues;
- all relevant base odd-counts `q61=39..61` for the survival equivalence;
- deterministic high coordinates `h=0,1,2,17,339,1024,1363` for implementation regression of parity and endpoint affine reconstruction;
- exact `H18` distribution and cumulative survival counts.

Outcome: `CONFIRMED`.

### N — Norm

Classification:

`FINITE EXACT / COMPUTATIONAL ACCELERATION`.

The descriptor is not promoted to an arbitrary-depth theorem or a complete Collatz state.

### O — Outcome

The repeated 18-step tail evolution needed by the depth-79 halo calculation may be replaced by a precomputed `2^18` descriptor table plus O(1) exact lookup/reconstruction per query.

No new first-cell exclusion follows from MATH-018 alone.

## Exact distribution regression

`H18` counts:

```text
39 16936
40 42414
41 55274
42 55882
43 44050
44 27498
45 13384
46 5002
47 1394
48 274
49 34
50 2
```

Total:

\[
262144=2^{18}.
\]

## Prohibited upgrades

Do not infer:

- finite tail completeness => full-state completeness;
- tail lookup acceleration => stronger Collatz theorem;
- `q61 >= H18(r)` => first-cell candidate survives all other obligations;
- the previous depth-78 zero-collision result => depth-79 zero collision without the remaining all-boundary comparison.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_dsd_tail18_complete_descriptor.py`

Commit:

`37ecd72ad037fc00d6c95c2ee5330cb8f7fa4c0f`

Explanatory note:

`collatz/notes/2026-09-08-dsd-tail18-complete-descriptor.md`

Note commit:

`e84379a35702e903ec579d4b48b56a58ab099c5e`
