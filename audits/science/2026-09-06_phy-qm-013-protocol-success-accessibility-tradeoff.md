# PHY-QM-013 — Protocol success probability and accessibility tradeoff

Date: 2026-09-06
Status: CONDITIONAL_EXACT_WITHIN_SUPPLIED_QUANTUM_CONSTRUCTION

## Setup
For the hidden-steering family constructed by applying the POVM-extension lemma twice to the d-dimensional Werner seed with alpha=(d-1)/d, the normalized pre-filter state carries the two extension normalizations (d+1)^{-2}. Project both parties onto the qubit subspace spanned by |0>,|1>.

The projected trace of the Werner seed is

Tr[(F_A\otimes F_B) rho_Wtilde (F_A\otimes F_B)]
= 2/d^2 + 4/d^3
= 2(d+2)/d^3.

Hence the bilateral success probability is

P_AB(d) = 2(d+2) / [ d^3 (d+1)^2 ].

The normalized successful branch has Werner visibility

p_d = d/(d+2).

## Numerical controls
| d | filtered visibility p_d | bilateral success P_AB |
|---:|---:|---:|
| 3 | 0.600000 | 0.02314814815 |
| 4 | 0.666667 | 0.00750000000 |
| 5 | 0.714286 | 0.00311111111 |
| 6 | 0.750000 | 0.00151171580 |
| 7 | 0.777778 | 0.00081997085 |

As d grows,

p_d -> 1,

while

P_AB(d) ~ 2/d^4 -> 0.

## DSD consequence
A conditioned branch may exhibit a stronger witness while becoming less frequently accessible. Therefore the following are distinct downstream descriptors:

- existence of a successful protocol branch;
- property value on that conditioned branch;
- success probability / accessibility weight of that branch;
- unconditional readout before conditioning.

A single Boolean `accessible / inaccessible` label would erase this difference. In probabilistic physical specializations, branch probability should therefore remain explicit supplied downstream data rather than be inferred from property applicability alone.

## Boundary
The probability formula is not a DSD law. It is derived from the supplied quantum state, Born trace rule, and the specific local-filter construction. The methodological lesson is the separation between branch existence and branch accessibility weight.

## Reproducibility
The values are produced by:

`audits/science/2026-09-06_hidden_steering_protocol_depth.py`
