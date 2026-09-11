# DSD Audit — Collatz r=17 global AP-union closure

Date: 2026-09-11

Status: `SAFE EXACT SET-UNION COMPRESSION / r=17 CLOSED / r<=16 OPEN`

Canonical math note:

- `dominicus9708/Math-verification/collatz/notes/2026-09-11-math068-r17-global-ap-union-closure.md`

## 1. Audit question

MATH-067 leaves 76,866 completed negative-candidate AP cylinders in the `r=17`, `65<=m<=1023` band.

The DSD question is whether different macro/AP lineages may be merged without losing proof-relevant information.

## 2. Resolution boundary

Before macro completion, lineage includes phase, slack, dyadic source congruence, endpoint affine map, and reduced-cost information.  Arbitrary merging there is unsafe.

After a branch has completed the audited macro and has already been classified as a negative-cost candidate, the remaining obligation used by MATH-068 is only:

> Does this ordinary target integer eventually enter the frozen verified region `<=2^71`?

At this resolution, two states with the same ordinary integer are not merely similar. They are the same deterministic Collatz state.

Therefore the legitimate projection is

\[
\text{completed macro lineage}
\longrightarrow
\text{ordinary target integer set}.
\]

## 3. Safe AP set equality

A finite AP cylinder is

\[
P(a,b,m)=\{a+bk:0\le k<m\}.
\]

For `m>1`, APs may be unioned without information loss only when their grids agree:

\[
(b,a\bmod b)
\]

and the corresponding parameter intervals overlap or touch.

This is exact ordinary-set union.

For `m=1`,

\[
P(a,b,1)=\{a\}=P(a,1,1).
\]

Hence the step `b -> 1` for singletons discards only an obsolete coordinate.  It does not identify different ordinary integers.

## 4. Safe future merge

The shortcut Collatz map is deterministic. Therefore

\[
x=y
\Longrightarrow
T^j(x)=T^j(y)\quad\forall j\ge0.
\]

Once two different histories arrive at the same ordinary integer, retaining both histories for the future-descent obligation is redundant.

This differs sharply from earlier unsafe compressions in which distinct symbolic states merely shared Hensel or aggregate correction data.

## 5. Exact finite result

The medium band begins with

\[
76\,866\text{ AP representations}
\]

and 14,980,075 lineage-counted target occurrences.

Same-grid set union gives 70,426 intervals with summed grid multiplicity 13,995,185.

Exact shortcut-set propagation gives:

- depth 10: 1,259,308 singleton states;
- depth 120: 1,929 states;
- depth 307: 2 states;
- depth 315: 1 state;
- depth 333: one value still above `2^71`;
- depth 334: that value is below `2^71`;
- sweep 335: empty unresolved set.

Thus every target in the medium band reaches the frozen floor, with exact maximum reach depth 334.

Together with the MATH-067 small/large multiplicity closures, the entire `r=17` layer is closed.

## 6. Claim hierarchy

### SAFE

1. exact same-grid AP union;
2. exact shortcut AP splitting;
3. singleton canonicalization by literal set equality;
4. exact equality merge of ordinary integers after macro completion;
5. removal of integers already at or below the frozen verification floor;
6. `r=17` paid-count closure in the current first-cell calculation;
7. combined `r>=17` paid-count closure with MATH-065.

### OPEN

1. `2<=r<=16`;
2. the complete first universal cell;
3. later Farey cells;
4. Collatz conjecture.

### PROHIBITED

1. Do not transfer singleton equality merging backward to pre-completion symbolic states.
2. Do not merge different ordinary integers merely because low-bit residues or AP slopes agree.
3. Do not infer first-cell closure from `r>=17` closure.
4. Do not interpret finite descent in this first-cell candidate family as universal Collatz descent.

## 7. Methodological consequence

The correct DSD distinction is now four-level:

\[
\boxed{
\text{symbolic resolution collapse}
\neq
\text{singleton handoff}
\neq
\text{ordinary-set equality merge}
\neq
\text{paid-layer closure}.
}
\]

MATH-068 is safe because it crosses from symbolic to ordinary resolution only after the proof-facing macro conditions have already been preserved and audited.
