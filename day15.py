import re

with open(__file__[:-2]+"txt", "r") as f:
    lines = map(str.strip, f.readlines())

lines = map(lambda s:map(int, re.match(r'Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).', s).groups()), lines)


print lines

eqns =  map(lambda (a,b,c):((a+c)%b, b), lines)
eqns.append((7, 11))

print eqns

i = 0
while True:
    if all([(i + n) % m == 0 for (n,m) in eqns]):
        print i
        break
    i += 1

