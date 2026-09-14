#!/usr/bin/env python3
"""BH-RB-022: trapped-core EOS coupling gate.

Couples the BH-RB-021 globally causal self-bound EOS control to the
spherically symmetric Misner-Sharp collapse identities in geometrized units
G=c=1. The audit asks whether positive pressure from the causal self-bound EOS
can by itself generate a finite-radius turning point while the same comoving
shell remains trapped.

This is a standard-GR comparator, not a DSD-derived gravity law and not a
derivation of a physical black-hole-core EOS.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class EOSParams:
    mc2: float = 1.0
    B: float = 1.0
    y: float = 0.2

    @property
    def A(self) -> float:
        return math.sqrt(4.0 * self.B * self.mc2 * self.y)

    @property
    def n_star(self) -> float:
        return self.A / (2.0 * self.B)

    @property
    def n_causal(self) -> float:
        return math.sqrt(self.mc2 / (3.0 * self.B))


@dataclass
class Check:
    name: str
    passed: bool
    detail: str


def eps_low(n: float, q: EOSParams) -> float:
    return q.mc2 * n - q.A * n**2 + q.B * n**3


def p_low(n: float, q: EOSParams) -> float:
    return -q.A * n**2 + 2.0 * q.B * n**3


def mu_low(n: float, q: EOSParams) -> float:
    return q.mc2 - 2.0 * q.A * n + 3.0 * q.B * n**2


def cs2_low(n: float, q: EOSParams) -> float:
    dp_dn = -2.0 * q.A * n + 6.0 * q.B * n**2
    return dp_dn / mu_low(n, q)


def misner_sharp_gamma_sq(compactness: float, u: float) -> float:
    """Gamma^2 = 1 + U^2 - 2m/R, with compactness C=2m/R."""
    return 1.0 + u * u - compactness


def trapped_speed_floor(compactness: float) -> float:
    """Minimum |U| allowed by Gamma^2>=0 when C>1."""
    if compactness <= 1.0:
        return 0.0
    return math.sqrt(compactness - 1.0)


def perfect_fluid_mass_rate(radius: float, pressure: float, u: float) -> float:
    """D_T m = -4 pi R^2 p U for a comoving spherical perfect fluid."""
    return -4.0 * math.pi * radius**2 * pressure * u


def compactness_rate(
    compactness: float,
    radius: float,
    mass_rate: float,
    u: float,
) -> float:
    """D_T(2m/R) in geometrized units."""
    return 2.0 * mass_rate / radius - compactness * u / radius


def mass_loss_threshold_for_decompaction(compactness: float, u: float) -> float:
    """dC/dtau<0 requires dm/dtau < C U / 2."""
    return 0.5 * compactness * u


def almost(a: float, b: float, tol: float = 2e-12) -> bool:
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)


def run_checks() -> list[Check]:
    q = EOSParams()
    checks: list[Check] = []

    checks.append(Check(
        "BH-RB-021 control remains inside the self-bound causal window",
        0.0 < q.y <= 1.0 / 3.0,
        f"y={q.y:.6f}, required 0<y<=1/3.",
    ))

    eps0 = eps_low(q.n_star, q)
    checks.append(Check(
        "finite-density zero-pressure self-bound surface is preserved",
        q.n_star > 0.0 and eps0 > 0.0 and almost(p_low(q.n_star, q), 0.0),
        f"n*={q.n_star:.12f}, epsilon0={eps0:.12f}, p(n*)={p_low(q.n_star,q):.3e}.",
    ))

    sample_n = [
        q.n_star + (q.n_causal - q.n_star) * i / 100.0
        for i in range(101)
    ]
    pressures = [p_low(n, q) for n in sample_n]
    sounds = [cs2_low(n, q) for n in sample_n]
    checks.append(Check(
        "declared low-density physical branch has nonnegative pressure",
        min(pressures) >= -1e-12,
        f"pressure range=[{min(pressures):.12f}, {max(pressures):.12f}].",
    ))
    checks.append(Check(
        "declared low-density physical branch remains causal",
        min(sounds) >= -1e-12 and max(sounds) <= 1.0 + 1e-12,
        f"cs^2/c^2 range=[{min(sounds):.12f}, {max(sounds):.12f}].",
    ))

    for c in (1.01, 1.10, 1.50, 2.00):
        umin = trapped_speed_floor(c)
        gamma2 = misner_sharp_gamma_sq(c, -umin)
        checks.append(Check(
            f"trapped compactness C={c:.2f} enforces nonzero collapse-speed floor",
            umin > 0.0 and almost(gamma2, 0.0),
            f"|U|min=sqrt(C-1)={umin:.12f}, Gamma^2 at the floor={gamma2:.3e}.",
        ))

    turning_cs = [0.2, 0.8, 1.0, 1.2, 2.0]
    admissible = [
        c for c in turning_cs
        if misner_sharp_gamma_sq(c, 0.0) >= -1e-12
    ]
    checks.append(Check(
        "a regular spherical turning point U=0 requires C<=1",
        all(c <= 1.0 + 1e-12 for c in admissible)
        and all(misner_sharp_gamma_sq(c, 0.0) < 0.0 for c in turning_cs if c > 1.0),
        f"turning-point-admissible sample compactness values={admissible}.",
    ))

    delta = 0.25
    r0 = 1.0
    r_target = 0.2
    speed_floor = math.sqrt(delta)
    tau_max = (r0 - r_target) / speed_floor
    checks.append(Check(
        "persistent C>=1+delta gives a proper-time contraction bound",
        speed_floor > 0.0 and tau_max > 0.0,
        (
            f"delta={delta:.3f}: |U|>={speed_floor:.6f}; "
            f"R:{r0:.1f}->{r_target:.1f} cannot take longer than "
            f"{tau_max:.6f} geometrized proper-time units if the bound persists."
        ),
    ))

    n_probe = 0.5 * (q.n_star + q.n_causal)
    p_probe = p_low(n_probe, q)
    radius = 1.0
    u = -0.5
    mdot = perfect_fluid_mass_rate(radius, p_probe, u)
    checks.append(Check(
        "positive pressure during comoving collapse increases Misner-Sharp mass",
        p_probe > 0.0 and u < 0.0 and mdot > 0.0,
        f"n={n_probe:.12f}, p={p_probe:.12f}, U={u:.3f}, D_T m={mdot:.12f}.",
    ))

    c = 1.5
    cdot = compactness_rate(c, radius, mdot, u)
    checks.append(Check(
        "no-flux positive-pressure collapse increases compactness",
        cdot > 0.0,
        f"C={c:.3f}, D_T C={cdot:.12f}>0.",
    ))

    mdot_surface = perfect_fluid_mass_rate(radius, 0.0, u)
    cdot_surface = compactness_rate(c, radius, mdot_surface, u)
    checks.append(Check(
        "a collapsing zero-pressure comoving surface still increases compactness",
        almost(mdot_surface, 0.0) and cdot_surface > 0.0,
        f"D_T m={mdot_surface:.3e}, D_T C={cdot_surface:.12f}>0.",
    ))

    threshold = mass_loss_threshold_for_decompaction(c, u)
    checks.append(Check(
        "decompaction during collapse requires sufficiently negative mass rate",
        threshold < 0.0 and mdot > threshold,
        (
            f"For C={c:.3f}, U={u:.3f}, D_T C<0 requires "
            f"D_T m<{threshold:.12f}; perfect-fluid value is {mdot:.12f}."
        ),
    ))

    synthetic_mdot = 1.2 * threshold
    synthetic_cdot = compactness_rate(c, radius, synthetic_mdot, u)
    checks.append(Check(
        "sufficient outward mass-energy loss can in principle reduce compactness",
        synthetic_mdot < threshold and synthetic_cdot < 0.0,
        f"synthetic D_T m={synthetic_mdot:.12f} gives D_T C={synthetic_cdot:.12f}.",
    ))

    near_marginal = [1.1, 1.01, 1.001, 1.000001]
    floors = [trapped_speed_floor(cn) for cn in near_marginal]
    checks.append(Check(
        "the collapse-speed floor vanishes only as C approaches the marginal value 1",
        all(floors[i+1] < floors[i] for i in range(len(floors)-1))
        and floors[-1] < 0.002,
        "speed floors=" + ", ".join(f"{v:.6g}" for v in floors) + ".",
    ))

    return checks


def report() -> int:
    checks = run_checks()
    passed = sum(c.passed for c in checks)
    total = len(checks)

    for i, c in enumerate(checks, 1):
        print(f"[{i:02d}] {'PASS' if c.passed else 'FAIL'} — {c.name}")
        print(f"     {c.detail}")

    print()
    print(f"RESULT: {passed}/{total} PASS")

    if passed == total:
        print(
            "VERDICT: PASS_WITH_BOUNDARY / "
            "CAUSAL_SELF_BOUND_EOS_COUPLED_TO_SPHERICAL_GR / "
            "PERSISTENTLY_TRAPPED_TURNING_POINT_EXCLUDED / "
            "NO_FLUX_POSITIVE_PRESSURE_DOES_NOT_GENERATE_RMIN / "
            "DETRAPPING_OR_MASS_FLUX_OR_NONSPHERICAL_DYNAMICS_REQUIRED / "
            "FINITE_BLACK_HOLE_CORE_RADIUS_NOT_DERIVED"
        )
        return 0

    print("VERDICT: FAIL")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("all", "checks"), default="all")
    args = parser.parse_args()

    if args.mode in {"all", "checks"}:
        return report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
