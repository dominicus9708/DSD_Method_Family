#!/usr/bin/env python3
"""Peres-Mermin square reproducibility witness for DSD quantum-context audit.

This script verifies the operator identities of a standard two-qubit
Peres-Mermin square and exhaustively enumerates all 2^9 context-independent
{+1,-1} value assignments.

It does not derive quantum mechanics from DSD. Quantum Pauli operators and
the product constraints are supplied as the external quantum specialization.
"""

from __future__ import annotations

import itertools
from collections import Counter
import numpy as np


def kron(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.kron(a, b)


def matrix_product(items: list[np.ndarray]) -> np.ndarray:
    out = np.eye(4, dtype=complex)
    for item in items:
        out = out @ item
    return out


def identity_sign(m: np.ndarray, atol: float = 1e-12) -> int:
    eye = np.eye(4, dtype=complex)
    if np.allclose(m, eye, atol=atol):
        return 1
    if np.allclose(m, -eye, atol=atol):
        return -1
    raise ValueError("context product is neither +I nor -I")


def commute(a: np.ndarray, b: np.ndarray, atol: float = 1e-12) -> bool:
    return np.allclose(a @ b, b @ a, atol=atol)


def classical_context_products(values: tuple[int, ...]) -> list[int]:
    grid = np.array(values, dtype=int).reshape(3, 3)
    return [
        int(np.prod(grid[0, :])),
        int(np.prod(grid[1, :])),
        int(np.prod(grid[2, :])),
        int(np.prod(grid[:, 0])),
        int(np.prod(grid[:, 1])),
        int(np.prod(grid[:, 2])),
    ]


def main() -> None:
    i2 = np.eye(2, dtype=complex)
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    z = np.array([[1, 0], [0, -1]], dtype=complex)

    # Standard two-qubit Peres-Mermin square.
    square = [
        [kron(x, i2), kron(i2, x), kron(x, x)],
        [kron(i2, y), kron(y, i2), kron(y, y)],
        [kron(x, y), kron(y, x), kron(z, z)],
    ]

    contexts = [
        square[0], square[1], square[2],
        [square[r][0] for r in range(3)],
        [square[r][1] for r in range(3)],
        [square[r][2] for r in range(3)],
    ]
    labels = ["row1", "row2", "row3", "col1", "col2", "col3"]

    commute_ok = []
    signs = []
    for label, context in zip(labels, contexts):
        pairwise = all(
            commute(context[a], context[b])
            for a in range(3) for b in range(a + 1, 3)
        )
        commute_ok.append(pairwise)
        signs.append(identity_sign(matrix_product(context)))
        print(f"{label}: pairwise_commuting={pairwise}, product_sign={signs[-1]:+d}")

    targets = [1, 1, 1, 1, 1, -1]
    assert signs == targets
    assert all(commute_ok)

    satisfaction_distribution: Counter[int] = Counter()
    score_distribution: Counter[int] = Counter()
    exact_global = 0

    for values in itertools.product((-1, 1), repeat=9):
        products = classical_context_products(values)
        satisfied = sum(p == t for p, t in zip(products, targets))
        score = sum(t * p for t, p in zip(targets, products))
        satisfaction_distribution[satisfied] += 1
        score_distribution[score] += 1
        if satisfied == 6:
            exact_global += 1

    local_assignments_per_context = 4  # x*y*z=fixed sign over three ±1 variables
    unconstrained_local_product = local_assignments_per_context ** 6
    max_satisfied = max(satisfaction_distribution)
    max_noncontextual_score = max(score_distribution)
    quantum_context_score = 6

    print("\nExhaustive global-assignment audit")
    print(f"total_global_assignments={2**9}")
    print(f"exact_noncontextual_global_assignments={exact_global}")
    print(f"satisfaction_distribution={dict(sorted(satisfaction_distribution.items()))}")
    print(f"max_context_constraints_satisfied={max_satisfied}/6")
    print(f"noncontextual_score_max={max_noncontextual_score}")
    print(f"quantum_operator_context_score={quantum_context_score}")
    print(f"local_assignments_per_context={local_assignments_per_context}")
    print(f"independent_context_local_products_before_overlap_gluing={unconstrained_local_product}")

    assert exact_global == 0
    assert max_satisfied == 5
    assert max_noncontextual_score == 4
    assert quantum_context_score == 6


if __name__ == "__main__":
    main()
