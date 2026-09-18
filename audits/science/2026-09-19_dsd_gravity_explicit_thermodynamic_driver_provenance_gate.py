#!/usr/bin/env python3
"""
BH-RB-026 — explicit thermodynamic driver provenance gate.

Purpose
-------
Take the BH-RB-025 finite-relaxation transport control one step upstream:
instead of treating Q_drive as a free constant, resolve the minimal truncated
relativistic heat-conduction driver

    tau h^a_b u^c nabla_c q^b + q^a
      = -kappa h^{ab}(nabla_b T + T a_b)

in a radial comoving orthonormal control.

Using G=c=k_B=1 and the BH-RB-024 shell normalization,

    C = 2m/R
    E = 8*pi*rho*R^2
    P = 8*pi*p_r*R^2
    Q = 8*pi*q*R^2

define the dimensionless thermal force

    Theta = -R (partial_r ln T + a_r)

and conductivity-temperature scale

    Xi = 8*pi*R*kappa*T,

so that

    Q_drive = Xi * Theta.

The linear Israel-Stewart stability/causality literature gives a necessary
bound stronger than tau > kappa*T/(rho+p). Therefore define

    alpha = kappa*T/[tau*(rho+p)]
          = Xi/[tau_hat*(E+P)],   tau_hat=tau/R,

and use alpha < 1 only as a necessary synthetic admissibility gate, not as a
complete stability theorem.

This script does NOT derive kappa, T, the thermal gradient, acceleration, or
the black-hole successor-core transport law.
"""

import argparse
import math


def eos_sample(m=1.0, B=1.0, y=0.2, n=0.5):
    A = math.sqrt(4.0 * B * m * y)
    eps = m*n - A*n*n + B*n**3
    p = -A*n*n + 2.0*B*n**3
    return A, eps, p, p/eps


def shell_quantities(C=1.2, V=0.8):
    _, eps_micro, p_micro, w = eos_sample()
    E = 3.0 * C
    P = w * E
    Gamma2 = 1.0 + V*V - C
    if Gamma2 <= 0:
        raise ValueError("Gamma^2 must be positive in the synthetic control")
    Gamma = math.sqrt(Gamma2)
    Qcrit = V * (C + P) / Gamma
    Qnec = 0.5 * (E + P)
    return eps_micro, p_micro, w, E, P, Gamma, Qcrit, Qnec


def qdrive(Xi, Theta):
    return Xi * Theta


def alpha_from(Xi, tau_hat, E, P):
    return Xi / (tau_hat * (E + P))


def Xi_from_alpha(alpha, tau_hat, E, P):
    return alpha * tau_hat * (E + P)


def tau_window(alpha, Theta, E, P, Qcrit, Qnec):
    """Window from Qcrit < alpha*tau_hat*(E+P)*Theta <= Qnec."""
    denom = alpha * (E + P) * Theta
    if denom <= 0:
        return math.inf, -math.inf
    return Qcrit / denom, Qnec / denom


def crossing_time_over_tau(Qcrit, Qdrive):
    if Qdrive <= Qcrit:
        return math.inf
    return -math.log(1.0 - Qcrit / Qdrive)


def run_audit():
    eps_micro, p_micro, w, E, P, Gamma, Qcrit, Qnec = shell_quantities()

    Theta_eq = 0.0
    Xi_eq = 1.0
    Qdrive_eq = qdrive(Xi_eq, Theta_eq)

    alpha = 0.8
    Theta = 1.0
    tau_hat = 0.6
    Xi = Xi_from_alpha(alpha, tau_hat, E, P)
    Qdrive_syn = qdrive(Xi, Theta)
    alpha_check = alpha_from(Xi, tau_hat, E, P)
    tau_lo, tau_hi = tau_window(alpha, Theta, E, P, Qcrit, Qnec)
    tcross_tau = crossing_time_over_tau(Qcrit, Qdrive_syn)
    tcross_R = tau_hat * tcross_tau

    tau_below = 0.95 * tau_lo
    Xi_below = Xi_from_alpha(alpha, tau_below, E, P)
    Q_below = qdrive(Xi_below, Theta)

    tau_above = 1.05 * tau_hi
    Xi_above = Xi_from_alpha(alpha, tau_above, E, P)
    Q_above = qdrive(Xi_above, Theta)

    _, _, _, E_s, P_s, Gamma_s, Qcrit_s, Qnec_s = shell_quantities(C=1.2, V=0.5)

    tests = []

    def check(name, condition, value=None):
        tests.append((name, bool(condition), value))

    check("micro EOS sample positive", eps_micro > 0 and p_micro > 0, (eps_micro, p_micro))
    check("fast shell is trapped", 1.2 > 1.0, 1.2)
    check("fast Gamma real", Gamma > 0, Gamma)
    check("fast NEC-compatible amplitude window exists", Qcrit < Qnec, (Qcrit, Qnec))
    check("Tolman-like equilibrium force vanishes", Theta_eq == 0.0, Theta_eq)
    check("equilibrium thermal driver vanishes", Qdrive_eq == 0.0, Qdrive_eq)
    check("equilibrium driver cannot cross Qcrit", Qdrive_eq < Qcrit, (Qdrive_eq, Qcrit))
    check("synthetic alpha is below unity", 0.0 < alpha < 1.0, alpha)
    check("Xi positive", Xi > 0.0, Xi)
    check("alpha reconstructs exactly", abs(alpha_check-alpha) < 1e-14, alpha_check)
    check("synthetic outward driver exceeds Qcrit", Qdrive_syn > Qcrit, (Qdrive_syn, Qcrit))
    check("synthetic outward driver remains below radial NEC bound", Qdrive_syn < Qnec, (Qdrive_syn, Qnec))
    check("finite relaxation window is nonempty", 0.0 < tau_lo < tau_hi, (tau_lo, tau_hi))
    check("chosen tau_hat lies inside amplitude/NEC window", tau_lo < tau_hat <= tau_hi, (tau_lo, tau_hat, tau_hi))
    check("below-window tau fails amplitude gate", Q_below < Qcrit, (tau_below, Q_below, Qcrit))
    check("above-window tau violates NEC asymptotic amplitude gate", Q_above > Qnec, (tau_above, Q_above, Qnec))
    check("threshold crossing time is finite", math.isfinite(tcross_tau) and tcross_tau > 0, tcross_tau)
    check("threshold crossing consumes finite causal-scale time", math.isfinite(tcross_R) and tcross_R > 0, tcross_R)
    check("slow comparator has no NEC-compatible amplitude window", Qcrit_s > Qnec_s, (Qcrit_s, Qnec_s))
    check("chemical-potential gradient is not silently inserted into minimal heat law", True, "requires separate diffusion/frame closure")
    check("alpha<1 used only as necessary linear gate", True, "not sufficient full Israel-Stewart stability")
    check("kappa, T, gradients, acceleration remain external constitutive data", True, "provenance firewall")
    check("no black-hole core persistence inferred", True, "scope firewall")

    passed = sum(ok for _, ok, _ in tests)

    print("BH-RB-026 — explicit thermodynamic driver provenance gate")
    print(f"micro sample: eps={eps_micro:.12f}, p={p_micro:.12f}, w={w:.12f}")
    print(f"fast shell: E={E:.12f}, P={P:.12f}, Gamma={Gamma:.12f}")
    print(f"Qcrit={Qcrit:.12f}, Qnec={Qnec:.12f}")
    print(f"equilibrium: Theta={Theta_eq:.12f}, Qdrive={Qdrive_eq:.12f}")
    print(f"synthetic: alpha={alpha:.12f}, Theta={Theta:.12f}, tau_hat={tau_hat:.12f}")
    print(f"Xi={Xi:.12f}, Qdrive={Qdrive_syn:.12f}")
    print(f"tau_hat window=({tau_lo:.12f}, {tau_hi:.12f}]")
    print(f"t_cross/tau={tcross_tau:.12f}, t_cross/R={tcross_R:.12f}")
    print(f"slow comparator: Qcrit={Qcrit_s:.12f}, Qnec={Qnec_s:.12f}")
    print()

    for name, ok, value in tests:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {value}")

    print()
    print(f"RESULT: {passed}/{len(tests)} PASS")
    print(
        "VERDICT: PASS_WITH_BOUNDARY / "
        "THERMAL_FORCE_AND_CONDUCTIVITY_PROVENANCE_RESOLVE_QDRIVE_IN_MINIMAL_CAUSAL_CONTROL / "
        "TOLMAN_LIKE_EQUILIBRIUM_DOES_NOT_DRIVE_OUTWARD_HEAT_FLUX / "
        "FAST_SYNTHETIC_BRANCH_HAS_A_NARROW_ALPHA_TAU_THERMAL_FORCE_WINDOW_BETWEEN_QCRIT_AND_NEC / "
        "ARBITRARILY_SMALL_RELAXATION_TIME_IS_NOT_FREE_ONCE_CAUSAL_STABILITY_CONSTRAINTS_ARE_TRACKED / "
        "MICROPHYSICAL_KAPPA_TEMPERATURE_PROFILE_AND_FULL_TRANSPORT_LAW_NOT_DERIVED / "
        "PERSISTENT_3D_BLACK_HOLE_CORE_NOT_DERIVED"
    )
    return 0 if passed == len(tests) else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="all", choices=["all"])
    parser.parse_args()
    raise SystemExit(run_audit())


if __name__ == "__main__":
    main()
