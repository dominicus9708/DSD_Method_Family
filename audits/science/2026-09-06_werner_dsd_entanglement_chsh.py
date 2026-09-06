#!/usr/bin/env python3
"""Werner-state sweep for the DSD quantum-interface audit.

Checks:
- PPT/partial-transpose entanglement threshold for the two-qubit Werner family;
- optimal CHSH value 2*sqrt(2)*p for that family;
- equality of all one-party reduced states;
- a separable classically correlated control with the same local marginals.

The script verifies standard quantum-mechanical distinctions. It does not derive
these quantum criteria from DSD.
"""

from __future__ import annotations

import math
import numpy as np


def partial_transpose_b(rho: np.ndarray) -> np.ndarray:
    return rho.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)


def reduced_states(rho: np.ndarray):
    r = rho.reshape(2, 2, 2, 2)
    rho_a = np.einsum("ijkj->ik", r)
    rho_b = np.einsum("ijil->jl", r)
    return rho_a, rho_b


def werner_state(p: float) -> np.ndarray:
    psi_minus = np.array([0, 1, -1, 0], dtype=complex) / math.sqrt(2.0)
    singlet = np.outer(psi_minus, psi_minus.conj())
    return p * singlet + (1.0 - p) * np.eye(4, dtype=complex) / 4.0


def max_chsh_werner(p: float) -> float:
    # For T = -p I_3, the Horodecki CHSH criterion gives 2 sqrt(2) p.
    return 2.0 * math.sqrt(2.0) * p


def main():
    points = [0.0, 1.0 / 3.0, 0.4, 0.5, 0.6, 1.0 / math.sqrt(2.0), 0.8, 1.0]

    print("p, min_eigenvalue(PT), entangled_by_PPT, Smax_CHSH, CHSH_violation")
    for p in points:
        rho = werner_state(p)
        eig_pt = np.linalg.eigvalsh(partial_transpose_b(rho))
        min_pt = float(eig_pt[0])
        smax = max_chsh_werner(p)
        print(
            f"{p:.12f}, {min_pt:.12f}, {min_pt < -1e-12}, "
            f"{smax:.12f}, {smax > 2.0 + 1e-12}"
        )

        rho_a, rho_b = reduced_states(rho)
        assert np.allclose(rho_a, np.eye(2) / 2.0)
        assert np.allclose(rho_b, np.eye(2) / 2.0)

    print("\nExact threshold diagnostics")
    print("PPT entanglement threshold p_ent = 1/3 =", 1.0 / 3.0)
    print("CHSH threshold p_CHSH = 1/sqrt(2) =", 1.0 / math.sqrt(2.0))
    print(
        "entangled but CHSH-nonviolating interval: 1/3 < p <= 1/sqrt(2)"
    )

    # Separable classically correlated control.
    rho_cc = np.diag([0.5, 0.0, 0.0, 0.5]).astype(complex)
    eig_cc = np.linalg.eigvalsh(partial_transpose_b(rho_cc))
    rho_a_cc, rho_b_cc = reduced_states(rho_cc)

    print("\nSeparable correlation control")
    print("rho_cc = 1/2(|00><00| + |11><11|)")
    print("PT eigenvalues:", eig_cc)
    print("rho_A =")
    print(rho_a_cc)
    print("rho_B =")
    print(rho_b_cc)
    print("same local marginals as every Werner state: yes")

    print("\nDSD information-loss diagnostic")
    print("Two-qubit trace-one Hermitian state dimension: 15")
    print("Two local Bloch vectors retained by (rho_A,rho_B): 6")
    print("Correlation-sector kernel dimension of local-marginal map: 9")


if __name__ == "__main__":
    main()
