#!/usr/bin/env python3
"""
BH-RB-016 — Repeated reorganization / radius-floor persistence gate.

Purpose:
- Continue BH-RB-014/015 without assuming a permanent finite core radius.
- Ask whether repeated rotational-instability episodes plus angular-momentum
  transport can by themselves generate a strictly positive asymptotic 3D
  radius floor.
- Use the conditional rotational-volume floor
      R_floor = [J_core/(kappa M_core c)] q^(1/3)
  inherited from the BH-RB-014 finite-rotator control plus a positive
  aspect-ratio control q.
- Track repeated cycles
      J_{n+1}=s_J J_n, M_{n+1}=s_M M_n
  and determine when the floor shrinks, stays fixed, or grows.
- Add an optional Newtonian bar-mode trigger scale
      beta=T/|W|,
      I=kappa M a^2,
      |W|=alpha G M^2/a,
  solely as a scaling control for how an instability radius moves across cycles.

Important boundaries:
- This is not a relativistic black-hole interior solution.
- The finite-body moment of inertia and Newtonian binding-energy formulas are
  controls only; frame dragging, strong-field geometry, fluxes, and a
  constitutive stress law are not solved here.
- Maclaurin/bar-mode thresholds are external standard-fluid comparators, not
  DSD-derived constants and not universal black-hole-core thresholds.
- The audit explicitly permits the answer "no positive radius floor follows".
"""

from __future__ import annotations

import argparse
import math

G = 6.67430e-11
C = 299_792_458.0
M_SUN = 1.98847e30
M_SGRA = 4.297e6 * M_SUN

KAPPA_UNIFORM_SPHEROID = 2.0 / 5.0
ALPHA_UNIFORM_SPHERE = 3.0 / 5.0
BETA_DYN_MACLAURIN = 0.2738
E_DYN_MACLAURIN = 0.9529
Q_DYN_MACLAURIN = math.sqrt(1.0 - E_DYN_MACLAURIN**2)


def r_g(mass: float) -> float:
    return G * mass / C**2


def j_from_chi(mass: float, chi: float) -> float:
    """Total angular momentum corresponding to a Kerr-scale dimensionless spin."""
    return chi * G * mass**2 / C


def rotational_volume_floor(
    angular_momentum: float,
    mass: float,
    kappa: float = KAPPA_UNIFORM_SPHEROID,
    q: float = 1.0,
) -> float:
    """
    Conditional finite-body control:
      a_causal = J/(kappa M c),
      R_V = a q^(1/3),
    hence
      R_floor = J/(kappa M c) q^(1/3).

    This is a conditional control, not a black-hole-core radius law.
    """
    if angular_momentum < 0.0:
        raise ValueError("Use the magnitude of angular momentum; J must be >= 0.")
    if mass <= 0.0:
        raise ValueError("mass must be positive.")
    if kappa <= 0.0:
        raise ValueError("kappa must be positive.")
    if q < 0.0:
        raise ValueError("q must be nonnegative.")
    return angular_momentum * q ** (1.0 / 3.0) / (kappa * mass * C)


def cycle_state(
    j0: float,
    m0: float,
    s_j: float,
    s_m: float,
    n: int,
) -> tuple[float, float]:
    """Geometric retention toy: J_n=s_J^n J0, M_n=s_M^n M0."""
    if not (0.0 <= s_j <= 1.0):
        raise ValueError("s_j must lie in [0,1].")
    if not (0.0 < s_m <= 1.0):
        raise ValueError("s_m must lie in (0,1].")
    if n < 0:
        raise ValueError("n must be nonnegative.")
    return j0 * s_j**n, m0 * s_m**n


def floor_cycle(
    j0: float,
    m0: float,
    s_j: float,
    s_m: float,
    n: int,
    kappa: float = KAPPA_UNIFORM_SPHEROID,
    q: float = Q_DYN_MACLAURIN,
) -> float:
    jn, mn = cycle_state(j0, m0, s_j, s_m, n)
    return rotational_volume_floor(jn, mn, kappa, q)


def constant_shape_floor_ratio(s_j: float, s_m: float) -> float:
    """For fixed kappa and q, R_floor,n+1/R_floor,n = s_J/s_M."""
    if not (0.0 <= s_j <= 1.0) or not (0.0 < s_m <= 1.0):
        raise ValueError
    return s_j / s_m


def general_floor_ratio(
    s_j: float,
    s_m: float,
    kappa_n: float,
    kappa_np1: float,
    q_n: float,
    q_np1: float,
) -> float:
    """
    Exact one-cycle ratio for the conditional control:
      R_{n+1}/R_n
      = (s_J/s_M)(kappa_n/kappa_{n+1})(q_{n+1}/q_n)^(1/3).
    """
    if s_m <= 0.0 or kappa_n <= 0.0 or kappa_np1 <= 0.0:
        raise ValueError
    if q_n <= 0.0 or q_np1 < 0.0:
        raise ValueError
    return (
        (s_j / s_m)
        * (kappa_n / kappa_np1)
        * (q_np1 / q_n) ** (1.0 / 3.0)
    )


def newtonian_bar_trigger_radius(
    angular_momentum: float,
    mass: float,
    beta_crit: float = BETA_DYN_MACLAURIN,
    kappa: float = KAPPA_UNIFORM_SPHEROID,
    alpha: float = ALPHA_UNIFORM_SPHERE,
) -> float:
    """
    Scaling control from
      beta=T/|W|,
      T=J^2/(2 I), I=kappa M a^2,
      |W|=alpha G M^2/a.

    Solving beta=beta_crit:
      a_bar = J^2/(2 kappa alpha beta_crit G M^3).

    The use of alpha=3/5 is a uniform-sphere calibration only.
    """
    if angular_momentum < 0.0 or mass <= 0.0:
        raise ValueError
    if beta_crit <= 0.0 or kappa <= 0.0 or alpha <= 0.0:
        raise ValueError
    return angular_momentum**2 / (
        2.0 * kappa * alpha * beta_crit * G * mass**3
    )


def bar_trigger_cycle_ratio(s_j: float, s_m: float) -> float:
    """For fixed kappa, alpha, beta_crit: a_bar,n+1/a_bar,n=s_J^2/s_M^3."""
    if not (0.0 <= s_j <= 1.0) or not (0.0 < s_m <= 1.0):
        raise ValueError
    return s_j**2 / s_m**3


def checks() -> list[tuple[str, bool]]:
    out: list[tuple[str, bool]] = []

    m0 = M_SGRA
    chi0 = 0.9
    j0 = j_from_chi(m0, chi0)
    rg0 = r_g(m0)
    kappa = KAPPA_UNIFORM_SPHEROID
    q = Q_DYN_MACLAURIN

    floor0 = rotational_volume_floor(j0, m0, kappa, q)

    out.append((
        "BH-RB-014 conditional floor identity recovered",
        abs(floor0 / rg0 - (chi0 / kappa) * q ** (1.0 / 3.0)) < 1e-12,
    ))

    s_j = 0.80
    s_m = 0.99
    ratio = s_j / s_m

    out.append((
        "constant-shape repeated floor ratio equals sJ/sM",
        abs(
            floor_cycle(j0, m0, s_j, s_m, 1, kappa, q) / floor0
            - ratio
        ) < 1e-12,
    ))

    out.append((
        "J loss faster than mass loss drives the rotational floor inward",
        ratio < 1.0
        and floor_cycle(j0, m0, s_j, s_m, 10, kappa, q) < floor0,
    ))

    out.append((
        "equal fractional J and M retention keeps the conditional floor fixed",
        abs(
            floor_cycle(j0, m0, 0.95, 0.95, 20, kappa, q) / floor0 - 1.0
        ) < 1e-12,
    ))

    out.append((
        "slower fractional J loss than mass loss makes the conditional floor grow",
        floor_cycle(j0, m0, 0.98, 0.95, 5, kappa, q) > floor0,
    ))

    out.append((
        "positive q alone does not prevent floor -> 0 when J/M -> 0",
        floor_cycle(j0, m0, 0.80, 0.99, 100, kappa, q)
        < 1e-8 * floor0,
    ))

    out.append((
        "finite number of cycles retains a positive floor while J and M remain positive",
        all(
            floor_cycle(j0, m0, 0.80, 0.99, n, kappa, q) > 0.0
            for n in range(25)
        ),
    ))

    out.append((
        "zero retained core angular momentum removes this rotational floor",
        rotational_volume_floor(0.0, m0, kappa, q) == 0.0,
    ))

    out.append((
        "general ratio reproduces constant-shape result",
        abs(
            general_floor_ratio(0.8, 0.99, 0.4, 0.4, q, q)
            - 0.8 / 0.99
        ) < 1e-12,
    ))

    out.append((
        "increasing q or decreasing kappa can offset some J/M floor loss",
        general_floor_ratio(
            0.80, 0.99, 0.40, 0.36, 0.25, 0.50
        ) > 0.80 / 0.99,
    ))

    abar0 = newtonian_bar_trigger_radius(j0, m0)
    out.append((
        "Newtonian bar-trigger scaling is proportional to J^2/M^3",
        abs(
            newtonian_bar_trigger_radius(
                j0 * 0.8, m0 * 0.99
            ) / abar0
            - bar_trigger_cycle_ratio(0.8, 0.99)
        ) < 1e-12,
    ))

    out.append((
        "representative J-shedding cycle moves the toy bar trigger inward",
        bar_trigger_cycle_ratio(0.8, 0.99) < 1.0,
    ))

    out.append((
        "Maclaurin dynamical shape control remains strictly 3D at onset",
        Q_DYN_MACLAURIN > 0.0,
    ))

    out.append((
        "repeated reorganization alone does not mathematically enforce positive asymptotic radius",
        ratio < 1.0
        and floor_cycle(j0, m0, s_j, s_m, 200, kappa, q)
        < 1e-16 * floor0,
    ))

    return out


def report() -> None:
    m0 = M_SGRA
    chi0 = 0.9
    j0 = j_from_chi(m0, chi0)
    rg0 = r_g(m0)
    kappa = KAPPA_UNIFORM_SPHEROID
    q = Q_DYN_MACLAURIN

    print("BH-RB-016 repeated reorganization / radius-floor persistence gate")
    print("Toy recurrence and finite-rotator controls only; not a GR interior solution.")
    print(f"M0 = 4.297e6 Msun, chi0 = {chi0:.3f}, r_g0 = {rg0/1000:.6f} km")
    print(f"kappa = {kappa:.6f}, q_control = {q:.9f}")
    print()

    floor0 = rotational_volume_floor(j0, m0, kappa, q)
    print("Conditional BH-RB-014 + shape-control floor:")
    print(f"R_floor,0/r_g0 = {floor0/rg0:.9f}")
    print()

    s_j = 0.80
    s_m = 0.99
    print("Example repeated reorganization control: s_J=0.80, s_M=0.99")
    print("n     J_n/J_0       M_n/M_0       R_floor,n/r_g0")
    for n in (0, 1, 5, 10, 20, 50):
        jn, mn = cycle_state(j0, m0, s_j, s_m, n)
        rf = rotational_volume_floor(jn, mn, kappa, q)
        print(f"{n:2d}    {jn/j0:11.6e}  {mn/m0:11.6e}  {rf/rg0:14.9e}")
    print()

    print("Exact constant-shape recurrence:")
    print("R_floor,n+1/R_floor,n = s_J/s_M")
    print(f"example ratio = {s_j/s_m:.9f} < 1")
    print("Thus repeated J loss faster than mass loss sends this rotational floor toward zero.")
    print()

    abar0 = newtonian_bar_trigger_radius(j0, m0)
    print("Optional Newtonian bar-trigger scaling control:")
    print(f"a_bar,0/r_g0 = {abar0/rg0:.9f}")
    print("a_bar,n+1/a_bar,n = s_J^2/s_M^3")
    print(
        f"example bar-trigger ratio = {bar_trigger_cycle_ratio(s_j, s_m):.9f}"
    )
    print()

    print("General persistence condition inside this control:")
    print(
        "inf_n R_floor,n > 0 requires inf_n "
        "[J_n q_n^(1/3)/(kappa_n M_n)] > 0."
    )
    print(
        "Rotational instability and reorganization do not by themselves guarantee that condition."
    )

    results = checks()
    passed = sum(ok for _, ok in results)
    print()
    for name, ok in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"\n{passed}/{len(results)} checks PASS")
    if passed != len(results):
        raise SystemExit(1)

    print(
        "\nVERDICT: PASS_WITH_BOUNDARY / REPEATED_REORGANIZATION_CHANNEL_IDENTIFIED / "
        "ROTATIONAL_FLOOR_NOT_SELF_PERSISTING_UNDER_GENERIC_J_LOSS / "
        "POSITIVE_ASYMPTOTIC_RADIUS_REQUIRES_ADDITIONAL_CLOSURE"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["all", "report"], default="all")
    _ = parser.parse_args()
    report()


if __name__ == "__main__":
    main()
