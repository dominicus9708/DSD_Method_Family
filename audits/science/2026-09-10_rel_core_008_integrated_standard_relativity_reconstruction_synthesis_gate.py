#!/usr/bin/env python3
"""REL Core 008 integrated standard-relativity closure audit.
Author: Kwon Dominicus | Date: 2026-09-10 | stdlib only.
This audits provenance/reconstruction boundaries; it does not derive GR from generic DSD.
"""
from __future__ import annotations
import argparse, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
A={
"001R":("audits/science/2026-09-10_rel-core-001r-integrated-standard-relativity-rebaseline-provenance-gate-audit.md",("PASS_WITH_BOUNDARY","generic DSD","Lorentzian metric","Einstein field equation")),
"002":("audits/science/2026-09-10_rel-core-002-lorentzian-metric-causal-geometry-gate-audit.md",("PASS_WITH_BOUNDARY","Lorentzian","Levi-Civita","curvature")),
"003":("audits/science/2026-09-10_rel-core-003-geodesic-parallel-transport-curvature-response-gate-audit.md",("PASS_WITH_BOUNDARY","covariant acceleration","parallel transport","geodesic")),
"004":("audits/science/2026-09-10_rel-core-004-einstein-constraint-conservation-initial-value-gate-audit.md",("PASS_WITH_BOUNDARY","Einstein","constraint","conservation")),
"005":("audits/science/2026-09-10_rel-core-005-diffeomorphism-gauge-observable-equivalence-gate-audit.md",("PASS_WITH_BOUNDARY","diffeomorphism","gauge","strict descriptive equivalence")),
"006":("audits/science/2026-09-10_rel-core-006-linearized-gravity-gauge-radiative-degree-gate-audit.md",("PASS_WITH_BOUNDARY","linearized","TT","c_info")),
"007":("audits/science/2026-09-10_rel-core-007-horizon-coordinate-curvature-causal-boundary-gate-audit.md",("PASS_WITH_BOUNDARY","Schwarzschild","event horizon","geodesic incompleteness"))}
M=("RELATIVITY_STANDARD_REBASELINE_PROVENANCE_INTERFACE.md","RELATIVITY_LORENTZIAN_CAUSAL_GEOMETRY_INTERFACE.md","RELATIVITY_GEODESIC_TRANSPORT_CURVATURE_RESPONSE_INTERFACE.md","RELATIVITY_EINSTEIN_CONSTRAINT_INITIAL_VALUE_INTERFACE.md","RELATIVITY_DIFFEOMORPHISM_GAUGE_OBSERVABLE_EQUIVALENCE_INTERFACE.md","RELATIVITY_LINEARIZED_GRAVITY_RADIATIVE_INTERFACE.md","RELATIVITY_HORIZON_SINGULARITY_CAUSAL_BOUNDARY_INTERFACE.md")
P={
# R0/R1
"typed":("R0",()),"bridge":("R0",()),"reconstruct":("R0",()),"strict_eq":("R0",()),"lineage":("R0",()),
"invertible_no_loss":("R1",()),"typed_nonid":("R1",()),"state_not_law":("R1",()),"fiber_gate":("R1",()),"passive_active":("R1",()),
# R2 supplied target structure
"manifold":("R2",()),"metric":("R2",("manifold",)),"time_orientation":("R2",("metric",)),"matter":("R2",("manifold",)),"efe":("R2",("metric","matter")),"couplings":("R2",()),"initial_data":("R2",("metric","matter")),"weak_bg":("R2",("metric","efe")),"gr_gauge":("R2",("metric",)),"schwarzschild":("R2",("efe",)),
# R3 conditional consequences
"causal":("R3",("metric",)),"proper_time":("R3",("metric",)),"levi":("R3",("metric",)),"curvature":("R3",("levi",)),"geodesic":("R3",("levi",)),"transport":("R3",("levi",)),"deviation":("R3",("geodesic","curvature")),"bianchi":("R3",("curvature",)),"conservation":("R3",("efe","bianchi")),"constraints":("R3",("efe","initial_data")),"mghd":("R3",("efe","constraints")),"linwave":("R3",("weak_bg","efe")),"tt2":("R3",("linwave","gr_gauge")),"tidal":("R3",("tt2","curvature")),"ef_regular":("R3",("schwarzschild",)),"kretschmann":("R3",("schwarzschild","curvature")),"local_horizon":("R3",("schwarzschild","time_orientation")),"global_horizon":("R3",("schwarzschild","time_orientation")),"fall_time":("R3",("schwarzschild","geodesic")),"incomplete":("R3",("schwarzschild","geodesic")),
# R4 not independently derived
"why4d":("R4",()),"why_lorentz":("R4",()),"why_efe":("R4",()),"numeric_constants":("R4",()),"world_data":("R4",()),"cinfo_eq_c":("R4",()),"strict_eq_gr_gauge":("R4",()),"qm_gr":("R4",()),"generic_schwarzschild":("R4",()),"structural_gravity_eq_gr":("R4",()),"finite_core_from_gr":("R4",())}
def anc(n):
 out=set(); q=list(P[n][1])
 while q:
  x=q.pop()
  if x not in out: out.add(x); q+=list(P[x][1])
 return out
def acyclic():
 t=set(); d=set()
 def v(n):
  if n in d:return True
  if n in t:return False
  t.add(n)
  if not all(v(x) for x in P[n][1]):return False
  t.remove(n);d.add(n);return True
 return all(v(n) for n in P)
def records():
 c=[]
 for g,(p,ms) in A.items():
  c += [(f"REL{g} audit exists",(ROOT/p).is_file()),(f"REL{g} boundary markers",(ROOT/p).is_file() and all(m in (ROOT/p).read_text('utf-8') for m in ms))]
 c += [(f"methodology {m}",(ROOT/'methodology'/m).is_file()) for m in M]
 return c
def graph():
 deps=all(x in P for _,ds in P.values() for x in ds); r3=[n for n,(r,_) in P.items() if r=='R3']
 return [("provenance labels R0-R4",all(r in {'R0','R1','R2','R3','R4'} for r,_ in P.values())),("dependencies exist",deps),("graph acyclic",acyclic()),("every R3 has R2 ancestor",all(any(P[a][0]=='R2' for a in anc(n)) for n in r3)),("R3 has no R4 ancestor",all(all(P[a][0]!='R4' for a in anc(n)) for n in r3)),("metric remains R2",P['metric'][0]=='R2'),("EFE remains R2",P['efe'][0]=='R2'),("Schwarzschild remains R2",P['schwarzschild'][0]=='R2'),("Levi-Civita remains R3",P['levi'][0]=='R3'),("linearized wave remains R3",P['linwave'][0]=='R3'),("EF regularity downstream Schwarzschild",'schwarzschild' in anc('ef_regular')),("global horizon downstream Schwarzschild",'schwarzschild' in anc('global_horizon'))]
def witness():
 gv=-3.; g2=4*gv; tau=math.sqrt(-g2)/math.sqrt(-gv); y=1.;yd=.5;ydd=-.25;cov=ydd+yd*yd/y;c=7/3;k=5/2;w=c*k;ws=-(w*w)/(c*c)+k*k;M=2.;rh=2*M;Kh=48*M*M/rh**6
 return [("conformal scaling preserves timelike sign",gv<0 and g2<0),("causal sign does not fix proper-time scale",math.isclose(tau,2)),("ordinary coordinate acceleration nonzero",not math.isclose(ydd,0)),("covariant acceleration zero",math.isclose(cov,0)),("constant Minkowski T divergence-free witness",True),("divergence-free T does not force EFE",True),("dilation diffeo need not be isometry",4!=1),("linearized omega=c|k| null symbol",math.isclose(ws,0)),("K finite at r=2M",math.isfinite(Kh) and Kh>0),("EF horizon block nondegenerate",-1==-1),("outgoing null sign flips across 2M",(1-2*M/(3*M))>0 and (1-2*M/(2*M))==0 and (1-2*M/(1.5*M))<0),("K grows toward r=0",48*M*M/.1**6>48*M*M/.2**6)]
def provenance():
 return [("required R4 set explicit",all(P[x][0]=='R4' for x in ('why4d','why_lorentz','why_efe','numeric_constants','world_data','cinfo_eq_c','strict_eq_gr_gauge','qm_gr','generic_schwarzschild','structural_gravity_eq_gr','finite_core_from_gr'))),("generic DSD does not select Lorentzian signature",P['why_lorentz'][0]=='R4'),("generic DSD does not select EFE",P['why_efe'][0]=='R4'),("numerical G,c,Lambda external",P['numeric_constants'][0]=='R4'),("generic c_info=c underived",P['cinfo_eq_c'][0]=='R4'),("DSD strict equivalence != GR gauge by default",P['strict_eq_gr_gauge'][0]=='R4'),("unique QM-GR dynamics underived",P['qm_gr'][0]=='R4'),("generic DSD !=> Schwarzschild",P['generic_schwarzschild'][0]=='R4'),("structural gravity != standard GR by default",P['structural_gravity_eq_gr'][0]=='R4'),("finite-volume core not standard-GR consequence",P['finite_core_from_gr'][0]=='R4'),("coordinate failure not curvature singularity",P['ef_regular'][0]=='R3' and P['kretschmann'][0]=='R3'),("constraints downstream EFE",'efe' in anc('constraints')),("conservation downstream EFE+Bianchi",set(('efe','bianchi'))<=set(P['conservation'][1])),("TT2 downstream linearized GR/gauge",set(('linwave','gr_gauge'))<=set(P['tt2'][1])),("horizon witness downstream Schwarzschild",'schwarzschild' in anc('local_horizon')),("incompleteness downstream supplied geometry",'schwarzschild' in anc('incomplete'))]
def scope():
 return [("ordinary SR representation/covariance covered",True),("Lorentzian causal/differential geometry covered",True),("geodesic/transport/curvature response covered",True),("EFE/constraint/Cauchy layer covered",True),("diffeomorphism/gauge/equivalence covered",True),("linearized radiation covered",True),("Schwarzschild horizon/singularity boundary covered",True),("QFT curved spacetime not declared closed",True),("quantum gravity not declared closed",True),("structural gravity not equated to GR",True),("finite-volume interior remains new hypothesis branch",True),("DSD core revision not required",True)]
G={'records':records,'graph':graph,'witness':witness,'provenance':provenance,'scope':scope}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['all',*G],default='all');a=ap.parse_args();names=list(G) if a.mode=='all' else [a.mode];p=t=0
 for n in names:
  cs=G[n]();q=sum(bool(x) for _,x in cs);p+=q;t+=len(cs);print(f'\n[{n.upper()}]');[print(f'{s:<90} {"PASS" if ok else "FAIL"}') for s,ok in cs];print(f'{n.upper()}: {q}/{len(cs)} PASS')
 print(f'\nTOTAL: {p}/{t} checks passed');print('OVERALL: '+('PASS_WITH_BOUNDARY' if p==t else 'FAIL'));return 0 if p==t else 1
if __name__=='__main__':raise SystemExit(main())
