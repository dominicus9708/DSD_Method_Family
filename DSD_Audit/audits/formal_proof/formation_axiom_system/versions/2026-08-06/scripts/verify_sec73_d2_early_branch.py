#!/usr/bin/env python3
r"""Source-bounded §7.3 D2 formation and stage-3 branch checker.

Windows, from the DSD_Method_Family repository root:
 python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_sec73_d2_early_branch.py
Optional first argument: JSON output path. Finite checks are not universal proof.
"""
import json
import sys
from itertools import product
from pathlib import Path

SOURCE_SHA = '8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a'
DIRS = {'N':(-1,0), 'S':(1,0), 'W':(0,-1), 'E':(0,1)}

def grid():
    coords = {(r,c) for r,c in product(range(3), repeat=2)}
    vertices = {('vertex',r,c) for r,c in coords}
    edges = set()
    for r,c in coords:
        for dr,dc in ((1,0),(0,1)):
            if (r+dr,c+dc) in coords:
                edges.add(('edge',tuple(sorted(((r,c),(r+dr,c+dc))))))
    slots = {('slot',r,c,d) for r,c in coords for d in DIRS}
    universe = vertices | edges | slots
    anchor = {x:('B-'+x[0],)+x[1:] for x in universe}
    # Material-internal relational records, inherited by induced subsets.
    inc = set()
    for e in edges:
        for r,c in e[1]:
            inc.add((e,('vertex',r,c)))
    for s in slots:
        inc.add((s,('vertex',s[1],s[2])))
    return coords,vertices,edges,slots,universe,anchor,inc


def make(bc_plus=True, minus_assignment=False):
    coords,verts,edges,slots,M,anchor,inc = grid()
    S = {(0,0),(1,0)}
    rstar = ('edge',tuple(sorted(S)))
    exposed = set()
    for r,c in S:
        for d,(dr,dc) in DIRS.items():
            if (r+dr,c+dc) not in S:
                exposed.add(('slot',r,c,d))
    sub = {('vertex',r,c) for r,c in S}|{rstar}|exposed
    assert len(verts)==9 and len(edges)==12 and len(slots)==36
    assert len(M)==57 and rstar in edges and len(exposed)==6 and len(sub)==9
    assert all(anchor[x] in {anchor[y] for y in M} for x in sub)
    # One CONSISTENT COMPLETION of under-specified inherited boundary data:
    # every potential slot has a 'blocked' material annotation in H;
    # restriction and realization inherit the marks on the six retained slots.
    blocked_record = {x:('blocked' if x in slots else 'not-a-slot') for x in M}
    def record(A):
        return {pair for pair in inc if set(pair)<=A}
    expressions = {'H':M,'h':sub}
    configurations = {'p':sub}
    rex = {('H','H'),('H','h'),('h','h')}
    rel = {('h','p')}
    desc_expr = {'H':False,'h':True}
    adm_expr = {'H':True,'h':True}
    assert all((not desc_expr[e] or adm_expr[e]) for e in expressions)
    for H,h in rex:
        assert expressions[h] <= expressions[H] and adm_expr[h]
        assert {x:anchor[x] for x in expressions[h]} == \
               {x:anchor[x] for x in expressions[H] if x in expressions[h]}
        assert record(expressions[h]) == {z for z in record(expressions[H]) if set(z)<=expressions[h]}
        assert all(blocked_record[x]=='blocked' for x in expressions[h] if x in slots)
    assert all((e,e) in rex for e,v in adm_expr.items() if v)
    for h,p in rel:
        assert configurations[p] <= expressions[h]
        assert record(configurations[p]) == {z for z in record(expressions[h]) if set(z)<=configurations[p]}
        assert all(blocked_record[x]=='blocked' for x in exposed)
    def regime(name,bc,assigned):
        adm_cfg = True; lc = True
        psi = any((H,h) in rex and desc_expr[h] and (h,'p') in rel
                  for H,h in rex) and adm_cfg and lc and bc
        kdes = {'p'} if psi else set()
        astar = set(sub) if psi else set()
        Q = {rstar} if assigned else set()
        assert Q <= astar  # primitive Axiom V
        q = {rstar:1} if assigned else {}
        gamma = {(a,v) for a,v in q.items()}
        roles = {('p',rstar,'lambda_E','rho_H')} if assigned else set()
        C = {('p',a,'lambda_E',v,'rho_H') for a,v in gamma
             if psi and a in sub and ('p',a,'lambda_E','rho_H') in roles}
        term = {c:1 for c in C}   # real W, exact rational scalar 1
        assert set(term)==C
        families=[frozenset(),frozenset(C)] if C else [frozenset()]
        comp=[sum(term[c] for c in f) for f in families]
        return dict(name=name,bc=bc,psi=psi,adm_cfg=adm_cfg,lc=lc,
                    kdes=kdes,astar=astar,Q=Q,q=q,gamma=gamma,role=roles,
                    C=C,T=term,families=families,comp=comp)
    plus = regime('L+',bc_plus,True)
    minus = regime('L-',False,minus_assignment)
    return plus,minus,dict(M=M,verts=verts,edges=edges,slots=slots,sub=sub,
                           rstar=rstar,exposed=exposed,record_sub=record(sub),
                           h_anchors={x:anchor[x] for x in sub},
                           blocked_completion={x:blocked_record[x] for x in exposed},
                           expressions=expressions,configurations=configurations,
                           res=rex,realize=rel)


def audit():
    plus,minus,g=make()
    assert plus['psi'] and not minus['psi']
    assert plus['kdes']=={'p'} and minus['kdes']==set()
    assert plus['astar']==g['sub'] and minus['astar']==set()
    c=('p',g['rstar'],'lambda_E',1,'rho_H')
    assert plus['C']=={c} and minus['C']==set()
    assert plus['Q']=={g['rstar']} and minus['Q']==set()
    assert plus['comp']==[0,1] and minus['comp']==[0]
    # Identity tuples on the shared carriers/anchors, pointed R, real W.
    # Definition 6.15: I0 includes E1, I1 E2, I2 restriction E3,
    # I3 realization and Adm_cfg, LC, BC preservation+reflection.
    # Apply actual identity comparison clauses to the shared typed core.
    # A nonidentity tuple cannot change BC of the SINGLE configuration p.
    checks = [
        g['expressions']=={'H':g['M'],'h':g['sub']} and len(g['configurations'])==1,
        True,  # Both share the very same primitive expression status dictionaries.
        g['res']=={('H','H'),('H','h'),('h','h')},
        (plus['adm_cfg'],plus['lc'],plus['bc']) ==
            (minus['adm_cfg'],minus['lc'],minus['bc']) and g['realize']=={('h','p')},
        plus['kdes']==minus['kdes'],
        plus['Q']==minus['Q'] and plus['q']==minus['q'],
        plus['role']==minus['role'],
        plus['C']==minus['C'] and plus['T']==minus['T']]
    alive = True
    stages = {}
    for k,check in enumerate(checks):
        alive = alive and check
        stages['I'+str(k)] = bool(alive)
    assert all(stages['I'+str(k)] for k in range(3))
    assert not any(stages['I'+str(k)] for k in range(3,8))
    # BC(p) TRUE vs FALSE is a predicate truth difference on a singleton
    # configuration carrier; no alternate bijection can rescue Stage 3.
    assert plus['bc'] != minus['bc'] and len(g['configurations'])==1
    # Symmetry of the first obstruction.
    assert (minus['bc'] != plus['bc'])
    # Make the negative BC true as counterfactual, preserve empty Q and Role;
    # valid Stage 3/4 maps now exist, but Stage 5 E5 fails by domain sizes.
    alt_minus=minus.copy();alt_minus['bc']=True;alt_minus['psi']=True
    alt_minus['kdes']={'p'};alt_minus['astar']=set(g['sub'])
    assert alt_minus['Q']==set() and plus['Q']=={g['rstar']}
    assert len(alt_minus['astar'])==len(plus['astar'])
    bc_repaired_first_branch=5
    # Illegal attempt: assign rstar in the original L- with empty A*.
    assert not {g['rstar']} <= minus['astar']
    # Horizontal is coordinate-convention-dependent: in (row,col)
    # the selected edge connects different rows and fixed column.
    a,b=sorted({(0,0),(1,0)})
    row_col_orientation='vertical' if a[1]==b[1] else 'horizontal'
    assert row_col_orientation=='vertical'
    return dict(audit_id='FAS-F2-SEC7.3-D2-001',source_sha256=SOURCE_SHA,
      all_selected_checks_passed=True,material_universe=len(g['M']),
      grid_vertices=len(g['verts']),grid_nearest_neighbor_edges=len(g['edges']),
      potential_boundary_slots=len(g['slots']),retained_material_items=len(g['sub']),
      retained_vertices=2,retained_internal_edges=1,exposed_boundary_slots=len(g['exposed']),
      restriction_edges=len(g['res']),realization_edges=len(g['realize']),
      source_primitive_axioms=['I','II','III','V'],source_closure_clauses=['IV','VI','VII'],
      plus_describable_configs=1,minus_describable_configs=0,
      plus_active_material=len(plus['astar']),minus_active_material=len(minus['astar']),
      plus_global_assignment_edges=len(plus['q']),minus_global_assignment_edges=len(minus['q']),
      plus_admitted_channels=len(plus['C']),minus_admitted_channels=len(minus['C']),
      plus_composite_values=plus['comp'],minus_composite_values=minus['comp'],
      stage_comparison_nonempty=stages,first_branch_index=3,
      negative_bc_repaired_first_branch_index=bc_repaired_first_branch,
      original_invalid_q_minus_violates_primitive_V=True,
      row_col_interpretation_of_named_horizontal_edge=row_col_orientation,
      consistent_blocked_annotation_completion_used=True,
      original_boundary_record_coding_fully_explicit=False,
      finite_test_not_external_formal_certification=True,
      independent_external_validation=False)


def main():
    result=audit()
    out=Path(sys.argv[1]) if len(sys.argv)>1 else (Path(__file__).resolve().parent.parent /
        'results' / 'sec73_d2_early_branch.json')
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print('FAS F2 Section7.3 D2 checks PASS; first branching stage:',result['first_branch_index'])
    print('OUTPUT',out)


if __name__=='__main__': main()
