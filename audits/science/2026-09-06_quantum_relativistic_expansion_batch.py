#!/usr/bin/env python3
"""
DSD quantum-relativistic expansion batch controls.

Covers:
- correlated environment synergy/redundancy
- conditional mutual information / Markov sufficiency
- no-cloning vs pointer-basis copying
- three-qubit bit-flip error correction
- dephasing pointer basis selection
- Wigner-friend-style local/global distinguishability
- local CPTP no-signalling control

Dependencies: numpy only.
"""

from __future__ import annotations
import argparse
import itertools
import math
from collections import Counter
import numpy as np

ZERO = np.array([1.0, 0.0], dtype=complex)
ONE = np.array([0.0, 1.0], dtype=complex)
PLUS = (ZERO + ONE) / math.sqrt(2.0)

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)

def H_probs(vals):
    vals = np.asarray(vals, dtype=float)
    vals = vals[vals > 1e-15]
    return float(-(vals * np.log2(vals)).sum())

def entropy_counter(dist):
    return H_probs(list(dist.values()))

def mutual_information(joint):
    A, B = Counter(), Counter()
    for (a, b), p in joint.items():
        A[a] += p
        B[b] += p
    total = 0.0
    for (a, b), p in joint.items():
        if p > 0:
            total += p * math.log2(p / (A[a] * B[b]))
    return total

def marginal(data, inds):
    out = Counter()
    for vals, p in data.items():
        key = tuple(vals[i] for i in inds)
        if len(key) == 1:
            key = key[0]
        out[key] += p
    return out

def mi_from_triples(data, Ainds, Binds):
    joint = Counter()
    for vals, p in data.items():
        a = tuple(vals[i] for i in Ainds)
        b = tuple(vals[i] for i in Binds)
        if len(a) == 1:
            a = a[0]
        if len(b) == 1:
            b = b[0]
        joint[(a, b)] += p
    return mutual_information(joint)

def cmi_ABC(data):
    return (
        entropy_counter(marginal(data, [0, 1]))
        + entropy_counter(marginal(data, [1, 2]))
        - entropy_counter(marginal(data, [1]))
        - entropy_counter(marginal(data, [0, 1, 2]))
    )

def trace_distance(rho, sigma):
    vals = np.linalg.eigvalsh(rho - sigma)
    return float(0.5 * np.sum(np.abs(vals)))

def partial_trace_A(rho):
    R = rho.reshape(2, 2, 2, 2)
    return np.einsum("abad->bd", R)

def correlated_environment():
    parity = Counter()
    for e1, e2 in itertools.product([0, 1], repeat=2):
        parity[(e1 ^ e2, e1, e2)] += 0.25

    duplicate = Counter()
    for s in [0, 1]:
        duplicate[(s, s, s)] += 0.5

    print("=== Correlated environment ===")
    print("Parity synergy:")
    print("I(S:E1)   =", mi_from_triples(parity, [0], [1]))
    print("I(S:E2)   =", mi_from_triples(parity, [0], [2]))
    print("I(S:E1E2) =", mi_from_triples(parity, [0], [1, 2]))
    print("I(S:E2|E1)=", cmi_ABC(parity))

    print("Duplicate redundancy:")
    print("I(S:E1)   =", mi_from_triples(duplicate, [0], [1]))
    print("I(S:E2)   =", mi_from_triples(duplicate, [0], [2]))
    print("I(S:E1E2) =", mi_from_triples(duplicate, [0], [1, 2]))
    print("I(S:E2|E1)=", cmi_ABC(duplicate))

def markov_control(q=0.2, r=0.3):
    data = Counter()
    for s in [0, 1]:
        for n1, p1 in [(0, 1-q), (1, q)]:
            b = s ^ n1
            for n2, p2 in [(0, 1-r), (1, r)]:
                c = b ^ n2
                data[(s, b, c)] += 0.5 * p1 * p2
    print("=== Markov control S->B->C ===")
    print("q =", q, "r =", r)
    print("I(S:B)    =", mi_from_triples(data, [0], [1]))
    print("I(S:C)    =", mi_from_triples(data, [0], [2]))
    print("I(S:C|B)  =", cmi_ABC(data))

def no_cloning_control():
    CNOT = np.array(
        [[1,0,0,0],
         [0,1,0,0],
         [0,0,0,1],
         [0,0,1,0]], dtype=complex
    )
    psi_out = CNOT @ np.kron(PLUS, ZERO)
    desired = np.kron(PLUS, PLUS)
    fidelity = abs(np.vdot(desired, psi_out))**2
    print("=== No-cloning control ===")
    print("CNOT(|+>|0>) =", psi_out)
    print("Fidelity with |+>|+> =", float(fidelity))
    print("Classical pointer basis controls:")
    print("CNOT(|0>|0>) exact copy =", np.allclose(CNOT @ np.kron(ZERO,ZERO), np.kron(ZERO,ZERO)))
    print("CNOT(|1>|0>) exact copy =", np.allclose(CNOT @ np.kron(ONE,ZERO), np.kron(ONE,ONE)))

def qec_bitflip():
    alpha = 0.6 + 0.2j
    beta = 0.3 - 0.7j
    norm = math.sqrt(abs(alpha)**2 + abs(beta)**2)
    alpha, beta = alpha/norm, beta/norm
    enc = np.zeros(8, dtype=complex)
    enc[0], enc[7] = alpha, beta

    def k3(a,b,c):
        return np.kron(np.kron(a,b),c)

    S1, S2 = k3(Z,Z,I2), k3(I2,Z,Z)
    errors = [np.eye(8), k3(X,I2,I2), k3(I2,X,I2), k3(I2,I2,X)]
    labels = ["I", "X1", "X2", "X3"]

    print("=== 3-qubit bit-flip QEC ===")
    for lab, E in zip(labels, errors):
        damaged = E @ enc
        synd = (
            int(round(np.vdot(damaged, S1 @ damaged).real)),
            int(round(np.vdot(damaged, S2 @ damaged).real)),
        )
        recovered = E @ damaged if lab != "I" else damaged
        fidelity = abs(np.vdot(enc, recovered))**2
        print(lab, "syndrome", synd, "recovery fidelity", float(fidelity))

def dephasing_pointer(gamma=0.3):
    def dephase(rho):
        out = rho.copy()
        out[0,1] *= gamma
        out[1,0] *= gamma
        return out
    rho0 = np.outer(ZERO, ZERO.conj())
    rhop = np.outer(PLUS, PLUS.conj())
    print("=== Dephasing / pointer control ===")
    print("gamma =", gamma)
    print("D(|0>, E(|0>)) =", trace_distance(rho0, dephase(rho0)))
    print("D(|+>, E(|+>)) =", trace_distance(rhop, dephase(rhop)))
    print("Expected latter =", abs(1-gamma)/2)
    print("Pauli transfer eigenvalues: I->1, Z->1, X->gamma, Y->gamma")

def wigner_friend_control():
    phi = (np.kron(ZERO,ZERO) + np.kron(ONE,ONE))/math.sqrt(2.0)
    rho_pure = np.outer(phi, phi.conj())
    ket00 = np.kron(ZERO,ZERO)
    ket11 = np.kron(ONE,ONE)
    rho_mix = 0.5*np.outer(ket00,ket00.conj()) + 0.5*np.outer(ket11,ket11.conj())
    rhoF_pure = partial_trace_A(rho_pure)
    rhoF_mix = partial_trace_A(rho_mix)

    phi_minus = (ket00-ket11)/math.sqrt(2.0)
    Pplus = np.outer(phi,phi.conj())
    Pminus = np.outer(phi_minus,phi_minus.conj())
    p_pure = [np.trace(P @ rho_pure).real for P in [Pplus,Pminus]]
    p_mix = [np.trace(P @ rho_mix).real for P in [Pplus,Pminus]]

    print("=== Wigner-friend-style local/global control ===")
    print("local trace distance =", trace_distance(rhoF_pure, rhoF_mix))
    print("global trace distance =", trace_distance(rho_pure, rho_mix))
    print("Bell-coherence test pure [Phi+,Phi-] =", p_pure)
    print("Bell-coherence test mix  [Phi+,Phi-] =", p_mix)

def local_cptp_no_signal(gamma=0.4):
    phi = (np.kron(ZERO,ZERO) + np.kron(ONE,ONE))/math.sqrt(2.0)
    rho = np.outer(phi,phi.conj())
    K0 = np.array([[1,0],[0,math.sqrt(1-gamma)]],dtype=complex)
    K1 = np.array([[0,math.sqrt(gamma)],[0,0]],dtype=complex)
    out = np.zeros_like(rho)
    for K in [K0,K1]:
        M=np.kron(K,I2)
        out += M @ rho @ M.conj().T
    rhoB_before=partial_trace_A(rho)
    rhoB_after=partial_trace_A(out)
    print("=== Local CPTP no-signalling control ===")
    print("gamma =", gamma)
    print("Bob reduced state before:\n", rhoB_before)
    print("Bob reduced state after:\n", rhoB_after)
    print("trace distance =", trace_distance(rhoB_before,rhoB_after))

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--mode", default="all",
                   choices=["all","correlated","markov","cloning","qec","pointer","wigner","nosignal"])
    p.add_argument("--q", type=float, default=0.2)
    p.add_argument("--r", type=float, default=0.3)
    p.add_argument("--gamma", type=float, default=0.3)
    args=p.parse_args()
    if args.mode in ("all","correlated"): correlated_environment()
    if args.mode in ("all","markov"): markov_control(args.q,args.r)
    if args.mode in ("all","cloning"): no_cloning_control()
    if args.mode in ("all","qec"): qec_bitflip()
    if args.mode in ("all","pointer"): dephasing_pointer(args.gamma)
    if args.mode in ("all","wigner"): wigner_friend_control()
    if args.mode in ("all","nosignal"): local_cptp_no_signal(args.gamma)

if __name__ == "__main__":
    main()
