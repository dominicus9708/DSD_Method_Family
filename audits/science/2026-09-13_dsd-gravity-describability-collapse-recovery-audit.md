# DSD Gravity Describability Collapse / Recovery Audit — BH-RB-006

Date: 2026-09-13

Status: **PASS_WITH_BOUNDARY / DESCRIBABILITY_COLLAPSE_IDENTIFIED / PHYSICAL_INFORMATION_LOSS_NOT_DERIVED**

## Purpose

Continue the active QM/relativity-based DSD gravity rebaseline after BH-RB-005 while introducing the new DSD idea of **describability collapse** and **describability recovery**.

The purpose is not to claim that one physical quantity is literally converted into another. It is to test whether distinct physical/global states can become indistinguishable under a selected descriptor, and whether adding independent descriptive channels can refine that collapsed equivalence class again.

The discarded structural-gravity branch is not used.

## DSD source basis

The current Formation Axiom System introduces finite composition only after operational-channel formation and explicitly permits non-injective composition. Proposition 5.14 gives distinct finite channel families with the same composite output. The comparison theory also states that composite-level coincidence is strictly weaker than strict formation equivalence.

The current Property Axiom System and dynamics additionally preserve the distinction between undefined and defined zero. Therefore a missing/undefined physical bridge must not be zero-filled merely to obtain a convenient comparator.

These facts support a DSD-level distinction between:

- the underlying structured state;
- the descriptor applied to that state;
- equality of descriptor outputs;
- equality of the underlying state.

## Working definition

Let the underlying state space be `S`, and let

\[
D_\eta:S\to Y_\eta
\]

be a descriptor under descriptive conditions `eta`, which may include observer access, measurement channels, resolution, language, aggregation, or other representation conditions.

Define

\[
x\sim_{D_\eta}y
\quad\Longleftrightarrow\quad
D_\eta(x)=D_\eta(y).
\]

A **describability collapse** occurs when states that were distinguishable under one descriptive condition are no longer distinguishable under another:

\[
D_{\eta_0}(x)\neq D_{\eta_0}(y),
\qquad
D_{\eta_1}(x)=D_{\eta_1}(y).
\]

A **describability recovery** occurs when a later or refined descriptor splits such a collapsed class:

\[
D_{\eta_1}(x)=D_{\eta_1}(y),
\qquad
D_{\eta_2}(x)\neq D_{\eta_2}(y).
\]

Recovery means refinement of the descriptive partition, not automatic reconstruction of a full microstate.

## Closed M/J/Q comparator-family gate

After BH-RB-003, 004, and 005, the external standard black-hole comparator family is selected only when global `M`, `J`, and `Q` statuses are sufficiently defined.

For defined zero/nonzero `J` and `Q`:

| J status | Q status | External comparator |
|---|---|---|
| zero | zero | Schwarzschild |
| nonzero | zero | Kerr |
| zero | nonzero | Reissner–Nordstrom |
| nonzero | nonzero | Kerr–Newman |

If either required `J` or `Q` status is undefined, the family is **UNRESOLVED**. Undefined is not silently replaced by zero.

The standard external normalized parameters remain

\[
\chi=\frac{Jc}{GM^2},
\qquad
\hat q=\frac{Q}{\sqrt{4\pi\varepsilon_0G}\,M},
\qquad
r_g=\frac{GM}{c^2},
\]

and the outer-horizon comparator is

\[
r_+=r_g\left(1+\sqrt{1-\chi^2-\hat q^2}\right)
\]

inside

\[
\chi^2+\hat q^2\le1.
\]

These are external standard-GR/electromagnetic comparator relations, not generic DSD laws.

## Experiment A — charge-sign describability collapse

Fix the active Sgr A* external mass benchmark

\[
M=4.297\times10^6M_\odot
\]

and use control parameters

\[
\chi=0.9,
\qquad
\hat q=\pm0.3.
\]

The two states are distinct because the signed global charge differs, but

\[
r_+(+0.3)=r_+(-0.3)
\approx8.3517938\times10^6\ \mathrm{km}.
\]

Thus the radius-only descriptor

\[
D_r(M,\chi,\hat q)=r_+
\]

is non-injective:

\[
D_r(s_+) = D_r(s_-)
\quad\text{while}\quad
s_+\neq s_-.
\]

This is a clean describability-collapse witness. It does **not** mean positive and negative charge physically become the same quantity.

## Experiment B — different J/Q allocations collapse to one radius

At fixed mass compare

\[
(\chi,\hat q)_A=(0.6,0.4),
\qquad
(\chi,\hat q)_B=(0.4,0.6).
\]

Both satisfy

\[
\chi^2+\hat q^2=0.52,
\]

so the external horizon comparator gives

\[
r_{+,A}=r_{+,B}
\approx1.0741368\times10^7\ \mathrm{km}.
\]

The radius readout therefore loses not only charge sign but also the allocation between spin and charge magnitude.

Adding an independent spin descriptor recovers this distinction:

\[
D_{r,\chi}(s)=(r_+(s),\chi(s)).
\]

Then

\[
D_{r,\chi}(s_A)\neq D_{r,\chi}(s_B).
\]

This is a partial describability recovery.

## Experiment C — staged recovery

For the charge-sign pair, adding `chi` is insufficient because `chi` is already equal:

\[
D_{r,\chi}(s_+)=D_{r,\chi}(s_-).
\]

Adding signed charge information gives

\[
D_{r,\chi,Q}(s)
=
(r_+(s),\chi(s),\hat q(s)),
\]

and now

\[
D_{r,\chi,Q}(s_+)\neq D_{r,\chi,Q}(s_-).
\]

Therefore recovery can be staged: one added channel may split some collapsed classes while leaving others collapsed.

## Experiment D — inadmissible collapse from zero-padding

Compare two states with the same defined nonzero spin:

1. charge status = **undefined**;
2. charge status = **defined zero**.

A status-aware selector gives

\[
\text{undefined charge}\to\text{UNRESOLVED},
\]

but

\[
Q=0\to\text{Kerr}.
\]

A deliberately bad zero-padding rule maps both to `KERR`.

Hence silent zero-padding creates an **inadmissible describability collapse**:

\[
\text{undefined}\not=\text{defined zero}
\quad\text{but bad readout identifies them}.
\]

This directly connects the new idea to the Property/Dynamics status firewall.

## Experiment E — resolution-induced collapse and recovery

Use two distinct control states

\[
(\chi,\hat q)_A=(0.9,0.30),
\qquad
(\chi,\hat q)_B=(0.9,0.31).
\]

Their exact external comparator radii differ:

\[
r_{+,A}\approx8.3517938\times10^6\ \mathrm{km},
\]

\[
r_{+,B}\approx8.2896313\times10^6\ \mathrm{km}.
\]

Under a deliberately coarse `200,000 km` floor-binned readout, both become

\[
8.2\times10^6\ \mathrm{km}.
\]

Under a finer `10,000 km` readout they separate into

\[
8.35\times10^6\ \mathrm{km}
\quad\text{and}\quad
8.28\times10^6\ \mathrm{km}.
\]

This demonstrates that describability collapse need not correspond to any physical collapse at all. It can be induced purely by readout resolution, and a finer readout can partially restore the distinction.

The bin widths in this control are synthetic audit parameters, not claimed instrument resolutions.

## Computational audit

The reproduction script passes 10/10 checks:

1. horizon radius collapses the sign of charge;
2. horizon radius can collapse different `J/Q` allocations;
3. adding `chi` recovers the tradeoff pair;
4. adding signed `Q` recovers the charge-sign pair;
5. undefined charge is not neutral charge;
6. zero-padding creates an inadmissible descriptive collapse;
7. defined zero/nonzero `J,Q` select the four standard comparator families;
8. unresolved status blocks numerical radius comparison;
9. coarse resolution can induce describability collapse;
10. finer resolution can partially recover distinction.

## Interpretation boundary

The audit establishes a property of descriptors and comparator readouts:

\[
\boxed{
D(x)=D(y)\not\Rightarrow x=y
}
\]

and shows that descriptive equivalence classes can coarsen or refine.

It does **not** establish any of the following:

- that stellar information is physically destroyed;
- that charge becomes gravity;
- that mass, spin, and charge are the complete microstate of a black hole;
- that Hawking-radiation information recovery has been solved;
- that DSD derives Kerr-Newman or Einstein-Maxwell dynamics.

The safe black-hole statement is instead:

\[
\boxed{
\text{information distinguishable in one description can become non-separable in a later/reduced description}
}
\]

while the physical ontology and conservation laws remain separately audited.

## Verdict

- radius equality -> full physical-state equality: **FAIL**;
- undefined charge -> neutral charge: **FAIL**;
- reduced readout can create describability collapse: **PASS**;
- additional independent descriptor can produce partial describability recovery: **PASS**;
- descriptive collapse -> physical information destruction: **NOT DERIVED**;
- status-aware `M/J/Q` comparator family selection: **PASS WITH EXTERNAL PROVENANCE**.

Final status:

\[
\boxed{
\text{PASS\_WITH\_BOUNDARY / DESCRIBABILITY\_COLLAPSE\_IDENTIFIED / PHYSICAL\_INFORMATION\_LOSS\_NOT\_DERIVED}
}
\]

## Next step

The next gravity audit should preserve this descriptor/state distinction while asking whether any DSD-native or explicitly bridged dynamical quantity constrains the transition from a pre-collapse stellar component-resolved state to the externally accessible black-hole descriptors. The goal is not to assume that the initial state is compressed into `M,J,Q`, but to classify which distinctions are preserved, externally recoverable, unresolved, or collapsed under each declared descriptor.

Reproduction script:

`audits/science/2026-09-13_dsd_gravity_describability_collapse_recovery_audit.py`
