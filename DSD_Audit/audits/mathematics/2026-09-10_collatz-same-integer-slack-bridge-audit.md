# DSD Audit — Collatz same-integer slack bridge

Date: 2026-09-10
Status: `FINITE EXACT BRIDGE / HENSEL-ONLY IMPLICATION REJECTED / UNIVERSAL PENALTY GROWTH OPEN`

## Audited claim

Candidate implication under review:

\[
\text{nested Hensel maximality}\Longrightarrow\text{positive boundary slack}.
\]

Verdict: **REJECT as a standalone bridge.**

The zero-slack mechanical boundary word remains Hensel-undominated through the finite audited frontier used in the current calculation. Therefore Hensel maximality alone is insufficient to force a positive slack penalty.

## Missing information channel

The ordinary-integer dyadic start address is non-redundant. At depth 72 the unique zero-slack mechanical word maps to top-address 2037, outside the current first-cell window 1024..1363. Thus the correct composed bridge is

\[
\boxed{
\text{same-integer address}
+\text{coefficient survival}
+\text{Hensel maximality}
\Longrightarrow
\text{slack penalty}.
}
\]

## Finite exact result

For length-72 coefficient-valid prefixes in the first-cell ordinary-start window, all prefixes with at most `B` positive-slack odd events were enumerated for `B<=5`, converted to the unique ordinary start, and that same integer was continued through root-safe depth 195.

| B | first-cell starts | coefficient survivors through 195 |
|---:|---:|---:|
| 0 | 1 | 0 |
| 1 | 5 | 0 |
| 2 | 47 | 0 |
| 3 | 585 | 0 |
| 4 | 4,484 | 0 |
| 5 | 27,959 | 7 |

Therefore any same-integer first-cell candidate obeying coefficient survival through depth 195 has at least five positive-slack odd events in the first 72 steps.

With

\[
S_*-S(w)=\frac13\sum_n(1-2^{-u_n})\Omega_n,
\qquad \Omega_n>1/2,
\]

this implies

\[
\boxed{S_*-S(w)>5/12}.
\]

A targeted nested-Hensel check through depth 72 removes one of the seven minimal budget-5 coefficient survivors at depth 56; six remain.

## DSD interpretation

The audit distinguishes three channels that must not be collapsed prematurely:

1. coefficient/mechanical boundary state;
2. exact Hensel dominance state;
3. ordinary-integer dyadic address / endpoint lineage.

The zero-slack counterexample to the Hensel-only implication shows that channel 3 carries decisive information. It cannot be treated as decorative metadata.

## Prohibited upgrades

- five slack events in the first 72 steps => positive asymptotic slack density;
- penalty >5/12 => first-cell closure;
- six budget-5 survivors through depth72 Hensel => survival through depth195;
- first-cell finite result => later strip coverage;
- any finite computation => Collatz proof.

## Next audit target

Construct an exact product state combining normalized Hensel state and same-integer address lineage, and attach the slack penalty as a min-plus weight. Audit whether a finite or recursively sufficient lower-bound value function exists without reintroducing parity-word enumeration.
