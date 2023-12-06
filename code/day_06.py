import time, re, functools, numpy
start_time = time.time()

with open("inputs/day_06.txt", "r") as f:
    data = f.read().split("\n")

limits, records = [re.findall("(\d+)", data[i]) for i in range(2)]
better_races = lambda lim, record: int(abs(numpy.diff(numpy.ceil(numpy.roots([-1, lim, -record]))))[0])
print(f"1) {numpy.prod([better_races(int(lim), int(rec)) for lim, rec in zip(limits, records)])}")

print(f"2) {better_races(*[int(functools.reduce(lambda x,y: x+y, a)) for a in (limits, records)])}")
print(f"time: {time.time() - start_time}s")