#!/usr/bin/env python3
"""
PHY-REL-006 — Cauchy data / domain-of-dependence / reconstruction audit.

Standard-library finite witness for Track-2 detailed relativity analysis.

The script uses the 1+1 dimensional wave equation with c=1,

    u_tt - u_xx = 0,

and the d'Alembert solution formula for initial data

    f(x) = u(0,x),
    g(x) = u_t(0,x).

Checks:
1. Complete Cauchy data require both field value and initial velocity in this model.
2. Data supported outside an initial interval do not affect points in its domain of dependence.
3. Two globally distinct initial data sets can agree on an interval and generate identical
   solutions throughout the corresponding finite sampled causal diamond.
4. Those same data sets can generate different values outside that domain, so domain-limited
   completeness does not imply global reconstruction.
5. One-slice data alone do not select a unique continuation unless an evolution relation is
   supplied; a same-initial-data non-wave continuation provides a structural control.

This does not derive general relativity from DSD and does not identify the wave speed with
DSD c_info. The wave equation is a standard hyperbolic comparator supplied externally.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Callable


TOL = 1e-12


@dataclass(frozen=True)
class CauchyData:
    f: Callable[[float], float]
    g_integral: Callable[[float, float], float]


def zero_field(x: float) -> float:
    return 0.0


def zero_integral(a: float, b: float) -> float:
    return 0.0


def triangle_bump(x: float, center: float = 4.0, halfwidth: float = 1.0) -> float:
    """Compact triangular bump with support [center-halfwidth, center+halfwidth]."""
    d = abs(x - center)
    return max(0.0, 1.0 - d / halfwidth)


def box_integral(a: float, b: float, left: float = -1.0, right: float = 1.0) -> float:
    """Integral of the indicator of [left,right] over [a,b]."""
    lo = max(a, left)
    hi = min(b, right)
    return max(0.0, hi - lo)


def dalembert(data: CauchyData, t: float, x: float) -> float:
    if t < -TOL:
        raise ValueError("This finite audit uses t >= 0")
    return 0.5 * (data.f(x - t) + data.f(x + t)) + 0.5 * data.g_integral(x - t, x + t)


def in_future_domain_of_interval(t: float, x: float, left: float, right: float) -> bool:
    """For the unit-speed 1+1 wave equation: [x-t,x+t] subset of [left,right]."""
    return t >= -TOL and x - t >= left - TOL and x + t <= right + TOL


def cauchy_component_audit() -> dict[str, object]:
    base = CauchyData(zero_field, zero_integral)
    same_f_different_g = CauchyData(
        zero_field,
        lambda a, b: box_integral(a, b, -1.0, 1.0),
    )

    target = (0.5, 0.0)
    u_base = dalembert(base, *target)
    u_velocity = dalembert(same_f_different_g, *target)

    return {
        "target": target,
        "same_initial_field_f": True,
        "different_initial_velocity_g": True,
        "u_with_zero_velocity": u_base,
        "u_with_nonzero_velocity": u_velocity,
        "field_value_alone_insufficient": abs(u_base - u_velocity) > TOL,
    }


def domain_of_dependence_audit() -> dict[str, object]:
    initial_interval = (-2.0, 2.0)

    data_a = CauchyData(zero_field, zero_integral)
    data_b = CauchyData(
        lambda x: triangle_bump(x, center=4.0, halfwidth=1.0),
        zero_integral,
    )

    # Every sampled point lies in D^+([-2,2]); the bump is entirely outside the initial interval.
    diamond_points = [
        (0.0, 0.0),
        (0.5, 0.0),
        (1.0, 0.0),
        (1.0, 0.5),
        (1.5, 0.0),
        (0.5, 1.0),
    ]

    diamond_membership = [
        in_future_domain_of_interval(t, x, *initial_interval)
        for t, x in diamond_points
    ]

    values_a = [dalembert(data_a, t, x) for t, x in diamond_points]
    values_b = [dalembert(data_b, t, x) for t, x in diamond_points]
    equal_inside = all(abs(a - b) <= TOL for a, b in zip(values_a, values_b))

    outside_point = (0.5, 4.0)
    outside_a = dalembert(data_a, *outside_point)
    outside_b = dalembert(data_b, *outside_point)

    return {
        "initial_interval": initial_interval,
        "diamond_points": diamond_points,
        "all_sampled_points_in_domain": all(diamond_membership),
        "solutions_equal_on_sampled_domain": equal_inside,
        "outside_point": outside_point,
        "outside_value_a": outside_a,
        "outside_value_b": outside_b,
        "solutions_differ_outside": abs(outside_a - outside_b) > TOL,
        "global_initial_data_distinct": True,
        "domain_limited_reconstruction_not_global": equal_inside and abs(outside_a - outside_b) > TOL,
    }


def law_necessity_audit() -> dict[str, object]:
    # u_wave = 0 satisfies the wave equation with f=g=0.
    # u_alt = t^2 shares u(0,x)=0 and u_t(0,x)=0, but has residual u_tt-u_xx = 2.
    target_t = 1.0
    target_x = 0.0

    u_wave = 0.0
    u_alt = target_t * target_t
    alt_wave_residual = 2.0

    return {
        "same_one_slice_field": True,
        "same_one_slice_time_derivative": True,
        "u_wave_at_target": u_wave,
        "u_alt_at_target": u_alt,
        "continuations_distinct": abs(u_wave - u_alt) > TOL,
        "alt_wave_equation_residual": alt_wave_residual,
        "evolution_relation_required_for_unique_standard_continuation": abs(alt_wave_residual) > TOL,
    }


def report() -> int:
    print("PHY-REL-006 — CAUCHY DATA / DOMAIN OF DEPENDENCE / RECONSTRUCTION AUDIT")
    print("Comparator: 1+1 wave equation, c=1; d'Alembert formula.\n")

    c = cauchy_component_audit()
    print("[1] Completeness of Cauchy data")
    for key, value in c.items():
        print(f"{key}: {value}")
    print()

    d = domain_of_dependence_audit()
    print("[2] Domain of dependence / reconstruction")
    for key, value in d.items():
        print(f"{key}: {value}")
    print()

    l = law_necessity_audit()
    print("[3] Evolution-law necessity control")
    for key, value in l.items():
        print(f"{key}: {value}")
    print()

    assert c["field_value_alone_insufficient"]
    assert d["all_sampled_points_in_domain"]
    assert d["solutions_equal_on_sampled_domain"]
    assert d["solutions_differ_outside"]
    assert d["domain_limited_reconstruction_not_global"]
    assert l["continuations_distinct"]
    assert l["evolution_relation_required_for_unique_standard_continuation"]

    print("SCOPED OUTCOMES")
    print("complete wave Cauchy data (f,g) under the fixed PDE: VALID_IN_DOMAIN")
    print("field value f alone -> unique future: NOT_SUFFICIENT_FOR_EXTENSION")
    print("interval data -> solution in its domain of dependence: VALID_IN_DOMAIN")
    print("domain-limited solution -> global solution reconstruction: NOT_SUFFICIENT_FOR_EXTENSION")
    print("global reconstruction from restricted domain: RECONSTRUCTION_LOSS")
    print("one-slice data without an evolution relation -> unique continuation: REJECTED")
    print("SUMMARY: PASS_WITH_REFINEMENT")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("all",), default="all")
    parser.parse_args()
    return report()


if __name__ == "__main__":
    raise SystemExit(main())
