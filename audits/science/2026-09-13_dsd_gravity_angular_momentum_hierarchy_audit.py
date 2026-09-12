#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

G = 6.67430e-11
C = 299_792_458.0
M_SUN = 1.98847e30

Vec3 = tuple[float, float, float]


@dataclass(frozen=True)
class Particle:
    position: Vec3
    momentum: Vec3
    energy: float


def add(a: Vec3, b: Vec3) -> Vec3:
    return tuple(x + y for x, y in zip(a, b))


def sub(a: Vec3, b: Vec3) -> Vec3:
    return tuple(x - y for x, y in zip(a, b))


def cross(a: Vec3, b: Vec3) -> Vec3:
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def total_momentum(parts: list[Particle]) -> Vec3:
    out = (0.0, 0.0, 0.0)
    for p in parts:
        out = add(out, p.momentum)
    return out


def orbital_angular_momentum(parts: list[Particle], origin: Vec3 = (0.0, 0.0, 0.0)) -> Vec3:
    out = (0.0, 0.0, 0.0)
    for p in parts:
        out = add(out, cross(sub(p.position, origin), p.momentum))
    return out


def total_energy(parts: list[Particle]) -> float:
    return sum(p.energy for p in parts)


def gravitational_radius_km(mass_msun: float) -> float:
    return G * mass_msun * M_SUN / C**2 / 1000.0


def horizon_envelope_fixed_mass_spin_km(mass_msun: float, chi: float) -> tuple[float, float]:
    if abs(chi) > 1.0 + 1e-14:
        raise ValueError("|chi| > 1 leaves no Kerr-Newman horizon for any real charge")
    chi = max(-1.0, min(1.0, chi))
    rg = gravitational_radius_km(mass_msun)
    # With Q still unknown, qhat^2 may range from 0 to 1-chi^2.
    lower = rg
    upper = rg * (1.0 + math.sqrt(max(0.0, 1.0 - chi**2)))
    return lower, upper


def audit(mass_msun: float, chi: float) -> list[tuple[str, bool, str]]:
    checks: list[tuple[str, bool, str]] = []

    # Same energy and total momentum, different localization -> different angular momentum.
    upper = [Particle((0.0, 1.0, 0.0), (1.0, 0.0, 0.0), 1.0)]
    lower = [Particle((0.0, -1.0, 0.0), (1.0, 0.0, 0.0), 1.0)]
    checks.append((
        "ENERGY_AND_TOTAL_P_DO_NOT_FIX_J_WITHOUT_LOCALIZATION",
        total_energy(upper) == total_energy(lower)
        and total_momentum(upper) == total_momentum(lower)
        and orbital_angular_momentum(upper) != orbital_angular_momentum(lower),
        "equal scalar energy and equal total linear momentum can coexist with different orbital angular momentum",
    ))

    # Origin shift law J' = J - a x P.
    state = [Particle((0.0, 1.0, 0.0), (1.0, 0.0, 0.0), 1.0)]
    a = (0.0, 2.0, 0.0)
    j0 = orbital_angular_momentum(state)
    ja = orbital_angular_momentum(state, origin=a)
    predicted = sub(j0, cross(a, total_momentum(state)))
    checks.append((
        "ORIGIN_SHIFT_LAW",
        all(math.isclose(x, y, abs_tol=1e-14) for x, y in zip(ja, predicted)),
        "orbital J changes under origin translation when total linear momentum is nonzero",
    ))

    # Center-of-momentum control: P=0 makes constant-origin translation harmless.
    com_state = [
        Particle((0.0, 1.0, 0.0), (1.0, 0.0, 0.0), 1.0),
        Particle((0.0, -1.0, 0.0), (-1.0, 0.0, 0.0), 1.0),
    ]
    checks.append((
        "P_ZERO_TRANSLATION_CONTROL",
        total_momentum(com_state) == (0.0, 0.0, 0.0)
        and orbital_angular_momentum(com_state) == orbital_angular_momentum(com_state, origin=a),
        "with total P=0, a constant change of spatial origin leaves this orbital-J witness unchanged",
    ))

    rg = gravitational_radius_km(mass_msun)
    rlo, rhi = horizon_envelope_fixed_mass_spin_km(mass_msun, chi)
    checks.append((
        "FIXED_M_AND_CHI_UNKNOWN_Q_ENVELOPE",
        math.isclose(rlo, rg, rel_tol=1e-14)
        and rhi >= rlo
        and rhi <= 2.0 * rg + 1e-9,
        "after M and chi are externally supplied but Q is not, the Kerr-Newman comparator obeys r_g <= r_+ <= r_g(1+sqrt(1-chi^2))",
    ))

    checks.append((
        "LOCAL_MATTER_J_NOT_IDENTIFIED_WITH_GLOBAL_SPACETIME_J",
        True,
        "a separate external asymptotic/boundary construction is required; vacuum exterior does not force global black-hole J to vanish",
    ))

    return checks


def main() -> None:
    parser = argparse.ArgumentParser(
        description="BH-RB-004 audit: DSD-to-physical angular-momentum hierarchy gate."
    )
    parser.add_argument("--mass-msun", type=float, default=4.297e6)
    parser.add_argument("--chi", type=float, default=0.9)
    args = parser.parse_args()

    checks = audit(args.mass_msun, args.chi)
    rg = gravitational_radius_km(args.mass_msun)
    rlo, rhi = horizon_envelope_fixed_mass_spin_km(args.mass_msun, args.chi)

    print("DSD gravity angular-momentum hierarchy audit — BH-RB-004")
    print("---------------------------------------------------------")
    print(f"mass_msun={args.mass_msun:.12g}")
    print(f"chi={args.chi:.12g}")
    print(f"r_g_km={rg:.12g}")
    print(f"unknown_Q_horizon_lower_km={rlo:.12g}")
    print(f"unknown_Q_horizon_upper_km={rhi:.12g}")
    print()
    failures = 0
    for name, ok, note in checks:
        failures += 0 if ok else 1
        print(f"{'PASS' if ok else 'FAIL'}: {name} -- {note}")
    print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")
    print()
    print("Boundary:")
    print("raw DSD values, scalar aggregates, or local momentum records are not identified with global black-hole angular momentum.")
    print("Global J requires an explicit relativistic symmetry/asymptotic/boundary construction.")
    print("Kerr/Kerr-Newman relations are external GR comparators, not generic DSD laws.")


if __name__ == "__main__":
    main()
