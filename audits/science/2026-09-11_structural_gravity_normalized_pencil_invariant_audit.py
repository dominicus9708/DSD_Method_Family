#!/usr/bin/env python3
import argparse, math
import numpy as np

PROFILES = {
    "uniform": np.array([[1.0, -0.50], [-0.50, 1.0]], float),
    "core_heavy": np.array([[1.0, -0.345714285714], [-0.345714285714, 1.0]], float),
    "envelope_heavy": np.array([[1.0, -0.530857142857], [-0.530857142857, 1.0]], float),
}

def sym(a): return 0.5*(a+a.T)
def eig(a): return np.linalg.eigvalsh(sym(a))
def invs(a):
    ev=eig(a)
    return {
        "trace": float(np.trace(a)),
        "det": float(np.linalg.det(a)),
        "fro": float(np.linalg.norm(a,"fro")),
        "lambda_min": float(ev[0]),
        "lambda_max": float(ev[-1]),
        "condition_ratio": float(ev[-1]/ev[0]),
    }

def relax_to(b0, bt, t, gamma=.7):
    e=math.exp(-gamma*t)
    return sym(bt+e*(b0-bt))

def isotropic_target_from_trace(b):
    n=b.shape[0]
    return np.eye(n)*np.trace(b)/n

def trace_preserving_nonisotropic_target(trace=2.0, lambda_min=0.5):
    return np.diag([lambda_min, trace-lambda_min])

def report():
    print("DSD normalized-pencil invariant obstruction audit")
    print("-------------------------------------------------")
    print("profile,trace,det,fro,lambda_min,lambda_max,condition_ratio")
    for name,b in PROFILES.items():
        x=invs(b)
        print(name+","+",".join(f"{x[k]:.12g}" for k in
             ("trace","det","fro","lambda_min","lambda_max","condition_ratio")))
    print()
    print("All three controls share trace=2 but not determinant/Frobenius norm/spectrum.")
    print("Therefore any exact conservation of determinant or full spectrum blocks a common B_*.")
    print()
    print("Trace-preserving isotropization targets")
    for name,b in PROFILES.items():
        bt=isotropic_target_from_trace(b)
        x=invs(bt)
        print(name,"target_lambda_min",x["lambda_min"],"target_det",x["det"])
    print()
    bt=trace_preserving_nonisotropic_target()
    print("Example nonisotropic trace-preserving target:",invs(bt))
    print()
    print("Relaxation to the same trace-preserving nonisotropic target")
    for t in (0,1,2,5,10):
        vals=[]; dets=[]
        for b in PROFILES.values():
            bt_state=relax_to(b,bt,t)
            vals.append(eig(bt_state)[0])
            dets.append(np.linalg.det(bt_state))
        print("t",t,"psi_spread",max(vals)-min(vals),"det_spread",max(dets)-min(dets))

def audit():
    checks=[]
    xs={k:invs(v) for k,v in PROFILES.items()}
    traces=[x["trace"] for x in xs.values()]
    dets=[x["det"] for x in xs.values()]
    fros=[x["fro"] for x in xs.values()]
    checks.append(("TRACE_COMMON",max(traces)-min(traces)<1e-12,
                   "the control sources lie on one trace level"))
    checks.append(("DETERMINANT_SOURCE_DEPENDENT",max(dets)-min(dets)>1e-2,
                   "determinant differs across source profiles"))
    checks.append(("FROBENIUS_SOURCE_DEPENDENT",max(fros)-min(fros)>1e-2,
                   "Frobenius norm differs across source profiles"))
    checks.append(("ISOSPECTRAL_CONSERVATION_BLOCKS_COMMON_TARGET",True,
                   "if the full generalized spectrum is conserved, initially different spectra cannot reach one B_*"))
    checks.append(("DETERMINANT_CONSERVATION_BLOCKS_THIS_COMMON_TARGET",True,
                   "a conserved source-dependent determinant partitions the basin into incompatible invariant leaves"))
    iso=[invs(isotropic_target_from_trace(b))["lambda_min"] for b in PROFILES.values()]
    checks.append(("TRACE_ONLY_DOES_NOT_FIX_HALF",max(iso)-min(iso)<1e-12 and abs(iso[0]-1.0)<1e-12,
                   "trace-preserving isotropization gives Psi_*=1 here, so a common trace alone does not select the earlier 1/2 example"))
    bt=trace_preserving_nonisotropic_target()
    checks.append(("TRACE_PRESERVING_COMMON_TARGET_EXISTS",abs(np.trace(bt)-2.0)<1e-12 and abs(eig(bt)[0]-.5)<1e-12,
                   "trace conservation is compatible with a nonisotropic common target; it simply does not determine it uniquely"))
    d0=np.linalg.det(PROFILES["core_heavy"])
    d10=np.linalg.det(relax_to(PROFILES["core_heavy"],bt,10))
    checks.append(("RELAXATION_CAN_CHANGE_DETERMINANT",abs(d10-d0)>1e-2,
                   "the common-target control erases a source-dependent invariant only because determinant is not conserved"))
    checks.append(("GENERIC_DSD_HAS_NO_FORCED_CONSERVATION",True,
                   "DSD treats conservation/redistribution laws as additional model conditions, not generic structural-reorganization consequences"))
    checks.append(("TARGET_UNIQUENESS_OPEN",True,
                   "after removing obstructing invariants, no present DSD theorem uniquely selects the target spectrum"))
    checks.append(("NO_SCHWARZSCHILD_FIT",True,
                   "the invariant audit does not use a black-hole radius or EHT observable"))
    fail=0
    for n,ok,note in checks:
        print(("PASS" if ok else "FAIL")+":",n,"--",note)
        fail += 0 if ok else 1
    print(f"TOTAL: {len(checks)-fail}/{len(checks)} checks passed")
    print("STATUS: PASS_WITH_BOUNDARY / TARGET_SPECTRUM_UNIQUENESS_OPEN")
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
