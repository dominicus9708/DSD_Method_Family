#!/usr/bin/env python3
"""
Track-2 B4 finite witness: reduction/access map vs induced transition closure.

Purpose
-------
Test the exact map-level condition for a reduced state to admit an autonomous
induced transition:

    R o Gamma = Gamma_red o R

on the declared domain.

The script checks:
1. Generic finite fiber-compatibility criterion.
2. Standard-QM two-qubit witnesses using partial trace and unitary dynamics.
3. A 1+1 wave-equation domain-restriction witness using d'Alembert evolution.

It does not identify the physical mechanisms in QM and relativity, and it does
not infer any standard-theory dynamics from DSD.

Python standard library only.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from typing import Callable, Hashable, Iterable, TypeVar

X = TypeVar("X", bound=Hashable)
Y = TypeVar("Y", bound=Hashable)

TOL = 1e-12


def freeze(value):
    if isinstance(value, dict):
        return tuple(sorted((k, freeze(v)) for k, v in value.items()))
    if isinstance(value, (list, tuple)):
        return tuple(freeze(v) for v in value)
    if isinstance(value, complex):
        return (round(value.real, 12), round(value.imag, 12))
    if isinstance(value, float):
        return round(value, 12)
    return value


def fibers(domain: Iterable[X], reduce_map: Callable[[X], Y]):
    out = defaultdict(list)
    for x in domain:
        out[freeze(reduce_map(x))].append(x)
    return dict(out)


def induced_transition_exists(
    domain: Iterable[X],
    reduce_map: Callable[[X], Y],
    transition: Callable[[X], X],
):
    """
    Finite criterion for an induced transition on im(R):

        R(x)=R(x') => R(Gamma(x))=R(Gamma(x')).
    """
    failures = []
    for reduced_value, xs in fibers(domain, reduce_map).items():
        image_values = {freeze(reduce_map(transition(x))) for x in xs}
        if len(image_values) > 1:
            failures.append((reduced_value, tuple(xs), image_values))
    return len(failures) == 0, failures


def generic_witness():
    domain = ("a", "b", "c")
    reduced = {"a": 0, "b": 0, "c": 1}

    gamma_good = {"a": "c", "b": "c", "c": "a"}
    gamma_bad = {"a": "a", "b": "c", "c": "c"}

    r = lambda x: reduced[x]
    good, good_fail = induced_transition_exists(domain, r, lambda x: gamma_good[x])
    bad, bad_fail = induced_transition_exists(domain, r, lambda x: gamma_bad[x])

    return {
        "fibers": fibers(domain, r),
        "fiber_compatible_transition_closes": good,
        "fiber_compatible_failures": good_fail,
        "fiber_splitting_transition_closes": bad,
        "fiber_splitting_failures": bad_fail,
    }


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def dagger(a):
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def outer(v):
    return [[v[i] * v[j].conjugate() for j in range(len(v))] for i in range(len(v))]


def kron(a, b):
    return [
        [a[i][j] * b[k][l] for j in range(len(a[0])) for l in range(len(b[0]))]
        for i in range(len(a))
        for k in range(len(b))
    ]


def apply_unitary(rho, u):
    return matmul(matmul(u, rho), dagger(u))


def partial_trace_b_2q(rho):
    return [
        [sum(rho[2 * a + b][2 * ap + b] for b in range(2)) for ap in range(2)]
        for a in range(2)
    ]


def qm_witness():
    ket00 = [1.0 + 0j, 0j, 0j, 0j]
    ket01 = [0j, 1.0 + 0j, 0j, 0j]

    states = {
        "rho00": outer(ket00),
        "rho01": outer(ket01),
    }

    swap = [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]

    x = [[0.0, 1.0], [1.0, 0.0]]
    ident = [[1.0, 0.0], [0.0, 1.0]]
    local_x = kron(x, ident)

    names = tuple(states)
    reduce_a = lambda name: partial_trace_b_2q(states[name])

    def swap_transition(name):
        return (name, "swap")

    def local_transition(name):
        return (name, "local_x")

    ext_states = {}
    for name, rho in states.items():
        ext_states[(name, "swap")] = apply_unitary(rho, swap)
        ext_states[(name, "local_x")] = apply_unitary(rho, local_x)

    def reduce_extended(key):
        if isinstance(key, tuple):
            return partial_trace_b_2q(ext_states[key])
        return reduce_a(key)

    swap_closes, swap_failures = induced_transition_exists(
        names, reduce_extended, swap_transition
    )
    local_closes, local_failures = induced_transition_exists(
        names, reduce_extended, local_transition
    )

    return {
        "same_initial_A_reduction": freeze(reduce_a("rho00")) == freeze(reduce_a("rho01")),
        "initial_A_rho00": reduce_a("rho00"),
        "initial_A_rho01": reduce_a("rho01"),
        "after_SWAP_A_rho00": reduce_extended(("rho00", "swap")),
        "after_SWAP_A_rho01": reduce_extended(("rho01", "swap")),
        "SWAP_induced_A_transition_exists_on_witness_domain": swap_closes,
        "SWAP_failures": swap_failures,
        "after_local_X_A_rho00": reduce_extended(("rho00", "local_x")),
        "after_local_X_A_rho01": reduce_extended(("rho01", "local_x")),
        "local_X_induced_A_transition_exists_on_witness_domain": local_closes,
        "local_X_failures": local_failures,
    }


def f_zero(x: float) -> float:
    return 0.0


def f_outside_right(x: float) -> float:
    return 1.0 if x > 2.0 else 0.0


def wave_value(f, t: float, x: float) -> float:
    """d'Alembert solution for g=0 and wave speed c=1."""
    return 0.5 * (f(x - t) + f(x + t))


def rel_wave_witness():
    t = 1.0
    initial_interval = (-2.0, 2.0)
    inner_target_samples = (-1.0, -0.5, 0.0, 0.5, 1.0)
    fixed_interval_boundary_sample = 1.5

    inner_zero = tuple(wave_value(f_zero, t, x) for x in inner_target_samples)
    inner_outside = tuple(wave_value(f_outside_right, t, x) for x in inner_target_samples)

    boundary_zero = wave_value(f_zero, t, fixed_interval_boundary_sample)
    boundary_outside = wave_value(f_outside_right, t, fixed_interval_boundary_sample)

    return {
        "initial_interval": initial_interval,
        "initial_restrictions_equal": True,
        "time": t,
        "domain_of_dependence_inner_samples": inner_target_samples,
        "inner_values_zero_data": inner_zero,
        "inner_values_outside_modified_data": inner_outside,
        "inner_target_determined_by_initial_restriction": freeze(inner_zero) == freeze(inner_outside),
        "same_fixed_interval_sample": fixed_interval_boundary_sample,
        "fixed_interval_value_zero_data": boundary_zero,
        "fixed_interval_value_outside_modified_data": boundary_outside,
        "same_fixed_interval_autonomous_closure_fails": abs(boundary_zero - boundary_outside) > TOL,
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
        assert g["fiber_compatible_transition_closes"] is True
        assert g["fiber_splitting_transition_closes"] is False
        print_block("GENERIC REDUCED-TRANSITION CLOSURE", g)

    if args.mode in ("all", "qm"):
        q = qm_witness()
        assert q["same_initial_A_reduction"] is True
        assert q["SWAP_induced_A_transition_exists_on_witness_domain"] is False
        assert q["local_X_induced_A_transition_exists_on_witness_domain"] is True
        print_block("STANDARD-QM PARTIAL TRACE / UNITARY", q)

    if args.mode in ("all", "rel"):
        r = rel_wave_witness()
        assert r["inner_target_determined_by_initial_restriction"] is True
        assert r["same_fixed_interval_autonomous_closure_fails"] is True
        print_block("1+1 WAVE DOMAIN RESTRICTION", r)

    print("\nVERDICT: PASS_WITH_BOUNDARY")
    print("COMMON: induced reduced dynamics exists exactly when Gamma respects R-fibers.")
    print("BOUNDARY: the physical reasons for closure/failure remain theory-specific.")


if __name__ == "__main__":
    main()
