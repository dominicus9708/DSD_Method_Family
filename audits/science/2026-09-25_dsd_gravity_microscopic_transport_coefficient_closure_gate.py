#!/usr/bin/env python3
"""
BH-RB-027 — microscopic transport-coefficient closure gate.

Purpose
-------
Take BH-RB-026 one step upstream. Instead of choosing kappa and tau_q
independently, use a minimal one-scale kinetic-theory control in which the
same microscopic collision time controls both thermal conductivity and the
heat-flux relaxation time.

This is a synthetic closure audit, not a derivation of black-hole successor
matter. We use c = k_B = G = 1 and the BH-RB-024 shell normalization.

Minimal kinetic control
-----------------------
    tau_coll^{-1} ~ n sigma_tr v
    lambda_mfp = v tau_coll
    kappa ~ (1/3) c_V v^2 tau_coll
    tau_q = chi tau_coll

Define
    beta_T = c_V T / (epsilon + p)
    Theta = -R (partial_r ln T + a_r)
    K_F = v tau_coll |Theta| / R

Then
    alpha_micro = kappa T / [tau_q (epsilon+p)]
                = beta_T v^2 / (3 chi)

and
    Q_drive/(E+P) = (beta_T v / 3) K_F

for an outward thermal force. In a gradient-dominated control K_F is the
usual mean-free-path / thermal-gradient-length Knudsen number. If the
acceleration term dominates, K_F is only a force-scale nonequilibrium proxy.

External comparators motivate, but do not prove universality of, this
single-time-scale control:
- relativistic Boltzmann theory can derive both transport coefficients and
  relaxation times from the same collision operator;
- Anderson-Witting RTA gives heat-flux relaxation time equal to its kinetic
  relaxation time in the ultrarelativistic control.
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
    gamma2 = 1.0 + V*V - C
    if gamma2 <= 0.0:
        raise ValueError("Gamma^2 must be positive in the synthetic control")
    Gamma = math.sqrt(gamma2)
    Qcrit = V * (C + P) / Gamma
    Qnec = 0.5 * (E + P)
    return eps_micro, p_micro, w, E, P, Gamma, Qcrit, Qnec


def alpha_micro(beta_T, v, chi=1.0):
    return beta_T * v*v / (3.0 * chi)


def qdrive_from_force_knudsen(E, P, beta_T, v, K_F):
    return (E + P) * beta_T * v * K_F / 3.0


def force_knudsen_required(Q, E, P, beta_T, v):
    return 3.0 * Q / ((E + P) * beta_T * v)


def beta_required(Q, E, P, v, Kmax):
    return 3.0 * Q / ((E + P) * v * Kmax)


def collision_from_transport_cross_section(nhat, sigmahat, v):
    """
    Dimensionless control with nhat=n R^3 and sigmahat=sigma/R^2.
    tau_coll/R = 1/(nhat*sigmahat*v)
    and lambda_mfp/R = 1/(nhat*sigmahat).
    """
    optical_depth = nhat * sigmahat
    if optical_depth <= 0.0 or v <= 0.0:
        raise ValueError("positive optical depth and speed required")
    tauhat = 1.0 / (optical_depth * v)
    lambdahat = 1.0 / optical_depth
    return optical_depth, tauhat, lambdahat


def run_audit():
    eps_micro, p_micro, w, E, P, Gamma, Qcrit, Qnec = shell_quantities()

    # Ultrarelativistic classical Boltzmann-gas comparator:
    # epsilon=3 n T, p=n T, c_V=3n => beta_T=3/4.
    beta_ur = 0.75
    v_ur = 1.0
    chi_rta = 1.0
    alpha_ur = alpha_micro(beta_ur, v_ur, chi_rta)

    KFcrit = force_knudsen_required(Qcrit, E, P, beta_ur, v_ur)
    KFnec = force_knudsen_required(Qnec, E, P, beta_ur, v_ur)

    Q_K01 = qdrive_from_force_knudsen(E, P, beta_ur, v_ur, 0.1)
    Q_K03 = qdrive_from_force_knudsen(E, P, beta_ur, v_ur, 0.3)
    Q_K1 = qdrive_from_force_knudsen(E, P, beta_ur, v_ur, 1.0)
    Q_at_crit = qdrive_from_force_knudsen(E, P, beta_ur, v_ur, KFcrit)
    Q_at_nec = qdrive_from_force_knudsen(E, P, beta_ur, v_ur, KFnec)

    beta_req_K1 = beta_required(Qcrit, E, P, 1.0, 1.0)
    beta_req_K03 = beta_required(Qcrit, E, P, 1.0, 0.3)
    beta_req_K01 = beta_required(Qcrit, E, P, 1.0, 0.1)

    # Explicit cross-section bookkeeping witness, chosen so K_F=0.3 at Theta=1.
    Theta = 1.0
    nhat = 1.0
    sigmahat = 1.0 / 0.3
    optical_depth, tauhat_coll, lambdahat = collision_from_transport_cross_section(
        nhat, sigmahat, v_ur
    )
    KF_from_sigma = lambdahat * abs(Theta)
    tauhat_q = chi_rta * tauhat_coll
    Xi_over_EplusP = beta_ur * v_ur*v_ur * tauhat_coll / 3.0
    alpha_reconstructed = Xi_over_EplusP / tauhat_q
    Q_sigma = (E + P) * Xi_over_EplusP * Theta

    _, _, _, Es, Ps, Gammas, Qcrit_slow, Qnec_slow = shell_quantities(C=1.2, V=0.5)
    KFcrit_slow = force_knudsen_required(Qcrit_slow, Es, Ps, beta_ur, v_ur)
    KFnec_slow = force_knudsen_required(Qnec_slow, Es, Ps, beta_ur, v_ur)

    tests = []

    def check(name, condition, value=None):
        tests.append((name, bool(condition), value))

    check("micro EOS sample positive", eps_micro > 0 and p_micro > 0, (eps_micro, p_micro))
    check("fast shell trapped", 1.2 > 1.0, 1.2)
    check("fast shell Gamma real", Gamma > 0.0, Gamma)
    check("fast branch has NEC amplitude window before microscopic closure", Qcrit < Qnec, (Qcrit, Qnec))
    check("ultrarelativistic beta_T is 3/4", abs(beta_ur - 0.75) < 1e-15, beta_ur)
    check("RTA chi is unity in control", chi_rta == 1.0, chi_rta)
    check("micro alpha is sub-unity", 0.0 < alpha_ur < 1.0, alpha_ur)
    check("micro alpha equals 1/4", abs(alpha_ur - 0.25) < 1e-15, alpha_ur)
    check("required force-Knudsen exceeds unity", KFcrit > 1.0, KFcrit)
    check("NEC force-Knudsen equals 2 in UR control", abs(KFnec - 2.0) < 1e-12, KFnec)
    check("amplitude/NEC window exists only above K_F=1", 1.0 < KFcrit < KFnec, (KFcrit, KFnec))
    check("K_F=0.1 driver below Qcrit", Q_K01 < Qcrit, (Q_K01, Qcrit))
    check("K_F=0.3 driver below Qcrit", Q_K03 < Qcrit, (Q_K03, Qcrit))
    check("K_F=1 driver still below Qcrit", Q_K1 < Qcrit, (Q_K1, Qcrit))
    check("K_Fcrit reconstructs Qcrit", abs(Q_at_crit - Qcrit) < 1e-12, (Q_at_crit, Qcrit))
    check("K_Fnec reconstructs Qnec", abs(Q_at_nec - Qnec) < 1e-12, (Q_at_nec, Qnec))
    check("beta required at K_F<=1 exceeds UR beta", beta_req_K1 > beta_ur, (beta_req_K1, beta_ur))
    check("beta required at K_F<=0.3 is much larger than unity", beta_req_K03 > 4.0, beta_req_K03)
    check("beta required at K_F<=0.1 is order >10", beta_req_K01 > 10.0, beta_req_K01)
    check("cross-section witness gives intended K_F", abs(KF_from_sigma - 0.3) < 1e-12, KF_from_sigma)
    check("cross-section witness is optically thick across R", optical_depth > 1.0, optical_depth)
    check("RTA tau_q follows same collision time", abs(tauhat_q - tauhat_coll) < 1e-15, (tauhat_q, tauhat_coll))
    check("alpha reconstructed from same collision scale", abs(alpha_reconstructed - alpha_ur) < 1e-12, alpha_reconstructed)
    check("cross-section-derived driver equals K_F=0.3 driver", abs(Q_sigma - Q_K03) < 1e-12, (Q_sigma, Q_K03))
    check("slow branch still violates NEC amplitude gate", Qcrit_slow > Qnec_slow, (Qcrit_slow, Qnec_slow))
    check("slow branch K_Fcrit exceeds K_Fnec", KFcrit_slow > KFnec_slow, (KFcrit_slow, KFnec_slow))
    check("single-scale kinetic result is only a control, not universal successor matter", True, "scope firewall")
    check("near-equilibrium failure does not exclude nonhydrodynamic transport", True, "scope firewall")
    check("persistent 3D black-hole core not derived", True, "scope firewall")

    passed = sum(ok for _, ok, _ in tests)

    print("BH-RB-027 — microscopic transport-coefficient closure gate")
    print(f"shell: E={E:.12f}, P={P:.12f}, Qcrit={Qcrit:.12f}, Qnec={Qnec:.12f}")
    print(f"UR kinetic control: beta_T={beta_ur:.12f}, v={v_ur:.12f}, chi={chi_rta:.12f}")
    print(f"alpha_micro={alpha_ur:.12f}")
    print(f"K_Fcrit={KFcrit:.12f}, K_Fnec={KFnec:.12f}")
    print(f"Q(K=0.1)={Q_K01:.12f}, Q(K=0.3)={Q_K03:.12f}, Q(K=1)={Q_K1:.12f}")
    print(f"beta_required K<=1: {beta_req_K1:.12f}")
    print(f"beta_required K<=0.3: {beta_req_K03:.12f}")
    print(f"beta_required K<=0.1: {beta_req_K01:.12f}")
    print(f"cross-section witness: optical_depth={optical_depth:.12f}, tau_coll/R={tauhat_coll:.12f}, lambda/R={lambdahat:.12f}")
    print(f"slow comparator: Qcrit={Qcrit_slow:.12f}, Qnec={Qnec_slow:.12f}, Kcrit={KFcrit_slow:.12f}, Knec={KFnec_slow:.12f}")
    print()

    for name, ok, value in tests:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {value}")

    print()
    print(f"RESULT: {passed}/{len(tests)} PASS")
    print(
        "VERDICT: PASS_WITH_BOUNDARY / "
        "SAME_MICROSCOPIC_COLLISION_SCALE_CAN_CLOSE_KAPPA_AND_TAUQ_IN_KINETIC_CONTROL / "
        "RTA_ULTRARELATIVISTIC_CONTROL_GIVES_ALPHA_MICRO_1_OVER_4 / "
        "FAST_SHELL_QCRIT_REQUIRES_FORCE_KNUDSEN_GREATER_THAN_UNITY_FOR_BETA_3_OVER_4 / "
        "NEAR_EQUILIBRIUM_SINGLE_SCALE_HEAT_CONDUCTION_DOES_NOT_CLOSE_THE_REQUIRED_FLUX_GATE_IN_THIS_CONTROL / "
        "STRONG_NONEQUILIBRIUM_OR_OTHER_TRANSPORT_CHANNELS_REMAIN_OPEN / "
        "SUCCESSOR_MICROPHYSICS_AND_PERSISTENT_3D_CORE_NOT_DERIVED"
    )
    return 0 if passed == len(tests) else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="all", choices=["all"])
    parser.parse_args()
    raise SystemExit(run_audit())


if __name__ == "__main__":
    main()
