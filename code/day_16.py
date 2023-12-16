import time
import numpy as np
start_time = time.time()

with open("inputs/day_16.txt", "r") as f:
    data = [line for line in f.read().split("\n") if len(line)>0]

change = {
    "/": {1:{0},0:{1},2:{3},3:{2}},
    "\\":{0:{3},3:{0},2:{1},1:{2}},
    "-": {1:{1},3:{3},0:{1,3},2:{1,3}},
    "|": {0:{0},2:{2},1:{0,2},3:{0,2}}, 
    ".": {0:{0},1:{1},2:{2},3:{3}}
}
xchange, ychange = {0:-1,1:0,2:1,3:0}, {0:0,1:1,2:0,3:-1}

def move(x, y, vel):
    return x+xchange[vel], y+ychange[vel]

def new_vel(data, x, y, vel):
    return change[data[x][y]][vel]

def energize(data, q):
    cache = np.zeros((len(data), len(data[0]), 4),dtype=bool)
    while len(q)>0:
        cx,cy,cv = q.pop(-1)
        if cache[cx,cy,cv]:
            continue
        cache[cx,cy,cv] = True
        for nv in new_vel(data, cx,cy,cv):
            x,y = move(cx,cy,nv)
            if x>=0 and y>=0 and x<len(data) and y<len(data[0]):
                q.append((x,y,nv))
    return cache

def get_energized(cache):
    return np.sum(np.any(cache, axis=2))

print(f"1) {get_energized(energize(data, [(0,0,1)]))}")

starts = [(0, y, 2) for y in range(len(data[0]))] + [(len(data)-1, y, 0) for y in range(len(data[0]))]
starts += [(x, 0, 1) for x in range(len(data))] + [(x, len(data[0])-1, 3) for x in range(len(data))]
print(f"2) {max([get_energized(energize(data, [(x,y,v)])) for x,y,v in starts])}")

print(f"time: {time.time() - start_time}s")