# DSD-AUDIT-20260907-MATH-006 — Collatz 11-bit block-label continuation sieve

Date: 2026-09-07
Domain: Mathematics / Collatz
Primary repository: `dominicus9708/Math-verification`

## Outcome

**Verdict: CONFIRMED finite-exact address-preserving sieve through depth 72.**

For a fixed lower-61-bit start residue, the 340 surviving top-address labels act by an affine permutation on the next 11 parity bits. Exhaustive enumeration over every possible endpoint residue modulo `2^11` gives deterministic, pointwise caps on how many of the 340 labels can maintain coefficient survival through depth 72.

## Setup

Write

\[
N=a2^{61}+x,
\qquad
1024\le a\le1363,
\qquad
0\le x<2^{61}.
\]

For the canonical lower prefix let

\[
q=q_{61}(x),
\qquad
y=T^{61}(x).
\]

Then exactly

\[
T^{61}(N)=y+a3^q.
\]

The next 11 parity bits depend only on this endpoint modulo `2048`.

## Affine-permutation theorem

Because `3^q` is odd,

\[
a\mapsto y+a3^q\pmod{2048}
\]

is a permutation of all 2048 residues when `a` ranges over all 11-bit labels.

Combined with the audited parity-vector residue bijection, every possible 11-bit parity continuation occurs exactly once across all 2048 labels for each fixed lower state.

The current candidate interval selects only labels `1024,...,1363`.

## Exact uniform caps

The least coefficient-surviving odd count at depth 61 is `q61=39`.

For every `q61=39,...,61`, every endpoint residue `y mod2048`, and all 340 actual block labels, the certificate checks coefficient survival at all depths `62,...,72`.

Uniform extrema:

| q61 | min labels surviving | max labels surviving |
|---:|---:|---:|
| 39 | 36 | 47 |
| 40 | 124 | 141 |
| 41 | 221 | 235 |
| 42 | 288 | 303 |
| 43 | 320 | 333 |
| 44 | 336 | 340 |
| 45 | 339 | 340 |
| 46–61 | 340 | 340 |

Therefore, pointwise in the lower endpoint residue,

\[
q_{61}=39
\Longrightarrow
\#\text{ surviving block labels}\le47,
\]

and similarly `141` for `q61=40`, `235` for `q61=41`.

## Eight-axis audit

### D — Describability

PASS.

Lower address `x`, block label `a`, odd count `q`, endpoint residue `y mod2048`, and 11-bit continuation are explicit.

### R — Resolution

PASS.

All 340 actual labels and all 2048 endpoint residues are evaluated exactly. No average replaces the pointwise result.

### S — Selection

PASS.

The 340 labels are exactly those surviving the previously certified first-cell start cap.

### E — Exclusion

PASS AS CONDITIONAL SOURCE-SIDE PRUNING.

For each fixed lower state, block labels that violate coefficient survival before depth 72 are excluded exactly. The cap is conditional on `q61` and does not claim that every block is globally excluded.

### T — Transition / lineage

PASS.

The identity `T^61(a2^61+x)=y+a3^q` keeps the same ordinary start. The final 11 bits are generated from that exact state.

### C — Consistency

PASS.

The result is compatible with the previously audited parity-vector bijection and the universal coefficient-spine condition.

### N — Norm

PASS.

Only necessary minimal-counterexample prefix conditions are imposed.

### O — Outcome

CONFIRMED.

Low-surplus lower-61 states admit strong deterministic block-label reduction; high-surplus states remain open to this particular sieve.

## External-literature status

No new external result is imported in this audit. The parity-vector residue bijection was already classified **A — SAFE EXTERNAL THEOREM** in the Tong Niu 2026 audit.

## Required prohibited upgrades

- do not read the 47/141/235 caps as probabilities;
- do not assume the same labels survive for different endpoint residues;
- do not multiply caps across depths as independent factors;
- do not discard `q61>=46` states;
- do not infer first-cell or Collatz closure.

## Evidence

Certificate commit:

`f208051d6992186507dafe0587bfd3315ae1c69a`

Explanatory note commit:

`5f4f4bc333c57f41522867d2ae83bcdb45bc04bf`

Prior external theorem audit:

`1bafc5d5d2d6b6d91bc523311c9d4768ab0be95f`

## Next audited transition

Compress the lower-61 state sufficiently to combine this exact 340-label transducer with endpoint/Hensel eligibility after depth 72. Any proposed descriptor must preserve enough information to determine the actual continuation rather than only its average distribution.