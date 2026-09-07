#!/usr/bin/env python3
"""Finite control calculations for DSD QM/QFT/QRF interface audits.

Modes:
  dpi       : relative-entropy data-processing witness under dephasing
  recovery  : exact recovery witness for a product ancilla under partial trace
  modular   : finite-dimensional modular-flow phase witness
  qrf       : finite Z2 relational quantum-reference-frame coordinate transform
  all       : run every control

These are finite diagnostic controls. They do not derive quantum theory from DSD.
"""

import argparse
import math
import numpy as np


def hermitian_log(mat: np.ndarray) -> np.ndarray:
    vals, vecs = np.linalg.eigh((mat + mat.conj().T) / 2)
    if np.any(vals < -1e-12):
        raise ValueError("matrix has a negative eigenvalue")
    logs = np.array([math.log(v) if v > 1e-12 else 0.0 for v in vals])
    return vecs @ np.diag(logs) @ vecs.conj().T


def qrel(rho: np.ndarray, sigma: np.ndarray) -> float:
    vals_r, _ = np.linalg.eigh((rho + rho.conj().T) / 2)
    tr_r_log_r = sum(float(v * math.log(v)) for v in vals_r if v > 1e-12)
    log_sigma = hermitian_log(sigma)
    return float(tr_r_log_r - np.real(np.trace(rho @ log_sigma)))


def run_dpi() -> None:
    eye = np.eye(2, dtype=complex)
    plus = np.array([1.0, 1.0], dtype=complex) / math.sqrt(2)
    rho = np.outer(plus, plus.conj())
    sigma = eye / 2
    rho_d = np.diag(np.diag(rho))
    sigma_d = np.diag(np.diag(sigma))

    before = qrel(rho, sigma)
    after = qrel(rho_d, sigma_d)

    print("[DPI CONTROL]")
    print(f"D(rho||sigma) before = {before:.15f}")
    print(f"D(Nrho||Nsigma) after = {after:.15f}")
    print(f"ln(2) = {math.log(2):.15f}")
    print(f"drop = {before - after:.15f}")


def run_recovery() -> None:
    rho_a = np.diag([0.8, 0.2]).astype(complex)
    sig_a = np.diag([0.5, 0.5]).astype(complex)
    tau_b = np.diag([0.7, 0.3]).astype(complex)

    rho_ab = np.kron(rho_a, tau_b)
    sig_ab = np.kron(sig_a, tau_b)

    d_ab = qrel(rho_ab, sig_ab)
    d_a = qrel(rho_a, sig_a)

    # Recovery map for this model class is R(X)=X tensor tau_b.
    recovered_rho = np.kron(rho_a, tau_b)
    recovered_sig = np.kron(sig_a, tau_b)

    print("[EXACT RECOVERY CONTROL]")
    print(f"D(rho_AB||sigma_AB) = {d_ab:.15f}")
    print(f"D(rho_A||sigma_A)   = {d_a:.15f}")
    print(f"difference          = {d_ab - d_a:.3e}")
    print(f"rho recovery error  = {np.linalg.norm(recovered_rho-rho_ab):.3e}")
    print(f"sig recovery error  = {np.linalg.norm(recovered_sig-sig_ab):.3e}")


def run_modular() -> None:
    p = 0.8
    theta = math.log(p / (1 - p))
    phase = np.exp(1j * theta)

    print("[MODULAR FLOW CONTROL]")
    print("rho = diag(0.8,0.2), A=|0><1|, t=1")
    print(f"ln(p/(1-p)) = {theta:.15f}")
    print(f"phase real   = {phase.real:.15f}")
    print(f"phase imag   = {phase.imag:.15f}")
    print("sigma_t(A) = exp(i t ln 4) A")


def run_qrf() -> None:
    print("[Z2 RELATIONAL FRAME-CHANGE CONTROL]")
    print("A-frame coordinates: (r_B=A xor B, r_C=A xor C)")
    print("B-frame coordinates: (r_A=A xor B, r_C'=B xor C)")
    seen = set()
    for r_b in (0, 1):
        for r_c in (0, 1):
            out = (r_b, r_b ^ r_c)
            seen.add(out)
            print(f"A-frame {(r_b, r_c)} -> B-frame {out}")
    print(f"number of distinct outputs = {len(seen)}")
    print("bijection =", len(seen) == 4)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["dpi", "recovery", "modular", "qrf", "all"], default="all")
    args = parser.parse_args()

    if args.mode in ("dpi", "all"):
        run_dpi()
    if args.mode in ("recovery", "all"):
        run_recovery()
    if args.mode in ("modular", "all"):
        run_modular()
    if args.mode in ("qrf", "all"):
        run_qrf()


if __name__ == "__main__":
    main()
