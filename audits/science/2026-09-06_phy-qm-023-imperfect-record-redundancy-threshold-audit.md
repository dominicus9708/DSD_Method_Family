# PHY-QM-023 — Imperfect record redundancy threshold audit

## Model
Let the pointer variable S be equiprobable in |0>,|1>. Each environment fragment carries one of two pure conditional states |e_0>, |e_1> with overlap

c = |<e_0|e_1>|,  0 <= c < 1.

A fragment containing m independent environment units has conditional-state overlap c^m.

For the classical-quantum state

rho_SF = 1/2 |0><0| tensor |E_0^(m)><E_0^(m)|
       + 1/2 |1><1| tensor |E_1^(m)><E_1^(m)|,

the fragment quantum mutual information is

I_QMI(S:F_m) = h_2((1+c^m)/2).

For the symmetric binary pure-state ensemble, optimal binary discrimination has Helstrom error

e_m = (1-sqrt(1-c^(2m)))/2,

and the corresponding optimally accessible binary information is

I_acc(m) = 1 - h_2(e_m).

Define m_delta as the smallest fragment reaching 1-delta bits, and integer redundancy

R_delta = floor(N/m_delta)

when m_delta <= N.

## N=100, delta=0.1 control

| c | m_QMI | R_QMI | m_acc | R_acc |
|---:|---:|---:|---:|---:|
| 0.00 | 1 | 100 | 1 | 100 |
| 0.50 | 2 | 50 | 3 | 33 |
| 0.80 | 5 | 20 | 7 | 14 |
| 0.90 | 10 | 10 | 15 | 6 |
| 0.95 | 20 | 5 | 29 | 3 |
| 0.99 | 100 | 1 | 148 | 0 |

Thus the mutual-information threshold can be reached by smaller fragments than the operationally accessible-information threshold.

For example, at c=0.8:

m_QMI=5, R_QMI=20,
m_acc=7, R_acc=14.

At c=0.95:

m_QMI=20, R_QMI=5,
m_acc=29, R_acc=3.

## DSD verdict

FRAGMENT CORRELATION != OPERATIONALLY ACCESSIBLE RECORD.

A redundancy count is therefore indexed by the diagnostic and access rule used to define a qualifying fragment.

The safe DSD representation is not one universal scalar R, but a typed quantity such as

R_delta[diagnostic, measurement/access class, fragment partition].

## Audit boundary
The formulas above come from a deliberately homogeneous conditional-product control model. They are not universal laws of arbitrary environments.

## Status
PASS_WITH_BOUNDARY.

## Reproducibility
python audits/science/2026-09-06_quantum_darwinism_dsd_redundancy.py --mode threshold --N 100 --delta 0.1
