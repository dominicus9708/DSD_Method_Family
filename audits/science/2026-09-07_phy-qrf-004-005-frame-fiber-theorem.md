# PHY-QRF-004~005 — Frame-Change Fiber Preservation and Coarse-Graining Audit

Date: 2026-09-07

## Scope
This note formulates a conditional DSD-analysis proposition for quantum/reference-frame representations. It does not add an axiom to the DSD core and does not derive QRF theory.

## PHY-QRF-004 — Bijective frame change preserves readout fibers under compatible transport
Let Q_A and Q_B be two admitted relative-state spaces and let

F: Q_A -> Q_B

be a bijection representing an ideal frame change.

Let

R_B: Q_B -> Y

be a readout in frame B and define the transported frame-A readout by

R_A = R_B o F.

For x in Q_A,

Fib_A(x) = {u in Q_A : R_A(u)=R_A(x)},

Fib_B(Fx) = {v in Q_B : R_B(v)=R_B(Fx)}.

Then

F(Fib_A(x)) = Fib_B(Fx).

### Proof
If u belongs to Fib_A(x), then

R_B(Fu)=R_A(u)=R_A(x)=R_B(Fx),

so Fu belongs to Fib_B(Fx). Conversely, if v belongs to Fib_B(Fx), bijectivity gives v=Fu for a unique u. Then

R_A(u)=R_B(Fu)=R_B(v)=R_B(Fx)=R_A(x),

so u belongs to Fib_A(x).

Thus the fibers correspond bijectively.

### Consequence
An invertible change of frame coordinates does not by itself enlarge or shrink the indistinguishability class when the readout is transported compatibly.

This gives a precise DSD-analysis form of

```text
invertible perspective change != describability loss.
```

## PHY-QRF-005 — Coarse-graining after a frame change enlarges fibers because of the coarse map, not because of the frame change itself
Let the frame change F remain bijective, but let

C: Q_B -> Z

be a noninjective coarse readout. Define

G = C o F.

Then

G^{-1}(z) = F^{-1}(C^{-1}(z)).

Hence every loss of identifiability in G is inherited from the noninjective C, not from the bijective F.

### Finite Z2 witness
Use the relational map

F(r_B,r_C)=(r_B,r_B xor r_C)

on the four binary relational states. F is bijective.

Now let

C(y_1,y_2)=y_1.

The composite G has fibers

```text
0 : {(0,0),(0,1)}
1 : {(1,0),(1,1)}
```

of size 2.

The frame change alone preserved four distinct relative states; the later coarse readout erased one bit.

## Audit consequence
Reference-frame analyses should distinguish at least:

```text
FRAME TRANSFORMATION MAP
RELATIVE-STATE QUOTIENT
READOUT / ACCESS MAP
COARSE-GRAINING MAP
```

Only the appropriate noninjective stage should be labelled as the source of information loss.

Candidate general-audit label:

```text
FRAME-INVERTIBILITY / FIBER-PRESERVATION AUDIT
```

## Relation to current DSD
This theorem is directly compatible with the current DSD descriptive projection language, where distinct complete states may share one projected state, and with the existing requirement that reduced aggregates/readouts not be treated as complete classifiers without injectivity or reconstruction.

## External QRF reference
- T. Carette, J. Głowacki, L. Loveridge, Operational Quantum Reference Frame Transformations, arXiv:2303.14002.

## Verdict
CONDITIONAL THEOREM / PASS.

The theorem is purely map-theoretic once the relative-state spaces, bijective frame bridge, and compatible readout are supplied. Its physical applicability depends on the external QRF construction actually satisfying those assumptions.
