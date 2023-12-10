import time
start_time = time.time()

with open("inputs/day_10.txt", "r") as f:
    data = [l for l in f.read().split("\n") if len(l)>0]

dir_to_coord = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
transform = {"|": (1,3), "-": (0,2), "L": (0,3), "J": (2,3), "7": (1,2), "F": (0,1)}
xmin,xmax,ymin,ymax = 0, len(data)-1, 0, len(data[0])-1
row,col = 0,0
for i,p in enumerate(data):
    for j,q in enumerate(p):
        if q=="S":
            row,col = i,j
adj = lambda x,y,i: (x+dir_to_coord[i%4][0], y+dir_to_coord[i%4][1])
for istart in range(4):
    xstart,ystart = adj(row, col, istart)
    if (istart+2)%4 in transform[data[xstart][ystart]]:
        break
s1 = 1
x,y,i = xstart, ystart, istart
while x!=row or y!=col:
    i = [a for a in transform[data[x][y]] if a!=(i+2)%4][0]
    x,y = adj(x, y, i)
    s1+=1
print(f"1) {s1//2}")

def expand(side, pipe):
    fields = set()
    border = False
    for fx, fy in side-pipe:
        new = [(fx,fy)]
        while len(new)>0:
            x,y = new.pop()
            if (x,y) in pipe or (x,y) in fields: continue
            if x<xmin or x>xmax or y<ymin or y>ymax:
                border = True
                continue
            if (x,y) not in fields and (x,y) not in pipe: fields.add((x,y))
            for p,q in [(x+i,y+j) for i,j in dir_to_coord.values()]:
                if (p,q) not in fields and (p,q) not in pipe and (p,q) not in new: new.append((p,q))
    return fields, border

right, left, pipe = set(), set(), set()
x,y,i = xstart, ystart, istart
while x!=row or y!=col:
    right.add(adj(x,y,i+1)), left.add(adj(x,y,i-1)), pipe.add((x,y))
    i = [a for a in transform[data[x][y]] if a!=(i+2)%4][0]
    right.add(adj(x,y,i+1)), left.add(adj(x,y,i-1))
    x,y = x+dir_to_coord[i][0], y+dir_to_coord[i][1]

pipe.add((row,col))
fields_left, f1 = expand(left, pipe)
print(f"2) {len(fields_left) if not f1 else (xmax+1)*(ymax+1)-len(pipe.union(fields_left))}")
print(f"time: {time.time() - start_time}s")