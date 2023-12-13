import time, re
start_time = time.time()

with open("inputs/day_13.txt", "r") as f:
    data = [l for l in f.read().split("\n\n")]
rotate = lambda data: ["".join([data[j][i] for j in range(len(data))]) for i in range(len(data[0]))]
patterns = [[b for b in a.split("\n") if b != ""] for a in data]

def find_mirror(field, err=0):
    es = []
    for i in range(1,len(field)):
        es.append(0)
        for j in range(i):
            if i+j>=len(field): break
            for k in range(len(field[0])):
                if field[i-1-j][k] != field[i+j][k]:
                    es[-1] += 1
    for i,e in enumerate(es):
        if e==err: return i+1

s1 = 0
for p in patterns:
    x,y = find_mirror(p),find_mirror(rotate(p))
    s1 += 100*x if x is not None else y
print(f"1) {s1}")

s2 = 0
for p in patterns:
    x,y = find_mirror(p, 1),find_mirror(rotate(p), 1)
    s2 += 100*x if x is not None else y
print(f"2) {s2}")
print(f"time: {time.time() - start_time}s")