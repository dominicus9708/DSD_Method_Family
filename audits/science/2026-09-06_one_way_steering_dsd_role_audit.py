import math
import numpy as np

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = [X, Y, Z]

KET0 = np.array([1.0, 0.0], dtype=complex)
KET1 = np.array([0.0, 1.0], dtype=complex)
P0 = np.outer(KET0, KET0.conj())
P1 = np.outer(KET1, KET1.conj())
PSI_MINUS = (np.kron(KET0, KET1) - np.kron(KET1, KET0)) / math.sqrt(2.0)
SINGLET = np.outer(PSI_MINUS, PSI_MINUS.conj())


def partial_trace(mat, dims, traced):
    da, db = dims
    reshaped = mat.reshape(da, db, da, db)
    if traced == "A":
        out = np.zeros((db, db), dtype=complex)
        for a in range(da):
            out += reshaped[a, :, a, :]
        return out
    if traced == "B":
        out = np.zeros((da, da), dtype=complex)
        for b in range(db):
            out += reshaped[:, b, :, b]
        return out
    raise ValueError("traced must be 'A' or 'B'")


def partial_transpose_b(mat, dims):
    da, db = dims
    return mat.reshape(da, db, da, db).transpose(0, 3, 2, 1).reshape(da * db, da * db)


def bowles_state(alpha):
    """Bowles et al. PRL 112, 200402 (2014), Eq. (3)."""
    return (
        alpha * SINGLET
        + (1.0 - alpha) / 5.0 * (
            2.0 * np.kron(P0, I2 / 2.0)
            + 3.0 * np.kron(I2 / 2.0, P1)
        )
    )


def bloch_vector(rho):
    return np.array([np.trace(rho @ P).real for P in PAULI])


def correlation_tensor(rho):
    out = np.zeros((3, 3), dtype=float)
    for i, pi in enumerate(PAULI):
        for j, pj in enumerate(PAULI):
            out[i, j] = np.trace(rho @ np.kron(pi, pj)).real
    return out


def swap_operator():
    return np.array(
        [[1, 0, 0, 0],
         [0, 0, 1, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 1]],
        dtype=complex,
    )


def povm_seed_state():
    """Quintino et al. PRA 92, 032107 (2015), Eq. (12)."""
    return 0.5 * (
        SINGLET
        + (3.0 / 5.0) * np.kron(P1, I2 / 2.0)
        + (2.0 / 5.0) * np.kron(I2 / 2.0, P0)
    )


def povm_lift(seed):
    """Lemma-1 lift for d=2: rho' = (rho + 2 P_perp x rho_B)/3."""
    rho_b = partial_trace(seed, (2, 2), "A")
    lifted = np.zeros((6, 6), dtype=complex)
    lifted[:4, :4] = seed / 3.0
    lifted[4:6, 4:6] = (2.0 / 3.0) * rho_b
    return lifted, rho_b


def local_filter_back(lifted):
    """Project Alice's qutrit onto the original qubit support."""
    block = lifted[:4, :4]
    prob = np.trace(block).real
    return block / prob, prob


def main():
    alpha = 0.5
    rho = bowles_state(alpha)
    rho_a = partial_trace(rho, (2, 2), "B")
    rho_b = partial_trace(rho, (2, 2), "A")
    pt = partial_transpose_b(rho, (2, 2))

    alpha_ent = (-6.0 + 5.0 * math.sqrt(6.0)) / 19.0

    print("=== Bowles one-way projective-steering control ===")
    print(f"alpha={alpha:.6f}")
    print(f"PPT entanglement threshold alpha_ent={alpha_ent:.12f}")
    print("rho(alpha=1/2)=")
    print(np.real_if_close(rho))
    print("state eigenvalues=", np.linalg.eigvalsh(rho))
    print("partial-transpose eigenvalues=", np.linalg.eigvalsh(pt))
    print("negativity=", float(np.sum(np.clip(-np.linalg.eigvalsh(pt), 0.0, None))))
    print("rho_A=", np.real_if_close(rho_a))
    print("rho_B=", np.real_if_close(rho_b))
    print("Bloch(A)=", bloch_vector(rho_a))
    print("Bloch(B)=", bloch_vector(rho_b))
    print("purity(A)=", float(np.trace(rho_a @ rho_a).real))
    print("purity(B)=", float(np.trace(rho_b @ rho_b).real))
    print("global purity=", float(np.trace(rho @ rho).real))
    print("correlation tensor T=")
    print(correlation_tensor(rho))

    # Literature theorem tags, not re-proved by this script:
    print("\nPublished directional result for projective measurements:")
    print("  A -> B: steerable at alpha=1/2 (13-setting witness exists; 14-setting threshold ~0.4983)")
    print("  B -> A: unsteerable for arbitrary projective measurements for alpha<=1/2")

    sw = swap_operator()
    rho_sw = sw @ rho @ sw.conj().T
    print("\n=== Swap/role-erasure control ===")
    print("spectrum difference max=", float(np.max(np.abs(np.linalg.eigvalsh(rho) - np.linalg.eigvalsh(rho_sw)))))
    print("purity difference=", float(abs(np.trace(rho @ rho) - np.trace(rho_sw @ rho_sw))))
    print("correlation singular values original=", np.linalg.svd(correlation_tensor(rho), compute_uv=False))
    print("correlation singular values swapped =", np.linalg.svd(correlation_tensor(rho_sw), compute_uv=False))
    print("Frobenius distance rho vs swapped rho=", float(np.linalg.norm(rho - rho_sw)))
    print("Bloch(A) swapped=", bloch_vector(partial_trace(rho_sw, (2, 2), "B")))
    print("Bloch(B) swapped=", bloch_vector(partial_trace(rho_sw, (2, 2), "A")))

    print("\n=== Arbitrary-POVM lift control ===")
    seed = povm_seed_state()
    lifted, seed_b = povm_lift(seed)
    filtered, success = local_filter_back(lifted)
    print("seed rho_B=", np.real_if_close(seed_b))
    print("lifted trace=", float(np.trace(lifted).real))
    print("lifted eigenvalues=", np.linalg.eigvalsh(lifted))
    print("lifted PT eigenvalues=", np.linalg.eigvalsh(partial_transpose_b(lifted, (3, 2))))
    print("filter success probability=", success)
    print("filter recovery max error=", float(np.max(np.abs(filtered - seed))))
    print("Published theorem tag:")
    print("  lifted state is one-way steerable for arbitrary single-round POVMs in the direction inherited from the seed construction.")


if __name__ == "__main__":
    main()
