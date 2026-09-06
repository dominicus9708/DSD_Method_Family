# PHY-QM-010 — Hidden steering and protocol depth audit

Date: 2026-09-06
Status: PASS_WITH_BOUNDARY

## Question
Can a state that is unsteerable for every single-round POVM become steerable when a sequential local protocol is allowed, and what does this imply for DSD describability?

## External quantum bridge
Use Quintino et al., Phys. Rev. A 92, 032107 (2015), arXiv:1501.03332. Their hidden-steering construction begins with a d-dimensional Werner state at alpha=(d-1)/d, applies the POVM-extension lemma on both parties, and obtains a state rho_HS that admits an LHS model for arbitrary non-sequential POVMs in both directions. Local qubit-subspace filters on both parties yield

rho_F = [1/(1+2/d)] [ |psi-><psi-| + (2/d) I_4/4 ].

Thus the post-filtered branch is an ordinary two-qubit Werner state with visibility

p_d = d/(d+2).

For every integer d>=3, p_d>1/2, so the filtered branch is steerable in both directions for projective measurements.

## DSD separation
The same initial state therefore has different model-completability status under two protocol classes:

P1 = {single-round POVMs}
P2 = {local filter -> conditioned successful branch -> steering measurement}

with P1 strictly contained in P2, and

LHS-completable(rho_HS; P1) = true,
LHS-completable(rho_HS; P2) = false.

Hence

state + measurement class

is not sufficient for the operational steering question. The allowed operation history/protocol class is an independent typed input.

## Protocol-indexed profile
A safe downstream specialization is

STEERING_ACCESS(state, untrusted_party, trusted_party, measurement_class, protocol_class, conditioning_rule).

This is not a new Property-core axiom. The current Property Axiom System already permits auxiliary sorts and ordered typed profiles; protocol data should therefore enter as an explicit downstream auxiliary input rather than be hidden in the property name.

## Model-class monotonicity
For protocol classes P1 subseteq P2, define C_LHS(P) as the states whose behaviors remain LHS-completable for every protocol in P. Then purely set-theoretically

C_LHS(P2) subseteq C_LHS(P1).

Enlarging the allowed protocol class can preserve or destroy a classical completion guarantee, but cannot create a stronger universal LHS guarantee.

## Verdict
- hidden steering = creation of entanglement by filtering: REJECTED.
- single-round unsteerability = sequential unsteerability: REJECTED.
- protocol class is relevant to operational describability: CONFIRMED.
- Property core must be rewritten to include quantum protocol depth: REJECTED.
- protocol/history should be an explicit downstream typed coordinate: CONFIRMED.

## Reproducibility
`audits/science/2026-09-06_hidden_steering_protocol_depth.py`

Run from repository root:

```bash
python audits/science/2026-09-06_hidden_steering_protocol_depth.py --d-min 3 --d-max 8
```
