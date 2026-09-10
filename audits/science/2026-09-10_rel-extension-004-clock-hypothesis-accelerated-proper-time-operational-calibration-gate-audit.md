# REL Extension 004 — Clock Hypothesis / Accelerated Proper-Time / Operational Calibration Gate

Date: 2026-09-10  
Status: **PASS_WITH_BOUNDARY**

## Purpose
REL Extension 003 separated Weyl integrability, standard-clock parametrization, local/global scale recovery, and physical clock calibration. This gate asks whether a supplied Lorentzian metric and its proper-time functional by themselves force every accelerated physical clock to read that proper time.

## Standard metric-proper-time lock
With c=1,
\[
d\tau^2=dt^2-d\mathbf x^2,
\qquad d\tau=\sqrt{1-v^2}\,dt.
\]
For uniform proper acceleration,
\[
t(\tau)=a^{-1}\sinh(a\tau),\quad x(\tau)=a^{-1}\cosh(a\tau),
\]
so
\[
u^\mu=(\cosh a\tau,\sinh a\tau),\quad u\cdot u=-1,
\]
\[
A^\mu=(a\sinh a\tau,a\cosh a\tau),\quad A\cdot A=a^2,\quad u\cdot A=0.
\]
The regression witness verifies these identities and \(\sqrt{1-v^2}\,dt/d\tau=1\) at multiple samples.

## Clock-condition boundary
The geometric functional contains no universal explicit acceleration term. But this does not imply that every real clock mechanism is acceleration-insensitive. As a countermodel only, take
\[
dT_{dev}=\left[1+\varepsilon(a/a_0)^2\right]d\tau.
\]
At the same event and tangent, two different accelerations have the same metric infinitesimal proper time but different device readings when \(\varepsilon\neq0\). Therefore
\[
\boxed{\text{metric proper time}\not\Rightarrow\text{response law of every physical clock}.}
\]
The countermodel is not proposed as new physics; it only exposes the logical boundary.

## Accelerated-path witness
For equal coordinate duration T, a stationary path has \(\tau=T\), while a symmetric out-and-back path at speed magnitude v has
\[
\tau=T\sqrt{1-v^2}<T.
\]
The turnaround changes the worldline tangent but adds no separate universal acceleration scalar to the metric line element. Proper time is worldline dependent, while real-clock robustness remains a distinct physical question.

## Calibration boundary
Even an accepted ideal clock can report
\[
T_{display}=\alpha\tau+\beta,\qquad \alpha>0.
\]
The metric does not itself choose device zero or display scale. Hence metric proper-time existence and full physical calibration remain distinct.

## Experimental comparator and circularity firewall
Bailey et al. measured relativistic time dilation for muons in the CERN storage ring at \(\gamma=29.33\); the positive-muon result was reported consistent with the special-relativistic dilation factor at fractional error \(2\times10^{-3}\) at 95% confidence. This is empirical support for clock-like relativistic time transformation under sustained acceleration.

The negative-muon proper lifetime quoted in the same abstract was derived assuming special relativity, so it is not reused as independent evidence for the same law. This distinction is encoded in the regression audit.

Mainwaring and Stedman analyzed alternative acceleration-dependent clock principles and experimental constraints. Mashhoon emphasized that the wider hypothesis of locality has a domain of applicability. Fletcher and later philosophical literature show that the exact status of the clock hypothesis—as independent postulate, ideal-clock condition, or recoverable behavior of suitable clock models—is not universally characterized in one way. This audit therefore keeps the operational bridge explicit rather than settling that interpretive dispute.

## DSD provenance
The following remain supplied or external:
```text
smooth Lorentzian spacetime
metric proper-time functional
ideal/standard-clock condition
momentarily comoving inertial comparison
physical clock mechanism
clock calibration
experimental identification of clock readout
Einstein dynamics, if gravity is added
```
DSD may type and audit these records, but its external evolution parameter is not automatically relativistic proper time. Likewise, DSD channel/property labels do not create clock hardware or a clock law, and accelerated-clock agreement does not identify c_info with relativistic c.

## Regression result
Run from repository root:
```bash
python audits/science/2026-09-10_rel_extension_004_clock_hypothesis_accelerated_proper_time_operational_calibration_gate.py --mode all
```
Observed:
```text
METRIC_PROPER_TIME:             PASS
CLOCK_HYPOTHESIS_BOUNDARY:      PASS
ACCELERATED_PATH:               PASS
CLOCK_CALIBRATION:              PASS
EXPERIMENT_AND_CIRCULARITY:     PASS
DSD_PROVENANCE:                 PASS
COMPARATOR_SCOPE:               PASS
TOTAL: 94/94 checks passed
OVERALL: PASS_WITH_BOUNDARY
```
The repeated hyperbola samples are regression witnesses, not a proof of all accelerated-clock physics.

## Verdict
**PASS_WITH_BOUNDARY**.

\[
\boxed{\text{physical clock reading}=\text{metric proper time}}
\]
is well supported for suitable standard clocks, but it is not identical to the bare mathematical existence of the proper-time functional. For DSD,
\[
\boxed{\text{geometry--clock--calibration provenance audit}\neq\text{independent derivation of relativistic chronometry}.}
\]
No contradiction with the current DSD core papers was found.

## External references
- J. Bailey et al., *Measurements of relativistic time dilatation for positive and negative muons in a circular orbit*, Nature 268, 301–305 (1977), DOI: 10.1038/268301a0.
- S. R. Mainwaring and G. E. Stedman, *Accelerated clock principles in special relativity*, Phys. Rev. A 47, 3611 (1993), DOI: 10.1103/PhysRevA.47.3611.
- B. Mashhoon, *The hypothesis of locality in relativistic physics*, Phys. Lett. A 145, 147–153 (1990), DOI: 10.1016/0375-9601(90)90670-J.
- S. C. Fletcher, *Light Clocks and the Clock Hypothesis*, Foundations of Physics 43, 1369–1383 (2013), DOI: 10.1007/s10701-013-9751-3.
- M. Bacelar Valente, *What do light clocks say to us regarding the so-called clock hypothesis?*, THEORIA 33, 435–446 (2018), DOI: 10.1387/theoria.18143.

## Next target
**REL Extension 005 — Equivalence Principle / Local Inertial Frame / Gravitational Clock-Rate Gate**.

Key firewalls:
\[
\text{local inertial removability of connection at one event}\neq\text{global removability of curvature},
\]
\[
\text{gravitational clock-rate prediction from a supplied metric}\neq\text{independent derivation of that metric or Einstein dynamics}.
\]
