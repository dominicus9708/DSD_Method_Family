#!/usr/bin/env python3
"""
DSD describability-regime partition and aggregate-dynamics audit.

This script is a finite structural witness for the common DSD structuring of
standard quantum-mechanics and relativity describability regimes. It does NOT
encode a quantum-gravity law and does NOT identify quantum and relativistic
physical quantities.

The finite universe is partitioned at each time into:

    Q_ONLY   = Q_t minus R_t
    OVERLAP  = Q_t intersect R_t
    R_ONLY   = R_t minus Q_t
    NEITHER  = outside Q_t union R_t within the supplied universe

For a supplied common bookkeeping weight w_t(x), each sector has a static
aggregate. Across a discrete time step the exact balance identity is

    delta A_b
      = incoming old-weight flux
      - outgoing old-weight flux
      + within/final-sector intrinsic term.

The script also checks two non-implications:
1. unchanged static aggregates do not imply absence of membership dynamics;
2. a coarse time step can hide an intermediate OVERLAP transition.

The bookkeeping weights are generic finite structural weights only. Sector-
specific physical aggregates require their own typed carriers and explicit
transport/comparison maps before cross-sector subtraction is allowed.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Dict, Mapping, Tuple

SECTORS = ("Q_ONLY", "OVERLAP", "R_ONLY", "NEITHER")
TOL = 1e-12


@dataclass(frozen=True)
class ElementState:
    q_describable: bool
    r_describable: bool
    weight: float


def sector_of(state: ElementState) -> str:
    q = state.q_describable
    r = state.r_describable
    if q and r:
        return "OVERLAP"
    if q:
        return "Q_ONLY"
    if r:
        return "R_ONLY"
    return "NEITHER"


def aggregate_by_sector(state: Mapping[str, ElementState]) -> Dict[str, float]:
    out = {sector: 0.0 for sector in SECTORS}
    for elem in state.values():
        out[sector_of(elem)] += elem.weight
    return out


def count_by_sector(state: Mapping[str, ElementState]) -> Dict[str, int]:
    out = {sector: 0 for sector in SECTORS}
    for elem in state.values():
        out[sector_of(elem)] += 1
    return out


def transition_flux(
    old: Mapping[str, ElementState],
    new: Mapping[str, ElementState],
) -> Tuple[Dict[Tuple[str, str], float], Dict[str, float]]:
    """
    Old-weight membership flux F[a,b] and intrinsic final-sector term G[b].

    F[a,b] = sum old weights of elements moving a -> b.
    G[b]   = sum over elements ending in b of (w_new - w_old).
    """
    if old.keys() != new.keys():
        raise ValueError("old and new states must use the same finite universe")

    flux = {(a, b): 0.0 for a in SECTORS for b in SECTORS}
    intrinsic = {b: 0.0 for b in SECTORS}

    for key in old:
        s0 = sector_of(old[key])
        s1 = sector_of(new[key])
        flux[(s0, s1)] += old[key].weight
        intrinsic[s1] += new[key].weight - old[key].weight

    return flux, intrinsic


def balance_residuals(
    old: Mapping[str, ElementState],
    new: Mapping[str, ElementState],
) -> Dict[str, float]:
    a0 = aggregate_by_sector(old)
    a1 = aggregate_by_sector(new)
    flux, intrinsic = transition_flux(old, new)

    residuals: Dict[str, float] = {}
    for b in SECTORS:
        incoming = sum(flux[(a, b)] for a in SECTORS if a != b)
        outgoing = sum(flux[(b, c)] for c in SECTORS if c != b)
        rhs = incoming - outgoing + intrinsic[b]
        lhs = a1[b] - a0[b]
        residuals[b] = lhs - rhs
    return residuals


def fine_witness() -> Dict[str, Dict[str, ElementState]]:
    return {
        "t0": {
            "a": ElementState(True, False, 1.0),
            "b": ElementState(True, False, 2.0),
            "c": ElementState(True, True, 3.0),
            "d": ElementState(True, True, 4.0),
            "e": ElementState(False, True, 5.0),
            "f": ElementState(False, False, 6.0),
        },
        "t1": {
            "a": ElementState(True, True, 1.5),
            "b": ElementState(True, False, 2.5),
            "c": ElementState(False, True, 2.5),
            "d": ElementState(True, True, 4.0),
            "e": ElementState(True, True, 4.5),
            "f": ElementState(True, False, 6.5),
        },
        "t2": {
            "a": ElementState(False, True, 1.2),
            "b": ElementState(True, True, 2.7),
            "c": ElementState(False, True, 2.8),
            "d": ElementState(True, False, 3.8),
            "e": ElementState(True, True, 4.8),
            "f": ElementState(True, True, 6.2),
        },
    }


def hidden_flow_witness() -> Tuple[Dict[str, ElementState], Dict[str, ElementState]]:
    # Equal weights keep sector aggregates unchanged although the elements swap.
    old = {
        "x": ElementState(True, False, 1.0),
        "y": ElementState(True, True, 1.0),
    }
    new = {
        "x": ElementState(True, True, 1.0),
        "y": ElementState(True, False, 1.0),
    }
    return old, new


def print_flux(flux: Mapping[Tuple[str, str], float]) -> None:
    print("old-weight membership flux:")
    header = "from\\to".ljust(11) + "".join(f"{s:>11}" for s in SECTORS)
    print(header)
    for a in SECTORS:
        row = a.ljust(11)
        for b in SECTORS:
            row += f"{flux[(a, b)]:11.3f}"
        print(row)


def audit_fine_dynamics() -> None:
    witness = fine_witness()

    print("[1] Static partition aggregates")
    for t in ("t0", "t1", "t2"):
        print(f"{t} counts     : {count_by_sector(witness[t])}")
        print(f"{t} aggregates : {aggregate_by_sector(witness[t])}")
    print()

    for t_old, t_new in (("t0", "t1"), ("t1", "t2")):
        print(f"[2] Exact aggregate balance {t_old} -> {t_new}")
        flux, intrinsic = transition_flux(witness[t_old], witness[t_new])
        print_flux(flux)
        print(f"intrinsic final-sector terms: {intrinsic}")
        residuals = balance_residuals(witness[t_old], witness[t_new])
        print(f"balance residuals: {residuals}")
        assert all(abs(v) <= TOL for v in residuals.values())
        print()


def audit_hidden_flow() -> None:
    print("[3] Static-aggregate invisibility of membership motion")
    old, new = hidden_flow_witness()
    a0 = aggregate_by_sector(old)
    a1 = aggregate_by_sector(new)
    flux, intrinsic = transition_flux(old, new)

    print(f"old aggregates: {a0}")
    print(f"new aggregates: {a1}")
    print_flux(flux)

    assert a0 == a1
    assert abs(flux[("Q_ONLY", "OVERLAP")] - 1.0) <= TOL
    assert abs(flux[("OVERLAP", "Q_ONLY")] - 1.0) <= TOL
    assert all(abs(v) <= TOL for v in intrinsic.values())
    print("result: aggregate time series unchanged, but sector membership moved")
    print()


def audit_time_resolution() -> None:
    print("[4] Time-resolution audit")
    witness = fine_witness()
    s0 = sector_of(witness["t0"]["a"])
    s1 = sector_of(witness["t1"]["a"])
    s2 = sector_of(witness["t2"]["a"])

    print(f"fine path for element a  : {s0} -> {s1} -> {s2}")
    print(f"coarse t0-to-t2 readout  : {s0} -> {s2}")

    assert (s0, s1, s2) == ("Q_ONLY", "OVERLAP", "R_ONLY")
    assert (s0, s2) == ("Q_ONLY", "R_ONLY")
    print("result: coarse sampling hides an intermediate overlap state")
    print()


def report() -> int:
    print("DSD DESCRIBABILITY-REGIME PARTITION / AGGREGATE DYNAMICS AUDIT")
    print("No quantum-gravity law or cross-theory physical scalarization is assumed.\n")

    audit_fine_dynamics()
    audit_hidden_flow()
    audit_time_resolution()

    print("AUDIT RESULT: PASS_WITH_BOUNDARY")
    print("- sector partition and sectorwise static aggregates are well-defined in the finite witness")
    print("- aggregate change decomposes exactly into membership-flow plus intrinsic update")
    print("- unchanged static aggregate does not imply unchanged describability membership")
    print("- coarse time resolution can hide intermediate overlap passage")
    print("- physical cross-sector subtraction still requires a common typed carrier or explicit maps")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("all",), default="all")
    parser.parse_args()
    return report()


if __name__ == "__main__":
    raise SystemExit(main())
