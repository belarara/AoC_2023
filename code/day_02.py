import time
start_time = time.time()

with open("inputs/day_02", "r") as f:
    data = f.read()

dc = {}
for l in data.split("\n"):
    if l=="": break
    game, sets = l.split(":")
    _, game = game.split(" ")
    dc[game] = {}
    if len(sets) < 3: continue
    sets = sets.split(";")
    for s in sets:
        colors = s.split(",")
        for n_col in colors:
            if n_col.startswith(" "): n_col = n_col[1:]
            n, col = n_col.split(" ")
            n = int(n)
            if col not in dc[game] or n > dc[game][col]:
                dc[game][col] = n

possible, s = {"red": 12, "green": 13, "blue": 14}, 0
for g, d in dc.items():
    p = True
    for k,v in possible.items():
        if k in d and d[k] > possible[k]:
            p = False
    if p:
        s += int(g)
print(f"1) {s}")

s2 = 0
for d in dc.values():
    s2 += (0 if "red" not in d else d["red"]) * (0 if "blue" not in d else d["blue"]) * (0 if "green" not in d else d["green"])
print(f"2) {s2}")
print(f"time: {time.time() - start_time}s")