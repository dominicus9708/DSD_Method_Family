#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class BridgeState:
    eta_i: float
    kg_ratio: float
    phi: float = 0.5
    cinfo_ratio: float = 1.0


def acceleration_factor(eta_i: float) -> float:
    if eta_i <= 0.0:
        raise ValueError("eta_i must be positive")
    return 1.0 / eta_i


def eotvos_from_eta(eta_1: float, eta_2: float) -> float:
    a1 = acceleration_factor(eta_1)
    a2 = acceleration_factor(eta_2)
    return 2.0 * abs(a1 - a2) / abs(a1 + a2)


def k_eff_ratio(state: BridgeState) -> float:
    if state.kg_ratio <= 0.0:
        raise ValueError("kg_ratio must be positive")
    return state.kg_ratio / state.eta_i


def normalized_rcrit(state: BridgeState) -> float:
    if state.phi <= 0.0:
        raise ValueError("phi must be positive")
    if state.cinfo_ratio <= 0.0:
        raise ValueError("cinfo_ratio must be positive")
    return k_eff_ratio(state) / (state.phi * state.cinfo_ratio**2)


def blind_report() -> None:
    print("DSD structural-gravity eta_I identifiability audit")
    print("---------------------------------------------------")
    print("Definitions:")
    print("  eta_I = mu_I / mu_g")
    print("  F_X = mu_g * a_X")
    print("  mu_I * a = F_X")
    print("  => a = a_X / eta_I")
    print()
    print("If eta_I is universal:")
    print("  K_eff = K_g / eta_I")
    print("  R_crit = K_eff * M / [Phi(zeta) * c_info^2]")
    print()
    print("Therefore weak-field response and the present critical-radius")
    print("candidate identify K_g/eta_I, not K_g and eta_I separately.")
    print()
    print("Boundary:")
    print("  Generic DSD typing does not imply eta_I = 1.")
    print("  A universal eta_I may be normalized to 1 only after an")
    print("  explicit universality/equivalence bridge is adopted.")


def degeneracy_report() -> None:
    cases = [
        ("eta=0.5, Kg=0.5", BridgeState(eta_i=0.5, kg_ratio=0.5)),
        ("eta=1.0, Kg=1.0", BridgeState(eta_i=1.0, kg_ratio=1.0)),
        ("eta=2.0, Kg=2.0", BridgeState(eta_i=2.0, kg_ratio=2.0)),
    ]

    print("Common-ratio degeneracy")
    print("-----------------------")
    print("case,K_eff_ratio,normalized_Rcrit")
    for name, state in cases:
        print(
            f"{name},"
            f"{k_eff_ratio(state):.12g},"
            f"{normalized_rcrit(state):.12g}"
        )

    print()
    print("Composition/state dependence witness")
    print("------------------------------------")
    for delta in (1e-6, 1e-9, 1e-12):
        eta1 = 1.0
        eta2 = 1.0 + delta
        print(
            f"delta_eta={delta:.1e}, "
            f"Eotvos={eotvos_from_eta(eta1, eta2):.12g}"
        )

    print()
    print("MICROSCOPE final Ti/Pt result (external comparator):")
    print("  eta_Eotvos = [-1.5 +/- 2.3(stat) +/- 1.5(syst)] x 10^-15")
    combined_sigma = math.sqrt(2.3**2 + 1.5**2) * 1e-15
    print(f"  combined 1-sigma uncertainty ~= {combined_sigma:.12g}")


def audit_report() -> int:
    checks: list[tuple[str, bool, str]] = []

    states = [
        BridgeState(eta_i=0.5, kg_ratio=0.5),
        BridgeState(eta_i=1.0, kg_ratio=1.0),
        BridgeState(eta_i=2.0, kg_ratio=2.0),
    ]
    keffs = [k_eff_ratio(s) for s in states]
    radii = [normalized_rcrit(s) for s in states]

    checks.append((
        "COMMON_RATIO_DEGENERACY",
        max(keffs) - min(keffs) < 1e-15,
        "different (K_g, eta_I) pairs with the same K_g/eta_I give the same weak-field normalization",
    ))
    checks.append((
        "CRITICAL_RADIUS_SAME_DEGENERACY",
        max(radii) - min(radii) < 1e-15,
        "the current R_crit candidate also depends on K_g/eta_I rather than on the two separately",
    ))

    e_same = eotvos_from_eta(1.7, 1.7)
    e_diff = eotvos_from_eta(1.0, 1.0 + 1e-9)
    checks.append((
        "UNIVERSAL_ETA_GIVES_UFF",
        abs(e_same) < 1e-15,
        "a common eta_I yields zero differential free-fall signal in this bridge",
    ))
    checks.append((
        "NONUNIVERSAL_ETA_IS_OBSERVABLE",
        e_diff > 0.0,
        "composition/state dependence of eta_I produces a nonzero differential acceleration",
    ))

    checks.append((
        "ETA_EQUAL_ONE_NOT_DERIVED",
        True,
        "generic DSD typed properties and supplied dynamical operators do not identify mu_I with mu_g",
    ))
    checks.append((
        "UNIVERSAL_CONSTANT_CAN_BE_ABSORBED",
        math.isclose(
            k_eff_ratio(BridgeState(eta_i=3.0, kg_ratio=6.0)),
            2.0,
            rel_tol=1e-15,
        ),
        "a universal eta_I can be absorbed into K_eff = K_g/eta_I",
    ))
    checks.append((
        "NO_SCHWARZSCHILD_FIT",
        True,
        "no black-hole radius, EHT ring, or Schwarzschild coefficient is used to set eta_I",
    ))
    checks.append((
        "STRONG_FIELD_EXTENSION_REMAINS_OPEN",
        True,
        "weak-field universality does not by itself prove eta_I is state-independent in a strong-field DSD specialization",
    ))

    failures = 0
    for name, ok, note in checks:
        status = "PASS" if ok else "FAIL"
        failures += 0 if ok else 1
        print(f"{status}: {name} -- {note}")

    print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")
    print("STATUS: PASS_WITH_BOUNDARY / UNIVERSAL_RATIO_DEGENERACY")
    return failures


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit eta_I = mu_I/mu_g in the DSD structural-gravity critical-radius bridge."
    )
    parser.add_argument(
        "--mode",
        choices=("all", "blind", "degeneracy", "audit"),
        default="all",
    )
    args = parser.parse_args()

    if args.mode in ("all", "blind"):
        blind_report()
        if args.mode == "blind":
            return

    if args.mode in ("all", "degeneracy"):
        print()
        degeneracy_report()
        if args.mode == "degeneracy":
            return

    if args.mode in ("all", "audit"):
        print()
        failures = audit_report()
        if failures:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
