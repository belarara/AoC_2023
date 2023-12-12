import time, re
start_time = time.time()

with open("inputs/day_12.txt", "r") as f:
    data = [l for l in f.read().split("\n") if len(l)>0]

def remain_possible(arrange, groups, expect=None):
    if (arrange, groups, expect) in done: return done[(arrange, groups, expect)]
    if len(groups)==0: return 1 if "#" not in arrange else 0
    if len(arrange)<sum(groups)+len(groups)-1: return 0
    count = 0
    if arrange[0] in "#?" and expect != "." and "." not in arrange[:groups[0]]:
        count += remain_possible(arrange[groups[0]:], groups[1:], ".")
    if arrange[0] in ".?":
        count += remain_possible(arrange[1:], groups)
    done[(arrange, groups, expect)] = count
    return count

done = {}
s1,s2 = 0,0
for i,line in enumerate(data):
    arrange, numbers = line.split(" ")
    numbers = tuple(int(a) for a in re.findall(r"(\d+)", numbers))
    s1 += remain_possible(arrange, numbers)
    s2 += remain_possible("?".join([arrange]*5), numbers*5)

print(f"1) {s1}")
print(f"2) {s2}")
print(f"time: {time.time() - start_time}s")