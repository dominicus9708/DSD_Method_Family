import math
import numpy as np

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)

PX = {+1: (I2 + X) / 2.0, -1: (I2 - X) / 2.0}
PZ = {+1: (I2 + Z) / 2.0, -1: (I2 - Z) / 2.0}

KET0 = np.array([1.0, 0.0], dtype=complex)
RHO0 = np.outer(KET0, KET0.conj())
KET_PLUS = np.array([1.0, 1.0], dtype=complex) / math.sqrt(2.0)
KET_MINUS = np.array([1.0, -1.0], dtype=complex) / math.sqrt(2.0)
RHO_PLUS = np.outer(KET_PLUS, KET_PLUS.conj())
RHO_MINUS = np.outer(KET_MINUS, KET_MINUS.conj())


def lueders(projector, rho):
    return projector @ rho @ projector


def sequential_projective(first, second, rho):
    joint = {}
    final_unconditional = np.zeros((2, 2), dtype=complex)
    for a, pa in first.items():
        rho_a = lueders(pa, rho)
        for b, pb in second.items():
            rho_ab = lueders(pb, rho_a)
            joint[(a, b)] = float(np.trace(rho_ab).real)
            final_unconditional += rho_ab
    return joint, final_unconditional


def z_lueders_instrument(outcome, rho):
    return lueders(PZ[outcome], rho)


def z_measure_reprepare_x_instrument(outcome, rho):
    probability = float(np.trace(PZ[outcome] @ rho).real)
    prepared = RHO_PLUS if outcome == +1 else RHO_MINUS
    return probability * prepared


def sequential_instrument_then_x(instrument, rho):
    joint = {}
    for z in (+1, -1):
        rho_z = instrument(z, rho)
        for x, px in PX.items():
            rho_zx = lueders(px, rho_z)
            joint[(z, x)] = float(np.trace(rho_zx).real)
    return joint


def adaptive_protocol(rho):
    # Step 1: X measurement.
    # Step 2 policy: if first outcome is +1, measure Z; if -1, measure X again.
    history = {}
    final_unconditional = np.zeros((2, 2), dtype=complex)
    for a, pa in PX.items():
        rho_a = lueders(pa, rho)
        second_name = "Z" if a == +1 else "X"
        second = PZ if a == +1 else PX
        for b, pb in second.items():
            rho_ab = lueders(pb, rho_a)
            history[(a, second_name, b)] = float(np.trace(rho_ab).real)
            final_unconditional += rho_ab
    return history, final_unconditional


def print_joint(title, table):
    print(title)
    for key in sorted(table, key=str):
        print(f"  {key}: {table[key]:.12f}")


def main():
    print("=== PHY-QM-014: order-sensitive sequential projective measurements ===")
    xz_joint, xz_final = sequential_projective(PX, PZ, RHO0)
    zx_joint, zx_final = sequential_projective(PZ, PX, RHO0)
    print_joint("X -> Z joint distribution", xz_joint)
    print_joint("Z -> X joint distribution", zx_joint)
    print("final state X->Z")
    print(xz_final)
    print("final state Z->X")
    print(zx_final)
    print("final-state max difference:", np.max(np.abs(xz_final - zx_final)))
    print("joint-table L1 distance:", sum(abs(xz_joint[k] - zx_joint[k]) for k in xz_joint))

    print("\n=== PHY-QM-015: same POVM, different instruments ===")
    pz = {z: float(np.trace(PZ[z] @ RHO0).real) for z in (+1, -1)}
    print("first-step Z POVM probabilities:", pz)
    luders_joint = sequential_instrument_then_x(z_lueders_instrument, RHO0)
    reprepare_joint = sequential_instrument_then_x(z_measure_reprepare_x_instrument, RHO0)
    print_joint("Lueders Z instrument -> X", luders_joint)
    print_joint("measure-Z/reprepare-X instrument -> X", reprepare_joint)
    print(
        "sequential-table L1 distance:",
        sum(abs(lueders_joint[k] - reprepare_joint[k]) for k in luders_joint),
    )

    print("\n=== PHY-QM-016: adaptive protocol tree ===")
    history, final_state = adaptive_protocol(RHO0)
    print_joint("adaptive histories", history)
    print("history probability sum:", sum(history.values()))
    print("adaptive unconditional final state")
    print(final_state)


if __name__ == "__main__":
    main()
