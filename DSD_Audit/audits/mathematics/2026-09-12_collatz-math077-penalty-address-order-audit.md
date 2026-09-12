# DSD Audit — Collatz MATH-077 first-crossing penalty/address order

Date: 2026-09-12

Status: `PASS WITH FINITE-SCOPE BOUNDARY`

## Audited object

At a fixed first coefficient-crossing layer, let `m` be the mechanical/Beatty maximum-correction reference and `w` any other crossing word. Define

\[
\mathcal P=S_m-S_w\ge0,
\qquad
\Delta r=r_w-r_m.
\]

The exact common-coordinate residual is

\[
\boxed{
\rho(y_m-y_w)=\mathcal P-\Delta r.
}
\]

## DSD channel interpretation

This equation separates and reconnects:

1. **analytic/correction channel** — `P`, the normalized correction deficit from the extremal mechanical envelope;
2. **dyadic address channel** — `Delta r`, the exact canonical source-address displacement;
3. **endpoint channel** — the scaled endpoint difference.

The result is important because the earlier mechanical-envelope theorem explicitly warned that remainder dominance alone cannot replace address information. MATH-077 does not remove that warning; it turns it into an exact balance equation.

## Finite exact regression

Through depth 26, including the two trivial first crossings at depths 1 and 2, the certificate checks 190069 crossing candidates.

Results:

- mechanical maximum uniqueness failures: 0;
- residual identity failures: 0;
- endpoint/address sign-order failures: 0;
- nontrivial equal endpoints with the mechanical reference: 0.

Thus the finite data satisfy

\[
\operatorname{sgn}(y_w-y_m)=\operatorname{sgn}(r_w-r_m).
\]

For `Delta r>0`, the nontrivial equivalent inequality is

\[
\mathcal P<\Delta r.
\]

For `Delta r<0`, endpoint ordering follows automatically from `P>=0`.

## Safe claims

- `P=S_m-S_w` in the fixed first-crossing layer is the exact normalized-correction deficit.
- `rho(y_m-y_w)=P-Delta r` is an exact identity.
- Address order and endpoint order agree for all audited first-crossing candidates through depth 26.
- The result supplies a concrete coupling between the mechanical envelope and exact dyadic address.

## Prohibited upgrades

- depth-26 sign order => arbitrary-depth sign order;
- `P<Delta r` for audited positive displacements => a global address-dominance theorem;
- mechanical maximum remainder => automatic elimination of all nonmechanical words without the address term;
- MATH-077 => first-cell closure, `2<=r<=13` closure, or Collatz.

## Relation to MATH-076

MATH-076 gives

\[
\Gamma_d-A_d=\rho_L\Delta y.
\]

MATH-077 is its same-`q` mechanical-reference specialization. This strengthens the common-state program by showing that the penalty and address terms enter with opposite signs in the actual endpoint residual.

## Verdict

`PASS WITH FINITE-SCOPE BOUNDARY`.

The most valuable next theorem target is a structural lower bound for positive address displacement,

\[
\Delta r-\mathcal P>0,
\]

or a residue-refined version sufficient to propagate its sign without enumerating all crossing words.
