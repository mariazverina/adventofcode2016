from collections import Counter

with open(__file__[:-2]+"txt", "r") as f:
    lines = map(str.strip, f.readlines())

print ''.join(map(lambda x:Counter(x).most_common(1)[0][0], zip(*lines)))
print ''.join(map(lambda x:Counter(x).most_common()[-1][0][0], zip(*lines)))