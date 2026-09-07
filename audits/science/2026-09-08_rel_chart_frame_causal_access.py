#!/usr/bin/env python3
"""
REL-005 — Representation/frame change versus causal-access audit.

Standard-library finite witness for the Track-2 detailed audit.

Checks:
1. A 1+1 Lorentz boost is invertible and preserves the Minkowski interval.
2. Spacelike-separated event coordinate-time order can reverse by frame.
3. Timelike future order is preserved for the tested proper orthochronous boosts.
4. Membership in the causal past J^-(O) is preserved by the boosts.
5. Restricting a global event-record to J^-(O) is non-injective when records
   may differ outside the accessible domain.

The script does not derive relativity from DSD and does not encode a DSD
gravity law.  Causal accessibility here is supplied by standard Minkowski
causal structure.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass


TOL = 1e-12


@dataclass(frozen=True)
class Event:
    t: float
    x: float


def gamma(beta: float) -> float:
    if not (-1.0 < beta < 1.0):
        raise ValueError("beta must satisfy |beta| < 1")
    return 1.0 / math.sqrt(1.0 - beta * beta)


def boost(event: Event, beta: float) -> Event:
    g = gamma(beta)
    return Event(
        t=g * (event.t - beta * event.x),
        x=g * (event.x - beta * event.t),
    )


def boost_det(beta: float) -> float:
    g = gamma(beta)
    return g * g * (1.0 - beta * beta)


def interval_sq(a: Event, b: Event) -> float:
    """Signature (-,+), c=1: ds^2 = dx^2 - dt^2."""
    dt = b.t - a.t
    dx = b.x - a.x
    return dx * dx - dt * dt


def causal_past_contains(point: Event, observer_event: Event) -> bool:
    """point in J^-(observer_event) in 1+1 Minkowski space, c=1."""
    dt = observer_event.t - point.t
    dx = observer_event.x - point.x
    return dt >= -TOL and dt * dt - dx * dx >= -TOL


def representation_audit(beta: float = 0.6) -> dict[str, object]:
    a = Event(0.0, -1.0)
    b = Event(0.0, +1.0)

    ap = boost(a, beta)
    bp = boost(b, beta)
    am = boost(a, -beta)
    bm = boost(b, -beta)

    spacelike_s2 = interval_sq(a, b)
    plus_s2 = interval_sq(ap, bp)
    minus_s2 = interval_sq(am, bm)

    # Simultaneous in the unboosted frame; opposite time order under +/- beta.
    plus_order = "A_before_B" if ap.t < bp.t else "B_before_A"
    minus_order = "A_before_B" if am.t < bm.t else "B_before_A"

    c = Event(0.0, 0.0)
    d = Event(2.0, 0.5)  # timelike future of c
    dp = boost(d, beta)
    dm = boost(d, -beta)

    return {
        "boost_determinant": boost_det(beta),
        "invertible": abs(boost_det(beta)) > TOL,
        "spacelike_interval_original": spacelike_s2,
        "spacelike_interval_plus": plus_s2,
        "spacelike_interval_minus": minus_s2,
        "spacelike_interval_invariant": (
            abs(spacelike_s2 - plus_s2) < TOL
            and abs(spacelike_s2 - minus_s2) < TOL
        ),
        "plus_frame_times": (ap.t, bp.t),
        "minus_frame_times": (am.t, bm.t),
        "plus_frame_order": plus_order,
        "minus_frame_order": minus_order,
        "spacelike_coordinate_order_reverses": plus_order != minus_order,
        "timelike_interval": interval_sq(c, d),
        "timelike_future_order_plus": dp.t > 0.0,
        "timelike_future_order_minus": dm.t > 0.0,
    }


def causal_access_audit(beta: float = 0.6) -> dict[str, object]:
    observer = Event(2.0, 0.0)
    points = {
        "P1": Event(0.0, 0.0),
        "P2": Event(1.0, 0.5),
        "P3": Event(1.0, 2.0),
        "P4": Event(3.0, 0.0),
    }

    base_membership = {
        name: causal_past_contains(point, observer)
        for name, point in points.items()
    }

    observer_boosted = boost(observer, beta)
    boosted_membership = {
        name: causal_past_contains(boost(point, beta), observer_boosted)
        for name, point in points.items()
    }

    # Two global records that agree on J^-(observer) and differ only outside it.
    global_record_1 = {
        "P1": "alpha",
        "P2": "beta",
        "P3": "outside-value-1",
        "P4": "future-value-1",
    }
    global_record_2 = {
        "P1": "alpha",
        "P2": "beta",
        "P3": "outside-value-2",
        "P4": "future-value-2",
    }

    def restrict(record: dict[str, str]) -> dict[str, str]:
        return {
            name: value
            for name, value in record.items()
            if base_membership[name]
        }

    restricted_1 = restrict(global_record_1)
    restricted_2 = restrict(global_record_2)

    return {
        "causal_membership_unboosted": base_membership,
        "causal_membership_boosted": boosted_membership,
        "causal_membership_frame_invariant": base_membership == boosted_membership,
        "global_records_distinct": global_record_1 != global_record_2,
        "restricted_record_1": restricted_1,
        "restricted_record_2": restricted_2,
        "restricted_records_equal": restricted_1 == restricted_2,
        "restriction_noninjective_witness": (
            global_record_1 != global_record_2
            and restricted_1 == restricted_2
        ),
    }


def report() -> int:
    print("REL-005 — FRAME/REPRESENTATION VS CAUSAL-ACCESS AUDIT")
    print("Standard Minkowski specialization; c=1; signature (-,+).\n")

    r = representation_audit()
    print("[1] Representation / Lorentz-frame checks")
    for key, value in r.items():
        print(f"{key}: {value}")
    print()

    c = causal_access_audit()
    print("[2] Causal-access / restriction checks")
    for key, value in c.items():
        print(f"{key}: {value}")
    print()

    assert r["invertible"]
    assert abs(r["boost_determinant"] - 1.0) < TOL
    assert r["spacelike_interval_invariant"]
    assert r["spacelike_coordinate_order_reverses"]
    assert r["timelike_interval"] < 0.0
    assert r["timelike_future_order_plus"]
    assert r["timelike_future_order_minus"]
    assert c["causal_membership_frame_invariant"]
    assert c["global_records_distinct"]
    assert c["restricted_records_equal"]
    assert c["restriction_noninjective_witness"]

    print("SCOPED OUTCOMES")
    print("Lorentz representation change: VALID_IN_DOMAIN")
    print("representation change = causal-access change: NON_IDENTICAL")
    print("coordinate-time order -> causal order: NOT_SUFFICIENT_FOR_EXTENSION")
    print("causal-domain restriction for global reconstruction: RECONSTRUCTION_LOSS")
    print("SUMMARY: PASS_WITH_REFINEMENT")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("all",), default="all")
    parser.parse_args()
    return report()


if __name__ == "__main__":
    raise SystemExit(main())
