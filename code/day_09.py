import time, functools
start_time = time.time()

with open("inputs/day_09.txt", "r") as f:
    data = f.readlines()

def reduce(ls):
    return [ls[i+1]-ls[i] for i in range(len(ls)-1)]

ans = 0
s, s2 = 0, 0
for line in data:
    numbers = list(map(int, line.split(" ")))
    red = [numbers]
    for _ in range(len(red[-1])-1):
        red.append(reduce(red[-1]))
        if len([a for a in red[-1] if a!=0])<=0: break
    s += sum([r[-1] for r in red])
    s2 += functools.reduce(lambda x, y: [y[0]-x[0]], reversed(red))[0]

print(f"1) {s}")
print(f"2) {s2}")
print(f"time: {time.time() - start_time}s")