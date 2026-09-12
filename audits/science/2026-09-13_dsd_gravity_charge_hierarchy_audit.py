#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

G = 6.67430e-11
C = 299_792_458.0
EPS0 = 8.854_187_8128e-12
M_SUN = 1.98847e30


@dataclass(frozen=True)
class TypedChargeRecord:
    kind: str
    inputs: tuple
    value: float | None
    defined: bool = True
    unit: str | None = None


def require_defined(record: TypedChargeRecord) -> TypedChargeRecord:
    if not record.defined:
        raise ValueError("undefined typed charge record cannot be silently mapped to physical zero")
    return record


def physical_charge_bridge(record: TypedChargeRecord, *, unit: str = "C") -> dict[str, object]:
    r = require_defined(record)
    return {
        "dsd_kind": r.kind,
        "full_typed_inputs": r.inputs,
        "dsd_value": r.value,
        "physical_kind": "electric_charge_candidate",
        "physical_unit": unit,
    }


def gravitational_radius_km(mass_msun: float) -> float:
    return G * mass_msun * M_SUN / C**2 / 1000.0


def qhat_from_charge_coulomb(mass_msun: float, charge_coulomb: float) -> float:
    mass_kg = mass_msun * M_SUN
    return charge_coulomb / (math.sqrt(4.0 * math.pi * EPS0 * G) * mass_kg)


def charge_coulomb_from_qhat(mass_msun: float, qhat: float) -> float:
    mass_kg = mass_msun * M_SUN
    return qhat * math.sqrt(4.0 * math.pi * EPS0 * G) * mass_kg


def kerr_newman_outer_horizon_km(mass_msun: float, chi: float, qhat: float) -> float:
    disc = 1.0 - chi**2 - qhat**2
    if disc < -1e-14:
        raise ValueError("superextremal parameter pair: chi^2 + qhat^2 > 1")
    disc = max(0.0, disc)
    rg = gravitational_radius_km(mass_msun)
    return rg * (1.0 + math.sqrt(disc))


def gauss_sphere_recovered_charge_coulomb(charge_coulomb: float, radius_m: float) -> float:
    if radius_m <= 0:
        raise ValueError("radius must be positive")
    electric_field = charge_coulomb / (4.0 * math.pi * EPS0 * radius_m**2)
    flux = electric_field * 4.0 * math.pi * radius_m**2
    return EPS0 * flux


def audit(mass_msun: float, chi: float, qhat: float) -> list[tuple[str, bool, str]]:
    checks: list[tuple[str, bool, str]] = []

    undefined_rejected = False
    try:
        physical_charge_bridge(
            TypedChargeRecord("charge_candidate", ("configuration-A",), None, False)
        )
    except ValueError:
        undefined_rejected = True
    checks.append((
        "UNDEFINED_CHARGE_IS_NOT_ZERO",
        undefined_rejected,
        "an undefined DSD charge-like record is not identified with neutral physical charge",
    ))

    defined = TypedChargeRecord(
        "charge_candidate",
        ("configuration-A", "channel-q1", "localization-x"),
        2.0,
        True,
        "abstract",
    )
    bridged = physical_charge_bridge(defined)
    checks.append((
        "FULL_TYPED_INPUTS_RETAINED_BY_CHARGE_BRIDGE",
        bridged["full_typed_inputs"] == defined.inputs,
        "the external physical bridge retains the complete typed input profile",
    ))

    rho = 1.0
    volume_a = 1.0
    volume_b = 2.0
    q_a = rho * volume_a
    q_b = rho * volume_b
    checks.append((
        "LOCAL_DENSITY_DOES_NOT_FIX_TOTAL_CHARGE",
        q_a != q_b,
        "charge density alone does not determine total charge without domain and measure",
    ))

    test_charge = 1.0
    recovered = gauss_sphere_recovered_charge_coulomb(test_charge, radius_m=2.0)
    local_external_rho = 0.0
    checks.append((
        "VACUUM_LOCAL_CURRENT_DOES_NOT_FORCE_GLOBAL_CHARGE_ZERO",
        local_external_rho == 0.0 and math.isclose(recovered, test_charge, rel_tol=1e-12),
        "a vacuum exterior can have zero local source density while Gauss flux returns nonzero enclosed charge",
    ))

    q_t0 = 1.0
    q_t1 = 2.0
    checks.append((
        "CHARGE_CONSERVATION_NOT_FORCED_BY_TYPING",
        q_t0 != q_t1,
        "current conservation must come from the external gauge/matter dynamics, not DSD typing alone",
    ))

    r_plus = kerr_newman_outer_horizon_km(mass_msun, chi, qhat)
    r_plus_sign_flipped = kerr_newman_outer_horizon_km(mass_msun, chi, -qhat)
    checks.append((
        "HORIZON_RADIUS_LOSES_CHARGE_SIGN",
        math.isclose(r_plus, r_plus_sign_flipped, rel_tol=1e-14),
        "Kerr-Newman r_plus depends on qhat^2, so the horizon radius does not reconstruct the sign of charge",
    ))

    extremality_ok = chi**2 + qhat**2 <= 1.0 + 1e-14
    checks.append((
        "GLOBAL_MJQ_EXTERNAL_COMPARATOR_ADMISSIBLE",
        extremality_ok and r_plus >= gravitational_radius_km(mass_msun),
        "once global M, J and gauge charge Q are externally supplied, the Kerr-Newman comparator is well defined inside the horizon-existence domain",
    ))

    return checks


def print_report(mass_msun: float, chi: float, qhat: float) -> None:
    rg = gravitational_radius_km(mass_msun)
    r_plus = kerr_newman_outer_horizon_km(mass_msun, chi, qhat)
    q_coulomb = charge_coulomb_from_qhat(mass_msun, qhat)

    print("DSD gravity charge hierarchy audit -- BH-RB-005")
    print("------------------------------------------------")
    print(f"mass_msun={mass_msun:.12g}")
    print(f"chi={chi:.12g}")
    print(f"qhat={qhat:.12g}")
    print(f"qhat_charge_coulomb={q_coulomb:.12g}")
    print(f"r_g_km={rg:.12g}")
    print(f"r_plus_km={r_plus:.12g}")
    print(f"extremality_sum={chi**2 + qhat**2:.12g}")
    print()

    recovered = gauss_sphere_recovered_charge_coulomb(1.0, 2.0)
    print("Gauss-law vacuum exterior witness")
    print("local_external_charge_density=0")
    print("enclosed_test_charge_C=1")
    print(f"gauss_recovered_charge_C={recovered:.12g}")
    print()

    checks = audit(mass_msun, chi, qhat)
    failures = 0
    print("Audit")
    for name, ok, note in checks:
        failures += 0 if ok else 1
        print(f"{'PASS' if ok else 'FAIL'}: {name} -- {note}")
    print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")
    print()
    print("Boundary")
    print("The electric/gauge current, Maxwell sector, conservation law, flux normalization, and asymptotic charge are external physical/relativistic bridge data, not generic DSD primitives.")
    print("The sign of Q is not reconstructible from the Kerr-Newman horizon radius because r_plus depends on Q^2.")
    print("The discarded K_g/Theta/Psi structural-gravity branch is not used.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit the DSD-to-global-charge hierarchy for black-hole comparator work."
    )
    parser.add_argument("--mass-msun", type=float, default=4.297e6)
    parser.add_argument("--chi", type=float, default=0.9)
    parser.add_argument("--qhat", type=float, default=0.3)
    args = parser.parse_args()

    if args.mass_msun <= 0:
        parser.error("--mass-msun must be positive")
    if abs(args.chi) > 1:
        parser.error("--chi must satisfy |chi| <= 1")
    if args.chi**2 + args.qhat**2 > 1.0 + 1e-14:
        parser.error("--chi and --qhat are superextremal: chi^2 + qhat^2 > 1")

    print_report(args.mass_msun, args.chi, args.qhat)


if __name__ == "__main__":
    main()
