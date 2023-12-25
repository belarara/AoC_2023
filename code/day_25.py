import time
start_time = time.time()

with open("inputs/day_25.txt", "r", encoding="UTF8") as f:
    data = [l for l in f.read().split("\n") if len(l)>0]

def get_vertices(edges):
    return list({v for v,_ in edges}.union({v for _,v in edges}))

def create_dct_from_edges(edges):
    cn = {a:set() for a in get_vertices(edges)}
    for e1,e2 in edges:
        cn[e1].add(e2)
        cn[e2].add(e1)
    return cn

def path(edges, start, end):
    cn = create_dct_from_edges(edges)
    q = [(start,[start])]
    s = set()
    while len(q)>0:
        c,p = q.pop(0)
        if c == end:
            return p
        if c in s:
            continue
        s.add(c)
        for n in cn[c]:
            if n not in p:
                q.append((n,p+[n]))
    return None

E = set()
for line in data:
    v1,es = line.split(": ")
    for v2 in es.split(" "):
        E.add((v1,v2))
V = get_vertices(E)

# find two vertices connected by at most 2 paths
brk = False
v1 = V[0]
for v2 in V[1:]:
    count = 0
    used = set()
    while count<4 and not brk:
        count += 1
        pth = path(E-used, v1, v2)
        if pth is not None:
            for i in range(len(pth)-1):
                used.add((pth[i],pth[i+1]))
                used.add((pth[i+1],pth[i]))
        else: brk = True
    if brk:
        break

# find components of graph with removed used edges
cons = create_dct_from_edges(E-used)
seen = set()
ls = []
for v in V:
    if v not in seen:
        ls.append([])
        queue = [v]
        while len(queue)>0:
            nxt = queue.pop(0)
            if nxt not in seen:
                seen.add(nxt)
                ls[-1].append(nxt)
                for e in cons[nxt]:
                    if e not in seen:
                        queue.append(e)
print(f"1) {len(ls[0])*len(ls[1])}")
print(f"time: {time.time() - start_time}s")
