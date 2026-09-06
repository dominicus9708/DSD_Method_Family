# PHY-QM-024 — Fragment access class and observer-agreement audit

## Goal
Separate three questions that are easy to conflate:

1. Does a fragment physically carry information about the pointer variable?
2. Can an observer recover that information with the declared measurement class?
3. Do two observers agree with one another?

## Same physical fragment, different access class
Use the PHY-QM-023 binary pure-state fragment family with

|e_0> = |0>,
|e_1> = c|0> + sqrt(1-c^2)|1>.

For m copies, unrestricted optimal discrimination succeeds with

P_opt = (1+sqrt(1-c^(2m)))/2.

If the observer is restricted to measuring every copy in the computational Z basis and infers pointer=1 iff any result 1 appears, then

P_Z = 1 - c^(2m)/2.

Thus accessibility is indexed by the allowed measurement class even when the physical fragment is identical.

## Controls at the 90% QMI fragment threshold

| c | m_QMI | P_opt | P_Z |
|---:|---:|---:|---:|
| 0.50 | 2 | 0.984123 | 0.968750 |
| 0.80 | 5 | 0.972394 | 0.946313 |
| 0.90 | 10 | 0.968621 | 0.939212 |
| 0.95 | 20 | 0.966768 | 0.935744 |
| 0.99 | 100 | 0.965301 | 0.933010 |

Therefore a record may exist in the fragment while its practical accessibility depends on which measurements are admitted.

## Two-observer agreement
For two disjoint homogeneous fragments of the same size, assume independent optimal binary inference conditioned on the same pointer value. If e is the Helstrom error per observer, then

P_agree = (1-e)^2 + e^2.

At c=0.8, m=5:

P_agree = 0.946313.

At c=0.95, m=20:

P_agree = 0.935744.

Agreement is not the same as correctness: both observers can agree on the wrong label. Hence

OBSERVER AGREEMENT != TRUTH / CORRECT POINTER INFERENCE.

## DSD verdict
Keep distinct downstream coordinates such as

- physical record correlation,
- allowed measurement/access class,
- inference success,
- pairwise/multi-observer agreement.

A useful typed diagnostic is

A(F; M) = operational accessibility of fragment F under measurement class M.

Do not promote A to a universal DSD scalar.

## Status
PASS_WITH_BOUNDARY. The observer-agreement formula assumes conditionally independent, homogeneous fragments and a symmetric binary task.

## Reproducibility
python audits/science/2026-09-06_quantum_darwinism_dsd_redundancy.py --mode access --delta 0.1
