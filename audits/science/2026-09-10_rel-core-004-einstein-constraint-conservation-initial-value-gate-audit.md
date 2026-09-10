# REL Core 004 — Einstein Field Equation / Constraint / Conservation / Initial-Value Gate

Date: 2026-09-10  
Status: **PASS_WITH_BOUNDARY**  
Program: **Core-Theory Reconstruction Challenge — Standard Relativity Track**

## 1. Purpose

REL Core 002 separated Lorentzian metric admission from causal/differential geometry, and REL Core 003 separated coordinate acceleration, covariant acceleration, geodesic motion, transport, and curvature response.

REL Core 004 crosses the next boundary:

```text
supplied Lorentzian geometry
-> Einstein tensor
-> supplied Einstein field equation
-> constraint projections
-> supplied matter closure
-> admissible Cauchy data
-> standard Cauchy development theorem
```

The central firewall is

\[
\boxed{
\text{metric geometry}
\neq
\text{Einstein-equation satisfaction}
\neq
\text{constraint satisfaction}
\neq
\text{full evolution}
\neq
\text{matter closure}
\neq
\text{global development theorem}.
}
\]

No DSD-native gravity law is inferred from this gate.

---

## 2. Provenance lock

The REL Core 001R classes remain:

```text
R0  PRE_EXISTING_DSD
R1  GENERAL_MATHEMATICAL_STRUCTURAL
R2  RELATIVITY_SPECIALIZATION
R3  STANDARD_THEOREM_CONSEQUENCE
R4  REMAINS_EXTERNAL_NOT_DERIVED
```

For this gate:

```text
R0:
  typed identity/status/applicability
  explicit bridge discipline
  state/relation/transition separation
  support/readout/reconstruction discipline
  regular-epoch/transition separation

R1:
  relation satisfaction is not implied by operand existence
  projected constraints do not generally recover a stronger full relation
  one-slice data do not select an evolution law without a supplied law
  equal reduced records do not imply equal extensions without uniqueness/injectivity

R2:
  Lorentzian metric and Levi-Civita geometry
  Einstein field equation
  coupling constants and cosmological constant when used
  stress-energy model
  3+1 split / hypersurface structure
  matter closure equations
  constraint-satisfying initial data
  gauge/reduction assumptions used for the PDE formulation
  boundary/asymptotic conditions when required

R3:
  Einstein tensor from supplied metric
  contracted Bianchi identity
  covariant stress-energy conservation from EFE + Bianchi + metric compatibility
  Hamiltonian and momentum constraints as projections of EFE
  standard local/global Cauchy-development results
  maximal globally hyperbolic development under theorem hypotheses

R4:
  why Einstein dynamics is physically selected
  why the gravitational coupling has its observed value
  actual matter model of the world
  actual global topology / boundary / asymptotic data
  DSD-native derivation of the Einstein equation
  unique quantum-gravity cross-dynamics
```

A theorem consequence in R3 does not retroactively move its R2 premises into R0/R1.

---

## 3. Standard-relativity source lock

The standard comparison layer was checked against:

1. Sean M. Carroll, *Lecture Notes on General Relativity*, arXiv:gr-qc/9712019.
2. Éric Gourgoulhon, *3+1 Formalism and Bases of Numerical Relativity*, arXiv:gr-qc/0703035.
3. Y. Choquet-Bruhat and R. Geroch, *Global aspects of the Cauchy problem in general relativity*, Commun. Math. Phys. 14 (1969), 329–335.
4. J. Sbierski, *On the Existence of a Maximal Cauchy Development for the Einstein Equations — a Dezornification*, arXiv:1309.7591.

These are external standard-relativity sources. Their results are not counted as DSD-derived structure.

---

## 4. Geometry does not imply field-equation satisfaction

With \(c=1\),

\[
G_{\mu\nu}=R_{\mu\nu}-\frac12 Rg_{\mu\nu}.
\]

The Einstein equation with cosmological constant is

\[
\boxed{
G_{\mu\nu}+\Lambda g_{\mu\nu}=\kappa T_{\mu\nu},
\qquad \kappa=8\pi G.
}
\]

Once a smooth Lorentzian metric is supplied, its Einstein tensor is a geometric construction. The existence of \(G_{\mu\nu}\) does not imply that a supplied \(T_{\mu\nu}\) satisfies the field equation.

### Finite witness

Use Cartesian Minkowski spacetime with

\[
G_{\mu\nu}=0,
\qquad \Lambda=0,
\qquad \kappa=1.
\]

Supply the constant tensor

\[
T_{\mu\nu}=\operatorname{diag}(1,0,0,0).
\]

Its covariant divergence vanishes in Cartesian Minkowski coordinates, but

\[
G_{\mu\nu}-T_{\mu\nu}=-T_{\mu\nu}\neq0.
\]

Therefore

\[
\boxed{
\nabla_\mu T^{\mu\nu}=0
\not\Rightarrow
G_{\mu\nu}=\kappa T_{\mu\nu}.
}
\]

This blocks the shortcut `conservation -> Einstein equation`.

---

## 5. Contracted Bianchi identity and conservation

For the Levi-Civita connection,

\[
\boxed{\nabla_\mu G^{\mu\nu}=0}
\]

is the contracted Bianchi identity.

If

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}=\kappa T_{\mu\nu}
\]

is supplied, with constant \(\Lambda,\kappa\) and metric compatibility, then

\[
\boxed{\nabla_\mu T^{\mu\nu}=0.}
\]

The audited implication is

```text
EFE
+ contracted Bianchi identity
+ metric compatibility
+ constant couplings
-> covariant stress-energy conservation
```

and not the reverse.

### FLRW consistency witness

In flat FLRW with \(\kappa=1\), use dust

\[
a(t)=t^{2/3},\qquad
H=\frac{2}{3t},\qquad
\rho=\frac{4}{3t^2},\qquad p=0.
\]

Then

\[
3H^2=\rho,
\]

\[
2\dot H+3H^2=-p,
\]

and

\[
\dot\rho+3H(\rho+p)=0.
\]

The reproducibility script checks these identities at a sample \(t>0\). This is a special-case consistency witness, not a numerical proof of the general Bianchi theorem.

---

## 6. Constraint gate

For a spacelike hypersurface with induced metric \(h_{ij}\), extrinsic curvature \(K_{ij}\), spatial scalar curvature \(R^{(3)}\), normal energy density \(\rho\), and momentum density \(j^i\), a standard convention gives

\[
R^{(3)}+K^2-K_{ij}K^{ij}=16\pi G\,\rho+2\Lambda,
\]

\[
D_j(K^{ij}-h^{ij}K)=8\pi G\,j^i.
\]

In \(\kappa=8\pi G=1\), \(\Lambda=0\), the Hamiltonian equation becomes

\[
R^{(3)}+K^2-K_{ij}K^{ij}=2\rho.
\]

### Isotropic flat-slice witness

Take

\[
h_{ij}=\delta_{ij},\qquad K_{ij}=Hh_{ij}
\]

with constant \(H\). Then

\[
R^{(3)}=0,\qquad K=3H,\qquad K_{ij}K^{ij}=3H^2,
\]

so

\[
R^{(3)}+K^2-K_{ij}K^{ij}=6H^2.
\]

For \(H\neq0\), vacuum data fail the Hamiltonian constraint. With

\[
\rho=3H^2
\]

in the \(\kappa=1\) convention, the Hamiltonian constraint is satisfied. Constant isotropic \(K_{ij}\) with \(j^i=0\) also satisfies the momentum constraint.

Thus

\[
\boxed{(h_{ij},K_{ij})\text{ as typed data}\not\Rightarrow\text{admissible Einstein initial data}.}
\]

---

## 7. Constraints do not replace evolution equations

Use two flat-FLRW extensions:

\[
a_1(t)=1,
\]

\[
a_2(t)=1+\varepsilon t^2,\qquad \varepsilon>0.
\]

At \(t=0\),

\[
a_1=a_2=1,\qquad \dot a_1=\dot a_2=0.
\]

They therefore induce the same spatial metric and the same extrinsic curvature on the initial slice:

\[
h_{ij}^{(1)}=h_{ij}^{(2)},\qquad K_{ij}^{(1)}=K_{ij}^{(2)}=0.
\]

Both satisfy the vacuum Hamiltonian constraint there because

\[
G_{00}(0)=3H(0)^2=0.
\]

But for flat FLRW,

\[
\frac{G_{ii}}{a^2}=-\left(2\frac{\ddot a}{a}+H^2\right).
\]

Hence the first extension has zero spatial Einstein residual, while the second gives

\[
\frac{G_{ii}^{(2)}(0)}{a_2(0)^2}=-4\varepsilon\neq0.
\]

Therefore

\[
\boxed{
\text{constraint satisfaction on one slice}
\not\Rightarrow
\text{an arbitrary extension satisfies the full Einstein equations}.
}
\]

The full field/evolution law is indispensable.

---

## 8. Initial-value development

The Choquet-Bruhat–Geroch theorem is not a theorem that arbitrary tensor data determine a spacetime.

The relevant chain is schematically:

```text
initial-data manifold
+ admissible geometric initial data
+ constraint satisfaction
+ specified Einstein-matter system / closure
+ regularity and theorem hypotheses
-> local development
-> maximal globally hyperbolic development
   unique in the appropriate geometric sense
```

Required distinction:

\[
\boxed{\text{geometric uniqueness}\neq\text{fixed-coordinate component identity}.}
\]

Global extension beyond the maximal globally hyperbolic development is a separate question.

---

## 9. Matter closure is separate from the stress-energy symbol

Writing

\[
G_{\mu\nu}=\kappa T_{\mu\nu}
\]

does not specify how the matter variables inside \(T_{\mu\nu}\) evolve.

A closed system may require, depending on the matter model:

```text
matter variables
stress-energy construction
matter field/transport equations
constitutive relations or equation of state
coupling to geometry
```

Therefore

\[
\boxed{T_{\mu\nu}\text{ supplied}\not\Rightarrow\text{matter dynamics closed}.}
\]

---

## 10. DSD constitutive-bridge placement

Structural Reorganization Dynamics requires an explicitly supplied constitutive dynamic bridge before typed property data determine dynamic coefficients or operators. A GR specialization may use such a bridge to realize Einstein/matter operators, but the existence of the generic bridge does not derive those operators.

Required firewall:

```text
generic DSD constitutive bridge
!= Einstein field equation
```

and

```text
ability to encode EFE as a downstream dynamic specialization
!= independent DSD derivation of EFE
```

The DSD dynamics manuscript also treats conservation laws as additional model conditions rather than part of the universal definition of structural reorganization.

No DSD core revision is required.

---

## 11. Reconstruction/dependency ladder

```text
TARGET: Einstein tensor
  retain: smooth metric with sufficient derivatives
  status: standard geometric consequence

TARGET: Einstein-equation satisfaction
  retain: G_mu_nu, T_mu_nu, kappa, Lambda
  status: relation check required

TARGET: constraint satisfaction
  retain: h_ij, K_ij, matter projections, spatial derivatives/curvature
  status: initial-data relation check required

TARGET: full spacetime evolution
  retain:
    constraint-satisfying data
    + supplied field/evolution equations
    + gauge/reduction hypotheses
    + matter closure
  status: constraints alone insufficient

TARGET: maximal globally hyperbolic development
  retain:
    admissible initial data + specified Einstein-matter system
    + theorem regularity/hyperbolicity hypotheses
  status: standard theorem consequence, geometric uniqueness

TARGET: unique physical universe
  retain:
    additional actual matter/topology/boundary/asymptotic data
  status: not supplied by generic DSD or the abstract theorem alone
```

---

## 12. Rejected shortcuts

```text
metric -> Einstein field equation                                      REJECTED
conservation -> Einstein field equation                                REJECTED
arbitrary (h,K) -> constraint-satisfying initial data                  REJECTED
constraints on one slice -> full Einstein evolution                    REJECTED
T_mu_nu symbol -> closed matter dynamics                               REJECTED
DSD constitutive bridge -> Einstein dynamics without explicit supply   REJECTED
MGHD geometric uniqueness -> coordinate identity                       REJECTED
```

---

## 13. Verdict

\[
\boxed{\textbf{PASS\_WITH\_BOUNDARY}}
\]

```text
Einstein tensor constructible from supplied metric: YES
Einstein equation selected by generic DSD: NO
conservation follows conditionally from EFE+Bianchi: YES
conservation alone implies EFE: NO
arbitrary h,K are valid Einstein initial data: NO
constraint-satisfying data require explicit relation checks: YES
constraints alone determine arbitrary off-shell extension: NO
full Einstein-matter initial-value theorem usable under hypotheses: YES
MGHD uniqueness means coordinate identity: NO
DSD constitutive bridge independently yields EFE: NO
DSD core contradiction found: NO
DSD core revision required: NO
```

The strongest safe conclusion is

\[
\boxed{
\begin{aligned}
&\text{DSD can type and audit Einstein geometry, constraints,}\
&\text{matter closure, and Cauchy-development dependencies;}\\
&\text{the Einstein field equation itself remains an explicitly supplied}\
&\text{standard-relativity dynamical specialization.}
\end{aligned}
}
\]

---

## 14. Reproducibility

Script:

```text
audits/science/2026-09-10_rel_core_004_einstein_constraint_conservation_initial_value_gate.py
```

Run from repository root:

```bash
python audits/science/2026-09-10_rel_core_004_einstein_constraint_conservation_initial_value_gate.py --mode all
```

Dependency:

```text
Python standard library only
```

Observed result:

```text
TOTAL: 30/30 checks passed
OVERALL: PASS_WITH_BOUNDARY
```

---

## 15. Next target

Proceed to:

```text
REL Core 005 — Diffeomorphism / Gauge / Observable / Equivalence Gate
```

The next gate should separate:

```text
passive coordinate change
active diffeomorphism pullback
isometry
gauge-related representation
pointwise coordinate equality
scalar/tensor invariants
relational observables
local chart reconstruction
global geometric equivalence
DSD strict descriptive equivalence
```

The central question is whether the geometric uniqueness used in the initial-value theorem, standard GR gauge equivalence, and DSD strict equivalence can be related without silently identifying distinct equivalence relations.
