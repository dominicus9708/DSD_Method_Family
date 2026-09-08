#!/usr/bin/env python3
"""
QM Core Reconstruction 001R — integrated four-layer DSD witness.

Purpose:
- represent a finite-dimensional quantum prediction as:
  Formation background -> Property slice -> Static readout aggregate -> Dynamics
- verify that Born probabilities are downstream property/readout values rather than
  Stage-VI formation-channel identity values in a regular dynamical realization
- verify Schrödinger/Heisenberg prediction equality, basis covariance,
  and static-slice recovery under a non-unitary CPTP transition.

Standard library only.
"""
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Dict, Iterable, List, Sequence, Tuple

Matrix = List[List[complex]]
TOL = 1e-10


def zeros(n: int, m: int) -> Matrix:
    return [[0j for _ in range(m)] for _ in range(n)]


def mat_add(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_mul(a: Matrix, b: Matrix) -> Matrix:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def mat_scale(c: complex, a: Matrix) -> Matrix:
    return [[c * a[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def dagger(a: Matrix) -> Matrix:
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def trace(a: Matrix) -> complex:
    return sum(a[i][i] for i in range(min(len(a), len(a[0]))))


def expectation(rho: Matrix, effect: Matrix) -> float:
    z = trace(mat_mul(rho, effect))
    assert abs(z.imag) <= TOL
    return z.real


def mat_close(a: Matrix, b: Matrix, tol: float = TOL) -> bool:
    return all(
        abs(a[i][j] - b[i][j]) <= tol
        for i in range(len(a))
        for j in range(len(a[0]))
    )


I: Matrix = [[1 + 0j, 0j], [0j, 1 + 0j]]
X: Matrix = [[0j, 1 + 0j], [1 + 0j, 0j]]
P0: Matrix = [[1 + 0j, 0j], [0j, 0j]]
P1: Matrix = [[0j, 0j], [0j, 1 + 0j]]
PPLUS: Matrix = mat_scale(0.5, mat_add(I, X))


@dataclass(frozen=True)
class FormationChannel:
    configuration: str
    material: str
    quantity_kind: str
    assigned_value: str
    role: str


@dataclass
class QuantumPropertySlice:
    state: Matrix
    effects: Dict[str, Matrix]


@dataclass(frozen=True)
class BornRecord:
    outcome: str
    probability: float


def born_records(prop: QuantumPropertySlice) -> List[BornRecord]:
    return [
        BornRecord(outcome, expectation(prop.state, effect))
        for outcome, effect in prop.effects.items()
    ]


def static_probability_aggregate(records: Iterable[BornRecord], order: Sequence[str]) -> Tuple[float, ...]:
    by_outcome = {r.outcome: r.probability for r in records}
    return tuple(by_outcome[o] for o in order)


def amplitude_damping_kraus(gamma: float) -> List[Matrix]:
    return [
        [[1 + 0j, 0j], [0j, math.sqrt(1 - gamma) + 0j]],
        [[0j, math.sqrt(gamma) + 0j], [0j, 0j]],
    ]


def kraus_channel(kraus: Sequence[Matrix], rho: Matrix) -> Matrix:
    out = zeros(len(rho), len(rho[0]))
    for k in kraus:
        out = mat_add(out, mat_mul(mat_mul(k, rho), dagger(k)))
    return out


def kraus_dual(kraus: Sequence[Matrix], effect: Matrix) -> Matrix:
    out = zeros(len(effect), len(effect[0]))
    for k in kraus:
        out = mat_add(out, mat_mul(mat_mul(dagger(k), effect), k))
    return out


def transform_basis(v: Matrix, a: Matrix) -> Matrix:
    return mat_mul(mat_mul(dagger(v), a), v)


def test_layer_placement() -> None:
    channels = (
        FormationChannel("prep-plus/Z-measure", "qubit", "measurement-outcome", "admitted", "outcome-0"),
        FormationChannel("prep-plus/Z-measure", "qubit", "measurement-outcome", "admitted", "outcome-1"),
    )
    assert channels[0].assigned_value == channels[1].assigned_value == "admitted"

    prop = QuantumPropertySlice(PPLUS, {"0": P0, "1": P1})
    p = static_probability_aggregate(born_records(prop), ("0", "1"))
    assert all(abs(a - b) <= TOL for a, b in zip(p, (0.5, 0.5)))
    print("[layer-placement] PASS")
    print(f"  stable formation channels = {len(channels)}")
    print(f"  downstream Born aggregate = {p}")


def test_dynamic_static_slice() -> None:
    prop0 = QuantumPropertySlice(PPLUS, {"0": P0, "1": P1})
    p0 = static_probability_aggregate(born_records(prop0), ("0", "1"))

    kraus = amplitude_damping_kraus(0.25)
    prop1 = QuantumPropertySlice(kraus_channel(kraus, prop0.state), prop0.effects)
    p1 = static_probability_aggregate(born_records(prop1), ("0", "1"))

    assert all(abs(a - b) <= TOL for a, b in zip(p0, (0.5, 0.5)))
    assert all(abs(a - b) <= TOL for a, b in zip(p1, (0.625, 0.375)))
    assert abs(sum(p1) - 1.0) <= TOL
    print("[dynamic-static-slice] PASS")
    print(f"  p(t0) = {p0}")
    print(f"  p(t1) = {p1}")
    print("  same formation protocol, evolving property slice, valid static readout each slice")


def test_picture_factorization() -> None:
    kraus = amplitude_damping_kraus(0.25)
    rho1 = kraus_channel(kraus, PPLUS)

    for label, effect in {"0": P0, "1": P1}.items():
        schr = expectation(rho1, effect)
        heis = expectation(PPLUS, kraus_dual(kraus, effect))
        assert abs(schr - heis) <= TOL
        print(f"[picture-{label}] PASS: {schr:.12f}")


def test_basis_covariance() -> None:
    theta = math.pi / 3
    v: Matrix = [
        [math.cos(theta / 2) + 0j, -math.sin(theta / 2) + 0j],
        [math.sin(theta / 2) + 0j, math.cos(theta / 2) + 0j],
    ]
    rho_b = transform_basis(v, PPLUS)
    e_b = transform_basis(v, P0)
    p_original = expectation(PPLUS, P0)
    p_changed_basis = expectation(rho_b, e_b)
    assert abs(p_original - p_changed_basis) <= TOL
    print("[basis-covariance] PASS")
    print(f"  Born readout invariant under joint basis re-expression = {p_original:.12f}")


def test_formation_identity_warning() -> None:
    c0 = FormationChannel("same-protocol", "qubit", "Born-probability", "0.500", "outcome-1")
    c1 = FormationChannel("same-protocol", "qubit", "Born-probability", "0.375", "outcome-1")
    assert c0 != c1
    print("[formation-identity-warning] PASS")
    print("  changing Born value in the channel tuple changes formation-channel identity")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("all", "placement", "slice", "picture", "basis", "identity"),
        default="all",
    )
    args = parser.parse_args()
    tests = {
        "placement": test_layer_placement,
        "slice": test_dynamic_static_slice,
        "picture": test_picture_factorization,
        "basis": test_basis_covariance,
        "identity": test_formation_identity_warning,
    }
    if args.mode == "all":
        for f in tests.values():
            f()
        print("OVERALL: PASS_WITH_REFINEMENT")
    else:
        tests[args.mode]()


if __name__ == "__main__":
    main()
