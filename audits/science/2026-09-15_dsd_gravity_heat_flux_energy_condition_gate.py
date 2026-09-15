#!/usr/bin/env python3
"""
BH-RB-024 — internal heat-flux / energy-condition admissibility gate.

Purpose
-------
Starting from the trapped-region dynamic constraint already established in the
canonical BH-RB-022/023 line, test whether the outward internal flux required
to make Misner-Sharp compactness nonincreasing can satisfy necessary local
energy-condition bounds.

All dynamical relations use geometrized units G=c=1. Dimensionless shell
variables are used to avoid mixing the normalized microphysical EOS units with
an arbitrary radius:

    C = 2m/R
    E = 8*pi*rho*R^2
    P = 8*pi*p_r*R^2
    Q = 8*pi*q*R^2

The homogeneous-density relation E=3C is used only as a synthetic control.
It is not asserted for a black-hole successor core.
"""

import argparse
import math


def eos_sample(m=1.0, B=1.0, y=0.2, n=0.5):
    """Return normalized BH-RB-020/021 local EOS sample."""
    A = math.sqrt(4.0 * B * m * y)
    eps = m*n - A*n*n + B*n**3
    p = -A*n*n + 2.0*B*n**3
    return A, eps, p, p/eps


def gamma(C, V):
    """Gamma for collapse speed parameter V=-U>0."""
    g2 = 1.0 + V*V - C
    if g2 < 0:
        raise ValueError("Unphysical control: Gamma^2 < 0")
    return math.sqrt(g2)


def qcrit_dimless(C, P, V):
    """
    Qcrit = V(C+P)/Gamma from R D_T C = V(C+P) - Q Gamma.
    """
    Gm = gamma(C, V)
    return V * (C + P) / Gm


def radial_nec_qmax(E, P):
    """Necessary radial NEC bound for |Q|: E+P >= 2|Q|."""
    return 0.5 * (E + P)


def comoving_dec_qmax(E):
    """
    Necessary (not sufficient) DEC condition from causal comoving energy flux:
    |Q| <= E.
    """
    return E


def r_cdot_dimless(C, P, Q, V):
    """R D_T C for U=-V in the spherical dissipative control."""
    return V * (C + P) - Q * gamma(C, V)


def critical_V_for_nec(C, E, P):
    """
    Solve Qcrit <= (E+P)/2 for V, when the asymptotic ratio permits it.
    Let Anec=(E+P)/(2(C+P)).  Because V/Gamma > 1 for C>1,
    a solution requires Anec>1.  Equality gives
      V^2 = Anec^2 (C-1)/(Anec^2-1).
    """
    Anec = (E + P) / (2.0 * (C + P))
    if Anec <= 1.0:
        return math.inf, Anec
    v2 = Anec*Anec*(C - 1.0)/(Anec*Anec - 1.0)
    return math.sqrt(v2), Anec


def run_audit():
    Acoef, eps_micro, p_micro, w = eos_sample()

    # Synthetic homogeneous spherical shell control.
    C = 1.2
    E = 3.0 * C               # E=8*pi*rho R^2 for uniform-density m=4*pi rho R^3/3
    P = w * E                 # retain only p/rho from the normalized EOS sample

    V_slow = 0.5
    G_slow = gamma(C, V_slow)
    Qcrit_slow = qcrit_dimless(C, P, V_slow)
    Qnec = radial_nec_qmax(E, P)
    Qdec_comoving = comoving_dec_qmax(E)
    Rc_slow_nec = r_cdot_dimless(C, P, Qnec, V_slow)

    Vcrit, Anec = critical_V_for_nec(C, E, P)
    Qcrit_at_vcrit = qcrit_dimless(C, P, Vcrit)
    Rc_at_vcrit = r_cdot_dimless(C, P, Qnec, Vcrit)

    V_fast = 0.8
    G_fast = gamma(C, V_fast)
    Qcrit_fast = qcrit_dimless(C, P, V_fast)
    Rc_fast_nec = r_cdot_dimless(C, P, Qnec, V_fast)

    tests = []
    def check(name, condition, value=None):
        tests.append((name, bool(condition), value))

    check("micro EOS sample has positive energy density", eps_micro > 0, eps_micro)
    check("micro EOS sample has positive pressure", p_micro > 0, p_micro)
    check("pressure ratio is sub-unity", 0 < w < 1, w)
    check("synthetic shell is strictly trapped", C > 1, C)
    check("homogeneous control E=3C positive", E > 0, E)
    check("dimensionless pressure positive", P > 0, P)
    check("slow control Gamma real", G_slow > 0, G_slow)
    check("slow qcrit positive", Qcrit_slow > 0, Qcrit_slow)
    check("slow qcrit violates radial NEC necessary bound", Qcrit_slow > Qnec, (Qcrit_slow, Qnec))
    check("slow qcrit still below comoving flux-energy necessary bound", Qcrit_slow < Qdec_comoving, (Qcrit_slow, Qdec_comoving))
    check("NEC-saturating slow flux cannot reduce compactness", Rc_slow_nec > 0, Rc_slow_nec)
    check("NEC feasibility factor exceeds unity", Anec > 1, Anec)
    check("finite critical collapse parameter exists", math.isfinite(Vcrit) and Vcrit > math.sqrt(C-1), Vcrit)
    check("qcrit equals radial NEC bound at Vcrit", abs(Qcrit_at_vcrit - Qnec) < 1e-10, (Qcrit_at_vcrit, Qnec))
    check("compactness derivative vanishes at Vcrit with NEC-saturating flux", abs(Rc_at_vcrit) < 1e-10, Rc_at_vcrit)
    check("fast control Gamma real", G_fast > 0, G_fast)
    check("fast qcrit lies within radial NEC necessary bound", Qcrit_fast < Qnec, (Qcrit_fast, Qnec))
    check("NEC-saturating fast flux decreases compactness", Rc_fast_nec < 0, Rc_fast_nec)
    check("fast qcrit lies within comoving DEC necessary bound", Qcrit_fast < Qdec_comoving, (Qcrit_fast, Qdec_comoving))

    passed = sum(ok for _, ok, _ in tests)

    print("BH-RB-024 — internal heat-flux / energy-condition admissibility gate")
    print(f"micro: A={Acoef:.12f}, eps={eps_micro:.12f}, p={p_micro:.12f}, w=p/eps={w:.12f}")
    print(f"shell: C={C:.12f}, E={E:.12f}, P={P:.12f}")
    print(f"radial NEC Qmax={(Qnec):.12f}, comoving DEC necessary Qmax={Qdec_comoving:.12f}")
    print(f"slow V={V_slow:.12f}, Gamma={G_slow:.12f}, Qcrit={Qcrit_slow:.12f}, R*Cdot@NECmax={Rc_slow_nec:.12f}")
    print(f"Vcrit_NEC={Vcrit:.12f}, Qcrit(Vcrit)={Qcrit_at_vcrit:.12f}, R*Cdot={Rc_at_vcrit:.12e}")
    print(f"fast V={V_fast:.12f}, Gamma={G_fast:.12f}, Qcrit={Qcrit_fast:.12f}, R*Cdot@NECmax={Rc_fast_nec:.12f}")
    print()
    for name, ok, value in tests:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {value}")
    print()
    print(f"RESULT: {passed}/{len(tests)} PASS")
    print("VERDICT: PASS_WITH_BOUNDARY / LOCAL_NEC_COMPATIBLE_INTERNAL_FLUX_WINDOW_EXISTS_IN_SYNTHETIC_CONTROL / SLOW_COLLAPSE_CONTROL_REQUIRES_RADIAL_NEC_VIOLATION / NEC_COMPATIBILITY_IS_NOT_FULL_DEC_OR_TRANSPORT_CLOSURE / GLOBAL_DETRAPPING_AND_POSITIVE_RADIUS_CORE_NOT_DERIVED")
    return 0 if passed == len(tests) else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="all", choices=["all"])
    parser.parse_args()
    raise SystemExit(run_audit())


if __name__ == "__main__":
    main()
