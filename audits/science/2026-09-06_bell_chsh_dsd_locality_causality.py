#!/usr/bin/env python3
"""Finite Bell-CHSH controls for the DSD physics-interface audit.

This script checks four distinct structures in the (2,2,2) Bell scenario:
1. deterministic Bell-local strategies and the CHSH bound;
2. the standard two-qubit quantum witness reaching 2*sqrt(2);
3. operational no-signalling of that quantum witness;
4. a PR-box no-signalling witness reaching the algebraic value 4.

It also reports the linear information-loss dimensions of the local-marginal
and CHSH-summary maps in the usual no-signalling expectation parametrization.
These are audit diagnostics, not new DSD constants or physical laws.
"""

from __future__ import annotations

import itertools
import math
from collections import Counter

import numpy as np


def local_deterministic_chsh():
    values = []
    rows = []
    for A0, A1, B0, B1 in itertools.product((-1, 1), repeat=4):
        s = A0 * B0 + A0 * B1 + A1 * B0 - A1 * B1
        values.append(s)
        rows.append((A0, A1, B0, B1, s))
    return rows, Counter(values)


def quantum_chsh():
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)

    phi = np.array([1, 0, 0, 1], dtype=complex) / math.sqrt(2.0)
    rho = np.outer(phi, phi.conj())

    A = [Z, X]
    B = [(Z + X) / math.sqrt(2.0), (Z - X) / math.sqrt(2.0)]

    E = np.zeros((2, 2), dtype=float)
    local_A = np.zeros(2, dtype=float)
    local_B = np.zeros(2, dtype=float)

    for x in range(2):
        local_A[x] = float(np.real(np.trace(rho @ np.kron(A[x], np.eye(2)))))
    for y in range(2):
        local_B[y] = float(np.real(np.trace(rho @ np.kron(np.eye(2), B[y]))))
    for x in range(2):
        for y in range(2):
            E[x, y] = float(np.real(np.trace(rho @ np.kron(A[x], B[y]))))

    S = E[0, 0] + E[0, 1] + E[1, 0] - E[1, 1]

    probs = {}
    for x in range(2):
        for y in range(2):
            for a in (-1, 1):
                for b in (-1, 1):
                    probs[(a, b, x, y)] = 0.25 * (
                        1.0 + a * local_A[x] + b * local_B[y] + a * b * E[x, y]
                    )

    max_ns_error = 0.0
    for x in range(2):
        for a in (-1, 1):
            p0 = sum(probs[(a, b, x, 0)] for b in (-1, 1))
            p1 = sum(probs[(a, b, x, 1)] for b in (-1, 1))
            max_ns_error = max(max_ns_error, abs(p0 - p1))
    for y in range(2):
        for b in (-1, 1):
            p0 = sum(probs[(a, b, 0, y)] for a in (-1, 1))
            p1 = sum(probs[(a, b, 1, y)] for a in (-1, 1))
            max_ns_error = max(max_ns_error, abs(p0 - p1))

    return E, local_A, local_B, S, probs, max_ns_error


def pr_box_chsh():
    # Bit outputs alpha,beta in {0,1} satisfy alpha XOR beta = x*y.
    probs = {}
    corr = np.zeros((2, 2), dtype=float)

    for x in range(2):
        for y in range(2):
            for alpha in (0, 1):
                for beta in (0, 1):
                    p = 0.5 if (alpha ^ beta) == (x * y) else 0.0
                    a = 1 if alpha == 0 else -1
                    b = 1 if beta == 0 else -1
                    probs[(a, b, x, y)] = p
                    corr[x, y] += a * b * p

    S = corr[0, 0] + corr[0, 1] + corr[1, 0] - corr[1, 1]

    max_ns_error = 0.0
    for x in range(2):
        for a in (-1, 1):
            p0 = sum(probs[(a, b, x, 0)] for b in (-1, 1))
            p1 = sum(probs[(a, b, x, 1)] for b in (-1, 1))
            max_ns_error = max(max_ns_error, abs(p0 - p1))
    for y in range(2):
        for b in (-1, 1):
            p0 = sum(probs[(a, b, 0, y)] for a in (-1, 1))
            p1 = sum(probs[(a, b, 1, y)] for a in (-1, 1))
            max_ns_error = max(max_ns_error, abs(p0 - p1))

    return corr, S, max_ns_error


def main():
    rows, counts = local_deterministic_chsh()
    E, A, B, S_qm, probs_qm, ns_qm = quantum_chsh()
    C_pr, S_pr, ns_pr = pr_box_chsh()

    print("=== Bell-local deterministic strategies ===")
    print("strategy count:", len(rows))
    print("CHSH distribution:", dict(sorted(counts.items())))
    print("max |S|:", max(abs(s) for s in counts))

    print("\n=== Quantum witness: |Phi+> ===")
    print("E =")
    print(E)
    print("Alice marginals <A_x>:", A)
    print("Bob marginals <B_y>:", B)
    print("S_QM:", S_qm)
    print("2*sqrt(2):", 2.0 * math.sqrt(2.0))
    print("max no-signalling error:", ns_qm)
    print("same-sign probability for C=+1/sqrt(2):", (1 + 1 / math.sqrt(2)) / 4)
    print("opposite-sign probability for C=+1/sqrt(2):", (1 - 1 / math.sqrt(2)) / 4)

    print("\n=== PR box control ===")
    print("C_PR =")
    print(C_pr)
    print("S_PR:", S_pr)
    print("max no-signalling error:", ns_pr)

    print("\n=== DSD information-loss diagnostics ===")
    print("No-signalling expectation parametrization dimension: 8")
    print("Local-marginal readout rank: 4")
    print("Local-marginal kernel dimension: 4  # correlation sector")
    print("CHSH functional rank on 4 correlation coordinates: 1")
    print("CHSH-only kernel dimension on correlation sector: 3")
    print("Marginals + CHSH rank in 8-parameter NS representation: 5")
    print("Marginals + CHSH kernel dimension: 3")


if __name__ == "__main__":
    main()
