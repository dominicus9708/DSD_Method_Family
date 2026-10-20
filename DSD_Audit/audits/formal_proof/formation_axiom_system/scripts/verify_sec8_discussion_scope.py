#!/usr/bin/env python3
r"""F2 Discussion §8: executable counterexamples to unqualified logical weakening.

Standard-library selected witnesses; not external mathematical certification.
Windows (GitHub DSD_Method_Family root):
 python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_sec8_discussion_scope.py
Optional first argument supplies a JSON output path.
"""
import json
import sys
from pathlib import Path

SOURCE_SHA = '8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a'


def model(assigned):
    """Finite carrier source full formation model, with W=R externally supplied."""
    m = ('m', 0)
    h = ('h', 0)
    p = ('p', 0)
    lam = 'lambda'
    rho = 'rho'
    material = {m}
    expressions = {h}
    configurations = {p}
    admitted_expressions = {h}
    described_expressions = {h}
    restrictions = {(h, h)}
    realizations = {(h, p)}
    configuration_gates = {p: (True, True, True)}
    anchor = {m: 's0'}
    mat = {h: set(material)}
    act = {p: set(material)}
    assert described_expressions <= admitted_expressions
    assert all((x, x) in restrictions for x in admitted_expressions)
    assert all(mat[x] <= mat[y] and x in admitted_expressions for y, x in restrictions)
    assert all(act[y] <= mat[x] for x, y in realizations)
    assert all(anchor[x] == 's0' for x in material)
    psi = {x: any((H, y) in restrictions and y in described_expressions and
                       (y, x) in realizations for H, y in restrictions) and
                 all(configuration_gates[x]) for x in configurations}
    assert psi == {p: True}
    describable = {x for x in configurations if psi[x]}
    Astar = set().union(*(act[x] for x in describable))
    assert Astar == material
    Q = {m} if assigned else set()
    q = {m: 1} if assigned else {}
    role = {(p, m, lam, rho)} if assigned else set()
    assert Q <= Astar and set(q) == Q
    gamma = {(a, q[a]) for a in Q}
    candidate = {(p, m, lam, 1, rho)}
    C = {c for c in candidate if c[0] in describable and
         (c[1], c[3]) in gamma and (c[0], c[1], c[2], c[4]) in role}
    assert len(C) == int(assigned)
    traces = {c: {(h, h, c[0], c[1], c[2], c[3], c[4])} for c in C}
    assert all(traces[c] for c in C)
    T = {c: 1 for c in C}
    families = [frozenset()] + ([frozenset(C)] if C else [])
    sums = {f: sum(T[c] for c in f) for f in families}
    assert len(families) == (2 if assigned else 1)
    assert sums[frozenset()] == 0
    # These are all primitive inputs, supplied W,T, and exact derived data.
    return dict(material=material, expressions=expressions, configurations=configurations,
                adm=admitted_expressions, des=described_expressions,
                res=restrictions, real=realizations, gates=configuration_gates,
                mat=mat, act=act, anchor=anchor, kind={lam}, role_carrier={rho},
                value_zero=0, Q=Q, q=q, role=role, Astar=Astar, Kdes=describable,
                C=C, traces=traces, term=T, families=families, sums=sums)


def run():
    posL, posM = model(True), model(True)
    negL, negM = model(False), model(False)
    # Identical primitive+derived+supplied data admit STRICT IDENTITY ISOMORPHISM
    # with J0=id_R, irrespective of whether admitted channels exist.
    assert posL == posM and negL == negM
    id_strict_positive = (posL == posM)
    id_strict_empty = (negL == negM)
    j_neg = lambda x: -x
    j_id = lambda x: x
    samples = [-3, -2, -1, 0, 1, 2, 3]
    assert all(j_neg(a+b) == j_neg(a)+j_neg(b) for a in samples for b in samples)
    assert all(j_neg(k*a) == k*j_neg(a) for k in samples for a in samples)
    assert all(j_neg(j_neg(a)) == a for a in samples)
    assert j_neg(0)==0 and j_neg(1)==-1
    # The only NONEMPTY family of each positive singleton-channel model is {c}.
    nonempty_L = [f for f in posL['families'] if f]
    nonempty_M = [f for f in posM['families'] if f]
    assert len(nonempty_L)==len(nonempty_M)==1
    coincident_fixed_neg_J = any(j_neg(posL['sums'][f]) == posM['sums'][g]
                                 for f in nonempty_L for g in nonempty_M)
    coincident_fixed_identity_J = any(j_id(posL['sums'][f]) == posM['sums'][g]
                                      for f in nonempty_L for g in nonempty_M)
    assert not coincident_fixed_neg_J and coincident_fixed_identity_J
    # Empty C: even identity J has no admissible nonempty family.
    empty_nonempty_L = [f for f in negL['families'] if f]
    empty_nonempty_M = [f for f in negM['families'] if f]
    coincident_empty = any(j_id(negL['sums'][f]) == negM['sums'][g]
                           for f in empty_nonempty_L for g in empty_nonempty_M)
    assert not coincident_empty and not empty_nonempty_L and not empty_nonempty_M
    return dict(audit_id='FAS-F2-SEC8-DISC-001', source_sha256=SOURCE_SHA,
        all_checks_passed=True,
        standard_nonempty_full_model_primitive_and_closure_axioms_passed=True,
        standard_empty_channel_full_model_primitive_and_closure_axioms_passed=True,
        nonempty_case_strict_equivalence_by_identity=id_strict_positive,
        prescribed_J='J(x)=-x over real F=R; real-linear bijection',
        selected_scalar_linearity_tests_passed=True,
        nonempty_case_fixed_negative_J_coincidence=coincident_fixed_neg_J,
        nonempty_case_fixed_identity_J_coincidence=coincident_fixed_identity_J,
        empty_channel_case_strict_equivalence_by_identity=id_strict_empty,
        empty_channel_case_nonempty_families_count_L=len(empty_nonempty_L),
        empty_channel_case_nonempty_families_count_M=len(empty_nonempty_M),
        empty_channel_case_fixed_identity_J_coincidence=coincident_empty,
        implication_strict_equivalent_implies_coincident_for_arbitrary_prescribed_J=False,
        proposition_6_22_counterexample_not_refuted=True,
        source_discussion_unqualified_strictly_weaker_needs_clarification=True,
        source_discussion_no_new_physical_theorem=True,
        section8_other_claims_require_source_ledger_not_program_proof=True,
        independent_external_validation=False)


def main():
    result=run()
    out=Path(sys.argv[1]) if len(sys.argv)>1 else (
        Path(__file__).resolve().parent.parent / 'results' / 'sec8_discussion_scope.json')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf8')
    print('Section8 fixed-J counterexamples PASS:', result['all_checks_passed'])
    print('OUTPUT:',out)


if __name__=='__main__':
    main()
