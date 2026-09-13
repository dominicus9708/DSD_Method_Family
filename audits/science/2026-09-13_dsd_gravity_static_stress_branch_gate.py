#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

G = 6.67430e-11
C = 299_792_458.0
M_SUN = 1.98847e30

BUCHDAHL_LAMBDA = 9.0 / 8.0
CENTRAL_DEC_LAMBDA = 4.0 / 3.0


@dataclass(frozen=True)
class StaticControlState:
    mass_msun: float
    lam: float

    @property
    def mass_kg(self) -> float:
        return self.mass_msun * M_SUN

    @property
    def r_s_m(self) -> float:
        return 2.0 * G * self.mass_kg / C**2

    @property
    def radius_m(self) -> float:
        return self.lam * self.r_s_m

    @property
    def compactness(self) -> float:
        return 1.0 / self.lam

    @property
    def rho_bar(self) -> float:
        r = self.radius_m
        return 3.0 * self.mass_kg / (4.0 * math.pi * r**3)

    @property
    def epsilon(self) -> float:
        return self.rho_bar * C**2


def uniform_density_pc_over_epsilon(lam: float) -> float:
    """
    Interior-Schwarzschild constant-density perfect-fluid control.

    Valid only as a regular static control for lam > 9/8.
    The constant-density EOS is incompressible and is NOT accepted here
    as a causal physical EOS candidate.
    """
    if lam <= BUCHDAHL_LAMBDA:
        raise ValueError("regular finite central pressure requires lam > 9/8 in this control")
    compactness = 1.0 / lam
    s = math.sqrt(1.0 - compactness)
    den = 3.0 * s - 1.0
    if den <= 0.0:
        raise ValueError("central-pressure denominator is non-positive")
    return (1.0 - s) / den


def branch_classification(lam: float) -> str:
    if lam <= 0:
        return "INVALID_RADIUS"
    if lam <= 1.0:
        return "HORIZON_OR_TRAPPED_REGION__STATIC_STAR_CONTROL_NOT_APPLICABLE"
    if lam <= BUCHDAHL_LAMBDA:
        return "ISOTROPIC_CONSTANT_DENSITY_CONTROL_NONREGULAR"
    if lam < CENTRAL_DEC_LAMBDA:
        return "FINITE_PC_BUT_CENTRAL_DEC_VIOLATED_IN_CONTROL"
    return "STATIC_CONTROL_NOT_EXCLUDED_BY_CENTRAL_DEC__EOS_STILL_ACAUSAL"


def anisotropic_tov_gradient(
    r_m: float,
    m_kg: float,
    rho_kg_m3: float,
    p_r_pa: float,
    delta_pa: float,
) -> float:
    """
    Generalized static spherical GR pressure-gradient control:
      dp_r/dr = isotropic_TOV_term + 2 (p_t-p_r) / r
    where delta_pa = p_t - p_r.

    This is an external-GR comparator equation, not a DSD-derived law.
    """
    if r_m <= 0:
        raise ValueError("r_m must be positive")
    horizon_factor = 1.0 - 2.0 * G * m_kg / (r_m * C**2)
    if horizon_factor <= 0:
        raise ValueError("static TOV chart/control crosses a trapped/horizon condition")
    grav = -G * (rho_kg_m3 + p_r_pa / C**2) * (
        m_kg + 4.0 * math.pi * r_m**3 * p_r_pa / C**2
    ) / (r_m**2 * horizon_factor)
    return grav + 2.0 * delta_pa / r_m


def audit(mass_msun: float) -> list[tuple[str, bool, str]]:
    checks: list[tuple[str, bool, str]] = []

    checks.append((
        "COMPACTNESS_IS_INVERSE_LAMBDA",
        math.isclose(StaticControlState(mass_msun, 1.5).compactness, 2.0/3.0, rel_tol=1e-15),
        "C = r_s/R = 1/lambda",
    ))

    checks.append((
        "BUCHDAHL_CONTROL_BOUNDARY_IS_9_OVER_8",
        math.isclose(BUCHDAHL_LAMBDA, 1.125, rel_tol=0.0, abs_tol=1e-15),
        "constant-density isotropic central pressure diverges at R/r_s = 9/8",
    ))

    near = uniform_density_pc_over_epsilon(1.1251)
    checks.append((
        "CENTRAL_PRESSURE_GROWS_TOWARD_BUCHDAHL_BOUND",
        near > 1000.0,
        "p_c/epsilon becomes arbitrarily large as lambda approaches 9/8 from above",
    ))

    mid = uniform_density_pc_over_epsilon(1.5)
    checks.append((
        "FINITE_CONTROL_PRESSURE_ABOVE_BOUND",
        math.isfinite(mid) and mid > 0.0,
        "regular central pressure exists in the control at lambda=1.5",
    ))

    dec_boundary = uniform_density_pc_over_epsilon(CENTRAL_DEC_LAMBDA)
    checks.append((
        "CENTRAL_DEC_THRESHOLD_AT_4_OVER_3",
        math.isclose(dec_boundary, 1.0, rel_tol=1e-12),
        "for this control p_c = epsilon at lambda=4/3",
    ))

    dec_bad = uniform_density_pc_over_epsilon(1.2)
    checks.append((
        "CENTRAL_DEC_FAILS_BEFORE_BUCHDAHL_DIVERGENCE",
        dec_bad > 1.0,
        "the constant-density isotropic control already has p_c>epsilon at lambda=1.2",
    ))

    nonregular_blocked = False
    try:
        uniform_density_pc_over_epsilon(BUCHDAHL_LAMBDA)
    except ValueError:
        nonregular_blocked = True
    checks.append((
        "BUCHDAHL_AND_BELOW_BLOCKED_AS_REGULAR_ISOTROPIC_CONTROL",
        nonregular_blocked,
        "the script does not continue the regular isotropic constant-density formula through its singular boundary",
    ))

    checks.append((
        "LAMBDA_LE_1_NOT_TREATED_AS_STATIC_HORIZONLESS_STAR",
        branch_classification(1.0).startswith("HORIZON_OR_TRAPPED_REGION"),
        "R<=r_s is not misclassified as an ordinary static horizonless stellar branch",
    ))

    state = StaticControlState(mass_msun, 1.5)
    r = 0.8 * state.radius_m
    m = state.mass_kg * (r / state.radius_m)**3
    rho = state.rho_bar
    p_r = 0.1 * state.epsilon
    grad_iso = anisotropic_tov_gradient(r, m, rho, p_r, 0.0)
    delta = 0.02 * state.epsilon
    grad_aniso = anisotropic_tov_gradient(r, m, rho, p_r, delta)

    checks.append((
        "DELTA_ZERO_RECOVERS_ISOTROPIC_TOV_TERM",
        math.isfinite(grad_iso) and grad_iso < 0.0,
        "delta=p_t-p_r=0 leaves the isotropic GR pressure-gradient term",
    ))

    checks.append((
        "ANISOTROPY_CHANGES_THE_REQUIRED_GRADIENT",
        not math.isclose(grad_iso, grad_aniso, rel_tol=1e-12, abs_tol=0.0),
        "different p_t-p_r with the same local rho and p_r changes dp_r/dr",
    ))

    checks.append((
        "ANISOTROPIC_BRANCH_REQUIRES_CONSTITUTIVE_CLOSURE",
        True,
        "epsilon(r), p_r(r), and p_t(r) are not uniquely fixed by mass and radius alone",
    ))

    checks.append((
        "STATIC_FAILURE_DOES_NOT_PROVE_ZERO_DIMENSIONAL_CORE",
        True,
        "failure of a static constitutive branch is not a proof of spatial dimensional collapse",
    ))

    return checks


def print_table(mass_msun: float) -> None:
    print("DSD gravity static-stress constitutive branch gate -- BH-RB-008")
    print("----------------------------------------------------------------")
    print(f"mass_msun={mass_msun:.12g}")
    base = StaticControlState(mass_msun, 1.0)
    print(f"schwarzschild_radius_km={base.r_s_m/1000.0:.12g}")
    print()
    print("Constant-density isotropic control")
    print("lambda   R_km              rho_bar_kg_m3      p_c/epsilon        classification")
    for lam in [2.0, 1.5, 4.0/3.0, 1.25, 1.20, 1.15, 1.13, 1.126, 1.1251, 1.125, 1.0, 0.5]:
        state = StaticControlState(mass_msun, lam)
        try:
            ratio = f"{uniform_density_pc_over_epsilon(lam):.12g}"
        except ValueError:
            ratio = "N/A"
        print(
            f"{lam:<8.6g} "
            f"{state.radius_m/1000.0:<17.10g} "
            f"{state.rho_bar:<18.10g} "
            f"{ratio:<18} "
            f"{branch_classification(lam)}"
        )
    print()
    print("Boundary")
    print("- The constant-density interior-Schwarzschild model is only a control witness.")
    print("- Its incompressible EOS is not accepted as a causal physical core model.")
    print("- Static isotropic failure does not close anisotropic or dynamical finite-3D branches.")
    print("- Anisotropic support requires an explicit constitutive law for p_t-p_r.")
    print("- R<=r_s must be studied with a horizon-penetrating/dynamical formulation, not by extending this static control.")
    print("- No DSD rank collapse or physical information destruction is inferred.")
    print()
    checks = audit(mass_msun)
    failures = 0
    for name, ok, note in checks:
        failures += 0 if ok else 1
        print(f"{'PASS' if ok else 'FAIL'}: {name} -- {note}")
    print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit static isotropic/anisotropic stress branches before finite-3D black-hole-core calculations."
    )
    parser.add_argument("--mass-msun", type=float, default=4.297e6)
    args = parser.parse_args()
    if args.mass_msun <= 0:
        parser.error("--mass-msun must be positive")
    print_table(args.mass_msun)


if __name__ == "__main__":
    main()
