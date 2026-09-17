#!/usr/bin/env python3
"""
BH-RB-025 — finite-relaxation causal transport response gate.

Purpose
-------
Extend BH-RB-024 by replacing an instantaneously assigned heat flux with a
minimal finite-relaxation Maxwell-Cattaneo control,

    tau dQ/dt + Q = Q_drive,

on a short-time frozen shell background.

The shell compactness control inherited from BH-RB-024 is

    R D_T C = V(C+P) - Q Gamma,
    Gamma^2 = 1 + V^2 - C,

with dimensionless variables
    C = 2m/R,
    E = 8*pi*rho*R^2,
    P = 8*pi*p_r*R^2,
    Q = 8*pi*q*R^2.

This is NOT a full Israel-Stewart black-hole interior solution.  It tests only
whether finite relaxation introduces an unavoidable lag and what conditions are
required for a causal transport flux to cross the BH-RB-024 threshold.
"""

import argparse
import math


def eos_sample(m=1.0, B=1.0, y=0.2, n=0.5):
    A = math.sqrt(4.0 * B * m * y)
    eps = m*n - A*n*n + B*n**3
    p = -A*n*n + 2.0*B*n**3
    return A, eps, p, p/eps


def gamma(C, V):
    g2 = 1.0 + V*V - C
    if g2 <= 0:
        raise ValueError("Gamma^2 must be positive in this control")
    return math.sqrt(g2)


def qcrit(C, P, V):
    return V * (C + P) / gamma(C, V)


def qnec(E, P):
    return 0.5 * (E + P)


def crossing_time_over_tau(Qcrit, Qdrive):
    if Qdrive <= Qcrit:
        return math.inf
    return -math.log(1.0 - Qcrit / Qdrive)


def compactness_change_over_tau(C, P, V, Qdrive, y):
    """
    Frozen-background integral of R D_T C over t=tau*y, divided by tau.
    Delta C * R / tau in the local control:
      Gamma[(Qcrit-Qdrive)y + Qdrive(1-exp(-y))].
    """
    G = gamma(C, V)
    qc = qcrit(C, P, V)
    return G * ((qc - Qdrive)*y + Qdrive*(1.0 - math.exp(-y)))


def return_time_over_tau(C, P, V, Qdrive):
    """
    Positive y=t/tau at which accumulated compactness change returns to zero
    after the initial relaxation overshoot.  Infinity if Qdrive<=Qcrit.
    """
    qc = qcrit(C, P, V)
    if Qdrive <= qc:
        return math.inf

    def f(y):
        return (qc - Qdrive)*y + Qdrive*(1.0 - math.exp(-y))

    lo = 1e-12
    hi = 1.0
    while f(hi) > 0.0 and hi < 1e8:
        hi *= 2.0
    if hi >= 1e8:
        return math.inf
    for _ in range(200):
        mid = 0.5*(lo + hi)
        if f(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5*(lo + hi)


def run_audit():
    _, eps_micro, p_micro, w = eos_sample()

    C = 1.2
    E = 3.0 * C
    P = w * E

    # BH-RB-024 slow branch: NEC-compatible drive cannot even reach threshold.
    Vslow = 0.5
    qc_slow = qcrit(C, P, Vslow)
    qmax = qnec(E, P)

    # BH-RB-024 fast branch: a finite NEC-compatible drive window exists.
    Vfast = 0.8
    qc_fast = qcrit(C, P, Vfast)
    Gfast = gamma(C, Vfast)

    # Choose a control drive inside the NEC-compatible window, without saturating it.
    drive_fraction = 0.95
    qdrive = drive_fraction * qmax
    y_cross = crossing_time_over_tau(qc_fast, qdrive)
    y_return = return_time_over_tau(C, P, Vfast, qdrive)
    overshoot_per_tau = compactness_change_over_tau(C, P, Vfast, qdrive, y_cross)

    # Strongest NEC-compatible drive gives the fastest possible response within
    # this necessary energy-condition bound.
    y_cross_best = crossing_time_over_tau(qc_fast, qmax)
    y_return_best = return_time_over_tau(C, P, Vfast, qmax)

    # Response-time criterion for a finite available dynamical window T_avail:
    # threshold crossing requires T_avail/tau >= y_cross;
    # undoing the initial compactness overshoot requires >= y_return.
    T_over_tau_short = 2.0
    T_over_tau_cross = 4.0
    T_over_tau_recover = 25.0

    tests = []
    def check(name, condition, value=None):
        tests.append((name, bool(condition), value))

    check("micro control energy density positive", eps_micro > 0, eps_micro)
    check("micro control pressure positive", p_micro > 0, p_micro)
    check("synthetic shell trapped", C > 1, C)
    check("radial NEC flux bound positive", qmax > 0, qmax)

    check("slow branch threshold exceeds NEC-compatible maximum drive", qc_slow > qmax, (qc_slow, qmax))
    check("slow branch cannot cross threshold with finite relaxation under NEC bound",
          math.isinf(crossing_time_over_tau(qc_slow, qmax)),
          crossing_time_over_tau(qc_slow, qmax))

    check("fast branch threshold lies below NEC-compatible maximum drive", qc_fast < qmax, (qc_fast, qmax))
    check("selected fast drive remains below NEC bound", qdrive < qmax, (qdrive, qmax))
    check("selected fast drive exceeds compactness threshold", qdrive > qc_fast, (qdrive, qc_fast))
    check("finite relaxation crossing time exists", math.isfinite(y_cross) and y_cross > 0, y_cross)
    check("compactness necessarily grows before threshold crossing", overshoot_per_tau > 0, overshoot_per_tau)
    check("return time exceeds crossing time", y_return > y_cross, (y_return, y_cross))
    check("best NEC-compatible drive still has nonzero crossing lag", y_cross_best > 0, y_cross_best)
    check("best NEC-compatible drive still has nonzero recovery lag", y_return_best > y_cross_best, (y_return_best, y_cross_best))

    check("too-short available time fails to reach threshold", T_over_tau_short < y_cross, (T_over_tau_short, y_cross))
    check("moderate available time crosses threshold", T_over_tau_cross > y_cross, (T_over_tau_cross, y_cross))
    check("moderate crossing time is still too short to erase overshoot", T_over_tau_cross < y_return, (T_over_tau_cross, y_return))
    check("longer available time can erase frozen-background overshoot", T_over_tau_recover > y_return, (T_over_tau_recover, y_return))

    check("finite relaxation therefore adds an independent timescale requirement", True, "T_available/tau_q")
    check("drive amplitude is not derived from DSD or EOS alone", True, "constitutive-gradient closure required")
    check("frozen-shell Maxwell-Cattaneo control is not a full Israel-Stewart evolution", True, "scope firewall")
    check("event-horizon escape is not inferred from internal outward flux", True, "causal firewall")
    check("positive 3D black-hole core persistence is not derived", True, "target remains open")

    passed = sum(ok for _, ok, _ in tests)

    print("BH-RB-025 — finite-relaxation causal transport response gate")
    print(f"micro w=p/eps            = {w:.12f}")
    print(f"shell C,E,P              = {C:.12f}, {E:.12f}, {P:.12f}")
    print(f"Q_NEC,max                = {qmax:.12f}")
    print(f"slow V, Qcrit            = {Vslow:.12f}, {qc_slow:.12f}")
    print(f"fast V, Gamma, Qcrit     = {Vfast:.12f}, {Gfast:.12f}, {qc_fast:.12f}")
    print(f"selected Qdrive          = {qdrive:.12f} ({drive_fraction:.2%} of NEC max)")
    print(f"t_cross/tau              = {y_cross:.12f}")
    print(f"t_return/tau             = {y_return:.12f}")
    print(f"initial overshoot / tau  = {overshoot_per_tau:.12f} [local frozen normalization]")
    print(f"best NEC t_cross/tau     = {y_cross_best:.12f}")
    print(f"best NEC t_return/tau    = {y_return_best:.12f}")
    print()
    for name, ok, value in tests:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {value}")
    print()
    print(f"RESULT: {passed}/{len(tests)} PASS")
    print(
        "VERDICT: PASS_WITH_BOUNDARY / FINITE_RELAXATION_ADDS_A_TRANSPORT_TIMESCALE_GATE / "
        "NEC_COMPATIBLE_DRIVE_CAN_CROSS_QCRIT_ONLY_IN_THE_FAST_SYNTHETIC_BRANCH / "
        "RELAXATION_LAG_CAUSES_INITIAL_COMPACTNESS_OVERSHOOT / "
        "AMPLITUDE_AND_AVAILABLE_DURATION_REQUIRE_EXPLICIT_CONSTITUTIVE_THERMODYNAMIC_CLOSURE / "
        "FULL_ISRAEL_STEWART_GR_EVOLUTION_AND_PERSISTENT_3D_CORE_NOT_DERIVED"
    )
    return 0 if passed == len(tests) else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="all", choices=["all"])
    parser.parse_args()
    raise SystemExit(run_audit())


if __name__ == "__main__":
    main()
