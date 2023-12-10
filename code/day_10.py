import time
start_time = time.time()

with open("inputs/day_10.txt", "r") as f:
    data = [l for l in f.read().split("\n") if len(l)>0]

dir_to_coord = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
transform = {"|": (1,3), "-": (0,2), "L": (0,3), "J": (2,3), "7": (1,2), "F": (0,1)}
xmin,xmax,ymin,ymax = 0, len(data)-1, 0, len(data[0])-1
print("MIN/MAX", xmin,xmax,ymin,ymax)
row,col = 0,0
for i,p in enumerate(data):
    for j,q in enumerate(p):
        if q=="S":
            row,col = i,j
for i in range(4):
    x,y = row+dir_to_coord[i][0], col+dir_to_coord[i][1]
    if (i+2)%4 in transform[data[x][y]]:
        break
s1 = 1
right, left, pipe = set(), set(), set()
dirs = []
while x!=row or y!=col:
    right.add((x+dir_to_coord[(i-1)%4][0], y+dir_to_coord[(i-1)%4][1]))
    left.add((x+dir_to_coord[(i+1)%4][0], y+dir_to_coord[(i+1)%4][1]))
    pipe.add((x,y))
    i = (i+2)%4
    dirs.append((x,y,i))
    symbol = data[x][y]
    i = [a for a in transform[symbol] if a!=i][0]
    right.add((x+dir_to_coord[(i-1)%4][0], y+dir_to_coord[(i-1)%4][1]))
    left.add((x+dir_to_coord[(i+1)%4][0], y+dir_to_coord[(i+1)%4][1]))
    x,y = x+dir_to_coord[i][0], y+dir_to_coord[i][1]
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

pipe.add((row,col))
fields_left, f1 = expand(left, pipe)
fields_right, f2 = expand(right, pipe)
print(f"2) {len(fields_left if not f1 else fields_right)}")
print(f"time: {time.time() - start_time}s")

for x in range(xmax):
    for y in range(ymax):
        line = list(data[x])
        line[y] = "@"
        data[x] = "".join(line)

for x,y in fields_left:
    line = list(data[x])
    line[y] = "O"
    data[x] = "".join(line)

for x,y in fields_right:
    line = list(data[x])
    line[y] = "@"
    data[x] = "".join(line)

for x,y in (pipe):
    line = list(data[x])
    line[y] = "#"
    data[x] = "".join(line)

for x,y,i in dirs:
    line = list(data[x])
    line[y] = ">v<^"[i]
    data[x] = "".join(line)

for l in data:
   print(l)