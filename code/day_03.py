import time
start_time = time.time()

with open("inputs/day_03.txt", "r") as f:
    data = f.read()
data = [a for a in data.split("\n") if len(a)>0]

def get_index(string_map, line, pos):
    if line >= 0 and line < len(string_map) and pos >= 0 and pos < len(string_map[0]):
        return string_map[line][pos]
    
def get_adjacent(x,y):
    return [(x+a, y+b) for a,b in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]]

def get_number(indexes):
    return int("".join([get_index(data, a, b) for a,b in indexes]))

counter, dct, catch_number = 0, {}, False
for i, row in enumerate(data):
    if catch_number:
        counter += 1
        catch_number = False
    for j, letter in enumerate(row):
        if letter.isdigit():
            if not catch_number:
                catch_number = True
                dct[counter] = [(i, j)]
            else:
                dct[counter].append((i,j))
        if catch_number and not letter.isdigit():
            counter += 1
            catch_number = False

s = 0
for k,v in dct.items():
    adj = {(x,y) for a,b in v for x,y in get_adjacent(a,b) if (x,y) not in v}
    symbols = ""
    for x,y in adj:
        ns = get_index(data, x, y)
        if ns is not None and ns != ".": symbols += ns
    if len(symbols) > 0:
        s += get_number(v)
print(f"1) {s}")

s2, gears = 0, {}
for k,v in dct.items():
    adj = {(x,y) for a,b in v for x,y in get_adjacent(a,b) if (x,y) not in v}
    for x,y in adj:
        if get_index(data, x, y) == "*":
            if (x,y) not in gears:
                gears[(x,y)] = [get_number(v)]
            else:
                gears[(x,y)].append(get_number(v))

for v in gears.values():
    if len(v)==2:
        s2 += v[0] * v[1]

print(f"2) {s2}")
print(f"time: {time.time() - start_time}s")