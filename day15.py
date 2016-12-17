import re

with open(__file__[:-2]+"txt", "r") as f:
    lines = list(map(str.strip, f.readlines()))

lines = [list(map(int, re.match(r'Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).', s).groups())) for s in lines]


print(lines)

eqns =  [((a_b_c[0]+a_b_c[2])%a_b_c[1], a_b_c[1]) for a_b_c in lines]
eqns.append((7, 11))

print(eqns)

i = 0
while True:
    if all([(i + n) % m == 0 for (n,m) in eqns]):
        print(i)
        break
    i += 1

