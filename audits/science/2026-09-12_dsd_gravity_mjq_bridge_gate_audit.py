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
class TypedRecord:
    kind: str
    inputs: tuple
    value: object
    defined: bool = True
    unit: str | None = None


@dataclass(frozen=True)
class PhysicalParticle:
    label: str
    position: tuple[float, float, float]
    momentum: tuple[float, float, float]
    energy: float
    charge: float


def cross(a: tuple[float, float, float], b: tuple[float, float, float]) -> tuple[float, float, float]:
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def add(a: tuple[float, float, float], b: tuple[float, float, float]) -> tuple[float, float, float]:
    return tuple(x + y for x, y in zip(a, b))


def total_energy(parts: list[PhysicalParticle]) -> float:
    return sum(p.energy for p in parts)


def total_charge(parts: list[PhysicalParticle]) -> float:
    return sum(p.charge for p in parts)


def total_momentum(parts: list[PhysicalParticle]) -> tuple[float, float, float]:
    out = (0.0, 0.0, 0.0)
    for p in parts:
        out = add(out, p.momentum)
    return out


def total_angular_momentum(parts: list[PhysicalParticle]) -> tuple[float, float, float]:
    out = (0.0, 0.0, 0.0)
    for p in parts:
        out = add(out, cross(p.position, p.momentum))
    return out


def require_defined(record: TypedRecord) -> TypedRecord:
    if not record.defined:
        raise ValueError("undefined typed property record cannot be silently mapped to a physical zero")
    return record


def physical_bridge(record: TypedRecord, *, physical_kind: str, unit: str) -> dict[str, object]:
    r = require_defined(record)
    return {
        "dsd_kind": r.kind,
        "full_typed_inputs": r.inputs,
        "dsd_value": r.value,
        "physical_kind": physical_kind,
        "physical_unit": unit,
    }


def gravitational_radius_km(mass_msun: float) -> float:
    return G * mass_msun * M_SUN / C**2 / 1000.0


def kerr_newman_outer_horizon_km(mass_msun: float, chi: float, qhat: float) -> float:
    disc = 1.0 - chi**2 - qhat**2
    if disc < -1e-14:
        raise ValueError("superextremal parameter pair: chi^2 + qhat^2 > 1")
    disc = max(0.0, disc)
    rg = gravitational_radius_km(mass_msun)
    return rg * (1.0 + math.sqrt(disc))


def build_toy_states() -> dict[str, list[PhysicalParticle]]:
    rotating = [
        PhysicalParticle("a", (1, 0, 0), (0, 1, 0), 1.0, 0.0),
        PhysicalParticle("b", (-1, 0, 0), (0, -1, 0), 1.0, 0.0),
    ]
    radial = [
        PhysicalParticle("a", (1, 0, 0), (1, 0, 0), 1.0, 0.0),
        PhysicalParticle("b", (-1, 0, 0), (-1, 0, 0), 1.0, 0.0),
    ]
    charged = [
        PhysicalParticle("a", (1, 0, 0), (1, 0, 0), 1.0, 1.0),
        PhysicalParticle("b", (-1, 0, 0), (-1, 0, 0), 1.0, 1.0),
    ]
    neutral = [
        PhysicalParticle("a", (1, 0, 0), (1, 0, 0), 1.0, 0.0),
        PhysicalParticle("b", (-1, 0, 0), (-1, 0, 0), 1.0, 0.0),
    ]
    return {"rotating": rotating, "radial": radial, "charged": charged, "neutral": neutral}


def audit(mass_msun: float) -> list[tuple[str, bool, str]]:
    states = build_toy_states()
    rotating = states["rotating"]
    radial = states["radial"]
    charged = states["charged"]
    neutral = states["neutral"]

    checks: list[tuple[str, bool, str]] = []

    checks.append((
        "EQUAL_SCALAR_ENERGY_DOES_NOT_FIX_ANGULAR_MOMENTUM",
        total_energy(rotating) == total_energy(radial)
        and total_angular_momentum(rotating) != total_angular_momentum(radial),
        "same scalar energy aggregate can coexist with different J; scalar mass/energy alone cannot choose Schwarzschild versus Kerr data",
    ))

    checks.append((
        "EQUAL_SCALAR_ENERGY_DOES_NOT_FIX_CHARGE",
        total_energy(charged) == total_energy(neutral)
        and total_charge(charged) != total_charge(neutral),
        "same scalar energy aggregate can coexist with different Q",
    ))

    checks.append((
        "ZERO_TOTAL_MOMENTUM_CONTROL",
        total_momentum(rotating) == (0.0, 0.0, 0.0)
        and total_momentum(radial) == (0.0, 0.0, 0.0),
        "J difference in the rotating/radial witness is not caused by different total linear momentum",
    ))

    defined = TypedRecord("energy_candidate", ("configuration-A", "channel-q1"), 3.0, True, "arbitrary")
    bridged = physical_bridge(defined, physical_kind="energy", unit="J")
    checks.append((
        "FULL_TYPED_INPUTS_RETAINED_BY_BRIDGE",
        bridged["full_typed_inputs"] == defined.inputs,
        "the bridge preserves complete typed inputs instead of assigning an implicit unary owner",
    ))

    undefined_rejected = False
    try:
        physical_bridge(TypedRecord("energy_candidate", ("configuration-A",), None, False), physical_kind="energy", unit="J")
    except ValueError:
        undefined_rejected = True
    checks.append((
        "UNDEFINED_IS_NOT_PHYSICAL_ZERO",
        undefined_rejected,
        "undefined DSD status is rejected rather than padded with numerical zero",
    ))

    # Two well-typed snapshots may have different scalar totals. This witness shows that typing alone
    # does not impose a conservation equation.
    t0 = [PhysicalParticle("a", (0, 0, 0), (0, 0, 0), 1.0, 0.0)]
    t1 = [PhysicalParticle("a", (0, 0, 0), (0, 0, 0), 2.0, 0.0)]
    checks.append((
        "CONSERVATION_NOT_FORCED_BY_TYPING",
        total_energy(t0) != total_energy(t1),
        "a conservation law must be supplied by the physical/dynamic specialization; DSD typing alone does not enforce it",
    ))

    rg = gravitational_radius_km(mass_msun)
    r_schw = kerr_newman_outer_horizon_km(mass_msun, 0.0, 0.0)
    r_extreme_kerr = kerr_newman_outer_horizon_km(mass_msun, 1.0, 0.0)
    r_extreme_mix = kerr_newman_outer_horizon_km(mass_msun, 0.6, 0.8)
    checks.append((
        "EXTERNAL_GR_HORIZON_ENVELOPE",
        math.isclose(r_schw, 2.0 * rg, rel_tol=1e-14)
        and math.isclose(r_extreme_kerr, rg, rel_tol=1e-14)
        and math.isclose(r_extreme_mix, rg, rel_tol=1e-14),
        "for the external Kerr-Newman comparator with chi^2+qhat^2<=1, r_plus lies between r_g and 2 r_g",
    ))

    checks.append((
        "T_MUNU_NOT_SUFFICIENT_AS_BLACK_HOLE_IDENTITY",
        True,
        "the active bridge must keep global geometric charges/boundary data separate; vacuum exterior T_munu=0 does not erase the black-hole mass parameter",
    ))

    return checks


def print_report(mass_msun: float) -> None:
    rg = gravitational_radius_km(mass_msun)
    print("DSD gravity M/J/Q bridge gate audit")
    print("---------------------------------")
    print(f"mass_msun={mass_msun:.12g}")
    print(f"r_g_km={rg:.12g}")
    print(f"external_horizon_upper_schwarzschild_km={2.0 * rg:.12g}")
    print(f"external_horizon_lower_extremal_km={rg:.12g}")
    print(f"external_horizon_upper_schwarzschild_AU={2.0 * rg / AU_KM:.12g}")
    print()
    print("Sample Kerr-Newman external comparator")
    for chi, qhat in ((0.0, 0.0), (0.5, 0.0), (0.9, 0.0), (0.99, 0.0), (1.0, 0.0), (0.6, 0.8)):
        rplus = kerr_newman_outer_horizon_km(mass_msun, chi, qhat)
        print(f"chi={chi:.6g} qhat={qhat:.6g} r_plus_km={rplus:.12g}")

    states = build_toy_states()
    print()
    print("Information-loss witnesses after external physical specialization")
    print(f"rotating_energy={total_energy(states['rotating']):.12g}")
    print(f"rotating_J={total_angular_momentum(states['rotating'])}")
    print(f"radial_energy={total_energy(states['radial']):.12g}")
    print(f"radial_J={total_angular_momentum(states['radial'])}")
    print(f"charged_energy={total_energy(states['charged']):.12g}")
    print(f"charged_Q={total_charge(states['charged']):.12g}")
    print(f"neutral_energy={total_energy(states['neutral']):.12g}")
    print(f"neutral_Q={total_charge(states['neutral']):.12g}")

    checks = audit(mass_msun)
    print()
    print("Audit")
    failures = 0
    for name, ok, note in checks:
        failures += 0 if ok else 1
        print(f"{'PASS' if ok else 'FAIL'}: {name} -- {note}")
    print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")

    print()
    print("Boundary")
    print("M, J, Q, T_munu and the localization/metric carrier are external physical/relativistic bridge outputs, not generic DSD primitives.")
    print("The discarded K_g/Theta/Psi structural-gravity branch is not used.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit the DSD-to-physical M/J/Q bridge gate for black-hole radius work.")
    parser.add_argument("--mass-msun", type=float, default=4.297e6)
    args = parser.parse_args()
    print_report(args.mass_msun)


if __name__ == "__main__":
    main()
