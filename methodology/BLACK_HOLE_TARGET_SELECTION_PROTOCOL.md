# Black-Hole Target-Selection Protocol
# 블랙홀 normalized-target 선택 프로토콜

```text
METHOD_ID: DSD-METHOD-20260911-BH-TARGET-SELECT-001
STATUS: ACTIVE_DRAFT
DATE: 2026-09-11
PARENT: BLACK_HOLE_NORMALIZED_PENCIL_ATTRACTOR_PROTOCOL
```

## 1. Purpose

After the normalized support pencil is defined by

\[
B(S)=L(S)^{-1/2}H_0(S)L(S)^{-1/2},
\qquad
\Psi_*(S)=\lambda_{\min}(B(S)),
\]

and a common-target relaxation mechanism has been shown to be mathematically possible, the remaining task is to determine whether the target spectrum can be selected independently of Schwarzschild fitting.

## 2. Prohibited shortcuts

Do not select the target by:

- setting \(\Psi_*=1/2\) because the Schwarzschild comparator later needs it;
- calling one state `critical` and reading the desired coefficient from that label;
- identifying a rank transition with a support-spectrum transition;
- assuming a relation-valued transition is deterministic;
- importing EHT ring/shadow scales into target normalization.

## 3. Critical-coupling rule

For any candidate coupling parameter \(\kappa\), distinguish:

1. **pre-load normalized support spectrum** \(B(\kappa)\);
2. **external/increasing load parameter** \(\Theta\);
3. **zero-margin condition** \(\lambda_{\min}[B(\kappa)-\Theta L]=0\).

The critical value of a coupling parameter that makes \(B\) itself singular is not generally the same object as the finite load threshold \(\Psi_*\).

Therefore a coupling branch is admissible only if a constitutive law determines \(\kappa\) before the black-hole radius comparator is opened.

## 4. Transition universality criterion

Let a typed hybrid transition be

\[
J:X^-\Rightarrow X^+.
\]

Let \(B_+\) be the normalized-pencil readout on the post-transition state class.

Coefficient universality requires

\[
\boxed{
\operatorname{Osc}_{\operatorname{Im}J}
\lambda_{\min}(B_+)=0
}
\]

for the admitted predecessor class.

Operator universality is stronger. A sufficient spectral condition is

\[
B_+(\operatorname{Im}J)
\subseteq
\{U^TB_*U:U\in O(n)\}.
\]

Literal common-target reset requires the still stronger singleton condition

\[
B_+(\operatorname{Im}J)=\{B_*\}.
\]

These conditions are tests; generic DSD does not guarantee them.

## 5. Separation from balance laws

Target selection and conservation are different interfaces.

If a transition changes the regular support signature or formation background, any conserved quantity across the transition needs an explicit jump/balance law.

Thus

\[
B_+=B_*
\]

does not imply a value for

\[
C(S^+)-C(S^-)=J_C.
\]

## 6. Current branch status

```text
isotropic target:                mathematically possible, coefficient not fixed to 1/2
critical-coupling label:         insufficient
kappa=1/2 two-mode toy:          gives 1/2 but is not independently selected
source-dependent transition:     fails exact universality
rank-only transition:            fails exact universality
branched relation:               fails uniqueness without selector
explicit universal reset:        sufficient by construction, but requires a new law
```

## 7. Next blind selection candidates

Test these while Schwarzschild remains sealed:

1. fixed trace + extremal principle;
2. fixed trace + determinant/entropy-like objective;
3. coercivity/stability extremum under normalization;
4. symmetry-constrained variational selection;
5. lineage-compatible admissibility minimization.

For every candidate, record:

- supplied assumptions;
- whether the target is unique;
- whether the result is basis invariant;
- whether source-specific profile information survives;
- whether the target is stable under perturbation;
- whether a numerical half coefficient appears before the comparator is opened.

## 8. Decision labels

- `TARGET_NOT_SELECTED`: constraints leave a continuum or branching family.
- `TARGET_SELECTED_CONDITIONALLY`: explicit downstream law gives one spectrum.
- `TARGET_SOURCE_DEPENDENT`: selected spectrum depends on progenitor detail.
- `TARGET_UNIVERSAL`: one frozen law gives one source-independent spectrum across the admitted class.
- `HALF_COEFFICIENT_BLIND_RECOVERY`: \(\Psi_*=1/2\) occurs uniquely without Schwarzschild/EHT input.

Current status:

```text
TARGET_NOT_SELECTED
```
