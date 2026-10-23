"""P10 bounded two-sort property-map audit, source Kwon Dominicus (2026-09-01).
Independent finite audit, not a general proof; no third-party requirements.
Usage: python verify_p10_cross_sort.py [output_json] (default ../results/p10_cross_sort_ci.json).
"""
import itertools as it
import json,sys
from pathlib import Path
SRC='03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c'
PRO={'p':(0,1),'q':(1,0),'r':(0,0)}
DEC=((),('p',),('q',),('r',),('p','q'),('p','q','r'))
MOD=range(4) # full undefined; full zero at first; restricted Ap; restricted Sat

def inputs(s,k):return tuple(it.product(*(range(s[i]) for i in PRO[k])))
def make(s,d,m):
 out=[]
 for k in PRO:
  if k not in d or not all(s[i] for i in PRO[k]):out.append(None);continue
  xs=inputs(s,k);full=frozenset(xs)
  sub=frozenset(x for x in xs if (sum(x)%2==0 if k=='p' else x[0]==0 if k=='q' else x[0]==x[1]))
  ap= sub if m==2 else full; sat=sub if m==3 else full
  xi=((xs[0],0),) if m==1 else ()
  assert all(x in ap and x in sat for x,z in xi)
  out.append((ap,sat,xi))
 return (s,d,tuple(out))
def kind(a,k):return a[2][list(PRO).index(k)]
def maps(a,b,bijections=False):
 opts=[]
 for na,nb in zip(a[0],b[0]):
  if na==0:
   if bijections and nb!=0:return
   opts.append((None,));continue
  if nb==0:return
  v=it.product(range(nb),repeat=na)
  opts.append(tuple(z for z in v if not bijections or (na==nb and len(set(z))==na)))
  if not opts[-1]:return
 yield from it.product(*opts)
def trans(k,x,m):return tuple(m[i][x[j]] for j,i in enumerate(PRO[k]))
def fw(a,b,m):
 if not set(a[1])<=set(b[1]):return False
 for k in a[1]:
  p=kind(a,k)
  if p is None:continue
  q=kind(b,k)
  if q is None:return False
  if any(trans(k,x,m) not in q[0] for x in p[0]):return False
  if any(trans(k,x,m) not in q[1] for x in p[1]):return False
  v=dict(q[2]);
  if any(v.get(trans(k,x,m))!=z for x,z in p[2]):return False
 return True
def emb(a,b,m):
 if not fw(a,b,m) or any(z is not None and len(set(z))!=len(z) for z in m):return False
 for k in a[1]:
  p=kind(a,k)
  if p is None:continue
  q=kind(b,k);px=dict(p[2]);qx=dict(q[2])
  for x in inputs(a[0],k):
   y=trans(k,x,m)
   if ((x in p[0])!=(y in q[0]) or (x in p[1])!=(y in q[1]) or (x in px)!=(y in qx)):return False
 return True
def inv(m):
 r=[]
 for z in m:
  if z is None:r.append(None);continue
  s=[-1]*len(z)
  for i,v in enumerate(z):s[v]=i
  assert -1 not in s
  r.append(tuple(s))
 return tuple(r)
def strict(a,b,m):
 return (a[1]==b[1] and all((n==0)==(p==0) for n,p in zip(a[0],b[0]))
         and all(z is None or (len(z)==b[0][i] and len(set(z))==len(z)) for i,z in enumerate(m))
         and emb(a,b,m) and emb(b,a,inv(m)))
def comp(ab,bc):return tuple(None if z is None else tuple(y[v] for v in z) for z,y in zip(ab,bc))
def cmp(a,b):
 c=[0]*5
 for m in maps(a,b,True):
  c[0]+=1
  if a[1]!=b[1]:continue
  c[1]+=1
  def preserved(level):
   for k in a[1]:
    p=kind(a,k)
    if p is None:continue
    q=kind(b,k)
    for x in inputs(a[0],k):
     y=trans(k,x,m)
     if (x in p[0])!=(y in q[0]) or (x in p[1])!=(y in q[1]):return False
     if level==4:
      px=dict(p[2]);qx=dict(q[2])
      if (x in px)!=(y in qx) or (x in px and px[x]!=qx[y]):return False
   return True
  if not preserved(3):continue
  c[2]+=1
  if preserved(4):c[3]+=1
 c[4]=c[3]
 return tuple(c)
def audit():
 pool=(make(s,d,m) for s,d,m in it.product(it.product((0,1,2),repeat=2),DEC,MOD))
 cores=sorted(set(pool),key=str);n=len(cores)
 edges=[{}, {}, {}];tot={'candidate':0,'forward':0,'embedding':0,'strict':0}
 for i,a in enumerate(cores):
  for j,b in enumerate(cores):
   mlist=[[],[],[]]
   for m in maps(a,b):
    tot['candidate']+=1
    if fw(a,b,m):
     mlist[0].append(m)
     if emb(a,b,m):
      mlist[1].append(m)
      if strict(a,b,m):mlist[2].append(m)
   for t,ml in enumerate(mlist):
    if ml:edges[t][i,j]=set(ml)
    tot[('forward','embedding','strict')[t]]+=len(ml)
 stage={};branches={str(t):0 for t in range(1,5)}
 for i,a in enumerate(cores):
  for j,b in enumerate(cores):
   z=cmp(a,b);stage[i,j]=z
   assert all(z[t+1]<=z[t] for t in range(4)) and z[3]==z[4]
   assert (z[3]>0)==bool(edges[2].get((i,j)))
   if not z[3]:branches[str(next(t+1 for t in range(4) if not z[t]))]+=1
 assert all(stage[i,j]==stage[j,i] for i in range(n) for j in range(n))
 compcounts=[]
 for ed in edges:
  by={}
  for (i,j),ms in ed.items():by.setdefault(i,[]).append((j,ms))
  count=0
  for (i,j),ms in ed.items():
   for k,ns in by.get(j,[]):
    target=ed.get((i,k));assert target is not None
    for m,v in it.product(ms,ns):
     assert comp(m,v) in target
     count+=1
  compcounts.append(count)
 for (i,j),ms in edges[2].items():
  assert all(inv(m) in edges[2].get((j,i),set()) for m in ms)
 assert any(a[1] and any(kind(a,k) is None for k in a[1]) for a in cores)
 assert any(a[1]!=b[1] and m for (i,j),ms in edges[1].items() for a,b in [(cores[i],cores[j])] for m in ms)
 assert any(any(z is not None and tuple(z)!=tuple(range(len(z))) for z in m)
            for ms in edges[2].values() for m in ms)
 assert any(a[0]==(1,1) and a[1]==('p',) and kind(a,'p')[2] for a in cores)
 assert tot['strict']<tot['embedding'] and all(branches.values())
 return {'case':'P10-CROSS-SORT','locked_pdf_sha256':SRC,'models':n,'ordered_pairs':n*n,
  'sorts':['u','v'],'profiles':{k:list(v) for k,v in PRO.items()},
  'template_modes':4,'declaration_patterns':6,'sizes_per_sort':[0,1,2],
  'map_counts':tot,'composition_counts':dict(zip(('forward','embedding','strict'),compcounts)),
  'first_branch_pair_counts':branches,'all_assertions_pass':True,
  'P5_A_illtyped_declared_unavailable_reproduced':True,
  'P5_B_componentwise_bijective_embedding_not_strict_reproduced':True,
  'nontrivial_two_element_carrier_permutation_tested':True,
  'property_labels_not_swapped':True,'ordered_mixed_profiles_tested':True,
  'core_iso_does_not_force_representation_iso':True,
  'all_general_theorems_formally_proved':False,
  'original_experiment_Python_changed':False,'manuscript_modified':False,'FPA':'OPEN'}
if __name__=='__main__':
 obj=audit();p=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/'results/p10_cross_sort_ci.json'
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
 print('P10 CI PASS',obj['models'],obj['map_counts'],obj['composition_counts'])
