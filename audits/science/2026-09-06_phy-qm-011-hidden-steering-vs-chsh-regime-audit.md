# PHY-QM-011 — Hidden steering vs CHSH regime audit

Date: 2026-09-06
Status: PASS_WITH_BOUNDARY

## Filtered family
The hidden-steering filter branch is the two-qubit Werner family

rho_F(d) = p_d |psi-><psi-| + (1-p_d) I_4/4,

p_d = d/(d+2), d>=3.

## Exact controls
For a two-qubit Werner state:

- projective-measurement steering occurs for p>1/2;
- the minimum eigenvalue of the partial transpose is (1-3p)/4;
- the maximal CHSH value is 2 sqrt(2) p.

Substituting p_d gives

lambda_min(PT) = -(d-1)/(2(d+2)) < 0,

so every filtered branch is entangled.

The CHSH threshold is

d/(d+2) > 1/sqrt(2),

which first holds at integer d=5.

## Regimes
| d | p_d | CHSH_max | interpretation |
|---:|---:|---:|---|
| 3 | 0.600000 | 1.697056 | steerable, CHSH-nonviolating |
| 4 | 0.666667 | 1.885618 | steerable, CHSH-nonviolating |
| 5 | 0.714286 | 2.020305 | steerable, CHSH-violating |
| 6 | 0.750000 | 2.121320 | steerable, CHSH-violating |

Therefore hidden steering is not merely a disguised CHSH violation. For d=3 and d=4, the sequential protocol reveals steering while the postselected two-qubit state still does not violate CHSH.

## DSD consequence
Three diagnostics remain distinct:

1. single-round LHS completion of the initial state;
2. sequentially accessible steering after a local filter;
3. CHSH violation of the filtered branch.

Thus `hidden steering`, `Bell witness violation`, and `protocol accessibility` are separate typed properties.

## Boundary
CHSH-nonviolating is not claimed to mean Bell-local under every possible Bell inequality or protocol. The calculation only establishes absence/presence of CHSH violation for this filtered Werner family.
