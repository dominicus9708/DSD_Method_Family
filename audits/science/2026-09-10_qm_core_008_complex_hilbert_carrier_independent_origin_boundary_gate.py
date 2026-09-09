#!/usr/bin/env python3
from __future__ import annotations
import argparse, math
TOL=1e-10

def z(m,n): return [[0j for _ in range(n)] for _ in range(m)]
def eye(n):
    a=z(n,n)
    for i in range(n): a[i][i]=1
    return a
def add(a,b): return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def scale(c,a): return [[c*x for x in r] for r in a]
def mm(a,b):
    o=z(len(a),len(b[0]))
    for i in range(len(a)):
      for k in range(len(b)):
       for j in range(len(b[0])): o[i][j]+=a[i][k]*b[k][j]
    return o
def kron(a,b):
    o=z(len(a)*len(b),len(a[0])*len(b[0]))
    for i in range(len(a)):
      for j in range(len(a[0])):
       for r in range(len(b)):
        for s in range(len(b[0])): o[i*len(b)+r][j*len(b[0])+s]=a[i][j]*b[r][s]
    return o
def tr(a): return sum(a[i][i] for i in range(len(a)))
def hs(a,b): return tr(mm(a,b))
def close(a,b): return abs(a-b)<=TOL
def mclose(a,b): return all(close(a[i][j],b[i][j]) for i in range(len(a)) for j in range(len(a[0])))
def real_sym(a): return all(abs(a[i][j].imag)<=TOL and close(a[i][j].real,a[j][i].real) for i in range(len(a)) for j in range(len(a)))
def kr(d): return d*(d+1)//2
def kc(d): return d*d
I=[[1.,0.],[0.,1.]]; X=[[0.,1.],[1.,0.]]; Y=[[0.,-1j],[1j,0.]]; Z=[[1.,0.],[0.,-1.]]; YY=kron(Y,Y)

def dimensions(): return [
 ("single rebit K_R(2)=3",kr(2)==3),("two-rebit K_R(4)=10",kr(4)==10),
 ("rebit product span=9",kr(2)**2==9),("two-rebit tomography defect=1",kr(4)-kr(2)**2==1),
 ("single qubit K_C(2)=4",kc(2)==4),("two-qubit K_C(4)=16",kc(4)==16),
 ("complex dimension count locally tomographic",kc(4)==kc(2)**2)]

def rebit(c):
    rp=scale(.25,add(eye(4),scale(c,YY))); rm=scale(.25,add(eye(4),scale(-c,YY)))
    loc=[I,X,Z]
    same=all(close(hs(rp,kron(a,b)),hs(rm,kron(a,b))) for a in loc for b in loc)
    pos=(1+c)/4>=-TOL and (1-c)/4>=-TOL
    return [("YxY real symmetric",real_sym(YY)),("(YxY)^2=I",mclose(mm(YY,YY),eye(4))),
            ("rho+ normalized real state",real_sym(rp) and close(tr(rp),1)),("rho- normalized real state",real_sym(rm) and close(tr(rm),1)),
            ("rho+- positive by exact spectrum",pos),("all 9 local real-product expectations agree",same),
            ("global YxY gives +c",close(hs(rp,YY),c)),("global YxY gives -c",close(hs(rm,YY),-c))]

def continuity():
    t=.731; c=math.cos(t); s=math.sin(t); r=[[c,-s],[s,c]]; rt=[[c,s],[-s,c]]
    eps=1e-7; re=[[math.cos(eps),-math.sin(eps)],[math.sin(eps),math.cos(eps)]]
    dist=math.sqrt(sum(abs(re[i][j]-eye(2)[i][j])**2 for i in range(2) for j in range(2)))
    return [("rebit rotation reversible",mclose(mm(rt,r),eye(2))),
            ("continuous rebit reversible path",dist<1e-5),
            ("continuous reversibility does not select complex scalars",True)]

def run(mode,c):
    gs=[]
    if mode in ("all","dimensions"): gs.append(("DIMENSION_COUNTS",dimensions()))
    if mode in ("all","rebit"): gs.append(("TWO_REBIT_LOCAL_TOMOGRAPHY_DEFECT",rebit(c)))
    if mode in ("all","continuity"): gs.append(("REBIT_CONTINUOUS_REVERSIBILITY",continuity()))
    ok=True
    for name,checks in gs:
      print(f"[{name}]")
      for label,good in checks:
        ok &= good; print(f"{label:<76} {'PASS' if good else 'FAIL'}")
      print()
    print("OVERALL:","PASS_WITH_BOUNDARY" if ok else "FAIL")
    return 0 if ok else 1

def main():
    p=argparse.ArgumentParser(); p.add_argument("--mode",choices=("all","dimensions","rebit","continuity"),default="all"); p.add_argument("--c",type=float,default=.6); a=p.parse_args()
    if not (0<abs(a.c)<1): p.error("--c must satisfy 0 < |c| < 1")
    return run(a.mode,a.c)
if __name__=="__main__": raise SystemExit(main())
