import time, sympy
from pprint import pprint
start_time = time.time()

with open("inputs/day_24.txt", "r") as f:
    data = f.read()

hails = [[int(a) for a in b.replace("@",",").split(",")] for b in data.split("\n") if len(b)>0]
hails = [((px,py,pz,vx,vy,vz),(vy, -vx, vy*px - vx*py)) for px,py,pz,vx,vy,vz in hails]

s,e,collide = 200000000000000,400000000000000,0
sm = 0
for i,(h1,e1) in enumerate(hails):
    for (h2,e2) in hails[:i]:
        (a1,b1,c1),(a2,b2,c2) = e1,e2
        divs = b2*a1-b1*a2
        if divs != 0:
            x = (c1*b2 - c2*b1) / divs
            if s<=x<=e:
                y = -(c1*a2 - c2*a1) / divs
                if s<=y<=e and all([all([(inter-hl[c])*hl[3+c]>=0 for hl in (h1,h2)]) for inter,c in [(x,0),(y,1)]]):
                    collide += 1
print(f"1) {sm}")

rx,ry,rz,rvx,rvy,rvz = sympy.symbols("rx ry rz rvx rvy rvz")
eqs = []
for (hx,hy,hz,hvx,hvy,hvz),_ in hails:
    eqs.append(((rx-hx)*(hvy-rvy) - (ry-hy)*(hvx-rvx)))
    eqs.append(((rx-hx)*(hvz-rvz) - (rz-hz)*(hvx-rvx)))
for i in range(10, len(eqs)):
    sol = sympy.solve(eqs[:i])
    if len(sol)>0 and all(v.is_integer for v in sol[0].values()):
        print(f"2) {sum(sol[0][sym] for sym in (rx,ry,rz))}")
        break
print(f"time: {time.time() - start_time}s")