# PHY-QRF-001~003 — Quantum Reference Frames and Describability Audit

Date: 2026-09-07

## Scope
Quantum-reference-frame (QRF) transformations are treated as external quantum theory. DSD is used to distinguish invertible representation change, operational equivalence, and genuine coarse-graining/information loss.

## PHY-QRF-001 — Relative states are equivalence classes under operationally available relational observables
Modern operational QRF frameworks construct relative observables and identify states that cannot be distinguished by those observables. Thus the relevant state space is already quotient-like: absolute descriptions related by inaccessible frame redundancy may represent the same operational relative state.

### DSD consequence
This is naturally represented by a descriptive projection/equivalence relation

Pi_O(U)=Pi_O(V)

without requiring U=V at the underlying presentation level.

However, QRF operational equivalence is an external specialization. DSD's general descriptive equivalence does not by itself determine which quantum frame observables are physical.

## PHY-QRF-002 — Ideal frame change can be an invertible representation change
Finite Z2 relational control:

Take three binary labels A,B,C with the global redundancy

(A,B,C) ~ (A xor 1, B xor 1, C xor 1).

Relative to A, use coordinates

r_B = A xor B,
r_C = A xor C.

Relative to B,

r_A' = A xor B = r_B,
r_C' = B xor C = r_B xor r_C.

Hence

(r_B,r_C) -> (r_B, r_B xor r_C).

Enumeration gives

```text
(0,0) -> (0,0)
(0,1) -> (0,1)
(1,0) -> (1,1)
(1,1) -> (1,0)
```

which is a bijection of all four relational states.

### DSD consequence
In this idealized relational control,

```text
reference-frame change != describability loss.
```

This directly parallels the earlier Lorentz-coordinate audit: an invertible change of representation can alter coordinates without erasing the represented relational structure.

## PHY-QRF-003 — Operational QRF change can become noninvertible when frame localizability/accessible structure is insufficient
Operational QRF work shows that frame-change maps need not always be invertible; invertibility depends on properties of the frames, including suitable localizability conditions in the cited construction.

### DSD consequence
The correct classification is therefore conditional:

```text
frame change
  = invertible representation change,
    if the supplied QRF bridge is invertible;

frame change
  may include operational coarse-graining,
    if the frame/readout structure identifies distinct relative states.
```

So neither of the following is safe universally:

```text
all frame changes preserve full information
all frame changes create information loss
```

The bridge must be audited.

## Cross-contact with relativity
This gives DSD a useful common language across classical relativity and QRF theory:

```text
coordinate/frame transformation
-> ask whether the representation map is invertible on the admitted state class
-> only then classify information loss or structural branching.
```

The result is not a claim that Lorentz transformations and QRF transformations are the same mathematical object.

## External references
- T. Carette, J. Głowacki, L. Loveridge, Operational Quantum Reference Frame Transformations, arXiv:2303.14002; later published in Quantum.
- M. Krumm, P. A. Hoehn, M. P. Mueller, Quantum reference frame transformations as symmetries and the paradox of the third particle, Quantum 5, 530 (2021), arXiv:2011.01951.
- J. M. Yang, Switching Quantum Reference Frames for Quantum Measurement, Quantum 4, 283 (2020), arXiv:1911.04903.

## Verdict
PASS_WITH_BOUNDARY.

QRF theory supports a DSD audit distinction between operational equivalence and complete presentation, and between invertible perspective change and lossy operational quotienting. It does not imply a universal observer-dependent loss of describability.
