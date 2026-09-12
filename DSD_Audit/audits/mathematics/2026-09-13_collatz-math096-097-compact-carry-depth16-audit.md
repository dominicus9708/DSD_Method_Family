# DSD Audit — Collatz MATH-096/097 compact carry and depth-16 closure

Date: 2026-09-13

Status: `PASS / t=16 BELLMAN-SAFE / 7<=t<=15 OPEN`

## 1. Scope

This audit reviews two linked claims:

1. MATH-096: finite normalized 2-adic precision `P(R)=73+R` is sufficient for every future one-paid compatibility decision from a multi-source family of resolution `R`;
2. MATH-097: using that compact state inside a phase-danger over-approximation closes every potentially negative singleton handoff at macro depth 16.

The audit does not promote Bellman safety to an ordinary Collatz descent theorem.

## 2. Hensel quotient identity

For an exact cylinder

\[
A+2^Hs\mapsto B+3^Qs,
\]

the affine correction identity gives

\[
X=3^{-Q}B=\frac{A+S}{2^H}.
\]

Thus `X` is a quotient/carry coordinate after consumption of the low `H` Hensel-address bits.  This is an exact identity, not a heuristic correspondence with earlier bounded-carry work.

`PASS`.

## 3. Precision sufficiency

Let `R=ceil(log2 M)`.  A future terminal one-paid edge needs at most 73 current 2-adic bits.  Before that terminal, the sum of resolutions consumed by multi edges is at most `R`.  Therefore `73+R` current bits are sufficient for the entire future.

More locally, if a multi edge consumes `h`, then `R'<=R-h`, while MATH-092 propagates `P` exact bits to `P-h`. Hence

\[
73+R'\le(73+R)-h.
\]

No high bit needed by a later compatibility test is discarded.

`PASS`.

## 4. Phase-danger corridor direction

MATH-097 first forgets address and keeps the minimum penalty representative of each exact phase cell. This can only enlarge the set of potentially dangerous paths. The backward corridor from negative depth-16 terminal cells therefore contains every actual negative same-integer path.

Actual states are retained whenever their exact phase interval intersects a corridor interval, which is again one-sided toward over-inclusion.

`PASS`.

## 5. Compact-state deduplication

The retained exact state contains:

- total source-modulus depth `H`;
- exact source count `M`;
- exact current phase interval;
- `X mod 2^(73+R)`;
- `G=3^(-Q) mod 2^(73+R)`.

MATH-096/092 show that these values determine every future one-paid phase/address transition relevant to the search. Therefore identical compact tuples may be merged without losing a future distinction.

`PASS`.

## 6. Universal terminal necessity

Every one-paid macro pays strictly more than `1/9`. For `t=16`, any negative terminal must satisfy

\[
z=h-R\ge48.
\]

This is a necessary condition only. MATH-097 uses it only for pruning edges that cannot possibly be negative.

`PASS`.

## 7. Exhaustive address result

The depth-15 compact danger corridor contains 2,460,473 states. Across those states there are exactly 45,094,414 phase-compatible canonical edge attempts satisfying `z>=48`.

Exact normalized residue testing gives zero with `r<M`. The minimum observed `r-M` is 197,239,627, so the incompatibility is strict rather than a boundary artifact.

Therefore no actual same-integer terminal at macro depth 16 can realize a negative Bellman margin.

`PASS`.

## 8. Claim hierarchy

The valid upgrade is

\[
\boxed{t=16\text{ Bellman-safe}.}
\]

Do not infer:

- `t=16` Bellman-safe `=>` ordinary descent theorem for all represented integers;
- `t=16` closure `=>` one-paid language fully closed;
- compact-state finiteness `=>` small symbolic state space;
- phase-danger exclusion `=>` address can be omitted elsewhere.

The unresolved detailed one-paid band is

\[
\boxed{7\le t\le15.}
\]

## 9. Verdict

MATH-096 and MATH-097 pass the DSD audit.  They establish a proof-facing finite carry/address state and use it to remove macro depth 16 without raw large-integer trajectory enumeration.
