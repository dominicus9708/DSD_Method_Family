#!/usr/bin/env python3
"""
Track-2 B2 finite witness: passive representation change vs active physical transition.

Purpose
-------
Compare only the structural distinction shared by standard QM and relativity:

    passive re-expression of the same semantic object
    !=
    active transition of the represented physical state/configuration.

Checks
------
1. Generic semantic-decoder criterion for passive re-encoding.
2. Qubit witness: the same numerical unitary can serve as a basis change or as
   an active state evolution, depending on which objects co-transform.
3. Relativity witness: an invertible Lorentz-frame change preserves the event
   and interval while a timelike worldline transition connects distinct events.

This script does not infer either standard-theory group action from DSD and does
not identify reversibility with temporal transition Gamma.

Python standard library only.
"""

from __future__ import annotations

import argparse
import math

TOL = 1e-12


def matvec(a, v):
    return [sum(a[i][j] * v[j] for j in range(len(v))) for i in range(len(a))]


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def dagger(a):
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def inner(u, v):
    return sum(u[i].conjugate() * v[i] for i in range(len(u)))


def expectation(psi, op):
    return inner(psi, matvec(op, psi))


def max_vector_difference(a, b):
    return max(abs(x - y) for x, y in zip(a, b))


def max_matrix_difference(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(len(a)) for j in range(len(a[0])))


def ry(theta):
    c = math.cos(theta / 2.0)
    s = math.sin(theta / 2.0)
    return [
        [complex(c), complex(-s)],
        [complex(s), complex(c)],
    ]


def qm_witness():
    # Standard qubit data.
    psi = [1.0 + 0.0j, 0.0 + 0.0j]
    z = [[1.0 + 0.0j, 0.0 + 0.0j], [0.0 + 0.0j, -1.0 + 0.0j]]
    u = ry(math.pi / 2.0)
    u_dag = dagger(u)

    # Passive basis/representation change: state coordinates and operator
    # coordinates co-transform. The represented physical expectation is unchanged.
    psi_passive = matvec(u_dag, psi)
    z_passive = matmul(matmul(u_dag, z), u)
    exp_original = expectation(psi, z)
    exp_passive = expectation(psi_passive, z_passive)

    # Active Schrödinger-picture state evolution: the state changes under the same
    # numerical U while the laboratory Z observable is held fixed.
    psi_active = matvec(u, psi)
    exp_active = expectation(psi_active, z)

    return {
        "original_Z_expectation": exp_original.real,
        "passive_Z_expectation": exp_passive.real,
        "passive_expectation_preserved": abs(exp_original - exp_passive) <= TOL,
        "passive_coordinates_changed": max_vector_difference(psi, psi_passive) > TOL,
        "active_Z_expectation": exp_active.real,
        "active_state_changed": max_vector_difference(psi, psi_active) > TOL,
        "active_selected_readout_changed": abs(exp_original - exp_active) > TOL,
        "same_numeric_U_used_for_both_roles": True,
    }


def gamma(beta):
    if not (-1.0 < beta < 1.0):
        raise ValueError("beta must satisfy |beta| < 1")
    return 1.0 / math.sqrt(1.0 - beta * beta)


def boost(point, beta):
    t, x = point
    g = gamma(beta)
    return (g * (t - beta * x), g * (x - beta * t))


def interval_sq(a, b):
    dt = b[0] - a[0]
    dx = b[1] - a[1]
    return dx * dx - dt * dt


def rel_witness():
    beta = 0.6

    # Passive frame representation of one event.
    p = (2.0, 1.0)
    p_prime = boost(p, beta)
    p_back = boost(p_prime, -beta)
    s2 = interval_sq((0.0, 0.0), p)
    s2_prime = interval_sq((0.0, 0.0), p_prime)

    # Physical timelike progression along a supplied worldline segment.
    e0 = (0.0, 0.0)
    e1 = (2.0, 1.0)
    e0_prime = boost(e0, beta)
    e1_prime = boost(e1, beta)
    worldline_s2 = interval_sq(e0, e1)
    worldline_s2_prime = interval_sq(e0_prime, e1_prime)
    proper_time = math.sqrt(-worldline_s2)

    return {
        "event_original": p,
        "event_boosted_coordinates": p_prime,
        "inverse_boost_recovers_event_coordinates": (
            abs(p_back[0] - p[0]) <= TOL and abs(p_back[1] - p[1]) <= TOL
        ),
        "event_interval_original": s2,
        "event_interval_boosted": s2_prime,
        "event_interval_preserved": abs(s2 - s2_prime) <= TOL,
        "worldline_events_distinct": e0 != e1,
        "worldline_interval_original": worldline_s2,
        "worldline_interval_boosted": worldline_s2_prime,
        "worldline_proper_time": proper_time,
        "worldline_proper_time_preserved_by_passive_boost": abs(worldline_s2 - worldline_s2_prime) <= TOL,
    }


def generic_role_witness():
    # A minimal semantic carrier and two coordinate systems.
    # Decoder D_r turns a representation tuple into the semantic scalar x+y.
    semantic = (2.0, 1.0)

    def decode_a(coords):
        return coords

    # B representation stores (u,v)=(x+y,x-y), with an inverse decoder.
    def transform_a_to_b(coords):
        x, y = coords
        return (x + y, x - y)

    def decode_b(coords):
        u, v = coords
        return ((u + v) / 2.0, (u - v) / 2.0)

    represented_b = transform_a_to_b(semantic)
    passive_commutes = decode_b(represented_b) == decode_a(semantic)

    # An active semantic transition changes the semantic object itself.
    def evolve_semantic(coords):
        x, y = coords
        return (x + 1.0, y)

    evolved = evolve_semantic(semantic)

    return {
        "semantic_before": semantic,
        "representation_b": represented_b,
        "passive_decoder_commutes": passive_commutes,
        "semantic_after_active_transition": evolved,
        "active_transition_nonidentity": evolved != semantic,
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
        g = generic_role_witness()
        assert g["passive_decoder_commutes"] is True
        assert g["active_transition_nonidentity"] is True
        print_block("GENERIC SEMANTIC / REPRESENTATION ROLE", g)

    if args.mode in ("all", "qm"):
        q = qm_witness()
        assert q["passive_expectation_preserved"] is True
        assert q["passive_coordinates_changed"] is True
        assert q["active_state_changed"] is True
        assert q["active_selected_readout_changed"] is True
        assert abs(q["original_Z_expectation"] - 1.0) <= TOL
        assert abs(q["active_Z_expectation"]) <= TOL
        print_block("STANDARD-QM PASSIVE VS ACTIVE UNITARY ROLE", q)

    if args.mode in ("all", "rel"):
        r = rel_witness()
        assert r["inverse_boost_recovers_event_coordinates"] is True
        assert r["event_interval_preserved"] is True
        assert r["worldline_events_distinct"] is True
        assert r["worldline_interval_original"] < 0.0
        assert r["worldline_proper_time_preserved_by_passive_boost"] is True
        print_block("RELATIVITY PASSIVE FRAME VS WORLDLINE TRANSITION", r)

    print("\nSCOPED OUTCOMES")
    print("passive representation change: VALID_IN_DOMAIN")
    print("active physical transition: VALID_IN_DOMAIN when supplied by the standard theory")
    print("passive representation change = temporal Gamma: NON_IDENTICAL")
    print("invertible/reversible map -> passive representation role: REJECTED")
    print("same algebraic transformation symbol/matrix -> same semantic role: REJECTED")
    print("VERDICT: PASS_WITH_BOUNDARY")


if __name__ == "__main__":
    main()
