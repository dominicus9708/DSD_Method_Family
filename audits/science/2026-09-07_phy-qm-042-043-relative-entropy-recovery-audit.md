# PHY-QM-042~043 — Relative Entropy, Data Processing, and Recovery Audit

Date: 2026-09-07

## Scope
This audit treats standard quantum theory as an external specialization. Umegaki relative entropy, CPTP maps, the data-processing inequality, and recovery maps are not derived from DSD.

## PHY-QM-042 — Pairwise distinguishability can be reduced by a valid channel
Take

- rho = |+><+|,
- sigma = I/2,
- N = complete Z-dephasing.

Then

D(rho||sigma) = ln 2,

while

N(rho) = N(sigma) = I/2,

so

D(N(rho)||N(sigma)) = 0.

Numerical control:

```text
before = 0.693147180559945
after  ~ 0
drop    = ln 2
```

### DSD interpretation
A downstream channel/projection may erase a distinction that existed in the complete state. This is stronger than merely saying that a scalar aggregate is non-injective: the same physically admissible CPTP processing can reduce a standard distinguishability functional.

Safe statement:

```text
complete-state distinction
  does not imply
post-channel distinction under a chosen readout/process.
```

This is compatible with the current DSD descriptive-projection layer, which allows Pi_O(U)=Pi_O(V) for U != V and does not infer reconstruction without an additional condition.

## PHY-QM-043 — Equality in data processing is a recovery/sufficiency statement, not identity of representations
Take

rho_AB = rho_A tensor tau_B,
sigma_AB = sigma_A tensor tau_B,

with

rho_A = diag(0.8,0.2),
sigma_A = diag(0.5,0.5),
tau_B = diag(0.7,0.3).

Under N = Tr_B,

D(rho_AB||sigma_AB) = D(rho_A||sigma_A) = 0.192744757021757... .

The model-class recovery map

R(X) = X tensor tau_B

exactly reconstructs both supplied states.

### DSD interpretation
This separates three questions:

1. Did a representation/process discard coordinates?
2. Did it reduce distinguishability for the state family of interest?
3. Is there an admissible recovery map on that family?

A reduced description may discard an explicit subsystem coordinate and still be sufficient for a restricted state family. Therefore

```text
coordinate loss != unavoidable information loss on every admissible model class.
```

Conversely, equality of one scalar diagnostic alone must not be promoted to full structural recovery without the required recovery theorem or injectivity/sufficiency conditions.

## Methodological consequence
Add the following audit distinction to the candidate general DSD audit vocabulary:

```text
DISTINGUISHABILITY-LOSS AUDIT
RECOVERY/SUFFICIENCY AUDIT
```

They are related to but not identical with the existing kernel/reconstruction audit.

## External references
- Petz equality/recovery results and later stability literature.
- E. A. Carlen, A. Vershynina, Recovery map stability for the Data Processing Inequality, arXiv:1710.02409.
- M. Junge, R. Renner, D. Sutter, M. M. Wilde, A. Winter, Universal recovery maps and approximate sufficiency of quantum relative entropy, arXiv:1509.07127.

## Verdict
PASS_WITH_BOUNDARY.

DSD supplies a useful separation between complete record, reduced readout, lost distinctions, and downstream recovery. Quantum relative entropy provides an external quantitative witness for that separation. No quantum law is derived from DSD.
