import math
import numpy as np

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = [X, Y, Z]

PSI_MINUS = np.array([0, 1, -1, 0], dtype=complex) / math.sqrt(2)
RHO_SINGLET = np.outer(PSI_MINUS, PSI_MINUS.conj())


def werner_state(p: float) -> np.ndarray:
    return p * RHO_SINGLET + (1.0 - p) * np.eye(4, dtype=complex) / 4.0


def partial_trace_a(mat: np.ndarray) -> np.ndarray:
    reshaped = mat.reshape(2, 2, 2, 2)
    out = np.zeros((2, 2), dtype=complex)
    for a in range(2):
        out += reshaped[a, :, a, :]
    return out


def partial_transpose_a(mat: np.ndarray) -> np.ndarray:
    reshaped = mat.reshape(2, 2, 2, 2)
    return reshaped.transpose(2, 1, 0, 3).reshape(4, 4)


def werner_assemblage(p: float, axes=None):
    if axes is None:
        axes = PAULI
    rho = werner_state(p)
    assemblage = {}
    for k, axis in enumerate(axes):
        for outcome in (+1, -1):
            projector = (I2 + outcome * axis) / 2.0
            subnormalized = partial_trace_a(np.kron(projector, I2) @ rho)
            assemblage[(k, outcome)] = subnormalized
    return assemblage


def closed_form_assemblage(p: float, axis: np.ndarray, outcome: int) -> np.ndarray:
    return (I2 - outcome * p * axis) / 4.0


def three_setting_steering_witness(p: float) -> float:
    # CJWR-type orthogonal 3-setting linear witness normalized to LHS bound 1.
    # For the singlet Werner family, each aligned correlation contributes p in magnitude.
    return math.sqrt(3.0) * p


def chsh_max_werner(p: float) -> float:
    return 2.0 * math.sqrt(2.0) * p


def assemblage_linear_rank(number_of_axes: int):
    # Trace-one two-qubit Hermitian states have 15 real perturbation directions.
    basis_single = [I2, X, Y, Z]
    perturbation_basis = []
    for mu in range(4):
        for nu in range(4):
            if mu == 0 and nu == 0:
                continue
            perturbation_basis.append(np.kron(basis_single[mu], basis_single[nu]) / 4.0)

    axes = PAULI[:number_of_axes]
    columns = []
    for delta in perturbation_basis:
        coords = []
        for axis in axes:
            for outcome in (+1, -1):
                projector = (I2 + outcome * axis) / 2.0
                sigma = partial_trace_a(np.kron(projector, I2) @ delta)
                coords.extend([
                    np.trace(sigma).real,
                    np.trace(sigma @ X).real,
                    np.trace(sigma @ Y).real,
                    np.trace(sigma @ Z).real,
                ])
        columns.append(coords)
    matrix = np.asarray(columns, dtype=float).T
    rank = int(np.linalg.matrix_rank(matrix, tol=1e-10))
    return rank, 15 - rank


def reconstruction_from_three_axis_assemblage(assemblage):
    # For known Alice axes X,Y,Z, recover the Bloch data
    # rho = 1/4[I⊗I + r_i sigma_i⊗I + s_j I⊗sigma_j + T_ij sigma_i⊗sigma_j].
    rho_b = assemblage[(0, +1)] + assemblage[(0, -1)]
    s = np.array([np.trace(rho_b @ P).real for P in PAULI])
    r = np.zeros(3)
    T = np.zeros((3, 3))
    for i in range(3):
        diff = assemblage[(i, +1)] - assemblage[(i, -1)]
        r[i] = np.trace(diff).real
        for j, P in enumerate(PAULI):
            T[i, j] = np.trace(diff @ P).real
    return r, s, T


def main():
    thresholds = {
        "entanglement_PPT": 1.0 / 3.0,
        "exact_steering_general_POVM": 1.0 / 2.0,
        "three_setting_linear_witness": 1.0 / math.sqrt(3.0),
        "CHSH_violation": 1.0 / math.sqrt(2.0),
    }

    print("Werner-state thresholds")
    for name, value in thresholds.items():
        print(f"  {name:34s} {value:.12f}")

    for p in (0.30, 0.40, 0.52, 0.58, 0.72, 1.00):
        rho = werner_state(p)
        pt_min = float(np.min(np.linalg.eigvalsh(partial_transpose_a(rho))).real)
        f3 = three_setting_steering_witness(p)
        chsh = chsh_max_werner(p)
        print(
            f"p={p:.2f}  PT_min={pt_min:+.8f}  "
            f"F3={f3:.8f}  CHSHmax={chsh:.8f}"
        )

    print("\nAssemblage closed-form check")
    for p in (0.0, 0.5, 1.0):
        assemblage = werner_assemblage(p)
        err = 0.0
        for i, axis in enumerate(PAULI):
            for outcome in (+1, -1):
                err = max(
                    err,
                    float(np.max(np.abs(
                        assemblage[(i, outcome)]
                        - closed_form_assemblage(p, axis, outcome)
                    ))),
                )
        print(f"  p={p:.1f} max_error={err:.3e}")

    print("\nPauli-axis assemblage identifiability ranks")
    for n in (1, 2, 3):
        rank, kernel_dim = assemblage_linear_rank(n)
        print(f"  axes={n}: rank={rank}, kernel_dim={kernel_dim}")

    p = 0.63
    assemblage = werner_assemblage(p)
    r, s, T = reconstruction_from_three_axis_assemblage(assemblage)
    print("\nWerner reconstruction control at p=0.63")
    print("  r =", r)
    print("  s =", s)
    print("  T =")
    print(T)


if __name__ == "__main__":
    main()
