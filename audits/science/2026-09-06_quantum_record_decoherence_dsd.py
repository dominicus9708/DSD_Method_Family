import argparse
import math
import numpy as np

I2 = np.eye(2, dtype=complex)
KET0 = np.array([1.0, 0.0], dtype=complex)
KET1 = np.array([0.0, 1.0], dtype=complex)
KETP = (KET0 + KET1) / math.sqrt(2.0)
KETM = (KET0 - KET1) / math.sqrt(2.0)
P0 = np.outer(KET0, KET0.conj())
P1 = np.outer(KET1, KET1.conj())
PP = np.outer(KETP, KETP.conj())
PM = np.outer(KETM, KETM.conj())

PHI = (np.kron(KET0, KET0) + np.kron(KET1, KET1)) / math.sqrt(2.0)
RHO_COH = np.outer(PHI, PHI.conj())
RHO_DEPH = sum(
    np.kron(I2, p) @ RHO_COH @ np.kron(I2, p)
    for p in (P0, P1)
)

CNOT_SR = np.array(
    [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
    ],
    dtype=complex,
)
TARGET_PREMEASUREMENT = np.kron(KETP, KET0)


def ptrace_second(rho, d_a=2, d_b=2):
    reshaped = rho.reshape(d_a, d_b, d_a, d_b)
    return np.einsum("abcb->ac", reshaped)


def ptrace_first(rho, d_a=2, d_b=2):
    reshaped = rho.reshape(d_a, d_b, d_a, d_b)
    return np.einsum("abad->bd", reshaped)


def entropy_bits(rho):
    vals = np.linalg.eigvalsh(rho).real
    vals = vals[vals > 1e-15]
    return float(-np.sum(vals * np.log2(vals)))


def mutual_information_sr(rho):
    rho_s = ptrace_second(rho)
    rho_r = ptrace_first(rho)
    return entropy_bits(rho_s) + entropy_bits(rho_r) - entropy_bits(rho)


def trace_distance(rho, sigma):
    vals = np.linalg.eigvalsh(rho - sigma)
    return float(0.5 * np.sum(np.abs(vals)))


def inverse_measurement_recovery_fidelity(rho):
    out = CNOT_SR @ rho @ CNOT_SR.conj().T
    return float(np.real(TARGET_PREMEASUREMENT.conj() @ out @ TARGET_PREMEASUREMENT))


def conditional_s_after_rx(rho, projector):
    measurement = np.kron(I2, projector)
    post = measurement @ rho @ measurement
    probability = float(np.trace(post).real)
    rho_s = ptrace_second(post) / probability
    return probability, rho_s


def ptrace_three(rho, keep):
    dims = [2, 2, 2]
    arr = rho.reshape(dims + dims)
    n = 3
    for i in sorted([j for j in range(3) if j not in keep], reverse=True):
        arr = np.trace(arr, axis1=i, axis2=i + n)
        n -= 1
    d_keep = int(np.prod([dims[i] for i in keep]))
    return arr.reshape(d_keep, d_keep)


def swap_record_environment():
    psi_sre = np.kron(PHI, KET0)
    rho_sre = np.outer(psi_sre, psi_sre.conj())
    swap_re = np.zeros((8, 8), dtype=complex)
    for s in range(2):
        for r in range(2):
            for e in range(2):
                i = 4 * s + 2 * r + e
                j = 4 * s + 2 * e + r
                swap_re[j, i] = 1.0
    rho_transfer = swap_re @ rho_sre @ swap_re.conj().T
    rho_back = swap_re @ rho_transfer @ swap_re.conj().T
    reversal_fidelity = float(np.real(psi_sre.conj() @ rho_back @ psi_sre))
    return rho_transfer, reversal_fidelity


def mutual_information_three(rho, a, b):
    rho_a = ptrace_three(rho, [a])
    rho_b = ptrace_three(rho, [b])
    rho_ab = ptrace_three(rho, sorted([a, b]))
    return entropy_bits(rho_a) + entropy_bits(rho_b) - entropy_bits(rho_ab)


def gamma_state(gamma):
    g = complex(gamma)
    return np.array(
        [
            [0.5, 0.0, 0.0, g / 2.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [np.conjugate(g) / 2.0, 0.0, 0.0, 0.5],
        ],
        dtype=complex,
    )


def run_core():
    print("Coherent unread carrier vs dephased carrier")
    for name, rho in (("coherent", RHO_COH), ("dephased", RHO_DEPH)):
        rho_s = ptrace_second(rho)
        rho_r = ptrace_first(rho)
        print(
            f"  {name:10s} S(S)={entropy_bits(rho_s):.12f} "
            f"S(R)={entropy_bits(rho_r):.12f} "
            f"I(S:R)={mutual_information_sr(rho):.12f} "
            f"F_recover={inverse_measurement_recovery_fidelity(rho):.12f}"
        )
        for label, projector in (("+", PP), ("-", PM)):
            prob, rho_s_cond = conditional_s_after_rx(rho, projector)
            print(
                f"    R_X={label} prob={prob:.12f} "
                f"conditional_S_coherence={abs(rho_s_cond[0,1]):.12f}"
            )

    print("\nDescriptor collision")
    print(
        f"  trace_distance(full coherent, dephased)={trace_distance(RHO_COH, RHO_DEPH):.12f}"
    )
    print(
        f"  trace_distance(S marginals)={trace_distance(ptrace_second(RHO_COH), ptrace_second(RHO_DEPH)):.12f}"
    )
    print(
        f"  trace_distance(R marginals)={trace_distance(ptrace_first(RHO_COH), ptrace_first(RHO_DEPH)):.12f}"
    )

    rho_transfer, reversal_fidelity = swap_record_environment()
    print("\nLocal record reset by reversible transfer to environment")
    print(f"  I(S:R)={mutual_information_three(rho_transfer, 0, 1):.12f}")
    print(f"  I(S:E)={mutual_information_three(rho_transfer, 0, 2):.12f}")
    print(f"  reversal_fidelity={reversal_fidelity:.12f}")
    print("  rho_R=")
    print(np.real_if_close(ptrace_three(rho_transfer, [1])))


def run_gamma(values):
    print("gamma-family decoherence diagnostics")
    print("gamma visibility distinguishability F_recover I(S:R)")
    for gamma in values:
        if gamma < 0.0 or gamma > 1.0:
            raise ValueError("gamma must lie in [0,1] for this real-overlap control")
        rho = gamma_state(gamma)
        visibility = abs(gamma)
        distinguishability = math.sqrt(max(0.0, 1.0 - visibility**2))
        recovery = inverse_measurement_recovery_fidelity(rho)
        info = mutual_information_sr(rho)
        print(
            f"{gamma:.6f} {visibility:.12f} {distinguishability:.12f} "
            f"{recovery:.12f} {info:.12f}"
        )


def main():
    parser = argparse.ArgumentParser(
        description="Finite DSD audit controls for unread records, dephasing, environment transfer, and recovery."
    )
    parser.add_argument(
        "--mode", choices=("all", "core", "gamma"), default="all"
    )
    parser.add_argument(
        "--gamma",
        type=float,
        nargs="*",
        default=[1.0, 0.8, 0.5, 0.2, 0.0],
        help="Real environment-overlap controls in [0,1].",
    )
    args = parser.parse_args()

    if args.mode in ("all", "core"):
        run_core()
    if args.mode in ("all", "gamma"):
        if args.mode == "all":
            print()
        run_gamma(args.gamma)


if __name__ == "__main__":
    main()
