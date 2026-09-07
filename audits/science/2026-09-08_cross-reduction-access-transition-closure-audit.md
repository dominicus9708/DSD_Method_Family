# Cross-Standard Countermodel Audit — Reduction / Access Map vs Transition Closure

Date: 2026-09-08  
Status: **PASS_WITH_BOUNDARY**  
Track: **2 — second-depth common-role stress test, B4**

## 1. Purpose

This audit tests when a reduced or access-limited state admits an autonomous induced transition.

Let

\[
R:S\to Y
\]

be a reduction/access map and

\[
\Gamma:S\to S
\]

be a full-state transition.

The target question is whether there exists a map

\[
\Gamma_{\mathrm{red}}:\operatorname{im}R\to\operatorname{im}R
\]

such that

\[
\boxed{
R\circ\Gamma
=
\Gamma_{\mathrm{red}}\circ R.
}
\]

The audit first derives the exact map-level condition, then tests it independently in standard QM and in a relativistic hyperbolic-PDE comparator.

No quantum-gravity, alternative-gravity, or new DSD physical premise is introduced.

---

## 2. Exact map-level theorem — reduced-transition closure

For arbitrary sets and maps

\[
R:S\to Y,
\qquad
\Gamma:S\to S,
\]

an induced map

\[
\Gamma_{\mathrm{red}}:\operatorname{im}R\to\operatorname{im}R
\]

satisfying

\[
R\Gamma=\Gamma_{\mathrm{red}}R
\]

exists **if and only if**

\[
\boxed{
R(s)=R(s')
\Longrightarrow
R(\Gamma(s))=R(\Gamma(s'))
}
\]

for every \(s,s'\in S\).

Equivalently, \(\Gamma\) must map every \(R\)-fiber into a single \(R\)-fiber.

Using the equivalence relation

\[
s\sim_R s'
\iff
R(s)=R(s'),
\]

the condition is

\[
\boxed{
s\sim_R s'\Longrightarrow\Gamma(s)\sim_R\Gamma(s').}
\]

If the condition holds, define

\[
\Gamma_{\mathrm{red}}(R(s)):=R(\Gamma(s)).
\]

Fiber compatibility guarantees this definition is well-defined.

The induced map is unique on \(\operatorname{im}R\). If \(R\) is not surjective onto a larger codomain \(Y\), no uniqueness outside \(\operatorname{im}R\) is implied.

This is the previous fiber-factorization theorem specialized to

\[
q=R\circ\Gamma.
\]

It is an elementary mathematical/structural theorem, not a physical law.

---

## 3. Generic finite witness

Let

```text
S = {a,b,c}
R(a)=R(b)=0
R(c)=1
```

For a fiber-compatible transition

```text
Gamma_good(a)=c
Gamma_good(b)=c
Gamma_good(c)=a
```

both members of the \(R=0\) fiber are sent to the same reduced output \(R=1\). Hence an induced reduced transition exists.

For

```text
Gamma_bad(a)=a
Gamma_bad(b)=c
Gamma_bad(c)=c
```

we have

\[
R(a)=R(b)
\]

but

\[
R(\Gamma_{bad}(a))\neq R(\Gamma_{bad}(b)).
\]

Therefore no autonomous map on the reduced value alone can represent the full transition over that declared domain.

---

## 4. Standard-QM specialization

### 4.1 External standard lock

Standard quantum mechanics supplies:

\[
\mathcal H_{AB}=\mathcal H_A\otimes\mathcal H_B,
\qquad
R_Q(\rho_{AB})=\operatorname{Tr}_B\rho_{AB},
\]

and global unitary evolution

\[
\Gamma_U(\rho_{AB})=U\rho_{AB}U^\dagger.
\]

Partial trace and unitary evolution are standard-QM structures, not DSD-derived structures.

Open-system literature also treats the dependence of reduced dynamics on system-environment preparation and initial correlations; in particular, a single reduced completely-positive map is not automatically available for arbitrary initially correlated global states without additional structure.

Reference:

```text
Paz-Silva, Hall, Wiseman,
On the dynamics of initially correlated open quantum systems: theory and applications,
arXiv:1810.12540
https://arxiv.org/abs/1810.12540
```

### 4.2 Exact two-qubit non-closure witness

Take

\[
\rho^{(0)}_{AB}=|00\rangle\langle00|,
\qquad
\rho^{(1)}_{AB}=|01\rangle\langle01|.
\]

Both have the same initial subsystem state

\[
\operatorname{Tr}_B\rho^{(0)}_{AB}
=
\operatorname{Tr}_B\rho^{(1)}_{AB}
=
|0\rangle\langle0|.
\]

Now use the standard SWAP unitary.

After SWAP,

\[
\operatorname{Tr}_B\Gamma_{\mathrm{SWAP}}(\rho^{(0)}_{AB})
=|0\rangle\langle0|,
\]

while

\[
\operatorname{Tr}_B\Gamma_{\mathrm{SWAP}}(\rho^{(1)}_{AB})
=|1\rangle\langle1|.
\]

Thus

\[
R_Q(\rho^{(0)}_{AB})=R_Q(\rho^{(1)}_{AB})
\]

but

\[
R_Q\Gamma_{\mathrm{SWAP}}(\rho^{(0)}_{AB})
\neq
R_Q\Gamma_{\mathrm{SWAP}}(\rho^{(1)}_{AB}).
\]

Therefore there is no autonomous subsystem-A transition

\[
\Gamma_A(\rho_A)
\]

on this unrestricted witness domain that reproduces SWAP dynamics from \(\rho_A\) alone.

The failure is not a failure of partial trace or of unitary evolution. It is

```text
reduced state valid in-domain
+
insufficient state description for this autonomous transition target.
```

### 4.3 Closure control

For a factorized unitary

\[
U=U_A\otimes U_B,
\]

standard QM gives

\[
\operatorname{Tr}_B
[(U_A\otimes U_B)\rho_{AB}(U_A^\dagger\otimes U_B^\dagger)]
=
U_A\rho_AU_A^\dagger.
\]

Hence

\[
\Gamma_A(\rho_A)=U_A\rho_AU_A^\dagger
\]

is an induced reduced transition, independent of the hidden \(B\)-state.

The finite script uses \(U_A=X\) as this positive control.

Therefore standard QM exhibits both cases:

\[
\boxed{
\text{reduction closure can hold or fail depending on supplied global dynamics/domain.}
}
\]

---

## 5. Relativistic hyperbolic-PDE specialization

### 5.1 External standard lock

For the 1+1 wave equation with \(c=1\),

\[
\partial_t^2u-\partial_x^2u=0,
\]

Cauchy data determine the solution in their domain of dependence. This finite-propagation/Cauchy structure is standard hyperbolic PDE on Lorentzian backgrounds, not DSD-derived.

References:

```text
Bär and Tagne Wafo,
Initial value problems for wave equations on manifolds,
arXiv:1408.4995
https://arxiv.org/abs/1408.4995

Waldmann,
Geometric Wave Equations,
arXiv:1208.4706
https://arxiv.org/abs/1208.4706
```

### 5.2 Same fixed spatial restriction need not close

Let initial data have \(g=\partial_tu(0,x)=0\), so d'Alembert gives

\[
u(t,x)=\frac12[f(x-t)+f(x+t)].
\]

Take the initial access interval

\[
I=[-2,2].
\]

Choose two global initial profiles

\[
f_0(x)=0,
\]

and

\[
f_1(x)=
\begin{cases}
0,&x\le2,\\
1,&x>2.
\end{cases}
\]

They agree identically on \(I\), so the initial restricted state is the same.

At \(t=1\), for every

\[
x\in[-1,1],
\]

both \(x-1\) and \(x+1\) remain inside \([-2,2]\), so both solutions agree there.

This is the expected domain-of-dependence closure.

However at the still-in-\(I\) point

\[
x=1.5,
\]

we have

\[
u_0(1,1.5)=0,
\]

but

\[
u_1(1,1.5)
=\frac12[f_1(0.5)+f_1(2.5)]
=\frac12.
\]

Thus the same fixed spatial interval \(I\) does **not** admit an autonomous later-state map from its initial restriction alone unless appropriate boundary/exterior information or boundary conditions are supplied.

The correct statement is target-domain relative:

\[
\boxed{
\text{initial data on }I
\to
\text{autonomous determination only on its dependence domain, absent extra boundary data.}
}
\]

This is not an identification between a quantum environment and a spacetime exterior.

---

## 6. Cross-standard structural result

Both standard-theory examples instantiate the same abstract criterion:

\[
\boxed{
R\circ\Gamma
\text{ factors through }R
\iff
\Gamma\text{ respects }R\text{-fibers}.
}
\]

But the physical reasons differ:

```text
QM:
  hidden subsystem/environment degrees of freedom + supplied global interaction

relativistic wave comparator:
  finite propagation + boundary/exterior dependence of the target region
```

Therefore the following identification remains rejected:

```text
quantum environment = spacetime exterior
partial trace = spatial/domain restriction
open-system memory = relativistic boundary influx
```

Only the map-level closure criterion is common.

---

## 7. DSD interpretation

For a declared DSD reduction/access/readout map

\[
R:\Sigma\to\Sigma_{\mathrm{red}},
\]

and a supplied transition

\[
\Gamma:\Sigma_t\to\Sigma_{t'},
\]

one may write an autonomous reduced dynamics

\[
\Gamma_{\mathrm{red}}
\]

only after verifying

\[
R(\Sigma)=R(\Sigma')
\Longrightarrow
R(\Gamma\Sigma)=R(\Gamma\Sigma').
\]

If this fails, the reduced state is still valid for its declared static/readout role, but it is not dynamically closed for that transition target.

Possible remedies are domain-specific and must be supplied explicitly, for example:

```text
- enlarge the retained state;
- retain additional environment/boundary variables;
- restrict the admissible global-state domain;
- restrict the target region/time interval;
- supply an explicit constitutive closure or memory/history structure.
```

None of these is automatically selected by the DSD core.

This is consistent with the existing DSD rule that a static/property bridge does not determine a dynamic operator.

---

## 8. Status classification

### Mathematical / structural theorem layer

- induced reduced transition exists iff \(\Gamma\) preserves the equivalence relation induced by \(R\);
- equivalently, \(R\Gamma\) is constant on every \(R\)-fiber;
- if it exists, the induced transition is unique on \(\operatorname{im}R\).

### Finite / exact witness layer

- generic three-state fiber-compatible vs fiber-splitting transitions;
- two-qubit SWAP counterexample and local-unitary closure control;
- 1+1 d'Alembert same-interval non-closure witness and shrunken domain-of-dependence control.

### Conditional standard-physics layer

- tensor-product systems, partial trace, and unitary evolution are supplied by standard QM;
- wave-equation Cauchy/domain-of-dependence structure is supplied by standard hyperbolic PDE/relativity mathematics.

### Unresolved / not established

- no universal DSD reduced dynamics is derived;
- no Markovianity criterion is identified with DSD closure;
- no environment is identified with a DSD external system by label alone;
- no relativistic boundary condition is inferred from DSD;
- no quantum-gravity implication follows.

---

## 9. Scoped outcome ledger

```text
R o Gamma = Gamma_red o R without fiber test:
  NOT JUSTIFIED

Gamma respects R-fibers -> induced reduced transition on im(R):
  VALID

same reduced state -> same later reduced state for arbitrary global dynamics:
  REJECTED

QM partial trace + SWAP -> autonomous A dynamics from rho_A alone on witness domain:
  REJECTED

QM factorized local unitary -> autonomous A unitary dynamics:
  VALID_IN_DOMAIN

wave initial restriction on I -> later full same-I restriction without boundary/exterior data:
  REJECTED by exact witness

wave initial restriction on I -> target inside its domain of dependence:
  VALID_IN_DOMAIN
```

No valid reduced state is labeled `FAIL` merely because it is not dynamically closed for a stronger target.

---

## 10. DSD core impact

No revision of the Formation Axiom System, Property Axiom System, Channel-Indexed Static Aggregation, or Structural Reorganization Dynamics is required.

The result strengthens the separation

\[
\boxed{
\text{valid reduced/static description}
\not\Rightarrow
\text{autonomous reduced dynamics}.
}
\]

and gives the exact closure test once \(R\) and \(\Gamma\) are supplied.

---

## 11. Verdict

\[
\boxed{\textbf{PASS\_WITH\_BOUNDARY}}
\]

The common map-level role survives and is stronger than a vocabulary analogy:

\[
\boxed{
\Gamma_{\mathrm{red}}\text{ exists on }\operatorname{im}R
\iff
\Gamma\text{ respects }R\text{-fibers}.
}
\]

The physical mechanisms producing closure or non-closure remain theory-specific.

---

## 12. Reproducibility

Script:

```text
audits/science/2026-09-08_cross_reduction_transition_closure.py
```

Run from repository root:

```bash
python audits/science/2026-09-08_cross_reduction_transition_closure.py --mode all
```

Dependency:

```text
Python standard library only
```

---

## 13. Next target

Proceed to B5:

```text
composition of reductions / readouts vs order dependence

abstract target:
  R2 o R1 ?= R1 o R2

questions:
  when do two valid reductions commute;
  when does order erase different information;
  when can sequential restriction be replaced by one joint reduction.

QM comparator:
  compatible vs non-equivalent subsystem/readout reductions.

relativity comparator:
  nested domain restriction vs representation/access operations.

goal:
  separate typed composability from mere existence of both maps,
  and identify the exact commutation/factorization conditions without
  identifying the physical reductions across theories.
```
