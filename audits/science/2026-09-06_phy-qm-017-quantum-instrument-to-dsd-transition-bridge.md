# PHY-QM-017 — Quantum instrument to DSD transition bridge

Date: 2026-09-06

## Purpose
Consolidate PHY-QM-014 to 016 into a minimal downstream quantum-dynamics interface without promoting standard quantum measurement laws into the DSD core.

## External bridge data
For a measurement step with classical outcome a, use a quantum instrument

\[
\mathcal I_a:\rho\mapsto\widetilde\rho_a,
\]

where each \(\mathcal I_a\) is completely positive and trace nonincreasing, and the sum over outcomes is trace preserving for a complete instrument.

The associated POVM effects describe one-step outcome probabilities, but they do not in general determine the postmeasurement state update.

## Minimal DSD-compatible specialization
A branch transition may be written schematically as

\[
J_k^{\rm QM}:(\rho_{k-1},h_{k-1})
\Rightarrow
\{(\rho_k,h_k,p_k)\}_{a_k},
\]

with

\[
\widetilde\rho_k=
\mathcal I^{(k)}_{a_k|h_{k-1}}(\rho_{k-1}),
\qquad
p_k=\operatorname{Tr}\widetilde\rho_k,
\]

\[
\rho_k=\widetilde\rho_k/p_k
\quad(p_k>0).
\]

The DSD transition relation supplies the typed branching/lineage architecture; the CP instrument and Born trace rule are external quantum constitutive data.

## Surviving distinctions
The audits require the following to remain separate:

1. measurement effect / POVM readout;
2. measurement instrument / postmeasurement transition;
3. protocol operation set;
4. temporal order;
5. adaptive policy;
6. realized branch history;
7. final unconditional state.

No one of items 1, 3, or 7 reconstructs all the others in general.

## Compression obstructions established
### Final-state erasure
There exist X->Z and Z->X protocols with identical final unconditional state \(I/2\) but different joint histories.

### POVM erasure
There exist distinct instruments with the same Z POVM statistics but different later X statistics.

### Policy erasure
An adaptive protocol cannot be reconstructed from a fixed unordered operation set because the next operation depends on preceding outcomes.

## Relation to current DSD papers
The Property Axiom System already retains complete ordered typed inputs and places dynamics in downstream specialization. Structural Reorganization Dynamics already allows relation-valued branching transitions and time-directed lineage, and explicitly rejects aggregate equality as a sufficient lineage criterion. Therefore the current quantum witness supports the existing layering rather than requiring a foundational rewrite.

## Verdict
**PASS_WITH_SPECIALIZATION**.

The current DSD architecture can host standard sequential quantum measurement theory if the specialization preserves instrument-level transition data and branch lineage. Treating POVM effects, final states, or unordered operation collections as complete dynamic descriptions is unsound.

## Next audit target
Test whether coarse-graining or erasing intermediate classical records can make two distinct adaptive histories observationally equivalent at a later readout, and distinguish reversible record omission from physically irreversible decoherence/environmental record formation.
