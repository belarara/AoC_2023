import time
start_time = time.time()

with open("inputs/day_21.txt", "r") as f:
    data = [l for l in f.read().split("\n") if len(l)>0]

d = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}
next = lambda x,y: [(x+dx, y+dy) for dx,dy in d.values()]
valid = lambda ar,x,y: x>=0 and x<len(ar) and y>=0 and y<len(ar[0])

ds = [[a!="#" for a in line] for line in data]
lookup = {}
for x in range(len(data)):
    for y in range(len(data[0])):
        lookup[(x,y)] = set((nx,ny) for nx,ny in next(x,y) if valid(ds, nx, ny) and ds[nx][ny])

def get_reachable(starts,end=200):
    reachable = {0:starts}
    for i in range(1,end+1):
        reachable[i] = set()
        for x,y in reachable[i-1]:
            for o in lookup[(x,y)]:
                reachable[i].add(o)
    return reachable

xmax,ymax = len(ds), len(ds[0])
center = (xmax//2,ymax//2)
print(f"1) {len(get_reachable({center}, 64)[64])}")

steps = 26501365
sq_radius = (steps-xmax) // xmax
tips = [(xmax//2,0),(xmax//2,ymax-1),(0,ymax//2),(xmax-1,ymax//2)]
corners = [(0,0),(0,ymax-1),(xmax-1,0),(xmax-1,ymax-1)]

sq_even_row, sq_odd_row = sq_radius//2+1, sq_radius//2
sq_radius_half = sq_radius//2
sq_odd = 1 + 4*sq_odd_row*(sq_odd_row+1) # (1 center square) + (gauss sum * 8)
sq_even = 4*sq_even_row*(sq_even_row+1) - 4*sq_even_row # (gauss sum * 8) - (4*n because start at 4)
# full squares
r = get_reachable({center}, xmax+1)
even_max, odd_max = len(r[xmax+1]), len(r[xmax])
full_sq_sum = even_max*sq_even + odd_max*sq_odd
# tips
tips_length = steps - sq_radius*xmax - xmax//2 - 1
tips_sum = sum([len(get_reachable({s}, tips_length)[tips_length]) for s in tips])
# corners
high, low = 3*xmax//2 - 1, xmax//2 - 1
corners_reach = [get_reachable({s}, max(low,high)) for s in corners]
low_sum = sum([len(r[low]) for r in corners_reach]) * (sq_radius+1)
high_sum = sum([len(r[high]) for r in corners_reach]) * sq_radius

print(f"2) {full_sq_sum + tips_sum + low_sum + high_sum}")
print(f"time: {time.time() - start_time}s")