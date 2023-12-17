import time, heapq
start_time = time.time()

with open("inputs/day_17.txt", "r") as f:
    data = [[int(a) for a in line] for line in f.read().split("\n") if len(line)>0]

dx,dy = {0:-1,1:0,2:1,3:0}, {0:0,1:1,2:0,3:-1}
valid = lambda ar, x, y: x>=0 and x<len(ar) and y>=0 and y<len(ar[0])

def min_heat_loss(data, starts, min_v, max_v):
    heapq.heapify(starts)
    visited = set()
    while len(starts)>0:
        value, x, y, d, c = heapq.heappop(starts)
        if (x, y, d, c) in visited: continue
        visited.add((x, y, d, c))
        if x==len(data)-1 and y==len(data[0])-1 and c>=min_v: break
        nx,ny = x+dx[d], y+dy[d]
        if c < max_v and valid(data, nx, ny):
            heapq.heappush(starts, (value+data[nx][ny], nx, ny, d, c+1))
        if c >= min_v:
            for i in [(d+1)%4, (d+3)%4]:
                nx,ny = x+dx[i], y+dy[i]
                if valid(data, nx, ny):
                    heapq.heappush(starts, (value+data[nx][ny], nx, ny, i, 1))
    return value

print(f"1) {min_heat_loss(data, [(0,0,0,1,0)], 0, 3)}")
print(f"2) {min_heat_loss(data, [(0,0,0,1,0),(0,0,0,2,0)], 4, 10)}")
print(f"time: {time.time() - start_time}s")