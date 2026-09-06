# PHY-QM-014 — Sequential measurement order and lineage audit

Date: 2026-09-06

## Question
Can two protocols use the same operation set and reach the same final unconditional state while retaining different physically relevant measurement histories?

## External quantum specialization
Initial state:

\[
\rho_0=|0\rangle\langle0|.
\]

Use ideal Lüders projective measurements of Pauli X and Z.

Protocol A: X then Z.

Protocol B: Z then X.

## Exact finite witness
For X -> Z:

\[
P(x,z)=1/4
\]

for all four outcome pairs.

For Z -> X:

\[
P(z=+1,x=\pm1)=1/2,
\qquad
P(z=-1,x=\pm1)=0.
\]

The joint-history tables differ, with L1 distance 1.

Nevertheless the unconditional final state in both protocols is

\[
\rho_f=I/2.
\]

Hence

\[
\boxed{\rho_f^{X\to Z}=\rho_f^{Z\to X}}
\]

but

\[
\boxed{P_{X\to Z}(h)\neq P_{Z\to X}(h)}.
\]

## DSD interpretation
This is an external finite witness for the distinction

\[
\boxed{\text{final reduced-state equality}\not\Rightarrow\text{lineage equality}.}
\]

The current Structural Reorganization Dynamics already states that lineage-connected succession is time-directed and that aggregate equality is not by itself a criterion for lineage succession. The quantum witness therefore converges with the existing DSD dynamics rather than requiring a core revision.

## Audit verdict
- Operation-set equality implies protocol equivalence: **FAIL**.
- Final-state equality implies sequential-history equivalence: **FAIL**.
- Ordered transition lineage is required when the downstream question depends on intermediate outcomes: **PASS**.
- This is a new quantum prediction of DSD: **NO**; it is a DSD analysis of standard quantum measurement theory.

## Impact
For quantum specializations, a protocol descriptor must preserve temporal order whenever sequential outcome structure matters. An unordered set of operations is an information-losing compression.

## Reproducibility
Run:

```bash
python audits/science/2026-09-06_sequential_quantum_instrument_dsd_order.py
```
