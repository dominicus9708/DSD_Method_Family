#!/usr/bin/env python3
"""
Cross-theory restriction/factorization firewall witness for DSD Track 2.

Purpose
-------
Compare only the map-level structure shared by

1. standard-QM subsystem reduction by partial trace, and
2. a finite relativistic causal-domain record restriction.

The script checks the following abstract rule on finite witnesses:

    A query q can be reconstructed from a reduced map f exactly when q is
    constant on every fiber of f.

It does NOT identify partial trace with causal restriction, quantum subsystem
structure with spacetime domains, entanglement with causal inaccessibility, or
any standard-theory object with a DSD primitive.

Standard-library only.
"""

from __future__ import annotations

import argparse
import math
from collections import defaultdict
from typing import Callable, Hashable, Iterable, TypeVar

X = TypeVar("X", bound=Hashable)
Y = TypeVar("Y", bound=Hashable)
Z = TypeVar("Z", bound=Hashable)

TOL = 1e-12


def freeze(value):
    """Convert the finite outputs used here into hashable comparison keys."""
    if isinstance(value, dict):
        return tuple(sorted((k, freeze(v)) for k, v in value.items()))
    if isinstance(value, (list, tuple)):
        return tuple(freeze(v) for v in value)
    if isinstance(value, complex):
        return (round(value.real, 12), round(value.imag, 12))
    if isinstance(value, float):
        return round(value, 12)
    return value


def fiber_partition(domain: Iterable[X], f: Callable[[X], Y]):
    fibers: dict[Hashable, list[X]] = defaultdict(list)
    for x in domain:
        fibers[freeze(f(x))].append(x)
    return dict(fibers)


def factors_through(domain: Iterable[X], f: Callable[[X], Y], q: Callable[[X], Z]):
    """Finite criterion: q factors through f iff q is constant on f-fibers."""
    failures = []
    for y, xs in fiber_partition(domain, f).items():
        values = {freeze(q(x)) for x in xs}
        if len(values) > 1:
            failures.append((y, xs, values))
    return len(failures) == 0, failures


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def outer(v):
    return [[v[i] * v[j].conjugate() for j in range(len(v))] for i in range(len(v))]


def kron(a, b):
    return [
        [a[i][j] * b[k][l] for j in range(len(a[0])) for l in range(len(b[0]))]
        for i in range(len(a))
        for k in range(len(b))
    ]


def partial_trace_b_2q(rho):
    """Partial trace over the second qubit of a 4x4 two-qubit density matrix."""
    return [
        [sum(rho[2 * a + b][2 * ap + b] for b in range(2)) for ap in range(2)]
        for a in range(2)
    ]


def expectation(rho, op):
    return trace(matmul(rho, op)).real


def qm_witness():
    s = 1.0 / math.sqrt(2.0)
    states = {
        "Phi+": outer([s, 0.0, 0.0, s]),
        "Phi-": outer([s, 0.0, 0.0, -s]),
    }

    x = [[0.0, 1.0], [1.0, 0.0]]
    z = [[1.0, 0.0], [0.0, -1.0]]
    ident = [[1.0, 0.0], [0.0, 1.0]]
    xx = kron(x, x)
    zi = kron(z, ident)

    names = tuple(states)
    reduce_a = lambda name: partial_trace_b_2q(states[name])
    global_query = lambda name: expectation(states[name], xx)
    local_query = lambda name: expectation(states[name], zi)

    global_factor, global_failures = factors_through(names, reduce_a, global_query)
    local_factor, local_failures = factors_through(names, reduce_a, local_query)

    rho_a_plus = reduce_a("Phi+")
    rho_a_minus = reduce_a("Phi-")
    same_reduction = freeze(rho_a_plus) == freeze(rho_a_minus)

    return {
        "same_reduced_state": same_reduction,
        "rho_A_Phi+": rho_a_plus,
        "rho_A_Phi-": rho_a_minus,
        "XX_Phi+": global_query("Phi+"),
        "XX_Phi-": global_query("Phi-"),
        "ZA_Phi+": local_query("Phi+"),
        "ZA_Phi-": local_query("Phi-"),
        "global_query_factors_through_partial_trace": global_factor,
        "global_factor_failures": global_failures,
        "local_query_factors_through_partial_trace": local_factor,
        "local_factor_failures": local_failures,
    }


def in_causal_past(point, observer=(2.0, 0.0)):
    """1+1 Minkowski causal-past membership, units c=1."""
    t, x = point
    to, xo = observer
    dt = to - t
    dx = xo - x
    return dt >= -TOL and dt * dt - dx * dx >= -TOL


def rel_witness():
    points = {
        "P1": (0.0, 0.0),
        "P2": (1.0, 0.5),
        "P3": (1.0, 2.0),
        "P4": (3.0, 0.0),
    }
    accessible = tuple(name for name, p in points.items() if in_causal_past(p))

    records = {
        "G1": {
            "P1": "alpha",
            "P2": "beta",
            "P3": "outside-1",
            "P4": "future-1",
        },
        "G2": {
            "P1": "alpha",
            "P2": "beta",
            "P3": "outside-2",
            "P4": "future-2",
        },
    }

    names = tuple(records)
    restrict = lambda name: {p: records[name][p] for p in accessible}
    outside_query = lambda name: records[name]["P3"]
    inside_query = lambda name: records[name]["P1"]

    outside_factor, outside_failures = factors_through(names, restrict, outside_query)
    inside_factor, inside_failures = factors_through(names, restrict, inside_query)

    return {
        "causal_domain": accessible,
        "same_restricted_record": freeze(restrict("G1")) == freeze(restrict("G2")),
        "restricted_G1": restrict("G1"),
        "restricted_G2": restrict("G2"),
        "outside_P3_G1": outside_query("G1"),
        "outside_P3_G2": outside_query("G2"),
        "outside_query_factors_through_restriction": outside_factor,
        "outside_factor_failures": outside_failures,
        "inside_query_factors_through_restriction": inside_factor,
        "inside_factor_failures": inside_failures,
    }


def generic_witness():
    domain = ("a", "b", "c")
    reduced = {"a": 0, "b": 0, "c": 1}
    q_good = {"a": "same", "b": "same", "c": "other"}
    q_bad = {"a": "left", "b": "right", "c": "other"}

    good, _ = factors_through(domain, lambda x: reduced[x], lambda x: q_good[x])
    bad, failures = factors_through(domain, lambda x: reduced[x], lambda x: q_bad[x])

    return {
        "fibers": fiber_partition(domain, lambda x: reduced[x]),
        "fiber_constant_query_factors": good,
        "fiber_nonconstant_query_factors": bad,
        "nonfactorization_witness": failures,
    }


def print_block(title, data):
    print(f"\n[{title}]")
    for key, value in data.items():
        print(f"{key}: {value}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("all", "generic", "qm", "rel"), default="all")
    args = parser.parse_args()

    if args.mode in ("all", "generic"):
        g = generic_witness()
        assert g["fiber_constant_query_factors"] is True
        assert g["fiber_nonconstant_query_factors"] is False
        print_block("GENERIC FIBER/FACTORIZATION", g)

    if args.mode in ("all", "qm"):
        q = qm_witness()
        assert q["same_reduced_state"] is True
        assert abs(q["XX_Phi+"] - 1.0) < TOL
        assert abs(q["XX_Phi-"] + 1.0) < TOL
        assert q["global_query_factors_through_partial_trace"] is False
        assert q["local_query_factors_through_partial_trace"] is True
        print_block("STANDARD-QM PARTIAL TRACE", q)

    if args.mode in ("all", "rel"):
        r = rel_witness()
        assert r["causal_domain"] == ("P1", "P2")
        assert r["same_restricted_record"] is True
        assert r["outside_query_factors_through_restriction"] is False
        assert r["inside_query_factors_through_restriction"] is True
        print_block("RELATIVISTIC FINITE DOMAIN RESTRICTION", r)

    print("\nVERDICT: PASS_WITH_BOUNDARY")
    print("COMMON: fiber/factorization theorem at map level.")
    print("BOUNDARY: physical meanings and extra structures remain theory-specific.")


if __name__ == "__main__":
    main()
