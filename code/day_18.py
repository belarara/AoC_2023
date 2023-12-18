import time
start_time = time.time()

with open("inputs/day_18.txt", "r") as f:
    data = [line.split(" ") for line in f.read().split("\n") if len(line)>0]

dr = {"U":0,"R":1,"D":2,"L":3}
dx,dy = {0:-1,1:0,2:1,3:0}, {0:0,1:1,2:0,3:-1}

def get_trench(data, part):
    trench = []
    x,y,o = 0,0,0
    for p,q,rgb in data:
        trench.append((x,y))
        d,c = dr[p], int(q)
        if part: d,c = (int(rgb[-2])+1)%4, int(rgb[2:-2], 16)
        x,y = x+c*dx[d], y+c*dy[d]
        o += c
    return trench, o

trench,o = get_trench(data, False)
plusminus_area = abs(sum([trench[i-1][0]*(trench[i][1]-trench[i-2][1]) for i in range(0,len(trench),2)]))
print(f"1) {plusminus_area + o//2 + 1}")

trench,o = get_trench(data, True)
plusminus_area = abs(sum([trench[i-1][0]*(trench[i][1]-trench[i-2][1]) for i in range(0,len(trench),2)]))
print(f"2) {plusminus_area + o//2 + 1}")
print(f"time: {time.time() - start_time}s")