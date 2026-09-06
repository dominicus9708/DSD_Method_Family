# PHY-QM-004 — Werner-state entanglement, CHSH, and local-reconstruction separation

Date: 2026-09-06
Status: PASS_WITH_BOUNDARY

## 1. External quantum specialization

Use the standard two-qubit Werner family

```text
rho_W(p) = p |Psi^-><Psi^-| + (1-p) I_4/4,
0 <= p <= 1.
```

Hilbert tensor product, density operators, partial transpose/PPT criterion, and the Horodecki CHSH criterion are external quantum-theory inputs. DSD does not derive them.

## 2. Entanglement threshold

The partial transpose of the singlet projector has eigenvalues

```text
{1/2,1/2,1/2,-1/2}.
```

Hence the partial-transpose eigenvalues of rho_W(p) are

```text
(1+p)/4  [multiplicity 3]
(1-3p)/4 [multiplicity 1].
```

For two qubits, PPT is necessary and sufficient for separability, so the Werner family is entangled exactly when

```text
p > 1/3.
```

## 3. Optimal CHSH threshold

The two-qubit correlation tensor of rho_W(p) is

```text
T = -p I_3.
```

The Horodecki criterion therefore gives

```text
S_max(p) = 2 sqrt(2) p.
```

The standard CHSH inequality is violated exactly when

```text
p > 1/sqrt(2) ~= 0.7071067811865475.
```

Thus there is an explicit interval

```text
1/3 < p <= 1/sqrt(2)
```

in which the state is entangled but does not violate CHSH even under optimal CHSH settings.

This is a direct counterexample to the identification

```text
ENTANGLED == CHSH_NONLOCAL.
```

## 4. Numerical control points

```text
p          min eig(PT)      entangled   S_max       CHSH violation
0.000000   +0.250000        no           0.000000    no
0.333333    0               boundary     0.942809    no
0.400000   -0.050000        yes          1.131371    no
0.500000   -0.125000        yes          1.414214    no
0.600000   -0.200000        yes          1.697056    no
0.707107   -0.280330        yes          2.000000    boundary
0.800000   -0.350000        yes          2.262742    yes
1.000000   -0.500000        yes          2.828427    yes
```

## 5. Local marginal reconstruction failure

For every p,

```text
rho_A = Tr_B rho_W(p) = I_2/2,
rho_B = Tr_A rho_W(p) = I_2/2.
```

Therefore complete tomography of each subsystem separately does not determine p and cannot reconstruct the global Werner state.

Using the Pauli expansion of an arbitrary two-qubit state,

```text
rho = 1/4 [I⊗I + r_i sigma_i⊗I + s_j I⊗sigma_j + T_ij sigma_i⊗sigma_j],
```

the trace-one Hermitian two-qubit state space has 15 real coordinates:

```text
r : 3
s : 3
T : 9.
```

The local-marginal readout keeps only r and s, so its linear kernel on the traceless-Hermitian direction space contains the full 9-dimensional correlation tensor sector.

Thus

```text
local complete subsystem readout != global state reconstruction.
```

## 6. Reconstruction failure is not entanglement

Consider the separable classically correlated state

```text
rho_CC = 1/2 (|00><00| + |11><11|).
```

Its partial transpose is positive, with eigenvalues

```text
{0,0,1/2,1/2},
```

so it is separable. Yet

```text
Tr_B rho_CC = Tr_A rho_CC = I_2/2,
```

exactly the same local marginals as every Werner state.

Therefore

```text
LOCAL_UNRECONSTRUCTIBILITY != ENTANGLEMENT.
```

Local reconstruction failure can arise from ordinary classical correlation as well as quantum entanglement.

## 7. Three distinct DSD ledgers

This witness requires at least three separate diagnostics:

```text
GLOBAL_SEPARABILITY
  Can the supplied bipartite quantum state be written as a convex mixture of product states?

BELL_CHSH_NONLOCALITY
  Does the state, with optimal dichotomic measurements, violate the CHSH local bound?

LOCAL_TO_GLOBAL_RECONSTRUCTIBILITY
  Do the supplied local readouts uniquely determine the full bipartite state?
```

For Werner states these ledgers branch at different parameter values:

```text
p <= 1/3:
  separable
  CHSH nonviolating
  local marginals still insufficient for global reconstruction except special trivial information supplied elsewhere

1/3 < p <= 1/sqrt(2):
  entangled
  CHSH nonviolating
  locally unreconstructible

p > 1/sqrt(2):
  entangled
  CHSH violating
  locally unreconstructible
```

The separable rho_CC control shows that the third property is not implied by the first.

## 8. DSD significance

The current Property core can retain the bipartite state, subsystem labels, measurement context, and status distinctions as typed data once the quantum specialization is supplied. The Static Aggregation layer already requires explicit injectivity/kernel conditions before reconstruction from reduced readouts.

The new result is therefore not a new quantum theorem. It is a DSD audit classification showing that three often-associated concepts occupy different structural roles and must not be merged by terminology.

The safest current chain is

```text
quantum tensor-product bridge
-> global density state
-> optional local reductions / measurement readouts
-> explicit reconstruction audit
-> separate entanglement criterion
-> separate Bell/CHSH criterion.
```

## 9. Verdict

```text
PASS_WITH_BOUNDARY
```

Confirmed:

- entanglement threshold in the selected Werner family occurs at p=1/3;
- optimal CHSH violation begins at p=1/sqrt(2);
- an interval of entangled but CHSH-nonviolating states therefore exists;
- all Werner states have identical maximally mixed one-party marginals;
- the local-marginal map loses a 9-dimensional correlation sector in the standard two-qubit Pauli representation;
- a separable classically correlated state can have the same local marginals, so local unreconstructibility is not entanglement.

Not established:

- no general Bell-locality threshold is inferred from CHSH nonviolation alone;
- DSD does not derive the PPT or Horodecki criteria;
- no quantum-gravity or DSD-specific causal claim follows from this static state-family audit.

## 10. Reproducibility

```text
audits/science/2026-09-06_werner_dsd_entanglement_chsh.py
```

Run from repository root:

```bash
python audits/science/2026-09-06_werner_dsd_entanglement_chsh.py
```

Dependency:

```text
numpy
```

## 11. Next target

The next useful separation is quantum steering. A controlled two-qubit family can test whether DSD incorrectly collapses

```text
entanglement
steering
Bell nonlocality
local reconstruction failure
```

into one generic notion of 'nonlocal describability'. The external steering criterion must be locked before any DSD interpretation is added.
