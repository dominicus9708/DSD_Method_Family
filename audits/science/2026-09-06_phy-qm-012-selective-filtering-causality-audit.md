# PHY-QM-012 — Selective filtering and causal-support audit

Date: 2026-09-06
Status: PASS_WITH_BOUNDARY

## Question
Does hidden steering or conditional remote-state change imply superluminal signalling or a violation of the DSD information-propagation bound?

## Local instrument control
Let F be the local success filter and G the complementary failure operator, with

F^\dagger F + G^\dagger G = I.

If Alice applies the complete local instrument and the outcome is ignored, Bob's reduced state is

rho_B' = Tr_A[(F\otimes I)rho(F^\dagger\otimes I) + (G\otimes I)rho(G^\dagger\otimes I)] = rho_B.

The accompanying script verifies this identity numerically for the explicit hidden-steering family to machine precision.

If one conditions on Alice's success branch, Bob's conditional state can differ from rho_B. This is not an operational faster-than-light signal: the distinction between the unconditional ensemble and the selected subensemble requires the local outcome/conditioning record.

## DSD separation
The following must remain distinct:

UNCONDITIONAL_LOCAL_READOUT
CONDITIONED_BRANCH_READOUT
PROTOCOL_SUCCESS_RECORD
CLASSICAL_OUTCOME_ACCESS
DYNAMIC_DISTINGUISHABILITY_PROPAGATION

The DSD quantity c_info belongs to the last item only after localization, metric time, discrepancy/evolution data, and a support-faithful dynamical representation have been supplied. A static conditional assemblage or postselected steering witness does not by itself define propagation speed.

## Consequence
Hidden steering therefore supplies a useful counterexample to the implication

conditional remote-state change -> superluminal information propagation.

The valid relation is weaker:

local stochastic operation + branch conditioning -> different conditional descriptive state,

while

complete local instrument + ignored outcome -> unchanged remote marginal.

## Verdict
- hidden steering implies FTL signalling: REJECTED.
- selective and nonselective readouts can be merged: REJECTED.
- conditioning record must be retained when the analysis uses a selected branch: CONFIRMED.
- static steering data determine c_info: REJECTED.

## Reproducibility
The numerical remote-marginal control is included in:

`audits/science/2026-09-06_hidden_steering_protocol_depth.py`
