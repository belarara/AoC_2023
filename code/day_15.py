import time
start_time = time.time()

with open("inputs/day_15.txt", "r") as f:
    data = f.read().strip("\n")

def my_hash(s):
    v = 0
    for c in s:
        v += ord(c)
        v *= 17
        v %= 256
    return v

print(f"1) {sum([my_hash(a) for a in data.split(",")])}")

boxes = [list() for _ in range(256)]
for step in data.split(","):
    label, lens = step.replace("-","=").split("=")
    box = my_hash(label)
    if lens != "":
        replace = False
        for i, (lb,ln) in enumerate(boxes[box]):
            if label == lb:
                replace = True
                boxes[box][i] = (label, int(lens))
                break
        if not replace:
            boxes[box].append((label,int(lens)))
    else:
        ind = [i for i,(e1,_) in enumerate(boxes[box]) if e1==label]
        if len(ind)>0:
            boxes[box].pop(ind[0])

print(f"2) {sum([sum([(i+1)*(slot+1)*focal for slot, (_, focal) in enumerate(box)]) for i,box in enumerate(boxes)])}")
print(f"time: {time.time() - start_time}s")