import re
with open(__file__[:-2]+"txt", "r") as f:
    lines = list(map(str.strip, f.readlines()))

print(lines[:6])
lines = lines[2:]
matcher = re.compile(r'/dev/grid/node-x(\d+)-y(\d+)\s+\d+T\s+(\d+)T\s+(\d+)T\s+\d+%')
lines = [list(map(int, matcher.match(line).groups())) for line in lines]

print(list(lines)[:6])

# part 1
n_pairs = 0
for (x, y, used, avail) in lines:
    n_pairs += sum([1 for (nx, ny, nused, navail) in lines if navail >= used and not(nx == x and ny == y) and used > 0])

print(n_pairs)

# part 2
maze = []
empty_node = [n for n in lines if n[2] == 0][0]
space = empty_node[-1]
print(empty_node)

coords = [tuple(n[:2]) for n in lines]
contents = ['.' if n[2] <= space else 'X' for n in lines]
cells = dict(zip(coords, contents))

for y in range(30):
    for x in range(33):
        print(cells[x,y], sep="", end="")
    print()

# solve manually based on puzzle layout
# 15,29 -> 3,29 -> 3,0 -> 32,0 (moving space) = 12 + 29 29 = 70
# Need to move target cell from 31,0 to 0,0. Each move takes 5 shuffles = 31 * 5 = 155
# 155 + 70 = 225