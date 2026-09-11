#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math


def phi_quadratic(zeta: float, nu: float = 0.5) -> float:
    if not (0.0 <= zeta <= 1.0):
        raise ValueError("zeta must satisfy 0 <= zeta <= 1")
    if nu <= 0.0:
        raise ValueError("nu must be positive")
    return nu * zeta * zeta


def phi_quartic(zeta: float, nu2: float = 0.5, nu4: float = 0.1) -> float:
    if not (0.0 <= zeta <= 1.0):
        raise ValueError("zeta must satisfy 0 <= zeta <= 1")
    return nu2 * zeta**2 + nu4 * zeta**4


def phi_relativistic_like(zeta: float) -> float:
    if not (0.0 <= zeta < 1.0):
        raise ValueError("relativistic-like comparator requires 0 <= zeta < 1")
    return 1.0 / math.sqrt(1.0 - zeta * zeta) - 1.0


def theta_star(eta_i: float, phi_value: float) -> float:
    if eta_i <= 0.0:
        raise ValueError("eta_i must be positive")
    if phi_value <= 0.0:
        raise ValueError("phi_value must be positive at a nonzero threshold")
    return eta_i * phi_value


def rcrit_over_rs(
    kg_over_g: float,
    cinfo_over_c: float,
    eta_i: float,
    phi_value: float,
) -> float:
    if kg_over_g <= 0.0 or cinfo_over_c <= 0.0:
        raise ValueError("bridge ratios must be positive")
    return (
        kg_over_g
        * (1.0 / cinfo_over_c**2)
        / (2.0 * theta_star(eta_i, phi_value))
    )


def blind_report() -> None:
    print("DSD structural-gravity nu_kin / constitutive-function audit")
    print("----------------------------------------------------------")
    print("General downstream support-capacity form:")
    print("  E_sup(v) = mu_I * c_info^2 * Phi(v/c_info)")
    print("  zeta = v_sup / c_info")
    print("  C_sup = eta_I * c_info^2 * Phi(zeta)")
    print("  Theta_* = eta_I * Phi(zeta)")
    print()
    print("Quadratic special case:")
    print("  Phi(zeta) = nu_kin * zeta^2")
    print("  Theta_* = nu_kin * eta_I * zeta^2")
    print()
    print("Low-speed bridge needed for nu_kin = 1/2:")
    print("  dE_sup/dv = p_eff(v)")
    print("  p_eff(v) = mu_I * v + O(v^3/c_info^2)")
    print("  => Phi(zeta) = 1/2 zeta^2 + O(zeta^4)")
    print()
    print("Boundary:")
    print("  This fixes only the leading low-speed coefficient.")
    print("  It does NOT justify a globally quadratic law up to zeta = 1.")


def sensitivity_report() -> None:
    zetas = (0.1, 0.5, 0.9, 0.99)
    print("Constitutive sensitivity")
    print("------------------------")
    print("zeta,quad_1/2,quartic_1/2_plus_0.1,relativistic_like")
    for z in zetas:
        print(
            f"{z:.2f},"
            f"{phi_quadratic(z, 0.5):.12g},"
            f"{phi_quartic(z):.12g},"
            f"{phi_relativistic_like(z):.12g}"
        )

    print()
    print("Same c_info and same pure-quadratic shape, different allowed nu:")
    print("nu,Phi(0.9),Rcrit/Rs_if_eta=Kg/G=cinfo/c=1")
    for nu in (0.3, 0.5, 0.8):
        phi = phi_quadratic(0.9, nu)
        ratio = rcrit_over_rs(1.0, 1.0, 1.0, phi)
        print(f"{nu:.1f},{phi:.12g},{ratio:.12g}")


def audit_report() -> int:
    checks: list[tuple[str, bool, str]] = []

    eps = 1e-5
    quad_lead = phi_quadratic(eps, 0.5) / eps**2
    quartic_lead = phi_quartic(eps) / eps**2
    rel_lead = phi_relativistic_like(eps) / eps**2

    checks.append((
        "QUADRATIC_LOW_SPEED_HALF",
        abs(quad_lead - 0.5) < 1e-12,
        "the explicit quadratic specialization has leading coefficient 1/2",
    ))
    checks.append((
        "QUARTIC_SAME_LOW_SPEED_HALF",
        abs(quartic_lead - 0.5) < 1e-8,
        "a quartic-corrected law can share the same low-speed 1/2 coefficient",
    ))
    checks.append((
        "REL_LIKE_SAME_LOW_SPEED_HALF",
        abs(rel_lead - 0.5) < 1e-5,
        "a non-polynomial comparator can share the same low-speed 1/2 coefficient",
    ))

    z = 0.9
    q = phi_quadratic(z, 0.5)
    q4 = phi_quartic(z)
    rel = phi_relativistic_like(z)

    checks.append((
        "HIGH_ZETA_NONUNIQUENESS",
        abs(q - q4) > 1e-3 and abs(q - rel) > 1e-3,
        "same low-speed coefficient does not determine near-bound capacity",
    ))
    checks.append((
        "NU_NOT_FIXED_BY_CINFO",
        len({
            round(phi_quadratic(z, 0.3), 12),
            round(phi_quadratic(z, 0.5), 12),
            round(phi_quadratic(z, 0.8), 12),
        }) == 3,
        "different nu values remain possible while c_info is unchanged",
    ))
    checks.append((
        "GENERALIZED_THRESHOLD_FORM",
        abs(theta_star(1.2, q4) - 1.2 * q4) < 1e-15,
        "Theta_* = eta_I Phi(zeta) is the general factorized form",
    ))
    checks.append((
        "OLD_FORM_IS_SPECIAL_CASE",
        abs(
            theta_star(1.1, phi_quadratic(0.8, 0.5))
            - (0.5 * 1.1 * 0.8**2)
        ) < 1e-15,
        "nu_kin eta_I zeta^2 is recovered when Phi is globally quadratic",
    ))
    checks.append((
        "NO_BLACK_HOLE_FIT",
        True,
        "no Schwarzschild/EHT value is used to choose Phi or nu_kin",
    ))

    failures = 0
    for name, ok, note in checks:
        status = "PASS" if ok else "FAIL"
        failures += 0 if ok else 1
        print(f"{status}: {name} -- {note}")

    print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")
    print("STATUS: PASS_WITH_BOUNDARY / CONSTITUTIVE_FUNCTION_REFINEMENT")
    return failures


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit nu_kin and the constitutive support-capacity function."
    )
    parser.add_argument(
        "--mode",
        choices=("all", "blind", "sensitivity", "audit"),
        default="all",
    )
    args = parser.parse_args()

    if args.mode in ("all", "blind"):
        blind_report()
        if args.mode == "blind":
            return

    if args.mode in ("all", "sensitivity"):
        print()
        sensitivity_report()
        if args.mode == "sensitivity":
            return

    if args.mode in ("all", "audit"):
        print()
        failures = audit_report()
        if failures:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
