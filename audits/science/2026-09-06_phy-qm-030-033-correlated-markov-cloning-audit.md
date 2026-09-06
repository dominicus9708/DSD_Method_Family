# PHY-QM-030~033 — Correlated Environments, Conditional Sufficiency, and No-Cloning

Date: 2026-09-06

Status: PASS_WITH_BOUNDARY

## PHY-QM-030 — Correlated environment: synergy counterexample

Use a classical diagonal cq control embedded in standard quantum theory. Let `S=E1 xor E2` with `E1,E2` independent unbiased bits. Then

- `I(S:E1)=0`
- `I(S:E2)=0`
- `I(S:E1E2)=1 bit`
- `I(S:E2|E1)=1 bit`

Thus no additive fragment law of the form `record(F)=sum_i record(i)` can be universal once fragment correlations are admitted.

DSD verdict:

`individual-fragment non-describability` does not imply `joint-fragment non-describability`.

This is a genuine support/correlation-retention issue, not specifically a quantum effect: the example is classical but is admissible as a diagonal quantum state.

## PHY-QM-031 — Redundant overlap and double counting

Use the duplicate record control `S=E1=E2` with an unbiased system bit. Then

- `I(S:E1)=1 bit`
- `I(S:E2)=1 bit`
- `I(S:E1E2)=1 bit`
- `I(S:E2|E1)=0`

The naive sum of local mutual informations is 2 bits although the joint record contains only 1 bit of system information.

DSD verdict:

`sum of fragment scores` is not a reconstruction theorem for independent information content.

The support structure and correlation/overlap structure must be retained when a downstream diagnostic claims redundancy or independent recoverability.

## PHY-QM-032 — Conditional mutual information as a sufficiency/recovery diagnostic

For a binary Markov control `S -> B -> C`, with bit-flip noise `q=0.2` from `S` to `B` and `r=0.3` from `B` to `C`, the reproducibility script gives

- `I(S:B)=0.2780719051 bits`
- `I(S:C)=0.0419579778 bits`
- `I(S:C|B)=0` up to floating-point error.

This distinguishes two questions:

1. whether `C` contains information about `S`;
2. whether `C` contains any information about `S` that is not already mediated/summarized by `B`.

For quantum states, zero quantum conditional mutual information is the equality case of strong subadditivity and characterizes a short quantum Markov structure; the Petz recovery structure supplies exact recovery in that equality case. Small conditional mutual information also controls approximate recoverability in the Fawzi-Renner sense.

DSD verdict:

A candidate middle record `B` should not be called sufficient merely because it has a high aggregate score. A stronger downstream test is whether omitted coordinates add conditional information or whether a declared recovery map exists.

Do not promote quantum CMI or the Petz map into the universal DSD core. They are quantum-domain diagnostics supplied by the specialization.

## PHY-QM-033 — No-cloning versus pointer-record proliferation

Standard no-cloning forbids a universal operation that copies arbitrary unknown nonorthogonal quantum states. A minimal CNOT control gives

`CNOT |+>|0> = (|00>+|11>)/sqrt(2)`

rather than `|+>|+>`. The fidelity with the desired cloned state is `1/2`.

By contrast, the same CNOT copies the orthogonal computational-basis states exactly:

- `|0>|0> -> |0>|0>`
- `|1>|0> -> |1>|1>`

Therefore Quantum-Darwinism-style proliferation of selected pointer information is not universal quantum-state cloning.

DSD verdict:

`record redundancy` must be typed by the property actually being redundantly encoded. Repeated records of one stable pointer observable do not imply multiple copies of the full underlying quantum state.

This is a strong boundary against interpreting DSD redundancy as unrestricted structural duplication.

## Combined methodological result

The product-record approximation used in PHY-QM-026~029 is therefore explicitly restricted. With correlations present, the relevant information descriptor becomes a set function `F -> J(F)` rather than an additive sum over elementary supports.

At least three distinct phenomena must remain separate:

- synergy: information appears only jointly;
- redundancy: multiple supports encode the same information;
- conditional sufficiency: one support makes another informationally unnecessary relative to a target.

These are downstream analysis structures, not new Formation or Property axioms.

## Reproducibility

Run from repository root:

```bash
python audits/science/2026-09-06_quantum_relativistic_expansion_batch.py --mode correlated
python audits/science/2026-09-06_quantum_relativistic_expansion_batch.py --mode markov --q 0.2 --r 0.3
python audits/science/2026-09-06_quantum_relativistic_expansion_batch.py --mode cloning
```

## External references

- Wootters, W. K. & Zurek, W. H. (1982), *A single quantum cannot be cloned*, Nature 299, 802–803.
- Hayden, P., Jozsa, R., Petz, D. & Winter, A. (2004), *Structure of States Which Satisfy Strong Subadditivity of Quantum Entropy with Equality*, Commun. Math. Phys. 246, 359–374.
- Fawzi, O. & Renner, R. (2015), *Quantum Conditional Mutual Information and Approximate Markov Chains*, Commun. Math. Phys. 340, 575–611.
