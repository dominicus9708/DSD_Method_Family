# DSD Audit — Collatz r=16 hybrid ordinary-target union

Date: 2026-09-11

Status: `SAFE EXACT r=16 CLOSURE / r>=16 CLOSED / r<=15 OPEN`

Canonical math note:

- `dominicus9708/Math-verification/collatz/notes/2026-09-11-math069-r16-hybrid-union-closure.md`

## 1. Audit issue

The r=16 branch contains more than 213 million lineage-counted target occurrences.  Treating that number as the future state count would confuse representation multiplicity with ordinary-state multiplicity.

The audit therefore separates two resolutions:

1. pre-completion symbolic lineage, where phase/cost/dyadic information must remain distinct;
2. post-completion ordinary targets, where literal set equality is the relevant future identity.

## 2. Safe projection

The projection

\[
\text{completed negative-candidate macro state}
\to
\text{ordinary target set}
\]

is applied only after MATH-065 has preserved and audited all proof-facing macro information.

From that point onward, the remaining obligation is deterministic descent to the frozen verified floor.

Therefore exact equality merging of ordinary targets is safe.

## 3. Hybrid representation

Large and medium target families remain finite APs while they contain multiple values. Singleton states are represented only by their integer value.

This is not a heuristic optimization. For a singleton,

\[
P(a,b,1)=\{a\},
\]

so the AP step coordinate is no longer future-relevant.

Keeping singleton values out of the AP-grid sort changes computational cost but not the represented ordinary set.

## 4. Exact result

The r=16 workload is partitioned computationally into `m<=64`, `65<=m<=1023`, and `m>=1024`.

All three exact target unions reach `<=2^71`.

Maximum additional shortcut reach depths are respectively

\[
326,\qquad314,\qquad347.
\]

Hence the complete r=16 layer is closed.

Combined with prior results:

\[
\boxed{r\ge16\text{ is closed in the current first-cell calculation}.}
\]

## 5. Claim hierarchy

### SAFE

- exact symbolic lineage until macro completion;
- exact ordinary-set projection after completion;
- same-grid AP interval union;
- singleton integer-equality merge;
- hybrid representation by multiplicity for computational efficiency;
- r=16 closure;
- combined r>=16 closure.

### OPEN

- `2<=r<=15`;
- one-paid / remaining multi-paid interaction;
- first universal Farey cell;
- later cells;
- Collatz conjecture.

### PROHIBITED

- do not infer that multiplicity bands are mathematically distinct dynamical classes;
- do not use post-completion equality merging on unresolved symbolic states;
- do not promote r>=16 closure to first-cell or global Collatz closure.
