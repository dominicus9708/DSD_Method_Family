# Structural-Gravity Target-Selection Branch Audit
# 구조적 중력 target-selection 분기 감사

```text
AUDIT_ID: DSD-AUDIT-20260911-SG-TARGET-SELECTION-001
STATUS: PASS_WITH_BOUNDARY / TARGET_SELECTION_LAW_STILL_OPEN
DATE: 2026-09-11
DOMAIN: structural gravity / black-hole critical-radius benchmark
```

## 1. Question

Can the remaining normalized target spectrum, especially the candidate threshold readout

\[
\Psi_* = \lambda_{\min}(B_*),
\]

be selected by either:

1. a critical-coupling condition; or
2. a DSD transition relation,

without importing the Schwarzschild coefficient?

## 2. Source boundary

The Structural Reorganization Dynamics framework distinguishes transport, coupling, restoration/relaxation, and source terms. Their coefficients are supplied by a constitutive dynamic bridge; the framework does not assign a universal dissipative sign to coupling or infer stability from a restoration-like label.

A transition is a typed relation

\[
J_k:X_k^-\Rightarrow X_k^+
\]

and may be relation-valued rather than deterministic. The foundational dynamic interface does not choose a unique post-transition numerical state. Conservation across a transition requires a separate balance/jump law.

## 3. Critical-coupling branch

Use the normalized symmetric two-mode family

\[
B(\kappa)=
\begin{pmatrix}
1&-\kappa\\
-\kappa&1
\end{pmatrix}.
\]

Then

\[
\lambda_-(\kappa)=1-\kappa,
\qquad
\lambda_+(\kappa)=1+\kappa,
\]

and

\[
\det B=1-\kappa^2.
\]

For the identity-load specialization

\[
B(\Theta)=B-\Theta I,
\]

the support threshold is

\[
\Psi_*=\lambda_{\min}(B)=1-\kappa.
\]

Therefore

\[
\Psi_*=\frac12
\]

occurs when

\[
\kappa=\frac12.
\]

However the actual zero-margin critical coupling of the baseline pencil is

\[
\kappa=1,
\]

for which

\[
\Psi_*=0.
\]

Hence the phrase `critical coupling` does not independently select the half coefficient. A constitutive law must first determine the pre-load coupling spectrum.

## 4. Transition-selected branch

For a threshold readout

\[
\Psi_*:X^+\to\mathbb R,
\]

exact transition universality requires

\[
\boxed{
\operatorname{Osc}_{\operatorname{Im}J_k}\Psi_*=0
}
\]

where

\[
\operatorname{Osc}_A f
=\sup_A f-\inf_A f.
\]

A stronger operator-level condition is that the post-transition normalized pencils all lie in one orthogonal-similarity class,

\[
B(X^+)\subseteq\{U^TB_*U\},
\]

or are literally one singleton if full operator equality is claimed.

The control branches show:

- universal reset to one declared target: exact coefficient universality is possible;
- source-dependent target: coefficient spread survives;
- same coarse rank/geometric label: coefficient spread can survive;
- relation-valued branching: multiple valid post-transition spectra survive unless an extra selector is supplied.

Thus a transition can enforce a common target only when that common image is itself an explicit downstream law or admissibility condition. The generic transition relation does not supply it.

## 5. Numerical control

For the transition controls, the threshold oscillations were:

```text
universal_reset:      0
source_dependent:     0.08795679805056911
rank_only:            0.185142857143
branched_relation:    0.30000000000000004
```

The calculation passed 11/11 checks.

## 6. Verdict

```text
critical-coupling label -> unique Psi_*=1/2: REJECTED
kappa=1/2 -> Psi_*=1/2 in the normalized two-mode control: CONFIRMED
zero-margin baseline critical coupling -> Psi_*=1/2: REJECTED; gives Psi_*=0
transition relation alone -> unique B_*: REJECTED
explicit universal post-transition image -> common Psi_*: CONDITIONAL / POSSIBLE
rank/geometric transition alone -> common support spectrum: REJECTED
balance law supplied automatically by target selection: REJECTED
```

Current maximum supported statement:

\[
\boxed{
\text{the remaining problem is a genuine target-selection law, not a label-selection problem}
}
\]

## 7. Next target

Audit whether a noncircular post-transition admissibility condition can select a unique normalized spectrum using only DSD-side inputs, for example:

- trace or determinant constraints;
- extremal/minimal structural-support principles;
- symmetry plus stability/coercivity;
- lineage-compatible transition invariants;
- a variational principle on the normalized support pencil.

Schwarzschild and EHT values remain sealed during that derivation stage.

## 8. Reproduction

```bash
python audits/science/2026-09-11_structural_gravity_target_selection_branch_audit.py --mode all
```
