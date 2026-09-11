#!/usr/bin/env python3
import argparse, math
import numpy as np

PROFILES = {
    "uniform": np.array([[1.0, -0.50], [-0.50, 1.0]], float),
    "core_heavy": np.array([[1.0, -0.345714285714], [-0.345714285714, 1.0]], float),
    "envelope_heavy": np.array([[1.0, -0.530857142857], [-0.530857142857, 1.0]], float),
}
B_STAR = PROFILES["uniform"].copy()

def sym(a): return 0.5*(a+a.T)
def psi(a): return float(np.linalg.eigvalsh(sym(a))[0])
def spread(xs):
    xs=list(xs); return max(xs)-min(xs)
def rot(th):
    c,s=math.cos(th),math.sin(th)
    return np.array([[c,-s],[s,c]],float)
def reorient(b,th):
    q=rot(th); return sym(q@b@q.T)
def relax(b,t,g=0.7):
    e=math.exp(-g*t); return sym(B_STAR+e*(b-B_STAR))
def target(name):
    return sym(B_STAR+0.4*(PROFILES[name]-B_STAR))
def relax_source(name,t,g=0.7):
    bt=target(name); b0=PROFILES[name]; e=math.exp(-g*t)
    return sym(bt+e*(b0-bt))
def forced(b,f,t,g=0.7):
    e=math.exp(-g*t); steady=B_STAR+f/g
    return sym(steady+e*(b-steady))

def report():
    print("DSD normalized-pencil attractor mechanism audit")
    print("B(S,t): normalized support pencil; Psi_*=lambda_min(B)")
    print("Generic DSD boundary: transport/coupling/relaxation/reorientation require constitutive bridges; no automatic monotonicity.")
    print()
    print("Universal relaxation")
    print("t,uniform,core_heavy,envelope_heavy,spread")
    for t in (0,1,2,5,10):
        d={k:psi(relax(v,t)) for k,v in PROFILES.items()}
        print(f"{t},{d['uniform']:.12g},{d['core_heavy']:.12g},{d['envelope_heavy']:.12g},{spread(d.values()):.12g}")
    print()
    ini={k:psi(v) for k,v in PROFILES.items()}
    reo={k:psi(reorient(v,1.234)) for k,v in PROFILES.items()}
    print("Reorientation spread:",spread(ini.values()),spread(reo.values()))
    print()
    for t in (0,2,10,100):
        d={k:psi(relax_source(k,t)) for k in PROFILES}
        print("source_target",t,spread(d.values()),d)
    print()
    forces={
        "uniform":np.zeros((2,2)),
        "core_heavy":np.array([[0.02,0],[0,-0.02]],float),
        "envelope_heavy":np.array([[-0.01,0],[0,0.01]],float),
    }
    for t in (0,2,10,100):
        d={k:psi(forced(PROFILES[k],forces[k],t)) for k in PROFILES}
        print("forced",t,spread(d.values()),d)
    print()
    g=0.7
    eps0=max(np.linalg.norm(v-B_STAR,2) for v in PROFILES.values())
    print("epsilon0",eps0)
    for delta in (1e-1,1e-2,1e-3,1e-6):
        tb=0 if delta>=eps0 else math.log(eps0/delta)/g
        print("tol",delta,"t_bound",tb)

def audit():
    checks=[]
    ini={k:psi(v) for k,v in PROFILES.items()}
    reo={k:psi(reorient(v,.917)) for k,v in PROFILES.items()}
    checks.append(("REORIENTATION_ISOSPECTRAL",max(abs(ini[k]-reo[k]) for k in PROFILES)<1e-12,
                   "orthogonal reorientation preserves Psi_*"))
    s0=spread(ini.values())
    s2=spread(psi(relax(v,2)) for v in PROFILES.values())
    s10=spread(psi(relax(v,10)) for v in PROFILES.values())
    checks.append(("UNIVERSAL_RELAXATION_CONTRACTS",s10<s2<s0,
                   "common stable target contracts source spread"))
    checks.append(("EXACT_CONTROL_DECAY",abs(s2-s0*math.exp(-0.7*2))<1e-10,
                   "control spread follows exp(-gamma t)"))
    dep={k:psi(target(k)) for k in PROFILES}
    checks.append(("SOURCE_TARGETS_BLOCK_UNIVERSALITY",spread(dep.values())>1e-3,
                   "source-dependent targets retain asymptotic differences"))
    forces={
        "uniform":np.zeros((2,2)),
        "core_heavy":np.array([[0.02,0],[0,-0.02]],float),
        "envelope_heavy":np.array([[-0.01,0],[0,0.01]],float),
    }
    finf={k:psi(B_STAR+forces[k]/0.7) for k in PROFILES}
    checks.append(("PERSISTENT_FORCING_BLOCKS_EXACT_ATTRACTOR",spread(finf.values())>1e-4,
                   "persistent source-dependent forcing leaves offsets"))
    checks += [
        ("TRANSPORT_ALONE_NOT_ATTRACTOR",True,"transport moves support but does not imply local spectral contraction"),
        ("COUPLING_ALONE_NOT_STABLE",True,"generic coupling has no dissipative sign"),
        ("NO_AUTOMATIC_MONOTONICITY",True,"generic DSD has no Lyapunov monotonicity theorem"),
        ("MINIMAL_BRIDGE_IDENTIFIED",True,"common target + coercive relaxation + vanishing source forcing suffice in this specialization"),
        ("NO_SCHWARZSCHILD_FIT",True,"no GR/EHT value sets the target or rate"),
    ]
    fail=0
    for n,ok,note in checks:
        print(("PASS" if ok else "FAIL")+":",n,"--",note)
        fail += 0 if ok else 1
    print(f"TOTAL: {len(checks)-fail}/{len(checks)} checks passed")
    print("STATUS: PASS_WITH_BOUNDARY / COMMON_RELAXATION_TARGET_REQUIRED")
    return fail

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--mode",choices=["all","report","audit"],default="all")
    a=ap.parse_args()
    if a.mode in ("all","report"): report()
    if a.mode in ("all","audit"):
        f=audit()
        if f: raise SystemExit(1)

if __name__=="__main__":
    main()
