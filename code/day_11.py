import time
start_time = time.time()

with open("inputs/day_11.txt", "r") as f:
    data = [l for l in f.read().split("\n") if len(l)>0]

rotate = lambda data: ["".join([data[j][i] for j in range(len(data))]) for i in range(len(data[0]))]
empty = lambda ls: [x for x,line in enumerate(ls) if "#" not in line]
level_dist = lambda x1, x2, empties, val: len([a for a in empties if a>min(x1,x2) and a<max(x1,x2)])*(val-1)+abs(x1-x2)

x_empty, y_empty = empty(data), empty(rotate(data))
galaxies = [(x,y) for x, line in enumerate(data) for y,ch in enumerate(line) if ch=="#"]
s1,s2=0,0
while len(galaxies)>1:
    e1,e2 = galaxies.pop()
    for r1,r2 in galaxies:
        s1+= level_dist(e1, r1, x_empty, 2)+level_dist(e2, r2, y_empty, 2)
        s2+= level_dist(e1, r1, x_empty, 1000000)+level_dist(e2, r2, y_empty, 1000000)

print(f"1) {s1}")
print(f"2) {s2}")
print(f"time: {time.time() - start_time}s")