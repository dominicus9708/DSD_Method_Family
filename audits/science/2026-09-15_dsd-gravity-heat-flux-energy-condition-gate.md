# BH-RB-024 — Internal Heat-Flux / Energy-Condition Admissibility Gate

**Date:** 2026-09-15  
**Project:** DSD gravity rebaseline  
**Status:** PASS_WITH_BOUNDARY

## Scope

The canonical BH-RB-022/023 line already established that a positive-pressure, self-bound causal EOS does not by itself create a positive-radius turnaround while a regular spherical shell remains strictly trapped.

This audit asks the next question:

> Can the internal outward energy flux needed to reduce Misner-Sharp compactness satisfy necessary local energy-condition bounds, or would such a flux automatically require exotic matter?

The answer is conditional: **a local NEC-compatible window exists in a synthetic control, but not for every trapped collapsing state.**

This is not yet a transport law and does not derive global de-trapping or a finite core radius.

## Dimensionless shell variables

Use geometrized units \(G=c=1\) and define

\[
\mathcal C=\frac{2m}{R},
\qquad
E=8\pi\rho R^2,
\qquad
P=8\pi p_rR^2,
\qquad
Q=8\pi qR^2.
\]

For collapse let

\[
V=-U>0,
\]

and use the Misner-Sharp kinematic identity

\[
\Gamma^2=1+V^2-\mathcal C.
\]

For an outward comoving radial energy flux \(q>0\), the compactness evolution control becomes

\[
R D_T\mathcal C
=
V(\mathcal C+P)-Q\Gamma.
\]

Therefore nonincreasing compactness requires

\[
\boxed{
Q\ge Q_{\rm crit}
=
\frac{V(\mathcal C+P)}{\Gamma}
}.
\]

The event-horizon causal firewall remains explicit: this is an **internal redistribution condition for enclosed Misner-Sharp mass**, not a claim that energy generated inside a true event horizon escapes to future null infinity.

## Necessary radial NEC bound

In a local orthonormal frame, the radial \((\hat t,\hat r)\) stress-energy block with heat flux can be written schematically as

\[
T_{\hat a\hat b}
=
\begin{pmatrix}
\rho & q\\
q & p_r
\end{pmatrix}.
\]

For the two radial null directions, a necessary null-energy-condition bound is

\[
\rho+p_r\ge2|q|.
\]

In dimensionless variables,

\[
\boxed{
|Q|\le Q_{\rm NEC}
=
\frac{E+P}{2}
}.
\]

A separate necessary dominant-energy check from the comoving energy-current magnitude is

\[
|q|\le\rho,
\]

or

\[
|Q|\le E.
\]

This latter condition is only a necessary comoving DEC check; satisfying it does not prove the full DEC for all observers.

Hence a necessary local NEC-compatible de-compaction window is

\[
\boxed{
Q_{\rm crit}\le\frac{E+P}{2}
}.
\]

Equivalently,

\[
\frac{V}{\Gamma}
\le
\frac{E+P}{2(\mathcal C+P)}.
\]

## Synthetic homogeneous control

To make the dimensions consistent without identifying the BH-RB-021 normalized density with an arbitrary geometric radius, only the dimensionless pressure ratio

\[
w=\frac{p}{\varepsilon}
\]

is imported from the normalized microphysical sample.

At the BH-RB-020/021 sample

\[
mc^2=B=1,
\qquad
y=0.2,
\qquad n=0.5,
\]

one finds

\[
\varepsilon=0.401393202250,
\qquad
p=0.026393202250,
\]

and

\[
w=0.0657539841285.
\]

For a **synthetic uniform-density spherical control only**, use

\[
E=3\mathcal C,
\]

which follows from \(m=4\pi\rho R^3/3\), and set

\[
P=wE.
\]

At

\[
\mathcal C=1.2,
\]

this gives

\[
E=3.6,
\qquad
P=0.236714342862.
\]

This homogeneous relation is not asserted for a real successor core.

## Slow-collapse control

Take

\[
V=0.5.
\]

Then

\[
\Gamma=0.223606797750,
\]

and

\[
Q_{\rm crit}=3.212590934889.
\]

But the radial NEC allows at most

\[
Q_{\rm NEC}
=
\frac{E+P}{2}
=1.918357171431.
\]

Therefore

\[
Q_{\rm crit}>Q_{\rm NEC}.
\]

Even saturating the radial NEC leaves

\[
R D_T\mathcal C
=0.289399467387>0.
\]

Thus this particular slowly collapsing trapped control cannot reduce compactness through outward heat flux without violating the radial NEC.

Interestingly,

\[
Q_{\rm crit}<E=3.6,
\]

so the weaker comoving energy-current bound alone would not detect the obstruction. This demonstrates why the radial NEC gate must be kept separately.

## Critical collapse parameter

Define

\[
A_{\rm NEC}
=
\frac{E+P}{2(\mathcal C+P)}.
\]

For the synthetic control,

\[
A_{\rm NEC}=1.335239103696>1.
\]

Solving the equality

\[
Q_{\rm crit}=Q_{\rm NEC}
\]

gives

\[
\boxed{
V_{\rm crit}^2
=
\frac{A_{\rm NEC}^2(\mathcal C-1)}
{A_{\rm NEC}^2-1}
}.
\]

Numerically,

\[
V_{\rm crit}=0.674886945897.
\]

At that point,

\[
Q_{\rm crit}=Q_{\rm NEC}=1.918357171431
\]

and

\[
R D_T\mathcal C=0.
\]

## Faster-collapse control

For

\[
V=0.8,
\]

one finds

\[
\Gamma=0.663324958071,
\]

\[
Q_{\rm crit}=1.732742693162,
\]

which satisfies

\[
Q_{\rm crit}<Q_{\rm NEC}=1.918357171431
\]

and also

\[
Q_{\rm crit}<E=3.6.
\]

At radial-NEC saturation,

\[
R D_T\mathcal C
=-0.123122716015<0.
\]

Therefore the local algebra does **not** force NEC violation for every internal-flux de-compaction attempt.

## Interpretation

This result removes two opposite overstatements.

First, it is incorrect to claim

\[
\text{outward internal flux}
\Rightarrow
\text{energy-condition violation}
\]

in all trapped states.

Second, it is also incorrect to claim that the existence of a local NEC-compatible flux window produces a finite core.

The audit establishes only

\[
\boxed{
\text{some local trapped controls admit }
Q_{\rm crit}\text{ within necessary NEC bounds}
}
\]

while other controls do not.

The remaining missing object is a **constitutive transport law** that actually determines \(q\): e.g. causal dissipative transport, formation-transition energy redistribution, or another non-perfect-fluid closure.

Furthermore:

\[
\text{local }D_T\mathcal C<0
\not\Rightarrow
\mathcal C\le1\text{ is reached before }R\to0,
\]

and

\[
\mathcal C\le1
\not\Rightarrow
\text{global event horizon disappears}.
\]

Apparent/trapping structure and the global event horizon must remain distinguished.

## Audit result

The Python control gives

\[
\boxed{19/19\ \mathrm{PASS}}.
\]

Final verdict:

\[
\boxed{
\begin{aligned}
&\text{PASS\_WITH\_BOUNDARY /}\\
&\text{LOCAL\_NEC\_COMPATIBLE\_INTERNAL\_FLUX\_WINDOW\_EXISTS\_IN\_SYNTHETIC\_CONTROL /}\\
&\text{SLOW\_COLLAPSE\_CONTROL\_REQUIRES\_RADIAL\_NEC\_VIOLATION /}\\
&\text{NEC\_COMPATIBILITY\_IS\_NOT\_FULL\_DEC\_OR\_TRANSPORT\_CLOSURE /}\\
&\text{GLOBAL\_DETRAPPING\_AND\_POSITIVE\_RADIUS\_CORE\_NOT\_DERIVED}.
\end{aligned}
}
\]

## Next gate

BH-RB-025 should stop prescribing \(q\) by hand and test a causal transport closure. The minimum question is whether a finite relaxation-time dissipative law can dynamically generate

\[
Q\ge Q_{\rm crit}
\]

for long enough to drive \(\mathcal C\) from \(>1\) to \(\le1\), while respecting local energy-condition and causality constraints.

## External comparators

- L. Herrera and N. O. Santos, *Dynamics of dissipative gravitational collapse*, arXiv:gr-qc/0410014. Extends the Misner-Sharp approach to dissipative collapse and couples the dynamics to causal Israel-Stewart transport.
- C. W. Misner, *Relativistic Equations for Spherical Gravitational Collapse with Escaping Neutrinos*, Physical Review 137, B1360 (1965), DOI: 10.1103/PhysRev.137.B1360.
- The radial NEC inequality used here follows directly by contracting the local heat-flux stress-energy block with the two radial null vectors.

## Reproducibility

From the repository root:

```powershell
python audits/science/2026-09-15_dsd_gravity_heat_flux_energy_condition_gate.py --mode all
```
