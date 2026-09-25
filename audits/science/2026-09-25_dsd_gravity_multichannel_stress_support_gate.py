#!/usr/bin/env python3
"""
BH-RB-028 — multi-channel causal transport / stress-support gate.

Purpose
-------
BH-RB-027 showed that a one-scale near-equilibrium heat-conduction channel
requires a force-Knudsen number K_F > 1 in the fast trapped-shell control.
BH-RB-028 asks whether anisotropic stress can reduce the radial heat-flux
burden without violating basic energy-condition checks.

This is an algebraic frozen-shell control built on the exact Misner-Sharp
mass-balance structure already used in BH-RB-024:

    R D_T C = V (C + P_r) - Q Gamma,

with C=2m/R, collapse speed V=-U>0, Gamma^2=1+V^2-C,
P_r=8*pi*p_r*R^2, Q=8*pi*q*R^2.

Tangential pressure does not enter this mass-balance equation directly, but
anisotropic stress can change P_r at fixed mean pressure. This does NOT prove
a complete dynamical support mechanism or a persistent finite 3D core.
"""

import argparse
import math


def eos_sample(m=1.0, B=1.0, y=0.2, n=0.5):
    A = math.sqrt(4.0 * B * m * y)
    eps = m*n - A*n*n + B*n**3
    p = -A*n*n + 2.0*B*n**3
    return A, eps, p, p/eps


def shell(C=1.2, V=0.8):
    _, eps_micro, p_micro, w = eos_sample()
    E = 3.0*C
    Pbar = w*E
    Gamma2 = 1.0 + V*V - C
    if Gamma2 <= 0.0:
        raise ValueError("Gamma^2 must be positive")
    Gamma = math.sqrt(Gamma2)
    A_dyn = V/Gamma
    return eps_micro, p_micro, w, E, Pbar, Gamma, A_dyn


def split_pressure(Pbar, delta):
    """delta = P_t - P_r at fixed mean pressure (P_r+2P_t)/3=Pbar."""
    Pr = Pbar - 2.0*delta/3.0
    Pt = Pbar + delta/3.0
    return Pr, Pt


def delta_from_Pr(Pbar, Pr):
    return 1.5*(Pbar-Pr)


def qcrit(C, A_dyn, Pr):
    return A_dyn*(C+Pr)


def qnec_radial(E, Pr):
    return 0.5*(E+Pr)


def heat_fraction(beta_T, v, Kmax):
    """Q_heat,max = h*(E+P_r) for the BH-RB-027 one-scale control."""
    return beta_T*v*Kmax/3.0


def Pr_required_for_heat_closure(C, E, A_dyn, h):
    """
    Solve h(E+Pr) >= A_dyn(C+Pr) at equality.
    For A_dyn>h the heat channel closes only for Pr <= Pr_star.
    """
    if A_dyn <= h:
        return math.inf
    return (h*E - A_dyn*C)/(A_dyn-h)


def type1_eigenframe(E, Pr, Q):
    """
    For orthonormal t-r block T_ab=[[E,Q],[Q,Pr]].
    If D=(E+Pr)^2-4Q^2 > 0, it is type-I diagonalizable in the radial block.
    Return D, rho0, pr0.
    """
    D = (E+Pr)**2 - 4.0*Q*Q
    if D <= 0.0:
        return D, math.nan, math.nan
    root = math.sqrt(D)
    rho0 = 0.5*(E-Pr+root)
    pr0 = 0.5*(Pr-E+root)
    return D, rho0, pr0


def feasibility_ratio(C, E, A_dyn, Pr):
    """Qcrit/Qnec for radial NEC bound."""
    return 2.0*A_dyn*(C+Pr)/(E+Pr)


def run_audit():
    eps_micro, p_micro, w, E, Pbar, Gamma, A_dyn = shell()
    C = 1.2
    beta_T = 0.75
    v = 1.0

    Qcrit_iso = qcrit(C, A_dyn, Pbar)
    Qnec_iso = qnec_radial(E, Pbar)
    ratio_iso = Qcrit_iso/Qnec_iso

    rows = []
    for Kmax in (1.0, 0.3, 0.1):
        h = heat_fraction(beta_T, v, Kmax)
        Pr_star = Pr_required_for_heat_closure(C, E, A_dyn, h)
        delta = delta_from_Pr(Pbar, Pr_star)
        Pr, Pt = split_pressure(Pbar, delta)
        Q = h*(E+Pr)
        Qc = qcrit(C, A_dyn, Pr)
        Qn = qnec_radial(E, Pr)
        D, rho0, pr0 = type1_eigenframe(E, Pr, Q)
        inv_re = max(abs(Pr-Pbar), abs(Pt-Pbar))/(E+Pbar)
        rows.append({
            "K": Kmax, "h": h, "Pr": Pr, "Pt": Pt, "delta": delta,
            "Q": Q, "Qcrit": Qc, "Qnec": Qn, "D": D,
            "rho0": rho0, "pr0": pr0, "inv_re": inv_re,
            "ratio": Qc/Qn,
        })

    # Bulk-viscous sign control: compression Theta_expansion < 0 and zeta>=0
    # gives Pi_bulk=-zeta*Theta_expansion > 0 in Navier-Stokes limit.
    bulk_shift = 0.2
    ratio_bulk = feasibility_ratio(C, E, A_dyn, Pbar+bulk_shift)

    tests = []
    def check(name, condition, value=None):
        tests.append((name, bool(condition), value))

    check("micro EOS sample positive", eps_micro > 0 and p_micro > 0, (eps_micro, p_micro))
    check("fast shell is trapped", C > 1.0, C)
    check("Gamma real", Gamma > 0.0, Gamma)
    check("isotropic fast branch has NEC amplitude window", Qcrit_iso < Qnec_iso, (Qcrit_iso, Qnec_iso))
    check("isotropic heat-only K<=1 remains insufficient", heat_fraction(beta_T,v,1.0)*(E+Pbar) < Qcrit_iso,
          (heat_fraction(beta_T,v,1.0)*(E+Pbar), Qcrit_iso))
    check("feasibility ratio rises with radial pressure in this control", E > C, (E, C))
    check("positive bulk pressure shift worsens Qcrit/Qnec ratio", ratio_bulk > ratio_iso, (ratio_iso, ratio_bulk))

    for row in rows:
        K = row["K"]
        check(f"K={K}: positive tangential anisotropy", row["delta"] > 0.0, row["delta"])
        check(f"K={K}: required radial stress is tension", row["Pr"] < 0.0, row["Pr"])
        check(f"K={K}: heat channel exactly closes Qcrit", abs(row["Q"]-row["Qcrit"]) < 1e-12,
              (row["Q"], row["Qcrit"]))
        check(f"K={K}: radial NEC margin remains", row["Q"] < row["Qnec"], (row["Q"], row["Qnec"]))
        check(f"K={K}: radial block remains type-I", row["D"] > 0.0, row["D"])
        check(f"K={K}: eigenframe energy density positive", row["rho0"] > 0.0, row["rho0"])
        check(f"K={K}: eigenframe radial DEC", row["rho0"] >= abs(row["pr0"]), (row["rho0"], row["pr0"]))
        check(f"K={K}: eigenframe tangential DEC", row["rho0"] >= abs(row["Pt"]), (row["rho0"], row["Pt"]))
        check(f"K={K}: anisotropic correction finite", math.isfinite(row["inv_re"]) and row["inv_re"] > 0.0,
              row["inv_re"])

    # DSD / scope firewalls
    check("tangential stress does not directly replace heat flux in the mass-balance equation", True,
          "it acts here by changing P_r at fixed mean pressure")
    check("diffusion is not added as an independent energy flux without a frame/current closure", True,
          "Landau/Eckart provenance firewall")
    check("formation transition is not treated as a free additive force term", True,
          "it may change the constitutive branch instead")
    check("anisotropic algebraic witness does not prove causal shear generation", True,
          "requires tau_pi, eta, shear-rate closure")
    check("negative radial pressure is tension, not ordinary pressure support", True,
          "interpretation firewall")
    check("same-shell trapped turning point is not inferred", True, "BH-RB-011 firewall")
    check("persistent finite 3D black-hole core is not derived", True, "scope firewall")

    passed = sum(ok for _, ok, _ in tests)

    print("BH-RB-028 — multi-channel causal transport / stress-support gate")
    print(f"EOS: eps={eps_micro:.12f}, p={p_micro:.12f}, w={w:.12f}")
    print(f"shell: C={C:.12f}, E={E:.12f}, Pbar={Pbar:.12f}, Gamma={Gamma:.12f}")
    print(f"isotropic Qcrit={Qcrit_iso:.12f}, Qnec={Qnec_iso:.12f}, ratio={ratio_iso:.12f}")
    print(f"bulk +{bulk_shift:.3f}: ratio={ratio_bulk:.12f}")
    print()
    for row in rows:
        print(
            f"K={row['K']:.1f}: Pr={row['Pr']:.12f}, Pt={row['Pt']:.12f}, "
            f"Delta={row['delta']:.12f}, Q={row['Q']:.12f}, "
            f"Qnec={row['Qnec']:.12f}, invRe_proxy={row['inv_re']:.12f}"
        )
    print()
    for name, ok, value in tests:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {value}")

    print()
    print(f"RESULT: {passed}/{len(tests)} PASS")
    print(
        "VERDICT: PASS_WITH_BOUNDARY / "
        "POSITIVE_TANGENTIAL_ANISOTROPY_CAN_REDUCE_RADIAL_HEAT_FLUX_BURDEN_IN_FROZEN_SHELL_CONTROL / "
        "ALGEBRAIC_TYPE_I_DEC_COMPATIBLE_WITNESSES_EXIST_EVEN_FOR_KF_LE_1 / "
        "COMPRESSIVE_BULK_VISCOUS_PRESSURE_DOES_NOT_HELP_THIS_COMPACTNESS_GATE / "
        "DIFFUSION_AND_FORMATION_CHANGE_REQUIRE_SEPARATE_PROVENANCE / "
        "CAUSAL_SHEAR_STRESS_GENERATION_NOT_DERIVED / "
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
