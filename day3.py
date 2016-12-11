import operator

with open(__file__[:-2]+"txt", "r") as f:
    lines = map(str.strip, f.readlines())

trips = map(lambda x:map(int, x.split()), lines)

trips = reduce(operator.add, zip(*trips))

trips = zip(*([iter(trips)] * 3))

trips = [sorted(x) for x in trips]

print sum([1 if a+b > c else 0 for (a, b, c) in trips])
