import time, numpy
start_time = time.time()

with open("inputs/day_07.txt", "r") as f:
    data = f.read().split("\n")

def val_ret(ct):
    if 5 in ct.values(): return 20
    if 4 in ct.values(): return 19
    if 3 in ct.values() and 2 in ct.values(): return 18
    if 3 in ct.values(): return 17
    if len([a for a in ct.values() if a>1])>1: return 16
    if 2 in ct.values(): return 15
    return 14

def val(hand):
    return val_ret({x:hand.count(x) for x in order})

def val2(hand):
    ct = {x:hand.count(x) for x in order if x!="J"}
    m = max(ct, key=ct.get)
    ct[m] += hand.count("J")
    return val_ret(ct)

order, order2 = "23456789TJQKA", "J23456789TQKA"
hands, hands2 = [], []
for i, line in enumerate(data):
    if line != "":
        hand, bet = line.split(" ")
        hands.append((val(hand),*tuple(order.index(a) for a in hand), int(bet)))
        hands2.append((val2(hand),*tuple(order2.index(a) for a in hand), int(bet)))

winnings = lambda ls: sum([a[-1]*(i+1) for i,a in enumerate(sorted(ls, key=lambda x: x[:-1]))])
print(f"1) {winnings(hands)}")
print(f"2) {winnings(hands2)}")
print(f"time: {time.time() - start_time}s")