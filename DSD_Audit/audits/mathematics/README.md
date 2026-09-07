# Mathematics audit index / 수학 감사 인덱스

이 디렉터리는 DSD Audit의 수학 분야 감사 기록을 보존합니다. 개별 파일은 역사 판정과 근거를 보존하고, 이 README는 **현재 탐색용 인덱스**입니다.

## Current Collatz status

- **Collatz conjecture:** `OPEN`
- **First universal Farey cell:** `OPEN`
- **Proof architecture:** `PARTIALLY_CONFIRMED`
- **Current start window:**

\[
2^{71}<N<\frac{1364}{1024}2^{71}
\]

- **Current top-address labels:** `340` (`1024..1363`)
- **MATH-008:** lower-61 phase reachability refinement is saturated.
- **MATH-009:** root-Hensel correction ordering and endpoint/minimum-start ordering are one affine ordering inside a fixed `(k,q,E)` fiber; no independent pruning credit.
- **MATH-010:** DSD descriptors/stage gates were inserted into the exact 61+11 computation; a concrete double-address-lift representation error was blocked, while MATH-006 arithmetic was reproduced unchanged.
- **MATH-011:** the depth-72 coefficient-survival predicate was compressed to the complete finite threshold descriptor `H(r)`, and the 340-address scan was converted exactly to a cyclic sliding window. The address-predicate evaluation layer drops from `16,015,360` lookups to `47,104` threshold evaluations across `q61=39..61`.
- **Current frontier:** seek an analogous complete descriptor for depth-72+ same-integer continuation/Hensel eligibility, keeping only descriptors that yield safe pruning, safe merging, or fewer exact state expansions.

## Canonical Collatz audit sequence

| Audit ID | Record | Outcome / role |
|---|---|---|
| `DSD-AUDIT-20260907-MATH-001` | [`2026-09-07_collatz-proof-architecture-full-audit.md`](2026-09-07_collatz-proof-architecture-full-audit.md) | Full proof-architecture audit; global result `PARTIALLY_CONFIRMED`, Collatz remains `OPEN` |
| `DSD-AUDIT-20260907-MATH-002` | [`2026-09-07_collatz-external-literature-citation-audit.md`](2026-09-07_collatz-external-literature-citation-audit.md) | Claim-level external literature audit and `A/B/C/D/FINITE ONLY` citation policy |
| `DSD-AUDIT-20260907-MATH-003` | [`2026-09-07_collatz-denjoy-koksma-first-cell-audit.md`](2026-09-07_collatz-denjoy-koksma-first-cell-audit.md) | Denjoy–Koksma/Ostrowski input; first-cell top-address count `341 → 340`; scalar-only frontier fixed |
| `DSD-AUDIT-20260907-MATH-004` | [`2026-09-07_collatz-first-cell-endpoint-q-lock-audit.md`](2026-09-07_collatz-first-cell-endpoint-q-lock-audit.md) | Endpoint q-lock/address-faithful Hensel interpretation |
| `DSD-AUDIT-20260907-MATH-005` | [`2026-09-07_collatz-340block-endpoint-halo-audit.md`](2026-09-07_collatz-340block-endpoint-halo-audit.md) | Same-endpoint coupling localized to adjacent-block halos |
| `DSD-AUDIT-20260907-MATH-006` | [`2026-09-07_collatz-block-label-11bit-transducer-audit.md`](2026-09-07_collatz-block-label-11bit-transducer-audit.md) | Exact 61+11 block-label transducer; low-surplus pointwise label caps |
| `DSD-AUDIT-20260907-MATH-007` | [`2026-09-07_collatz-block-label-right-congruence-audit.md`](2026-09-07_collatz-block-label-right-congruence-audit.md) | Exact right-congruence barrier; low-surplus masks retain full endpoint-phase distinction |
| `DSD-AUDIT-20260908-MATH-008` | [`2026-09-08_collatz-lower61-endpoint-phase-reachability-audit.md`](2026-09-08_collatz-lower61-endpoint-phase-reachability-audit.md) | All 2048 phases occur for `q61=39..58`; phase-sparsity refinement is `STRATEGY SATURATION` |
| `DSD-AUDIT-20260908-MATH-009` | [`2026-09-08_collatz-root-hensel-endpoint-ordering-redundancy-audit.md`](2026-09-08_collatz-root-hensel-endpoint-ordering-redundancy-audit.md) | Same-fiber correction ordering and minimum-start ordering are algebraically identical; `REDUNDANT / NO NEW PRUNING` |
| `DSD-AUDIT-20260908-MATH-010` | [`2026-09-08_collatz-dsd-native-61plus11-computation-audit.md`](2026-09-08_collatz-dsd-native-61plus11-computation-audit.md) | DSD-native stage/resolution/exclusion/margin state added; double address lift rejected; exact MATH-006 regression retained |
| `DSD-AUDIT-20260908-MATH-011` | [`2026-09-08_collatz-dsd-complete-descriptor-cyclic-window-acceleration-audit.md`](2026-09-08_collatz-dsd-complete-descriptor-cyclic-window-acceleration-audit.md) | Complete tail threshold descriptor `H(r)` + exact inverse-multiplier cyclic-window transform; `CONFIRMED WITHIN SCOPE / COMPUTATIONAL ACCELERATION` |

## Reading order

1. `MATH-001` — global dependency/status map.
2. `MATH-002` — legal external inputs.
3. `MATH-003` — 340-block first-cell start window.
4. `MATH-004` — same-endpoint ordinary-integer lineage.
5. `MATH-005` — adjacent-block locality.
6. `MATH-006` — exact 61+11 transducer.
7. `MATH-007` — phase right-congruence barrier.
8. `MATH-008` — actual phase reachability saturation.
9. `MATH-009` — Hensel/endpoint ordering redundancy.
10. `MATH-010` — DSD-native computation state and transition gate.
11. `MATH-011` — DSD complete descriptor used for exact calculation acceleration.

## Current finite boundary

The exact reachable-phase cardinalities remain

\[
\#\operatorname{Reach}_{61}(q)=
\begin{cases}
2048,&39\le q\le58,\\
1166,&q=59,\\
58,&q=60,\\
1,&q=61.
\end{cases}
\]

MATH-010 does not change those values or the MATH-006 survivor caps. It changes the **calculation semantics**: `BASE_ENDPOINT` and `ADDRESS_LIFTED` are different stages, and the affine address lift may be applied exactly once.

For `q61=39`, MATH-010 additionally records the exact 2048-residue first-failure profile:

- depth62: 1024;
- depth64: 256;
- depth65: 256;
- depth67: 96;
- depth69: 56;
- depth70: 76;
- depth72: 37;
- survive through72: 247.

All 247 survivors attain minimum coefficient margin `0` within depths62..72. This is a finite exact diagnostic, not a density statement.

## DSD-native computation rule introduced by MATH-010

Exact arithmetic remains primary. DSD metadata is carried alongside it:

\[
\mathcal A=(D,R,S,E,T,C,N,O).
\]

The key transition gate is

\[
\texttt{BASE\_ENDPOINT}\to\texttt{ADDRESS\_LIFTED}
\]

exactly once. Reapplying the address contribution to an already lifted phase is a prohibited transition.

## DSD computational compression introduced by MATH-011

For each lifted residue `r mod 2048`, let `s_j(r)` be the tail odd-count through `j` steps and define

\[
H(r)=\max_{1\le j\le11}\bigl(q_{\min}(61+j)-s_j(r)\bigr).
\]

Then

\[
r\text{ survives through depth }72\iff q_{61}\ge H(r).
\]

So `H(r)` is complete for this finite predicate. Its exact distribution is

`39:247, 40:554, 41:570, 42:406, 43:195, 44:63, 45:12, 46:1`.

For fixed `q`, the invertible multiplier `m=3^q mod2048` gives the coordinate change `z=m^{-1}y`, turning

\[
\sum_{a=1024}^{1363}\mathbf1[H(y+am)\le q]
\]

into a cyclic contiguous length-340 window. Full legacy count vectors are reproduced exactly.

This is a computational acceleration, not a stronger Collatz theorem.

## Audit discipline

### SAFE does not mean global proof

A `CONFIRMED` local audit applies only to its locked scope.

### Computation does not become a theorem by scale

\[
\text{finite computation}\not\Rightarrow\text{universal theorem}.
\]

### Measure/density language is not emptiness

\[
\text{almost all}\not\Rightarrow\text{all},
\qquad
\mu(S)=0\not\Rightarrow S=\varnothing.
\]

### Preserve ordinary-integer lineage and representation stage

A residue, quotient state, endpoint class, or symbolic path may be used only when the bridge back to the same ordinary integer is explicit at the required resolution. A derived/address-lifted representation cannot silently be reused as though it were the original base representation.

### Redundant information is not new evidence

The same exact affine relation expressed in different coordinates cannot be counted twice as independent pruning.

### A complete descriptor is scope-bound

A descriptor complete for one finite predicate may be used to accelerate exactly that predicate. It cannot be promoted to arbitrary-depth completeness without a new proof.

### Saturated route is not a false theorem

A refinement that adds no exclusion is recorded as `STRATEGY SATURATION` or `NO NEW PRUNING`; valid upstream results remain valid.

## External literature citation classes

- `A` — positive prior art
- `B` — conditional prior art
- `C` — partial absorption
- `D` — audited anti-pattern / negative methodological prior art
- `FINITE ONLY` — finite evidence only

## Revision policy

- Do not silently erase older reasonable verdicts.
- Revise scope explicitly or add linked migration records.
- Preserve old commits and paths for traceability.
- Use this README to identify the current sequence rather than moving historical files merely for appearance.

## Related repository

Current calculation/proof index:

`dominicus9708/Math-verification/collatz/README.md`
