import time, re
start_time = time.time()

with open("inputs/day_05.txt", "r") as f:
    data = f.read()

seeds = [int(a) for a in re.findall("(\d+)", data.split("\n")[0])]
keys = re.findall("([a-z]+)-to-([a-z]+) map", data)
conversions = data.split("\n", 2)[-1].split("\n\n")
dct = {}
for i, key in enumerate(keys):
    dct[key] = {"dest":[], "source":[], "range":[]}
    for line in [y for y in conversions[i].split("\n")[1:] if y!=""]:
        a,b,c = [int(x) for x in line.split(" ")]
        dct[key]["dest"].append(a), dct[key]["source"].append(b), dct[key]["range"].append(c)

conv_seeds = []
for s in seeds:
    c=s
    for key in keys:
        for i, e in enumerate(dct[key]["dest"]):
            if c >= dct[key]["source"][i] and c < dct[key]["source"][i] + dct[key]["range"][i]:
                c = (c-dct[key]["source"][i])+dct[key]["dest"][i]
                break
    conv_seeds.append(c)
print(f"1) {min(conv_seeds)}")

seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_ranges.append((seeds[i], seeds[i]+seeds[i+1]-1))
for key in keys:
    new_range = []
    while len(seed_ranges)>0:
        seed_min, seed_max = seed_ranges.pop()
        ol = False
        for j, source in enumerate(dct[key]["source"]):
            source_min, source_max = source, source + dct[key]["range"][j]-1
            overlap_min, overlap_max = max(seed_min, source_min), min(seed_max, source_max)
            if overlap_min <= overlap_max:
                ol = True
                if seed_min<overlap_min: seed_ranges.append((seed_min, overlap_min-1))
                if overlap_max<seed_max: seed_ranges.append((overlap_max+1, seed_max))
                new_range.append((overlap_min-source+dct[key]["dest"][j], overlap_max-source+dct[key]["dest"][j]))
                break
        if not ol: new_range.append((seed_min,seed_max))
    seed_ranges = new_range

print(f"2) {min([a for a,_ in seed_ranges])}")
print(f"time: {time.time() - start_time}s")