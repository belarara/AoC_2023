import time, re
start_time = time.time()

with open("inputs/day_04.txt", "r") as f:
    data = f.read()
data = [a for a in data.split("\n") if len(a)>0]

s, dct = 0, {}
for line in data:
    game, winning, current = line.replace("|", ":").split(":")
    wins = re.findall("(\d+)", winning)
    nums = [int(a) for a in re.findall("(\d+)", current) if a in wins]
    if len(nums)>0:
        s += 1 << (len(nums)-1)
    dct[int(game.split(" ")[-1])] = len(nums)
print(f"1) {s}")

cards = {a:1 for a in dct}
for a in sorted(dct):
    for i in range(1,dct[a]+1):
        cards[a+i] += cards[a]

print(f"2) {sum(cards.values())}")
print(f"time: {time.time() - start_time}s")