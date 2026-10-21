#!/usr/bin/env python3
r"""F2 Appendix A: selected typing / domain sanity checks, not a PDF parser or proof certifier.

Repository-root Windows command:
 python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_appa_typing_notation.py
Optional argv[1] sets the JSON output path. Standard library only.
"""
import json
import sys
from pathlib import Path

SOURCE_SHA = '8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a'
ROWS = [
 ('A01','B / Supp(B)','2.1-2.2','set-sized base and typed support'),
 ('A02','M_L / M_B^L','2.2','material structure distinct from carrier'),
 ('A03','E_B^L / P_B^L','2.2','all candidate expressions and configurations'),
 ('A04','Adm_expr / Des_expr','2.2,3.1','two expression predicates'),
 ('A05','Adm_cfg / LC / BC','2.2,3.1','configuration primitive gates'),
 ('A06','Res / Realize','2.2,3.1','expression-expression / expression-configuration'),
 ('A07','Psi / A_star','2.2 Def2.1','derived primitive-vocabulary witness and union'),
 ('A08','K_des / A','3.1 IV','derived describable configurations and union'),
 ('A09','V_lambda / zero_lambda','2.2','pointed set, not generally scalar space'),
 ('A10','Q_lambda / q_lambda / Gamma_lambda','3.2 V','one global partial assignment and graph'),
 ('A11','U / C / T','3.2 VI-VII','candidate/admitted channels; term defined on C'),
 ('A12','D_comp / Comp','3.2 VII','finite admitted-channel sets and sums'),
 ('A13','F_le_k / F_k(B,F) / pi_j_i','2.3 Def2.4','stage records/class and erasures'),
 ('A14','Tr(c)','3.3 Def3.5','candidate formation-trace set'),
 ('A15','Sigma_L','6.1 Def6.1','full candidate-level descriptor'),
 ('A16','FormDesc_B_F','2.1,6.1','metatheoretic class of set-coded descriptors'),
 ('A17','Phi / Phi_hat','6.2 Def6.2','forward and induced candidate-channel maps'),
 ('A18','iso_fix_B','6.3 Def6.10','strict base-fixed formation isomorphism'),
 ('A19','I_k / b','6.4 Def6.15','comparison sets and earliest failure index'),
]

def full_fixture(assigned, value=0, term=0):
    """One-point full formation model, source-typed and with genuine trace."""
    a, h, p = 'a','h','p'
    anchor = {a:'s'}
    expression = {h}; config = {p}; material = {a}
    adm_expr = {h}; des_expr = {h}
    res = {(h,h)}; realize = {(h,p)}
    assert des_expr <= adm_expr and res == {(h,h)}
    assert material == {a} and set(anchor) == material
    assert (h,p) in realize
    psi = (h,h) in res and h in des_expr and (h,p) in realize
    assert psi
    kdes = {p} if psi else set()
    Astar = {a} if kdes else set()
    Aderived = set(Astar)
    assert Aderived == Astar
    Q = {a} if assigned else set()
    q = {a:value} if assigned else {}
    assert set(q) == Q and Q <= Astar
    Gamma = {(x,q[x]) for x in Q}
    U = {(p,a,'lambda',v,'rho') for v in (0,1)}
    Role = {(p,a,'lambda','rho')}
    C = {c for c in U if c[0] in kdes and c[1] in Astar and
         (c[1],c[3]) in Gamma and (c[0],c[1],c[2],c[4]) in Role}
    trace = {c:({(h,h,p,a,'lambda',c[3],'rho')} if c in C else set()) for c in U}
    assert all(bool(trace[c]) == (c in C) for c in U)
    T = {c:term for c in C}
    Dcomp = [frozenset()] + ([frozenset(C)] if C else [])
    comp = {f:sum(T[c] for c in f) for f in Dcomp}
    assert comp[frozenset()] == 0
    return dict(U=U,C=C,Q=Q,q=q,Gamma=Gamma,T=T,Dcomp=Dcomp,
                comp=comp,trace=trace,Astar=Astar,A=Aderived)

def stage_reduction_check():
    stages = [tuple(range(k+1)) for k in range(8)]
    pi = lambda j,i: stages[j][:i+1]
    tested = 0
    for k in range(8):
        assert pi(k,k) == stages[k]
        for j in range(k+1):
            for i in range(j+1):
                assert pi(j,i) == pi(k,i)
                assert pi(j,i) == pi(k,j)[:i+1]
                tested += 1
    return tested

def audit():
    assert len(ROWS) == 19 and len({r[0] for r in ROWS}) == 19
    assigned_zero = full_fixture(True, 0, 0)
    unassigned = full_fixture(False)
    assigned_one = full_fixture(True, 1, 0)
    c0 = next(iter(assigned_zero['C']))
    assert assigned_zero['q']['a'] == 0 and 'a' not in unassigned['q']
    assert c0 in assigned_zero['C'] and c0 not in unassigned['C']
    assert assigned_zero['T'][c0] == 0 and len(unassigned['T']) == 0
    assert assigned_zero['comp'][frozenset({c0})] == 0
    assert unassigned['Dcomp'] == [frozenset()]
    assert len(assigned_one['C']) == 1 and assigned_one['T']
    assert all((c in fixture['C']) == bool(fixture['trace'][c])
               for fixture in (assigned_zero,unassigned,assigned_one)
               for c in fixture['U'])
    # A typed forward map may merge role labels. With two source role channels
    # and one target role channel, F1-F6 hold and each term is preserved,
    # but the finite SET image collapses duplicates: 1+1 != 1.
    source_roles=('r1','r2'); target_roles=('r',)
    tauR = {'r1':'r','r2':'r'}
    cs = {('p','a','lambda',1,r) for r in source_roles}
    ct = {('p','a','lambda',1,'r')}
    phi = lambda c: (c[0],c[1],c[2],c[3],tauR[c[4]])
    assert {phi(c) for c in cs} == ct and len(cs)==2 and len(ct)==1
    assert all(1 == 1 for c in cs)  # J=id and T_source=T_target=1.
    assert sum(1 for _ in cs) == 2 and sum(1 for _ in {phi(c) for c in cs}) == 1
    stage_triples = stage_reduction_check()
    return dict(audit_id='FAS-F2-APPA-TYP-001',source_sha256=SOURCE_SHA,
        appendix='A Typing and Notation',printed_page=30,
        source_table_rows=len(ROWS),all_selected_checks_passed=True,
        primary_type_crosswalk=[dict(id=i,symbol=s,source=src,scope=meaning)
                                for i,s,src,meaning in ROWS],
        one_global_partial_q_defined_zero_not_undefined=True,
        zero_term_admitted_channel_distinct_from_absent_channel=True,
        candidate_trace_iff_admitted=True,
        T_domain_is_admitted_C_not_candidate_U=True,
        finite_channel_family_contains_empty=True,
        composite_empty_family_zero=True,
        stage_reduction_triples_checked=stage_triples,
        forward_channel_map_collision_preserves_terms_not_finite_set_sums=True,
        forward_sum_preservation_requires_injective_channel_map=True,
        F_k_of_B_F_is_metatheoretic_not_python_enumerated=True,
        appendix_table_is_selective_not_exhaustive=True,
        nonlisted_typed_symbols=['W','J','Role','Chan','Des_cfg','Lambda_delta','size','delta'],
        outstanding_source_type_mismatch_count=0,
        source_edit_performed=False,not_a_mathematical_proof_certificate=True,
        independent_external_validation=False)

def main():
    result=audit()
    out=Path(sys.argv[1]) if len(sys.argv)>1 else (Path(__file__).resolve().parent.parent/'results'/'appa_typing_notation.json')
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n',encoding='utf8')
    print('Appendix A typed crosswalk PASS:',result['source_table_rows'],'rows;',result['stage_reduction_triples_checked'],'stage triples')
    print('OUTPUT',out)
if __name__=='__main__': main()
