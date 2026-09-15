# BH-RB-022 — Trapped-Region Self-Bound EOS Dynamic Closure Gate

**Date:** 2026-09-15  
**Project:** DSD gravity rebaseline  
**Status:** PASS_WITH_BOUNDARY

## Question

BH-RB-021 constructed a globally causal self-bound EOS family preserving a positive zero-pressure energy density \(\varepsilon_0>0\).

This gate asks a narrower dynamical question:

> Is that EOS, by itself, sufficient to generate a positive-radius turnaround \(R_{\min}>0\) for a spherically symmetric material core that is already inside a trapped region?

The answer is **no** for the no-flux perfect-fluid Misner-Sharp branch.

## External GR control

Use geometrized units \(G=c=1\).

For spherical Misner-Sharp dynamics,

\[
\Gamma^2=1+U^2-\frac{2m}{R},
\]

with

\[
U=D_T R,\qquad
\mathcal C=\frac{2m}{R}.
\]

Thus

\[
\Gamma^2=1+U^2-\mathcal C.
\]

A genuine material turning point has

\[
U=0,
\]

hence

\[
\Gamma^2=1-\mathcal C\ge0
\quad\Rightarrow\quad
\mathcal C\le1.
\]

Therefore a regular spherical shell cannot have a turnaround while remaining at

\[
\mathcal C>1.
\]

This is a kinematic constraint, independent of the detailed EOS.

For a no-flux perfect fluid, the Misner-Sharp mass evolution is

\[
D_Tm=-4\pi pUR^2.
\]

During collapse,

\[
U<0,
\]

and on the compressed self-bound branch,

\[
p>0,
\]

so

\[
D_Tm>0.
\]

For

\[
\mathcal C=\frac{2m}{R},
\]

one obtains

\[
D_T\mathcal C
=
-\frac{U}{R}
\left(
\mathcal C+8\pi pR^2
\right).
\]

Therefore

\[
U<0,\quad p\ge0,\quad\mathcal C>0
\quad\Rightarrow\quad
D_T\mathcal C>0.
\]

So positive pressure in the no-flux perfect-fluid branch does not drive an already trapped collapsing shell toward \(\mathcal C=1\); it makes its compactness increase.

## Relation to BH-RB-021

The BH-RB-020 low-density self-binding control was

\[
e(n)=mc^2-An+Bn^2,
\]

with

\[
p=-An^2+2Bn^3.
\]

The self-bound surface is

\[
n_*=\frac{A}{2B},
\]

and the causal cutoff of that low-density polynomial control is

\[
n_{\rm causal}=\sqrt{\frac{mc^2}{3B}}.
\]

For the normalized BH-RB-021 control

\[
mc^2=B=1,\qquad
y=\frac{A^2}{4Bmc^2}=0.2,
\]

the audit uses

\[
A=0.894427191000,
\]

\[
n_*=0.447213595500,
\]

\[
n_{\rm causal}=0.577350269190.
\]

At

\[
n=0.5,
\]

the branch gives

\[
\varepsilon=0.401393202250,
\]

\[
p=0.026393202250>0,
\]

and

\[
\frac{c_s^2}{c^2}
=
\frac{dp}{d\varepsilon}
=
0.707798100442<1.
\]

Thus the sample is inside the previously admitted causal self-bound region.

## Trapped-shell control

Take the dimensionless spherical control

\[
R=1,\qquad
\mathcal C=1.2,\qquad
U=-0.5.
\]

Then

\[
\Gamma^2
=
1+U^2-\mathcal C
=
0.05,
\]

so

\[
\Gamma=0.223606797750
\]

is real.

The no-flux mass evolution is

\[
D_Tm
=
0.165833380587>0,
\]

and

\[
D_T\mathcal C
=
0.931666761174>0.
\]

Therefore the globally causal self-bound EOS does not by itself produce de-trapping or a positive-radius turning point once this control shell is already trapped and collapsing.

## Dissipative extension gate

For a spherical dissipative control with outward comoving energy flux \(q\),

\[
D_Tm
=
-4\pi R^2(pU+q\Gamma).
\]

Then

\[
D_T\mathcal C
=
-8\pi R(pU+q\Gamma)
-
\frac{\mathcal C U}{R}.
\]

During collapse define \(V=-U>0\).

The condition

\[
D_T\mathcal C\le0
\]

requires

\[
q\Gamma
\ge
V
\left(
p+\frac{\mathcal C}{8\pi R^2}
\right).
\]

Hence

\[
\boxed{
q_{\rm crit}
=
\frac{-U}{\Gamma}
\left(
p+\frac{\mathcal C}{8\pi R^2}
\right)
}
\]

is the local threshold for nonincreasing compactness in this simplified dissipative spherical control.

For the numerical control,

\[
q_{\rm crit}
=
0.165781375888.
\]

The script verifies

\[
D_T\mathcal C(q=q_{\rm crit})=0,
\]

and

\[
D_T\mathcal C(q=1.1q_{\rm crit})
=
-0.093166676117<0.
\]

This does **not** mean that energy escapes from inside a true event horizon to infinity.

It means that an internal outward energy-transport channel can, in principle, reduce the Misner-Sharp mass enclosed by a given comoving shell.

External causal escape and internal redistribution remain distinct questions.

## Negative-pressure control

With no flux,

\[
D_T\mathcal C\le0
\]

during collapse would require

\[
p
\le
-\frac{\mathcal C}{8\pi R^2}.
\]

For the numerical control,

\[
p_{\rm crit}
=
-0.047746482928.
\]

The BH-RB-021 self-bound positive-pressure branch does not satisfy this condition.

Therefore tension/negative radial pressure would be a genuinely different constitutive branch, not a consequence of the present EOS.

## Result

The audit gives

\[
\boxed{16/16\ \mathrm{PASS}}.
\]

Final verdict:

\[
\boxed{
\begin{aligned}
&\text{PASS\_WITH\_BOUNDARY /}\\
&\text{SELF\_BOUND\_CAUSAL\_EOS\_DOES\_NOT\_BY\_ITSELF\_PRODUCE\_TRAPPED\_REGION\_TURNAROUND /}\\
&\text{OUTWARD\_FLUX\_OR\_OTHER\_NONPERFECT\_DYNAMIC\_CHANNEL\_REQUIRED /}\\
&\text{POSITIVE\_RADIUS\_CORE\_NOT\_YET\_DERIVED}.
\end{aligned}
}
\]

## Interpretation

BH-RB-021 solved one problem:

\[
\text{self-binding}
+
\text{global EOS causality}.
\]

BH-RB-022 shows that this is still not enough for

\[
R_{\min}>0
\]

inside a trapped region.

The remaining closure cannot be supplied by positive isotropic pressure alone.

At least one additional branch must be audited:

1. internal outward energy/enthalpy flux;
2. anisotropic stress or radial tension;
3. rotation/non-spherical dynamics;
4. formation-transition energy redistribution;
5. a different global causal structure.

The next recommended audit is therefore a **dissipative/internal-transport successor-core gate**, keeping the event-horizon causal firewall explicit.

## External references

- C. W. Misner, "Relativistic Equations for Spherical Gravitational Collapse with Escaping Neutrinos," *Physical Review* **137**, B1360 (1965), DOI: 10.1103/PhysRev.137.B1360.
- S. A. Hayward, "Gravitational energy in spherical symmetry," *Physical Review D* **53**, 1938 (1996), DOI: 10.1103/PhysRevD.53.1938.
- Modern Misner-Sharp formulations retain
  \[
  \Gamma^2=1+U^2-\frac{2m}{R}
  \]
  and, with radial flux, a mass-evolution term of the form
  \[
  D_Tm=-4\pi R^2(p_rU+q\Gamma)
  \]
  in the corresponding comoving conventions.

## Reproducibility

From the repository root:

```powershell
python audits/science/2026-09-15_dsd_gravity_trapped_region_self_bound_dynamic_gate.py --mode all
```
