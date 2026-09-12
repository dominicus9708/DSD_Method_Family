#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

G = 6.67430e-11
C = 299_792_458.0
M_SUN = 1.98847e30

UNDEFINED = "undefined"
DEFINED_ZERO = "defined_zero"
DEFINED_NONZERO = "defined_nonzero"


@dataclass(frozen=True)
class ComparatorState:
    label: str
    mass_msun: float
    j_status: str
    chi: float | None
    q_status: str
    qhat: float | None


def _validate_status_value(status: str, value: float | None, name: str) -> None:
    if status not in {UNDEFINED, DEFINED_ZERO, DEFINED_NONZERO}:
        raise ValueError(f"{name} status is invalid: {status}")
    if status == UNDEFINED:
        if value is not None:
            raise ValueError(f"{name} undefined status requires value=None")
        return
    if value is None:
        raise ValueError(f"{name} defined status requires a numerical value")
    if status == DEFINED_ZERO and not math.isclose(value, 0.0, abs_tol=1e-15):
        raise ValueError(f"{name} defined_zero requires value=0")
    if status == DEFINED_NONZERO and math.isclose(value, 0.0, abs_tol=1e-15):
        raise ValueError(f"{name} defined_nonzero requires a nonzero value")


def validate_state(state: ComparatorState) -> None:
    if state.mass_msun <= 0:
        raise ValueError("mass must be positive")
    _validate_status_value(state.j_status, state.chi, "J/chi")
    _validate_status_value(state.q_status, state.qhat, "Q/qhat")
    if state.chi is not None and abs(state.chi) > 1.0 + 1e-14:
        raise ValueError("|chi| must not exceed 1 inside the standard comparator domain")
    if state.chi is not None and state.qhat is not None:
        if state.chi**2 + state.qhat**2 > 1.0 + 1e-14:
            raise ValueError("superextremal comparator parameters")


def select_comparator_family(state: ComparatorState) -> str:
    validate_state(state)
    if state.j_status == UNDEFINED or state.q_status == UNDEFINED:
        return "UNRESOLVED"
    j_nonzero = state.j_status == DEFINED_NONZERO
    q_nonzero = state.q_status == DEFINED_NONZERO
    if not j_nonzero and not q_nonzero:
        return "SCHWARZSCHILD"
    if j_nonzero and not q_nonzero:
        return "KERR"
    if not j_nonzero and q_nonzero:
        return "REISSNER_NORDSTROM"
    return "KERR_NEWMAN"


def bad_zero_filled_family(state: ComparatorState) -> str:
    """Deliberately inadmissible control: silently treats undefined as numerical zero."""
    chi = 0.0 if state.chi is None else state.chi
    qhat = 0.0 if state.qhat is None else state.qhat
    j_nonzero = not math.isclose(chi, 0.0, abs_tol=1e-15)
    q_nonzero = not math.isclose(qhat, 0.0, abs_tol=1e-15)
    if not j_nonzero and not q_nonzero:
        return "SCHWARZSCHILD"
    if j_nonzero and not q_nonzero:
        return "KERR"
    if not j_nonzero and q_nonzero:
        return "REISSNER_NORDSTROM"
    return "KERR_NEWMAN"


def gravitational_radius_km(mass_msun: float) -> float:
    return G * mass_msun * M_SUN / C**2 / 1000.0


def horizon_radius_km(state: ComparatorState) -> float:
    family = select_comparator_family(state)
    if family == "UNRESOLVED":
        raise ValueError("horizon comparator is unresolved while J or Q status is undefined")
    assert state.chi is not None
    assert state.qhat is not None
    disc = 1.0 - state.chi**2 - state.qhat**2
    if disc < -1e-14:
        raise ValueError("no standard outer horizon in the superextremal parameter domain")
    return gravitational_radius_km(state.mass_msun) * (1.0 + math.sqrt(max(0.0, disc)))


def radius_descriptor(state: ComparatorState) -> tuple[float]:
    return (horizon_radius_km(state),)


def radius_chi_descriptor(state: ComparatorState) -> tuple[float, float]:
    assert state.chi is not None
    return (horizon_radius_km(state), state.chi)


def signed_parameter_descriptor(state: ComparatorState) -> tuple[float, float, float, str, str]:
    assert state.chi is not None
    assert state.qhat is not None
    return (
        horizon_radius_km(state),
        state.chi,
        state.qhat,
        state.j_status,
        state.q_status,
    )


def floor_quantize(value: float, bin_width: float) -> float:
    if bin_width <= 0:
        raise ValueError("bin width must be positive")
    return math.floor(value / bin_width) * bin_width


def make_states(mass_msun: float) -> dict[str, ComparatorState]:
    return {
        "schwarzschild": ComparatorState(
            "schwarzschild", mass_msun, DEFINED_ZERO, 0.0, DEFINED_ZERO, 0.0
        ),
        "kerr": ComparatorState(
            "kerr", mass_msun, DEFINED_NONZERO, 0.9, DEFINED_ZERO, 0.0
        ),
        "rn": ComparatorState(
            "rn", mass_msun, DEFINED_ZERO, 0.0, DEFINED_NONZERO, 0.3
        ),
        "kn_plus": ComparatorState(
            "kn_plus", mass_msun, DEFINED_NONZERO, 0.9, DEFINED_NONZERO, 0.3
        ),
        "kn_minus": ComparatorState(
            "kn_minus", mass_msun, DEFINED_NONZERO, 0.9, DEFINED_NONZERO, -0.3
        ),
        "trade_a": ComparatorState(
            "trade_a", mass_msun, DEFINED_NONZERO, 0.6, DEFINED_NONZERO, 0.4
        ),
        "trade_b": ComparatorState(
            "trade_b", mass_msun, DEFINED_NONZERO, 0.4, DEFINED_NONZERO, 0.6
        ),
        "q_undefined": ComparatorState(
            "q_undefined", mass_msun, DEFINED_NONZERO, 0.9, UNDEFINED, None
        ),
        "q_neutral": ComparatorState(
            "q_neutral", mass_msun, DEFINED_NONZERO, 0.9, DEFINED_ZERO, 0.0
        ),
        "resolution_a": ComparatorState(
            "resolution_a", mass_msun, DEFINED_NONZERO, 0.9, DEFINED_NONZERO, 0.30
        ),
        "resolution_b": ComparatorState(
            "resolution_b", mass_msun, DEFINED_NONZERO, 0.9, DEFINED_NONZERO, 0.31
        ),
    }


def audit(mass_msun: float) -> list[tuple[str, bool, str]]:
    s = make_states(mass_msun)
    checks: list[tuple[str, bool, str]] = []

    r_plus = horizon_radius_km(s["kn_plus"])
    r_minus = horizon_radius_km(s["kn_minus"])
    checks.append((
        "RADIUS_READOUT_COLLAPSES_CHARGE_SIGN",
        s["kn_plus"] != s["kn_minus"] and math.isclose(r_plus, r_minus, rel_tol=1e-14),
        "distinct signed global charges can share the same Kerr-Newman horizon-radius readout",
    ))

    r_trade_a = horizon_radius_km(s["trade_a"])
    r_trade_b = horizon_radius_km(s["trade_b"])
    checks.append((
        "RADIUS_READOUT_COLLAPSES_DIFFERENT_JQ_MAGNITUDES",
        s["trade_a"].chi != s["trade_b"].chi
        and s["trade_a"].qhat != s["trade_b"].qhat
        and math.isclose(r_trade_a, r_trade_b, rel_tol=1e-14),
        "fixed mass with equal chi^2+qhat^2 can hide different J/Q allocations",
    ))

    checks.append((
        "ADDING_CHI_RECOVERS_TRADEOFF_PAIR",
        radius_descriptor(s["trade_a"]) == radius_descriptor(s["trade_b"])
        and radius_chi_descriptor(s["trade_a"]) != radius_chi_descriptor(s["trade_b"]),
        "adding an independent spin descriptor refines the collapsed radius equivalence class",
    ))

    checks.append((
        "ADDING_SIGNED_Q_RECOVERS_CHARGE_SIGN",
        radius_chi_descriptor(s["kn_plus"]) == radius_chi_descriptor(s["kn_minus"])
        and signed_parameter_descriptor(s["kn_plus"]) != signed_parameter_descriptor(s["kn_minus"]),
        "adding signed charge information refines the remaining sign-collapsed class",
    ))

    checks.append((
        "UNDEFINED_Q_IS_NOT_NEUTRAL",
        select_comparator_family(s["q_undefined"]) == "UNRESOLVED"
        and select_comparator_family(s["q_neutral"]) == "KERR",
        "undefined charge status and defined-zero charge lead to different admissible comparator states",
    ))

    checks.append((
        "ZERO_FILL_CREATES_INADMISSIBLE_DESCRIBABILITY_COLLAPSE",
        bad_zero_filled_family(s["q_undefined"]) == bad_zero_filled_family(s["q_neutral"]) == "KERR",
        "silent zero filling collapses an unresolved charge state onto a neutral Kerr state",
    ))

    expected = {
        "schwarzschild": "SCHWARZSCHILD",
        "kerr": "KERR",
        "rn": "REISSNER_NORDSTROM",
        "kn_plus": "KERR_NEWMAN",
    }
    checks.append((
        "DEFINED_STATUS_SELECTS_FOUR_STANDARD_COMPARATOR_FAMILIES",
        all(select_comparator_family(s[name]) == family for name, family in expected.items()),
        "defined zero/nonzero J and Q status selects the standard external comparator family without zero-padding",
    ))

    unresolved_raises = False
    try:
        horizon_radius_km(s["q_undefined"])
    except ValueError:
        unresolved_raises = True
    checks.append((
        "UNRESOLVED_STATUS_BLOCKS_RADIUS_COMPARATOR",
        unresolved_raises,
        "a numerical horizon readout is not produced while required global charge status is undefined",
    ))

    ra = horizon_radius_km(s["resolution_a"])
    rb = horizon_radius_km(s["resolution_b"])
    coarse = 200_000.0
    fine = 10_000.0
    checks.append((
        "COARSE_RESOLUTION_CAN_INDUCE_DESCRIBABILITY_COLLAPSE",
        not math.isclose(ra, rb, rel_tol=1e-14)
        and floor_quantize(ra, coarse) == floor_quantize(rb, coarse),
        "two distinct horizon radii can become indistinguishable after a deliberately coarse readout",
    ))

    checks.append((
        "FINER_RESOLUTION_CAN_PARTIALLY_RECOVER_DISTINCTION",
        floor_quantize(ra, coarse) == floor_quantize(rb, coarse)
        and floor_quantize(ra, fine) != floor_quantize(rb, fine),
        "refining the readout resolution can split a previously collapsed descriptive class",
    ))

    return checks


def print_report(mass_msun: float) -> None:
    s = make_states(mass_msun)
    print("DSD black-hole comparator + describability-collapse audit -- BH-RB-006")
    print("---------------------------------------------------------------------")
    print(f"mass_msun={mass_msun:.12g}")
    print(f"r_g_km={gravitational_radius_km(mass_msun):.12g}")
    print()

    for name in ("schwarzschild", "kerr", "rn", "kn_plus", "kn_minus", "trade_a", "trade_b"):
        state = s[name]
        print(
            f"{name}: family={select_comparator_family(state)}, "
            f"chi={state.chi}, qhat={state.qhat}, "
            f"r_plus_km={horizon_radius_km(state):.12g}"
        )

    print()
    print("Status-collapse control")
    print(f"q_undefined status-aware family={select_comparator_family(s['q_undefined'])}")
    print(f"q_neutral status-aware family={select_comparator_family(s['q_neutral'])}")
    print(f"q_undefined bad zero-filled family={bad_zero_filled_family(s['q_undefined'])}")
    print(f"q_neutral bad zero-filled family={bad_zero_filled_family(s['q_neutral'])}")

    ra = horizon_radius_km(s["resolution_a"])
    rb = horizon_radius_km(s["resolution_b"])
    print()
    print("Resolution-control witness")
    print(f"resolution_a_r_plus_km={ra:.12g}")
    print(f"resolution_b_r_plus_km={rb:.12g}")
    print(f"coarse_200000km_a={floor_quantize(ra, 200_000.0):.12g}")
    print(f"coarse_200000km_b={floor_quantize(rb, 200_000.0):.12g}")
    print(f"fine_10000km_a={floor_quantize(ra, 10_000.0):.12g}")
    print(f"fine_10000km_b={floor_quantize(rb, 10_000.0):.12g}")

    print()
    checks = audit(mass_msun)
    failures = 0
    print("Audit")
    for name, ok, note in checks:
        failures += 0 if ok else 1
        print(f"{'PASS' if ok else 'FAIL'}: {name} -- {note}")
    print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")

    print()
    print("Boundary")
    print("Describability collapse here means non-injectivity or coarse-graining of a chosen descriptor.")
    print("It does not establish physical destruction, conversion, or quantum-information loss.")
    print("Recovery means refinement of the selected descriptive equivalence classes, not full microstate reconstruction.")
    print("Kerr/Newman/Schwarzschild/Reissner-Nordstrom remain external standard comparators.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit status-aware black-hole comparator selection and DSD describability collapse/recovery."
    )
    parser.add_argument("--mass-msun", type=float, default=4.297e6)
    args = parser.parse_args()
    if args.mass_msun <= 0:
        parser.error("--mass-msun must be positive")
    print_report(args.mass_msun)


if __name__ == "__main__":
    main()
