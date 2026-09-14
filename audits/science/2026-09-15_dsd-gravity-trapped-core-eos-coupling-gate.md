# BH-RB-022 — Trapped-core EOS coupling gate

**Date:** 2026-09-15  
**Project:** DSD gravity rebaseline  
**Status:** `PASS_WITH_BOUNDARY`

## Question

Does the globally causal self-bound EOS family constructed in BH-RB-021, when coupled to standard spherically symmetric GR collapse, generate a finite positive black-hole-core turning radius without inserting \(R_{\min}\) by hand?

## Provenance boundary

This audit uses the DSD formation/property/QM work only to preserve the provenance of the successor-core state and of the constitutive closure. The gravitational dynamics used here are standard external GR in Misner-Sharp form. Therefore:

\[
\text{DSD successor-core record}
\rightarrow
\text{explicit matter/EOS bridge}
\rightarrow
\text{standard spherical GR}
\]

is the allowed chain.

The Misner-Sharp identities are not claimed to be derived from generic DSD.

## External GR control

In geometrized units \(G=c=1\), define

\[
U=D_T R,\qquad
\Gamma=D_rR,\qquad
\mathcal C=\frac{2m}{R}.
\]

The Misner-Sharp constraint is

\[
\Gamma^2=1+U^2-\frac{2m}{R}
=1+U^2-\mathcal C.
\]

For a regular real spherical fluid description, \(\Gamma^2\ge0\). Therefore

\[
U^2\ge \mathcal C-1.
\]

Under the usual spherical convention, \(\mathcal C=1\) is the marginal/apparent-horizon condition and \(\mathcal C>1\) is the trapped side.

Hence for \(\mathcal C>1\),

\[
|U|\ge \sqrt{\mathcal C-1}>0.
\]

A true material turning point requires \(U=0\), which implies

\[
\Gamma^2=1-\mathcal C\ge0
\quad\Rightarrow\quad
\boxed{\mathcal C\le1}.
\]

Thus

\[
\boxed{
\text{persistently trapped spherical shell}
\not\rightarrow
\text{finite-radius turning point while remaining trapped}.
}
\]

This statement is kinematic/geometric inside the specified Misner-Sharp branch and does not depend on how stiff the EOS is.

## Coupling the BH-RB-021 EOS

The BH-RB-020/021 low-density self-bound control is

\[
e(n)=mc^2-An+Bn^2,
\]

\[
\varepsilon(n)=mc^2n-An^2+Bn^3,
\]

\[
p(n)=-An^2+2Bn^3,
\]

with

\[
n_*=\frac{A}{2B},
\qquad
p(n_*)=0,
\]

and

\[
\varepsilon_0
=
\varepsilon(n_*)
=
\frac{A}{2B}
\left(
mc^2-\frac{A^2}{4B}
\right)>0.
\]

On the declared physical branch \(n\ge n_*\), pressure is nonnegative. BH-RB-021 replaces the acausal polynomial extrapolation at high density by a causal CSS completion, preserving nonnegative pressure.

For a comoving spherical perfect fluid without heat flux, the standard Misner-Sharp mass equation is

\[
D_Tm=-4\pi R^2pU.
\]

During collapse,

\[
U<0,\qquad p>0
\]

therefore

\[
\boxed{D_Tm>0}.
\]

Compression work increases the Misner-Sharp energy inside a comoving shell.

Now

\[
\mathcal C=\frac{2m}{R},
\]

so

\[
D_T\mathcal C
=
\frac{2D_Tm}{R}
-\frac{\mathcal C U}{R}.
\]

Using the no-flux perfect-fluid mass law gives

\[
D_T\mathcal C
=
-U
\left(
8\pi Rp+\frac{\mathcal C}{R}
\right).
\]

For

\[
U<0,\qquad p\ge0,\qquad \mathcal C>0,
\]

we obtain

\[
\boxed{D_T\mathcal C>0}.
\]

Therefore positive pressure can alter the acceleration through pressure gradients, but in this comoving no-flux branch it does not by itself reduce trapped compactness. In fact the compactness increases during continued collapse.

Even at a zero-pressure material surface \(p=0\),

\[
D_Tm=0
\]

but

\[
D_T\mathcal C
=
-\frac{\mathcal C U}{R}>0
\]

for \(U<0\).

## Proper-time contraction bound

If over an interval

\[
\mathcal C\ge1+\delta,
\qquad
\delta>0,
\]

then

\[
|U|\ge\sqrt{\delta}.
\]

For a collapsing shell,

\[
D_TR=U\le-\sqrt{\delta},
\]

so

\[
R(\tau)
\le
R(\tau_0)
-
\sqrt{\delta}\,(\tau-\tau_0).
\]

Therefore a shell cannot asymptote to a positive fixed radius while remaining a regular spherical shell with compactness bounded away from unity.

A finite positive lower radius requires at least one assumption of this branch to cease applying before the putative endpoint.

## Necessary decompaction condition

From

\[
D_T\mathcal C
=
\frac{2D_Tm}{R}
-\frac{\mathcal C U}{R},
\]

a collapsing shell \(U<0\) can satisfy

\[
D_T\mathcal C<0
\]

only if

\[
\boxed{
D_Tm
<
\frac{\mathcal C U}{2}
<0.
}
\]

Thus decompaction requires sufficiently strong loss/redistribution of Misner-Sharp mass-energy from the tracked comoving region.

The no-flux positive-pressure perfect-fluid law instead gives \(D_Tm\ge0\), so it cannot meet this condition.

## Consequence for the successor-core hypothesis

BH-RB-021 succeeded in constructing a globally causal self-bound EOS family with \(\varepsilon_0>0\). BH-RB-022 shows that this is not yet enough to produce a trapped finite-radius core.

The following implication is rejected:

\[
\boxed{
\text{self-binding}
+
\text{causal stiff pressure}
\not\Rightarrow
R_{\min}>0
\text{ inside a persistently trapped spherical branch}.
}
\]

The following escape channels are separated rather than merged:

1. **mass-energy flux / redistribution:** \(m\) must decrease sufficiently fast for the tracked region;
2. **marginalization / horizon retreat:** \(\mathcal C\to1\) before \(U\to0\);
3. **non-spherical rotating dynamics:** the exact spherical Misner-Sharp turning-point gate no longer directly applies;
4. **formation/lineage replacement:** the tracked comoving shell may cease to be the same physical support after a successor transition;
5. **new microphysics beyond the current perfect-fluid closure:** must be supplied explicitly and cannot be inferred from DSD property labels alone.

These are alternatives to be audited. None is established merely by this result.

## Numerical control

Using the normalized BH-RB-021 control

\[
mc^2=B=1,\qquad y=0.2
\]

gives

\[
n_*=0.447213595500,
\qquad
\varepsilon_0=0.357770876400,
\qquad
n_{\rm causal}=0.577350269190.
\]

At the midpoint of the low-density causal branch,

\[
n=0.512281932345,
\qquad
p=0.034152128823.
\]

For the synthetic shell control

\[
R=1,\qquad
U=-0.5,\qquad
\mathcal C=1.5,
\]

the perfect-fluid mass law gives

\[
D_Tm=0.214584154029>0,
\]

and hence

\[
D_T\mathcal C=1.179168308059>0.
\]

To make compactness decrease at the same \((\mathcal C,U)\), the general condition would instead require

\[
D_Tm<-0.375.
\]

This number is a normalized diagnostic only, not a black-hole-core prediction.

## Audit result

Python audit:

\[
\boxed{16/16\ \mathrm{PASS}}
\]

Verdict:

\[
\boxed{
\begin{aligned}
&\texttt{PASS\_WITH\_BOUNDARY /}\\
&\texttt{CAUSAL\_SELF\_BOUND\_EOS\_COUPLED\_TO\_SPHERICAL\_GR /}\\
&\texttt{PERSISTENTLY\_TRAPPED\_TURNING\_POINT\_EXCLUDED /}\\
&\texttt{NO\_FLUX\_POSITIVE\_PRESSURE\_DOES\_NOT\_GENERATE\_RMIN /}\\
&\texttt{DETRAPPING\_OR\_MASS\_FLUX\_OR\_NONSPHERICAL\_DYNAMICS\_REQUIRED /}\\
&\texttt{FINITE\_BLACK\_HOLE\_CORE\_RADIUS\_NOT\_DERIVED}.
\end{aligned}
}
\]

## External references

- Misner, C. W. & Sharp, D. H. (1964), *Relativistic Equations for Adiabatic, Spherically Symmetric Gravitational Collapse*, Physical Review 136, B571.
- Aurrekoetxea et al. (2025), *Cosmology using numerical relativity*, Living Reviews in Relativity. The review gives \(U=D_tR\), \(\Gamma=D_rR\), and \(\Gamma^2=1+U^2-2M/R\).
- Escrivà Mañas, A. (2021), *Numerical simulations of primordial black holes*, PhD thesis, Universitat de Barcelona. Chapter 4 states the standard Misner-Sharp perfect-fluid equations including \(D_tM=-4\pi R^2Up\).

## Next gate

**BH-RB-023 — mass-flux / marginalization gate**

Test whether an explicitly supplied outward flux or internal mass-energy redistribution can satisfy

\[
D_Tm<\frac{\mathcal C U}{2}
\]

early enough to drive

\[
\mathcal C>1\rightarrow\mathcal C\le1
\]

before the tracked support reaches zero areal radius, without violating causality, energy bookkeeping, or the DSD lineage/provenance firewall.
