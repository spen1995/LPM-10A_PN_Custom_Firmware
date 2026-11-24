import sys
from emu4 import *
def runts(path):
    img=open(path,'rb').read(); cave=BASE+28552; p=fresh(img,cave,0); res=[]
    # power-on tune
    q=Probe(img,cave); q.boot(); q.ccr.clear(); q.run(800)
    ev=[t for t,v in q.ccr if v!=800]; g=[b-a for a,b in zip(ev,ev[1:])]
    tune=sum(1 for i in range(1,len(g)-1) if g[i]<0.6*min(g[i-1],g[i+1]) )
    for th in range(14):
        tot=0; n=0
        for sig in (36,90,146):
            p.signal=sig; p.run(300); p.ccr.clear(); pl=pulses(p,4)
            for a,b in pl:
                ev=[t for t,v in p.ccr if a<=t<b and v!=800]; g=[y-x for x,y in zip(ev,ev[1:])]
                n+=len(g); tot+=sum(1 for i in range(1,len(g)-1) if g[i]<0.6*min(g[i-1],g[i+1]))
        res.append((th,tot,n)); p.signal=None; p.run(400); p.hold(0,2700); p.run(600)
    return tune,res
for f in sys.argv[1:]:
    tune,res=runts(f); print(f.split('/')[-1]); print("  tune cut half-waves:",tune)
    print("  theme: cut/total  "+"  ".join(f"{t}:{c}/{n}" for t,c,n in res))
