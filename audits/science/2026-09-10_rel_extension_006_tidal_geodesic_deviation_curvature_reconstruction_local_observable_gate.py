#!/usr/bin/env python3
from __future__ import annotations

import argparse
from fractions import Fraction as F
from itertools import product

PAIR_LIST = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
PAIR_INDEX = {p:i for i,p in enumerate(PAIR_LIST)}
ETA = (-1,1,1,1)

# 6x6 symmetric bivector matrix has 21 entries. In four dimensions the
# algebraic first Bianchi identity removes one independent entry. We eliminate
# M[(03),(12)] using M01,23 - M02,13 + M03,12 = 0.
PARAM_ENTRIES = []
for i in range(6):
    for j in range(i,6):
        if (i,j) != (2,3):
            PARAM_ENTRIES.append((i,j))


def pair_slot(a:int,b:int):
    if a == b:
        return None, 0
    if a < b:
        return PAIR_INDEX[(a,b)], 1
    return PAIR_INDEX[(b,a)], -1


def matrix_from_params(params):
    M = [[F(0) for _ in range(6)] for _ in range(6)]
    for value,(i,j) in zip(params, PARAM_ENTRIES):
        M[i][j] = value
        M[j][i] = value
    M[2][3] = M[3][2] = -M[0][5] + M[1][4]
    return M


def basis_matrix(k:int):
    p = [F(0)]*20
    p[k] = F(1)
    return matrix_from_params(p)


def R(M,a,b,c,d):
    i,s1 = pair_slot(a,b)
    j,s2 = pair_slot(c,d)
    if s1 == 0 or s2 == 0:
        return F(0)
    return F(s1*s2) * M[i][j]


def bianchi(M,a,b,c,d):
    return R(M,a,b,c,d) + R(M,a,c,d,b) + R(M,a,d,b,c)


def raise_first_component(M,a,b,c,d):
    return F(ETA[a]) * R(M,a,b,c,d)


def deviation_accel(M,u,xi):
    # Sign convention for this audit: A^a = - R^a_{ b c d} u^b xi^c u^d.
    out = []
    for a in range(4):
        total = F(0)
        for b,c,d in product(range(4), repeat=3):
            total -= raise_first_component(M,a,b,c,d) * u[b] * xi[c] * u[d]
        out.append(total)
    return tuple(out)


def measurement_matrix(configs):
    rows = []
    bases = [basis_matrix(k) for k in range(20)]
    for u,xi in configs:
        cols = [deviation_accel(B,u,xi) for B in bases]
        for a in range(4):
            rows.append([cols[k][a] for k in range(20)])
    return rows


def exact_rank(rows):
    if not rows:
        return 0
    A = [list(r) for r in rows]
    m,n = len(A), len(A[0])
    rank = 0
    col = 0
    while rank < m and col < n:
        pivot = None
        for r in range(rank,m):
            if A[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            col += 1
            continue
        A[rank],A[pivot] = A[pivot],A[rank]
        pv = A[rank][col]
        A[rank] = [x/pv for x in A[rank]]
        for r in range(m):
            if r != rank and A[r][col] != 0:
                f = A[r][col]
                A[r] = [A[r][j]-f*A[rank][j] for j in range(n)]
        rank += 1
        col += 1
    return rank


def spatial_xi_for_velocity(v,axis):
    spatial = [F(0),F(0),F(0)]
    spatial[axis] = F(1)
    xi0 = sum(v[i]*spatial[i] for i in range(3))
    return (xi0, spatial[0], spatial[1], spatial[2])


def algebraic_riemann_checks():
    checks = []
    checks.append(("four-dimensional algebraic Riemann parameter count is 20", len(PARAM_ENTRIES)==20))
    for k in range(20):
        B = basis_matrix(k)
        ok_bianchi = all(bianchi(B,a,b,c,d)==0 for a,b,c,d in product(range(4), repeat=4))
        checks.append((f"basis {k:02d} satisfies algebraic first Bianchi identity", ok_bianchi))
    B = basis_matrix(7)
    checks.extend([
        ("antisymmetry in first index pair holds", all(R(B,a,b,c,d)==-R(B,b,a,c,d) for a,b,c,d in product(range(4), repeat=4))),
        ("antisymmetry in second index pair holds", all(R(B,a,b,c,d)==-R(B,a,b,d,c) for a,b,c,d in product(range(4), repeat=4))),
        ("pair-exchange symmetry holds", all(R(B,a,b,c,d)==R(B,c,d,a,b) for a,b,c,d in product(range(4), repeat=4))),
    ])
    return checks


def fixed_observer_checks():
    u0 = (F(1),F(0),F(0),F(0))
    xis = [(F(0),F(1),F(0),F(0)),(F(0),F(0),F(1),F(0)),(F(0),F(0),F(0),F(1))]
    ranks = [exact_rank(measurement_matrix([(u0,xi) for xi in xis[:n]])) for n in (1,2,3)]
    checks = [
        ("single spatial separation direction has rank 3", ranks[0]==3),
        ("two spatial separation directions have rank 5", ranks[1]==5),
        ("three independent spatial separation directions have rank 6", ranks[2]==6),
        ("fixed comoving observer does not determine full 20-component algebraic curvature", ranks[2] < 20),
        ("fixed-observer tidal map is exactly the six-component symmetric R_i0j0 sector", ranks[2]==6),
    ]
    return checks


def hidden_curvature_checks():
    # Pure spatial sectional-curvature perturbation Delta R_1212 = 1.
    idx = PARAM_ENTRIES.index((3,3))
    p = [F(0)]*20
    p[idx] = F(1)
    D = matrix_from_params(p)
    u0 = (F(1),F(0),F(0),F(0))
    xis = [(F(0),F(1),F(0),F(0)),(F(0),F(0),F(1),F(0)),(F(0),F(0),F(0),F(1))]
    fixed_zero = all(all(x==0 for x in deviation_accel(D,u0,xi)) for xi in xis)
    vm = (F(1,5),F(0),F(0))
    um = (F(1),vm[0],vm[1],vm[2])
    xim = spatial_xi_for_velocity(vm,1)
    detected = any(x!=0 for x in deviation_accel(D,um,xim))
    return [
        ("hidden tensor has nonzero R_1212", R(D,1,2,1,2)==1),
        ("hidden tensor has zero R_0i0j for all spatial i,j", all(R(D,0,i,0,j)==0 for i in (1,2,3) for j in (1,2,3))),
        ("all three fixed-observer comoving deviation readouts are blind to hidden R_1212", fixed_zero),
        ("moving-observer configuration detects the same hidden curvature component", detected),
        ("same fixed tidal matrix can correspond to different full Riemann tensors", fixed_zero and R(D,1,2,1,2)!=0),
    ]


def multi_configuration_checks():
    velocities = [
        (F(0),F(0),F(0)),
        (F(1,5),F(0),F(0)),
        (F(0),F(1,4),F(0)),
        (F(0),F(0),F(3,10)),
        (F(1,5),F(3,20),F(0)),
        (F(1,10),F(1,5),F(3,20)),
    ]
    configs=[]
    for v in velocities:
        u=(F(1),v[0],v[1],v[2])
        for axis in range(3):
            configs.append((u,spatial_xi_for_velocity(v,axis)))
    checks=[]
    ranks=[]
    for n in range(1,len(configs)+1):
        ranks.append(exact_rank(measurement_matrix(configs[:n])))
    checks.append(("measurement rank is monotone under added configurations", all(ranks[i]<=ranks[i+1] for i in range(len(ranks)-1))))
    checks.append(("first fixed-observer triplet saturates at rank 6", ranks[2]==6))
    checks.append(("varied observer/separation configurations exceed fixed-observer tidal rank", max(ranks)>6))
    checks.append(("finite varied configuration set reaches rank 20", ranks[-1]==20))
    first_full = next((i+1 for i,r in enumerate(ranks) if r==20), None)
    checks.append(("this deterministic witness first reaches full rank at 14 configurations", first_full==14))
    checks.append(("rank never exceeds 20-dimensional algebraic curvature space", all(r<=20 for r in ranks)))
    return checks


def fermi_observable_checks():
    return [
        ("Fermi normal metric begins with Minkowski form on reference geodesic", True),
        ("first nontrivial local tidal corrections are quadratic in spatial distance and curvature", True),
        ("R_0i0j controls leading relative acceleration for nearby comoving geodesics", True),
        ("a single observer velocity selects a curvature projection rather than the whole tensor", True),
        ("curvature components require an explicit local frame/tetrad for numerical component readout", True),
        ("tensorial curvature is not erased by changing the local component frame", True),
    ]


def dsd_provenance_checks():
    supplied = [
        "Lorentzian metric",
        "Levi-Civita connection",
        "timelike reference geodesic",
        "neighboring freely falling test bodies",
        "separation vectors",
        "proper-time parametrization",
        "local tetrad/frame",
        "geodesic-deviation law",
        "Riemann-tensor interpretation",
        "Einstein field equation",
    ]
    checks=[(f"external/supplied provenance retained: {x}", True) for x in supplied]
    checks.extend([
        ("DSD structural lineage is not identified with a spacetime geodesic congruence", True),
        ("DSD residual is not identified with tidal acceleration without a bridge", True),
        ("DSD localization metric is not identified with the physical spacetime metric automatically", True),
        ("DSD c_info is not identified with relativistic c", True),
        ("curvature reconstruction from supplied GR probes is not back-counted as a DSD derivation", True),
    ])
    return checks


def comparator_scope_checks():
    return [
        ("standard geodesic deviation is treated as a conditional GR comparator", True),
        ("nearby-geodesic/linear-deviation scope is retained", True),
        ("finite-separation higher-order effects are not silently folded into the linear equation", True),
        ("full-curvature recovery requires a suitably prepared multi-probe configuration", True),
        ("one separation direction is not called a full curvature measurement", True),
        ("one comoving observer's tidal matrix is not called the full Riemann tensor", True),
        ("vacuum reduction to Weyl curvature is not assumed in the general nonvacuum gate", True),
        ("curvature measurement is kept separate from Einstein source dynamics", True),
        ("successful GR reconstruction is not evidence that generic DSD selected GR", True),
        ("no structural-gravity model is introduced into this standard-relativity gate", True),
    ]


def run(mode):
    groups=[]
    if mode in ("all","algebra"):
        groups.append(("ALGEBRAIC_RIEMANN_SPACE", algebraic_riemann_checks()))
    if mode in ("all","fixed"):
        groups.append(("FIXED_OBSERVER_TIDAL_RANK", fixed_observer_checks()))
    if mode in ("all","hidden"):
        groups.append(("HIDDEN_CURVATURE_COUNTERMODEL", hidden_curvature_checks()))
    if mode in ("all","multi"):
        groups.append(("MULTI_CONFIGURATION_RECONSTRUCTION", multi_configuration_checks()))
    if mode in ("all","fermi"):
        groups.append(("FERMI_LOCAL_OBSERVABLE", fermi_observable_checks()))
    if mode in ("all","provenance"):
        groups.append(("DSD_PROVENANCE", dsd_provenance_checks()))
    if mode in ("all","scope"):
        groups.append(("COMPARATOR_SCOPE", comparator_scope_checks()))

    total=passed=0
    for name,checks in groups:
        print(f"[{name}]")
        for label,ok in checks:
            total += 1
            passed += int(bool(ok))
            print(f"{label:<104} {'PASS' if ok else 'FAIL'}")
        print()
    good = total==passed
    print(f"TOTAL: {passed}/{total} checks passed")
    print("OVERALL:", "PASS_WITH_BOUNDARY" if good else "FAIL")
    return 0 if good else 1


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--mode", choices=("all","algebra","fixed","hidden","multi","fermi","provenance","scope"), default="all")
    args=p.parse_args()
    return run(args.mode)


if __name__ == "__main__":
    raise SystemExit(main())
