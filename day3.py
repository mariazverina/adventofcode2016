import operator
from functools import reduce

with open(__file__[:-2]+"txt", "r") as f:
    lines = list(map(str.strip, f.readlines()))

trips = [list(map(int, x.split())) for x in lines]

trips = reduce(operator.add, list(zip(*trips)))

trips = list(zip(*([iter(trips)] * 3)))

trips = [sorted(x) for x in trips]

print(sum([1 if a+b > c else 0 for (a, b, c) in trips]))
