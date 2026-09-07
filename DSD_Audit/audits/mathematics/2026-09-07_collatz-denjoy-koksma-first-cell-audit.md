# DSD Audit — Collatz Denjoy–Koksma/Ostrowski first-cell reduction

Audit ID: `DSD-AUDIT-20260907-MATH-003`

Date: 2026-09-07

Outcome: **PARTIALLY_CONFIRMED / SAFE POSITIVE REDUCTION.**

Scope: audit the import of the classical Denjoy–Koksma/Ostrowski rotation-sum theorem into the current first universal Collatz cell and audit the resulting start-window reduction from 341 to 340 top-11-bit address blocks.

This audit does not claim the Collatz conjecture is proved.

---

## 1. Audit frame

Use the standard DSD audit tuple

\[
\mathcal A=(D,R,S,E,T,C,N,O).
\]

### D — describability

Objects are explicitly separated:

- irrational rotation angle `theta=log_2(3/2)`;
- BV observable `f(x)=2^{-fractional_part(x)}`;
- convergent denominators of `theta`;
- Ostrowski digits of the first-cell odd count `q0`;
- mechanical correction `S_*`;
- ordinary start `N` and its dyadic address block.

Status: **CONFIRMED.**

### R — resolution

The imported theorem acts on the scalar rotation sum only. The same-integer dyadic address is retained as a separate higher-resolution channel and is not averaged away.

Status: **CONFIRMED.**

### S — selection

External results are selected at theorem level:

1. Denjoy–Koksma at continued-fraction denominators;
2. arbitrary-time decomposition by Ostrowski digits.

No unrelated probabilistic or metric conclusion is imported.

Status: **CONFIRMED.**

### E — exclusion

The exclusion `N >= (1364/1024)B0` is justified by a universal scalar correction upper bound. The next block `1363` is explicitly **not** excluded because the mechanical lower bound shows scalar capacity remains sufficient there.

Status: **CONFIRMED.**

### T — transition

The critical bridge is

\[
\text{Denjoy–Koksma at }q_i
+\text{Ostrowski block decomposition}
\Longrightarrow
\left|S_N-N\int f\right|
\le \operatorname{Var}(f)\sum b_i.
\]

The translation of each `q_i` block is allowed because Denjoy–Koksma is uniform in the phase. Triangle inequality then gives the stated arbitrary-time bound.

For the actual first-cell odd count,

\[
q_0=q_{22}+q_{21},
\]

so `sum b_i=2`.

Status: **CONFIRMED.**

### C — consistency

The result is consistent with the previous 1024-block cap: it is strictly sharper and closes only the former top block `a=1364`. It does not contradict the earlier correction-only barrier; instead it sharpens that barrier to show the scalar route saturates at block `1363`.

Status: **CONFIRMED.**

### N — norm

Ordinary mathematical proof remains the norm. DSD classification does not replace the external theorem or exact arithmetic certificate.

Status: **CONFIRMED.**

### O — outcome

Positive reduction:

\[
2^{71}<N<\frac{1364}{1024}2^{71}=1364\cdot2^{61}.
\]

Remaining address blocks:

\[
1024,\ldots,1363,
\]

exactly `340`.

Scalar-route barrier:

\[
S_*>
\varepsilon\frac{1363}{1024}B_0.
\]

Therefore further elimination requires same-integer coupling.

Outcome: **PARTIALLY_CONFIRMED / SAFE REDUCTION; GLOBAL PROOF OPEN.**

---

## 2. External literature classification

The imported Denjoy–Koksma/Ostrowski claim is classified

\[
\boxed{A\text{ — POSITIVE PRIOR ART}.}
\]

Permitted use:

- deterministic bounded-variation rotation-sum discrepancy;
- exact arbitrary-time bound via Ostrowski digits.

Prohibited upgrades:

- rotation discrepancy -> parity independence;
- scalar correction capacity -> same-integer existence;
- one-cell start reduction -> Collatz proof.

---

## 3. Exact arithmetic evidence

The linked Math-verification certificate verifies with rational logarithm intervals:

1. the needed continued-fraction cylinder for `theta`;
2. denominators
   `q21=6586818670`,
   `q22=65470613321`,
   `q23=137528045312`;
3. `q0=q22+q21`;
4. normalized correction discrepancy at most `2/3`;
5. the strict cap at `1364/1024`;
6. the strict scalar lower barrier at `1363/1024`.

Evidence status: **ESTABLISHED_WITHIN_SCOPE.**

---

## 4. Regression rules added

### DK-R1 — keep phase-uniformity explicit

A translated Ostrowski block may use Denjoy–Koksma only because the bound is uniform in the starting phase.

### DK-R2 — compute actual digit sum

Do not substitute a generic `O(log N)` or `sum a_i` estimate when the exact Ostrowski digit sum is available. Here it is exactly `2`.

### DK-R3 — scalar route stops at its certified barrier

Once an explicit admissible word has scalar correction above a block threshold, a word-independent maximum-correction argument cannot exclude that whole block.

### DK-R4 — preserve same-integer address

Any next compression must preserve the exact ordinary start at depth 72 and may not identify states solely because their scalar correction bounds agree.

---

## 5. Final verdict

\[
\boxed{
\text{Denjoy–Koksma/Ostrowski import: CONFIRMED.}
}
\]

\[
\boxed{
\text{341 -> 340 first-cell address blocks: CONFIRMED.}
}
\]

\[
\boxed{
\text{correction-only elimination below block 1363: INSUFFICIENT BASIS / PROHIBITED WITHOUT SAME-INTEGER DATA.}
}
\]

The next open transition is the address-faithful coupling of the 340 surviving ordinary starts to root-Hensel maximality through depth 195 and terminal first-crossing correction.
