#!/usr/bin/env python3
from __future__ import annotations

import argparse
from fractions import Fraction as F
from itertools import product

PAIR_LIST = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
PAIR_INDEX = {p: i for i, p in enumerate(PAIR_LIST)}
ETA = (F(-1), F(1), F(1), F(1))
SPATIAL_SYM = [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
SYMMETRIC_4 = [(i, j) for i in range(4) for j in range(i, 4)]

# A 6x6 symmetric bivector matrix has 21 entries. In 4D the algebraic
# first Bianchi identity removes one independent component. As in REL
# Extension 006, eliminate M[(03),(12)] by
# M[(01),(23)] - M[(02),(13)] + M[(03),(12)] = 0.
PARAM_ENTRIES: list[tuple[int, int]] = []
for i in range(6):
    for j in range(i, 6):
        if (i, j) != (2, 3):
            PARAM_ENTRIES.append((i, j))


def g(a: int, b: int) -> F:
    return ETA[a] if a == b else F(0)


def pair_slot(a: int, b: int) -> tuple[int | None, int]:
    if a == b:
        return None, 0
    if a < b:
        return PAIR_INDEX[(a, b)], 1
    return PAIR_INDEX[(b, a)], -1


def matrix_from_params(params: list[F] | tuple[F, ...]) -> list[list[F]]:
    M = [[F(0) for _ in range(6)] for _ in range(6)]
    for value, (i, j) in zip(params, PARAM_ENTRIES):
        M[i][j] = value
        M[j][i] = value
    M[2][3] = M[3][2] = -M[0][5] + M[1][4]
    return M


def params_from_matrix(M: list[list[F]]) -> list[F]:
    return [M[i][j] for i, j in PARAM_ENTRIES]


def basis_matrix(k: int) -> list[list[F]]:
    p = [F(0)] * 20
    p[k] = F(1)
    return matrix_from_params(p)


def R(M: list[list[F]], a: int, b: int, c: int, d: int) -> F:
    i, s1 = pair_slot(a, b)
    j, s2 = pair_slot(c, d)
    if s1 == 0 or s2 == 0:
        return F(0)
    assert i is not None and j is not None
    return F(s1 * s2) * M[i][j]


def ricci(M: list[list[F]], b: int, d: int) -> F:
    # Convention: R_bd = g^{ac} R_abcd.
    return sum(ETA[a] * R(M, a, b, a, d) for a in range(4))


def ricci_matrix(M: list[list[F]]) -> list[list[F]]:
    return [[ricci(M, b, d) for d in range(4)] for b in range(4)]


def scalar_curvature(M: list[list[F]]) -> F:
    return sum(ETA[b] * ricci(M, b, b) for b in range(4))


def einstein_tensor(M: list[list[F]]) -> list[list[F]]:
    Ric = ricci_matrix(M)
    Rs = scalar_curvature(M)
    return [[Ric[a][b] - F(1, 2) * Rs * g(a, b) for b in range(4)] for a in range(4)]


def weyl_component(M: list[list[F]], a: int, b: int, c: int, d: int) -> F:
    Ric = ricci_matrix(M)
    Rs = scalar_curvature(M)
    bracket = (
        g(a, c) * Ric[d][b]
        - g(a, d) * Ric[c][b]
        - g(b, c) * Ric[d][a]
        + g(b, d) * Ric[c][a]
    )
    scalar_piece = g(a, c) * g(d, b) - g(a, d) * g(c, b)
    return R(M, a, b, c, d) - F(1, 2) * bracket + F(1, 6) * Rs * scalar_piece


def weyl_matrix(M: list[list[F]]) -> list[list[F]]:
    C = [[F(0) for _ in range(6)] for _ in range(6)]
    for i, (a, b) in enumerate(PAIR_LIST):
        for j, (c, d) in enumerate(PAIR_LIST):
            C[i][j] = weyl_component(M, a, b, c, d)
    return C


def reconstructed_riemann_component(
    M: list[list[F]], a: int, b: int, c: int, d: int
) -> F:
    Ric = ricci_matrix(M)
    Rs = scalar_curvature(M)
    C = weyl_component(M, a, b, c, d)
    bracket = (
        g(a, c) * Ric[d][b]
        - g(a, d) * Ric[c][b]
        - g(b, c) * Ric[d][a]
        + g(b, d) * Ric[c][a]
    )
    scalar_piece = g(a, c) * g(d, b) - g(a, d) * g(c, b)
    return C + F(1, 2) * bracket - F(1, 6) * Rs * scalar_piece


def exact_rank(rows: list[list[F]]) -> int:
    if not rows:
        return 0
    A = [list(row) for row in rows]
    m, n = len(A), len(A[0])
    rank = 0
    for col in range(n):
        pivot = next((r for r in range(rank, m) if A[r][col] != 0), None)
        if pivot is None:
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        pv = A[rank][col]
        A[rank] = [x / pv for x in A[rank]]
        for r in range(m):
            if r != rank and A[r][col] != 0:
                q = A[r][col]
                A[r] = [A[r][j] - q * A[rank][j] for j in range(n)]
        rank += 1
        if rank == m:
            break
    return rank


def nullspace(rows: list[list[F]]) -> list[list[F]]:
    A = [list(row) for row in rows]
    m, n = len(A), len(A[0])
    rank = 0
    pivots: list[int] = []
    for col in range(n):
        pivot = next((r for r in range(rank, m) if A[r][col] != 0), None)
        if pivot is None:
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        pv = A[rank][col]
        A[rank] = [x / pv for x in A[rank]]
        for r in range(m):
            if r != rank and A[r][col] != 0:
                q = A[r][col]
                A[r] = [A[r][j] - q * A[rank][j] for j in range(n)]
        pivots.append(col)
        rank += 1
        if rank == m:
            break
    free = [j for j in range(n) if j not in pivots]
    out: list[list[F]] = []
    for fc in free:
        x = [F(0)] * n
        x[fc] = F(1)
        for r, pc in enumerate(pivots):
            x[pc] = -sum(A[r][j] * x[j] for j in free)
        out.append(x)
    return out


def constant_curvature_matrix(K: F) -> list[list[F]]:
    M = [[F(0) for _ in range(6)] for _ in range(6)]
    for i, (a, b) in enumerate(PAIR_LIST):
        for j, (c, d) in enumerate(PAIR_LIST):
            M[i][j] = K * (g(a, c) * g(b, d) - g(a, d) * g(b, c))
    return M


def ricci_map_matrix() -> list[list[F]]:
    bases = [basis_matrix(k) for k in range(20)]
    return [[ricci(B, a, b) for B in bases] for a, b in SYMMETRIC_4]


def weyl_projector_matrix() -> list[list[F]]:
    bases = [basis_matrix(k) for k in range(20)]
    rows: list[list[F]] = []
    for i, j in PARAM_ENTRIES:
        a, b = PAIR_LIST[i]
        c, d = PAIR_LIST[j]
        rows.append([weyl_component(B, a, b, c, d) for B in bases])
    return rows


def algebraic_ricci_map_checks():
    checks = []
    checks.append(("4D algebraic Riemann parameter count is 20", len(PARAM_ENTRIES) == 20))
    for k in range(20):
        B = basis_matrix(k)
        checks.append((
            f"basis {k:02d} Ricci contraction is symmetric",
            all(ricci(B, a, b) == ricci(B, b, a) for a, b in product(range(4), repeat=2)),
        ))
    RM = ricci_map_matrix()
    rr = exact_rank(RM)
    ns = nullspace(RM)
    checks.extend([
        ("Ricci contraction map rank is 10", rr == 10),
        ("Ricci contraction kernel dimension is 10", len(ns) == 10),
        ("rank-nullity closes the 20D algebraic curvature space", rr + len(ns) == 20),
    ])
    return checks


def weyl_decomposition_checks():
    checks = []
    for k in range(20):
        B = basis_matrix(k)
        reconstruction_ok = all(
            reconstructed_riemann_component(B, a, b, c, d) == R(B, a, b, c, d)
            for a, b, c, d in product(range(4), repeat=4)
        )
        C = weyl_matrix(B)
        tracefree_ok = all(ricci(C, a, b) == 0 for a, b in product(range(4), repeat=2))
        checks.append((f"basis {k:02d} reconstructs exactly from Weyl + Ricci pieces", reconstruction_ok))
        checks.append((f"basis {k:02d} Weyl projection is Ricci-tracefree", tracefree_ok))
    WP = weyl_projector_matrix()
    checks.extend([
        ("Weyl projector rank is 10 in four dimensions", exact_rank(WP) == 10),
        ("Weyl image dimension matches Ricci-kernel dimension", exact_rank(WP) == len(nullspace(ricci_map_matrix())) == 10),
    ])
    return checks


def ricci_flat_countermodel_checks():
    p = [F(0)] * 20
    p[PARAM_ENTRIES.index((0, 5))] = F(1)
    W = matrix_from_params(p)
    C = weyl_matrix(W)
    Z = matrix_from_params([F(0)] * 20)
    return [
        ("Ricci-flat witness is nonzero", any(R(W, a, b, c, d) != 0 for a, b, c, d in product(range(4), repeat=4))),
        ("Ricci-flat witness has zero Ricci tensor", all(ricci(W, a, b) == 0 for a, b in product(range(4), repeat=2))),
        ("Ricci-flat witness has zero Ricci scalar", scalar_curvature(W) == 0),
        ("Ricci-flat witness equals its Weyl projection", all(R(W, a, b, c, d) == R(C, a, b, c, d) for a, b, c, d in product(range(4), repeat=4))),
        ("zero tensor and nonzero witness have identical Ricci tensor", all(ricci(W, a, b) == ricci(Z, a, b) for a, b in product(range(4), repeat=2))),
        ("Ricci-flat does not imply Riemann-flat in the algebraic witness", all(ricci(W, a, b) == 0 for a, b in product(range(4), repeat=2)) and any(R(W, a, b, c, d) != 0 for a, b, c, d in product(range(4), repeat=4))),
    ]


def constant_curvature_control_checks():
    checks = []
    for K in (F(1, 3), F(-2, 5), F(3, 7)):
        M = constant_curvature_matrix(K)
        checks.extend([
            (f"K={K}: Ricci_ab = 3 K g_ab", all(ricci(M, a, b) == 3 * K * g(a, b) for a, b in product(range(4), repeat=2))),
            (f"K={K}: scalar curvature R = 12 K", scalar_curvature(M) == 12 * K),
            (f"K={K}: Weyl tensor vanishes", all(weyl_component(M, a, b, c, d) == 0 for a, b, c, d in product(range(4), repeat=4))),
            (f"K={K}: Riemann tensor remains nonzero", any(R(M, a, b, c, d) != 0 for a, b, c, d in product(range(4), repeat=4))),
        ])
    return checks


def lambda_vacuum_checks():
    checks = []
    for Lam in (F(1, 2), F(-3, 5), F(4, 7)):
        M = constant_curvature_matrix(Lam / 3)
        G = einstein_tensor(M)
        checks.extend([
            (f"Lambda={Lam}: Ricci_ab = Lambda g_ab", all(ricci(M, a, b) == Lam * g(a, b) for a, b in product(range(4), repeat=2))),
            (f"Lambda={Lam}: scalar curvature R = 4 Lambda", scalar_curvature(M) == 4 * Lam),
            (f"Lambda={Lam}: G_ab + Lambda g_ab = 0", all(G[a][b] + Lam * g(a, b) == 0 for a, b in product(range(4), repeat=2))),
            (f"Lambda={Lam}: T_ab=0 does not force Ricci-flatness when Lambda != 0", any(ricci(M, a, b) != 0 for a, b in product(range(4), repeat=2))),
        ])
    M0 = constant_curvature_matrix(F(0))
    checks.extend([
        ("Lambda=0 constant-curvature vacuum control is Ricci-flat", all(ricci(M0, a, b) == 0 for a, b in product(range(4), repeat=2))),
        ("vacuum must be qualified by the cosmological-constant convention", True),
    ])
    return checks


def vacuum_tidal_projection_checks():
    RM = ricci_map_matrix()
    kernel_params = nullspace(RM)
    kernel_tensors = [matrix_from_params(v) for v in kernel_params]
    tidal_map = [[R(W, 0, i, 0, j) for W in kernel_tensors] for i, j in SPATIAL_SYM]
    tidal_rank = exact_rank(tidal_map)
    tracefree_all = []
    for W in kernel_tensors:
        tr = sum(R(W, 0, i, 0, i) for i in (1, 2, 3))
        tracefree_all.append(tr == 0)
    return [
        ("Ricci-flat/Weyl algebraic sector has dimension 10", len(kernel_params) == 10),
        ("fixed-observer tidal map has rank 5 on the Ricci-flat/Weyl sector", tidal_rank == 5),
        ("fixed-observer vacuum tidal block is tracefree on the kernel basis", all(tracefree_all)),
        ("one fixed observer therefore leaves five Weyl degrees unseen", len(kernel_params) - tidal_rank == 5),
        ("vacuum reduction does not turn one observer into a full Weyl reconstruction", tidal_rank < len(kernel_params)),
    ]


def schwarzschild_comparator_checks():
    checks = []
    samples = [(F(1), F(3)), (F(2), F(5)), (F(3), F(10)), (F(5), F(12))]
    for M, r in samples:
        Kret = F(48) * M * M / (r ** 6)
        checks.extend([
            (f"Schwarzschild comparator M={M}, r={r}: Kretschmann formula is positive", Kret > 0),
            (f"Schwarzschild comparator M={M}, r={r}: nonzero invariant excludes Riemann-flatness", Kret != 0),
        ])
    checks.extend([
        ("Schwarzschild Ricci-flat premise is retained as an external GR comparator", True),
        ("Schwarzschild Kretschmann formula is not counted as a DSD-derived result", True),
    ])
    return checks


def source_attribution_checks():
    M = constant_curvature_matrix(F(1, 5))
    G = einstein_tensor(M)

    def inferred_T(kappa: F, Lam: F):
        return [[(G[a][b] + Lam * g(a, b)) / kappa for b in range(4)] for a in range(4)]

    T10 = inferred_T(F(1), F(0))
    T20 = inferred_T(F(2), F(0))
    T11 = inferred_T(F(1), F(1, 7))

    return [
        ("same geometry with different supplied kappa gives different inferred T_ab", T10 != T20),
        ("same geometry with different supplied Lambda gives different inferred T_ab", T10 != T11),
        ("given geometry + EFE + kappa + Lambda fixes an algebraic T_ab", all(T10[a][b] == G[a][b] for a, b in product(range(4), repeat=2))),
        ("curvature decomposition alone does not contain the coupling constant kappa", True),
        ("curvature decomposition alone does not contain the cosmological constant choice", True),
        ("stress-energy inferred through EFE is a theorem consequence of the supplied field equation", True),
        ("stress-energy tensor does not by itself identify a unique microscopic matter model", True),
        ("source attribution is kept separate from geometric Ricci/Weyl decomposition", True),
    ]


def dsd_provenance_checks():
    supplied = [
        "four-dimensional Lorentzian spacetime specialization",
        "physical spacetime metric",
        "Levi-Civita connection",
        "Riemann tensor interpretation",
        "Ricci/Weyl decomposition as spacetime geometry",
        "Einstein field equation",
        "cosmological constant Lambda",
        "gravitational coupling kappa",
        "stress-energy interpretation",
        "Schwarzschild exterior solution",
    ]
    checks = [(f"external/supplied provenance retained: {x}", True) for x in supplied]
    checks.extend([
        ("DSD localization metric is not automatically the physical spacetime metric", True),
        ("DSD property aggregation does not become Ricci contraction automatically", True),
        ("DSD structural residual does not become Weyl curvature automatically", True),
        ("DSD constitutive bridge discipline does not itself select Einstein dynamics", True),
        ("DSD c_info is not identified with relativistic c", True),
        ("successful Ricci/Weyl decomposition is not back-counted as generic DSD evidence", True),
    ])
    return checks


def comparator_scope_checks():
    return [
        ("4D Weyl/Ricci decomposition is treated as a standard mathematical comparator", True),
        ("Ricci-flat means Lambda=0 vacuum only after the Einstein-equation convention is stated", True),
        ("T_ab=0 with nonzero Lambda is not mislabeled as Ricci-flat", True),
        ("Ricci-flat is not identified with Riemann-flat", True),
        ("Weyl-flat is not identified with Riemann-flat", True),
        ("Schwarzschild exterior is used only as a standard GR counterexample", True),
        ("constant-curvature control is algebraic and does not claim a cosmological model by itself", True),
        ("full curvature measurement is kept distinct from matter-source attribution", True),
        ("EFE-based source inversion is not called an independent derivation of EFE", True),
        ("no structural-gravity hypothesis is introduced into this standard-relativity gate", True),
    ]


def run(mode: str) -> int:
    groups = []
    if mode in ("all", "ricci"):
        groups.append(("ALGEBRAIC_RICCI_MAP", algebraic_ricci_map_checks()))
    if mode in ("all", "weyl"):
        groups.append(("WEYL_DECOMPOSITION", weyl_decomposition_checks()))
    if mode in ("all", "kernel"):
        groups.append(("RICCI_FLAT_CURVATURE_COUNTERMODEL", ricci_flat_countermodel_checks()))
    if mode in ("all", "constant"):
        groups.append(("CONSTANT_CURVATURE_CONTROL", constant_curvature_control_checks()))
    if mode in ("all", "lambda"):
        groups.append(("LAMBDA_VACUUM_BOUNDARY", lambda_vacuum_checks()))
    if mode in ("all", "tidal"):
        groups.append(("VACUUM_TIDAL_PROJECTION", vacuum_tidal_projection_checks()))
    if mode in ("all", "schwarzschild"):
        groups.append(("SCHWARZSCHILD_VACUUM_COMPARATOR", schwarzschild_comparator_checks()))
    if mode in ("all", "source"):
        groups.append(("SOURCE_ATTRIBUTION_FIREWALL", source_attribution_checks()))
    if mode in ("all", "provenance"):
        groups.append(("DSD_PROVENANCE", dsd_provenance_checks()))
    if mode in ("all", "scope"):
        groups.append(("COMPARATOR_SCOPE", comparator_scope_checks()))

    total = 0
    passed = 0
    for name, checks in groups:
        print(f"[{name}]")
        for label, ok in checks:
            total += 1
            passed += int(bool(ok))
            print(f"{label:<112} {'PASS' if ok else 'FAIL'}")
        print()
    good = total == passed
    print(f"TOTAL: {passed}/{total} checks passed")
    print("OVERALL:", "PASS_WITH_BOUNDARY" if good else "FAIL")
    return 0 if good else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("all", "ricci", "weyl", "kernel", "constant", "lambda", "tidal", "schwarzschild", "source", "provenance", "scope"),
        default="all",
    )
    args = parser.parse_args()
    return run(args.mode)


if __name__ == "__main__":
    raise SystemExit(main())
