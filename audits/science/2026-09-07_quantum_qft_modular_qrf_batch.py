import numpy as np


def matlog(a):
    vals, vecs = np.linalg.eigh(a)
    return vecs @ np.diag(np.log(vals)) @ vecs.T


def qrel(rho, sigma):
    return float(np.real(np.trace(rho @ (matlog(rho) - matlog(sigma)))) / np.log(2.0))


def dephase_z(rho):
    return np.diag(np.diag(rho))


def modular_hamiltonian(rho):
    return -matlog(rho)


def main():
    rho = np.array([[0.7, 0.2], [0.2, 0.3]], dtype=float)
    sigma = np.array([[0.6, 0.0], [0.0, 0.4]], dtype=float)

    d_before = qrel(rho, sigma)
    d_after = qrel(dephase_z(rho), dephase_z(sigma))

    print("PHY-QM-042 relative-entropy data-processing control")
    print(f"D(rho||sigma)          = {d_before:.15f} bits")
    print(f"D(Delta rho||Delta s)  = {d_after:.15f} bits")
    print(f"loss under dephasing   = {d_before - d_after:.15f} bits")
    print(f"monotonicity respected = {d_after <= d_before + 1e-12}")

    rho1 = np.diag([0.8, 0.2])
    rho2 = np.diag([0.6, 0.4])
    k1 = modular_hamiltonian(rho1)
    k2 = modular_hamiltonian(rho2)
    print("\nPHY-QFT-005 finite faithful-state modular-generator control")
    print("eig K(rho1) =", np.linalg.eigvalsh(k1))
    print("eig K(rho2) =", np.linalg.eigvalsh(k2))
    print("same algebra, different faithful states -> different modular generators:", not np.allclose(k1, k2))

    bell = np.array([1, 0, 0, 1], dtype=float) / np.sqrt(2.0)
    rho_bell = np.outer(bell, bell)
    rho_a = np.array([[rho_bell[0,0]+rho_bell[1,1], rho_bell[0,2]+rho_bell[1,3]],
                      [rho_bell[2,0]+rho_bell[3,1], rho_bell[2,2]+rho_bell[3,3]]])
    vals = np.linalg.eigvalsh(rho_a)
    entropy = -sum(v*np.log2(v) for v in vals if v > 1e-15)
    print("\nPHY-QRF-001 control")
    print(f"Bell-state reduced entropy in supplied A|B factorization = {entropy:.12f} bits")
    print("This number is factorization-relative; the script does not claim a QRF transformation law.")


if __name__ == "__main__":
    main()
