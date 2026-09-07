#!/usr/bin/env python3
"""Finite controls for the 2026-09-07 DSD QM/QFT/QRF expansion batch.

Modes
-----
access : nested-access relative-entropy witness
unruh  : Bisognano-Wichmann/Unruh rescaling control in natural units
qrf    : finite Z2 frame-bijection and coarse-graining fiber control
all    : run all controls

The standard QM/QFT formulas used here are external specialization data.
They are not derived from DSD.
"""

import argparse
import math
import itertools
import numpy as np


def _hermitian_log(mat: np.ndarray) -> np.ndarray:
    vals, vecs = np.linalg.eigh((mat + mat.conj().T) / 2)
    if np.any(vals < -1e-12):
        raise ValueError("matrix has a negative eigenvalue")
    logs = np.array([math.log(v) if v > 1e-15 else 0.0 for v in vals])
    return vecs @ np.diag(logs) @ vecs.conj().T


def relative_entropy(rho: np.ndarray, sigma: np.ndarray) -> float:
    vals = np.linalg.eigvalsh((rho + rho.conj().T) / 2)
    tr_rho_log_rho = sum(float(v * math.log(v)) for v in vals if v > 1e-15)
    return float(tr_rho_log_rho - np.real(np.trace(rho @ _hermitian_log(sigma))))


def run_access() -> None:
    rho_a = np.diag([0.8, 0.2]).astype(complex)
    sigma_a = np.eye(2, dtype=complex) / 2
    rho_b = np.diag([1.0, 0.0]).astype(complex)
    sigma_b = np.eye(2, dtype=complex) / 2

    rho_ab = np.kron(rho_a, rho_b)
    sigma_ab = np.kron(sigma_a, sigma_b)

    d_a = relative_entropy(rho_a, sigma_a)
    d_ab = relative_entropy(rho_ab, sigma_ab)

    print("[NESTED ACCESS / RELATIVE ENTROPY]")
    print(f"D_A  = {d_a:.15f}")
    print(f"D_AB = {d_ab:.15f}")
    print(f"gain = {d_ab - d_a:.15f}")
    print(f"ln2  = {math.log(2):.15f}")
    print("D_AB >= D_A:", d_ab + 1e-12 >= d_a)


def run_unruh(a: float, modular_s: float) -> None:
    # Magnitude convention: eta = 2*pi*s for the wedge modular/boost relation.
    # Overall sign depends on wedge/convention and is not physically used here.
    eta = 2 * math.pi * modular_s
    tau = eta / a
    temperature = a / (2 * math.pi)

    print("[BW / UNRUH SPECIAL-BRIDGE CONTROL]")
    print(f"proper acceleration a = {a:.15f}")
    print(f"modular parameter |s| = {modular_s:.15f}")
    print(f"boost rapidity |eta| = 2*pi*|s| = {eta:.15f}")
    print(f"proper time |tau| = |eta|/a = {tau:.15f}")
    print(f"Unruh T = a/(2*pi) = {temperature:.15f}")
    print(f"a*|tau|/(2*pi) = {a * tau / (2 * math.pi):.15f}")


def run_qrf() -> None:
    mapping = {}
    for r_b, r_c in itertools.product((0, 1), repeat=2):
        mapping[(r_b, r_c)] = (r_b, r_b ^ r_c)

    coarse_fibers = {0: [], 1: []}
    for x, y in mapping.items():
        coarse_fibers[y[0]].append(x)

    print("[QRF BIJECTION / COARSE-GRAINING CONTROL]")
    for x in sorted(mapping):
        print(f"A-frame {x} -> B-frame {mapping[x]}")
    print("bijection:", len(set(mapping.values())) == 4)
    print("coarse readout C(y1,y2)=y1 fibers:")
    for key in sorted(coarse_fibers):
        print(f"  {key}: {coarse_fibers[key]} (size={len(coarse_fibers[key])})")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["access", "unruh", "qrf", "all"], default="all")
    parser.add_argument("--acceleration", type=float, default=2.0)
    parser.add_argument("--modular-s", type=float, default=0.25)
    args = parser.parse_args()

    if args.acceleration <= 0:
        raise ValueError("--acceleration must be positive")

    if args.mode in ("access", "all"):
        run_access()
    if args.mode in ("unruh", "all"):
        run_unruh(args.acceleration, abs(args.modular_s))
    if args.mode in ("qrf", "all"):
        run_qrf()


if __name__ == "__main__":
    main()
