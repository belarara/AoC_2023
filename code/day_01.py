with open("inputs/day_01.txt", "r") as f:
    data = f.read()

fdg = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
def find_first_digit(s, rng, only_digit=True):
    for i in rng:
        if s[i].isdigit():
            return int(s[i])
        elif not only_digit:
            for k,v in fdg.items():
                if s[i:].startswith(k):
                    return v

# part 1
print(f"1) {sum([find_first_digit(l, range(len(l)))*10 + find_first_digit(l, range(len(l)-1, -1, -1)) for l in data.split("\n")])}")

# part 2
print(f"2) {sum([find_first_digit(l, range(len(l)), False)*10 + find_first_digit(l, range(len(l)-1, -1, -1), False) for l in data.split("\n")])}")