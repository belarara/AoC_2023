import time
from pprint import pprint
from collections import deque
start_time = time.time()

with open("inputs/day_23.txt", "r") as f:
    data = [l for l in f.read().split("\n") if len(l)>0]

next = {
    "^":{(-1, 0)},
    ">":{( 0, 1)},
    "v":{( 1, 0)},
    "<":{( 0, 1)},
    ".":{(-1, 0), ( 1, 0), ( 0,-1), ( 0, 1)}}

mx,my = len(data), len(data[0])
valid = lambda ar,x,y: x>=0 and x<mx and y>=0 and y<my
get_next = lambda ar,x,y: [(x+nx,y+ny) for nx,ny in next[ar[x][y]] if valid(ar,x+nx,y+ny)]

lookup, lookup_next = {}, {}
for x,line in enumerate(data):
    for y,ch in enumerate(line):
        if ch != "#":
            lookup[(x,y)], lookup_next[(x,y)] = set(), set()
            for nx,ny in get_next(data, x, y):
                if data[nx][ny] != "#":
                    lookup[(x,y)].add((nx,ny))
                    if data[nx][ny]=="." or not any([x==px and y==py for px,py in get_next(data, nx, ny)]):
                        lookup_next[(x,y)].add((nx,ny))

forks = {k:lookup_next[k] for k,v in lookup.items() if len(v)>2}
forks[(0,1)], forks[(mx-1,my-2)] = {(1,1)},set()

fork_lookup = {pos:{} for pos in forks}
for fork in forks:
    nq = deque([(a,0) for a in forks[fork]])
    nseen = set()
    while len(nq)>0:
        npos,v = nq.pop()
        if npos in nseen: continue
        nseen.add(npos)
        for next_pos in lookup_next[npos]:
            if next_pos in forks and next_pos!=fork:
                fork_lookup[fork][next_pos] = v+1
            else:
                nq.append((next_pos,v+1))

bruteforced = []
start = ((0,1), 0)
q = deque([start])
seen = {}
while len(q)>0:
    cr,val = q.pop()
    if cr in seen and seen[cr]>=val: continue
    seen[cr] = val
    for next_fork,v in fork_lookup[cr].items():
        if next_fork==(mx-1,my-2):
            bruteforced.append(val+v)
        else:
            q.append((next_fork,val+v+1))

print(f"1) {max(bruteforced)+1}")

data = ["".join(["#" if x=="#" else "." for x in line]) for line in data]

lookup, lookup_next = {}, {}
for x,line in enumerate(data):
    for y,ch in enumerate(line):
        if ch != "#":
            lookup[(x,y)], lookup_next[(x,y)] = set(), set()
            for nx,ny in get_next(data, x, y):
                if data[nx][ny] != "#":
                    lookup[(x,y)].add((nx,ny))
                    if data[nx][ny]=="." or not any([x==px and y==py for px,py in get_next(data, nx, ny)]):
                        lookup_next[(x,y)].add((nx,ny))

forks = {k:lookup_next[k] for k,v in lookup.items() if len(v)>2}
forks[(0,1)], forks[(mx-1,my-2)] = {(1,1)},set()

fork_lookup = {pos:{} for pos in forks}
for fork in forks:
    for sp in forks[fork]:
        path = [sp]
        while path[-1] not in forks:
            for x in lookup_next[path[-1]]:
                if x not in path and x!=fork:
                    path.append(x)
                    break
        fork_lookup[fork][path[-1]] = len(path)

bruteforced = []
start = ((0,1), 0, [(0,1)])
q = deque([start])
top = 0
while len(q)>0:
    cr,val,path = q.pop()
    for next_fork,v in fork_lookup[cr].items():
        if next_fork==(mx-1,my-2):
            if val+v>top: top = val+v
        else:
            if next_fork not in path:
                q.append((next_fork,val+v, path+[next_fork]))

print(f"2) {top}")
print(f"time: {time.time() - start_time}s")