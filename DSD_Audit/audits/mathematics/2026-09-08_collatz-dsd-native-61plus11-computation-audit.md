# DSD-AUDIT-20260908-MATH-010

## Subject

Pilot integration of DSD descriptors and transition gates directly into the exact Collatz 61+11 address-transducer calculation.

## Verdict

`CONFIRMED WITHIN FINITE 61+11 SCOPE / REPRESENTATION ERROR BLOCKED / NO NEW GLOBAL PRUNING`

Collatz conjecture: `OPEN`.

## Locked arithmetic

For

\[
N=a2^{61}+x,
\qquad y=T^{61}(x),
\qquad q=q_{61}(x),
\]

we have

\[
T^{61}(N)=y+a3^q.
\]

Thus the 11-bit tail phase is

\[
r=(y+a3^q)\bmod 2048.
\]

MATH-006 already evaluates this affine address lift internally.

## Representation issue detected

A proposed follow-up refinement treated `y+a3^q` as if it could be supplied to the existing MATH-006 predicate as another base endpoint phase. That would apply the same address contribution a second time.

The DSD-native implementation therefore introduces two explicit representation stages:

1. `BASE_ENDPOINT` — `y mod 2048`;
2. `ADDRESS_LIFTED` — `(y+a3^q) mod 2048`.

The transition

\[
\texttt{ADDRESS\_LIFTED}\to\texttt{ADDRESS\_LIFTED}
\]

by another address lift is prohibited and tested as a negative control.

## Audit tuple

\[
\mathcal A=(D,R,S,E,T,C,N,O).
\]

### D — Describability

Each finite tail state explicitly carries `q61`, lifted phase, first failure depth, minimum coefficient margin and survival outcome.

### R — Resolution

The scope is exactly 61 root parity bits followed by 11 tail parity bits, with modulus `2^11=2048` and block labels `1024..1363`.

No statement beyond depth 72 is imported from this finite transducer.

### S — Selection

A tail remains selected iff its cumulative odd count satisfies the coefficient-survival threshold at every depth 62..72.

### E — Exclusion

The first depth where the integer coefficient margin becomes negative is stored as `first_fail_depth`. Exclusion therefore carries an explicit local cause rather than only a Boolean result.

### T — Transition

The only permitted address transition is

\[
y\mapsto y+a3^q\pmod{2048}
\]

from `BASE_ENDPOINT` to `ADDRESS_LIFTED` exactly once.

The negative control confirms that a second application is rejected.

### C — Consistency

The DSD-native implementation reproduces the MATH-006 exact min/max survivor counts:

- q61=39: 36..47;
- q61=40: 124..141;
- q61=41: 221..235;
- q61=42: 288..303;
- q61=43: 320..333;
- q61=44: 336..340;
- q61=45: 339..340;
- q61=46..61: 340..340.

Thus the new descriptor layer changes representation safety and diagnostics, not the established exact arithmetic.

### N — Norm

The residue tables and regressions are exact finite statements within the locked 61+11 scope. They are not upgraded to a universal Collatz theorem.

### O — Outcome

1. the attempted additional affine-coupling filter is identified as semantically redundant with MATH-006 because MATH-006 already contains the address lift;
2. DSD stage tracking blocks the concrete double-lift representation error;
3. exact first-failure and minimum-margin diagnostics are now retained by the calculation;
4. no new global pruning is credited.

## Diagnostic example: q61=39

Among all 2048 lifted residues:

- first fail at 62: 1024;
- 64: 256;
- 65: 256;
- 67: 96;
- 69: 56;
- 70: 76;
- 72: 37;
- survive through 72: 247.

Every surviving q61=39 residue has minimum coefficient margin 0 over depths 62..72.

This is an exact finite structural profile, not a probability or density claim.

## Prohibited upgrades

\[
\text{DSD-native gate catches a representation error}
\not\Rightarrow
\text{DSD proves Collatz}.
\]

\[
\text{finite exact margin profile}
\not\Rightarrow
\text{universal tail exclusion}.
\]

\[
\text{no new pruning in MATH-010}
\not\Rightarrow
\text{MATH-006 is invalid}.
\]

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_dsd_native_61plus11_computation_certificate.py`

Math-verification note:

`collatz/notes/2026-09-08-dsd-native-61plus11-computation-pilot.md`
