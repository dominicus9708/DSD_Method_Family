# DSD Gravity-Principle Research Log — Experiments 656–663

Date: 2026-09-07

Primary external basis:

```text
standard weak-field relativity
standard nonrelativistic quantum mechanics
externally supplied classical gravitational potential/background
```

No alternative quantum-gravity theory is used.

---

## Experiment 656 — weak-field proper-time benchmark

For a static weak potential \(\Phi\),

\[
|\Phi|/c^2\ll1,
\]

use

\[
ds^2
\approx
-\left(1+\frac{2\Phi}{c^2}\right)c^2dt^2
+\left(1-\frac{2\Phi}{c^2}\right)d\mathbf x^2.
\]

For stationary branches,

\[
\boxed{
\Delta\tau
\approx
\frac{\Delta\Phi}{c^2}T
}
\]

at first order.

### Verdict

- coordinate holding time \(T\) = proper-time difference: **REJECTED**
- weak-field stationary proper-time relation: **CONFIRMED WITH STATED APPROXIMATION**

---

## Experiment 657 — standard Schrödinger phase on supplied classical potential

Use

\[
i\hbar\partial_t\psi
=
\left[-\frac{\hbar^2}{2m}\nabla^2+m\Phi\right]\psi.
\]

A fixed-potential branch acquires the potential phase

\[
\varphi_\Phi=-\frac{m\Phi T}{\hbar},
\]

so two branches satisfy

\[
\boxed{
\Delta\varphi
=-\frac{m\Delta\Phi T}{\hbar}
}
\]

under the stated specialization.

### Verdict

- quantum state generates the gravitational background: **NOT ASSUMED / REJECTED AS A PRESENT INFERENCE**
- ordinary QM evolution on an externally supplied classical potential: **CONFIRMED AS STANDARD CONTROL**

---

## Experiment 658 — proper-time / quantum-phase correspondence under the controlled bridge

Combining Experiments 656–657 gives

\[
\boxed{
\Delta\varphi
\approx
-\frac{mc^2}{\hbar}\Delta\tau
}
\]

for the stationary weak-field control.

This does not identify phase with proper time as one physical quantity. It is a bridge between different typed descriptors under explicit assumptions.

### Verdict

- phase = proper time as a DSD primitive identity: **REJECTED**
- first-order numerical correspondence under supplied weak-field + \(V=m\Phi\) assumptions: **CONFIRMED**

---

## Experiment 659 — phase-to-probability fiber collision

For equal-amplitude two-path interference,

\[
P_+(\Delta\varphi)
=\frac{1+\cos\Delta\varphi}{2}.
\]

Then

\[
P_+(\theta)
=P_+(\theta+2\pi k)
=P_+(-\theta+2\pi k).
\]

Hence a single interference probability does not uniquely reconstruct phase.

### DSD consequence

Separate:

```text
unwrapped phase
phase modulo 2pi
selected interference probability
```

### Verdict

- equal probability implies equal phase: **REJECTED**
- measurement probability is a lossy phase readout in this control: **CONFIRMED**

---

## Experiment 660 — potential/time parameter non-identifiability

At first order,

\[
\Delta\tau\propto\Delta\Phi T,
\qquad
\Delta\varphi\propto\Delta\Phi T.
\]

Therefore distinct pairs can produce the same outputs:

\[
(\Delta\Phi_1,T_1)\ne(\Delta\Phi_2,T_2),
\qquad
\Delta\Phi_1T_1=\Delta\Phi_2T_2.
\]

Explicit control:

```text
(DeltaPhi,T)=(2,3)
(DeltaPhi,T)=(1,6)
```

Both give the same first-order proper-time difference and the same phase for fixed mass.

### Verdict

- \(\Delta\tau\) uniquely reconstructs \((\Delta\Phi,T)\): **REJECTED**
- \(\Delta\varphi\) uniquely reconstructs \((\Delta\Phi,T)\): **REJECTED**
- an independent measurement of at least one factor is required: **CONFIRMED**

---

## Experiment 661 — typed time/phase chain

The controlled chain is

\[
(\Delta\Phi,T)
\to
\Delta\tau
\to
\Delta\varphi
\to
P.
\]

Each arrow has a different status:

```text
weak-field relativistic map,
conditional proper-time/phase bridge,
quantum measurement readout.
```

They must not be compressed into one generic `time` or `describability` scalar.

### Verdict

- coordinate time / proper time / phase / probability as one DSD variable: **REJECTED**
- typed-chain representation: **CONFIRMED**

---

## Experiment 662 — standard-only route for testing DSD gravity

A safe future benchmark separates two stages.

### Stage A — gravity comparison

```text
DSD gravity response
-> explicit comparison map
-> standard relativistic DeltaTau or weak-field DeltaPhi
```

### Stage B — downstream standard QM

```text
externally supplied classical DeltaPhi/DeltaTau
-> ordinary Schrödinger phase
-> measurement probability
```

This avoids using a quantum state as a gravitational source unless a future independent bridge is supplied and validated.

### Verdict

- quantum phase -> DSD gravity source by default: **REJECTED**
- DSD gravity -> standard-relativity benchmark -> downstream QM: **CONFIRMED AS SAFE ARCHITECTURE**

---

## Experiment 663 — next standard-only extension

Next control family:

```text
A. moving branch: gravitational + kinematic time dilation separated
B. internal two-level clock: global phase vs observable relative internal phase
C. finite readout set: reconstructibility of velocity, potential, and energy splitting
```

The target is to determine which variables remain identifiable after the successive standard-theory readouts.

### Verdict

- next target admitted: **CONFIRMED**
- quantum-gravity interpretation preinstalled: **REJECTED**

---

## Combined consequence

The active DSD gravity-principle route can now use a strictly standard comparison stack:

```text
DSD gravity-principle response
-> standard relativistic gravitational observable
-> standard quantum evolution on that supplied classical background
-> experiment/readout fiber audit.
```

This keeps gravity generation, relativistic clock behavior, quantum evolution, and measurement reconstruction as separate technical layers.

## Reproducibility

```bash
python audits/science/2026-09-07_weak_field_time_phase_describability.py
```

Parameterized example:

```bash
python audits/science/2026-09-07_weak_field_time_phase_describability.py --mass 1e-26 --delta-phi 1.0 --time 1.0
```
