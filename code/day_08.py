import time, re, math
start_time = time.time()

with open("inputs/day_08.txt", "r") as f:
    data = f.readlines()

instruction = data[0][:-1]
choice = {"L":0, "R":1}
dct = {}
for e in data[2:]:
    if len(e)>1:
        node, r, l = re.findall(r"([A-Z0-9]{3})", e)
        dct[node] = (r, l)

def new_node(current, choice, dct, full_inst, counter):
    return dct[current][choice[full_inst[counter%len(full_inst)]]]

def find_z(node):
    c = 0
    while node[-1] != "Z":
        node = new_node(node, choice, dct, instruction, c)
        c+=1
    return c

print(f"1) {find_z('AAA')}")
print(f"2) {math.lcm(*[find_z(a) for a in dct if a.endswith("A")])}")
print(f"time: {time.time() - start_time}s")