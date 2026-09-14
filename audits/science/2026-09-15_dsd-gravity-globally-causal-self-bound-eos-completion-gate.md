# BH-RB-021 — Globally causal self-bound EOS completion gate

**Date:** 2026-09-15  
**Status:** `PASS_WITH_BOUNDARY / GLOBALLY_CAUSAL_SELF_BOUND_EOS_FAMILY_CONSTRUCTED / THERMODYNAMIC_MATCHING_PRESERVES_N_AND_MU / EPSILON0_SURVIVES_CAUSAL_COMPLETION / MICROPHYSICAL_HIGH_DENSITY_BRANCH_NOT_DERIVED / BLACK_HOLE_CORE_RADIUS_NOT_YET_DERIVED`

## Scope

BH-RB-020 produced a finite-density self-binding scale from the local toy closure

\[
e(n)=mc^2-An+Bn^2,
\qquad A>0,\ B>0,
\]

where \(e=\varepsilon/n\) is energy per constituent.

That closure is useful near its saturation point but becomes acausal if extrapolated indefinitely to high density. This audit asks a narrower question:

> Can the BH-RB-020 self-bound branch be extended to arbitrarily high density while preserving thermodynamic consistency and \(0\le dp/d\varepsilon\le1\), without replacing the already-derived positive zero-pressure density \(\varepsilon_0\)?

The answer is yes at the phenomenological EOS-family level.

This does **not** derive the microscopic successor-core Hamiltonian, prove a trapped finite core, or determine a black-hole-core radius.

## Low-density self-bound branch retained from BH-RB-020

The zero-temperature relations are

\[
\varepsilon(n)=n e(n)
=mc^2n-An^2+Bn^3,
\]

\[
p(n)=n^2\frac{de}{dn}
=-An^2+2Bn^3,
\]

\[
\mu(n)=\frac{d\varepsilon}{dn}
=mc^2-2An+3Bn^2,
\]

and therefore

\[
\boxed{\varepsilon+p=n\mu}.
\]

The self-bound saturation density is

\[
\boxed{n_*=\frac{A}{2B}},
\]

with

\[
p(n_*)=0.
\]

Defining

\[
y:=\frac{A^2}{4Bmc^2},
\]

the surface energy per constituent and surface energy density are

\[
e_*=mc^2(1-y),
\]

\[
\boxed{
\varepsilon_0
=
\varepsilon(n_*)
=
\frac{A}{2B}
\left(
mc^2-\frac{A^2}{4B}
\right).
}
\]

The BH-RB-020 local causal condition is

\[
0<y\le\frac13.
\]

## Exact causal endpoint of the local polynomial branch

The adiabatic sound-speed ratio is

\[
\frac{c_s^2}{c^2}
=
\frac{dp}{d\varepsilon}
=
\frac{-2An+6Bn^2}
{mc^2-2An+3Bn^2}.
\]

Setting the ratio equal to one cancels the attractive coefficient \(A\) and gives

\[
\boxed{
n_{\rm causal}
=
\sqrt{\frac{mc^2}{3B}}.
}
\]

For \(0<y\le1/3\),

\[
n_*\le n_{\rm causal}.
\]

On the physical self-bound interval

\[
n_*\le n\le n_{\rm causal},
\]

the branch is mechanically stable and causal:

\[
0\le \frac{dp}{d\varepsilon}\le1.
\]

The dominant-energy inequality is also explicit there:

\[
\varepsilon-p
=
n(mc^2-Bn^2)>0,
\]

because \(Bn^2\le mc^2/3\).

Thus the BH-RB-020 branch has a finite, well-defined causal domain rather than being discarded entirely.

## Thermodynamically matched constant-sound-speed completion

Choose any matching density

\[
n_m\in[n_*,n_{\rm causal}],
\]

and define the low-branch values

\[
\varepsilon_m=\varepsilon(n_m),\qquad
p_m=p(n_m),\qquad
\mu_m=\mu(n_m).
\]

Let

\[
s_m
:=
\left.\frac{dp}{d\varepsilon}\right|_{n_m},
\qquad
0\le s_m\le1.
\]

For higher density define a constant-sound-speed branch

\[
\boxed{
p
=
p_m+s_m(\varepsilon-\varepsilon_m).
}
\]

This is the standard constant-sound-speed type of high-density parametrization, here used only as a causal completion device.

At \(T=0\),

\[
d\varepsilon=\mu\,dn,
\qquad
\varepsilon+p=n\mu.
\]

Using the linear high-density branch gives

\[
\frac{dn}{n}
=
\frac{d\varepsilon}{\varepsilon+p}.
\]

Integration with the matching condition at \(n=n_m\) yields

\[
\boxed{
\varepsilon+p
=
(\varepsilon_m+p_m)
\left(\frac{n}{n_m}\right)^{1+s_m}.
}
\]

Hence

\[
\boxed{
\mu(n)
=
\mu_m
\left(\frac{n}{n_m}\right)^{s_m}.
}
\]

Writing

\[
D_m:=\varepsilon_m+p_m,
\qquad
C_m:=p_m-s_m\varepsilon_m,
\qquad
z:=\frac{n}{n_m},
\]

the completed high-density branch is

\[
\boxed{
\varepsilon(z)
=
\frac{D_m z^{1+s_m}-C_m}{1+s_m},
}
\]

\[
\boxed{
p(z)
=
\frac{s_m D_m z^{1+s_m}+C_m}{1+s_m}.
}
\]

At \(z=1\), all four thermodynamic quantities match:

\[
\varepsilon\to\varepsilon_m,\qquad
p\to p_m,\qquad
n\to n_m,\qquad
\mu\to\mu_m.
\]

Because the high-density slope is chosen as the low-density sound speed at the matching point,

\[
\left(\frac{dp}{d\varepsilon}\right)_{\rm low,m}
=
\left(\frac{dp}{d\varepsilon}\right)_{\rm high,m}
=s_m,
\]

so \(p(\varepsilon)\) is also \(C^1\) at the match.

## Canonical maximal-causal envelope

A particularly economical choice is to keep the BH-RB-020 polynomial until the point where it first reaches the causal bound:

\[
n_m=n_{\rm causal},
\qquad
s_m=1.
\]

This introduces no new dimensionful matching scale because

\[
n_m
=
\sqrt{\frac{mc^2}{3B}}
\]

is already fixed by the BH-RB-020 coefficients.

The high-density branch becomes

\[
p=p_m+(\varepsilon-\varepsilon_m).
\]

Equivalently,

\[
\frac{dp}{d\varepsilon}=1
\]

for all densities above the match.

This is the maximally stiff causal envelope. It should not be mistaken for a microscopic prediction that the real successor phase has exactly luminal sound speed.

If strict subluminality is preferred, one may instead choose

\[
n_m<n_{\rm causal},
\]

so that

\[
0<s_m<1,
\]

and the same thermodynamic construction yields a globally subluminal constant-sound-speed continuation.

## The self-bound \(\varepsilon_0\) survives the high-density completion

The physical zero-pressure boundary remains

\[
n=n_*,
\qquad
p(n_*)=0,
\]

with

\[
\boxed{
\varepsilon_0
=
\frac{A}{2B}
\left(
mc^2-\frac{A^2}{4B}
\right)>0.
}
\]

The linear high-density segment, if algebraically extrapolated below its declared matching domain, may possess a different zero-pressure intercept. That extrapolated intercept is **not** the material surface and must not be renamed as \(\varepsilon_0\).

Therefore

\[
\boxed{
\text{causal high-density completion}
\not\Rightarrow
\text{loss or replacement of the derived self-binding scale}.
}
\]

This is the key closure result of BH-RB-021.

## Stability and energy-condition control

The high-density branch has

\[
\frac{dp}{d\varepsilon}=s_m,
\qquad
0\le s_m\le1.
\]

Thus it is causal by construction.

Because

\[
\mu(n)
=
\mu_m
\left(\frac{n}{n_m}\right)^{s_m}>0,
\]

it is mechanically/thermodynamically well oriented on the audited branch.

If

\[
p_m\le\varepsilon_m
\]

at the match, then for \(s_m\le1\)

\[
p-\varepsilon
\]

cannot increase with increasing \(\varepsilon\). Hence

\[
0\le p\le\varepsilon
\]

is preserved throughout the completed high-density branch.

The script checks these relations numerically for both the maximal \(s_m=1\) envelope and a strictly subluminal matched example.

## Standard-physics provenance

The thermodynamic identities used here are standard relativistic-fluid thermodynamics, not DSD-native gravity laws.

For an extensive one-component fluid,

\[
p+\varepsilon=Ts+\mu n,
\]

and at zero temperature,

\[
p+\varepsilon=\mu n,
\qquad
d\varepsilon=\mu\,dn.
\]

The causal-limit logic also has a standard compact-star precedent: Rhoades and Ruffini used relativity, causality, and stability to bound unknown high-density equations of state.

Constant-sound-speed parametrizations are likewise standard tools for representing high-density phases.

In this audit those ingredients remain external physical comparators/specializations. DSD contributes the provenance and formation/property separation; it does not relabel the external thermodynamics or causal EOS as a generic DSD theorem.

## DSD interpretation

The admissible chain is now

\[
F_{\rm core}
\to
(m,A,B,\ldots)_{\rm typed}
\to
\varepsilon(n),p(n),\mu(n)
\to
\varepsilon_0
\to
\text{causal completion}
\to
T_{\mu\nu}.
\]

The formation threshold remains distinct from the self-bound saturation point:

\[
n_{\rm form}
\neq_{\rm automatically}
n_*.
\]

Likewise the completed EOS does not prove that the successor formation exists in nature.

The important result is narrower:

\[
\boxed{
\text{a positive self-binding scale generated below the causal cutoff can be retained in a globally causal thermodynamic EOS family}.
}
\]

This removes the specific BH-RB-020 failure mode in which the local polynomial became acausal at sufficiently high density.

## What is still not derived

BH-RB-021 does not determine:

1. the microscopic Hamiltonian or field theory that fixes \(m,A,B\);
2. the actual high-density sound-speed function of the successor phase;
3. dissipative transport, viscosity, heat flux, shear response, or reaction rates;
4. a formation-transition threshold \(n_{\rm form}\);
5. a trapped-region equilibrium or persistent dynamical core;
6. a unique \(R_{\min}\).

The high-density CSS segment is a **causal envelope/completion**, not the claimed black-hole-core microphysics.

## Result

The audit script reports **17/17 PASS**.

For the normalized control

\[
mc^2=B=1,\qquad y=0.2,
\]

it gives

\[
n_*=0.447213595500,
\qquad
\varepsilon_0=0.357770876400,
\]

\[
n_{\rm causal}=0.577350269190.
\]

At the canonical maximal-causal match,

\[
\varepsilon_m=0.471657961920,
\qquad
p_m=0.086757782460,
\qquad
\mu_m=0.967204441011,
\]

and both the low and high branches have

\[
\left.\frac{dp}{d\varepsilon}\right|_m=1.
\]

A strictly subluminal example matched earlier gives

\[
\frac{dp}{d\varepsilon}\simeq0.755768136641.
\]

## Verdict

\[
\boxed{
\text{PASS\_WITH\_BOUNDARY /
GLOBALLY\_CAUSAL\_SELF\_BOUND\_EOS\_FAMILY\_CONSTRUCTED /
THERMODYNAMIC\_MATCHING\_PRESERVES\_N\_AND\_MU /
EPSILON0\_SURVIVES\_CAUSAL\_COMPLETION /
MICROPHYSICAL\_HIGH\_DENSITY\_BRANCH\_NOT\_DERIVED /
BLACK\_HOLE\_CORE\_RADIUS\_NOT\_YET\_DERIVED}
}
\]

## Reproducibility

```powershell
python audits/science/2026-09-15_dsd_gravity_globally_causal_self_bound_eos_completion_gate.py --mode all
```

## External comparators

- C. E. Rhoades Jr. and R. Ruffini, *Maximum Mass of a Neutron Star*, Physical Review Letters **32**, 324 (1974), DOI: `10.1103/PhysRevLett.32.324`.
- N. Andersson and G. L. Comer, *Relativistic fluid dynamics: physics for many different scales*, Living Reviews in Relativity **24** (2021), DOI: `10.1007/s41114-021-00031-6`.
- M. G. Alford, G. F. Burgio, S. Han, G. Taranto, and D. Zappalà, *Constraining and applying a generic high-density equation of state*, arXiv:`1501.07902`.

## Next gate

BH-RB-022 should no longer spend effort repairing the local EOS.

The next question is dynamical:

\[
\boxed{
\text{Does a collapsing GR configuration supplied with this globally causal self-bound constitutive family ever acquire a positive dynamical radius floor without inserting }R_{\min}\text{ by hand?}
}
\]

That requires coupling the EOS to the trapped-region evolution/flux constraints already isolated in BH-RB-009 through BH-RB-011, while preserving the firewall

\[
\text{matter-radius response}
\neq
\text{trapped-to-untrapped null defocusing}.
\]
