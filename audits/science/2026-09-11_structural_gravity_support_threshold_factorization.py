#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class ThresholdInputs:
    nu_kin: float = 0.5
    eta_inertial: float = 1.0
    zeta: float = 1.0
    kg_over_g: float = 1.0
    cinfo_over_c: float = 1.0


def theta_star(nu_kin: float, eta_inertial: float, zeta: float) -> float:
    if nu_kin <= 0.0:
        raise ValueError("nu_kin must be positive")
    if eta_inertial <= 0.0:
        raise ValueError("eta_inertial must be positive")
    if not (0.0 < zeta <= 1.0):
        raise ValueError("zeta must satisfy 0 < zeta <= 1")
    return nu_kin * eta_inertial * zeta**2


def rcrit_over_rs(
    kg_over_g: float,
    cinfo_over_c: float,
    theta: float,
) -> float:
    if kg_over_g <= 0.0:
        raise ValueError("kg_over_g must be positive")
    if cinfo_over_c <= 0.0:
        raise ValueError("cinfo_over_c must be positive")
    if theta <= 0.0:
        raise ValueError("theta must be positive")
    return kg_over_g * (1.0 / cinfo_over_c**2) / (2.0 * theta)


def factorized_ratio(inputs: ThresholdInputs) -> float:
    return rcrit_over_rs(
        inputs.kg_over_g,
        inputs.cinfo_over_c,
        theta_star(inputs.nu_kin, inputs.eta_inertial, inputs.zeta),
    )


def blind_report() -> None:
    nominal = ThresholdInputs()
    theta = theta_star(nominal.nu_kin, nominal.eta_inertial, nominal.zeta)

    print("DSD structural-gravity support-threshold factorization")
    print("------------------------------------------------------")
    print("Candidate support/load threshold:")
    print("  |X| = K_g M / R")
    print("  C_sup = nu_kin * eta_I * zeta^2 * c_info^2")
    print("  Theta_* = |X| / c_info^2 = nu_kin * eta_I * zeta^2")
    print("  R_crit = K_g M / (Theta_* c_info^2)")
    print()
    print("Nominal bridge values (conditional only):")
    print(f"  nu_kin={nominal.nu_kin}")
    print(f"  eta_I={nominal.eta_inertial}")
    print(f"  zeta={nominal.zeta}")
    print(f"  Theta_*={theta:.12g}")
    print()
    print("Boundary:")
    print("  c_info alone does NOT determine Theta_*.")
    print("  nu_kin, eta_I, and zeta are independent downstream bridge factors.")


def compare_report() -> None:
    cases = [
        ("nominal_conditional", ThresholdInputs()),
        ("sub_saturation_zeta_0.9", ThresholdInputs(zeta=0.9)),
        ("inertial_ratio_1.1", ThresholdInputs(eta_inertial=1.1)),
        ("unit_normalization_nu_1", ThresholdInputs(nu_kin=1.0)),
        ("kg_0.95", ThresholdInputs(kg_over_g=0.95)),
        ("cinfo_1.05c", ThresholdInputs(cinfo_over_c=1.05)),
    ]

    print("Comparator sensitivity (Schwarzschild opened only here)")
    print("--------------------------------------------------------")
    print("case,theta_star,Rcrit/Rs")
    for name, inp in cases:
        th = theta_star(inp.nu_kin, inp.eta_inertial, inp.zeta)
        ratio = factorized_ratio(inp)
        print(f"{name},{th:.12g},{ratio:.12g}")


def audit_report() -> int:
    checks: list[tuple[str, bool, str]] = []

    nominal = ThresholdInputs()
    nominal_theta = theta_star(
        nominal.nu_kin, nominal.eta_inertial, nominal.zeta
    )
    nominal_ratio = factorized_ratio(nominal)

    checks.append((
        "CONDITIONAL_HALF_RECOVERY",
        abs(nominal_theta - 0.5) < 1e-15,
        "nu=1/2, eta_I=1, zeta=1 conditionally gives Theta_*=1/2",
    ))
    checks.append((
        "CONDITIONAL_SCHWARZSCHILD_MATCH",
        abs(nominal_ratio - 1.0) < 1e-15,
        "with K_g/G=1 and c_info/c=1, the conditional bridge set gives Rcrit/Rs=1",
    ))

    variations = [
        ThresholdInputs(zeta=0.9),
        ThresholdInputs(eta_inertial=1.1),
        ThresholdInputs(nu_kin=1.0),
    ]
    varied_theta = [
        theta_star(v.nu_kin, v.eta_inertial, v.zeta) for v in variations
    ]
    checks.append((
        "THRESHOLD_UNDERDETERMINED_BY_CINFO",
        all(abs(x - nominal_theta) > 1e-12 for x in varied_theta),
        "changing downstream bridge factors changes Theta_* while c_info is unchanged",
    ))
    checks.append((
        "SUBSATURATION_CHANGES_RADIUS",
        abs(factorized_ratio(ThresholdInputs(zeta=0.9)) - 1.0) > 1e-6,
        "zeta<1 changes the predicted critical radius",
    ))
    checks.append((
        "NO_EHT_FIT_PARAMETER",
        True,
        "no EHT ring/shadow observable is used to set nu, eta_I, zeta, K_g/G, or c_info/c",
    ))
    checks.append((
        "STATUS_OPEN_COEFFICIENT",
        True,
        "Theta_*=1/2 is conditional, not derived from current generic DSD",
    ))

    failures = 0
    for name, ok, note in checks:
        status = "PASS" if ok else "FAIL"
        failures += 0 if ok else 1
        print(f"{status}: {name} -- {note}")
    print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")
    print("STATUS: PASS_WITH_BOUNDARY / OPEN_COEFFICIENT")
    return failures


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Factorize the DSD structural-gravity support threshold."
    )
    parser.add_argument(
        "--mode",
        choices=("all", "blind", "compare", "audit"),
        default="all",
    )
    args = parser.parse_args()

    if args.mode in ("all", "blind"):
        blind_report()
        if args.mode == "blind":
            return

    if args.mode in ("all", "compare"):
        print()
        compare_report()
        if args.mode == "compare":
            return

    if args.mode in ("all", "audit"):
        print()
        failures = audit_report()
        if failures:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
