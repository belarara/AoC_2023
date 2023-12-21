import time
import numpy as np
start_time = time.time()

with open("inputs/day_21t.txt", "r") as f:
    data = [l for l in f.read().split("\n") if len(l)>0]

def valid(ar, x, y):
    return x>=0 and x<len(ar) and y>=0 and y<len(ar[0])

def next(ar, x, y):
    return [(x+dx, y+dy) for dx,dy in d.values()]

d = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}
ds = np.array([[a!="#" for a in line] for line in data])
lookup = {(x,y):{(a,b) for a,b in [(x+nx,y+ny) for nx,ny in d.values()] if valid(ds,a,b) and ds[a,b]} for (x,y) in np.ndindex(ds.shape)}

reachable = {0:{(x,y) for x in range(len(data)) for y in range(len(data[0])) if data[x][y] == "S"}}
for i in range(1,200):
    reachable[i] = []
    new = set()
    for x,y in reachable[i-1]:
        for o in lookup[(x,y)]:
            new.add(o)
    reachable[i] = new
    if i>1 and len(reachable[i]-reachable[i-2])==0:
        break

def prt(ar, lst):
    ax = [list(l) for l in ar]
    for (x,y) in lst:
        ax[x][y] = "O"
    for l in ax:
        print("".join(l))
        
#for i in range(7):
#    print()
#    print(i)
#    prt(data, reachable[i])
print(f"1) {1 if 64 not in reachable else len(reachable[64])}")

xs = [(ds.shape[0]//2,0),(ds.shape[0]//2,ds.shape[1]-1)]
ys = [(0,ds.shape[1]//2),(ds.shape[0]-1,ds.shape[1]//2)]
prt(data, xs+ys)

edges = [{(0,64)}, {(64,0)}, {(128,64)}, {(128,64)}]
al = zip(edges)

print(i,len(reachable[i]), len(reachable[i-1]), len(reachable[i-2]), len(reachable[i-3]))
#prt(data, {(0,64), (64,0), (128,64), (128,64)})

print(f"2) {2}")
print(f"time: {time.time() - start_time}s")
