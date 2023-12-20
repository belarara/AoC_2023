import time, math, functools
from collections import deque
start_time = time.time()

with open("inputs/day_20.txt", "r") as f:
    data = [l for l in f.read().split("\n") if len(l)>0]

mods, ins = {}, set()
for line in ["button -> broadcaster", "output -> ", "rx -> "]+data:
    label, outputs = line.split(" -> ")
    name = label if label[0] not in "%&" else label[1:]
    outputs = {o.strip() for o in outputs.split(",") if o!=""}
    ins = ins.union(outputs)
    mods[name] = {
        "type": (0 if label[0] not in "%&" else (1 if label[0]=="%" else 2)),
        "in": {},
        "out": outputs,
        "state": False
    }
for k,v in mods.items():
    for out in v["out"]:
        mods[out]["in"][k] = False
    
def press_button(mods, low, high, rec=None, cycle={}, n=0):
    signals = deque([("button", "broadcaster", False)])
    while len(signals)>0:
        inp, label, pulse = signals.popleft()
        high += pulse
        low += not pulse
        outp = pulse
        if label == rec and pulse:
            if inp not in cycle:
                cycle[inp] = n
        if mods[label]["type"]==1:
            if not pulse:
                mods[label]["state"] = not mods[label]["state"]
                outp = mods[label]["state"]
            else:
                continue
        if mods[label]["type"]==2:
            mods[label]["in"][inp] = pulse
            outp = not all(mods[label]["in"].values())
        for out in mods[label]["out"]:
            signals.append((label, out, outp))
    return mods, low, high

low, high = 0, 0
for i in range(1000):
    mods, low, high = press_button(mods, low, high)
print(f"1) {low*high}")

for m,v in mods.items():
    v["state"] = False
    for i in v["in"]:
        v["in"][i] = False

outp = [label for label,v in mods.items() if "rx" in v["out"]][0]
inputs = {k for k,v in mods.items() if outp in v["out"]}
c, cycle = 0, {}
while len(inputs - set(cycle))>0:
    c += 1
    mods, _, _ = press_button(mods, 0, 0, outp, cycle, c)
print(f"2) {functools.reduce(lambda x,y:x*y, cycle.values())*math.gcd(*cycle.values())}")
print(f"time: {time.time() - start_time}s")