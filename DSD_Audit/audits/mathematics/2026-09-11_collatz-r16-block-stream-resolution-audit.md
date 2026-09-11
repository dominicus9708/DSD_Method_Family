# DSD Audit — Collatz MATH-069 r=16 block/stream closure

Date: 2026-09-11

Verdict: `SAFE WITHIN THE FIRST-CELL r=16 LAYER / NO GLOBAL COLLATZ UPGRADE`

## Audited distinction

The MATH-069 pipeline keeps four statements separate:

1. **cylinder resolution** — a parity/phase family becomes a smaller exact arithmetic progression;
2. **singleton handoff** — an exact family contains one ordinary state;
3. **ordinary-state closure** — that state is actually continued to `<=2^71`;
4. **paid-count layer closure** — every negative-candidate cylinder in the complete `r=16` partition has passed one of the valid closure routes.

No implication from 1 or 2 directly to 3 is permitted.

## Exact information channels retained

The audit retains, until a valid handoff removes the need for them:

- source dyadic lineage;
- exact affine endpoint family;
- source phase cell;
- paid-count/slack reduced-cost bound;
- arithmetic-progression coefficient and multiplicity;
- ordinary integer value after singleton resolution.

The 8-step block is information-preserving because `n mod 256` fixes the next eight shortcut parity bits exactly.  For an odd-step AP, `k mod 256` and `n mod 256` correspond bijectively, so residue slicing is exact rather than statistical.

## Streaming handoff

MATH-069 deliberately does not deduplicate the 11,766,228 singleton occurrences before terminal continuation.

This is safe: duplicates can increase work but cannot remove a candidate.  Each emitted integer is independently processed by a deterministic exact transition.  The constant-memory implementation therefore changes computational resource use without weakening the quantified domain.

The terminal verifier also checks exact intermediate-step thresholds inside every 8-step block.  Hence a descent to the frozen floor cannot be hidden by continuing to the end of a block.

## Supported conclusion

The complete `r=16` negative-candidate layer is closed for the current first-universal-cell minimal-counterexample calculation.

Together with the prior paid-count certificates, the currently supported frontier is

\[
 r\ge16\text{ closed},\qquad 2\le r\le15\text{ open}.
\]

## Prohibited upgrades

Do not infer any of the following:

- `r>=16` closure implies every multi-paid cluster is closed;
- first-cell paid-count pruning implies first-cell emptiness;
- finite target continuation implies a universal Collatz descent theorem;
- a constant-memory stream is an asymptotic/density argument.

## Next audit target

Apply the same claim hierarchy to `r=15`.  In particular, any resolution gate that reduces a family to one ordinary integer must retain the explicit final ordinary-continuation obligation.
