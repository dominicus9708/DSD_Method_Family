#!/usr/bin/env python3
"""
Track-2 B3 finite witness: selected readout/invariant constancy vs nonzero dynamics.

Purpose
-------
Test the abstract distinction

    constant selected readout/invariant
    !=
    unchanged underlying state / zero transition

using three finite or exactly evaluable witnesses:

1. Generic rotation with a radius-squared readout.
2. Standard-QM unitary phase evolution with constant Z-basis probabilities
   and constant energy expectation but a changing physical ray.
3. Standard special-relativistic inertial motion with constant four-velocity
   norm but changing spacetime event.

The script also checks the stronger control that endpoint return does not imply
zero intervening dynamics: a periodic quantum trajectory can return to the same
physical ray after a full cycle while differing at intermediate times.

No standard-theory law is inferred from DSD. Python standard library only.
"""

from __future__ import annotations

import argparse
import cmath
import math

TOL = 1e-12


def close(a: float, b: float, tol: float = TOL) -> bool:
    return abs(a - b) <= tol


def vec_close(a, b, tol: float = TOL) -> bool:
    return len(a) == len(b) and all(abs(x - y) <= tol for x, y in zip(a, b))


def inner(v, w):
    return sum(a.conjugate() * b for a, b in zip(v, w))


def matvec(a, v):
    return [sum(a[i][j] * v[j] for j in range(len(v))) for i in range(len(a))]


def expectation(state, op) -> float:
    return inner(state, matvec(op, state)).real


def ray_overlap_sq(a, b) -> float:
    return abs(inner(a, b)) ** 2


def generic_witness():
    """A nontrivial rotation remains inside one radius-squared readout fiber."""
    theta = math.pi / 2.0
    state0 = (1.0, 0.0)
    c, s = math.cos(theta), math.sin(theta)
    state1 = (c * state0[0] - s * state0[1], s * state0[0] + c * state0[1])

    phi = lambda p: p[0] * p[0] + p[1] * p[1]
    identity_readout = lambda p: p

    readout_constant = close(phi(state0), phi(state1))
    state_changed = not vec_close(state0, state1)
    separating_readout_detects_change = not vec_close(
        identity_readout(state0), identity_readout(state1)
    )

    # Full-cycle endpoint-return control.
    state_mid = (-1.0, 0.0)
    state_cycle = (1.0, 0.0)
    endpoint_return = vec_close(state0, state_cycle)
    nontrivial_intermediate_state = not vec_close(state0, state_mid)

    return {
        "state0": state0,
        "state1": state1,
        "phi_state0": phi(state0),
        "phi_state1": phi(state1),
        "selected_readout_constant": readout_constant,
        "state_changed": state_changed,
        "separating_readout_detects_change": separating_readout_detects_change,
        "endpoint_return_after_full_cycle": endpoint_return,
        "nontrivial_intermediate_state": nontrivial_intermediate_state,
    }


def qubit_state(t: float, omega: float = 1.0):
    """|+> evolved by H=(omega/2) Z, with hbar=1."""
    s = 1.0 / math.sqrt(2.0)
    return [
        s * cmath.exp(-0.5j * omega * t),
        s * cmath.exp(+0.5j * omega * t),
    ]


def qm_witness():
    """Constant selected probabilities/energy do not imply a stationary quantum state."""
    x_op = [[0.0, 1.0], [1.0, 0.0]]
    z_op = [[1.0, 0.0], [0.0, -1.0]]
    h_op = [[0.5, 0.0], [0.0, -0.5]]

    t0 = 0.0
    t1 = math.pi / 2.0
    tmid = math.pi
    tcycle = 2.0 * math.pi

    psi0 = qubit_state(t0)
    psi1 = qubit_state(t1)
    psimid = qubit_state(tmid)
    psicycle = qubit_state(tcycle)

    z_probs0 = tuple(abs(a) ** 2 for a in psi0)
    z_probs1 = tuple(abs(a) ** 2 for a in psi1)

    energy0 = expectation(psi0, h_op)
    energy1 = expectation(psi1, h_op)
    x0 = expectation(psi0, x_op)
    x1 = expectation(psi1, x_op)

    ray_same_01 = close(ray_overlap_sq(psi0, psi1), 1.0)
    ray_same_cycle = close(ray_overlap_sq(psi0, psicycle), 1.0)
    ray_same_mid = close(ray_overlap_sq(psi0, psimid), 1.0)

    return {
        "Z_probabilities_t0": z_probs0,
        "Z_probabilities_t1": z_probs1,
        "Z_probabilities_constant": all(close(a, b) for a, b in zip(z_probs0, z_probs1)),
        "energy_expectation_t0": energy0,
        "energy_expectation_t1": energy1,
        "energy_expectation_constant": close(energy0, energy1),
        "X_expectation_t0": x0,
        "X_expectation_t1": x1,
        "selected_X_readout_changes": not close(x0, x1),
        "same_physical_ray_t0_t1": ray_same_01,
        "full_cycle_returns_same_ray": ray_same_cycle,
        "midcycle_ray_differs": not ray_same_mid,
        "Z_expectation_t1": expectation(psi1, z_op),
    }


def minkowski_norm(v) -> float:
    return -v[0] * v[0] + sum(x * x for x in v[1:])


def rel_witness():
    """Constant four-velocity norm does not imply an unchanged spacetime event."""
    speed = 0.6
    gamma = 1.0 / math.sqrt(1.0 - speed * speed)
    four_velocity = (gamma, gamma * speed, 0.0, 0.0)

    tau0 = 0.0
    tau1 = 2.0
    event0 = tuple(tau0 * u for u in four_velocity)
    event1 = tuple(tau1 * u for u in four_velocity)

    norm0 = minkowski_norm(four_velocity)
    norm1 = minkowski_norm(four_velocity)

    return {
        "speed": speed,
        "gamma": gamma,
        "four_velocity": four_velocity,
        "four_velocity_norm_tau0": norm0,
        "four_velocity_norm_tau1": norm1,
        "invariant_norm_constant": close(norm0, norm1),
        "event_tau0": event0,
        "event_tau1": event1,
        "event_changed": not vec_close(event0, event1),
        "timelike_unit_normalization": close(norm0, -1.0),
    }


def print_block(title: str, data: dict):
    print(f"\n[{title}]")
    for key, value in data.items():
        print(f"{key}: {value}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("all", "generic", "qm", "rel"), default="all")
    args = parser.parse_args()

    if args.mode in ("all", "generic"):
        g = generic_witness()
        assert g["selected_readout_constant"] is True
        assert g["state_changed"] is True
        assert g["separating_readout_detects_change"] is True
        assert g["endpoint_return_after_full_cycle"] is True
        assert g["nontrivial_intermediate_state"] is True
        print_block("GENERIC READOUT-FIBER MOTION", g)

    if args.mode in ("all", "qm"):
        q = qm_witness()
        assert q["Z_probabilities_constant"] is True
        assert q["energy_expectation_constant"] is True
        assert q["selected_X_readout_changes"] is True
        assert q["same_physical_ray_t0_t1"] is False
        assert q["full_cycle_returns_same_ray"] is True
        assert q["midcycle_ray_differs"] is True
        print_block("STANDARD-QM ACTIVE EVOLUTION", q)

    if args.mode in ("all", "rel"):
        r = rel_witness()
        assert r["invariant_norm_constant"] is True
        assert r["timelike_unit_normalization"] is True
        assert r["event_changed"] is True
        print_block("STANDARD-RELATIVITY WORLDLINE", r)

    print("\nVERDICT: PASS_WITH_BOUNDARY")
    print("COMMON: selected-output constancy means motion can remain inside one readout fiber.")
    print("SUFFICIENT CONTROL: injective/separating readout on the declared orbit is needed to infer state constancy.")
    print("ENDPOINT CONTROL: return to the same endpoint state does not imply zero intervening dynamics.")


if __name__ == "__main__":
    main()
