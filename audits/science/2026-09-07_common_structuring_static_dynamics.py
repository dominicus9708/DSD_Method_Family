#!/usr/bin/env python3
"""
DSD common-describability structuring: static aggregation + dynamics audit.

This script applies the existing DSD typed static-aggregation and structural-
reorganization discipline to a common structuring layer for standard quantum
mechanics and relativity.  It does not encode a quantum-gravity law.

Checks:
1. Separate quantum/relativistic sector aggregates are retained as an ordered
   pair rather than silently scalarized.
2. Distinct underlying supports can have the same combined aggregate.
3. Block-diagonal dynamics provide an admissible no-cross-coupling control.
4. Cross-sector influence appears only when explicit constitutive coupling
   coefficients are supplied.
5. A formation-identity change is flagged as requiring explicit lineage.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class TypedDatum:
    name: str
    sector: str
    value: float


@dataclass(frozen=True)
class CommonAggregate:
    quantum: float
    relativity: float


def finite_sector_aggregate(data: Iterable[TypedDatum], sector: str) -> float:
    total = 0.0
    for item in data:
        if item.sector != sector:
            raise TypeError(
                f"datum {item.name!r} has sector {item.sector!r}, expected {sector!r}"
            )
        total += item.value
    return total


def common_product_aggregate(
    quantum_data: Iterable[TypedDatum],
    relativity_data: Iterable[TypedDatum],
) -> CommonAggregate:
    return CommonAggregate(
        quantum=finite_sector_aggregate(quantum_data, "quantum"),
        relativity=finite_sector_aggregate(relativity_data, "relativity"),
    )


def aggregation_audit() -> dict[str, object]:
    # Two distinct quantum supports give the same quantum aggregate 0.
    q_pm = [
        TypedDatum("q_plus", "quantum", +1.0),
        TypedDatum("q_minus", "quantum", -1.0),
    ]
    q_zero = [TypedDatum("q_zero", "quantum", 0.0)]

    # Relativity-side data are held fixed.
    r_fixed = [TypedDatum("r_fixed", "relativity", 2.0)]

    agg_pm = common_product_aggregate(q_pm, r_fixed)
    agg_zero = common_product_aggregate(q_zero, r_fixed)

    return {
        "aggregate_pm": agg_pm,
        "aggregate_zero": agg_zero,
        "same_combined_aggregate": agg_pm == agg_zero,
        "different_quantum_support": tuple(x.name for x in q_pm)
        != tuple(x.name for x in q_zero),
        "product_output_preserves_sector_labels": isinstance(agg_pm, CommonAggregate),
    }


def euler_step_block_diagonal(
    q: float,
    r: float,
    a_q: float,
    a_r: float,
    dt: float,
) -> tuple[float, float]:
    return q + dt * a_q * q, r + dt * a_r * r


def euler_step_coupled(
    q: float,
    r: float,
    a_q: float,
    a_r: float,
    k_qr: float,
    k_rq: float,
    dt: float,
) -> tuple[float, float]:
    dq = a_q * q + k_qr * r
    dr = k_rq * q + a_r * r
    return q + dt * dq, r + dt * dr


def dynamics_audit() -> dict[str, object]:
    q0, r0 = 1.0, 3.0
    dt = 0.1

    block = euler_step_block_diagonal(q0, r0, a_q=2.0, a_r=-1.0, dt=dt)
    coupled_zero = euler_step_coupled(
        q0, r0, a_q=2.0, a_r=-1.0, k_qr=0.0, k_rq=0.0, dt=dt
    )
    coupled_nonzero = euler_step_coupled(
        q0, r0, a_q=2.0, a_r=-1.0, k_qr=0.5, k_rq=-0.25, dt=dt
    )

    return {
        "block_diagonal_step": block,
        "zero_coupling_matches_block": coupled_zero == block,
        "nonzero_explicit_coupling_changes_step": coupled_nonzero != block,
        "coupled_step": coupled_nonzero,
    }


def lineage_required(
    formation_before: tuple[str, ...], formation_after: tuple[str, ...]
) -> bool:
    return formation_before != formation_after


def lineage_audit() -> dict[str, bool]:
    fixed = ("channel:q", "channel:r")
    changed = ("channel:q-prime", "channel:r")
    return {
        "fixed_background_requires_transition_lineage": lineage_required(fixed, fixed),
        "changed_formation_requires_transition_lineage": lineage_required(fixed, changed),
    }


def type_firewall_audit() -> dict[str, bool]:
    q = [TypedDatum("q", "quantum", 1.0)]
    r = [TypedDatum("r", "relativity", 1.0)]
    rejected = False
    try:
        finite_sector_aggregate(q + r, "quantum")
    except TypeError:
        rejected = True
    return {"mixed_sector_blind_sum_rejected": rejected}


def report() -> int:
    print("DSD COMMON STRUCTURING STATIC + DYNAMICS AUDIT")
    print("No quantum-gravity or unification premise is encoded.\n")

    a = aggregation_audit()
    print("[1] Typed product aggregation")
    for k, v in a.items():
        print(f"{k}: {v}")
    print()

    t = type_firewall_audit()
    print("[2] Type firewall")
    for k, v in t.items():
        print(f"{k}: {v}")
    print()

    d = dynamics_audit()
    print("[3] Block-diagonal vs explicit coupling dynamics")
    for k, v in d.items():
        print(f"{k}: {v}")
    print()

    l = lineage_audit()
    print("[4] Formation-transition lineage")
    for k, v in l.items():
        print(f"{k}: {v}")
    print()

    assert a["same_combined_aggregate"]
    assert a["different_quantum_support"]
    assert a["product_output_preserves_sector_labels"]
    assert t["mixed_sector_blind_sum_rejected"]
    assert d["zero_coupling_matches_block"]
    assert d["nonzero_explicit_coupling_changes_step"]
    assert not l["fixed_background_requires_transition_lineage"]
    assert l["changed_formation_requires_transition_lineage"]

    print("AUDIT RESULT: PASS_WITH_BOUNDARY")
    print("- common structuring permits typed product aggregation")
    print("- common aggregation does not guarantee reconstruction")
    print("- shared structuring does not force cross-sector dynamics")
    print("- cross-sector dynamics require explicit constitutive data")
    print("- formation-level change requires explicit lineage")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("all",), default="all")
    parser.parse_args()
    return report()


if __name__ == "__main__":
    raise SystemExit(main())
