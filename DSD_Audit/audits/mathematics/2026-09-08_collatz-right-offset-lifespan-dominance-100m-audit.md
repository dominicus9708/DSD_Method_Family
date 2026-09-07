# DSD-AUDIT-20260908-MATH-024 — Collatz right-offset lifespan dominance frontier through 1e8

Date: 2026-09-08

Verdict:

`CONFIRMED / FINITE ONLY / DOMINANCE-COMPRESSED EVIDENCE`

Global status:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Audited question

Using the MATH-021 linear collision-complete halo,

\[
r\le\left\lfloor\frac{k-1}{3}\right\rfloor,
\]

can the finite right-offset bootstrap be extended from `10^7` to `10^8`, and can its output evidence be compressed safely without the unsafe phase aliasing found in MATH-023?

## DSD tuple

### D — Definition

For

\[
N=b2^{61}+r,
\qquad1025\le b\le1363,
\]

define `L(b,r)` as the final depth through which the ordinary shortcut trajectory preserves the audited coefficient-survival predicate.

Define

\[
L(r)=\max_b L(b,r).
\]

The object compressed by the second half of this audit is the finite output relation `(r,L(r))`, not the full dynamical state.

### R — Resolution

Right-offset resolution is exact on every integer

\[
0\le r\le10^8.
\]

All 339 internal right-side address labels are retained exactly.

The continuation audit uses depths through 700. The frozen published-floor condition

\[
(3+2^{-71})^q>2^k
\]

is checked to coincide with

\[
3^q\ge2^k
\]

at every depth `1..700` used by the certificate.

### S — Selection

There is no sampling.

Stage 1 exhausts all `100,000,001` offsets and retains exactly those satisfying coefficient survival through depth 61.

Result:

\[
\boxed{179,754}
\]

survivors.

The first and last are

\[
703,\qquad99,999,855.
\]

Stage 2 continues each surviving lower-61 state through every `b=1025..1363` using

\[
T^{61}(b2^{61}+r)=T^{61}(r)+b3^{q_{61}}.
\]

### E — Exclusion

MATH-021 proves that same-endpoint cross-boundary collision at depth `k` requires

\[
r\le\left\lfloor\frac{k-1}{3}\right\rfloor.
\]

Equivalently, offset `r` first becomes collision-eligible at

\[
k_{\rm enter}=3r+1.
\]

Every audited state satisfies

\[
L(b,r)<3r+1.
\]

No halo-entry violation occurs.

The finite domain therefore excludes internal adjacent-block same-endpoint coupling through

\[
\boxed{3\cdot10^8+3=300,000,003}.
\]

This is a coupling exclusion only, not candidate emptiness.

### T — Transition

The largest finite candidate lifespan found is

\[
\boxed{504}
\]

at

\[
r=31,595,291,
\qquad b=1218.
\]

Selected minimum surviving offsets by depth are

| depth | minimum surviving `r` | linear collision halo |
|---:|---:|---:|
|61|703|20|
|100|703|33|
|150|703|49|
|200|6,383|66|
|250|18,599|83|
|300|18,599|99|
|350|276,199|116|
|400|276,199|133|
|450|29,660,287|149|
|500|31,595,291|166|

No audited depth has minimum surviving offset inside the collision halo.

### C — Consistency

MATH-023 showed that `(q61,T^61(r) mod 2^m)` is not a useful low-resolution exact lifespan quotient: ambiguity remains through `m=25`, while `m=26` nearly restores every original state.

MATH-024 therefore does **not** merge dynamical states by phase.

Instead it orders the exact finite outputs `(r,L(r))` and keeps only running-max records.

If `(r_i,L_i)` is a record, every survivor until the next record satisfies

\[
r\ge r_i,
\qquad L(r)\le L_i.
\]

Thus

\[
L_i<3r_i+1
\]

certifies the entire record interval against halo entry.

### N — Norm

Evidence status:

`ESTABLISHED_WITHIN_SCOPE / FINITE ONLY`.

Exactly 13 running-max dominance records summarize all 179,754 depth-61 survivor offsets:

| `r` | `L(r)` | witness `b` | `q61` |
|---:|---:|---:|---:|
|703|161|1147|42|
|1,055|182|1055|42|
|1,407|194|1264|41|
|1,583|199|1087|42|
|6,383|226|1243|42|
|17,023|245|1263|42|
|18,599|305|1229|41|
|106,239|345|1328|41|
|276,199|429|1177|42|
|11,991,359|439|1144|43|
|27,454,695|440|1152|45|
|29,660,287|462|1306|42|
|31,595,291|504|1218|42|

This is exact **evidence compression after computation**. It is not yet a proof that future input states can be skipped.

### O — Outcome

Established:

- exact finite offset audit expanded to `0..10^8`;
- `179,754` depth-61 survivor offsets;
- maximum lifespan `504` in the finite domain;
- zero halo-entry violations;
- internal adjacent-block same-endpoint coupling excluded through depth `300,000,003`;
- finite output evidence reduced to `13` dominance records.

Still open:

- offsets above `10^8`;
- a structural upper bound that avoids computing each new offset state;
- whether the 13-record dominance concept can be promoted to an input-pruning rule;
- first-cell candidate emptiness;
- Collatz.

## Prohibited upgrades

Do not infer:

\[
\text{finite }r\le10^8\Rightarrow\text{all right offsets}.
\]

Do not infer:

\[
L_{\max}=504\text{ in this domain}\Rightarrow\text{universal lifespan bound}.
\]

Do not infer:

\[
\text{no internal endpoint coupling}\Rightarrow\text{no Collatz candidate}.
\]

Do not treat the 13 output records as 13 complete dynamical states or as permission to discard uncomputed offsets.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_right_offset_lifespan_dominance_100m_certificate.cpp`

Math-verification note:

`collatz/notes/2026-09-08-right-offset-lifespan-dominance-100m.md`

Audit ID:

`DSD-AUDIT-20260908-MATH-024`
