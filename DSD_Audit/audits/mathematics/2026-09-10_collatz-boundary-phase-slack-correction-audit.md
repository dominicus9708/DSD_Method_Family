# DSD Audit — Collatz boundary phase / slack / correction bridge

Date: 2026-09-10
Status: `EXACT ALGEBRAIC REDUCTION / FINITE REGRESSION PASS / SAME-INTEGER BRIDGE OPEN`

## Scope

Audit the MATH-053 reparameterization of coefficient admissibility and normalized correction.  This audit does not upgrade the Collatz conjecture or first universal Farey cell to closed status.

## Exact reductions

Let

\[
\theta=\log_2(3/2),\quad m(q)=\lfloor q\theta\rfloor,\quad u=m(q)-d.
\]

Then

\[
3^q>2^{q+d}\iff u\ge0.
\]

The parity transitions are exactly

\[
E:u\mapsto u-1,
\qquad
O:u\mapsto u+[m(q+1)-m(q)].
\]

Define

\[
\Omega_q=\frac{2^{q+m(q)}}{3^q}.
\]

For normalized correction `S=C/3^q`, an odd step taken at current `(q,d)` contributes

\[
\boxed{\Delta S=\frac{\Omega_q}{3\,2^u}}.
\]

Therefore every coefficient-surviving word satisfies

\[
\boxed{S(w)=\frac13\sum_n 2^{-u_n}\Omega_n}.
\]

All identities are algebraic; the certificate evaluates `m(q)` through exact integer powers and compares the weighted-sum formula against the original correction recurrence with exact rationals.

## Information-loss audit

Safe to remove for the correction functional:

- the absolute `(k,d)` coordinate once `(q,u)` is known;
- repeated floating-point/log evaluation of the coefficient phase;
- the original parity word when only the scalar normalized correction is requested and the full slack history is retained.

Not safe to remove for the proof-facing same-integer problem:

- dyadic root address / ordinary starting residue;
- Hensel competitor/maximality state;
- first-cell membership and endpoint lineage.

In particular, terminal `(q,u,S)` does not uniquely determine the same ordinary integer.

## Negative audit: Hensel maximality alone is insufficient

A proposed implication

\[
\text{nested Hensel maximality}\Longrightarrow\text{uniform positive slack penalty}
\]

is rejected as a standalone bridge.

Targeted exact calculations found coefficient-boundary/extremal candidates with no same-class dominator over substantial finite tested ranges.  This is enough to reject the logical shortcut that Hensel maximality by itself forces positive slack.  It is not promoted to an arbitrary-depth theorem about that candidate family.

Therefore the proof-facing implication must retain the same-integer information:

\[
\boxed{
\text{Hensel maximality + dyadic address + first-cell/endpoint conditions}
\Longrightarrow
\text{weighted-slack lower bound}
}
\]

if such an implication is to be established.

## Exact same-integer coupling

For a parity prefix `(k,q,C)`, the ordinary starting residue is fixed by

\[
\boxed{N\equiv-C3^{-q}\pmod{2^k}}.
\]

Once `k` exceeds the bit-length of the first-cell start window, this residue is the ordinary start itself.  This equation is therefore the correct bridge between correction/Hensel coordinates and root address; the two must not be treated as independent filters.

## Required next audit

Construct an exact product state preserving:

1. mechanical coefficient phase / integer slack;
2. Hensel maximality information;
3. dyadic start address at the required resolution;
4. endpoint/correction budget.

Then test safe equivalences before merging any components.  The final target is an emptiness/no-infinite-bad-path statement, not a density or survivor-count statement.

## Prohibited upgrades

- finite regression => arbitrary-depth theorem;
- Hensel maximality => positive slack by itself;
- low survivor density => no survivor;
- scalar correction bound => same-integer address exclusion;
- common irrational rotation => identical semantic coordinate without orientation/index audit.

Collatz remains `OPEN`.
