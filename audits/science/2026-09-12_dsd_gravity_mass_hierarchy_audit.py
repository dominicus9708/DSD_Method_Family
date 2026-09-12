#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

G = 6.67430e-11
C = 299_792_458.0
M_SUN = 1.98847e30
AU_KM = 149_597_870.7


@dataclass(frozen=True)
class PromotionGate:
    name: str
    required: tuple[str, ...]
    note: str


def lorentz_gamma(beta: float) -> float:
    if not (0.0 <= abs(beta) < 1.0):
        raise ValueError("|beta| must be < 1")
    return 1.0 / math.sqrt(1.0 - beta * beta)


def sr_total_energy_j(rest_mass_kg: float, beta: float) -> float:
    return lorentz_gamma(beta) * rest_mass_kg * C**2


def sr_momentum_kg_m_s(rest_mass_kg: float, beta: float) -> float:
    return lorentz_gamma(beta) * rest_mass_kg * beta * C


def invariant_mass_from_energy_momentum_kg(energy_j: float, momentum_kg_m_s: float) -> float:
    m2 = (energy_j / C**2) ** 2 - (momentum_kg_m_s / C) ** 2
    if m2 < -1e-12:
        raise ValueError("spacelike four-momentum in this toy audit")
    return math.sqrt(max(0.0, m2))


def dust_energy_density_ratio(beta: float) -> float:
    # For pressureless dust T_ab = rho0 U_a U_b, an observer u measures
    # epsilon(u) = T_ab u^a u^b = rho0 * gamma_rel^2.
    g = lorentz_gamma(beta)
    return g * g


def gravitational_radius_km(mass_msun: float) -> float:
    return G * mass_msun * M_SUN / C**2 / 1000.0


def schwarzschild_horizon_km_from_global_mass(mass_msun: float) -> float:
    return 2.0 * gravitational_radius_km(mass_msun)


def naive_schwarzschild_horizon_km_from_observer_energy(mass_msun: float, beta: float) -> float:
    # Deliberately wrong promotion witness:
    # replace invariant/global mass by E_observer/c^2 = gamma M.
    # The frame dependence demonstrates why this cannot define a geometric BH mass.
    return lorentz_gamma(beta) * schwarzschild_horizon_km_from_global_mass(mass_msun)


def promotion_gates() -> tuple[PromotionGate, ...]:
    return (
        PromotionGate(
            "DSD_TYPED_VALUE_TO_LOCAL_ENERGY_DENSITY",
            (
                "defined typed DSD property record",
                "explicit physical interpretation and units",
                "spacetime localization",
                "Lorentzian metric",
                "observer four-velocity u^mu",
                "stress-energy representation T_munu",
            ),
            "A raw DSD scalar is not epsilon(u) by label; epsilon(u)=T_munu u^mu u^nu is observer-dependent.",
        ),
        PromotionGate(
            "LOCAL_DENSITY_TO_SLICE_MATTER_ENERGY",
            (
                "spacelike hypersurface Sigma",
                "future unit normal n^mu",
                "induced volume element dSigma",
                "integration domain and boundary data",
                "chosen observer or symmetry field",
            ),
            "A local density does not determine an integral until slice and measure structure are supplied.",
        ),
        PromotionGate(
            "SLICE_MATTER_ENERGY_TO_CONSERVED_MATTER_CHARGE",
            (
                "divergence law nabla_mu T^{mu nu}=0",
                "Killing/symmetry vector xi^mu or equivalent conservation structure",
                "appropriate boundary-flux conditions",
            ),
            "Typing and integration alone do not create a conserved charge.",
        ),
        PromotionGate(
            "CONSERVED_MATTER_CHARGE_TO_GLOBAL_GRAVITATIONAL_MASS",
            (
                "Einstein/relativistic gravitational dynamics",
                "metric and extrinsic-curvature initial data",
                "asymptotic flatness or another explicit global-mass framework",
                "normalization/frame conditions",
            ),
            "Matter charge is not generically ADM/Komar/Bondi mass; gravity has global geometric energy data.",
        ),
        PromotionGate(
            "GLOBAL_MASS_TO_BLACK_HOLE_RADIUS_PARAMETER",
            (
                "specified standard-GR solution class",
                "stationarity/symmetry assumptions as required",
                "asymptotic/boundary normalization",
            ),
            "Only at this external GR stage may M be inserted into Schwarzschild/Kerr/Kerr-Newman comparator radii.",
        ),
    )


def audit(mass_msun: float, beta: float) -> list[tuple[str, bool, str]]:
    checks: list[tuple[str, bool, str]] = []

    gamma = lorentz_gamma(beta)
    rest_mass_kg = mass_msun * M_SUN
    energy = sr_total_energy_j(rest_mass_kg, beta)
    momentum = sr_momentum_kg_m_s(rest_mass_kg, beta)
    recovered = invariant_mass_from_energy_momentum_kg(energy, momentum)

    checks.append((
        "OBSERVER_ENERGY_IS_FRAME_DEPENDENT",
        beta == 0.0 or gamma > 1.0,
        "E_observer=gamma M c^2 changes with frame and therefore is not itself the invariant black-hole mass.",
    ))

    checks.append((
        "INVARIANT_MASS_RECOVERED_FROM_FOUR_MOMENTUM",
        math.isclose(recovered, rest_mass_kg, rel_tol=2e-15),
        "sqrt((E/c^2)^2-(p/c)^2) recovers the invariant mass in the SR control witness.",
    ))

    checks.append((
        "LOCAL_DUST_ENERGY_DENSITY_IS_OBSERVER_DEPENDENT",
        beta == 0.0 or dust_energy_density_ratio(beta) > 1.0,
        "for dust, epsilon(u)/rho0=gamma^2; local energy density is not an observer-independent mass scalar.",
    ))

    invariant_horizon = schwarzschild_horizon_km_from_global_mass(mass_msun)
    naive_horizon = naive_schwarzschild_horizon_km_from_observer_energy(mass_msun, beta)
    checks.append((
        "OBSERVER_ENERGY_CANNOT_DEFINE_SCHWARZSCHILD_RADIUS",
        beta == 0.0 or not math.isclose(invariant_horizon, naive_horizon, rel_tol=1e-15),
        "substituting E_observer/c^2 for M makes the horizon radius frame-dependent, which is a category error.",
    ))

    checks.append((
        "VACUUM_EXTERIOR_MATTER_ENERGY_NOT_EQUAL_GLOBAL_MASS",
        True,
        "standard vacuum black-hole exterior can have T_munu=0 while ADM/Komar mass is nonzero; local/slice matter energy does not exhaust gravitational mass.",
    ))

    checks.append((
        "GLOBAL_MASS_REQUIRES_EXTERNAL_GEOMETRIC_STRUCTURE",
        True,
        "ADM mass requires asymptotically flat geometric initial data; stationary Komar mass requires a timelike Killing field and normalization.",
    ))

    checks.append((
        "DSD_AGGREGATE_NOT_PROMOTED_DIRECTLY_TO_BH_MASS",
        True,
        "current DSD papers require explicit downstream physical bridges and do not identify static aggregates with physical mass by definition.",
    ))

    return checks


def print_report(mass_msun: float, beta: float) -> None:
    gamma = lorentz_gamma(beta)
    rest_mass_kg = mass_msun * M_SUN
    energy = sr_total_energy_j(rest_mass_kg, beta)
    momentum = sr_momentum_kg_m_s(rest_mass_kg, beta)
    recovered = invariant_mass_from_energy_momentum_kg(energy, momentum)
    r_h = schwarzschild_horizon_km_from_global_mass(mass_msun)
    r_naive = naive_schwarzschild_horizon_km_from_observer_energy(mass_msun, beta)

    print("DSD gravity mass hierarchy audit — BH-RB-003")
    print("--------------------------------------------")
    print(f"mass_msun={mass_msun:.12g}")
    print(f"beta={beta:.12g}")
    print(f"gamma={gamma:.12g}")
    print(f"dust_local_energy_density_ratio_gamma2={dust_energy_density_ratio(beta):.12g}")
    print(f"observer_total_energy_J={energy:.12g}")
    print(f"observer_momentum_kg_m_s={momentum:.12g}")
    print(f"recovered_invariant_mass_msun={recovered / M_SUN:.12g}")
    print(f"schwarzschild_horizon_from_global_mass_km={r_h:.12g}")
    print(f"naive_horizon_from_observer_E_over_c2_km={r_naive:.12g}")
    print(f"naive_radius_ratio={r_naive / r_h:.12g}")
    print(f"schwarzschild_horizon_from_global_mass_AU={r_h / AU_KM:.12g}")

    print()
    print("Promotion gates")
    for gate in promotion_gates():
        print(f"- {gate.name}")
        for req in gate.required:
            print(f"    requires: {req}")
        print(f"    note: {gate.note}")

    print()
    print("Audit")
    checks = audit(mass_msun, beta)
    failures = 0
    for name, ok, note in checks:
        failures += 0 if ok else 1
        print(f"{'PASS' if ok else 'FAIL'}: {name} -- {note}")
    print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")

    print()
    print("Boundary")
    print("epsilon(u), slice matter energy, symmetry energy, ADM/Komar/Bondi-type mass, and black-hole solution parameter M are not identified by definition.")
    print("Only an explicitly supplied global relativistic mass is eligible for the standard-GR black-hole radius comparator.")
    print("The discarded K_g/Theta/Psi structural-gravity branch is not used.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit the DSD-to-GR mass hierarchy used by black-hole radius work.")
    parser.add_argument("--mass-msun", type=float, default=4.297e6)
    parser.add_argument("--beta", type=float, default=0.6, help="SR control boost, |beta|<1; not a Sgr A* velocity measurement.")
    args = parser.parse_args()
    print_report(args.mass_msun, args.beta)


if __name__ == "__main__":
    main()
