import sys
from emu4 import *
img=open(sys.argv[1],'rb').read(); cave=BASE+28552
q=Probe(img,cave); q.boot(); q.ccr.clear(); q.run(800)
ev=[(t,abs(v-800)) for t,v in q.ccr if v!=800]
print("tune: first swings",[a for t,a in ev[:8]],"last",[a for t,a in ev[-8:]],"max",max(a for t,a in ev), "max step", max(abs(b[1]-a[1]) for a,b in zip(ev,ev[1:])))
p=fresh(img,cave,0)
for th in range(3):
    p.signal=36; p.run(200); p.ccr.clear(); a,b=pulses(p,1)[0]
    ev=[(t-a,abs(v-800)) for t,v in p.ccr if a<=t<b+40 and v!=800]
    print("theme",p.st()['theme'],"n flips",len(ev),"first",[x[1] for x in ev[:7]],"last",[x[1] for x in ev[-6:]],"end tick",ev[-1][0],"of",b-a)
    p.signal=None; p.run(400); p.hold(0,2700); p.run(600)
p.hold(0,120); p.run(300)
