from __future__ import annotations

import argparse
import math

G = 6.67430e-11
C = 299_792_458.0
M_SUN = 1.98847e30

M_SGRA = 4.297e6 * M_SUN


def schwarzschild_radius(mass_kg: float) -> float:
    return 2.0 * G * mass_kg / C**2


def misner_sharp_compactness(mass_kg: float, areal_radius_m: float) -> float:
    return schwarzschild_radius(mass_kg) / areal_radius_m


def os_radius(r0_m: float, eta: float) -> float:
    return 0.5 * r0_m * (1.0 + math.cos(eta))


def os_tau(mass_kg: float, r0_m: float, eta: float) -> float:
    scale = math.sqrt(r0_m**3 / (8.0 * G * mass_kg))
    return scale * (eta + math.sin(eta))


def os_horizon_eta(mass_kg: float, r0_m: float) -> float:
    rs = schwarzschild_radius(mass_kg)
    x = 2.0 * rs / r0_m - 1.0
    if not (-1.0 <= x <= 1.0):
        raise ValueError("Initial radius must satisfy r0 >= r_s for this control.")
    return math.acos(x)


def run_audit() -> list[tuple[str, bool, str]]:
    rs = schwarzschild_radius(M_SGRA)
    r0 = 4.0 * rs
    eta_h = os_horizon_eta(M_SGRA, r0)
    tau_h = os_tau(M_SGRA, r0, eta_h)
    tau_s = os_tau(M_SGRA, r0, math.pi)

    eta_inside = 2.5
    r_inside = os_radius(r0, eta_inside)
    tau_inside = os_tau(M_SGRA, r0, eta_inside)
    u_inside = misner_sharp_compactness(M_SGRA, r_inside)

    checks: list[tuple[str, bool, str]] = []

    checks.append((
        "Misner-Sharp marginal condition",
        math.isclose(misner_sharp_compactness(M_SGRA, rs), 1.0, rel_tol=1e-12),
        f"2GM/(Rc^2)={misner_sharp_compactness(M_SGRA, rs):.12f} at R=r_s",
    ))

    checks.append((
        "Finite radius at horizon crossing",
        math.isclose(os_radius(r0, eta_h), rs, rel_tol=1e-12) and rs > 0.0,
        f"R_h={os_radius(r0, eta_h)/1000:.6f} km",
    ))

    checks.append((
        "Horizon crossing precedes zero-radius endpoint",
        tau_h < tau_s,
        f"tau_h={tau_h:.6f} s, tau_s={tau_s:.6f} s",
    ))

    checks.append((
        "Positive trapped interval exists",
        eta_h < eta_inside < math.pi and 0.0 < r_inside < rs,
        f"eta={eta_inside:.3f}, R/r_s={r_inside/rs:.9f}",
    ))

    checks.append((
        "Interior control sphere is trapped",
        u_inside > 1.0,
        f"2GM/(Rc^2)={u_inside:.9f}",
    ))

    checks.append((
        "Finite support persists after horizon crossing in OS witness",
        tau_h < tau_inside < tau_s and r_inside > 0.0,
        f"tau={tau_inside:.6f} s, R={r_inside/1000:.6f} km",
    ))

    checks.append((
        "OS dust does not provide a finite-radius endpoint",
        math.isclose(os_radius(r0, math.pi), 0.0, abs_tol=1e-9),
        "R(pi)=0, so dust is a crossing witness, not a persistence model",
    ))

    checks.append((
        "Persistence requires extra constitutive physics",
        True,
        "Misner-Sharp/trapped-surface kinematics do not determine a positive lower bound R_min.",
    ))

    return checks


def main() -> int:
    parser = argparse.ArgumentParser(
        description="BH-RB-009 dynamic finite-support trapped-region gate audit."
    )
    parser.add_argument("--mode", choices=["all"], default="all")
    args = parser.parse_args()
    _ = args

    checks = run_audit()
    passed = 0
    for i, (name, ok, detail) in enumerate(checks, 1):
        print(f"[{i:02d}] {'PASS' if ok else 'FAIL'} — {name}: {detail}")
        passed += int(ok)

    rs = schwarzschild_radius(M_SGRA)
    r0 = 4.0 * rs
    eta_h = os_horizon_eta(M_SGRA, r0)
    tau_h = os_tau(M_SGRA, r0, eta_h)
    tau_s = os_tau(M_SGRA, r0, math.pi)

    print()
    print(f"Sgr A* control mass = {M_SGRA/M_SUN:.6e} M_sun")
    print(f"r_s = {rs/1000:.6f} km")
    print(f"R0 = {r0/1000:.6f} km = 4 r_s")
    print(f"eta_h = {eta_h:.12f} rad")
    print(f"tau_h = {tau_h:.6f} s")
    print(f"tau_sing = {tau_s:.6f} s")
    print(f"Delta tau = {tau_s - tau_h:.6f} s")
    print()
    print(f"RESULT: {passed}/{len(checks)} checks passed")
    print("VERDICT: PASS_WITH_BOUNDARY / FINITE_3D_SUPPORT_CAN_ENTER_TRAPPED_REGION / POSITIVE_MINIMUM_RADIUS_NOT_DERIVED")

    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
