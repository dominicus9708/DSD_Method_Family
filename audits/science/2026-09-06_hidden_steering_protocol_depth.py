import argparse
import math
import numpy as np


def swap_operator(d: int) -> np.ndarray:
    s = np.zeros((d * d, d * d), dtype=complex)
    for i in range(d):
        for j in range(d):
            s[j * d + i, i * d + j] = 1.0
    return s


def werner_seed(d: int) -> np.ndarray:
    ident = np.eye(d * d, dtype=complex)
    p_anti = (ident - swap_operator(d)) / 2.0
    alpha = (d - 1.0) / d
    return alpha * 2.0 * p_anti / (d * (d - 1.0)) + (1.0 - alpha) * ident / (d * d)


def partial_trace(rho: np.ndarray, da: int, db: int, over: str) -> np.ndarray:
    r = rho.reshape(da, db, da, db)
    if over.upper() == "A":
        return np.einsum("abad->bd", r)
    return np.einsum("abcb->ac", r)


def embed_a(rho: np.ndarray, da: int, db: int) -> np.ndarray:
    out = np.zeros(((da + 1) * db, (da + 1) * db), dtype=complex)
    out.reshape(da + 1, db, da + 1, db)[:da, :, :da, :] = rho.reshape(da, db, da, db)
    return out


def embed_b(rho: np.ndarray, da: int, db: int) -> np.ndarray:
    out = np.zeros((da * (db + 1), da * (db + 1)), dtype=complex)
    out.reshape(da, db + 1, da, db + 1)[:, :db, :, :db] = rho.reshape(da, db, da, db)
    return out


def hidden_steering_state(d: int) -> np.ndarray:
    # Implements Lemma 1 twice rather than relying on a typeset transcription of Eq. (14).
    rho = werner_seed(d)
    rho_b = partial_trace(rho, d, d, "A")

    p_perp_a = np.zeros((d + 1, d + 1), dtype=complex)
    p_perp_a[d, d] = 1.0
    rho1 = (embed_a(rho, d, d) + d * np.kron(p_perp_a, rho_b)) / (d + 1.0)

    rho1_a = partial_trace(rho1, d + 1, d, "B")
    p_perp_b = np.zeros((d + 1, d + 1), dtype=complex)
    p_perp_b[d, d] = 1.0
    rho2 = (embed_b(rho1, d + 1, d) + d * np.kron(rho1_a, p_perp_b)) / (d + 1.0)
    return rho2


def qubit_filter(d_total: int) -> np.ndarray:
    f = np.zeros((d_total, d_total), dtype=complex)
    f[0, 0] = 1.0
    f[1, 1] = 1.0
    return f


def apply_a(rho: np.ndarray, k: np.ndarray, da: int, db: int) -> np.ndarray:
    op = np.kron(k, np.eye(db, dtype=complex))
    return op @ rho @ op.conj().T


def apply_b(rho: np.ndarray, k: np.ndarray, da: int, db: int) -> np.ndarray:
    op = np.kron(np.eye(da, dtype=complex), k)
    return op @ rho @ op.conj().T


def two_qubit_filtered_branch(rho: np.ndarray, d_total: int):
    inds = [i * d_total + j for i in range(2) for j in range(2)]
    block = rho[np.ix_(inds, inds)]
    p_success = float(np.trace(block).real)
    return block / p_success, p_success


def two_qubit_werner(p: float) -> np.ndarray:
    psi_minus = np.array([0.0, 1.0, -1.0, 0.0], dtype=complex) / math.sqrt(2.0)
    singlet = np.outer(psi_minus, psi_minus.conj())
    return p * singlet + (1.0 - p) * np.eye(4, dtype=complex) / 4.0


def partial_transpose_two_qubit(rho: np.ndarray) -> np.ndarray:
    return rho.reshape(2, 2, 2, 2).transpose(2, 1, 0, 3).reshape(4, 4)


def audit_dimension(d: int):
    rho_hs = hidden_steering_state(d)
    d_total = d + 1
    filtered, p_success = two_qubit_filtered_branch(rho_hs, d_total)

    visibility = d / (d + 2.0)
    target = two_qubit_werner(visibility)
    max_filter_error = float(np.max(np.abs(filtered - target)))
    pt_min = float(np.min(np.linalg.eigvalsh(partial_transpose_two_qubit(filtered))).real)
    chsh_max = 2.0 * math.sqrt(2.0) * visibility

    # Nonselective local filtering instrument on Alice: {F, I-F}.
    f = qubit_filter(d_total)
    g = np.eye(d_total, dtype=complex) - f
    rho_b_before = partial_trace(rho_hs, d_total, d_total, "A")
    rho_after_nonselective = apply_a(rho_hs, f, d_total, d_total) + apply_a(rho_hs, g, d_total, d_total)
    rho_b_after = partial_trace(rho_after_nonselective, d_total, d_total, "A")
    remote_marginal_error = float(np.max(np.abs(rho_b_after - rho_b_before)))

    alice_success_branch = apply_a(rho_hs, f, d_total, d_total)
    p_alice = float(np.trace(alice_success_branch).real)
    rho_b_cond = partial_trace(alice_success_branch / p_alice, d_total, d_total, "A")
    conditional_remote_shift = float(np.max(np.abs(rho_b_cond - rho_b_before)))

    return {
        "d": d,
        "trace": float(np.trace(rho_hs).real),
        "visibility": visibility,
        "bilateral_success": p_success,
        "one_side_success": p_alice,
        "filter_error": max_filter_error,
        "pt_min": pt_min,
        "chsh_max": chsh_max,
        "remote_marginal_error": remote_marginal_error,
        "conditional_remote_shift": conditional_remote_shift,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--d-min", type=int, default=3)
    parser.add_argument("--d-max", type=int, default=8)
    args = parser.parse_args()

    print("hidden-steering sequential-protocol audit")
    print("d  vis       P_AB          PT_min       CHSHmax      remote_err   cond_shift")
    for d in range(args.d_min, args.d_max + 1):
        r = audit_dimension(d)
        print(
            f"{d:2d} {r['visibility']:.8f} {r['bilateral_success']:.10e} "
            f"{r['pt_min']:+.8f} {r['chsh_max']:.8f} "
            f"{r['remote_marginal_error']:.3e} {r['conditional_remote_shift']:.8f}"
        )
        if abs(r["trace"] - 1.0) > 1e-10:
            raise RuntimeError("hidden-steering state is not normalized")
        if r["filter_error"] > 1e-10:
            raise RuntimeError("filtered state does not match d/(d+2) Werner control")

    print("\nAnalytic controls")
    print("  filtered visibility p_d = d/(d+2)")
    print("  PVM steering: p_d > 1/2 for every d >= 3")
    print("  CHSH violation: d/(d+2) > 1/sqrt(2), first integer d = 5")
    print("  PT minimum: (1 - 3 p_d)/4 = -(d-1)/(2(d+2))")
    print("  nonselective local instrument leaves remote marginal unchanged")


if __name__ == "__main__":
    main()
