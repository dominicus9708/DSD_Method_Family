# PHY-QM-025 — Redundancy vs exact objectivity / spectrum-broadcast audit

## Goal
Test whether a large mutual-information redundancy is sufficient for exact multi-observer objectivity.

## External standard criterion
Spectrum broadcast structure (SBS) represents a system pointer variable redundantly recorded in environment fragments with conditional fragment states whose supports are mutually orthogonal for different pointer values. This supports independent, nondisturbing readout of the same classical label.

For the homogeneous binary record model of PHY-QM-023, a size-m fragment has conditional-state overlap

< E_0^(m) | E_1^(m) > = c^m.

Thus exact orthogonality requires

c^m = 0.

For any finite m and 0 < c < 1, exact orthogonality is absent even though the fragment mutual information can be arbitrarily close to one bit for large m.

## Numerical witnesses
At N=100 and delta=0.1:

### c=0.8
m_QMI = 5,
R_QMI = 20,
conditional overlap squared = c^(2m) = 0.1073741824 > 0.

### c=0.95
m_QMI = 20,
R_QMI = 5,
conditional overlap squared = 0.1285121566 > 0.

Therefore these controls satisfy a sizable QMI-based redundancy count while failing exact finite-fragment SBS orthogonality.

The perfect-copy limit c=0 is different:

m_delta = 1,
R_delta = N,
and the conditional fragment states are exactly orthogonal.

## DSD verdict

MUTUAL-INFORMATION REDUNDANCY != EXACT OBJECTIVITY.

The following must remain distinct:

- global information existence,
- fragment mutual information,
- operationally accessible classical information,
- redundancy count,
- exact broadcast/objectivity structure.

A possible downstream diagnostic tuple is

D_QD = (G, Q_m, A_m, R_delta, B_SBS),

where B_SBS is an externally supplied exact/approximate spectrum-broadcast criterion rather than a DSD primitive.

## Literature boundary
This distinction is consistent with work comparing ordinary Quantum Darwinism and spectrum broadcast structure: a mutual-information plateau or Darwinistic-looking redundancy need not by itself establish the stronger state structure associated with objectivity.

## Status
PASS_WITH_BOUNDARY. This is an analysis of standard quantum-information criteria through DSD reconstruction/completion distinctions, not a derivation of classical objectivity from DSD.

## References
- W. H. Zurek, Quantum Darwinism, Nature Physics 5, 181–188 (2009).
- R. Horodecki, J. K. Korbicz, P. Horodecki, Quantum origins of objectivity, Phys. Rev. A 91, 032122 (2015).
- T. P. Le, A. Olaya-Castro, Objectivity (or lack thereof): Comparison between predictions of quantum Darwinism and spectrum broadcast structure, Phys. Rev. A 98, 032103 (2018).
