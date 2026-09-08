#!/usr/bin/env python3
"""
Finite-dimensional quantum core reconstruction witness for the DSD Method Family.

Tests:
1. Schrödinger/Heisenberg prediction factorization for a unitary channel.
2. The same factorization for a non-unitary CPTP amplitude-damping channel.
3. Restricted-readout non-reconstruction versus Pauli-complete qubit reconstruction.
4. Contravariant composition of channel adjoints.

Standard library only.
"""

from __future__ import annotations

import argparse
import cmath
import math
from typing import Callable, List, Sequence

Matrix = List[List[complex]]
TOL = 1e-10


def zeros(n: int, m: int) -> Matrix:
    return [[0j for _ in range(m)] for _ in range(n)]


def mat_add(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_sub(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_scale(c: complex, a: Matrix) -> Matrix:
    return [[c * a[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_mul(a: Matrix, b: Matrix) -> Matrix:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def dagger(a: Matrix) -> Matrix:
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def trace(a: Matrix) -> complex:
    return sum(a[i][i] for i in range(min(len(a), len(a[0]))))


def expectation(rho: Matrix, effect: Matrix) -> complex:
    return trace(mat_mul(rho, effect))


def mat_close(a: Matrix, b: Matrix, tol: float = TOL) -> bool:
    return all(
        abs(a[i][j] - b[i][j]) <= tol
        for i in range(len(a))
        for j in range(len(a[0]))
    )


def scalar_close(a: complex, b: complex, tol: float = TOL) -> bool:
    return abs(a - b) <= tol


I: Matrix = [[1 + 0j, 0j], [0j, 1 + 0j]]
X: Matrix = [[0j, 1 + 0j], [1 + 0j, 0j]]
Y: Matrix = [[0j, -1j], [1j, 0j]]
Z: Matrix = [[1 + 0j, 0j], [0j, -1 + 0j]]

P0: Matrix = [[1 + 0j, 0j], [0j, 0j]]
P1: Matrix = [[0j, 0j], [0j, 1 + 0j]]
P_PLUS: Matrix = mat_scale(0.5, mat_add(I, X))
P_MINUS: Matrix = mat_scale(0.5, mat_sub(I, X))


def unitary_channel(u: Matrix, rho: Matrix) -> Matrix:
    return mat_mul(mat_mul(u, rho), dagger(u))


def unitary_dual(u: Matrix, effect: Matrix) -> Matrix:
    return mat_mul(mat_mul(dagger(u), effect), u)


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


def pauli_profile(rho: Matrix) -> tuple[float, float, float]:
    return tuple(expectation(rho, a).real for a in (X, Y, Z))  # type: ignore[return-value]


def reconstruct_qubit(profile: tuple[float, float, float]) -> Matrix:
    x, y, z = profile
    return mat_scale(
        0.5,
        mat_add(
            I,
            mat_add(
                mat_scale(x, X),
                mat_add(mat_scale(y, Y), mat_scale(z, Z)),
            ),
        ),
    )


def test_unitary_picture() -> None:
    theta = math.pi / 2
    u: Matrix = [
        [cmath.exp(-1j * theta / 2), 0j],
        [0j, cmath.exp(1j * theta / 2)],
    ]
    rho0 = P_PLUS
    effect = P_PLUS

    rho_t = unitary_channel(u, rho0)
    schr = expectation(rho_t, effect)
    heis = expectation(rho0, unitary_dual(u, effect))

    assert scalar_close(schr, heis)
    assert scalar_close(schr, 0.5)
    assert scalar_close(expectation(rho0, X), 1.0)
    assert scalar_close(expectation(rho_t, X), 0.0)
    assert scalar_close(expectation(rho_t, Y), 1.0)

    print("[unitary] PASS")
    print(f"  Schrödinger probability = {schr.real:.12f}")
    print(f"  Heisenberg probability  = {heis.real:.12f}")
    print("  same prediction, time dependence shifted from state to effect")


def amplitude_damping_kraus(gamma: float) -> list[Matrix]:
    return [
        [[1 + 0j, 0j], [0j, math.sqrt(1 - gamma) + 0j]],
        [[0j, math.sqrt(gamma) + 0j], [0j, 0j]],
    ]


def test_general_channel() -> None:
    gamma = 0.25
    kraus = amplitude_damping_kraus(gamma)
    rho0 = P_PLUS
    effect = P1

    rho_t = kraus_channel(kraus, rho0)
    pulled_effect = kraus_dual(kraus, effect)

    schr = expectation(rho_t, effect)
    heis = expectation(rho0, pulled_effect)

    assert scalar_close(schr, heis)
    assert scalar_close(schr, 0.375)
    assert mat_close(pulled_effect, mat_scale(0.75, P1))
    assert mat_close(kraus_dual(kraus, I), I)

    print("[channel] PASS")
    print(f"  amplitude-damping gamma = {gamma}")
    print(f"  output excited probability = {schr.real:.12f}")
    print("  dual map is unital and reproduces the same readout")


def test_reconstruction() -> None:
    z_plus = expectation(P_PLUS, P0).real
    z_minus = expectation(P_MINUS, P0).real
    assert abs(z_plus - z_minus) <= TOL

    kraus = amplitude_damping_kraus(0.25)
    rho = kraus_channel(kraus, P_PLUS)
    profile = pauli_profile(rho)
    recovered = reconstruct_qubit(profile)

    assert mat_close(rho, recovered)

    print("[reconstruction] PASS")
    print(f"  Z-only P(0): |+>={z_plus:.12f}, |->={z_minus:.12f}")
    print(f"  Pauli profile (x,y,z) = {profile}")
    print("  full Pauli profile reconstructs the tested qubit state")


def test_composition_dual() -> None:
    gamma = 0.25
    kraus = amplitude_damping_kraus(gamma)
    theta = math.pi / 3
    u: Matrix = [
        [cmath.exp(-1j * theta / 2), 0j],
        [0j, cmath.exp(1j * theta / 2)],
    ]

    rho0 = P_PLUS
    effect = P_PLUS

    rho_after = unitary_channel(u, kraus_channel(kraus, rho0))
    lhs = expectation(rho_after, effect)

    effect_back = kraus_dual(kraus, unitary_dual(u, effect))
    rhs = expectation(rho0, effect_back)

    assert scalar_close(lhs, rhs)

    print("[composition] PASS")
    print(f"  forward-state / reverse-dual prediction = {lhs.real:.12f}")
    print("  (Gamma2 o Gamma1)^* = Gamma1^* o Gamma2^* on the tested effect")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("all", "unitary", "channel", "reconstruction", "composition"),
        default="all",
    )
    args = parser.parse_args()

    tests: dict[str, Callable[[], None]] = {
        "unitary": test_unitary_picture,
        "channel": test_general_channel,
        "reconstruction": test_reconstruction,
        "composition": test_composition_dual,
    }

    if args.mode == "all":
        for test in tests.values():
            test()
        print("OVERALL: PASS_WITH_BOUNDARY")
    else:
        tests[args.mode]()


if __name__ == "__main__":
    main()
