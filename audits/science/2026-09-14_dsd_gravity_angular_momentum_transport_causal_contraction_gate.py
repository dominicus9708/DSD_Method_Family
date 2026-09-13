#!/usr/bin/env python3
"""
BH-RB-014 — Angular-momentum transport / causal contraction gate.

Purpose:
- Continue the J != 0 successor-core branch after BH-RB-012/013.
- Ask whether conserved nonzero core angular momentum can remain compatible with
  indefinite equatorial contraction in a minimal finite-rotator control.
- Derive a conditional causal equatorial lower scale from
      J_core = I Omega, I = kappa M_core a^2, v_eq = Omega a < c.
- Separate an equatorial angular-momentum bound from a genuine 3D finite-volume
  core bound.
- Derive the angular-momentum transport rate required to keep the local
  rotational control beta = v_eq/c from growing during contraction.

Important boundaries:
- I = kappa M a^2 is a Newtonian / weak-field finite-body control.
- General relativity has no unique Newtonian-style moment of inertia; for
  uniformly rotating relativistic stars I = J/Omega is commonly used instead.
- Inside a strong-field rotating black-hole region, frame dragging and the full
  metric determine physical azimuthal velocity. This script does NOT replace
  those relations with v = Omega a as an exact interior law.
- Kerr r_+ is used only as an external scale comparator.
- No finite black-hole core radius is derived here.
"""

from __future__ import annotations

import argparse
import math

G = 6.67430e-11
C = 299_792_458.0
M_SUN = 1.98847e30
M_SGRA = 4.297e6 * M_SUN
KAPPA_UNIFORM_SPHEROID = 2.0 / 5.0


def r_g(mass: float) -> float:
    return G * mass / C**2


def r_plus(mass: float, chi: float) -> float:
    return r_g(mass) * (1.0 + math.sqrt(max(0.0, 1.0 - chi**2)))


def causal_equatorial_scale(
    mass_total: float,
    chi: float,
    f_j: float = 1.0,
    f_m: float = 1.0,
    kappa: float = KAPPA_UNIFORM_SPHEROID,
) -> float:
    """
    Minimal-rotator control:
      J_core = f_j J_total,
      M_core = f_m M_total,
      I = kappa M_core a^2,
      v_eq/c = J_core/(kappa M_core c a).

    beta < 1 implies
      a > (f_j/f_m) chi r_g / kappa.
    """
    if not (0.0 < f_m <= 1.0):
        raise ValueError("f_m must lie in (0,1].")
    if not (0.0 <= f_j <= 1.0):
        raise ValueError("f_j must lie in [0,1].")
    if kappa <= 0.0:
        raise ValueError("kappa must be positive.")
    return (f_j / f_m) * chi * r_g(mass_total) / kappa


def beta_rot(
    a: float,
    mass_total: float,
    chi: float,
    f_j: float = 1.0,
    f_m: float = 1.0,
    kappa: float = KAPPA_UNIFORM_SPHEROID,
) -> float:
    """Toy physical-speed control beta = v_eq/c."""
    if a <= 0.0:
        raise ValueError("a must be positive.")
    return causal_equatorial_scale(mass_total, chi, f_j, f_m, kappa) / a


def eta_max_inside_kerr_horizon(chi: float, kappa: float = KAPPA_UNIFORM_SPHEROID) -> float:
    """
    eta := f_j/f_m.
    Requiring the toy causal equatorial scale not to exceed r_+ gives
      eta <= kappa (1 + sqrt(1-chi^2))/chi.
    """
    if chi == 0.0:
        return math.inf
    return kappa * (1.0 + math.sqrt(max(0.0, 1.0 - chi**2))) / chi


def chi_critical_all_mass_all_j(kappa: float = KAPPA_UNIFORM_SPHEROID) -> float:
    """
    For eta=1, solve a_causal = r_+:
      chi/kappa = 1 + sqrt(1-chi^2)
      chi_crit = 2 kappa/(1+kappa^2).
    """
    return 2.0 * kappa / (1.0 + kappa * kappa)


def volume_equivalent_radius(a: float, q: float) -> float:
    """
    Oblate control with c = q a:
      V = 4 pi a^2 c / 3,
      R_V = (a^2 c)^(1/3) = a q^(1/3).
    """
    if a < 0.0 or q < 0.0:
        raise ValueError("a and q must be nonnegative.")
    return a * q ** (1.0 / 3.0)


def beta_log_rate(
    j_log_rate: float,
    kappa_log_rate: float,
    m_log_rate: float,
    a_log_rate: float,
) -> float:
    """
    From beta = J/(kappa M c a):
      d ln beta = d ln J - d ln kappa - d ln M - d ln a.
    Rates may be taken with respect to proper time or any common evolution
    parameter used consistently inside the toy control.
    """
    return j_log_rate - kappa_log_rate - m_log_rate - a_log_rate


def checks() -> list[tuple[str, bool]]:
    out: list[tuple[str, bool]] = []
    kappa = KAPPA_UNIFORM_SPHEROID
    chi = 0.9
    rg = r_g(M_SGRA)

    a_min = causal_equatorial_scale(M_SGRA, chi)
    out.append((
        "causal equatorial identity a_min/r_g = chi/kappa",
        abs(a_min / rg - chi / kappa) < 1e-12,
    ))

    out.append((
        "beta reaches unity exactly at the toy causal scale",
        abs(beta_rot(a_min, M_SGRA, chi) - 1.0) < 1e-12,
    ))

    out.append((
        "fixed-J contraction increases beta inversely with a",
        abs(beta_rot(a_min * 2.0, M_SGRA, chi) - 0.5) < 1e-12
        and abs(beta_rot(a_min * 0.5, M_SGRA, chi) - 2.0) < 1e-12,
    ))

    out.append((
        "J proportional to a keeps beta constant for fixed M and kappa",
        abs(beta_log_rate(-0.1, 0.0, 0.0, -0.1)) < 1e-15,
    ))

    out.append((
        "insufficient J loss during contraction makes beta grow",
        beta_log_rate(-0.05, 0.0, 0.0, -0.10) > 0.0,
    ))

    out.append((
        "sufficient fractional J loss can prevent beta growth",
        beta_log_rate(-0.12, 0.0, 0.0, -0.10) < 0.0,
    ))

    eta_max = eta_max_inside_kerr_horizon(chi, kappa)
    out.append((
        "chi=0.9 uniform-spheroid toy fit ratio eta_max matches control",
        abs(eta_max - 0.6381732863795855) < 1e-12,
    ))

    out.append((
        "all-mass/all-J chi=0.9 toy causal scale exceeds Kerr r_plus",
        causal_equatorial_scale(M_SGRA, chi) > r_plus(M_SGRA, chi),
    ))

    out.append((
        "half-J/all-mass chi=0.9 toy causal scale fits below Kerr r_plus",
        causal_equatorial_scale(M_SGRA, chi, f_j=0.5, f_m=1.0)
        < r_plus(M_SGRA, chi),
    ))

    crit = chi_critical_all_mass_all_j(kappa)
    out.append((
        "critical-spin closed form satisfies a_causal = r_plus",
        abs(
            causal_equatorial_scale(M_SGRA, crit)
            - r_plus(M_SGRA, crit)
        ) / rg < 1e-12,
    ))

    out.append((
        "uniform-spheroid critical spin equals 20/29",
        abs(crit - 20.0 / 29.0) < 1e-12,
    ))

    a = 2.0 * rg
    out.append((
        "finite equatorial radius does not prevent volume radius from tending to zero",
        volume_equivalent_radius(a, 1e-12) < 1e-3 * a,
    ))

    q_min = 0.125
    rv_bound = volume_equivalent_radius(a_min, q_min)
    out.append((
        "positive aspect-ratio floor converts equatorial floor into positive 3D radius floor",
        rv_bound > 0.0
        and abs(rv_bound / a_min - q_min ** (1.0 / 3.0)) < 1e-12,
    ))

    return out


def report() -> None:
    kappa = KAPPA_UNIFORM_SPHEROID
    rg = r_g(M_SGRA)
    print("BH-RB-014 angular-momentum transport / causal contraction gate")
    print("Minimal finite-rotator control only; not a relativistic black-hole interior solution.")
    print(f"M = 4.297e6 Msun, r_g = {rg/1000:.6f} km, kappa = {kappa:.6f}")
    print()
    print("chi    r_+/r_g   eta_max=fJ/fM   a_causal(all M,J)/r_g")
    for chi in (0.3, 0.5, 0.7, 0.9, 0.99, 1.0):
        print(
            f"{chi:4.2f}   {r_plus(M_SGRA, chi)/rg:9.6f}   "
            f"{eta_max_inside_kerr_horizon(chi, kappa):14.9f}   "
            f"{causal_equatorial_scale(M_SGRA, chi)/rg:14.9f}"
        )

    chi = 0.9
    a_all = causal_equatorial_scale(M_SGRA, chi)
    a_halfj = causal_equatorial_scale(M_SGRA, chi, f_j=0.5)
    rp = r_plus(M_SGRA, chi)
    print()
    print("Sgr A* scale control at chi=0.9:")
    print(f"r_+ = {rp/1000:.6f} km")
    print(f"a_causal(fJ=fM=1) = {a_all/1000:.6f} km = {a_all/rg:.9f} r_g")
    print(f"a_causal(fJ=0.5,fM=1) = {a_halfj/1000:.6f} km = {a_halfj/rg:.9f} r_g")
    print(f"eta_max inside r_+ = {eta_max_inside_kerr_horizon(chi, kappa):.9f}")
    print(f"chi_crit(eta=1,kappa=2/5) = {chi_critical_all_mass_all_j(kappa):.9f}")
    print()
    print("Dynamic transport identity:")
    print("d ln beta = d ln J_core - d ln kappa - d ln M_core - d ln a")
    print("For fixed kappa and M_core, constant beta during contraction requires J_core proportional to a.")
    print()
    print("3D firewall:")
    print("R_V = a q^(1/3), q=c/a.")
    print("A finite a floor alone does not prevent q -> 0 and R_V -> 0.")
    print("If a separate polar closure yields q >= q_min > 0, then")
    print("R_V,min >= a_causal q_min^(1/3) in this control.")

    results = checks()
    passed = sum(ok for _, ok in results)
    print()
    for name, ok in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"\n{passed}/{len(results)} checks PASS")
    if passed != len(results):
        raise SystemExit(1)

    print(
        "\nVERDICT: PASS_WITH_BOUNDARY / ANGULAR_MOMENTUM_CAUSAL_SCALE_IDENTIFIED / "
        "CONTRACTION_REQUIRES_J_TRANSPORT_OR_STRONG_FIELD_REORGANIZATION / "
        "POLAR_CLOSURE_STILL_REQUIRED / FINITE_3D_CORE_RADIUS_NOT_DERIVED"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["all", "report"], default="all")
    _ = parser.parse_args()
    report()


if __name__ == "__main__":
    main()
