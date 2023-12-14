import time
start_time = time.time()

with open("inputs/day_14.txt", "r") as f:
    data = [list(l) for l in f.read().split("\n") if l!=""]

rotate_r = lambda ds: [[ds[x][y] for x in range(len(ds)-1,-1,-1)] for y in range(len(ds[0]))]
rotate_l = lambda ds: [[ds[x][y] for x in range(len(ds))] for y in range(len(ds[0])-1,-1,-1)]

def tilt_line(line):
    last = 0
    for i in range(len(line)):
        if line[i] == "#": last = i+1
        if line[i] == "O":
            line[i] = "."
            line[last] = "O"
            last += 1
    return line

def tilt(ls):
    for i,line in enumerate(ls):
        ls[i] = tilt_line(line)
    return ls

def beam_load(ar):
    s = 0
    for i, line in enumerate(ar):
        for ch in line:
            if ch=="O":
               s += len(ar)-i
    return s

print(f"1) {beam_load(rotate_r(tilt(rotate_l(data))))}")

def cycle(ds):
    xs = ds
    for _ in range(4):
        xs = rotate_r(tilt(xs))
    return xs

data = rotate_l(data)
k = tuple("".join(l) for l in data)
save, ct = {}, 0
while k not in save:
    save[k] = ct
    data = cycle(data)
    ct += 1
    k = tuple("".join(l) for l in data)
start, end = save[k], ct
repeats = (1000000000-start)//(end-start)
val = start+ repeats*(end-start)

print(f"2) {beam_load(rotate_r([k for k,v in save.items() if v==1000000000-val+start][0]))}")
print(f"time: {time.time() - start_time}s")