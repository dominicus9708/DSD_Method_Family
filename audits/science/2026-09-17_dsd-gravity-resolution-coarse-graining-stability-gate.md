# BH-GC-005 — Resolution / Coarse-Graining Stability Gravitational-Core Gate

**Date:** 2026-09-17  
**Project:** DSD gravity rebaseline  
**Branch:** side audit; does **not** replace canonical BH-RB-025 finite-relaxation transport audit  
**Status:** PASS_WITH_BOUNDARY

## Question

BH-GC-004 reduced dependence on one superlevel threshold by using the full threshold filtration, but a second ambiguity remains: the descriptor itself may change when spatial resolution or coarse-graining changes.

BH-GC-005 therefore asks whether an apparent gravitational-core split or merger can be distinguished from a split or merger caused only by the observation/coarse-graining map.

The required firewall is

\[
\boxed{
\text{physical split/merger}
\neq
\text{resolution-induced split/merger}.
}
\]

## 1. Resolution-indexed descriptor

Let the underlying descriptor at fixed physical state and fixed flow/slice choice be \(\mathcal T_u(x)\).  Introduce an explicit coarse-graining scale \(\ell\) through a normalized Gaussian kernel \(G_\ell\):

\[
\boxed{
\mathcal T_u^{(\ell)}
=
G_\ell * \mathcal T_u.
}
\]

The map

\[
\mathcal R_{\ell_1\to\ell_2}:
\mathcal T_u^{(\ell_1)}
\mapsto
\mathcal T_u^{(\ell_2)}
\]

is a **resolution map**, not a physical time-evolution map.

Therefore a change in connected-component count under \(\ell\) alone must not be recorded as material lineage.

## 2. Analytic Gaussian control

Use a deliberately non-black-hole 1D equal-peak control with intrinsic width \(\sigma_0\) and centers at \(\pm d\):

\[
\mathcal T(x)
=
\exp\!\left[-\frac{(x-d)^2}{2\sigma_0^2}\right]
+
\exp\!\left[-\frac{(x+d)^2}{2\sigma_0^2}\right].
\]

Gaussian coarse-graining preserves the Gaussian form and changes the common width to

\[
\boxed{
\sigma_{\rm eff}(\ell)
=
\sqrt{\sigma_0^2+\ell^2}.
}
\]

For two equal Gaussians, the midpoint \(x=0\) changes from a local minimum to a local maximum at

\[
d=\sigma_{\rm eff}.
\]

Hence, for fixed physical separation \(d>\sigma_0\), the exact resolution-induced merger scale is

\[
\boxed{
\ell_{\rm crit}
=
\sqrt{d^2-\sigma_0^2}.
}
\]

With

\[
\sigma_0=0.8,
\qquad
 d=2,
\]

this gives

\[
\boxed{
\ell_{\rm crit}
\approx1.833030278.
}
\]

The numerical scan brackets the transition:

\[
\ell=1.82\Rightarrow 2\text{ maxima},
\qquad
\ell=1.84\Rightarrow 1\text{ maximum}.
\]

The physical descriptor was unchanged.  Only the coarse-graining scale changed.

Thus

\[
\boxed{
\text{two descriptor cores}
\rightarrow
\text{one observed descriptor core}
}
\]

can occur **without any physical merger**.

## 3. Persistence also collapses under sufficient coarse-graining

At fixed physical separation \(d=2\), the secondary 0D superlevel persistence decreases with increasing \(\ell\):

\[
\begin{array}{c|c|c}
\ell & N_{\rm max} & \Pi_{\rm secondary}\\
\hline
0.0 & 2 & 0.91212646\\
1.0 & 2 & 0.41389064\\
1.5 & 2 & 0.07213474\\
1.8 & 2 & 0.00069140\\
1.82 & 2 & 0.00010722\\
1.84 & 1 & 0
\end{array}
\]

So threshold persistence by itself does not remove resolution dependence.

The correct statement is

\[
\boxed{
\text{threshold persistence}
\neq
\text{resolution invariance}.
}
\]

## 4. Physical merger at fixed resolution

Now hold the observation scale fixed at

\[
\ell=0.4.
\]

The effective width is

\[
\sigma_{\rm eff}
=
\sqrt{0.8^2+0.4^2}
=
0.894427191.
\]

Therefore physical motion of the two centers gives a merger threshold

\[
\boxed{
 d_{\rm crit}
 =0.894427191.
}
\]

The numerical control gives

\[
 d=0.90\Rightarrow 2\text{ maxima},
\qquad
 d=0.88\Rightarrow 1\text{ maximum}.
\]

Thus an actual change in physical separation at fixed resolution can also generate the same topology change.

## 5. Topological degeneracy at one resolution

Two distinct histories can therefore produce the same one-core observation:

\[
\boxed{
(d,\ell)=(0.75,0.4)
\Rightarrow
1\text{ observed core},
}
\]

while

\[
\boxed{
(d,\ell)=(2.0,2.2)
\Rightarrow
1\text{ observed core}.
}
\]

The first is a physical approach at fixed good resolution; the second is a resolution-induced merger with unchanged physical separation.

Hence

\[
\boxed{
N_{\rm core}=1
\text{ at one resolution does not identify how that state arose.}
}
\]

This directly blocks the inference

\[
\text{observed descriptor merger}
\Rightarrow
\text{physical material merger}.
\]

## 6. Sampling-grid stability

Coarse-graining scale \(\ell\) and numerical sampling interval \(\Delta x\) are different provenance variables.

For an asymmetric two-feature control with physical separation \(d=2\), blur \(\ell=0.4\), and amplitudes \(1:0.35\), the descriptor remained two-peaked for

\[
\Delta x
\in
\{0.002,0.005,0.01,0.02,0.04,0.08\}.
\]

The reference finite persistence was

\[
\Pi_{\rm ref}
\approx0.2562073813.
\]

At the coarsest tested grid, the relative persistence error was only

\[
\boxed{
5.93\times10^{-4}
\approx0.0593\%.
}
\]

Thus this control has a nontrivial range in which ordinary grid coarsening does not change the inferred core count or materially change persistence.

This does **not** establish a universal acceptable \(\Delta x\).  It only demonstrates how a numerical resolution-stability audit can be performed.

## 7. DSD lineage refinement

The descriptor-lineage vocabulary must now separate resolution transformation from physical or descriptor-time succession.

Keep

\[
\Lambda_{\rm mat},
\quad
\Lambda_{\rm sig},
\quad
\Lambda_{\rm desc},
\quad
\Lambda_{\rm dom},
\quad
\Lambda_{\rm reg},
\quad
\Lambda_{\rm pers},
\]

and add

\[
\boxed{
\mathcal R_{\ell_1\to\ell_2}
:
\text{resolution/coarse-graining transformation}.
}
\]

The firewall is

\[
\boxed{
\mathcal R_{\ell_1\to\ell_2}
\neq
\Lambda_{\rm mat}
\neq
\Lambda_{\rm sig}.
}
\]

A component merger caused only by \(\mathcal R\) is not a physical merger event.

## 8. Required provenance

A gravitational-core descriptor now needs at least

\[
\boxed{
(
 u,
 \Sigma_\tau,
 \mathcal T_u,
 \text{normalization},
 \lambda/\text{filtration rule},
 \ell,
 \Delta x,
 \text{sampling/interpolation rule}
).
}
\]

In particular, \(\ell\) and \(\Delta x\) must not be hidden.

The existence of a core feature should be reported together with the interval of resolution scales over which it remains stable.

## 9. Firewalls

The following implications remain forbidden:

\[
\text{stable over one tested resolution range}
\not\Rightarrow
\text{resolution invariant at all scales},
\]

\[
\text{observed one-core topology}
\not\Rightarrow
\text{physical one-core ontology},
\]

\[
\text{resolution-induced merger}
\not\Rightarrow
\text{material/energy merger},
\]

\[
\text{control }\ell_{\rm crit}
\not\Rightarrow
\text{physical black-hole core scale}.
\]

## 10. Result

Python audit: **21/21 PASS**.

**Verdict:**

`PASS_WITH_BOUNDARY / CORE_DESCRIPTOR_IS_STABLE_OVER_A_FINITE_RESOLUTION_RANGE_IN_CONTROL / SUFFICIENT_COARSE_GRAINING_CAN_MERGE_DISTINCT_DESCRIPTOR_CORES_WITHOUT_PHYSICAL_MERGER / PHYSICAL_AND_RESOLUTION_INDUCED_MERGERS_ARE_TOPOLOGICALLY_DEGENERATE_AT_ONE_RESOLUTION / RESOLUTION_AND_SAMPLING_PROVENANCE_ARE_REQUIRED / NO_UNIQUE_PHYSICAL_RESOLUTION_OR_BLACK_HOLE_CORE_MULTIPLICITY_DERIVED`

## 11. Next side audit — BH-GC-006

A single threshold filtration still depends on one resolution scale, while BH-GC-005 shows that a single resolution can hide or merge features.

The next side audit should therefore study the two-parameter family

\[
\boxed{
\mathcal K_{u,\lambda,\ell}(\tau)
=
\{x:(G_\ell*\mathcal T_u)(x,\tau)\ge\lambda\}
}
\]

and distinguish features that persist over both a nontrivial threshold interval and a nontrivial resolution interval.

The target is a **threshold-resolution bifiltration** or equivalent multi-resolution persistence descriptor, while retaining the firewall that such a structural feature is not automatically a material black-hole core.
