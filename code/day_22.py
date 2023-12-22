import time, re
from collections import deque
start_time = time.time()

with open("inputs/day_22.txt", "r") as f:
    data = [l for l in f.read().split("\n") if len(l)>0]

bricks = [[int(a) for a in re.findall(r"(\d+)", l)] for l in data]
mx,my,mz = [max(a) for a in [[max(x[i],x[i+3]) for x in bricks] for i in range(3)]]
zmap = {z:{} for z in range(mz+1)}
sbricks = sorted(bricks, key=lambda e: min(e[2],e[5]))

def fall(zmap, brick):
    bx,by,bz,bxm,bym,_ = brick
    fall = 0
    while bz-fall>1:
        stopped, z = False, bz-fall-1
        for x in range(bx,bxm+1):
            if stopped: break
            for y in range(by,bym+1):
                if (x,y) in zmap[z]:
                    stopped = True
                    break
        if stopped: break
        fall += 1
    return fall

def map_input(zmap, brick, fall, index):
     bx,by,bz,bxm,bym,bzm = brick
     for z in range(bz-fall,bzm-fall+1):
          for x in range(bx,bxm+1):
              for y in range(by,bym+1):
                  zmap[z][(x,y)] = index

new_bricks = []
for i,brick in enumerate(sbricks):
    bx,by,bz,bxm,bym,bzm = brick
    fl = fall(zmap, brick)
    map_input(zmap, brick, fl, i)
    new_bricks.append((bx,by,bz-fl,bxm,bym,bzm-fl))

deps = {i:set() for i in range(len(sbricks))}
support = {i:set() for i in range(len(sbricks))}
for z in range(mz+1):
    for c in zmap[z]:
        if z+1 in zmap and c in zmap[z+1] and zmap[z+1][c]!=zmap[z][c]:
            deps[zmap[z+1][c]].add(zmap[z][c])
            support[zmap[z][c]].add(zmap[z+1][c])

print(f"1) {sum([0 not in [len(deps[e]-{i}) for e in support[i]] for i in range(len(sbricks))])}")

for v in zmap[1].values():
    deps[v].add(-1)

bricks_num = {i for i in range(len(sbricks))}
s = 0
for i in range(len(sbricks)):
    removed = {i,}
    for _ in range(len(bricks_num)):
        nr = set(removed)
        for b in bricks_num-removed:
            supported = False
            for sp in deps[b]:
                if sp not in nr:
                    supported = True
            if not supported: nr.add(b)
        if nr == removed: break
        removed = nr
    s += len(removed)-1

print(f"2) {s}")
print(f"time: {time.time() - start_time}s")