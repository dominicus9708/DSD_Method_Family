# PHY-QM-021 — Accessibility, coarse-graining, dephasing, and erasure taxonomy

Date: 2026-09-06

## Purpose

The preceding quantum audits show that the word `record` or `erasure` is too coarse unless the physical carrier, readout support, transition law, and environment scope are all declared. This note gives the DSD-safe taxonomy for later quantum specializations.

## Six distinct cases

### 1. Coherent outcome carrier exists but is unread

No physical quantum channel is applied. The full state remains unchanged; only the chosen observer/protocol does not read the carrier.

```text
physical state change: no
readout restriction: yes
coherence may remain: yes
```

### 2. Descriptive coarse-graining / discarded coordinate

A readout map such as partial trace or an aggregate projection is applied to the description.

```text
underlying larger state changed by the map: not asserted
reduced descriptor loses information: generally yes
```

This is a representation/readout operation, not automatically a physical transition.

### 3. Carrier inaccessible to the current protocol

The carrier exists in the chosen physical model but is not in the admissible support of the current readout or control protocol.

```text
carrier existence: yes
current access: no
```

`inaccessible` is not identified with the Property Axiom System statuses `undefined`, `inapplicable`, or `prerequisite-unsatisfied`.

### 4. Physical dephasing

A quantum channel suppresses off-diagonal coherence in a declared basis. In the explicit control,

\[
\rho_C\mapsto\rho_D.
\]

This is a downstream dynamical operation.

### 5. Local reset with correlation transfer

A local carrier can be reset while the correlation is transferred to another carrier/environment. The explicit SWAP witness gives

\[
I(S:R):2\to0,
\qquad
I(S:E):0\to2.
\]

Thus local reset is not sufficient evidence for global destruction.

### 6. Effective irreversibility under an environment scope

When environmental degrees of freedom are physically uncontrolled or dispersed, reversal can become operationally unavailable. This should be recorded as a scope-dependent accessibility/recoverability statement. It is not, by itself, proof that all global quantum information has been ontologically destroyed.

## DSD method rule

For a quantum specialization, use separate coordinates for at least

```text
PHYSICAL_CARRIER_SET
ACCESSIBLE_CARRIER_SET
READOUT_MAP
QUANTUM_CHANNEL_OR_INSTRUMENT
COHERENCE_DIAGNOSTIC
CONDITIONING_RULE
LINEAGE / PROTOCOL HISTORY
RECOVERABILITY_TEST
```

Do not use one `record status` field to silently replace these distinctions.

## Exact factorization witness

For the coherent and dephased states,

\[
\Phi_{\rm local}(\rho_C)=\Phi_{\rm local}(\rho_D),
\]

but a future reversal or X-basis conditional protocol gives different responses. Therefore

\[
\boxed{
\ker\Phi_{\rm local}\not\subseteq\ker R_{\rm protocol}
}
\]

for the witness pair, and the future response cannot factor through the local-marginal descriptor.

This is the same structural form as the existing DSD static aggregation warning that a reduced aggregate does not reconstruct complete typed/support structure without a separate injectivity or reconstruction result.

## Relation to current DSD papers

The Property Axiom System already keeps typed inputs and assignment statuses distinct, while explicitly leaving probabilistic, dynamical, and representation-specific structure to downstream extensions. Therefore no Property-core rewrite is required by these quantum results.

Structural Reorganization Dynamics already requires status distinctions used by the claimed result to be preserved or explicitly coarse-grained, and states that reduced readouts do not replace component-resolved state without an injectivity/reconstruction result. The quantum controls give external physical witnesses for that design choice.

## Terminology recommendation

Within DSD quantum notes, prefer

```text
measurement outcome carrier
carrier accessibility
readout coarse-graining
physical dephasing
local reset / correlation transfer
conditional recoverability
```

over the unqualified word `record` when the distinction matters.

## Audit verdict

- `unread = inaccessible = dephased = erased`: **FAIL**.
- `partial trace = physical decoherence`: **FAIL**.
- `local carrier reset = global information destruction`: **FAIL**.
- explicit carrier/access/readout/channel/lineage separation: **PASS**.
- current DSD core requires modification: **NO**; downstream specialization is sufficient.

Verdict: **PASS_WITH_BOUNDARY**.

## Next target

The next audit should test whether environment-induced decoherence plus redundant environment fragments changes the analysis from simple inaccessible-carrier loss to a many-carrier reconstruction problem. A natural finite target is quantum Darwinism / redundant pointer-state records, with a strict separation between local accessibility, redundancy, and objective agreement.

## Reproducibility

```bash
python audits/science/2026-09-06_quantum_record_decoherence_dsd.py --mode all
```
