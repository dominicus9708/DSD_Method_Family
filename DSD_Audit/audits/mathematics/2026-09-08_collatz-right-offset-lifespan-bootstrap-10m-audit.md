# DSD-AUDIT-20260908-MATH-022 — Collatz right-offset lifespan bootstrap to 10^7

Date: 2026-09-08

Verdict:

`CONFIRMED / FINITE EXACT / STRUCTURAL COMPUTATIONAL ACCELERATION`

Global status:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Audited claim

MATH-021 proves that a right offset `r` near an internal adjacent-block boundary can participate in a same-endpoint collision only at depths

\[
k\ge3r+1.
\]

MATH-022 exhausts every

\[
0\le r\le10^7.
\]

After exact depth-61 prefix filtering, 17,745 right offsets remain.  Every surviving offset is continued for all 339 internal boundaries.  None remains in the coefficient-survival candidate language through depth 512; the maximum lifespan is 429, attained first at

\[
r=276,199,\qquad b=1177.
\]

The smallest halo-entry depth among all audited survivors is 2110, from `r=703`.

Therefore every audited right state dies strictly before its collision-halo entry, and the MATH-021 linear halo implies

\[
\boxed{
\text{no internal adjacent-block same-endpoint candidate pair for}
\quad61\le k\le30,000,003.
}
\]

## DSD tuple

### D — Definition

The finite domain and downstream event are explicit:

- offsets `0..10,000,000`;
- internal boundaries `1025..1363`;
- universal-spine coefficient-survival candidate language;
- same-endpoint cross-boundary coupling only.

### R — Resolution

MATH-021 supplies the exact collision-complete coordinate `r` through the linear displacement bound.  MATH-022 therefore does not scan irrelevant exponentially large endpoint halos.

The candidate threshold used through continuation depth 512 is checked against the exact frozen-floor inequality

\[
(3+2^{-71})^q>2^k
\]

with exact integer arithmetic.  The minimum integer q agrees with the simpler `3^q>=2^k` threshold at every used depth.

### S — Selection

Stage 1 exhaustively evaluates every offset in `[0,10^7]` through depth 61.

Exactly

\[
17,745
\]

survive all prefix gates.

Stage 2 continues only these exact survivor states, using

\[
T^{61}(b2^{61}+r)=T^{61}(r)+b3^{q_{61}(r)}.
\]

This is a safe calculation reduction, not sampling.

### E — Exclusion

For each surviving offset and each internal boundary, its exact candidate lifespan is followed until prefix failure.

Results:

- no state survives through depth 512;
- maximum lifespan = 429;
- no state satisfies `lifespan >= 3r+1`.

Thus every audited right offset is excluded before it can enter the collision-complete halo.

### T — Transition

For any depth

\[
61\le k\le30,000,003,
\]

the MATH-021 displacement theorem forces

\[
r\le\lfloor(k-1)/3\rfloor\le10^7.
\]

Therefore every potential right offset at those depths lies inside the exhaustively audited finite domain.

The transfer from offset audit to depth interval is exact.

### C — Consistency

MATH-022 is consistent with MATH-019/MATH-020's larger-halo endpoint separation.

It identifies an earlier gate: the actual collision-complete small-offset region has no live right candidate at the time collision eligibility begins.  The previous endpoint-order calculations remain valid but are not needed for exclusion in this interval.

### N — Norm

Evidence status:

`ESTABLISHED_WITHIN_SCOPE / FINITE EXACT`

No claim is made beyond `r<=10^7` or depth `30,000,003`.

### O — Outcome

Closed within scope:

1. all right offsets `0..10^7` are classified;
2. none reaches its halo-entry depth;
3. internal adjacent-block same-endpoint coupling is excluded through depth 30,000,003.

Open:

1. right offsets above `10^7`;
2. same-block candidate structure;
3. outer-window competitors;
4. unrelated Hensel/terminal-correction constraints;
5. first universal cell and Collatz.

## Prohibited upgrades

Do not infer finite bootstrap behavior for unaudited offsets.

Do not infer internal endpoint independence implies candidate emptiness.

Do not infer endpoint locality closes full arbitrary-word Hensel maximality.

Do not promote the depth interval to arbitrary depth.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_right_offset_lifespan_bootstrap_10m_certificate.cpp`

Math-verification note:

`collatz/notes/2026-09-08-right-offset-lifespan-bootstrap-10m.md`

Audit ID:

`DSD-AUDIT-20260908-MATH-022`
