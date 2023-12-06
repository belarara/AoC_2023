import time, re, functools, numpy
start_time = time.time()

with open("inputs/day_06.txt", "r") as f:
    data = f.read().split("\n")

limits, records = [int(a) for a in re.findall("(\d+)", data[0])], [int(a) for a in re.findall("(\d+)", data[1])]
print(f"1) {functools.reduce(lambda x,y: x*y, [len([i*(lim-i) for i in range(lim) if i*(lim-i)>records[curr]]) for curr, lim in enumerate(limits)])}")

lim, record = [int(a) for a in re.findall("(\d+)", data[0].replace(" ", "")+data[1].replace(" ", ""))]
print(f"2) {int(abs(numpy.diff(numpy.ceil(numpy.roots([-1, lim, -record]))))[0])}")
print(f"time: {time.time() - start_time}s")