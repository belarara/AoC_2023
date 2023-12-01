with open("inputs/day_01", "r") as f:
    data = f.read()

ls = []
for l in data.split("\n"):
    d = [int(a) for a in l if a.isdigit()]
    if len(d)>0:
        ls.append(10*d[0]+d[-1])
out = sum(ls)

dg = {"one":1, "two":2, "thr":3, "fou":4, "fiv":5, "six":6, "sev":7, "eig":8, "nin":9}
fdg = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

ls2 = []
for l in data.split("\n"):
    d = []
    for pos,v in enumerate(l):
        if v.isdigit():
            d.append(int(v))
        elif any((l[pos:pos+i] in fdg) for i in [3,4,5]):
            d.append(dg[l[pos:pos+3]])
    ls2.append(d[0]*10+d[-1])
out2 = sum(ls2)

print(f"1) {out}")
print(f"2) {out2}")