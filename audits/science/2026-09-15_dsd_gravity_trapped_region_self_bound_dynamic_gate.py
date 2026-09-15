#!/usr/bin/env python3
"""
BH-RB-022 — trapped-region self-bound EOS dynamic closure gate.

Purpose
-------
Audit whether the globally causal, self-bound EOS family constructed in
BH-RB-021 is by itself sufficient to produce a positive-radius turnaround
inside a spherically symmetric trapped region.

All Misner-Sharp dynamical formulas below use geometrized units G=c=1.
This is an audit/control script, not a full numerical-relativity solver.
"""

import argparse
import math


def low_density_eos(n: float, m: float = 1.0, A: float = math.sqrt(0.8), B: float = 1.0):
    """BH-RB-020 local self-binding branch in normalized units."""
    eps = m*n - A*n*n + B*n**3
    p = -A*n*n + 2.0*B*n**3
    deps_dn = m - 2.0*A*n + 3.0*B*n*n
    dp_dn = -2.0*A*n + 6.0*B*n*n
    cs2 = dp_dn / deps_dn
    return eps, p, cs2


def gamma_sq(C: float, U: float) -> float:
    """Misner-Sharp kinematic identity: Gamma^2 = 1 + U^2 - C, C=2m/R."""
    return 1.0 + U*U - C


def dm_dt_perfect(R: float, p: float, U: float) -> float:
    """No-flux perfect-fluid Misner-Sharp mass change: D_t m = -4 pi p U R^2."""
    return -4.0 * math.pi * p * U * R*R


def dC_dt_perfect(C: float, R: float, p: float, U: float) -> float:
    """D_t C for C=2m/R in the no-flux perfect-fluid branch."""
    return (-U / R) * (C + 8.0 * math.pi * p * R*R)


def dC_dt_flux(C: float, R: float, p: float, U: float, q: float, Gamma: float) -> float:
    """
    Dissipative spherical control:
      D_t m = -4 pi R^2 (p U + q Gamma)
    so
      D_t C = -8 pi R (p U + q Gamma) - C U/R.
    Positive q is outward in the comoving convention used here.
    """
    return -8.0 * math.pi * R * (p * U + q * Gamma) - C * U / R


def qcrit_for_nonincreasing_compactness(C: float, R: float, p: float, U: float, Gamma: float) -> float:
    """Threshold q for D_t C <= 0 when U<0 and Gamma>0."""
    V = -U
    return V * (p + C / (8.0 * math.pi * R*R)) / Gamma


def run_audit():
    # BH-RB-021 normalized self-bound control.
    m = 1.0
    B = 1.0
    y = 0.2
    A = math.sqrt(4.0 * B * m * y)
    n_star = A / (2.0 * B)
    n_causal = math.sqrt(m / (3.0 * B))

    # Pick a density inside the causal low-density branch and above self-bound surface.
    n = 0.5
    eps, p, cs2 = low_density_eos(n, m=m, A=A, B=B)

    # Trapped collapsing shell control. Must satisfy Gamma^2 >= 0.
    R = 1.0
    C = 1.2
    U = -0.5
    gsq = gamma_sq(C, U)
    Gamma = math.sqrt(gsq)

    mdot = dm_dt_perfect(R, p, U)
    Cdot0 = dC_dt_perfect(C, R, p, U)
    qcrit = qcrit_for_nonincreasing_compactness(C, R, p, U, Gamma)
    Cdot_crit = dC_dt_flux(C, R, p, U, qcrit, Gamma)
    Cdot_super = dC_dt_flux(C, R, p, U, 1.1*qcrit, Gamma)

    tests = []
    def check(name, condition, value=None):
        tests.append((name, bool(condition), value))

    check("self-bound surface finite", n_star > 0, n_star)
    check("chosen density above surface", n > n_star, n)
    check("chosen density below causal cutoff", n < n_causal, n_causal)
    check("pressure positive inside compressed phase", p > 0, p)
    check("sound speed causal in local branch", 0 <= cs2 <= 1, cs2)
    check("control shell trapped", C > 1, C)
    check("Misner-Sharp Gamma^2 regular", gsq >= 0, gsq)
    check("collapse velocity negative", U < 0, U)
    check("positive pressure work raises m during collapse", mdot > 0, mdot)
    check("no-flux compactness grows", Cdot0 > 0, Cdot0)
    check("turnaround inside C>1 impossible by Gamma^2=1-C at U=0", 1.0 - C < 0, 1.0-C)
    check("finite outward-flux threshold positive", qcrit > 0, qcrit)
    check("flux threshold gives zero compactness derivative", abs(Cdot_crit) < 1e-12, Cdot_crit)
    check("supercritical outward flux decreases compactness", Cdot_super < 0, Cdot_super)
    pcrit_tension = -C / (8.0 * math.pi * R*R)
    check("no-flux nonincreasing C would require negative pressure", pcrit_tension < 0, pcrit_tension)
    check("BH-RB-021 positive-pressure branch does not meet tension criterion", p > pcrit_tension, (p, pcrit_tension))

    passed = sum(ok for _, ok, _ in tests)

    print("BH-RB-022 — trapped-region self-bound EOS dynamic closure gate")
    print(f"A={A:.12f}, n*={n_star:.12f}, n_causal={n_causal:.12f}")
    print(f"sample: n={n:.6f}, eps={eps:.12f}, p={p:.12f}, cs2={cs2:.12f}")
    print(f"shell: C={C:.6f}, U={U:.6f}, Gamma={Gamma:.12f}")
    print(f"D_t m(no flux)={mdot:.12f}")
    print(f"D_t C(no flux)={Cdot0:.12f}")
    print(f"q_crit={qcrit:.12f}")
    print(f"D_t C(q=qcrit)={Cdot_crit:.12e}")
    print(f"D_t C(q=1.1 qcrit)={Cdot_super:.12f}")
    print(f"p_crit(no-flux, D_t C<=0)={pcrit_tension:.12f}")
    print()
    for name, ok, value in tests:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {value}")
    print()
    print(f"RESULT: {passed}/{len(tests)} PASS")
    print("VERDICT: PASS_WITH_BOUNDARY / SELF_BOUND_CAUSAL_EOS_DOES_NOT_BY_ITSELF_PRODUCE_TRAPPED_REGION_TURNAROUND / OUTWARD_FLUX_OR_OTHER_NONPERFECT_DYNAMIC_CHANNEL_REQUIRED / POSITIVE_RADIUS_CORE_NOT_YET_DERIVED")
    return 0 if passed == len(tests) else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="all", choices=["all"])
    parser.parse_args()
    raise SystemExit(run_audit())


if __name__ == "__main__":
    main()
