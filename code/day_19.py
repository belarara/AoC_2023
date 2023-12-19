import time
start_time = time.time()

with open("inputs/day_19.txt", "r") as f:
    data = f.read()

def gen_flow(flow):
    label, interior = flow[:-1].split("{")
    rules = interior.split(",")
    tups = []
    for rule in rules[:-1]:
        ch, sym = rule[0], True if rule[1]==">" else False
        val, dest = rule[2:].split(":")
        tups.append((ch, None if sym else int(val), None if not sym else int(val), dest))
    tups.append(rules[-1])
    return label, tups

flows,parts = data.split("\n\n")
flows = {l:t for l,t in [gen_flow(flow) for flow in flows.split("\n")]}
parts = [{"x": int(x[2:]), "m": int(m[2:]), "a": int(a[2:]), "s":int(s[2:])}
         for x,m,a,s in [line[1:-1].split(",")
         for line in parts.split("\n") if line.startswith("{")]]
labels = []
for p in parts:
    current_label = "in"
    while current_label in flows:
        change = False
        for sb, low, high, dest in flows[current_label][:-1]:
            if (low is not None and p[sb]<low) or (high is not None and p[sb]>high):
                current_label, change = dest, True
                break
        if not change:
            current_label = flows[current_label][-1]
    labels.append(current_label)

print(f"1) {sum([sum(parts[i].values()) for i,e in enumerate(labels) if e=="A"])}")

real = lambda x1,x2,x3,x4,x5,x6,x7,x8: x1<=x2 and x3<=x4 and x5<=x6 and x7<=x8
ls, A = [("in", (1,4000,1,4000,1,4000,1,4000))], []
while len(ls)>0:
    label, values = ls.pop(-1)
    if label=="R": continue
    if label=="A":
        A.append(values)
        continue
    values = list(values)
    rest = True
    for sb, low, high, dest in flows[label][:-1]:
        index = "xmas".index(sb)*2
        if (low is not None) and values[index]<low:
            ls.append((dest, tuple(e if i!=index+1 else low-1 for i,e in enumerate(values))))
            values[index] = low
        if (high is not None) and values[index+1]>high:
            ls.append((dest, tuple(e if i!=index else high+1 for i,e in enumerate(values))))
            values[index+1] = high
        if not real(*values):
            rest = False
            break
    if rest:
        ls.append((flows[label][-1], tuple(values)))

print(f"2) {sum([(x1-x+1)*(m1-m+1)*(a1-a+1)*(s1-s+1) for x,x1,m,m1,a,a1,s,s1 in A])}")
print(f"time: {time.time() - start_time}s")