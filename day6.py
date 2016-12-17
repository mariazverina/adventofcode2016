from collections import Counter

with open(__file__[:-2]+"txt", "r") as f:
    lines = list(map(str.strip, f.readlines()))

print(''.join([Counter(x).most_common(1)[0][0] for x in zip(*lines)]))
print(''.join([Counter(x).most_common()[-1][0][0] for x in zip(*lines)]))