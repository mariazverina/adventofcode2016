from collections import Counter
import re
import string

with open(__file__[:-2]+"txt", "r") as f:
    lines = list(map(str.strip, f.readlines()))

print(lines)

s = 0

alphabet = string.ascii_lowercase
rot_dicts = []
for i in range(26):
    rot_dicts.append(string.maketrans(alphabet + "-", alphabet[i:] + alphabet[:i] + " "))

for line in lines:
    name, id, checksum = re.match(r'(\D+)-(\d+)\[(.*?)\]', line).groups()
    name = re.sub('-', '', name)

    k = ''.join(zip(*sorted(Counter(name).most_common(), key=lambda a_b:(-a_b[1],a_b[0]))[:5])[0])
    if k == checksum:

        print(string.translate(line, rot_dicts[int(id) % 26]), line, k)

        s += int(id)

print(s)






