# PHY-QM-050 — Configuration-State Audit of POVM Readout and Quantum-Instrument Transition

Date: 2026-09-08
Status: **PASS_WITH_REFINEMENT**
Track: **2 — Full DSD structural analysis of standard quantum mechanics and relativity**

## 1. Purpose

This audit revisits the already established standard-QM witness in PHY-QM-015 and PHY-QM-017 under the newer DSD configuration-state decomposition

\[
\boxed{\Sigma_t + \mathcal R_{\mathrm{std}} + \Gamma_{t\to t'}}.
\]

The purpose is not to repeat the earlier numerical result and not to derive the Born rule or quantum instruments from DSD. The purpose is to test whether the newer one-slice configuration-state interpretation keeps three logically different objects separate:

1. what is currently describable at one time slice;
2. standard-domain relations connecting current data to readout;
3. the actual outcome-conditioned transition law.

No quantum-gravity, unification, or nonstandard quantum premise is used.

---

## 2. Source and interface lock

### Standard quantum mechanics

For an outcome family \(a\), a quantum instrument supplies completely positive trace-nonincreasing maps

\[
\mathcal I_a:\rho\mapsto \widetilde\rho_a,
\]

with the sum over outcomes trace preserving for a complete instrument. Its POVM effects satisfy the standard relation

\[
E_a=\mathcal I_a^*(I),
\]

and the one-step probabilities are

\[
p(a|\rho)=\operatorname{Tr}(\rho E_a)
=\operatorname{Tr}(\mathcal I_a(\rho)).
\]

For \(p(a|\rho)>0\), the conditional postmeasurement state is

\[
\rho_a'=
\frac{\mathcal I_a(\rho)}{p(a|\rho)}.
\]

These are external standard-QM data. DSD does not derive complete positivity, the Born trace rule, or the instrument-to-effect relation.

### DSD interfaces

The current Property Axiom System retains typed property declaration, applicability, contextual prerequisite satisfaction, and partial assignment over a fixed Stage-VI formation background. Optional representation, static aggregation, dynamics, and physical specialization remain downstream.

The current Structural Reorganization Dynamics layer requires explicit constitutive dynamic data when property or external-domain data are used to define transition operators. A property label or readout value does not canonically determine a dynamic operator.

Therefore a standard quantum instrument is admissible only as explicit downstream standard-domain transition data; it is not inferred from a DSD property name.

---

## 3. Reuse of the established finite witness

This audit deliberately reuses, rather than duplicates, the exact witness from:

```text
audits/science/2026-09-06_phy-qm-015-povm-vs-instrument-dynamics-obstruction.md
audits/science/2026-09-06_phy-qm-017-quantum-instrument-to-dsd-transition-bridge.md
audits/science/2026-09-06_sequential_quantum_instrument_dsd_order.py
```

Use the same Z POVM

\[
E_{\pm}=P^Z_{\pm}
\]

with two different instruments.

Lueders instrument:

\[
\mathcal I^L_z(\rho)=P_z^Z\rho P_z^Z.
\]

Measure-Z/reprepare-X instrument:

\[
\mathcal I^R_+(\rho)
=\operatorname{Tr}(P^Z_+\rho)|+\rangle\langle+|,
\]

\[
\mathcal I^R_-(\rho)
=\operatorname{Tr}(P^Z_-\rho)|-\rangle\langle-|.
\]

For

\[
\rho_0=|0\rangle\langle0|,
\]

both give the same first readout

\[
p(z=+1)=1,
\qquad
p(z=-1)=0.
\]

A subsequent X measurement separates them:

\[
P_L(z=+1,x=+1)=P_L(z=+1,x=-1)=\frac12,
\]

while

\[
P_R(z=+1,x=+1)=1,
\qquad
P_R(z=+1,x=-1)=0.
\]

Hence

\[
\boxed{\text{same one-step POVM readout}\not\Rightarrow
\text{same measurement transition}}.
\]

This is an exact standard-QM finite witness already computationally reproduced in the repository.

---

## 4. Configuration-state refinement

The new configuration-state language makes an additional distinction necessary.

### 4.1 Reduced system/readout state

If the declared DSD system boundary retains only the current quantum state and the selected one-step measurement/readout data, a reduced one-slice record may be written schematically as

\[
\Sigma_{Q,t}^{\mathrm{red}}
=
\bigl(
F_t,
P_t,
R_t[\rho],
A_t[\mathcal M],
\Phi_t[p]
\bigr).
\]

Two physically different measurement implementations can project to the same reduced record when their current state, POVM effects, and one-step outcome probabilities agree.

Thus equality of \(\Sigma_{Q,t}^{\mathrm{red}}\) at this deliberately coarse boundary does not reconstruct the active instrument.

This is not a failure of temporality and not a contradiction. It is a declared compression/reconstruction limit of the reduced configuration state.

### 4.2 Experiment-complete one-slice state

If the actual apparatus, control setting, or operation-selection record is itself currently describable and is included inside the declared system boundary, then a more complete experiment-level record must retain that difference:

\[
\Sigma_{Q,t}^{\mathrm{exp}}
=
\bigl(
F_t,
P_t,
R_t[\rho,\mathrm{setup}],
A_t[\mathcal M,\mathrm{allowed\ operations}],
\Phi_t[p]
\bigr).
\]

The exact location of `setup` is specialization-dependent: it may enter through Formation-level material/configuration data, Property auxiliary typed inputs, or a downstream representation/access package. No new universal DSD primitive is introduced here.

Therefore, if the two instrument implementations correspond to different presently describable apparatus/control configurations, then calling them the same **complete experiment-level configuration state** would be an under-description.

This yields the refinement

\[
\boxed{
\text{same reduced configuration snapshot}
\not\Rightarrow
\text{same experiment-complete configuration state}
}.
\]

The completeness of a configuration state is therefore relative to the declared system boundary and retained typed coordinates.

---

## 5. Where the transition belongs

Even an experiment-complete one-slice record should not absorb the quantum transition map itself as though it were an ordinary static value.

Let the standard-domain relation package contain the instrument-to-effect/Born-readout relations:

\[
\mathcal R_{\mathrm{QM}}
\supset
\left\{
E_a=\mathcal I_a^*(I),
\quad
p_a=\operatorname{Tr}(\rho E_a)
\right\}.
\]

Then the outcome-conditioned transition remains

\[
\Gamma_{\mathcal I,a}:
\Sigma_{Q,t}^{-}
\longrightarrow
\Sigma_{Q,t'}^{+,a},
\]

with the quantum-state coordinate updated according to

\[
\rho
\longmapsto
\rho_a'
=
\frac{\mathcal I_a(\rho)}{\operatorname{Tr}(\mathcal I_a(\rho))}.
\]

Accordingly,

\[
\boxed{
\Sigma_t
\neq
\mathcal R_{\mathrm{QM}}
\neq
\Gamma
}
\]

as logical roles, even though the three are jointly needed for an experiment-complete sequential description.

---

## 6. Non-injectivity of the transition-to-readout projection

The standard map

\[
\{\mathcal I_a\}_a
\longmapsto
\{E_a\}_a
\longmapsto
\bigl(p(a|\rho)\bigr)_a
\]

is not injective over the witness family.

The two different instruments \(\mathcal I^L\neq\mathcal I^R\) induce the same Z POVM and the same first-step probability vector on \(\rho_0\), but different later sequential statistics.

Hence there is no reconstruction map from the one-step readout alone that recovers the transition law over this family:

\[
\boxed{
\Phi_{\mathrm{1step}}
\text{ is insufficient to reconstruct }\Gamma_{\mathcal I}
}.
\]

### Status

**Exact standard-QM finite witness + generic structural reconstruction statement over the exhibited family.**

This is not a new quantum theorem and does not validate DSD physics. It validates the need for the DSD layering to avoid an unsound identification.

---

## 7. Relation to static aggregation

The current Channel-Indexed Static Aggregation layer is a reduced downstream descriptor. Therefore neither equality of a one-step probability aggregate nor equality of any further reduced static aggregate can be promoted to equality of quantum-instrument transition data without an injectivity theorem for the supplied reduction.

The hierarchy is therefore

\[
\text{experiment-level typed state}
\to
\text{selected readout / aggregate}
\]

for the static reduction, while independently

\[
\text{experiment-level typed state}
\xrightarrow{\Gamma_{\mathcal I,a}}
\text{postmeasurement typed state}
\]

for the temporal transition.

Static equality and temporal-law equality are not equivalent notions.

---

## 8. Audit verdict

```text
STANDARD-QM WITNESS REPRODUCED PREVIOUSLY             : PASS
ONE-STEP POVM READOUT DISTINCT FROM INSTRUMENT         : PASS
REDUCED SNAPSHOT MAY ERASE INSTRUMENT IDENTITY         : PASS
COMPLETE EXPERIMENT STATE MUST RETAIN DESCRIBABLE SETUP: PASS_WITH_SCOPE
TRANSITION MAP REMAINS IN GAMMA / DYNAMIC SPECIALIZATION: PASS
NEW DSD CORE AXIOM REQUIRED                            : NO
NEW QUANTUM LAW DERIVED                                : NO
QUANTUM-GRAVITY CLAIM                                  : NO
```

Overall verdict: **PASS_WITH_REFINEMENT**.

The newer \(\Sigma_t+\mathcal R_{\mathrm{std}}+\Gamma\) decomposition survives the detailed standard-QM measurement test. The main refinement is that configuration-state completeness must be indexed by the declared system boundary: a reduced system/readout snapshot may identify two implementations that a complete experiment-level state must distinguish if their apparatus/control difference is itself within the retained describable structure.

---

## 9. Reproducibility

No duplicate Python file is created because the required finite computation already exists and is unchanged.

Run from the repository root:

```bash
python audits/science/2026-09-06_sequential_quantum_instrument_dsd_order.py
```

The relevant section is `PHY-QM-015: same POVM, different instruments`.

---

## 10. Next target

Proceed to the second detailed audit:

```text
QM composite access
  tensor-product carrier
  partial trace
  entanglement/separability
  local accessibility
  global-state reconstruction obstruction
```

The main question is whether the distinction

\[
\text{global state existence}
\neq
\text{subsystem accessibility}
\neq
\text{global reconstructibility from local data}
\]

fits the same configuration-state architecture without silently identifying standard-QM subsystem structure with DSD internal/external status.
