# PHY-QM-022 — Global information vs redundancy audit

## Goal
Test whether the mere existence of a complete environment record determines how redundantly that record is distributed.

## External quantum bridge
Use an equal-prior classical pointer variable S in basis {|0>,|1>} and N environment fragments E_1,...,E_N.

### Model A — localized perfect record
Only E_1 stores the pointer value; E_2,...,E_N are fixed blanks.

### Model B — perfect broadcast record
Every E_k stores the same pointer value in mutually orthogonal states.

Both models have one bit of global S:E information:

I(S:E)=1 bit.

However the number of disjoint one-fragment records differs:

R_A=1,
R_B=N.

Thus there exist two physical record structures with the same global mutual information and different redundancy.

## DSD verdict

GLOBAL_RECORD_EXISTENCE != REDUNDANCY.

Equivalently, if G denotes a global-information summary and R the record redundancy, there is no universal factorization R=g(G) on this family.

This is a reconstruction/factorization obstruction: a scalar statement that the environment as a whole contains the pointer information does not reconstruct how that information is distributed across typed fragments.

## Consequence for DSD quantum specialization
Keep at least these coordinates distinct:

- global record existence / total correlation,
- fragment identity and support,
- fragment-level accessibility,
- redundancy count.

Do not infer multi-observer objectivity from a global S:E mutual-information value alone.

## Status
PASS_WITH_BOUNDARY. The result uses standard quantum-information quantities as an external bridge and does not derive Quantum Darwinism from DSD.

## References
- W. H. Zurek, Quantum Darwinism, Nature Physics 5, 181–188 (2009).
- R. Horodecki, J. K. Korbicz, P. Horodecki, Quantum origins of objectivity, Phys. Rev. A 91, 032122 (2015).
